
class Teacher():
    def __init__(self, name, age, qualification):
        self.name = name
        self.age = age
        self.qualification = qualification

    def __repr__(self):
        return ("{0}, is a {1} year old teacher. Qualifications include {2}".format(self.name, self.age, self.qualification,))


