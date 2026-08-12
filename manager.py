from student import Student


class StudentManager:
    def __init__(self):
        self.student_list = []

    def add_student(self, name, age, score, is_admin):
        if not is_admin:
            print("❌权限不足！只有管理员可以添加学生")
            return
        stu = Student(name, age, score)
        self.student_list.append(stu)
        print(f"✅ 学生【{name}】添加成功！")

    def search_student(self, name):
        # 查询不需要权限，所有人可用
        for stu in self.student_list:
            if stu.name == name:
                return stu
        return None

    def show_all(self):
        if not self.student_list:
            print("📭 当前没有学生数据！")
            return
        print("\n========学生列表========")
        for idx, stu in enumerate(self.student_list, start=1):
            print(f"{idx}. {stu}")
        print("=======================\n")

    def modify_student(self, name, new_score, is_admin):
        if not is_admin:
            print("❌权限不足！只有管理员可以修改学生")
            return
        stu = self.search_student(name)
        if stu:
            stu.score = new_score
            print(f"🔄 修改成功！{name} 新分数：{new_score}")
        else:
            print(f"❌ 未找到学生：{name}")

    def delete_student(self, name, is_admin):
        if not is_admin:
            print("❌权限不足！只有管理员可以删除学生")
            return
        stu = self.search_student(name)
        if stu:
            self.student_list.remove(stu)
            print(f"🗑️ 学生【{name}】已删除")
        else:
            print(f"❌ 未找到学生：{name}")