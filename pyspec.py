# this file is use to collect all the file(useful for constructing spec project)
import os

exception = [
    'tewt',
    '__pychache__',
    '.vscode',
    'build',
    'dist',
]

def append(dir: str, files: [str]):
    for file in os.listdir(dir):
        if file in exception:
            continue
        if os.path.isdir(os.path.join(dir, file)): # there may be tewt dir
            append(os.path.join(dir, file), files)
        else:
            if file.endswith('.py'):
                files.append(os.path.join(dir, file).replace('.\\', '').replace('\\', '/'))

if __name__ == '__main__':
    curdir = os.curdir
    files = []
    append(curdir, files)
    print(files)
