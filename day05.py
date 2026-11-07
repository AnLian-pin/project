class Student:
    name=None
    gender=None
    nationality=None
    native_place=None
    age=None
    def test(self,msg):
        print(f"我的名字是{self.name},我来自{self.nationality},{msg}")

stu=Student()
stu.name="John"
stu.nationality="China"
stu.test("请大家多多关照")