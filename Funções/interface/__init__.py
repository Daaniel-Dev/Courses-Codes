# Melhorar essa função para centralizar a mensagem
def titulo(msg, quant_espaco, tipo='-', negrito=False):
    negrito = '\033[1m' if negrito else '\033[m'
    print(f'{tipo}' * (len(msg) + quant_espaco * 2 + 2))
    print(f'{negrito}{msg:^{len(msg) + quant_espaco * 2 + 2}}\033[m')
    print(f'{tipo}' * (len(msg) + quant_espaco * 2 + 2))