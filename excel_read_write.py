import pandas as pd


def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df


def write_to_excel(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)


# 使用示例
data = {"Column1": [1, 2, 3], "Column2": [4, 5, 6]}
write_to_excel(data, "/path/to/output.xlsx")
df = read_excel("/path/to/output.xlsx")
print(df)
