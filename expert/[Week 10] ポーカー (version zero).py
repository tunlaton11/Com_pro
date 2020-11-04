"""ポーカー (version zero)"""


def tam(lista):
    """ポーカー (version zero)"""
    if lista[0].isdigit():
        return int(lista[0])
    else:
        tamm = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        return tamm[lista[0]]


def flush(dok):
    """ポーカー (version zero)"""
    if len(set(dok)) == 1:
        return True
    return False


def staigth(tamm):
    """ポーカー (version zero)"""
    tamm.sort()
    for i in range(5):
        if tamm[0] + i != tamm[i]:
            return False
    return True


def four(tamm):
    """ポーカー (version zero)"""
    if len(list(set(tamm))) == 2:
        if max([tamm.count(i) for i in list(set(tamm))]) == 4:
            return True
    return False


def full(tamm):
    """ポーカー (version zero)"""
    if len(list(set(tamm))) == 2:
        if max([tamm.count(i) for i in list(set(tamm))]) == 3:
            return True
    return False


def three(tamm):
    """ポーカー (version zero)"""
    if len(list(set(tamm))) == 3:
        if max([tamm.count(i) for i in list(set(tamm))]) == 3:
            return True
    return False


def twop(tamm):
    """ポーカー (version zero)"""
    if len(list(set(tamm))) == 3:
        if max([tamm.count(i) for i in list(set(tamm))]) == 2:
            return True
    return False


def onep(tamm):
    """ポーカー (version zero)"""
    if len(list(set(tamm))) == 4:
        return True
    return False


def winner(rak, tamm):
    """win"""
    if rak[0] != rak[1]:
        print('Player', rak.index(max(rak)) + 1)
    else:
        if sum(tamm[0]) > sum(tamm[1]):
            print('Player 1')
        else:
            print('Player 2')


def main():
    """ポーカー (version zero)"""
    play = []
    dok = []
    tamm = []
    rak = []
    for i in range(2):
        play.append(input().replace('[', '').replace(',', '').replace(']', '')
                    .replace("'", '').split(' '))
        dok.append(list(map(lambda x: x[1], play[i])))
        tamm.append(list(map(tam, play[i])))
        rak.append(0)
    for i in range(2):
        if staigth(tamm[i]) and flush(tamm[i]):
            rak[i] = 9
        elif four(tamm[i]):
            rak[i] = 8
        elif full(tamm[i]):
            rak[i] = 7
        elif flush(dok[i]):
            rak[i] = 6
        elif staigth(tamm[i]):
            rak[i] = 5
        elif three(tamm[i]):
            rak[i] = 4
        elif twop(tamm[i]):
            rak[i] = 3
        elif onep(tamm[i]):
            rak[i] = 2
        else:
            rak[i] = 1
            tamm[i] = [max(tamm)]
    winner(rak, tamm)


main()
