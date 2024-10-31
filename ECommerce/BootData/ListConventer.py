from PythonUniverse.ECommerce.Entity.Speaker import Speaker
from PythonUniverse.ECommerce.Entity.Mouse import Mouse
from PythonUniverse.ECommerce.Entity.Bluetooth import Bluetooth
from PythonUniverse.ECommerce.Entity.KeyBoard import KeyBoard
from PythonUniverse.ECommerce.Entity.Laptop import Laptop

'''
    Attributes:
        No Instance Attributes
        No Class Attributes
        
    This Class Responsible for converting data into list of objects..
    Each Category has own method.
    It will receive single data.
    It will split each line as one entity.
    It will the attributes based on space and convert them as a attributes.
    It will Create a object for the particular category..
'''

class List_Converter:

    """
        Parameters:
              items -> data where all entity are stored
              Each line data represents a entity.
        Returns:
             list -> It will return list of objects belongs to laptop class

        It will read the data line by line.
        Each line is entity and its attributes are  separated by space.
        Iterated the data using for loop.
        Using split method attributes are obtained.
        Laptop category object created, and it was appended to the list.
        At final list will be returned.
    """

    @classmethod
    def laptop_converter(cls, items) -> list:
        list_of_laptops = []
        for item in items:
            attributes = item.strip().split(' ')
            laptop = Laptop(attributes[0], int(attributes[1]), float(attributes[2]), attributes[3], attributes[4], attributes[5], attributes[6])
            list_of_laptops.append(laptop)
        return list_of_laptops

    """
            Parameters:
                  items -> data where all entity are stored 
                  Each line data represents a entity.
            Returns:
                 list -> It will return list of objects belongs to bluetooth class

            It will read the data line by line.
            Each line is entity and its attributes are  separated by space.
            Iterated the data using for loop.
            Using split method attributes are obtained.
            Bluetooth category object created, and it was appended to the list.
            At final list will be returned.
        """

    @classmethod
    def bluetooth_converter(cls, items) -> list:
        list_of_bluetooth = []
        for item in items:
            attributes = item.strip().split(' ')
            bluetooth = Bluetooth(attributes[0], int(attributes[1]), float(attributes[2]), attributes[3], attributes[4], attributes[5])
            list_of_bluetooth.append(bluetooth)
        return list_of_bluetooth

    """
            Parameters:
                  items -> data where all entity are stored 
                  Each line data represents a entity.
            Returns:
                 list -> It will return list of objects belongs to keyboard class

            It will read the data line by line.
            Each line is entity and its attributes are  separated by space.
            Iterated the data using for loop.
            Using split method attributes are obtained.
            KeyBoard category object created, and it was appended to the list.
            At final list will be returned.
    """
    @classmethod
    def keyboard_converter(cls, items) -> list:
        list_of_keyboard = []
        for item in items:
            attributes = item.strip().split(' ')
            keyboard = KeyBoard(attributes[0], int(attributes[1]), float(attributes[2]), attributes[3])
            list_of_keyboard.append(keyboard)
        return list_of_keyboard

    """
            Parameters:
                  items -> data where all entity are stored 
                  Each line data represents a entity.
            Returns:
                 list -> It will return list of objects belongs to Mouse class

            It will read the data line by line.
            Each line is entity and its attributes are  separated by space.
            Iterated the data using for loop.
            Using split method attributes are obtained.
            Mouse category object created, and it was appended to the list.
            At final list will be returned.
    """
    @classmethod
    def mouse_converter(cls, items) -> list:
        list_of_mouse = []
        for item in items:
            attributes = item.strip().split(' ')
            mouse = Mouse(attributes[0], int(attributes[1]), float(attributes[2]), attributes[3], attributes[4], attributes[5], attributes[6])
            list_of_mouse.append(mouse)
        return list_of_mouse

    """
            Parameters:
                  items -> data where all entity are stored 
                  Each line data represents a entity.
            Returns:
                 list -> It will return list of objects belongs to Speaker class

            It will read the data line by line.
            Each line is entity and its attributes are  separated by space.
            Iterated the data using for loop.
            Using split method attributes are obtained.
            Speaker category object created, and it was appended to the list.
            At final list will be returned.
        """
    @classmethod
    def speaker_converter(cls, items) -> list:
        list_of_speaker = []
        for item in items:
            attributes = item.strip().split(' ')
            speaker = Speaker(attributes[0], int(attributes[1]), float(attributes[2]), attributes[3], attributes[4], attributes[5])
            list_of_speaker.append(speaker)
        return list_of_speaker
