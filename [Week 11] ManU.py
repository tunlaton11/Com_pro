"""[Week 11] ManU"""


def rate(price):
    """[Week 11] ManU"""
    if price > 60:
        return 0.8
    elif 41 <= price <= 60:
        return 0.82
    elif 31 <= price <= 40:
        return 0.85
    elif 21 <= price <= 30:
        return 0.9
    elif 10 <= price <= 20:
        return 0.93
    else:
        return False

def main():
    """[Week 11] ManU"""
    price = int(input())
    if rate(price) == False:
        print("I don't care.")
    else:
        print("%.3f" % (rate(price) * price))

main()
