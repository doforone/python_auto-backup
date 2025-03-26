# -*- coding: UTF-8 -*-
# 运行环境：Python 3.8（为兼容 Windows 7 及 Windows 2008 系统）
# 作者邮箱：chaoxian102@gmail.com
# 微信：chaoxian102（超弦102）
# 支付宝：abtrue@hotmail.com
# Paypal：https://paypal.me/abtruecom
# 感谢打赏


import os
import shutil

# 定义比较并删除文件的函数
def compare_and_delete(source_dir, target_dir):
    """
    在目标目录（target_dir）中检查文件和文件夹是否存在于源目录（source_dir）中。
    如果目标目录中的文件或文件夹在源目录中不存在，则删除它们。
    """
    # 遍历目标目录及其子目录
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            # 构造源文件和目标文件的完整路径
            source_file = os.path.join(source_dir, os.path.relpath(root, target_dir), file)
            target_file = os.path.join(root, file)

            # 如果源目录中没有对应的文件，则删除目标文件
            if not os.path.exists(source_file):
                print(f"Deleting: {target_file}")
                os.remove(target_file)  # 删除文件
            else:
                print(f"Passed: {target_file}")  # 文件存在，无需删除

        for dir in dirs:
            # 构造源子目录和目标子目录的完整路径
            source_subdir = os.path.join(source_dir, os.path.relpath(root, target_dir), dir)
            target_subdir = os.path.join(root, dir)

            # 如果源目录中没有对应的子目录，则删除目标子目录及其内容
            if not os.path.exists(source_subdir):
                print(f"Deleting: {target_subdir}")
                shutil.rmtree(target_subdir)  # 删除整个目录树
            else:
                print(f"Passed: {target_subdir}")  # 子目录存在，无需删除

# 定义源目录和目标目录
source_folder = 'd:\\'  # 源目录（要备份的目录）
target_folder = 'e:\\ddd\\'  # 目标目录（备份到哪里）

# 调用比较并删除文件的函数
compare_and_delete(source_folder, target_folder)


