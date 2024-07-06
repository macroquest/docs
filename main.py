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