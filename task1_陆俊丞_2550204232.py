"""
学生信息管理系统 —— 增删改查菜单
作者：陆俊丞
学号：2550204232
"""

# 存储所有学生信息，格式：{学号: {"姓名": ..., "年龄": ..., "成绩": ...}}
students = {}


def show_menu():
    """显示主菜单"""
    print("\n" + "=" * 30)
    print("     学生信息管理系统")
    print("=" * 30)
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 修改学生信息")
    print("4. 删除学生")
    print("5. 显示所有学生")
    print("0. 退出系统")
    print("=" * 30)


def add_student():
    """添加学生信息"""
    print("\n--- 添加学生 ---")
    sid = input("请输入学号: ").strip()
    if sid in students:
        print(f"学号 {sid} 已存在，请使用修改功能！")
        return
    name = input("请输入姓名: ").strip()
    age = input("请输入年龄: ").strip()
    score = input("请输入成绩: ").strip()
    students[sid] = {"姓名": name, "年龄": age, "成绩": score}
    print(f"学生 {name} 添加成功！")


def query_student():
    """按学号查询学生"""
    print("\n--- 查询学生 ---")
    if not students:
        print("系统中暂无学生信息。")
        return
    sid = input("请输入要查询的学号: ").strip()
    info = students.get(sid)
    if info:
        print(f"学号: {sid}  姓名: {info['姓名']}  年龄: {info['年龄']}  成绩: {info['成绩']}")


def update_student():
    """修改学生信息"""
    print("\n--- 修改学生信息 ---")
    if not students:
        print("系统中暂无学生信息。")
        return
    sid = input("请输入要修改的学号: ").strip()
    if sid not in students:
        print(f"未找到学号为 {sid} 的学生。")
        return
    print("留空则不修改该项。")
    new_name = input(f"新姓名（当前: {students[sid]['姓名']}）: ").strip()
    new_age = input(f"新年龄（当前: {students[sid]['年龄']}）: ").strip()
    new_score = input(f"新成绩（当前: {students[sid]['成绩']}）: ").strip()
    if new_name:
        students[sid]["姓名"] = new_name
    if new_age:
        students[sid]["年龄"] = new_age
    if new_score:
        students[sid]["成绩"] = new_score
    print("修改成功！")


def delete_student():
    """删除学生信息"""
    print("\n--- 删除学生 ---")
    if not students:
        print("系统中暂无学生信息。")
        return
    sid = input("请输入要删除的学号: ").strip()
    if sid in students:
        name = students[sid]["姓名"]
        del students[sid]
        print(f"学生 {name} 已删除！")
    else:
        print(f"未找到学号为 {sid} 的学生。")


def show_all():
    """显示所有学生信息"""
    print("\n--- 所有学生 ---")
    if not students:
        print("系统中暂无学生信息。")
        return
    print(f"{'学号':<12} {'姓名':<10} {'年龄':<8} {'成绩':<8}")
    print("-" * 38)
    for sid, info in students.items():
        print(f"{sid:<12} {info['姓名']:<10} {info['年龄']:<8} {info['成绩']:<8}")


def main():
    """主程序入口"""
    while True:
        show_menu()
        choice = input("请输入操作编号: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            query_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            show_all()
        elif choice == "0":
            print("感谢使用，再见！")
            break
        else:
            print("无效输入，请重新选择。")
        input("\n按回车键继续...")


if __name__ == "__main__":
    main()
