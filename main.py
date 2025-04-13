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

    @env.macro
    def embedCommand(command_file):
        data = parse_command_file(command_file)

        doc_url = data.get("doc_url", "#")
        syntax_content = data.get("syntax_content")
        is_codeblock = data.get("is_codeblock", False)
        lexer = data.get("lexer", "")
        full_description = data.get("full_description", "")
        has_more_content = data.get("has_more_content", False)

        syntax = f'<a href="{doc_url}">⚠️ Syntax missing</a>' 
        if syntax_content:
            if is_codeblock:
                lexer_str = lexer or ''
                syntax = f'<a href="{doc_url}">\n```{lexer_str}\n{syntax_content}\n```\n</a>'
            else:
                syntax = f'<a href="{doc_url}">{syntax_content}</a>'

        # Format Description (add "read more" link if it's long)
        formatted_description = ""
        if full_description:
            description = full_description
            read_more_link = f' [:material-book-arrow-right-outline:]({doc_url})'
            max_description_length = 280
            if len(description) > max_description_length:
                # Find a space between words before cutting off a long description
                break_point = description.rfind(' ', 0, max_description_length - len(read_more_link) - 3)
                if break_point == -1:
                    break_point = max_description_length - len(read_more_link) - 3
                formatted_description = description[:break_point] + '...' + read_more_link
            elif has_more_content:
                formatted_description = description + read_more_link
            else:
                formatted_description = description
        
        return f"{syntax}\n:   {formatted_description}"

    @env.macro
    def embedMQType(doc_file):
        data = parse_mq_type(doc_file)

        doc_url = data.get("doc_url", "#") # the default URL is a same page link
        name = data.get("name", "Unknown Type")
        description = data.get("description", "No description available.")
        members = data.get("members", [])
        link_refs = data.get("link_refs", [])

        members_table = ""
        if members:
            members_table = "\n\n" + render_members_table(members, link_refs) + "\n\n"

        link_refs_part = ""
        if link_refs:
            formatted_links = "\n".join([f"[{ref_name}]: {ref_url}" for ref_name, ref_url in link_refs])
            link_refs_part = f"\n\n{formatted_links}"

        # Add read more link only if description exists
        read_more_indicator = f" [:material-book-arrow-right-outline:]({doc_url})" if description else ""

        result = (
            f"### [`{name}`]({doc_url})\n\n"
            f"{description}{read_more_indicator}\n\n"
            f"{members_table}"
            f"{link_refs_part}"
        )

        return result

# == Helper functions ==

def parse_command_file(command_file):
    """
    Parse command file for syntax and description.
    """
    try:
        content = Path(command_file).read_text()
        base_dir = Path(command_file).parent
        doc_url = make_content_link(command_file)
    except FileNotFoundError:
        return {
            "doc_url": "#",
            "syntax_content": "Error: File not found",
            "lexer": "",
            "is_codeblock": False,
            "full_description": "",
            "has_more_content": False,
        }

    syntax_content = None
    lexer = ""
    is_codeblock = False
    full_description = ""
    has_more_content = False

    # Extract syntax (and lexer) that's in a code block so we can render the link correctly.
    syntax_match = re.search(
        r'## Syntax\s*\n\s*```(\w+)?\s*\n(.*?)\n```',
        content, re.DOTALL
    )
    if syntax_match:
        is_codeblock = True
        lexer = syntax_match.group(1) or ""
        syntax_content = syntax_match.group(2).strip()
    else:
        # Extract syntax that's not in a code block, which is much simpler to render:
        syntax_match = re.search(
            r'## Syntax\s+\n+(.+?)(?=\n\n|\n##)',
            content, re.DOTALL
        )
        if syntax_match:
            syntax_content = syntax_match.group(1).strip()

    # Extract first paragraph of description (before any subsections)
    description_match = re.search(
        r'## Description\s+\n+(.*?)(?=\n\n\*\*|\n##|$)',
        content, re.DOTALL
    )
    if description_match:
        description_text = description_match.group(1).strip()
        # Convert links and collapse whitespace
        full_description = convert_relative_links(description_text, base_dir)
        full_description = re.sub(r'\s*\n\s*', ' ', full_description)
        # Check if there's more content after the description paragraph
        remaining_content = content[description_match.end():]
        if re.search(r'\n\n\*\*|\n##', remaining_content):
            has_more_content = True

    return {
        "doc_url": doc_url,
        "syntax_content": syntax_content,
        "lexer": lexer,
        "is_codeblock": is_codeblock,
        "full_description": full_description,
        "has_more_content": has_more_content,
    }

def parse_mq_type(doc_file):
    """
    Extract information from a TLO or datatype file
    """
    try:
        content = Path(doc_file).read_text()
        doc_path = Path(doc_file)
        base_dir = doc_path.parent
        doc_url = make_content_link(doc_file)
    except FileNotFoundError:
        return {
            "name": "Error: File not found",
            "description": "",
            "section_name": "",
            "members": [],
            "link_refs": [],
            "doc_url": "#",
        }

    # Initialize variables with default values
    name = ""
    description = ""
    section_name = ""
    members = []
    link_refs = [] # Initialize link_refs as an empty list

    # Extract the name from the top of the page.
    name_match = re.search(r'# `(.+?)`', content)
    if name_match:
        name = name_match.group(1)

    # Extract the description as the first paragraph after the header.
    desc_match = re.search(r'# `.+?`\s*\n+(.*?)(?=\n\n|\n##|$)', content, re.DOTALL)
    if desc_match: # Check if match was found
        description_text = desc_match.group(1).strip()
        description = re.sub(r'\s*\n\s*', ' ', description_text)
        description = convert_relative_links(description, base_dir)

    # Extract the Members or Forms section. Stops when a new level-2 header (##) appears.
    section_match = re.search(r'## (Forms|Members)\s*\n+(.*?)(?=\n##(?!#)|$)', content, re.DOTALL)
    if section_match:
        section_name = section_match.group(1)
        raw_section_content = section_match.group(2).strip()
        # Parse out the individual member definitions.
        members = parse_render_members(raw_section_content, base_dir)

    # Process link references using helper
    link_ref_matches = re.findall(r'^\[([^\]]+)\]:\s*(.+?)(?:\s*)$', content, re.MULTILINE)
    for ref_name, ref_url in link_ref_matches:
        if ref_url.endswith('.md'):  # Only process .md links
            try:
                absolute_ref = make_content_link(ref_url, base_dir)
                link_refs.append((ref_name, absolute_ref))
            except Exception as e:
                print(f"Warning: Could not process link ref [{ref_name}]: {ref_url} in {doc_file}. Error: {e}")

    return {
        "name": name,
        "description": description,
        "section_name": section_name,
        "members": members,
        "link_refs": link_refs,
        "doc_url": doc_url,
    }

def parse_render_members(raw_content, base_dir):
    """
    parse renderMember macro calls for member info.
    """
    # Pattern captures the parameters inside renderMember and then the description
    pattern = r"###\s*\{\{\s*renderMember\s*\((.*?)\)\s*\}\}\s*\n\s*\:\s*(.*?)(?=\n###|\Z)"
    matches = re.findall(pattern, raw_content, re.DOTALL)
    
    members = []
    for params_str, description in matches:
        # Capture key='value' pairs from the renderMember call.
        kv_pattern = r"(\w+)\s*=\s*'([^']+)'"
        kv_pairs = re.findall(kv_pattern, params_str)
        params = {k: v for k, v in kv_pairs}
        
        member_name = params.get("name", "").strip()
        member_type = params.get("type", "").strip()
        members.append({
            "name": member_name,
            "type": member_type,
            "description": convert_relative_links(description.strip(), base_dir)
        })
    return members

def make_content_link(file_path, base_dir=None):
    """
    Convert a file path to mkdocs url
    - (when base_dir=None): "commands/foo.md" → "/commands/foo/"
    - (with base_dir): "../datatypes/bar.md" → "/datatypes/bar/"
    """
    if base_dir:
        # For relative links within embedded content
        full_path = PurePosixPath(base_dir / file_path)
    else:
        # For main document (embed-er) links
        full_path = PurePosixPath(file_path)
        
    return f"/{full_path.with_suffix('')}/"

def convert_relative_links(content, base_dir):
    """
    Convert relative links to absolute links for embedded content
    """
    def replace_link(match):
        text = match.group(1)
        rel_path = match.group(2)
        return f"[{text}]({make_content_link(rel_path, base_dir)})"
    
    return re.sub(
        r'\[([^\]]+)\]\(([^\)]+\.md)\)',
        replace_link,
        content
    )

def render_members_table(members, link_refs):
    """
    Use members and link_refs to create a markdown table.
    """
    lines = [
        "| Type | Member | Description |",
        "| ---- | ------ | ----------- |"
    ]
    # Convert link_refs to a dictionary for easier lookup
    link_dict = {ref_name: ref_url for ref_name, ref_url in link_refs}
    for m in members:
        type_val = m["type"]
        if type_val in link_dict:
            type_rendered = f"[{type_val}]({link_dict[type_val]})"
        else:
            type_rendered = type_val
        lines.append(f"| {type_rendered} | `{m['name']}` | {m['description']} |")
    return "\n".join(lines)