from pathlib import Path as p

cwds = p.cwd()
parent = cwds.parent
print(f'Is this a directory? {str(parent.is_dir())}')
for child in parent.iterdir():
    if child.is_dir():
        print(child)
