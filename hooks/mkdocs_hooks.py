import mkdocs.plugins

@mkdocs.plugins.event_priority(0) #default priority
def on_page_context(context, page, config, nav):
    """
    Constructs edit URLs using page frontmatter, usually added in .meta.yml files.
    """
    # Use the documentation repository for edit URLs
    docs_repo_url = page.meta.get("docs_repository") or config.repo_url
    
    # Use the documentation edit URI
    edit_uri = page.meta.get("docs_edit_uri") or config.edit_uri
    
    # Determine the file path for the edit URL
    if "docs_file_path" in page.meta:
        # Complete override of file path
        file_src_uri = page.meta["docs_file_path"]
    else:
        # Use original path with optional transformations
        file_src_uri = page.file.src_uri
        
        # Apply path transformation if specified
        if "docs_path_transform" in page.meta:
            transform = page.meta["docs_path_transform"]
            if isinstance(transform, dict) and "from" in transform and "to" in transform:
                from_path = transform["from"]
                to_path = transform["to"]
                if file_src_uri.startswith(from_path):
                    file_src_uri = to_path + file_src_uri[len(from_path):]

    # Only build edit_url if we have the required components
    if docs_repo_url and edit_uri:
        page.edit_url = f"{docs_repo_url.rstrip('/')}/{edit_uri}{file_src_uri}"
    
    return context