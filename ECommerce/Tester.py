from Entity import Laptop, KeyBoard, Bluetooth, Speaker, Mouse


laptop = Laptop.Laptop('Mega Book', 20, 45000.00, 'Techno', 32, "Intel I5", 1024)
print(laptop)

keyBoard = KeyBoard.KeyBoard('JackPot', 12, 1000.00, 'Dell')
print(keyBoard)

blueTooth = Bluetooth.Bluetooth('KaVin', 30, 2800.00, 'One Plus Nord Buds', 20, 'AAC')
print(blueTooth)

speaker = Speaker.Speaker('Smarter', 20, 10000.00, 'Samsung', 'tweeters, woofers', 'Bluetooth')
print(speaker)

mouse = Mouse.Mouse('Rat', 24, 1000.00, 'Dell', 'Heavy DOI', 1000, True)
print(mouse)