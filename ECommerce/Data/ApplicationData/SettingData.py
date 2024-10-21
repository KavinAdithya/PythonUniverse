from PythonUniverse.ECommerce.Feature.ViewAvailabilty import Feature


class SettingData:
    dictionary : dict = Feature.dictionary
    path = 'A:/Python/PycharmProjects/PythonUniverse/ECommerce/Data/AppData/'

    @classmethod
    def store(cls, category):
        items = cls.dictionary[category]
        file = open(cls.path + category +'.txt', 'w')

        if category == 'laptop':
            cls.__laptop_data(file, items)
        elif category == 'bluetooth':
            cls.__bluetooth_data(file, items)
        elif category == 'keyboard':
            cls.__keyboard_data(file, items)
        elif category == 'mouse':
            cls.__mouse_data(file, items)
        else:
            cls.__speaker_data(file, items)


    @classmethod
    def __laptop_data(cls,file, laptops : list) :
        for lap in laptops:
            item_data : str  = (lap.name + ' '+
                        str(lap.quantity) + ' ' +
                        str(lap.price) + ' ' +
                        lap.brand + ' ' +
                        str(lap.main_memory) + ' ' +
                        lap.processor + ' ' +
                        str(lap.secondary_storage)) + '\n'
            file.write(item_data)

    @classmethod
    def __bluetooth_data(cls, file, bluetooth):
        for blue in bluetooth:
            item_data = (blue.name + ' '+
                        str(blue.quantity) + ' ' +
                        str(blue.price) + ' ' +
                        blue.brand + ' ' +
                        str(blue.range) + ' ' +
                        blue.codec_support) + '\n'
            file.write(item_data)

    @classmethod
    def __keyboard_data(cls, file, keyBoard):
        for key in keyBoard:
            item_data = (key.name + ' '+
                        str(key.quantity) + ' ' +
                        str(key.price) + ' ' +
                        key.brand) + '\n'
            file.write(item_data)

    @classmethod
    def __mouse_data(cls, file, mouse):
        for mou in mouse:
            item_data = (mou.name + ' '+
                        str(mou.quantity) + ' ' +
                        str(mou.price) + ' ' +
                        mou.brand + ' ' +
                        mou.DOI + ' ' +
                        str(mou.polling_rate) + ' ' +
                        str(mou.isErgonomics)) + '\n'
            file.write(item_data)

    @classmethod
    def __speaker_data(cls, file, speaker: list) :
        for speak in speaker:
            item_data = (speak.name + ' '+
                        str(speak.quantity) + ' ' +
                        str(speak.price) + ' ' +
                        speak.brand + ' ' +
                        speak.driver + ' ' +
                        speak.connectivity) + '\n'
            file.write(item_data)
    @classmethod
    def store_data(cls):
            cls.store('laptop')
            cls.store('bluetooth')
            cls.store('keyboard')
            cls.store('speaker')
            cls.store('mouse')