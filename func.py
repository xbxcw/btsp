import os
# import psutil


def find_specified_file(path, suffix=''):
    """
    查找指定文件
    :param path: 根目录
    :param suffix: 格式，默认是空
    :return: 文件地址列表
    """
    _file = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(suffix):
                _file.append(os.path.join(root, file))
    return _file


def create_directory(directory):
    """
    创建路径，如果文件夹不存在，就创建
    :param directory (str)
    :return: directory(str)
    """
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory