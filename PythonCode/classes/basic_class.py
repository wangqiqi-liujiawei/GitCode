class Presenter():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('hello, ' + self.name)


presenter = Presenter('wangqijia')
# presenter.name = 'yangchangjiang'
presenter.say_hello()
