"""[Week 11] Pizza Number"""

def findsum(pizza, target): #check possible sum**
    """[Week 11] Pizza Number"""
    possible_sum = [[] for i in range(target + 1)]

    for j in pizza:
        for i in range(target+1):
            if i < j:
                continue
            if i == j:
                possible_sum[i].append(j)
            else:
                for blist in possible_sum[i - j]:
                    possible_sum[i].append(blist + j)

    return possible_sum


def main():
    """[Week 11] Pizza Number"""
    num = int(input())
    if num >= 6:
        list2 = [list(set(x)) for x in findsum([6, 9, 20], num) if x != []]
        for i in list2:
            print(str(i).replace("[", '').replace("]", ''))
    else:
        print("no") 

main()
