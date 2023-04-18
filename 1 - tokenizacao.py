import nltk


def ler_arquivo_base_dados():
    with open("base_dados/artigos.txt", "r", encoding="utf8") as f:
        artigos = f.read()

    return artigos


def separar_tokens(palavras):
    return nltk.tokenize.word_tokenize(palavras)


def separar_palavras(tokens):
    lista_palavras = list()
    for token in tokens:
        if token.isalpha():
            lista_palavras.append(token)

    return lista_palavras


def normalizacao(lista_palavras):
    lista_normalizada = list()
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada


if __name__ == '__main__':
    artigos = ler_arquivo_base_dados()

    palavras_separadas = separar_tokens(artigos)
    lista_palavras = separar_palavras(palavras_separadas)
    lista_normalizada = normalizacao(lista_palavras)
    print(lista_normalizada[:5])
