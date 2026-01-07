# Instructions

You are a coordinator for MacroQuest scripting tasks.

Read and follow the coordinator instructions at:
${DOCS_DIR}/ai_helpers/claude/mq-full.md

If the above file does not exist, after loading from the configuration below, help the user set it.

Use the configuration below. Pass paths to agents when delegating tasks.

---

# Configuration

## Documentation Path (required)
DOCS_DIR: D:\path\to\mq_docs\

## MacroQuest Installations
Define one or more installations below. The first one is the primary (default).
Each installation needs a name, and optionally LUA_DIR and/or MACROS_DIR.

### Live
LUA_DIR: C:\path\to\MacroQuest\lua\
MACROS_DIR: C:\path\to\MacroQuest\Macros\

### Test
LUA_DIR: C:\path\to\MacroQuest-Test\lua\
MACROS_DIR: C:\path\to\MacroQuest-Test\Macros\
