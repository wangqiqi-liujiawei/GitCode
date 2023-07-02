from pathlib import Path as path

cwd = path.cwd()
print(f'Current working directory: {str(cwd)}')

new_file = path.joinpath(cwd, 'new_file.txt')
print(f'full path:{str(new_file)}')

print(f'Does that file exist? {str(new_file.exists())}')
