class bodyParts:
    def __init__(self):
        self.hand = "hand"
        self.foot = "foot"

    

class creatures:
    def _init_(self, name):
        self.bP = self.bodyPart()
        self.name = name

    class bodyPart(bodyParts):
        def display(self):
            super().__init__() 
        
        def display(self):
            return self.hand

x = creatures().bodyPart().display()
# y = x.bodyPart()
print(x)


# class A:
#     def __init__(self):
#         self.db = self.Inner()

#     def display(self):
#         print('In Parent Class')

#     # this is inner class
#     class Inner:

#         def display1(self):
#             print('Inner Of Parent Class')


# class B(A):
#     def __init__(self):
#         print('In Child Class')
#         super().__init__()

#     class Inner(A.Inner):

#         def display2(self):
#             print('Inner Of Child Class')


# # creating child class object
# p = B()
# p.display()

# # create inner class object
# x = p.db
# x.display1()
# x.display2()
