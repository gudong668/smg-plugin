# coding=utf-8
import os
import json
import codecs
import requests
from resource_management import *
from resource_management.core.logger import Logger
from setup_utils import split_packages, get_package, decompression, rm_package
from file_utils import link, file, directory, copy, remove, replace, rename, chmod
class Master(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print "======Binginning install Smg Flinker ...======"
        self.install_packages(env)
        Execute('echo {0} | xargs wget -P {1}'.format(params.flinker_url, params.smg_install_dir), user=params.user,
                ignore_failures=True)
        package_dir = os.path.join(params.smg_install_dir, params.flinker_conf_name)
        Execute('unzip {0} -d {1}'.format(package_dir, params.smg_install_dir), user=params.user, ignore_failures=True)
        # Execute('mv {0}/kafka-manager-1.3.3.16 {1}'.format(params.smg_install_dir, params.install_dir), user=params.user,
        #         ignore_failures=True)
        Execute('rm -rf {0}'.format(package_dir), user=params.user, ignore_failures=True)
        self.configure(env)
        print "====== Install SMG finished!======"



    def configure(self, env):
        import params
        env.set_params(params)
        print "======Bingining configure Smg Flinker ...======"
        filed = self.encryption(env)
        File(os.path.join(params.flinker_conf, "admin.properties"),
             mode=0755,
             content=InlineTemplate(filed),
             owner=params.smg_user,
             group=params.smg_group
             )

        print "Configure Smg Flinker Finished!"


    def start(self, env):
        import params
        env.set_params(params)
        print "======Binginning start Smg Flinker ...======"
        self.configure(env)
        cmd = "sh {0}/startup.sh".format(params.flinker_bin)
        print cmd,'--------------------------------------------'
        Execute(cmd, user=params.smg_user, ignore_failures=True)
        Logger.info("execute {0}".format(cmd))
        print "======Start  Smg Flinker Service status finished======"


    def stop(self, env):
        import params
        env.set_params(params)
        print "======Binginning stop Smg Flinker ...======"
        cmd = 'sh {0}/stop.sh'.format(params.flinker_bin)
        Execute(cmd, user=params.smg_user, ignore_failures=True)
        Logger.info("execut {0}".format(cmd))
        print "======Stop Smg Flinker finished======"



    def status(self, env):
        import status_params
        env.set_params(status_params)
        print "======check  Smg Flinker status ...======"
        # use built-in method to check status using pidfile
        check_process_status(status_params.flinker_pid)
        print "======check  Smg Flinker status finished======"


    def encryption(self,env):
        import params
        env.set_params(params)
        print "======encryption SMG Flinker-config.....============"
        d = params.flinker_application
        s = d.split("\n")
        print s,'---------------------------------------------------------------------'
        dd = s[6].split("=")
        l = dd[1]
        url = "http://10.1.0.237:8080/encrypt?str=" + str(l)
        s = requests.get(url)
        a = dd [0] + "=" + s.json()
        en = s[1]+'/n'+s[2]+'/n'+s[3]+'/n'+s[4]+'/n'+s[5]+'/n'+s[7]+'/n'+a
        return en





if __name__ == "__main__":
    Master().execute()
