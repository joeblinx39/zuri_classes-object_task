class Student:
    student_name = 'Ben'
    age = 24
    track = 'FE, BE'
    score = 20.94
    

    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    @classmethod
    def change_name(cls, student_name):
        # class_name.class_variable
        cls.student_name = student_name
        
    @classmethod
    def change_age(cls, age):
        # class_name.class_variable
        cls.age = age
        
    @classmethod
    def add_track(cls, track):
        # class_name.class_variable
        cls.track = track
        
    @classmethod
    def get_score(cls, score):
        # class_name.class_variable
        cls.score = score    

    # instance method
    def show(self):
        print('Name:', self.name, 'Age:',self.age, 'Track:', self.track, 'Score:', self.score)
    
    def change(self):
        print('Name:', Student.student_name, 'Age:', Student.age, 'Track:', Student.track, 'Score:', Student.score)

Bob = Student('Bob', 24, 'FE/BE', 20.94)
Bob.show()

# change school_name
Bob.change_name('Peter')
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(45.67)
Bob.change()
