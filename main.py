def define_env(env):

    @env.macro
    def renderMember(name, type=None, params=None):
      type_str = f"[{type}][{type}]" if type else ""
      params_str = f"[{params}]" if params else ""

      return f"{type_str} `{name}` {{ #{name}{params_str} data-toc-label='{name}{params_str}' }}"