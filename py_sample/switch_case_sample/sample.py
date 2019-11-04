import sys


def switch_case(target):
    temp = {
        'sunny': '晴れ',
        'cloudy': '曇り',
        'rainy': '雨'
    }.get(target)
    
    if not temp:
        temp = 'その他'

    return temp


def main():
    print(switch_case('sunny'))
    print(switch_case('rainy'))
    print(switch_case('snowy'))
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
