import re
from pathlib import Path, PurePosixPath

def define_env(env):

    @env.macro
    def renderMember(name, type=None, params=None, toc_label=None):
        if type == 'varies':
            type_str = '_varies_'
        elif type:
            type_str = f"[{type}][{type}]"
        else:
            type_str = ''

        params_str = f"[{params}]" if params else ""
        
        if toc_label is None:
            toc_label = f'{name}{params_str}'

        return f"{type_str} `{name}{params_str}` {{ #{toc_label} data-toc-label='{toc_label}' }}"

    # output a read more link if the file has sections beyond Members/Forms/Description
    @env.macro
    def readMore(doc_file):
        page = env.variables.page
        file_result = read_file(doc_file, page)
        
        if not file_result["success"]:
            return ""
            
        has_extra = has_extra_sections(file_result["content"])
        doc_url = file_result["doc_url"]
        
        if has_extra:
            return f'[:material-book-arrow-right-outline:]({doc_url} "Full documentation")'
        return ''

# == Helper Functions ==

def read_file(file_path, page):
    try:
        doc_path = Path(file_path)
        content = doc_path.read_text()
        base_dir = doc_path.parent
        doc_url = relative_link(file_path, page.file.src_uri) # src_uri is the path to the embedding page
        return {
            "content": content,
            "base_dir": base_dir,
            "doc_url": doc_url,
            "success": True,
            "error": None
        }
    except Exception as e:
        return {
            "content": "",
            "base_dir": None,
            "doc_url": "#",
            "success": False,
            "error": str(e)
        }

# create an mkdocs-style url that's relative to the embedding page
def relative_link(target_file_path, embedding_page_src_uri, base_dir=None):
    # Absolute path of the target markdown file
    target_path = (PurePosixPath(base_dir) / target_file_path if base_dir else PurePosixPath(target_file_path))
    embedding_file = PurePosixPath(embedding_page_src_uri)
    
    if embedding_file.stem.lower() in ("readme", "index"):
        # main/guide/README.md   ->  main/guide/
        output_dir = embedding_file.parent
    else:
        # main/foo.md       ->  main/foo/
        output_dir = embedding_file.parent / embedding_file.stem

    # Relative path from the embedding page to the target file
    relative_path = target_path.relative_to(output_dir, walk_up=True)

    # strip .md, add trailing slash
    if relative_path.name.lower() in ("index.md", "readme.md"):
        parent_dir = relative_path.parent
        return "./" if str(parent_dir) == "." else f"{parent_dir}/"
    return f"{relative_path.with_suffix('')}/"

# extra sections beyond Members/Forms/Description
def has_extra_sections(content):
    SECTION_PATTERN = r'^##\s+(.+?)\s*$'
    target_sections = {"Members", "Forms", "Description", "Associated DataTypes", "DataTypes"}
    
    lines = content.split('\n')
    sections = []
    
    # Find all section headers and their positions
    for i, line in enumerate(lines):
        match = re.match(SECTION_PATTERN, line)
        if match:
            sections.append((i, match.group(1).strip()))
    
    # Find last occurrence of target sections
    last_target_index = -1
    for idx, (line_num, section) in enumerate(sections):
        if section in target_sections:
            last_target_index = idx
    
    # Check if there are sections after the last target section
    if last_target_index != -1 and len(sections) > last_target_index + 1:
        return True
        
    return False