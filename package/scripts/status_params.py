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
from resource_management.libraries.script import Script
config = Script.get_config()
pid_dir = "/var/run/smg"
# dashboard_pid = os.path.join(pid_dir, "dashboard.pid")
# service_pid = os.path.join(pid_dir, "service.pid")
# node_pid = os.path.join(pid_dir, "node.pid")
flinker_pid = config['configurations']['smg-env']['smg_flinker_pid_dir']
manager_pid = config['configurations']['smg-env']['smg_manager_pid_dir']
worker_pid = config['configurations']['smg-env']['smg_worker_pid_dir']