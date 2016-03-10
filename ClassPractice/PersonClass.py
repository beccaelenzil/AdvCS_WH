class Person():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        s = "My name is " + str(self.name) + "."
        return s

    def iLike(self):
        print "I like going for walks."


class Student(Person):
    def __init__(self, name, grade):
        Person.__init__(self, name)
        self.name = name
        self.grade = grade

    def __repr__(self):
        s = "My name is " + str(self.name) + ". I am in " + str(self.grade) + "th grade."
        return s

    def iLike(self):
        print "I like hanging out with friends."


lucas = Student("Lucas", 23)
lucas.iLike()
