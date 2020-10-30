"""[Week 10] Roman Number"""

def main():
    """[Week 10] Roman Number"""
    text = input()
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD':400, 'CM': 900}
    i = 0
    num = 0
    while i < len(text):
        if i + 1 < len(text) and text[i: i + 2] in roman_num:
            num += roman_num[text[i: i + 2]]
            i += 2
        else:
            num += roman_num[text[i]]
            i += 1
    print(num)

main()
