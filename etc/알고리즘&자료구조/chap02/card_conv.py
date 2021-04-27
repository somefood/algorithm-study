def card_conv(x: int, r: int) -> str:
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMnOPQRSTUWXYZ'

    while x > 0:
        d += dchar[x%r]
        x //= r
    
    return d[::-1]


if __name__ == '__main__':
    while True:
        while True:
            no = int(input('input over 0: '))
            if no > 0:
                break
        
        while True:
            cd = int(input('어떤 진수로 변환: '))
            if 2 <= cd <= 36:
                break
        
        print(f'{cd}진수로는 {card_conv(no, cd)}')

        retry = input("Y/N")
        if retry in {'N', 'n'}:
            break