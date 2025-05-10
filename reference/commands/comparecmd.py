#lets find out if we have all the commands in the README.md file
import os
import re

# Configuration
commands_dir = "D:/Users/Trevor/Dropbox/work/scripts/readguides/docs/projects/macroquest/reference/commands"
readme_path = "D:/Users/Trevor/Dropbox/work/scripts/readguides/docs/projects/macroquest/reference/commands/README.md"




# Get list of command files (excluding README.md)
command_files = set()
for f in os.listdir(commands_dir):
    if f.endswith(".md") and f != "README.md":
        command_files.add(f[:-3].lower())  # Remove .md extension and normalize case

# Parse README.md for listed commands
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

# Find all command links in format [/command](command)
listed_commands = set(re.findall(r"\[/(\w+)\]\([\w/.-]+\)", readme_content, re.IGNORECASE))

# Compare sets
missing_in_readme = command_files - listed_commands
extra_in_readme = listed_commands - command_files

# Print results
print("Commands missing from README.md:")
print("\n".join(sorted(missing_in_readme)) or "None")

print("\nCommands in README but missing documentation files:")
print("\n".join(sorted(extra_in_readme)) or "None")

# Print summary
print(f"\nDocumentation coverage: {len(command_files & listed_commands)}/{len(command_files)} commands documented")