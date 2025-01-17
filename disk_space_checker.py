import shutil


def check_disk_space(path, threshold):
    total, used, free = shutil.disk_usage(path)
    free_gb = free // (2**30)
    if free_gb < threshold:
        print(f"Warning: Free disk space is below {threshold} GB.")
    else:
        print(f"Free disk space: {free_gb} GB.")


# 使用示例check_disk_space('/', 10)
