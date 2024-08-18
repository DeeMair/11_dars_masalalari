"""Boshlash"""

"""1.Masala"""

# shaxslar = [
#     {"ism": "Ali", "yosh": 17},
#     {"ism": "Vali", "yosh": 22},
#     {"ism": "Hasan", "yosh": 30},
#     {"ism": "Husan", "yosh": 16}
# ]
#
# natija = list(filter(lambda shaxs: shaxs["yosh"] > 18, shaxslar))
#
# print(natija)

"""2.Masala"""

# mahsulotlar = [
#     {"nomi": "Mahsulot1", "narx": 45},
#     {"nomi": "Mahsulot2", "narx": 55},
#     {"nomi": "Mahsulot3", "narx": 30},
#     {"nomi": "Mahsulot4", "narx": 70}
# ]
#
# natija = list(filter(lambda maxsulot: maxsulot["narx"] < 50, mahsulotlar))
# print(natija)


"""3.Masala"""

# def kichiklashtir(matn):
#     return matn.lower()
#
# print(kichiklashtir("SalOM dUNyo"))


"""4.Masala"""


# def tekari_qilish(gap):
#     return gap[::-1]
# matn = "Salom dunyo"
#
# print(tekari_qilish(matn))

"""5.Masala"""

# names = ["Ali", "Vali", "Hasan", "Husan"]
#
# with open("names.txt", "w") as file:
#     for name in names:
#         file.write(name + "\n")


"""6.Masala"""


# with open("data.txt","w") as file:
#     file.write("Wanna be yours\n")
#     file.write("Summertime\n")
#
# with open("data.txt", "r") as file:
#     for qator in file:
#         qator = qator.strip()
#         print(len(qator))


"""7.Masala"""
"""OOP"""


# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Salom, mening ismim {self.name} va men {self.age} yoshdaman."
#
#
# aziz = Person("Aziz", 25)
# print(aziz.greet())


"""8.Masala"""

# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return f"{math.pi * self.radius ** 2}" #bu yerdagi pi sonini math kutubxonasi orqali chaqirib oldim
#         # sababi shartida matematik qiymat soralgan ekan bunga GPTning aloqasi yoq buni ancha avval satrlar bilan ishlayotgan vaqtimizda o'rganganman
#
#
#
# doira = Circle(5)
# print(doira.area())


"""9.masala"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#
# gurbat = Student("G'urbatjon", 20, "birbalo001")
# print(f"Name: {gurbat.name}")
# print(f"Age: {gurbat.age}")
# print(f"Studentning IDsi: {gurbat.student_id}")


"""10.Masala"""

# class Employee:
#     def __init__(self,name, salary):
#         self.name = name
#         self.salary =salary
#
#     def give_raise(self):
#         self.salary *= 1.10
#
# class Manager(Employee):
#     def __init__(self,name, salary, department):
#         super().__init__(name,salary)
#         self.department = department
#
# class Developer(Employee):
#     def __init__(self,name, salary, programming_language):
#         super().__init__(name, salary)
#         self.programming_language= programming_language
#
# manager = Manager("BAxodir", 50000,"Savdo")
# developer= Developer("G'ani", 60000, "Python")
#
# print(f"Managerni ismi: {manager.name}")
# print(f"Managerni oyligi: {manager.salary}")
# print(f"Managerni bolimi: {manager.department}")
#
# print(f"dasturchini ismi: {developer.name}")
# print(f"dasturchini oyligi: {developer.salary}")
# print(f"dasturchini bilgan tili: {developer.programming_language}")
#
# manager.give_raise()
# developer.give_raise()
# print(f"managerni oyigini kotardik: {manager.salary}")
# print(f"dasturchini oyligini kotardik: {developer.salary}")

"""MAsala tuzishda GPT ishlatmadim baxoni kech qoganimga tushirsez mayli lekin GPT sabab bo'lmasin pils o'zi paslab yotibman"""