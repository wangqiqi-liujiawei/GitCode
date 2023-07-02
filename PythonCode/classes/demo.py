class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self) -> str:
        return 'hello, ' + self.name


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def sing_school_song(self):
        print('sing ' + self.school + '校歌')

    def say_hello(self):
        str = super().say_hello()
        print(str + ' I am rather tired')

    def __str__(self) -> str:
        return f'{self.name} attends {self.school}'


student = Student('wangqijia', '中国科学院大学')
print(student)
# student = Student()
# student.say_hello()
# student.sing_school_song()

# print(f'Is this a student? {isinstance(student, Student)}')
# print(f'Is this a person? {isinstance(student, Person)}')
# print(f'Is this a Person? {issubclass(Student, Person)}')
