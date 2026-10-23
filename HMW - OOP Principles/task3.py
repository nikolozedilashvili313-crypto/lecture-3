class SmartDevice:
    def __init__(self, brand):
        self.brand = brand
        self.__is_on = False 

    def turn_on(self):
        self.__is_on = True
        print(f"{self.brand} მოწყობილობა ჩართულია.")

    def turn_off(self):
        self.__is_on = False
        print(f"{self.brand} მოწყობილობა გამორთულია.")

    @property
    def is_on(self):
        return self.__is_on


class SmartLight(SmartDevice):
    def __init__(self, brand, brightness=50):
        super().__init__(brand)
        self.brightness = brightness 

    def turn_on(self):
        super().turn_on()
        print(f"ბრენდი: {self.brand}, სიკაშკაშე: {self.brightness}%")

light = SmartLight(brand="Xiaomi", brightness=80)
light.turn_on()
print(f"სტატუსი (is_on): {light.is_on}")

light.turn_off()
print(f"სტატუსი (is_on): {light.is_on}")