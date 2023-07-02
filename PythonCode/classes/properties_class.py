class Presenter():
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('In the getter')
        return self.__name

    @name.setter
    def name(self, value):
        print('In setter')
        self.__name = value

    def say_hello(self):
        print('hello, ' + self.name)


presenter = Presenter('wangqijia')
presenter.name = 'yangchangjiang'
presenter.say_hello()
