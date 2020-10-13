def card_conv(x:int, r:int) -> str:
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r

    return d[::-1]


if __name__ == '__main__':
    print('10진수를 n진수로 변환')

    while True:
        while True:
            no = int(input("양의 정수 입력"))
            if no > 0:
                break

        while True:
            cd = int(input('몇 진수로 변환'))
            if 2 <= cd <= 36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input("one more? (Y/N)")
        if retry in {'N', 'n'}:
            break