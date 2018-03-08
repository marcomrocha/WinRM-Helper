import winrm

from vm_classes.vm_window_7 import vm_window_7
import json

class winrm_session:
    global session
    def __init__(self,Ivm):
        self.host_name = Ivm.get_host_name()
        self.user_name = Ivm.get_user_name()
        self.user_password = Ivm.get_user_password()
        self.session = winrm.Session(self.host_name, auth=(self.user_name, self.user_password))

    def get_ipconfig_all(self):
        print('*********************** IP Configuration  ************************')
        return self.session.run_cmd('ipconfig', ['/all']).std_out


    def get_environment_variable(self):
        print('******************** Environment variable ************************')
        commandEnv = 'Get-ChildItem Env:'
        return self.session.run_ps(commandEnv).std_out

    def get_configuration_hostname(self):
        print('********************* Configuration HostName *********************')
        commandHostName = 'nbtstat -a 192.168.130.129'
        return self.session.run_ps(commandHostName).std_out

    def get_execution_policy(self):
        print('********************* Get ExecutionPolicy *********************')
        return self.session.run_ps('get-executionpolicy').std_out



    def set_execution_policy_to_unrestrict(self):
        print('********************* Configuration HostName *********************')
        code_status = self.session.run_ps('set-executionpolicy Unrestricted').status_code
        return "Successful" if code_status == 0 else "error"


    def set_execution_policy_to_restrict(self):
        print('********************* Configuration HostName *********************')
        code_status = self.session.run_ps('set-executionpolicy restricted').status_code
        return "Successful" if code_status == 0 else "error"

    def run_ps_scripts(self, path):
        print('********************* Configuration HostName *******************d**')
        return self.session.run_ps(path).std_out








win7 = vm_window_7('192.168.130.129', '\Marco Mendez', 'Control123')
win8 = vm_window_7('192.168.130.129', '\Marco Mendez', 'Control123')

winrm = winrm_session(win8)
print(winrm.host_name)
print(winrm.user_name)
print(winrm.user_password)






m = winrm.get_ipconfig_all()
n = json.dumps(m)
o = json.loads(n)
print '*************************************'
print o
print '*************************************'