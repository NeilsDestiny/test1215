# python面向对象编程

class persons():
    name = 'default'
    age = 0
    weight = 0
    gender = 'male'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 100

    # 类方法是不能访问实例方法的。类需要添加一个装饰器@classmethod就可以直接访问persons.set_play()
    @classmethod
    def set_play(self):
        print(f"{self.name} playing majiang")
        # print("majiang")


# print(persons.weight)
persons.set_play()

test = persons('wei',27)
print(test.name)
print(test.weight)