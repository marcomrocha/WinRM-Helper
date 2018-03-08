from abc import ABCMeta,abstractmethod


class Ivm(object):
    __metaclass__ = ABCMeta

    global host_name
    global user_name
    global user_password

    @abstractmethod
    def get_host_name(self): pass

    @abstractmethod
    def get_user_name(self): pass

    @abstractmethod
    def get_user_password(self): pass




