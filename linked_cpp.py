import ctypes


class CppIterator(object):
    def __init__(self, lib: ctypes.CDLL, it):
        self.lib = lib
        self.obj = it

    def __iter__(self):
        return self

    def __next__(self):
        if self.lib.is_finished(self.obj):
            raise StopIteration

        value = self.lib.get(self.obj)
        self.lib.next(self.obj)

        return value


class CppLinkedList(object):
    def __init__(self, lib: ctypes.CDLL):
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

        # Iterator functions
        lib.iter.argtypes = [ctypes.c_void_p]
        lib.iter.restype = ctypes.c_void_p

        lib.next.argtypes = [ctypes.c_void_p]
        lib.next.restype = ctypes.c_void_p

        lib.is_finished.argtypes = [ctypes.c_void_p]
        lib.is_finished.restype = ctypes.c_bool

        lib.get.argtypes = [ctypes.c_void_p]
        lib.get.restype = ctypes.c_int

        self.obj = lib.init()
        self.lib = lib

    def insert(self, index: int, value: int):
        self.lib.insert(self.obj, index, value)

    def pushHead(self, value: int):
        self.lib.pushHead(self.obj, value)

    def pushBack(self, value: int):
        self.lib.pushBack(self.obj, value)

    def pop(self, index: int):
        self.lib.pop(self.obj, index)

    def popHead(self):
        self.lib.popHead(self.obj)

    def popBack(self):
        self.lib.popBack(self.obj)

    def __len__(self) -> int:
        return self.lib.lenght(self.obj)

    def iter(self):
        return CppIterator(self.lib, self.lib.iter(self.obj))
