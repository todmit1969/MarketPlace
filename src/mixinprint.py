class MixinPrint:
    def __init__(self, *args, **kwargs):
        super().__init__()
        print(repr(self))

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, "
                f"{self.description}, {self.price}, {self.quantity})")