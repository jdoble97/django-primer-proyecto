class Person(object):
    def __init__(self, name, last_name):
        self.__name = name
        self.last_name= last_name
    def get_name(self):
        return self.__name