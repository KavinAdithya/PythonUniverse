class BlueTooth:
    brandName = 'One Plus Nord Buds'
    budsCount = 2
    batteryBackUpHours = 12
    blueToothVersion = 1.23
    def __init__(self, years):
        self.batteryCapacityAvailable = BlueTooth.batteryBackUpHours / years

    def printBlueToothConfiguration(self):
        print("Brand : " , BlueTooth.brandName)
        print("BlueTooth Version : ", BlueTooth.blueToothVersion)
        print("Number Of Buds : ", BlueTooth.budsCount)
        print("On Manufactured Battery Back Up : " , BlueTooth.batteryBackUpHours)
        print("Now Battery Capacity Back Up : ", self.batteryCapacityAvailable)
    def __str__(self):
        return 'One Plus Nord Buds'
#
# blueTooth = BlueTooth(2)
# BlueTooth.year = 2005
#
# def getName(self):
#     print('Kavin_adithya')
# BlueTooth.getName = getName
#
# # print(BlueTooth.__dict__)
# blueTooth.getName()
#
# blue1 = BlueTooth(1)
#
# blue1.getName()
# blue1.name = 'Kavinnnnnn'
# print(blue1.year)
# # print(blueTooth.name)

# blueTooth.printBlueToothConfiguration()

def printName(self):
    print("Kavinn")

b = BlueTooth(1)

b.print = printName.__get__(b)

b.print()

