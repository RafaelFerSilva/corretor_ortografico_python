import nltk


def ler_arquivo_base_dados():
    with open("base_dados/artigos.txt", "r", encoding="utf8") as f:
        artigos = f.read()

    return artigos


def fatiar_palavra(palavra):
    fatias = []

    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))

    return fatias


def separar_palavras(tokens):
    lista_palavras = list()
    for token in tokens:
        if token.isalpha():
            lista_palavras.append(token)

    return lista_palavras


def separar_tokens(palavras):
    return nltk.tokenize.word_tokenize(palavras)


def normalizacao(lista_palavras):
    lista_normalizada = list()
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada


def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)

    return novas_palavras


def gerador_palavras(palavra):
    fatias = fatiar_palavra(palavra)
    palavras_geradas = insere_letras(fatias)

    return palavras_geradas


class Corretor:

    def __init__(self):
        self.artigos = ler_arquivo_base_dados()
        self.palavras_separadas = separar_tokens(self.artigos)
        self.lista_palavras = separar_palavras(self.palavras_separadas)
        self.lista_normalizada = normalizacao(self.lista_palavras)
        self.total_palavras = len(self.lista_normalizada)
        self.frequencia = nltk.FreqDist(self.lista_normalizada)

    def probabilist(self, palavra_gerada):
        return self.frequencia[palavra_gerada] / self.total_palavras

    def corrector(self, palavra):
        palavras_geradas = gerador_palavras(palavra)
        palavra_correta = max(palavras_geradas, key=self.probabilist)

        return palavra_correta

    def cria_dados_teste(self, nome_arquivo):
        lista_palavras_teste = []
        f = open(nome_arquivo, "r", encoding="utf8")
        for linha in f:
            correta, errada = linha.split()
            lista_palavras_teste.append((correta, errada))

        f.close()
        return lista_palavras_teste

    def avaliador(self, testes):

        print('Taxa de acerto')


if __name__ == '__main__':
    new_corretor = Corretor()
    palavra_errada = "lgica"
    palavras_geradas = gerador_palavras(palavra_errada)
    palavra_correta = new_corretor.corrector(palavra_errada)
    lista_teste = new_corretor.cria_dados_teste("./base_dados/palavras.txt")
    print(lista_teste)
