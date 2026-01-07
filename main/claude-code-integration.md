# Claude Code Integration

MacroQuest includes optional integration with [Claude Code](https://claude.ai/claude-code), Anthropic's AI coding assistant. This integration provides specialized agents that understand MacroQuest's API, documentation, and best practices.

## Features

- **Documentation Research**: Ask questions about TLOs, commands, datatypes, and plugins
- **Script Creation**: Generate Lua scripts or macros with proper patterns
- **Debugging Help**: Get assistance troubleshooting scripts
- **Best Practices**: Learn recommended patterns and approaches

The system uses two specialized agents:

| Agent | Purpose |
|-------|---------|
| `MacroQuest-Researcher` | Read-only documentation lookups and API questions |
| `MacroQuest-Expert` | Code creation, editing, debugging, and review |

## Getting the Documentation

First, clone the MacroQuest documentation repository. Open a command prompt or PowerShell and run:

```powershell
git clone https://github.com/macroquest/docs.git C:\mq_docs
```

Or if you already have it, pull the latest:

```powershell
cd C:\mq_docs
git pull
```

## Installation

### Step 1: Copy the stub file

Copy `C:\mq_docs\ai_helpers\claude\mq-stub.md` to your Claude configuration folder:

```
%USERPROFILE%\.claude\commands\mq.md
```

You can do this with:

```powershell
copy C:\mq_docs\ai_helpers\claude\mq-stub.md %USERPROFILE%\.claude\commands\mq.md
```

### Step 2: Configure your paths

Edit `%USERPROFILE%\.claude\commands\mq.md` and update the paths:

```markdown
# Configuration

## Documentation Path (required)
DOCS_DIR: C:\mq_docs\

## MacroQuest Installations
Define one or more installations. First one is the default.

### Live
MACROS_DIR: C:\Users\Public\MacroQuest\Macros\
LUA_DIR: C:\Users\Public\MacroQuest\lua\

### Test
MACROS_DIR: C:\Users\Public\MacroQuest-Test\Macros\
LUA_DIR: C:\Users\Public\MacroQuest-Test\lua\

### EMU
MACROS_DIR: D:\EQEmu\MacroQuest\Macros\
LUA_DIR: D:\EQEmu\MacroQuest\lua\
```

**Configuration rules:**

- `DOCS_DIR` is required - points to your cloned mq_docs folder
- Add as many installations as you need (### Name sections)
- First installation is the default
- `MACROS_DIR` and `LUA_DIR` are optional, but at least one must be defined to work with scripts (LUA_DIR preferred)
- Leave paths as `C:\path\to\...` if not configured yet

That's it! One file, one-time setup.

## Usage

Invoke `/mq` in Claude Code and describe what you need:

```
/mq How do I check if a spell is ready to cast?
```

```
/mq I need a script that handles pulling mobs for my group
```

```
/mq Create a Lua script for my EMU server that tracks DPS
```

The coordinator will:

1. Validate your configuration
2. Determine if this is research or a code task
3. **Recommend Lua for new code** (you can request macro language if preferred)
4. Ask which installation to use (if you have multiple and didn't specify)
5. Ask clarifying questions if needed
6. Delegate to the appropriate agent
7. Summarize results

## Lua vs Macro Language

**For new code, Lua is recommended.** It's more powerful and easier to maintain.

Lua scripts use this structure:

```
LUA_DIR\
└── scriptname\
    └── init.lua    # Main script file
```

## Multi-Installation Support

If you have multiple MacroQuest installations, the coordinator will ask which one to use:

```
/mq Create a healing script

> Which installation should I use? [Live] [Test] [EMU]
```

Or specify upfront:

```
/mq Create a healing script for my Test server
```

## Task Types

| Task Type | Agent | Examples |
|-----------|-------|----------|
| Documentation lookup | Researcher | "What members does the spawn datatype have?" |
| API questions | Researcher | "How do I use MQ2Nav?" |
| Syntax help | Researcher | "What's the spawn search syntax?" |
| Best practices | Researcher | "What's the best way to check if target exists?" |
| Create new script | Expert | "Write a healing script for my cleric" |
| Edit existing code | Expert | "Add a pause feature to this script" |
| Debug issues | Expert | "Why is my script throwing this error?" |
| Code review | Expert | "Review this script for best practices" |

## Updating

To get updates, pull the latest mq_docs:

```powershell
cd C:\mq_docs
git pull
```

Your stub file never needs to change unless you add/move installations.

## Files Reference

The integration files are located in `mq_docs\ai_helpers\claude\`:

| File | Purpose |
|------|---------|
| `mq-stub.md` | Template to copy to `%USERPROFILE%\.claude\commands\mq.md` |
| `mq-full.md` | Coordinator logic (reads your config, spawns agents) |
| `MacroQuest-Researcher-Full.md` | Research agent instructions |
| `MacroQuest-Expert-Full.md` | Code expert agent instructions |
