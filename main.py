import ctypes

lib = ctypes.CDLL("./lib.dll", winmode=0)


class LinkedList(object):
    def __init__(self):
        lib.init.argtypes = []
        lib.init.restype = ctypes.c_void_p

        lib.insert.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        lib.insert.restype = ctypes.c_void_p

        lib.pushHead.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.pushHead.restype = ctypes.c_void_p

        lib.pushBack.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.pushBack.restype = ctypes.c_void_p

        lib.pop.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.pop.restype = ctypes.c_void_p

        lib.popHead.argtypes = [ctypes.c_void_p]
        lib.popHead.restype = ctypes.c_void_p

        lib.popBack.argtypes = [ctypes.c_void_p]
        lib.popBack.restype = ctypes.c_void_p

        lib.lenght.argtypes = [ctypes.c_void_p]
        lib.lenght.restype = ctypes.c_int

        lib.get.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.get.restype = ctypes.c_int

        self.obj = lib.init()

    def insert(self, index: int, value: int):
        lib.insert(self.obj, index, value)

    def pushHead(self, value: int):
        lib.pushHead(self.obj, value)

    def pushBack(self, value: int):
        lib.pushBack(self.obj, value)

    def pop(self, index: int):
        lib.pop(self.obj, index)

    def popHead(self):
        lib.popHead(self.obj)

    def popBack(self):
        lib.popBack(self.obj)

    def lenght(self):
        lib.popBack(self.obj)

    def __len__(self):
        return lib.lenght(self.obj)

    def get(self, index: int):
        return lib.get(self.obj, index)


list = LinkedList()
list.pushHead(10)

v = list.get(0)
print("TEST:", v)
