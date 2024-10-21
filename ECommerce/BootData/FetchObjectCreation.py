from PythonUniverse.ECommerce.BootData.ListConventer import List_Converter


class Entity_Data:
    @classmethod
    def get_laptop(cls, path) -> list:
        file = open(path + 'Laptop.txt', 'r')
        items = file.readlines()
        return List_Converter.laptop_converter(items)

    @classmethod
    def get_bluetooth(cls, path) -> list:
        file = open(path + 'Bluetooth.txt', 'r')
        items = file.readlines()
        return List_Converter.bluetooth_converter(items)

    @classmethod
    def get_speaker(cls, path) -> list:
        file = open(path + 'Speaker.txt', 'r')
        items = file.readlines()
        return List_Converter.speaker_converter(items)

    @classmethod
    def get_mouse(cls, path) -> list:
        file = open(path + 'Mouse.txt', 'r')
        items = file.readlines()
        return List_Converter.mouse_converter(items)

    @classmethod
    def get_keyboard(cls, path) -> list:
        file = open(path + 'Keyboard.txt', 'r')
        items = file.readlines()
        return List_Converter.keyboard_converter(items)

