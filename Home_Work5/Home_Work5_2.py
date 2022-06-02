class User():
    def __init__(self,name : str, surname : str, year_of_birth : int, city : str, hobby : str):
        """информация про человека"""
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
        self.city = city
        self.hobby = hobby
    def print_info(self):
        """вывод данных про человека"""
        print("Имя:", self.name)
        print("Фамилия:", self.surname)
        print("Возраст:", 2022 - self.year_of_birth)
        print("Город:",self.city)
        print("Хобби:", self.hobby)
        print(" ")
human1 = User("Иван", "Шишкин", 1988, "Волгоград", "Охота")
human2 = User("Екатерина", "Никонорова", 1999, "Учалы", "Чтение литературы")
human1.print_info()
human2.print_info()


    
