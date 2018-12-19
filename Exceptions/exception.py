


try:
    f = open('test.txt')
except FileNotFoundError:
    print('Sorry. This file doesn\'t exist')
except Exception:
    print('Sorry. This file does not exist')
