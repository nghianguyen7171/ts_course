# LaTeX Template Compilation Guide

## Quick Start

This template has been modified to compile locally without requiring Ghostscript.

### Basic Compilation

To compile the document, run:

```bash
pdflatex samplepaper.tex
```

**Important:** Run the command **twice** to resolve all cross-references correctly.

### Using BibTeX (Optional)

If you're using BibTeX for references:

```bash
pdflatex samplepaper.tex
bibtex samplepaper
pdflatex samplepaper.tex
pdflatex samplepaper.tex
```

## Adding Figures

The template supports multiple figure formats:

1. **PDF** (Recommended) - Works without additional software
2. **PNG/JPG** - Works without additional software  
3. **EPS** - Requires Ghostscript installation

### Steps to Add a Figure:

1. Place your figure file in the same directory as `samplepaper.tex`
2. Open `samplepaper.tex` and find the figure section
3. Uncomment one of the figure blocks (Option 1, 2, or 3)
4. Replace `myfigure.pdf` with your actual filename
5. Uncomment the figure reference in the text: `(see Fig.~\ref{fig1})`

## Customizing the Template

### Title and Author Information

Edit the following sections in `samplepaper.tex`:

- `\title{...}` - Your paper title
- `\author{...}` - Author names and affiliations
- `\institute{...}` - Institution information
- `\authorrunning{...}` - Short author list for running head

**Note:** ORCID IDs are optional. Remove `\orcidID{...}` if you don't have one.

### Abstract and Keywords

Edit the `abstract` environment to add your abstract and keywords.

## Troubleshooting

### Error: "Required program gs not found"

This means you're trying to use an EPS figure without Ghostscript. Solutions:

1. **Recommended:** Convert your EPS to PDF or use PNG/JPG format
2. **Alternative:** Install Ghostscript:
   - macOS: `brew install ghostscript`
   - Linux: `sudo apt-get install ghostscript` (Debian/Ubuntu)
   - Windows: Download from [Ghostscript website](https://www.ghostscript.com/)

### Missing References

If references don't appear correctly, make sure you:
1. Run `pdflatex` twice
2. If using BibTeX, run the full sequence: `pdflatex` → `bibtex` → `pdflatex` → `pdflatex`

### Font Warnings

The template uses T1 font encoding. If you see font warnings, they're usually harmless and can be ignored for local compilation.

## Files in This Directory

- `samplepaper.tex` - Main LaTeX source file
- `llncs.cls` - Springer LNCS document class
- `splncs04.bst` - BibTeX style file (if using BibTeX)
- `fig1.eps` - Sample figure (EPS format - requires Ghostscript)
- `llncsdoc.pdf` - Full documentation for the template

## Additional Resources

- Springer LNCS Author Guidelines: Check Springer's website for the latest submission guidelines
- LaTeX Documentation: [LaTeX Project](https://www.latex-project.org/)

