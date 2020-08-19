#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import shutil
def link(src, target):
    if not os.path.exists(src):
        directory(src)
    os.symlink(src, target)
def copy(src, target):
    if not os.path.exists(target):
        os.makedirs(target, 0o755)
    if os.path.isfile(src):
        name = src.path.split("/")[-1]
        open(os.path.join(target, name), "wb").write(open(src, "rb").read())
    for file in os.listdir(src):
        sourceFile = os.path.join(src, file)
        targetFile = os.path.join(target, file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(target):
                os.makedirs(target)
            if not os.path.exists(targetFile) or (
                    os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
        if os.path.isdir(sourceFile):
            First_Directory = False
            copy(sourceFile, targetFile)
def directory(dir, mode=0o755):
    if not os.path.exists(dir):
        os.makedirs(dir, mode)
    else:
        os.chmod(dir, mode)
def file(file, mode=0o644):
    index = file.rindex("/")
    name = file[0:index]
    if not os.path.exists(name):
        os.mkdir(name)
    if not os.path.exists(file):
        open(file, "w")
        os.mknod(file, mode)
    else:
        os.chmod(file, mode)
def rename(old, new):
    if os.path.exists(new):
        if os.path.isfile(new):
            os.remove(new)
        else:
            shutil.rmtree(new)
    if not os.path.exists(old):
        print "目录或者文件不存在"
    else:
        if os.path.isfile(old) or os.path.isdir(old):
            os.renames(old, new)
        else:
            print "文件名不合法"
def remove(path):
    if os.path.exists(path):
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        else :
            print "暂不支持删除该类型目录或文件"
    else:
        print "目录或文件不存在"
def replace(name, old, new):
    return name.replace(old, new)
def chmod(path, mode=0o755):
    os.chmod(path, mode)
