class Person:
    def __init__(self, name):
        self._name = name

    def __get_name(self):
        print("Get name")
        return self._name

    def __set_name(self, value):
        print("Set name")
        self._name = value

    def __del_name(self):
        print("Delete name")
        del self._name

    name = property(
        fget=__get_name,
        fset=__set_name,
        fdel=__del_name,
        doc="The name property."
    )


person = Person('Jack')
print(person.name)
person.name = "John Deere"
print(person.name)