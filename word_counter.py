def count_words(file_path):
    """
    统计指定文件路径中的单词数量。

    Args:
        file_path (str): 需要统计单词数量的文件路径。

    Returns:
        int: 文件中的单词数量。

    Example:
        >>> word_count = count_words("/path/to/file.txt")
        >>> print(word_count)
        100

    """
    with open(file_path, "r") as f:
        text = f.read()
    word_count = len(text.split())
    return word_count


# 使用示例
word_count = count_words("/path/to/file.txt")
print(f"Word count: {word_count}")
