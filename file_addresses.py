
from pathlib import Path


def create_file(name):
    current = Path(__file__).resolve().parent
    fldr_target = current / name
    files = [f for f in fldr_target.iterdir() if '.jpg' == f.suffix]
    st_files = list(map(str, files))
    file_target = current / f'{name}.txt'
    with open(str(file_target), 'w') as f:
        f.write('\n'.join(str(file) for file in files))

names = [
    'test',
    'train',
    'valid',
]

for name in names:
    create_file(name)