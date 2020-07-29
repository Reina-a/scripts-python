#!/usr/bin/env python3


import os
import time
import shutil
import argparse
import pyperclip
# 此模块地址: https://github.com/Reina-a/develop-tools-python/blob/master/path_convertor.py
import path_convertor as pc


# 预定义变量
tar_img_wsl_path, throw = pc.abs_win2wsl('C:\\Users\\Reina\\OneDrive\\Chirpy\\assets\\images\\', pc.FOLDER_MODE)
jek_img_url = '/assets/images/'

# 获取当前日期并格式化
formated_time = time.strftime("%Y-%m-%d", time.localtime())
tar_img_wsl_path += (formated_time + '/')
jek_img_url += (formated_time + '/')

# 检查目标路径是否存在, 若不存在则创建
if not os.path.exists(tar_img_wsl_path):
    os.makedirs(tar_img_wsl_path)

# 解析命令行参数

desc =  'Move picture(s) to your jekyll picture hub, and return the url you need for your site (print & clipboard)'
argument_parser = argparse.ArgumentParser(description=desc)
argument_parser.add_argument('-c','--disable-clipboard', dest='disable_clipboard', action='store_true',
                            help='do not change the clipboard')
argument_parser.add_argument('-r','--disable-rename', dest='disable_rename', action='store_true',
                            help='do not rename')
args = argument_parser.parse_args()

# 显示模式
if not args.disable_clipboard:
    print("- clipboard:\tenabled")
else:
    print("- clipboard:\tdisabled")

if not args.disable_rename:
    print("- rename:\tenabled")
else:
    print("- rename:\tdisabled")


# 循环输入图片路径
while True:
    src_img_win_path = input("Windows File Path: ")
    
    # 程序出口
    if src_img_win_path == 'quit':
        break

    # 将得到的windows路径转化为相应的wsl路径
    src_img_wsl_path, filename = pc.abs_win2wsl(src_img_win_path, pc.FILE_MODE)

    # 如果路径错误, 进入下个循环 (内置报错)
    if not src_img_wsl_path:
        print("")
        continue

    src_img_wsl_path += filename

    # 检查文件是否存在, 不存在则报错
    if not os.path.exists(src_img_wsl_path):
        print("File not exists, please check your input.")
        print("It is recommended to drag the file into the terminal directly.")
        print("")
        continue

    # 为路径补充文件名
    if args.disable_rename:
        tar_img_wsl_path += filename
        jek_img_url += filename
    else:
        new_filename = input("New filename: ")
        tar_img_wsl_path += new_filename    
        jek_img_url += new_filename
    
    # 打印jekyll所需的路径
    print(jek_img_url)
    
    if not args.disable_clipboard:
        # 把jekyll所需的路径复制到剪切板
        pyperclip.copy(jek_img_url)
        print("Copied to the clipboard!")

    # 移动图片文件到目标路径
    shutil.copy(src_img_wsl_path, tar_img_wsl_path)
    print("Moved!")
    print("")