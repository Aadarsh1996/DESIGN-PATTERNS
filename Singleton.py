class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args,**kwargs)
        return cls._instance[cls]
class Logger(metaclass=Singleton):
    def __init__(self):
        print("Creating logger..")

    def log(self,msg):
        print(msg)

class CustomLogger(Logger):
    def __init__(self):
        print("Creating custom logger")
        super(CustomLogger, self).__init__()

logger = CustomLogger()
logger2 = CustomLogger()
print(logger)
print(logger2)
logger.log(" First log  ")
logger.log(" Second log  ")

