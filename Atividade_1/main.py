def adicionarInfo(arquivo, nome, idade, sexo, telefone):
    with open(arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome}|{idade}|{sexo}|{telefone}\n")

def info():
    with open('info.txt', 'a', encoding='utf-8'):
        while True:
            nome = input('Nome (digite 0 para sair): ')
            if nome == '0':
                break

            idade = input('Idade: ')
            while not idade.isdigit():
                print('Idade deve ser um número inteiro.')
                idade = input('Idade: ')

            sexo = input('Sexo (F ou M): ').lower()
            while sexo not in ['f', 'm']:
                print('Sexo deve ser F ou M.')
                sexo = input('Sexo (F ou M): ').lower()

            telefone = input('Telefone: ')
            while not telefone.isdigit():
                print('Telefone deve ser um número inteiro.')
                telefone = input('Telefone: ')

            adicionarInfo('info.txt', nome, idade, sexo, telefone)

def ler(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    for linha in linhas:
        nome, idade, sexo, telefone = linha.strip().split('|')
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print(f"Sexo: {'Masculino' if sexo == 'm' else 'Feminino'}")
        print(f"Telefone: {telefone}")
        print()

def buscaUsuarioPorSexo(sexo, arquivo):
    resultados = []

    with open(arquivo, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    for linha in linhas:
        nome, idade, sexo_atual, telefone = linha.strip().split('|')
        if sexo_atual.lower() == sexo.lower():
            resultados.append({
                'Nome': nome,
                'Idade': idade,
                'Sexo': 'Masculino' if sexo_atual.lower() == 'm' else 'Feminino',
                'Telefone': telefone
            })

    return resultados

def infoPorSexo(sexo_procurado, arquivo):
    usuarios_encontrados = buscaUsuarioPorSexo(sexo_procurado, arquivo)

    if usuarios_encontrados:
        print(f"\nUsuários do sexo {sexo_procurado.upper()} encontrados:")
        for usuario in usuarios_encontrados:
            print(f"Nome: {usuario['Nome']}")
            print(f"Idade: {usuario['Idade']} anos")
            print(f"Sexo: {usuario['Sexo']}")
            print(f"Telefone: {usuario['Telefone']}")
            print()
    else:
        print(f"\nNenhum usuário do sexo {sexo_procurado.upper()} encontrado.")

def buscaUsuarioPorNome(nome_procurado, arquivo):
    resultados = []

    with open(arquivo, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    for linha in linhas:
        nome, idade, sexo, telefone = linha.strip().split('|')
        if nome_procurado.lower() in nome.lower():
            resultados.append({
                'Nome': nome,
                'Idade': idade,
                'Sexo': 'Masculino' if sexo.lower() == 'm' else 'Feminino',
                'Telefone': telefone
            })

    return resultados

def infoPorNome(nome_procurado, arquivo):
    usuarios_encontrados = buscaUsuarioPorNome(nome_procurado, arquivo)

    if usuarios_encontrados:
        print(f"\nUsuários encontrados com o nome '{nome_procurado}':")
        for usuario in usuarios_encontrados:
            print(f"Nome: {usuario['Nome']}")
            print(f"Idade: {usuario['Idade']} anos")
            print(f"Sexo: {usuario['Sexo']}")
            print(f"Telefone: {usuario['Telefone']}")
            print()
    else:
        print(f"\nNenhum usuário encontrado com o nome '{nome_procurado}'.")




infoPorNome('luc', 'info.txt')