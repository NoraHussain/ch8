from abc import ABC


class Person(ABC):
    pass


class Student(Person):
    name = None  # public
    _level = None  # protected
    __section = None  # private

    # Encapsulation
    def set_level(self, level):
        self._level = level

    # constructor
    def __init__(self, name):
        self.name = name

        print('init')

    def print_info(self):
        print("Name: ", self.name)
        print("Level: ", self._level)

        # destructor

        # def __del__(self):
        #     print('student deleted')


class SecondaryStudent(Student):
    # Polymorphism
    def print_info(self):
        print("secondary")


s1 = Student('nora')
s1.set_level(3)
s1.print_info()

s2 = SecondaryStudent('ali')
s2.set_level(4)
s2.print_info()

del s1
