from ECommerce.Entity.Bluetooth import Bluetooth
from ECommerce.Entity.KeyBoard import KeyBoard
from ECommerce.Entity.Laptop import Laptop
from ECommerce.Entity.Mouse import Mouse
from ECommerce.Entity.Speaker import Speaker


class List_Converter:
    @classmethod
    def laptop_converter(cls, items) -> list:
        list_of_laptops = []
        for item in items:
            attributes = item.strip().split(' ')
            laptop = Laptop(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5], attributes[6])
            list_of_laptops.append(laptop)
        return list_of_laptops

    @classmethod
    def bluetooth_converter(cls, items) -> list:
        list_of_bluetooth = []
        for item in items:
            attributes = item.strip().split(' ')
            bluetooth = Bluetooth(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5])
            list_of_bluetooth.append(bluetooth)
        return list_of_bluetooth

    @classmethod
    def keyboard_converter(cls, items) -> list:
        list_of_keyboard = []
        for item in items:
            attributes = item.strip().split(' ')
            keyboard = KeyBoard(attributes[0], attributes[1], attributes[2], attributes[3])
            list_of_keyboard.append(keyboard)
        return list_of_keyboard

    @classmethod
    def mouse_converter(cls, items) -> list:
        list_of_mouse = []
        for item in items:
            attributes = item.strip().split(' ')
            mouse = Mouse(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5], attributes[6])
            list_of_mouse.append(mouse)
        return list_of_mouse

    @classmethod
    def speaker_converter(cls, items) -> list:
        list_of_speaker = []
        for item in items:
            attributes = item.strip().split(' ')
            speaker = Speaker(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5], attributes[6])
            list_of_speaker.append(speaker)
        return list_of_speaker
