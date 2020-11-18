"""63070224"""


def main():
    grades = input()
    grade_split = split_input(grades)
    grade_num = map_grade(grade_split)
    grade_mean = cal_gpa(grade_num)
    print(grade_split)
    print(grade_num)
    print(grade_mean)


def split_input(grades):
    grade_list = grades.lower().split(", ")
    return grade_list


def map_grade(grades):
    grade_num = []
    for i in grades:
        if i == 'a':
            grade_num.append(4)
        elif i == 'b+':
            grade_num.append(3.5)
        elif i == 'b':
            grade_num.append(3)
        elif i == 'c+':
            grade_num.append(2.5)
        elif i == 'c':
            grade_num.append(2)
        else:
            grade_num.append(0)
    return grade_num


def cal_gpa(grades):
    mean = sum(grades) / len(grades)
    return mean


if __name__ == '__main__':
    main()
