# -*- coding: UTF-8 -*-
# 运行环境：Python 3.8（为兼容 Windows 7 及 Windows 2008 系统）
# 作者邮箱：chaoxian102@gmail.com
# 微信：chaoxian102（超弦102）
# 支付宝：abtrue@hotmail.com
# Paypal：https://paypal.me/abtruecom
# 感谢打赏


import os
import shutil
import datetime

# 文件备份函数
# 将源目录中的文件备份到目标目录
# 如果源文件比目标文件更新，将更新备份
# 如果目标文件不存在，则创建目标文件存放路径

def backup_files(source_dir, target_dir):
    # 遍历源目录与子目录中的文件
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # 生成源文件和目标文件的路径
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_dir, os.path.relpath(source_file, source_dir))

            # 如果目标文件存在，检查两者是否需要更新
            if os.path.exists(target_file):
                # 获取源文件和目标文件的最后修改时间
                source_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(source_file))
                target_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(target_file))

                # 如果源文件比目标文件新，则更新备份
                if source_mod_time > target_mod_time:
                    print(f"Backing up {source_file} to {target_file}")
                    shutil.copy2(source_file, target_file)
                else:
                    # 如果目标文件无需更新，则略过
                    print(f"Ignoring {source_file} as it's not modified")
            else:
                # 如果目标文件不存在，则创建目标子文件夹，并备份源文件
                target_subfolder = os.path.dirname(target_file)
                os.makedirs(target_subfolder, exist_ok=True)  # 确保目标文件夹存在
                print(f"Backing up {source_file} to {target_file}")
                shutil.copy2(source_file, target_file)  # 备份文件

# 设置源文件夹和目标文件夹
source_directory = "d:/"  # 源文件夹（要备份的目录）
target_directory = "e:/ddd/"  # 目标文件夹（备份到哪里）

# 执行文件备份操作
backup_files(source_directory, target_directory)

