class Registry:
    def __init__(self):
        self.__networks = {}

    def register(self, *names):
        def wrapper(cls):
            for n in names:
                self.__networks[n] = cls
            return cls
        return wrapper

    def get(self, name, default=None):
        return self.__networks.get(name, default)


registry = Registry()
