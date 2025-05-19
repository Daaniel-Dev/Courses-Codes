def titulo(msg, linha, espaco, negrito=False):
    msg = f'{msg:^{espaco}}'
    negrito = '\033[1m' if negrito else ''
    print(f'{linha}' * len(msg))
    print(f'{negrito}{msg}\033[m')
    print(f'{linha}' * len(msg))
