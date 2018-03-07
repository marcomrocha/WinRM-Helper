import winrm
class winrm_session:
    global session
    def __init__(self, host_name, user_name, user_password):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.session = winrm.Session(host_name, auth=(user_name, user_password))



run = winrm_session('192.168.130.129', '\Marco Mendez', 'Control123')

print('********************** Environment variable *************************')
commandEnv = 'Get-ChildItem Env:'
print(run.session.run_ps(commandEnv)).std_out


print('*********************** Configuration IP ************************')
print(run.session.run_cmd('ipconfig', ['/all'])).std_out


print('*********************** Configuration HostName ************************')
commandHostName = 'nbtstat -a 192.168.130.129'
print(run.session.run_ps(commandHostName)).std_out