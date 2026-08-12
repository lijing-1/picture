# 跨文件导入：从student文件导入Student类
from student import Student


class StudentManager:
    def __init__(self):
        self.student_list = []  # 存放Student对象

    def add_student(self, name, age, score):
        """添加学生"""
        stu = Student(name, age, score)
        self.student_list.append(stu)
        print(f"✅ 学生【{name}】添加成功！")

    def search_student(self, name):
        """查询学生，返回对象，给本文件其他方法调用"""
        for stu in self.student_list:
            if stu.name == name:
                return stu
        return None

    def show_all(self):
        """展示全部"""
        if not self.student_list:
            print("📭 当前没有学生数据！")
            return
        print("\n========学生列表========")
        for idx, stu in enumerate(self.student_list, start=1):
            print(f"{idx}. {stu}")
        print("=======================\n")

    def modify_student(self, name, new_score):
        """修改分数，调用本文件search_student"""
        stu = self.search_student(name)
        if stu:
            stu.score = new_score
            print(f"🔄 修改成功！{name} 新分数：{new_score}")
        else:
            print(f"❌ 未找到学生：{name}")

    def delete_student(self, name):
        """删除学生"""
        stu = self.search_student(name)
        if stu:
            self.student_list.remove(stu)
            print(f"🗑️ 学生【{name}】已删除")
        else:
            print(f"❌ 未找到学生：{name}")