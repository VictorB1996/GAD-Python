from abc import abstractmethod


class Animal:
    number_of_legs = 4

    def __init__(self, name, breed=None):
        self._name = name
        self.breed = breed

    # def set_name(self, name):
    #     self._name = name
    #
    # def get_name(self):
    #     return self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @staticmethod
    @abstractmethod
    def speak():
        pass


class Dog(Animal):

    @staticmethod
    def speak():
        print("Ham, ham!")

    @classmethod
    def create_instance(cls):
        return cls("Ben")

    # Used for converting object to string
    def __str__(self):
        return "<%s - Name = %s" % (type(self).__name__, self._name)

    # Used for representation inside a list or any other data structure
    def __repr__(self):
        return "%s(name = %s, breed = %s)" % (type(self).__name__, self._name, self.breed)

    def __len__(self):
        return len(self._name)


class CustomClass:
    number_of_legs = 2


class Cat(Animal, CustomClass):
    @staticmethod
    def speak():
        print("Miau, miau!")

    def __len__(self):
        return 20


# rex = Dog("Rex", "Bulldog")
# rex.name = "New Rex"
# print(f"Dog name is {rex.name} - {rex.breed} - {rex.number_of_legs} legs.")
# # del rex.name
# # print(f"Dog name is {rex.name} - {rex.breed} - {rex.number_of_legs} legs.")
# rex.speak()
# Dog.speak()
#
# new_dog = Dog.create_instance()
# print(new_dog)
#
# l = [new_dog]
# print(l)
#
# print(len(new_dog))
#
# julie = Cat("Julie")
# # julie.legs_number
#
# data_1 = [1, 2, 3, 4, 5]
# data_2 = "abcdefg"
# data_3 = julie
#
# my_list = [data_1, data_2, data_3]
# for i in my_list:
#     print(len(i))

# Iterators and iterables
class FibonacciIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.value = 1
        self.next_value = 1
        self.iteration = 0
        return self

    def __next__(self):
        if self.iteration < self.n:
            self.iteration += 1
            aux_value = self.value
            if self.next_value == 1:
                self.next_value += 1
            else:
                self.value = self.next_value
                self.next_value = aux_value + self.next_value
            return aux_value

        raise StopIteration


x = iter(FibonacciIterator(10))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
