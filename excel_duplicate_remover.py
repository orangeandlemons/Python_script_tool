import pandas as pd


def remove_duplicates(file_path):
    df = pd.read_excel(file_path)
    df.drop_duplicates(inplace=True)
    df.to_excel(file_path, index=False)


# 使用示例
remove_duplicates("/path/to/data.xlsx")
