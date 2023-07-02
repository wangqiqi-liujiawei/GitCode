from pathlib import Path as path

cwd = path.cwd()
demo_file = path(path.joinpath(cwd, 'demo.txt'))
print(f'file path: {demo_file}')
print(f'file name: {demo_file.name}')
print(f'file suffix: {demo_file.suffix}')
print(f'file folder: {demo_file.parent.name}')
print(f'file size: {str(demo_file.stat().st_size)}')
