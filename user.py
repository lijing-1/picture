class User:
    def __init__(self, username):
        self.username = username
        # 判断角色：username为admin就是管理员，其余普通用户
        if username == "admin":
            self.role = "admin"
        else:
            self.role = "normal"

    def is_admin(self):
        """判断是否管理员，给其他文件调用"""
        return self.role == "admin"


def login():
    """登录函数，输入用户名，返回User对象"""
    print("=====系统登录=====")
    username = input("请输入用户名：").strip()
    # 这里简单模拟，只要输入用户名就创建用户；admin则获得管理员权限
    current_user = User(username)
    print(f"✅登录成功！当前用户：{current_user.username}，角色：{current_user.role}")
    return current_user