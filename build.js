/**
 * Time Series Analysis and Forecasting — course site builder.
 *
 * Built on the NEU FDA course site template:
 *   https://github.com/nghianguyen7171/neu_fda_coursesite
 *
 * Notes specific to this course:
 *
 *  1. Output goes to the repository root, not docs/. slides/ is 49 MB and
 *     Topic/ is 27 MB; copying them into docs/ would nearly double the repo.
 *     deploy.sh publishes a *selected* copy to the gh-pages branch instead, so
 *     the repo root stops being the web root and we control what is published.
 *
 *  2. Because OUT is the repo root, this script NEVER removes OUT. It writes
 *     only the files listed in GENERATED. Deleting the output directory here
 *     would delete the repository.
 *
 *  3. The 15 topic pages are generated from Topic/<n>.<slug>/README.md plus the
 *     metadata in src/data/topics.yml. They used to be 15 hand-maintained HTML
 *     files that each had to be edited when the layout changed.
 */

const fs = require('fs-extra');
const path = require('path');
const Handlebars = require('handlebars');
const yaml = require('js-yaml');
const { marked } = require('marked');
const sass = require('sass');
const { globSync } = require('glob');

const ROOT = __dirname;
const SRC = path.join(ROOT, 'src');

const WITH_SOLUTIONS = process.env.SOLUTIONS === '1';

const log = (...a) => console.log(...a);
const fail = (msg) => {
  console.error(`\nBuild failed: ${msg}\n`);
  process.exit(1);
};

// ---------------------------------------------------------------- data

function loadData() {
  const dir = path.join(SRC, 'data');
  const data = {};
  for (const file of fs.readdirSync(dir).filter((f) => /\.ya?ml$/.test(f))) {
    const key = path.basename(file, path.extname(file)).replace(/-([a-z])/g, (_, c) => c.toUpperCase());
    data[key] = yaml.load(fs.readFileSync(path.join(dir, file), 'utf8'));
  }
  return data;
}

function validateCourse(course) {
  if (!course) fail('src/data/course.yml is missing or empty.');

  const items = (course.assessment && course.assessment.items) || [];
  if (!items.length) fail('course.yml defines no assessment items.');

  const total = items.reduce((sum, item) => {
    const n = parseFloat(String(item.weight).replace('%', ''));
    if (Number.isNaN(n)) fail(`assessment item "${item.name}" has an unparseable weight: ${item.weight}`);
    return sum + n;
  }, 0);
  if (Math.abs(total - 100) > 0.01) {
    fail(
      `assessment weights sum to ${total}%, not 100%.\n` +
        items.map((i) => `    ${String(i.weight).padStart(5)}  ${i.name}`).join('\n')
    );
  }

  const objectives = new Set((course.objectives || []).map((o) => o.id));
  for (const clo of course.learning_outcomes || []) {
    if (!objectives.has(clo.objective)) {
      fail(`${clo.id} maps to objective "${clo.objective}", which is not defined in course.yml.`);
    }
  }

  log(`  validated: ${items.length} assessment items sum to 100%, ${(course.learning_outcomes || []).length} CLOs mapped`);
}

/** Each topic must have the README and image its page is built from. */
function validateTopics(topics) {
  const problems = [];
  for (const t of topics.topics || []) {
    const readme = path.join(ROOT, t.dir, 'README.md');
    if (!fs.existsSync(readme)) problems.push(`topic ${t.id}: missing ${t.dir}/README.md`);
    if (!fs.existsSync(path.join(ROOT, t.image))) problems.push(`topic ${t.id}: missing image ${t.image}`);
  }
  if (problems.length) fail(problems.join('\n    '));
  log(`  validated: ${topics.topics.length} topics have a README and an image`);
}

/**
 * Every local link in every generated page must resolve to a real file.
 * Every in-page "#anchor" must have a matching element.
 */
function validateLinks(pages) {
  const missing = [];
  const dead = [];

  // Handlebars escapes "&" to "&amp;" and "=" to "&#x3D;" inside attributes.
  // Browsers decode these, so the links work; the validator must decode too or
  // it will report slides/…"&amp;"….pdf as missing.
  const unescape = (s) =>
    s
      .replace(/&amp;/g, '&')
      .replace(/&#x3D;/g, '=')
      .replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>')
      .replace(/&quot;/g, '"')
      .replace(/&#x27;/g, "'");

  for (const [name, html] of Object.entries(pages)) {
    const ids = new Set([...html.matchAll(/id="([^"]+)"/g)].map((m) => m[1]));
    for (const m of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
      const raw = unescape(m[1]);
      if (/^(https?:)?\/\//.test(raw) || raw.startsWith('mailto:') || raw.startsWith('data:')) continue;
      if (raw.startsWith('#')) {
        const id = raw.slice(1);
        if (id && !ids.has(id)) dead.push(`${name} -> #${id}`);
        continue;
      }
      const [target, frag] = decodeURIComponent(raw).split('#');
      if (!target) continue;
      // Pages produced by this build count as existing: validation runs before
      // anything is written, so index.html may not be on disk yet. While here,
      // check cross-page anchors too ("index.html#assessment").
      if (Object.prototype.hasOwnProperty.call(pages, target)) {
        if (frag) {
          const targetIds = new Set([...pages[target].matchAll(/id="([^"]+)"/g)].map((x) => x[1]));
          if (!targetIds.has(frag)) dead.push(`${name} -> ${target}#${frag}`);
        }
        continue;
      }
      const ok =
        fs.existsSync(path.join(ROOT, target.normalize('NFC'))) ||
        fs.existsSync(path.join(ROOT, target.normalize('NFD')));
      if (!ok) missing.push(`${name} -> ${target}`);
    }
  }

  if (missing.length || dead.length) {
    let msg = '';
    if (missing.length) msg += `${missing.length} link(s) point at missing files:\n    ` + [...new Set(missing)].join('\n    ') + '\n';
    if (dead.length) msg += `${dead.length} dead in-page anchor(s):\n    ` + [...new Set(dead)].join('\n    ');
    fail(msg);
  }
  log('  validated: every local link resolves, every in-page anchor exists');
}

// ------------------------------------------------------- markdown + solutions

const SOLUTION_RE = /^::: *solution *$\n([\s\S]*?)^::: *$/gm;

function processSolutions(md) {
  if (!WITH_SOLUTIONS) return md.replace(SOLUTION_RE, '');
  return md.replace(
    SOLUTION_RE,
    (_, body) => `\n<div class="solution">\n<p class="solution-label">Solution</p>\n\n${body.trim()}\n\n</div>\n`
  );
}

// ---------------------------------------------------------------- templating

function registerHelpers() {
  // The site is served from …github.io/ts_course/ with the published tree as
  // the web root, so links stay relative. encodeURI handles the slide filenames,
  // which contain spaces, commas, ampersands and en-dashes.
  Handlebars.registerHelper('url', (p) => {
    if (!p) return './';
    if (/^(https?:)?\/\//.test(p) || p.startsWith('mailto:')) return p;
    return encodeURI(String(p).replace(/^\//, '').normalize('NFC'));
  });

  Handlebars.registerHelper('eq', (a, b) => a === b);
  Handlebars.registerHelper('concat', (...args) => args.slice(0, -1).join(''));
  Handlebars.registerHelper('year', () => new Date().getFullYear());
  Handlebars.registerHelper('md', (s) => new Handlebars.SafeString(marked.parse(String(s || ''))));
  Handlebars.registerHelper('mdInline', (s) => new Handlebars.SafeString(marked.parseInline(String(s || ''))));
  Handlebars.registerHelper('isReleased', (status) => (status || 'released') === 'released');
  Handlebars.registerHelper('statusLabel', (status) => ({ draft: 'Draft', tbd: 'TBD' }[status] || ''));

  // Bonus points follow difficulty, per the legend on the topics page:
  // Easy = none, Medium = +1, Hard = +1.5. A topic may override with `bonus:`.
  Handlebars.registerHelper('bonusFor', (topic) => {
    if (topic.bonus !== undefined) return topic.bonus;
    return { medium: '+1 Bonus Point', hard: '+1.5 Bonus Points' }[topic.level] || '';
  });
}

function registerPartials() {
  const dir = path.join(SRC, 'partials');
  for (const file of globSync('**/*.hbs', { cwd: dir })) {
    Handlebars.registerPartial(file.replace(/\.hbs$/, ''), fs.readFileSync(path.join(dir, file), 'utf8'));
  }
}

const tpl = (rel) => Handlebars.compile(fs.readFileSync(path.join(SRC, rel), 'utf8'));

// ---------------------------------------------------------------- main

function main() {
  log(`\nBuilding ${WITH_SOLUTIONS ? 'INSTRUCTOR (with solutions)' : 'PUBLIC'} site -> repository root\n`);

  const data = loadData();
  validateCourse(data.course);
  validateTopics(data.topics);

  registerHelpers();
  registerPartials();

  const ctx = { ...data, withSolutions: WITH_SOLUTIONS };

  const css = sass.compile(path.join(SRC, 'styles', 'main.scss'), { style: 'compressed' });
  fs.outputFileSync(path.join(ROOT, 'assets', 'css', 'main.css'), css.css);
  log('  styles: assets/css/main.css');

  const base = tpl('templates/base.hbs');
  const generated = {};

  generated['index.html'] = base({
    ...ctx,
    content: new Handlebars.SafeString(tpl('index.hbs')(ctx)),
    page: { nav: 'home', prefix: '' },
  });

  generated['topics.html'] = base({
    ...ctx,
    content: new Handlebars.SafeString(tpl('templates/topics-index.hbs')(ctx)),
    page: { title: 'Project Topics', nav: 'topics', prefix: 'index.html' },
  });

  const topicTpl = tpl('templates/topic.hbs');
  for (const t of data.topics.topics) {
    const md = fs.readFileSync(path.join(ROOT, t.dir, 'README.md'), 'utf8');
    // Drop the leading "# Topic N – Title" heading; the hero already shows it.
    const body = md.replace(/^#\s+.*\n/, '');
    const bodyHtml = new Handlebars.SafeString(marked.parse(processSolutions(body)));
    generated[`topic${t.id}.html`] = base({
      ...ctx,
      content: new Handlebars.SafeString(topicTpl({ ...ctx, topic: t, bodyHtml })),
      page: { title: `Topic ${t.id}: ${t.title}`, nav: 'topics', prefix: 'index.html' },
    });
  }

  validateLinks(generated);

  for (const [name, html] of Object.entries(generated)) {
    fs.outputFileSync(path.join(ROOT, name), html);
  }
  log(`  pages: index.html, topics.html, topic1..${data.topics.topics.length}.html`);

  if (WITH_SOLUTIONS) log('\n  NOTE: this build renders solution blocks. Do not publish.');
  log('\nDone.\n');
}

main();
