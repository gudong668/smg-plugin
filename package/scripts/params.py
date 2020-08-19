# coding=utf-8
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
Ambari Agent
"""
import os
import json
from resource_management.libraries.script import Script
from resource_management.libraries.functions import format
from resource_management.libraries.functions.default import default
from resource_management.libraries.functions.version import compare_versions, format_stack_version
config = Script.get_config()
smg_user = config['configurations']['smg-env']['smg_user']
smg_group = config['configurations']['smg-env']['smg_group']


# smg_group = config['configurations']['smg-env']['smg_group']
http_port = config['configurations']['smg-env']['http_port']

# base_dir = config['configurations']['smg-env']['base_dir']


stack_root = config['configurations']['cluster-env']['stack_root']     #路径
current_version = config['hostLevelParams']['current_version']         #版本号
base_dir = os.path.join(stack_root,current_version)
component_name = 'smg'
smg_install_dir = os.path.join(base_dir,component_name)


java_home = config['hostLevelParams']['java_home']
manager_conf_name = "manager.zip"
worker_conf_name = "worker.zip"
flinker_conf_name = "flinker.zip"
flinker_name = "flinker"
manager_name = "manager"
worker_name = "worker"
# base_d = config['configurations']['smg-env']['base_d']
# install_dir = config['configurations']['manager-env']['package_name']
user = config['configurations']['smg-env']['smg_user']
# yum repo download url
# repo_info = default("/hostLevelParams/repo_info",None)
# repo_url = json.loads(repo_info)[0]["baseUrl"]
json_string = default("/hostLevelParams/repo_info",None)
str_json = json.loads(json_string)
manager_url = str_json[0]['baseUrl']+'smg/'+manager_conf_name
worker_url = str_json[0]['baseUrl']+'smg/'+worker_conf_name
flinker_url = str_json[0]['baseUrl']+'smg/'+flinker_conf_name
# download_url = "/sdp/Seabox-SDP-2.5/smg/smg.zip"

# smg service db configurations
datasource_driverClassName = config['configurations']['smg-common']['datasource.driverClassName']
datasource_url = config['configurations']['smg-common']['datasource.url']
datasource_username = config['configurations']['smg-common']['datasource.username']
datasource_password = config['configurations']['smg-common']['datasource.password']
# smg service dubbo configurations
# smg_service_dubbo_container = config['configurations']['smg-env']['smg_service_dubbo_container']
# smg_service_dubbo_spring_config = config['configurations']['smg-env']['smg_service_dubbo_spring_config']
# smg_service_dubbo_app_name = config['configurations']['smg-env']['smg_service_dubbo_app_name']
# smg_service_dubbo_protocol_port = config['configurations']['smg-env']['smg_service_dubbo_protocol_port']
# smg_service_dubbo_registry_address = config['configurations']['smg-env']['smg_service_dubbo_registry_address']
# smg flinker configurations
datax_admin_zkServers = config['configurations']['flinker-config']['datax.admin.zkServers']
datax_admin_dbconfig_address = config['configurations']['flinker-config']['datax.admin.dbconfig.address']
datax_admin_dbconfig_port = config['configurations']['flinker-config']['datax.admin.dbconfig.port']
datax_admin_schema = config['configurations']['flinker-config']['datax.admin.schema']
datax_admin_dbconfig_username = config['configurations']['flinker-config']['datax.admin.dbconfig.username']
datax_admin_dbconfig_password = config['configurations']['flinker-config']['datax.admin.dbconfig.password']
datax_admin_rest_server_port = config['configurations']['flinker-config']['datax.admin.rest.server.port']
# flinker_conf = config['configurations']['flinker-config']['smg_flinker_dir']




# flinker_conf1 = config['configurations']['worker-config-env']['smg_group']


# smg manager configurations
port = config['configurations']['manager-config']['port']
http_port = config['configurations']['manager-config']['http.port']
zookeeper_servers = config['configurations']['manager-config']['zookeeper.servers']
currentEnv = config['configurations']['manager-config']['currentEnv']
monitor_check_intervalTime = config['configurations']['manager-config']['monitor.check.intervalTime']
multiplexingRead = config['configurations']['manager-config']['multiplexingRead']
flinker_job_min_jvmMemory = config['configurations']['manager-config']['flinker.job.min.jvmMemory']
flinker_job_max_jvmMemory = config['configurations']['manager-config']['flinker.job.max.jvmMemory']
# manager_conf = config['configurations']['manager-config']['smg_manager_dir']

# smg worker configurations
bootstrap_servers = config['configurations']['worker-config']['bootstrap.servers']
zookeeper_servers = config['configurations']['worker-config']['zookeeper.servers']
zookeeper_session_timeout_ms = config['configurations']['worker-config']['zookeeper.session.timeout.ms']
zookeeper_connection_timeout_ms = config['configurations']['worker-config']['zookeeper.connection.timeout.ms']
zookeeper_root = config['configurations']['worker-config']['zookeeper.root']
worker_bootMode = config['configurations']['worker-config']['worker.bootMode']
worker_probe_blackList = config['configurations']['worker-config']['worker.probe.blackList']
client_id = config['configurations']['worker-config']['client.id']
classloader_type = config['configurations']['worker-config']['classloader.type']
# worker_conf = config['configurations']['worker-config']['smg_worker_dir']
# dashboard_application = config["configurations"]["manager-db"]["db"]
# dashboard_log4j = config["configurations"]["dashboard-config"]["log4j"]
# service_db = config["configurations"]["service-config"]["db"]
# service_dubbo = config["configurations"]["service-config"]["dubbo"]
# service_log4j = config["configurations"]["service-config"]["log4j"]
# node_application = config["configurations"]["node-config"]["application"]
# node_log4j = config["configurations"]["node-config"]["log4j"]

# datasource_driverClassName = config['configurations']['smg-env']['datasource.driverClassName']
# datasource_url = config['configurations']['smg-env']['datasource.url']
# datasource_username = config['configurations']['smg-env']['datasource.username']
# datasource_password = config['configurations']['smg-env']['datasource.password']
#
# print datasource_driverClassName,'+++++++++++++++++++++*********************************'

# dashboard_dir = os.path.join(base_d, "dl-{0}".format(flinker_name))
# service_dir = os.path.join(base_d, "dl-{0}".format(manager_name))
# node_dir = os.path.join(base_d, "dl-{0}".format(worker_name))
# print dashboard_dir,'0000000000000000000000000000000000000000000000000'
# """
# /usr/hdp/2.5.0.0-1245/smg/dl-flinker 0000000000000000000000000000000000000000000000000
# """
# /usr/hdp/2.5.0.0-1245/smg/dl-flinker/bin
# flinker_bin = config['configurations']['smg-env']['smg_flinker_bin_dir']
# manager_bin = config['configurations']['smg-env']['smg_manager_bin_dir']
# worker_bin = config['configurations']['smg-env']['smg_worker_bin_dir']
flinker_bin = smg_install_dir + "/dl-{}".format(flinker_name) + '/bin'
manager_bin = smg_install_dir + "/dl-{}".format(manager_name) + '/bin'
worker_bin = smg_install_dir + "/dl-{}".format(worker_name) + '/bin'



manager_conf= smg_install_dir + "/dl-{}".format(manager_name) + '/conf'
worker_conf = smg_install_dir + "/dl-{}".format(worker_name) + '/conf'
flinker_conf = smg_install_dir + "/dl-{}".format(flinker_name) + '/conf'


flinker_pid = flinker_bin + '/flinker.pid'
manager_pid = manager_bin + '/manager.pid'
worker_pid = worker_bin + '/worker.pid'



# datasource_driverClassName =  config['configurations']['smg-env']['datasource.driverClassName']
# datasource_url =  config['configurations']['smg-env']['datasource.url']
# datasource_username =  config['configurations']['smg-env']['datasource.username']
# datasource_password =  config['configurations']['smg-env']['datasource.password']

# flinker_pid = config['configurations']['smg-env']['smg_flinker_pid_dir']
# manager_pid = config['configurations']['smg-env']['smg_manager_pid_dir']
# worker_pid = config['configurations']['smg-env']['smg_worker_pid_dir']
#
# print manager_pid,'+++++++++++++++++++++++++++++++++++++++++++++++++'
# smg_flinker_bin_dir
# """
# /bin ------------------------------------
# """
# #
# manager_bin = os.path.join(service_dir, "bin")
# worker_bin = os.path.join(node_dir, "bin")
flinker_application = config["configurations"]["flinker-config"]["flinker-config"]
manager_application = config["configurations"]["manager-config"]["manager-config"]
manager_application_db = config["configurations"]["manager-db"]["manager-db"]
worker_application = config["configurations"]["worker-config"]["worker-config"]
worker_application_db = config["configurations"]["worker-db"]["worker-db"]