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

class Myname:
    def __init__(self, x, n):
        print(type(self))
        self.x = n
        self.n = x
    def SayHello(self):
        print(f"hello {self.n}")
        
c = Myname(10, 5)
v = Myname(10, 5)
