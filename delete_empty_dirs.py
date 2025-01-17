import os


def remove_empty_folders(directory_path):
    """
    删除指定目录及其子目录中的所有空文件夹。

    Args:
        directory_path (str): 要删除的根目录路径。

    Returns:
        None

    """
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


# 使用示例
remove_empty_folders("/path/to/directory")
