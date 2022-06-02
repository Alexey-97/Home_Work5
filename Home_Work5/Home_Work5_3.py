class User():
    """Информация про человека"""
    def __init__(self,name : str, surname : str, year_of_birth : int, city : str, hobby : str):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
        self.city = city
        self.hobby = hobby

    def print_info(self,):
        """вывод данных человека"""
        print("Имя:", self.name)
        print("Фамилия:", self.surname)
        print("Возраст:", 2022 - self.year_of_birth)
        print("Город:",self.city)
        print("Хобби:", self.hobby)
        print(" ")

    def setName(self,n):
        """переопределение имени"""
        self.name = n

    def setSurname(self,s):
        """переопределение фамилии"""
        self.surname = s

    def setAge(self, y):
        """переопределение возраста"""
        self.year_of_birth = y

    def setCite(self, c):
        """переопределение города проживания"""
        self.city = c

    def setHobbu(self, h):
        """переопределение хобби"""
        self.hobby = h
        
human1 = User("Николай", "Ворсин", 1995, "Бийск", "рыбалка")
human1.print_info()

human1.setName("Ирина")
human1.setSurname("Тяпкина")
human1.setAge(1967)
human1.setCite("Москва")
human1.setHobbu("рисование")
human1.print_info()


