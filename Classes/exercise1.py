
class Person:

    def __init__(self, firstname, age):
        self.firstname = firstname
        self.age = age


joe = Person("joe", 20)

#use the setattr method to set the lastname without hardcoding

setattr(joe, "lastname", "walsh")
firstname = getattr(joe, "firstname", None)
print(firstname + " " + joe.lastname)