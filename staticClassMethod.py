# class Calculator:

#     # create addNumbers static method
#     # @staticmethod
#     def addNumbers(self):
#         return 55

# c = Calculator()
# print('Product:', c.addNumbers())

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

new_line = "\n"
obj = MyClass()
print(obj.method())
print('\n')                            
print(obj.classmethod())
print('\n')
print(obj.staticmethod())
