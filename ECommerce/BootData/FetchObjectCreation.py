from PythonUniverse.ECommerce.BootData.ListConventer import List_Converter

''' 
    Attributes:
        No Instance Attributes
        No Class Attributes
        
    This class Responsible for fetching data from files using path as parameter.
    Each category has own text file and own method to do operation on it.
    It will Invoke particular Object Converter data to actual list converter.
    List_Converter Class method of category converter.
    It will return the list of objects belongs to the category.
    Here it will return the list to the invoker... 
'''
class Entity_Data:
    """
        Parameters:
            path ->  Path for laptop file.
        Returns:
            list -> It will return the list of laptop category Objects.
        Here it will read the data completely from laptop.txt file.
        It will Invoke List_Converter class method of laptop_converter and pass the data.
        laptop_converter converts the data into laptop category objects..
        It will convert it into list.
    """
    @classmethod
    def get_laptop(cls, path) -> list:
        file = open(path + 'Laptop.txt', 'r')
        items = file.readlines()
        return List_Converter.laptop_converter(items)

    """
        Parameters:
            path ->  Path for bluetooth file.
        Returns:
            list -> It will return the list of bluetooth category Objects.
        Here it will read the data completely from bluetooth.txt file.
        sIt will Invoke List_Converter class method of bluetooth_converter and pass the data.
        laptop_converter converts the data into bluetooth category objects..
        It will convert it into list.
    """
    @classmethod
    def get_bluetooth(cls, path) -> list:
        file = open(path + 'Bluetooth.txt', 'r')
        items = file.readlines()
        return List_Converter.bluetooth_converter(items)

    """
          Parameters:
              path ->  Path for speaker file.
          Returns:
              list -> It will return the list of speaker category Objects.
          Here it will read the data completely from speaker.txt file.
          It will Invoke List_Converter class method of speaker_converter and pass the data.
          laptop_converter converts the data into speaker category objects..
          It will convert it into list.
      """
    @classmethod
    def get_speaker(cls, path) -> list:
        file = open(path + 'Speaker.txt', 'r')
        items = file.readlines()
        return List_Converter.speaker_converter(items)

    """
          Parameters:
              path ->  Path for mouse file.
          Returns:
              list -> It will return the list of mouse category Objects.
          Here it will read the data completely from mouse.txt file.
          It will Invoke List_Converter class method of mouse_converter and pass the data.
          laptop_converter converts the data into mouse category objects..
          It will convert it into list.
    """

    @classmethod
    def get_mouse(cls, path) -> list:
        file = open(path + 'Mouse.txt', 'r')
        items = file.readlines()
        return List_Converter.mouse_converter(items)

    """
          Parameters:
              path ->  Path for keyboard file.
          Returns:
              list -> It will return the list of keyboard category Objects.
          Here it will read the data completely from keyboard.txt file.
          It will Invoke List_Converter class method of keyboard_converter and pass the data.
          laptop_converter converts the data into keyboard category objects..
          It will convert it into list.
    """
    @classmethod
    def get_keyboard(cls, path) -> list:
        file = open(path + 'Keyboard.txt', 'r')
        items = file.readlines()
        return List_Converter.keyboard_converter(items)