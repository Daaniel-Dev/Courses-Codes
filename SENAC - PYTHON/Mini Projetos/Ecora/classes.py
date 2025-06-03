class User:
    def __init__(self, cpf, senha, nome):
        self.cpf = cpf
        self.senha = senha
        self.nome = nome
    def chamar_dados(self):
        return self.cpf, self.senha, self.nome, 'Cliente'


class Vendedor(User):
    def __init__(self, cpf, senha, nome):
        super().__init__(cpf, senha, nome)
        self.produtos = []
    def chamar_dados(self):
        return self.cpf, self.senha, self.nome, 'Vendedor'


class Produto:
    def __init__(self, nome, preco, descricao, url_video=''):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.url_video = url_video

    def __str__(self):
        return (f'Produto: {self.nome}\nDescrição: {self.descricao}\nPreço: R${self.preco:.2f}\nVídeo: '
                f'{self.url_video if self.url_video else "Não informado"}')
