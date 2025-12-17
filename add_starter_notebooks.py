#!/usr/bin/env python3
"""
Script to add starter notebook content to topic pages.
Converts Jupyter notebooks to HTML and inserts them into topic HTML files.
"""

import json
import re
import html
from pathlib import Path

def markdown_to_html_simple(text):
    """Simple markdown to HTML converter for basic formatting."""
    if not text.strip():
        return ''
    
    lines = text.split('\n')
    result = []
    list_type = None  # 'ul', 'ol', or None
    in_code_block = False
    code_block_lines = []
    current_paragraph = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Code blocks (```)
        if stripped.startswith('```'):
            if in_code_block:
                # End code block
                if code_block_lines:
                    code_text = '\n'.join(code_block_lines)
                    escaped = html.escape(code_text)
                    result.append(f'<pre><code class="language-python">{escaped}</code></pre>')
                code_block_lines = []
                in_code_block = False
            else:
                # Start code block
                if current_paragraph:
                    result.append('<p>' + ' '.join(current_paragraph) + '</p>')
                    current_paragraph = []
                if list_type:
                    result.append(f'</{list_type}>')
                    list_type = None
                in_code_block = True
            i += 1
            continue
        
        if in_code_block:
            code_block_lines.append(line)
            i += 1
            continue
        
        # Headers
        if stripped.startswith('### '):
            if current_paragraph:
                result.append('<p>' + ' '.join(current_paragraph) + '</p>')
                current_paragraph = []
            if list_type:
                result.append(f'</{list_type}>')
                list_type = None
            header_text = stripped[4:]
            # Process inline formatting in headers
            header_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', header_text)
            header_text = re.sub(r'`([^`]+)`', r'<code>\1</code>', header_text)
            result.append(f'<h3>{header_text}</h3>')
            i += 1
            continue
        elif stripped.startswith('## '):
            if current_paragraph:
                result.append('<p>' + ' '.join(current_paragraph) + '</p>')
                current_paragraph = []
            if list_type:
                result.append(f'</{list_type}>')
                list_type = None
            header_text = stripped[3:]
            header_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', header_text)
            header_text = re.sub(r'`([^`]+)`', r'<code>\1</code>', header_text)
            result.append(f'<h2>{header_text}</h2>')
            i += 1
            continue
        elif stripped.startswith('# '):
            if current_paragraph:
                result.append('<p>' + ' '.join(current_paragraph) + '</p>')
                current_paragraph = []
            if list_type:
                result.append(f'</{list_type}>')
                list_type = None
            header_text = stripped[2:]
            header_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', header_text)
            header_text = re.sub(r'`([^`]+)`', r'<code>\1</code>', header_text)
            result.append(f'<h1>{header_text}</h1>')
            i += 1
            continue
        
        # Lists
        if stripped.startswith('- '):
            if current_paragraph:
                result.append('<p>' + ' '.join(current_paragraph) + '</p>')
                current_paragraph = []
            if list_type != 'ul':
                if list_type:
                    result.append(f'</{list_type}>')
                result.append('<ul>')
                list_type = 'ul'
            item_text = stripped[2:]
            # Process inline formatting
            item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
            item_text = re.sub(r'`([^`]+)`', r'<code>\1</code>', item_text)
            # Handle links [text](url)
            item_text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2" target="_blank">\1</a>', item_text)
            result.append(f'<li>{item_text}</li>')
            i += 1
            continue
        elif re.match(r'^\d+\.\s+', stripped):
            if current_paragraph:
                result.append('<p>' + ' '.join(current_paragraph) + '</p>')
                current_paragraph = []
            if list_type != 'ol':
                if list_type:
                    result.append(f'</{list_type}>')
                result.append('<ol>')
                list_type = 'ol'
            item_text = re.sub(r'^\d+\.\s+', '', stripped)
            item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
            item_text = re.sub(r'`([^`]+)`', r'<code>\1</code>', item_text)
            item_text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2" target="_blank">\1</a>', item_text)
            result.append(f'<li>{item_text}</li>')
            i += 1
            continue
        
        # Regular text
        if not stripped:
            if current_paragraph:
                result.append('<p>' + ' '.join(current_paragraph) + '</p>')
                current_paragraph = []
            if list_type:
                result.append(f'</{list_type}>')
                list_type = None
        else:
            # Process inline formatting
            formatted = stripped
            formatted = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', formatted)
            formatted = re.sub(r'`([^`]+)`', r'<code>\1</code>', formatted)
            # Handle links [text](url)
            formatted = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2" target="_blank">\1</a>', formatted)
            current_paragraph.append(formatted)
        
        i += 1
    
    # Close any open structures
    if current_paragraph:
        result.append('<p>' + ' '.join(current_paragraph) + '</p>')
    if list_type:
        result.append(f'</{list_type}>')
    if in_code_block and code_block_lines:
        code_text = '\n'.join(code_block_lines)
        escaped = html.escape(code_text)
        result.append(f'<pre><code class="language-python">{escaped}</code></pre>')
    
    return '\n'.join(result)

def notebook_to_html(notebook_path):
    """Convert a Jupyter notebook to HTML content."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    html_parts = []
    
    for cell in nb.get('cells', []):
        cell_type = cell.get('cell_type', '')
        source = ''.join(cell.get('source', []))
        
        if cell_type == 'markdown':
            # Convert markdown to HTML
            html_content = markdown_to_html_simple(source)
            html_parts.append(f'<div class="notebook-markdown">{html_content}</div>')
        elif cell_type == 'code':
            # Format code blocks
            escaped_code = html.escape(source)
            html_parts.append(f'<div class="notebook-code"><pre><code class="language-python">{escaped_code}</code></pre></div>')
    
    return '\n'.join(html_parts)

def get_topic_dir_name(topic_num):
    """Get the topic directory name for a given topic number."""
    topic_dirs = sorted(Path('Topic').glob(f'{topic_num}.*'))
    if topic_dirs:
        return topic_dirs[0].name
    return None

def update_topic_page(topic_num, topic_dir_name):
    """Update a topic HTML page with a link to the starter notebook on GitHub."""
    topic_file = Path(f'topic{topic_num}.html')
    
    if not topic_file.exists():
        print(f"Warning: {topic_file} not found, skipping...")
        return False
    
    if not topic_dir_name:
        print(f"Warning: Topic directory not found for topic {topic_num}, skipping...")
        return False
    
    with open(topic_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # GitHub repository URL
    github_url = f"https://github.com/nghianguyen7171/ts_course/blob/main/Topic/{topic_dir_name}/starter.ipynb"
    
    # Check if starter notebook section already exists
    if 'starter-notebook-section' in content:
        # Replace existing section
        pattern = r'<section class="card starter-notebook-section">.*?</section>'
        replacement = f'''<section class="card starter-notebook-section">
      <h2>Starter Notebook</h2>
      <p>The starter notebook contains installation instructions and data loading code to help you get started with this topic.</p>
      <div style="margin-top: 20px;">
        <a href="{github_url}" target="_blank" class="btn" style="display: inline-block;">
          📓 View Starter Notebook on GitHub
        </a>
      </div>
      <p style="margin-top: 15px; color: var(--muted);">
        <strong>Note:</strong> You can view the notebook directly on GitHub or download it to run locally in Jupyter.
      </p>
    </section>'''
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    else:
        # Insert before the "Getting Started" section
        getting_started_pattern = r'(<section class="card">\s*<h2>Getting Started</h2>)'
        replacement = f'''<section class="card starter-notebook-section">
      <h2>Starter Notebook</h2>
      <p>The starter notebook contains installation instructions and data loading code to help you get started with this topic.</p>
      <div style="margin-top: 20px;">
        <a href="{github_url}" target="_blank" class="btn" style="display: inline-block;">
          📓 View Starter Notebook on GitHub
        </a>
      </div>
      <p style="margin-top: 15px; color: var(--muted);">
        <strong>Note:</strong> You can view the notebook directly on GitHub or download it to run locally in Jupyter.
      </p>
    </section>

    \\1'''
        content = re.sub(getting_started_pattern, replacement, content)
    
    with open(topic_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Main function to process all starter notebooks."""
    topic_dirs = sorted(Path('Topic').glob('[0-9]*.*'))
    
    for topic_dir in topic_dirs:
        notebook_path = topic_dir / 'starter.ipynb'
        
        if not notebook_path.exists():
            print(f"Warning: {notebook_path} not found, skipping...")
            continue
        
        # Extract topic number from directory name
        topic_num = topic_dir.name.split('.')[0]
        topic_dir_name = topic_dir.name
        
        try:
            print(f"Processing Topic {topic_num}...")
            success = update_topic_page(topic_num, topic_dir_name)
            
            if success:
                print(f"✓ Updated topic{topic_num}.html")
            else:
                print(f"✗ Failed to update topic{topic_num}.html")
        except Exception as e:
            print(f"✗ Error processing Topic {topic_num}: {e}")

if __name__ == '__main__':
    main()

