from manager import StudentManager
from menu import show_menu, press_enter_continue
from user import login


def main():
    print("欢迎来到学生信息管理系统")
    # 先执行登录，拿到当前登录用户对象
    current_user = login()
    manager = StudentManager()

    while True:
        # 根据用户角色展示菜单
        show_menu(current_user.is_admin())
        choice = input("请输入你的选择: ")

        if choice == "1":
            # 添加学生，传入权限标记
            name = input("请输入学生姓名：")
            age = int(input("请输入学生年龄："))
            score = float(input("请输入学生分数："))
            manager.add_student(name, age, score, current_user.is_admin())

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
            manager.modify_student(s_name, new_sc, current_user.is_admin())

        elif choice == "5":
            s_name = input("输入要删除的学生姓名：")
            manager.delete_student(s_name, current_user.is_admin())

        elif choice == "0":
            print("👋 程序退出，再见！")
            break
        else:
            print("⚠️无效输入！")

        press_enter_continue()


if __name__ == "__main__":
    main()