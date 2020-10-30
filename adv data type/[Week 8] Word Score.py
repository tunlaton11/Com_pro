"""[Week 8] Word Score"""


def main():
    """[Week 8] Word Score"""
    num = int(input())
    word_list = []
    word = []
    score = 0
    score_sub_list = []
    score_list = []


    for _ in range(num):
        count = int(input())
        for _ in range(count):
            text = input()
            word.append(text)
            for i in text:
                if i in "EAIONRTLSU":
                    score += 1
                elif i in "DG":
                    score += 2
                elif i in "BCMP":
                    score += 3
                elif i in "FHVWY":
                    score += 4
                elif i in "K":
                    score += 5
                elif i in "JX":
                    score += 8
                elif i in "QZ":
                    score += 10
            score_sub_list.append(score)
            score = 0

        score_list.append(score_sub_list)
        word_list.append(word)
        word = []
        score_sub_list = []

    for j in range(len(score_list)):
        max_score = score_list[j].index(max(score_list[j]))
        print(word_list[j][max_score])

main()
