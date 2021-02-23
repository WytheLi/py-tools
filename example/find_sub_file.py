import os
from collections.abc import Generator   # isinstance(item, Generator)


def find_sub_file(path):
    """
    生成器实现查找子文件
    :param path:
    :return:
    """
    for file in os.listdir(path):
        subfile = os.path.join(path, file)
        if os.path.isdir(subfile):
            yield find_sub_file(subfile)


if __name__ == '__main__':
    for f in find_sub_file('D:\Desktop'):
        print(f)