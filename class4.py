class Display:
    def __init__(self, pad, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pad = pad
        self.permission = "10.1-11"


class Battery:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.container = "11560мАч"


class RAM:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quantity = "128ГБ"


class Camera:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pixels = "8МП"


class Pad(Display, Battery, RAM, Camera):
    def print_info(self):
        print(self.permission)
        print(self.container)
        print(self.quantity)
        print(self.pixels)
        print(self.pad)


pad = Pad(pad="The newest")
pad.print_info()