# NeoVim Syntax File

## Pre-Requisites

- [Neovim](https://neovim.io/)
- A Language Server Protocol (LSP) Extension such as [lua-ls](https://github.com/LuaLS/lua-language-server).

## Installation

- Download the latest syntax files from [here](https://github.com/macroquest/mq-definitions).
- Place the extracted files in a sub-directory of your neovim configuration directory.
    - e.g. `~/.config/nvim/mq-syntax/` on Linux or `c:\users\<user>\AppData\Local\nvim\mq-syntax` on Windows
- Modify the configuration of your LSP to load your third party syntax files and enable them.

```lua
lua_ls = function()
    local lspconfig = require("lspconfig")
    lspconfig.lua_ls.setup({
        capabilities = capabilities,
        settings = {
            Lua = {
                workspace = {
                    preloadFileSize = 1000,
                    checkThirdParty = true,
                    library = {
                        "C:/Users/<user>/AppData/Local/nvim/lua/mq-syntax",
                    },
                },

                runtime = { version = "Lua 5.2" },
                diagnostics = {
                    globals = {
                        "bit",
                        "vim",
                        "it",
                        "describe",
                        "before_each",
                        "after_each",
                        "mq",
                        "Mq",
                        "ImGui",
                    },
                },
            },
        },
    })
end,
```

