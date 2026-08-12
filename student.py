class Student:
    """学生实体类，存储单个学生数据"""
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"姓名:{self.name} | 年龄:{self.age} | 分数:{self.score}"