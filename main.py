# 跨文件导入
from manager import StudentManager
from menu import show_menu, press_enter_continue


def main():
    print("欢迎来到学生信息管理系统")
    manager = StudentManager()

    while True:
        # 调用menu.py里的函数
        show_menu()
        choice = input("请输入你的选择(0-5): ")

        if choice == "1":
            name = input("请输入学生姓名：")
            age = int(input("请输入学生年龄："))
            score = float(input("请输入学生分数："))
            manager.add_student(name, age, score)

        elif choice == "2":
            manager.show_all()

        elif choice == "3":
            s_name = input("输入要查询的学生姓名：")
            res = manager.search_student(s_name)
            if res:
                print(f"✅ 查询结果：{res}")
            else:
                print("❌ 未找到该学生")

        elif choice == "4":
            s_name = input("输入要修改的学生姓名：")
            new_sc = float(input("输入新分数："))
            manager.modify_student(s_name, new_sc)

        elif choice == "5":
            s_name = input("输入要删除的学生姓名：")
            manager.delete_student(s_name)

        elif choice == "0":
            print("👋 程序退出，再见！")
            break
        else:
            print("⚠️输入无效，请输入0~5之间数字！")

        press_enter_continue()


if __name__ == "__main__":
    main()