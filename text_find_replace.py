def find_replace(file_path, search_text, replace_text):
    """
    在文件中查找并替换文本。

    Args:
        file_path (str): 文件路径。
        search_text (str): 要查找的文本。
        replace_text (str): 用于替换的文本。

    Returns:
        None

    Raises:
        FileNotFoundError: 如果文件路径无效或文件不存在，则引发 FileNotFoundError 异常。
        IOError: 如果在读取或写入文件时发生错误，则引发 IOError 异常。

    """
    with open(file_path, "r") as f:
        text = f.read()
        modified_text = text.replace(search_text, replace_text)
        with open(file_path, "w") as f:
            f.write(modified_text)


# 使用示例
find_replace("/path/to/file.txt", "old", "new")
