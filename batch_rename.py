import os


def rename_files(directory_path, old_name, new_name):
    """
    批量重命名指定目录下的文件。

    Args:
        directory_path (str): 要重命名文件的目录路径。
        old_name (str): 文件中需要被替换的旧名称。
        new_name (str): 替换后的新名称。

    Returns:
        None

    Raises:
        FileNotFoundError: 如果指定的目录不存在。
        PermissionError: 如果程序没有足够的权限去重命名文件。

    """
    for filename in os.listdir(directory_path):
        if old_name in filename:
            new_filename = filename.replace(old_name, new_name)
            os.rename(
                os.path.join(directory_path, filename),
                os.path.join(directory_path, new_filename),
            )


# 使用示例
rename_files("/path/to/directory", "old", "new")
