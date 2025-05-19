def titulo(msg, linha, espaco):
    msg = f'{msg:^{espaco}}'
    print(f'{linha}' * len(msg))
    print(msg)
    print(f'{linha}' * len(msg))
