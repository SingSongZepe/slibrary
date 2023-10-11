
from typing import overload

class OVERLOAD:
    @overload
    def __init__(self):
        pass
    @overload
    def __init__(self, x: int):
        pass

    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            self.x = 0
        else:
            self.x = args[0]

class PASS:
    pass
    def __init__(self):
        pass

class THREEDOT:
    ...
    def __init__(self):
        ...

# if pass:
#     pass

if ...:
    ...

if __name__ == '__main__':
    ol1 = OVERLOAD()
    ol2 = OVERLOAD(1)

    print(ol1.x)
    print(ol2.x)
