#!/usr/bin/env python3
# Clone plugin repos, copy docs, delete clones
import subprocess
import json
import shutil
import tempfile
import os

def update_plugin(prefix, url, branch, docs_path):
    plugin_name = os.path.basename(prefix)
    
    with tempfile.TemporaryDirectory() as tmp:
        print(f"Cloning {plugin_name}...")
        subprocess.run(f'git clone -b {branch} --depth 1 {url} {tmp}/repo', 
                      shell=True, check=True, capture_output=True)
        
        src = os.path.join(tmp, 'repo', docs_path)
        if not os.path.exists(src):
            print(f"  Warning: {docs_path} not found, skipping")
            return
        
        print(f"  Copying {docs_path} -> {prefix}")
        if os.path.exists(prefix):
            shutil.rmtree(prefix)
        shutil.copytree(src, prefix)

def main():
    with open('community_docs.json', 'r') as f:
        plugins = json.load(f)
    
    for prefix, config in plugins.items():
        update_plugin(prefix, config['url'], config['branch'], config['docs_path'])
    
    print("\nDone!")

if __name__ == '__main__':
    main()

