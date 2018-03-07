
from class_example.Ivm import Ivm

class vm_window_7(Ivm):

    def __init__(self,host_name,user_name,user_password ):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password

        super(vm_window_7, self).__init__()



    def get_host_name(self):
        return self.host_name


    def get_user_name(self):
        return self.user_name


    def get_user_password(self):
        return self.user_password

