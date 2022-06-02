
class User():
    """информация про человека"""
    name = ""
    surname = ""
    year_of_birth = 0
    city = ""
    hobby = ""   
human1 = User()
human1.name = "Иван"
human1.surname = "Шишкин"
human1.year_of_birth = 1988
human1.city = "Волгоград"
human1.hobby = "Охота" 

human2 = User()
human2.name = "Екатерина"
human2.surname = "Никонорова"
human2.year_of_birth = 1999
human2.city = "Учалы"
human2.hobby = "Чтение литературы"
print("Возраст 1-го объекта:",2022 - human1.year_of_birth,"года")
print("Возраст 2-го объекта:",2022 - human2.year_of_birth,"года")
