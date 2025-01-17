import os
from shutil import move


def sort_files(directory_path):
    """
    将指定目录中的文件按扩展名分类并移动到相应的子目录中。

    Args:
        directory_path (str): 要处理的目录路径。

    Returns:
        None

    Raises:
        无

    """
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            parts = filename.rsplit(".", 1)
            file_extension = parts[-1] if len(parts) > 1 else ""
            if not file_extension:
                file_extension = "no_extension"
            destination_dir = os.path.join(directory_path, file_extension)
            try:
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                move(
                    os.path.join(directory_path, filename),
                    os.path.join(destination_dir, filename),
                )
            except Exception as e:
                print(f"Error processing file {filename}: {e}")


# 使用示例
sort_files("/path/to/directory")
