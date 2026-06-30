"""
学生信息统计功能 —— 演示新功能模块
作者：陆俊丞
学号：2550204232
"""


def student_statistics(students: dict) -> dict:
    """统计学生信息，返回各项统计数据。

    参数:
        students: 字典格式 {学号: {"姓名": str, "年龄": str, "成绩": str}}

    返回:
        包含统计结果的字典，字段包括：
        - total: 学生总数
        - avg_score: 平均成绩
        - max_score: 最高成绩（含姓名和学号）
        - min_score: 最低成绩（含姓名和学号）
        - avg_age: 平均年龄
        - pass_rate: 及格率（成绩 >= 60）
        - score_distribution: 成绩分段统计（优秀/良好/中等/及格/不及格）
    """
    if not students:
        print("暂无学生数据，无法统计。")
        return {}

    total = len(students)

    # 收集所有成绩和年龄（转换为数值类型）
    scores = []
    ages = []
    max_info = {"score": -1, "name": "", "sid": ""}
    min_info = {"score": 999, "name": "", "sid": ""}

    for sid, info in students.items():
        try:
            score = float(info.get("成绩", 0))
            age = float(info.get("年龄", 0))
        except ValueError:
            continue

        scores.append(score)
        ages.append(age)

        if score > max_info["score"]:
            max_info = {"score": score, "name": info["姓名"], "sid": sid}
        if score < min_info["score"]:
            min_info = {"score": score, "name": info["姓名"], "sid": sid}

    if not scores:
        print("无法解析有效的成绩数据。")
        return {}

    avg_score = sum(scores) / len(scores)
    avg_age = sum(ages) / len(ages)

    # 及格率
    pass_count = sum(1 for s in scores if s >= 60)
    pass_rate = pass_count / len(scores) * 100

    # 成绩分段统计
    distribution = {"优秀(>=90)": 0, "良好(80-89)": 0, "中等(70-79)": 0, "及格(60-69)": 0, "不及格(<60)": 0}
    for s in scores:
        if s >= 90:
            distribution["优秀(>=90)"] += 1
        elif s >= 80:
            distribution["良好(80-89)"] += 1
        elif s >= 70:
            distribution["中等(70-79)"] += 1
        elif s >= 60:
            distribution["及格(60-69)"] += 1
        else:
            distribution["不及格(<60)"] += 1

    return {
        "total": total,
        "avg_score": round(avg_score, 2),
        "max_score": max_info,
        "min_score": min_info,
        "avg_age": round(avg_age, 2),
        "pass_rate": round(pass_rate, 2),
        "score_distribution": distribution,
    }


def print_statistics(stats: dict):
    """格式化打印统计结果。

    参数:
        stats: student_statistics() 返回的统计字典
    """
    if not stats:
        return

    print("\n" + "=" * 40)
    print("          学生信息统计报表")
    print("=" * 40)
    print(f"  学生总数:     {stats['total']}")
    print(f"  平均成绩:     {stats['avg_score']}")
    print(f"  平均年龄:     {stats['avg_age']}")
    print(f"  及格率:       {stats['pass_rate']}%")
    print(f"  最高分:       {stats['max_score']['score']}  "
          f"({stats['max_score']['name']}, 学号: {stats['max_score']['sid']})")
    print(f"  最低分:       {stats['min_score']['score']}  "
          f"({stats['min_score']['name']}, 学号: {stats['min_score']['sid']})")
    print("-" * 40)
    print("  成绩分布:")
    for label, count in stats["score_distribution"].items():
        bar = "█" * count
        print(f"    {label:<14} {count}人  {bar}")
    print("=" * 40)


# 模块独立运行演示
if __name__ == "__main__":
    # 测试数据
    demo_students = {
        "001": {"姓名": "张三", "年龄": "20", "成绩": "85"},
        "002": {"姓名": "李四", "年龄": "19", "成绩": "92"},
        "003": {"姓名": "王五", "年龄": "21", "成绩": "55"},
        "004": {"姓名": "赵六", "年龄": "20", "成绩": "78"},
        "005": {"姓名": "孙七", "年龄": "22", "成绩": "63"},
    }

    result = student_statistics(demo_students)
    print_statistics(result)
