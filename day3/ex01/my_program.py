
from path import Path


def act():
    try:
        Path.makedirs('Test_dir')
    except FileExistsError as e:
        print(e)
    Path.touch('Test_dir/test_file')
    f = Path('Test_dir/test_file')
    f.write_lines(['test', 'text', 'test', 'line'])
    print(f.read_text())


if __name__ == '__main__':
    act()
