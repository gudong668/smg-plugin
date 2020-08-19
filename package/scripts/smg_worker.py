# coding=utf-8
import os
from resource_management import *
from resource_management.core.logger import Logger
from setup_utils import split_packages, get_package, decompression, rm_package
from file_utils import link, file, directory, copy, remove, replace, rename, chmod
class Master(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print "======Binginning install Smg Worker ...======"
        self.install_packages(env)
        Execute('echo {0} | xargs wget -P {1}'.format(params.worker_url, params.smg_install_dir), user=params.user,
                ignore_failures=True)
        package_dir = os.path.join(params.smg_install_dir, params.worker_conf_name)
        Execute('unzip {0} -d {1}'.format(package_dir, params.smg_install_dir), user=params.user, ignore_failures=True)
        Execute('rm -rf {0}'.format(package_dir), user=params.user, ignore_failures=True)
        self.configure(env)
        print
        "====== Install SMG finished!======"


    def configure(self, env):
        import params
        env.set_params(params)
        print "======Bingining configure Smg Dashboard ...======"
        File(os.path.join(params.worker_conf, "worker.properties"),
             mode=0755,
             content=InlineTemplate(params.worker_application),
             owner=params.smg_user,
             group=params.smg_group
             )

        File(os.path.join(params.worker_conf, "datasource.properties"),
             mode=0755,
             content=InlineTemplate(params.worker_application_db),
             owner=params.smg_user,
             group=params.smg_group
             )
        print "Configure Smg Dashboard Finished!"

    def start(self, env):
        import params
        env.set_params(params)
        print "======Binginning start Smg Worker ...======"
        self.configure(env)
        cmd = "sh {0}/startup.sh".format(params.worker_bin)
        Execute(cmd, user=params.smg_user, ignore_failures=True)
        Logger.info("execute {0}".format(cmd))
        print
        "======Start  Smg Worker Service status finished======"

    def stop(self, env):
        import params
        env.set_params(params)
        print "======Binginning stop Smg Worker ...======"

        cmd = 'sh {0}/stop.sh'.format(params.worker_bin)
        Execute(cmd, user=params.smg_user, ignore_failures=True)
        Logger.info("execut {0}".format(cmd))
        print
        "======Stop Smg Worker finished======"

    def status(self, env):
        import status_params
        env.set_params(status_params)
        print "======check  Smg Worker status ...======"
        # use built-in method to check status using pidfile
        print status_params.worker_pid, '//////////////////////////////////////////////////////'
        check_process_status(status_params.worker_pid)
        print
        "======check  Smg Worker status finished======"




if __name__ == "__main__":
    Master().execute()
