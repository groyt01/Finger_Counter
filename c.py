class Bird:
    className = 'птица'
    objCount = 0
    def __init__(self, name, id, age):
        self.__name = name
        self.id = id
        self.age = age
        Bird.objCount += 1
    def info(self):
        print(self.__name)
        print(self.id)
        print(self.age)

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

b = Bird('Евлампий', 1, 12)
b1 = Bird('Анна', 2, 14)
b.set_name('Савелий')
print(b.get_name())

b.info()
b1.info()