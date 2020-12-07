

def split_input(grades):
    grade_list = grades.lower().split(', ')
    return grade_list


def map_grade(grades):
    grade_value = {"a": 4, "b+": 3.5, "b": 3, "c+": 2.5, "c": 2}
    num_grade = [grade_value[i] for i in grades]
    return num_grade


def cal_grade(grades):
    mean = sum(grades) / len(grades)
    return mean


def main():
    word = input()
    print(split_input(word))
    print(map_grade(split_input(word)))
    print("%.2f" % cal_grade(map_grade(split_input(word))))


if __name__ == "__main__":
    main()
