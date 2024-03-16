import os

def contar_palavras(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()
        palavras = conteudo.split()
        return len(palavras)

def palavra_mais_longa(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()
        palavras = conteudo.split()
        palavra_mais_longa = max(palavras, key=lambda palavra: len(palavra.strip(".,;:!?")))
        return palavra_mais_longa.strip(".,;:!?")

def vogal_mais_comum(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        quant_igual_vogais = []
        conteudo = file.read().lower() 
        vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for char in conteudo:
            if char in vogais:
                vogais[char] += 1
        vogal_mais_comum = max(vogais, key=vogais.get)
        # print(vogais[vogal_mais_comum]) só queria ver se tava com o valor certo
        for vogal, quant in vogais.items():
            if quant == vogais[vogal_mais_comum]:
                quant_igual_vogais.append(vogal)
        return quant_igual_vogais

def encontrar_cao(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read().lower()
        linhas = conteudo.split('\n')
        for num_linha, linha in enumerate(linhas, start=1):
            if 'ção' in linha:
                return num_linha
        return None

import os

def main():
    
    diretorio_atual = os.path.dirname(__file__)
    print("Diretório atual:", diretorio_atual)

    arquivo = input("Digite o nome do arquivo texto: ")
    arquivo_completo = os.path.join(diretorio_atual, arquivo)

    if not os.path.exists(arquivo_completo):
        print("O arquivo não foi encontrado.")
        return
    main_processamento(arquivo_completo)

def main_processamento(arquivo):
    total_palavras = contar_palavras(arquivo)
    print(f"Total de palavras: {total_palavras}")

    palavra_longa = palavra_mais_longa(arquivo)
    print(f"Palavra(s) mais longa(s): {palavra_longa}")

    vogal_comum = vogal_mais_comum(arquivo)
    if len(vogal_comum) != 1:
        print('Apareceram a mesma quantidade de vezes: ', end='')
        for _, vogal in enumerate(vogal_comum):
            if _ != len(vogal_comum) -1:
                print(vogal, end=', ')
            else:
                print(vogal, end='.\n')
    else:
        print(f"Vogal mais comum: {vogal_comum[0]}")

    linha_cao = encontrar_cao(arquivo)
    if linha_cao:
        print(f"A palavra 'ção' ocorre na linha {linha_cao}.")
    else:
        print("A palavra 'ção' não foi encontrada no texto.")

if __name__ == "__main__":
    main()
