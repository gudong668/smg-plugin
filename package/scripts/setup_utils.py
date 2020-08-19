#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
from resource_management.core.resources.system import Execute
from resource_management.core.logger import Logger
"""
以symbol为分割，切割字符串
"""
def split_packages(packages, symbol):
    if len(packages) > 0:
        return packages.split(symbol)
"""
从远程获取package包放在本地指定目录下
"""
def get_package(target, package):
    if ping(package) == "OK":
        if os.path.exists(target):
            cmd = 'wget -P {0} {1}'.format(target, package)
            Execute(cmd, user='root')
            Logger.info(cmd)
"""
解压base_dir目录下的tar到target目录下
base_dir 源目录
packages 源目录下的多个tar包
target 解压的目标目录
"""
def decompression(base_dir, packages, target):
    if os.path.exists(base_dir):
        os.chdir(base_dir)
        for package in packages:
            full_path = os.path.join(base_dir, package)
            if os.path.exists(full_path):
                cmd = "tar -zxvf {0} -C {1}".format(full_path, target)
                Execute(cmd, user='root')
                Logger.info(cmd)
    else:
        print 'directory {0} not exist'.format(base_dir)
"""
获取url中ip，并测试port是否可以可用
"""
def ping(repo_url):
    import socket
    host, port = get_net(repo_url)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((host, port))
        print '{0} port {1} is open'.format(host, port)
        return "OK"
    except Exception as err:
        print '{0} port {1} is not open'.format(host, port)
        return "ERROR"
    finally:
        server.close()
"""
根据url获取ip和port
"""
def get_net(url):
    import urllib
    proto, rest = urllib.splittype(url)
    host, rest = urllib.splithost(rest)
    host, port = urllib.splitport(host)
    if port is None:
        port = 80
    return host, port
"""
删除base_dir目录下的packages
"""
def rm_package(base_dir, packages):
    for package in packages:
        full_path = os.path.join(base_dir, package)
        if os.path.exists(full_path):
            os.remove(full_path)
            Logger.info("remove package {0}".format(full_path))
