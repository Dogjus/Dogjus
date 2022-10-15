class Student:
    def __init__(self, magstory, plantologos, zelvar, trfiguration):
        self.magstory = magstory
        self.plantologos = plantologos
        self.zelvar = zelvar
        self.trfiguration = trfiguration

    def points(self):
        mp = self.magstory + self.plantologos
        zt = self.zelvar + self.trfiguration
        mpzt = mp + zt
        print("всего", mpzt, "баллов за экзамен по всем предметам")


student = Student(10, 30, 40, 5)
student.points()
