from utils.winrm.winrm_session import winrm_session
from vm_classes.vm_window_7 import vm_window_7

win7 = vm_window_7('192.168.130.129', '\Marco Mendez', 'Control123')
win8 = vm_window_7('192.168.130.129', '\Marco Mendez', 'Control123')

winrm = winrm_session(win8)
print(winrm.host_name)
print(winrm.user_name)
print(winrm.user_password)
print(winrm.get_environment_variable())
print(winrm.get_ipconfig_all())