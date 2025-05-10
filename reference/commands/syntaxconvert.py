# this script converts command syntax from markdown to the eqcommand lexer format.

import os
import re
from pathlib import Path
import argparse

def convert_syntax_line(line):
    # First remove all residual bold markers
    line = line.replace('**', '')
    # Then handle quoted names and parameters
    line = re.sub(r'_"([^"]+)"_', r'<"\1">', line)
    # Modified regex to capture phrases with spaces
    line = re.sub(r'_([^_]+)_', r'<\1>', line)
    return line

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Updated regex to capture entire syntax block
    converted = re.sub(
        r'(## Syntax\n+)(.*?)(?=\n##|\n\n|\Z)',
        lambda m: f'{m.group(1)}```eqcommand\n{convert_syntax_line(m.group(2))}\n```',
        content,
        flags=re.DOTALL
    )

    if converted != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(converted)
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description='Convert command syntax formatting')
    parser.add_argument('--file', help='Process a single file')  # <-- Argument definition
    args = parser.parse_args()  # <-- Argument parsing

    commands_dir = Path(__file__).parent
    
    if args.file:  # <-- Argument check
        target_file = commands_dir / args.file
        if not target_file.exists():
            print(f"Error: File {args.file} not found")
            return
        if process_markdown_file(target_file):
            print(f"Successfully processed {args.file}")
        else:
            print(f"No changes needed for {args.file}")
    else:
        processed_files = 0
        
        for md_file in commands_dir.glob('*.md'):
            if md_file.name == 'README.md':
                continue
            
            try:
                if process_markdown_file(md_file):
                    print(f'Processed: {md_file.name}')
                    processed_files += 1
            except Exception as e:
                print(f'Error processing {md_file.name}: {str(e)}')
        
        print(f'\nConversion complete. Modified {processed_files} files.')

if __name__ == '__main__':
    main()
