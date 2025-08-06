# class ChangName:
#     def WhatsName(self):
#         self.name = "mehdi"
        
# x = ChangName()
# x.name = "ali"
# print(x.name)

# x.WhatsName()
# print(x.name)
# ------------------------

# class point:
#     def __init__(self, x:float= 0, y:float =0):
#         self.x = x
#         self.y = y
#     def move(self, x, y):
#         self.x = x
#         self.y = y
        
#     def reset(self):
#         x = self.move(0,0)
#     def absoulute(self, other: "point"):
#         return ((self.x - other.x)**2) + ((self.y - other.y)**2)


# s = point(y = 10)
# f = point()
# print(s.y)
# s.reset()

# f.x = 0
# f.y = 0

# print(s.absoulute(f))

# class Myname:
#     def __init__(self, x, n):
#         print(type(self))
#         self.x = n
#         self.n = x
#     def SayHello(self):
#         print(f"hello {self.n}")
        
# c = Myname(10, 5)
# v = Myname(10, 5)

# class acount_inf:
#     def __init__(self, name, family):
#         self.name = name
#         self.family = family
#     def __str__(self):
#         return f"{self.name},{self.family}"
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}','{self.family}')"
    

# acount = acount_inf("mehdi", "ght")
# print(str(acount))
# print(repr(acount))
# ---------------------------------------
# from pprint import pprint


# class UserList(list):
#     def search(self, user_find: str) -> list["name"]:
#         user_col: list["name"] = []
#         for user in self:
#             if user_find in str(user) :
#                 user_col.append(user)
#         return user_col
# class name:
#     all_inf:list["name"] = UserList()
#     def __init__(self, person_name :str, age: str):
#         self.person_name = person_name
#         self.age = age
#         name.all_inf.append(self) 
#     def __repr__(self):
#          return f"{self.__class__.__name__}('{self.person_name}', {self.age})"
#     def __str__(self):
#         return f"{self.person_name}"



# class family(name):
#     def say_bye(self, famil):
#         self.famil = famil
#         print(f"bye {self.name} {self.famil}")



# def main():
#     c = name("mehdi", 18)
#     b = name("ali", 20)
#     print(name.all_inf.search("i"))



# if __name__ == "__main__":
#     main()

# -----------------------------

# class p0:
#     def __init__(self, d):
#         self.arg = d
#         print(f"{self.arg}")
# class p1(p0):
#     def __init__(self, c, **kwargs):
#         super().__init__(**kwargs)
#         self.c = c
#         print(f"{self.c}")

# class p2(p0):
#     def __init__(self, b, **kwargs):
#         super().__init__(**kwargs)
#         self.b = b
#         print(f"{self.b}")
        
# class pa(p1,p2):
#     def __init__(self, a,**kwargs):
#         super().__init__(**kwargs)
#         self.a = a
#         print(f"{self.a}")
        
        
# def main():
#     p = pa(a=1, b= 2, c=3, d=4)
    
    
# if __name__ == "__main__":
#     main()

# class wifi_mmixin:
#     def connect(self):
#         print(self.name)


# class viechle:
#     pass



# class car(viechle, wifi_mmixin):
#     pass


# class airplane(viechle):
#     pass

# c = car()
# c.connect("mehdi")

