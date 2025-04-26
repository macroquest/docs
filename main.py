import re
import textwrap
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
        page = env.variables.page
        data = parse_command_file(command_file, page)

        doc_url = data.get("doc_url", "#")
        syntax_content = data.get("syntax_content")
        is_codeblock = data.get("is_codeblock", False)
        lexer = data.get("lexer", "")
        full_description = data.get("full_description", "")
        has_more_content = data.get("has_more_content", False)

        # we use html links here because markdown wasn't able to link a codeblock.
        syntax = f'<a href="{doc_url}">⚠️ Syntax missing</a>'
        if syntax_content:
            if is_codeblock:
                lexer_str = lexer or ''
                syntax = f'<a href="{doc_url}">\n```{lexer_str}\n{syntax_content}\n```\n</a>'
            else:
                syntax = f'<a href="{doc_url}">{syntax_content}</a>'

        formatted_description = truncate_description(
            full_description,
            doc_url,
            has_more_content
        )

        return f"{syntax}\n:   {formatted_description}\n"

    @env.macro
    def embedMQType(doc_file):
        page = env.variables.page 
        data = parse_type_file(doc_file, page)

        doc_url = data.get("doc_url", "#") # the default URL is a same page link
        name = data.get("name", "Unknown Type")
        description = data.get("description", "No description available.")
        members = data.get("members", [])
        link_refs = data.get("link_refs", [])

        members_table = ""
        if members:
            members_table = "\n\n" + render_members_table(members, link_refs) + "\n\n"

        # Unified truncation using shared helper
        formatted_desc = truncate_description(
            data.get("full_description", data.get("description", "")),
            doc_url,
            data.get("has_more_content", False)
        )

        result = (
            f"### [`{name}`]({doc_url})\n\n"
            f"{formatted_desc}\n\n"  # Use processed description
            f"{members_table}"
        )

        return result

# == Helper functions ==

# Parse for syntax and description.
def parse_command_file(command_file, page):
    SYNTAX_CODEBLOCK_PATTERN = r'## Syntax\s*\n\s*```(\w+)?\s*\n(.*?)\n```'
    SYNTAX_NOCODE_PATTERN = r'## Syntax\s+\n+(.+?)(?=\n\n|\n##)'
    DESCRIPTION_PATTERN = r'## Description\s*\n(.*?)(?=\n\n\*\*|\n##|$)'

    file_result = read_file(command_file, page)

    # Initialize for clarity
    data = {
        "doc_url": file_result["doc_url"],
        "syntax_content": None,
        "lexer": "",
        "is_codeblock": False,
        "full_description": "",
        "has_more_content": False
    }

    # return on error
    if not file_result["success"]:
        data["syntax_content"] = f"Error: {file_result['error']}"
        data["full_description"] = "Documentation file could not be loaded"
        return data

    content = file_result["content"]
    base_dir = file_result["base_dir"]

    # This keeps track of how far down the file we've parsed for the has_more_content check
    end_pos = 0

    # Syntax is in codeblocks
    syntax_match = re.search(SYNTAX_CODEBLOCK_PATTERN, content, re.DOTALL)
    if syntax_match:
        data.update({
            "is_codeblock": True,
            "lexer": syntax_match.group(1) or "",
            "syntax_content": syntax_match.group(2).strip()
        })
        end_pos = max(end_pos, syntax_match.end())
    else:
        # Syntax if no codeblocks, we use extract_section for help.
        syntax_content_nocode, syntax_end = extract_section(SYNTAX_NOCODE_PATTERN, content)
        if syntax_content_nocode:
            data["syntax_content"] = syntax_content_nocode
            end_pos = max(end_pos, syntax_end)
        else:
             data["syntax_content"] = "⚠️ Syntax missing"

    description_text, desc_end = extract_section(
        DESCRIPTION_PATTERN, 
        content,
        clean_whitespace=True,
        convert_links=True,
        base_dir=base_dir,
        page=page
    )

    if description_text:
        data["full_description"] = description_text
        end_pos = max(end_pos, desc_end)
    # else: # No need for else, default is ""

    data["has_more_content"] = bool(re.search(r'\S', content[end_pos:].strip()))

    return data

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

# create a url that's relative to the embedding page
def relative_link(target_file_path, embedding_page_src_uri, base_dir=None):
    # i could only get this working with pureposixpath
    target_path = PurePosixPath(base_dir) / target_file_path if base_dir else PurePosixPath(target_file_path)
    embedding_dir = PurePosixPath(embedding_page_src_uri).parent

    relative_path = target_path.relative_to(embedding_dir, walk_up=True)

    # special case for index and readme files
    if relative_path.name.lower() in ('index.md', 'readme.md'):
        parent_dir = relative_path.parent
        return './' if str(parent_dir) == '.' else f"{parent_dir}/"

    # otherwise, remove the .md extension and add a trailing slash
    return f"{relative_path.with_suffix('')}/"

def extract_section(pattern, content, clean_whitespace=False, convert_links=False, base_dir=None, page=None):
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return None, None
        
    extracted = match.group(1).strip()
    
    if clean_whitespace:
        extracted = re.sub(r'\s*\n\s*', ' ', extracted)
        
    if convert_links and base_dir and page:
        extracted = rewrite_markdown_links(extracted, base_dir, page)
    
    return extracted, match.end()

def parse_type_file(doc_file, page):
    NAME_PATTERN = r'# `(.+?)`'
    DESCRIPTION_PATTERN = r'# `.+?`\s*\n+(.*?)(?=\n\n|\n##|$)'
    SECTION_PATTERN = r'## (Forms|Members)\s*\n+(.*?)(?=\n##(?!#)|$)'
    LINK_REF_PATTERN = r'^\[([^\]]+)\]:\s*(.+?)(?:\s*)$'

    file_result = read_file(doc_file, page)

    # Initialize for clarity
    data = {
        "doc_url": file_result["doc_url"], 
        "name": "Unknown Type",
        "full_description": "",
        "section_name": "",
        "members": [],
        "link_refs": [], 
        "has_more_content": False,
    }

    # return on error
    if not file_result["success"]:
        data["name"] = "Error loading type"
        data["full_description"] = f"Error: {file_result['error']}"
        return data

    content = file_result["content"]
    base_dir = file_result["base_dir"]
    
    # This keeps track of how far down the file we've parsed for the has_more_content check
    end_pos = 0

    # Name extraction
    name_match = re.search(NAME_PATTERN, content)
    if name_match:
        data["name"] = name_match.group(1) # Update data dict
        # Update end_pos to the end of the name section if it's further
        end_pos = max(end_pos, name_match.end())

    description_text, desc_end = extract_section(
        DESCRIPTION_PATTERN,
        content,
        clean_whitespace=True,
        convert_links=True,
        base_dir=base_dir,
        page=page
    )

    if description_text:
        data["full_description"] = description_text
        end_pos = max(end_pos, desc_end)

    # Members section extraction
    section_match = re.search(
        SECTION_PATTERN,
        content, re.DOTALL
    )

    if section_match:
        data["section_name"] = section_match.group(1) # Forms or Members
        raw_content = section_match.group(2).strip()
        data["members"] = parse_render_members(raw_content, base_dir, page) 
        end_pos = max(end_pos, section_match.end())

    # Link reference extraction
    link_ref_matches = re.findall(LINK_REF_PATTERN, content, re.MULTILINE)
    processed_link_refs = [] 
    for ref_name, ref_url in link_ref_matches:
        if ref_url.endswith('.md'):
            relative_ref_url = relative_link(ref_url, page.file.src_uri, base_dir=base_dir)
            processed_link_refs.append((ref_name, relative_ref_url))
    data["link_refs"] = processed_link_refs

    data["has_more_content"] = bool(re.search(r'\S', content[end_pos:].strip()))

    return data

# parse renderMember macro calls
def parse_render_members(raw_content, base_dir, page):
    MEMBER_PATTERN = r"###\s*\{\{\s*renderMember\s*\((.*?)\)\s*\}\}(?:\s*\n\s*\:\s*(.*?))?(?=\n\n|\n###|\Z)"
    KV_PAIR_PATTERN = r"(\w+)\s*=\s*'([^']+)'"

    matches = re.findall(MEMBER_PATTERN, raw_content, re.DOTALL)
    members = []
    for params_str, description in matches:
        kv_pairs = re.findall(KV_PAIR_PATTERN, params_str)
        params_dict = {k: v for k, v in kv_pairs}

        member_name = params_dict.get("name", "").strip()
        member_type = params_dict.get("type", "").strip()
        member_params = params_dict.get("params", "").strip()
        # convert any links in the description
        cleaned_description = rewrite_markdown_links(description.strip(), base_dir, page) if description else ""
        members.append({
            "name": member_name,
            "type": member_type,
            "params": member_params,
            "description": cleaned_description
        })
    return members

def rewrite_markdown_links(content, base_dir, page): 
    MARKDOWN_LINK_PATTERN = r'\[([^\]]+)\]\(([^\)]+\.md)\)'

    def replace_link(match):
        name = match.group(1)
        rel_path = match.group(2)
        return f"[{name}]({relative_link(rel_path, page.file.src_uri, base_dir=base_dir)})"

    return re.sub(
        MARKDOWN_LINK_PATTERN,
        replace_link,
        content
    )

# a nice little markdown table
def render_members_table(members, link_refs):
    lines = [
        "| Type | Member | Description |",
        "| ---- | ------ | ----------- |"
    ]
    link_dict = {ref_name: ref_url for ref_name, ref_url in link_refs}
    for m in members:
        type_val = m["type"]
        if type_val in link_dict: # does it match a link ref?
            type_rendered = f"[{type_val}]({link_dict[type_val]})"
        elif type_val:
            type_rendered = f"`{type_val}`"
        else:
            type_rendered = ''

        member_name = m['name']
        member_params = m.get('params')
        if member_params:
            member_name_rendered = f"`{member_name}[{member_params}]`"
        else:
            member_name_rendered = f"`{member_name}`"

        lines.append(f"| {type_rendered} | {member_name_rendered} | {m['description']} |")
    return "\n".join(lines)

def truncate_description(description_text, doc_url, has_more_content, max_length=280):
    if not description_text:
        return ""
    
    read_more_link = f' [:material-book-arrow-right-outline:]({doc_url})'
    max_desc_length = max(max_length - len(read_more_link), 0)
    
    shortened = textwrap.shorten(description_text, width=max_desc_length, break_long_words=False, placeholder='...')
    
    if has_more_content:
        return f"{shortened}{read_more_link}"
    
    if len(shortened) < len(description_text):
        return f"{shortened}{read_more_link}"
    
    return description_text