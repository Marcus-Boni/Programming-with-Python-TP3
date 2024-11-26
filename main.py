def ler_nome_completo():
    """
    Lê um nome e um sobrenome do usuário e exibe ambos na mesma linha.

    Exemplo:
    Entre com o nome: Maria
    Entre com o sobrenome: Maia
    Saída: Maria Maia
    """
    print("\nQuestão 1: Concatenar Nome e Sobrenome")
    print("----------------------------")
    nome = input("Entre com o nome: ")
    sobrenome = input("Entre com o sobrenome: ")
    print(nome + " " + sobrenome)

ler_nome_completo()

def ler_nome_sobrenome_validado():
    """
    Lê um nome e sobrenome na mesma linha e verifica se a entrada é válida.
    Uma entrada válida deve ter pelo menos dois caracteres para o nome e o sobrenome.

    Exemplo:
    Entrada: "Lu Ma"
    Saída: Entrada válida: Lu Ma
    """
    print("\nQuestão 2: Validação de Nome e Sobrenome com split")
    print("----------------------------------------")
    while True:
        entrada = input("Entre com o nome e sobrenome: ")
        partes = entrada.split()
        
        if len(partes) == 2 and len(partes[0]) >= 2 and len(partes[1]) >= 2:
            print("Entrada válida: " + entrada)
            break
        else:
            print("Entrada inválida. O nome e o sobrenome devem ter pelo menos dois caracteres cada. Tente novamente.")

ler_nome_sobrenome_validado()

def exibir_nome_formatado():
    """
    Lê um nome e sobrenome na mesma linha e exibe no formato "SOBRENOME, Nome".

    Exemplo:
    Entrada: "Maria Maia"
    Saída: "MAIA, Maria"
    """
    print("\nQuestão 3: Exibir Sobrenome, Nome")
    print("--------------------------------")
    entrada = input("Entre com o nome e sobrenome: ")
    partes = entrada.split()
    
    if len(partes) == 2:
        nome = partes[0]
        sobrenome = partes[1].upper()
        print(f"{sobrenome}, {nome}")
    else:
        print("Entrada inválida. Por favor, entre com um nome e um sobrenome.")

exibir_nome_formatado()

def ler_data_formatada():
    """
    Lê uma data no formato "dd/mm/aaaa" e mostra o dia, mês e ano como inteiros.

    Exemplo:
    Entrada: "25/12/2023"
    Saída: Dia: 25, Mês: 12, Ano: 2023
    """
    print("\nQuestão 4: Data em Formato Inteiro")
    print("-----------------------------")
    data = input("Entre com a data no formato dd/mm/aaaa: ")
    partes = data.split('/')
    
    if len(partes) == 3:
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
        print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")
    else:
        print("Entrada inválida. Por favor, entre com a data no formato dd/mm/aaaa.")

ler_data_formatada()

def ler_data_formatada_validada():
    """
    Lê uma data no formato "dd/mm/aaaa" e valida se a data é válida.
    Verifica os meses com 31, 30, 29 e 28 dias, além de validar o mês.

    Exemplo:
    Entrada: "29/02/2024"
    Saída: "Data válida"
    Entrada: "29/02/2023"
    Saída: "Data inválida"
    """
    print("\nQuestão 5: Validação de Data")
    print("-----------------------------")
    data = input("Entre com a data no formato dd/mm/aaaa: ")
    partes = data.split('/')
    
    if len(partes) == 3:
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
        
        if mes < 1 or mes > 12:
            print("Data inválida. Mês inválido.")
            return
        
        if dia < 1 or dia > 31:
            print("Data inválida. Dia inválido.")
            return
        
        if mes in [4, 6, 9, 11] and dia > 30:
            print("Data inválida. Este mês tem apenas 30 dias.")
            return
        
        if mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > 29:
                    print("Data inválida. Fevereiro em ano bissexto tem apenas 29 dias.")
                    return
            else:
                if dia > 28:
                    print("Data inválida. Fevereiro tem apenas 28 dias.")
                    return
        
        print("Data válida.")
    else:
        print("Entrada inválida. Por favor, entre com a data no formato dd/mm/aaaa.")

ler_data_formatada_validada()

def exibir_data_formatada():
    """
    Lê uma data no formato "dd/mm/aaaa" e mostra o dia, mês e ano no formato "dia de nome_do_mês de ano".

    Exemplo:
    Entrada: "02/11/2024"
    Saída: "02 de novembro de 2024"
    """
    print("\nQuestão 6: Formato “dia de mês de ano”")
    print("-----------------------------")
    data = input("Entre com a data no formato dd/mm/aaaa: ")
    partes = data.split('/')
    
    if len(partes) == 3:
        dia = partes[0]
        mes = int(partes[1])
        ano = partes[2]
        
        meses = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        
        if 1 <= mes <= 12:
            nome_do_mes = meses[mes - 1]
            print(f"{dia} de {nome_do_mes} de {ano}")
        else:
            print("Mês inválido. Por favor, entre com um mês entre 01 e 12.")
    else:
        print("Entrada inválida. Por favor, entre com a data no formato dd/mm/aaaa.")

exibir_data_formatada()

def verificar_palindromo():
    """
    Lê uma palavra do usuário e verifica se é um palíndromo.
    Uma palavra palíndromo é aquela cuja sequência de letras é simétrica,
    permitindo uma leitura idêntica da esquerda para a direita ou da direita para a esquerda.

    Exemplo:
    Entrada: "radar"
    Saída: "A palavra 'radar' é um palíndromo."
    """
    print("\nQuestão 7: Verificar Palíndromo")
    print("-----------------------------")
    palavra = input("Entre com uma palavra: ").strip().lower()
    
    if palavra == palavra[::-1]:
        print(f"A palavra '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")

verificar_palindromo()

def contar_vogais():
    """
    Lê uma frase do usuário e exibe o número de vogais contidas na frase.

    Exemplo:
    Entrada: "Olá, mundo!"
    Saída: "Número de vogais: 4"
    """
    print("\nQuestão 8: Contagem de Vogais")
    print("----------------------")
    frase = input("Entre com uma frase: ").strip().lower()
    vogais = "aeiou"
    contador = sum(1 for char in frase if char in vogais)
    
    print(f"Número de vogais: {contador}")

contar_vogais()

def formatar_numero_telefone():
    """
    Lê um número de telefone do usuário e exibe no formato (99) 99999-9999.
    A entrada deve ser validada até que o usuário entre com 11 números.

    Exemplo:
    Entrada: "21987654321"
    Saída: "(21) 98765-4321"
    """
    print("\nQuestão 9: Formatar Número de Telefone")
    print("-----------------------------------")
    while True:
        numero = input("Entre com um número de telefone (11 dígitos): ").strip()
        
        if len(numero) == 11 and numero.isdigit():
            ddd = numero[:2]
            primeira_parte = numero[2:7]
            segunda_parte = numero[7:]
            print(f"({ddd}) {primeira_parte}-{segunda_parte}")
            break
        else:
            print("Entrada inválida. Por favor, entre com um número de telefone contendo 11 dígitos.")

formatar_numero_telefone()

def exibir_dia_da_semana():
    """
    Lê um número entre 1 e 7 e exibe o dia da semana correspondente.
    O programa valida a entrada do usuário.

    Exemplo:
    Entrada: "8"
    Saída: "Erro: número inválido"
    Entrada: "1"
    Saída: "Domingo"
    Entrada: "7"
    Saída: "Sábado"
    """
    print("\nQuestão 10: Dia da Semana")
    print("-----------------------------")
    dias_da_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
    
    while True:
        numero = input("Entre com um número entre 1 e 7: ").strip()
        
        if numero.isdigit():
            numero = int(numero)
            if 1 <= numero <= 7:
                print(dias_da_semana[numero - 1])
                break
            else:
                print("Erro: número inválido. Por favor, entre com um número entre 1 e 7.")
        else:
            print("Erro: entrada inválida. Por favor, entre com um número entre 1 e 7.")

exibir_dia_da_semana()

def formatar_cpf():
    """
    Lê um número de CPF do usuário e exibe no formato 999.999.999-99.
    A entrada deve ser validada até que o usuário entre com 11 números.

    Exemplo:
    Entrada: "01234567890"
    Saída: "012.345.678-90"
    """
    print("\nQuestão 11: Formatar CPF")
    print("---------------------")
    while True:
        cpf = input("Entre com um número de CPF (11 dígitos): ").strip()
        
        if len(cpf) == 11 and cpf.isdigit():
            parte1 = cpf[:3]
            parte2 = cpf[3:6]
            parte3 = cpf[6:9]
            parte4 = cpf[9:]
            print(f"{parte1}.{parte2}.{parte3}-{parte4}")
            break
        else:
            print("Entrada inválida. Por favor, entre com um número de CPF contendo 11 dígitos.")

formatar_cpf()

def inverter_frase():
    """
    Lê uma frase do usuário e exibe a frase invertida utilizando o comando de repetição "for".

    Exemplo:
    Entrada: "eu gosto de programar"
    Saída: "ramargorp ed otsog ue"
    """
    print("\nQuestão 12: Inverter Frase com for")
    print("-----------------------")
    frase = input("Entre com uma frase: ").strip()
    frase_invertida = ""
    
    for char in reversed(frase):
        frase_invertida += char
    
    print(f"Frase invertida: {frase_invertida}")

inverter_frase()

def inverter_frase_com_slice():
    """
    Lê uma frase do usuário e exibe a frase invertida utilizando o comando de manipulação de strings [::].

    Exemplo:
    Entrada: "eu gosto de programar"
    Saída: "ramargorp ed otsog ue"
    """
    print("\nQuestão 13: Inverter Frase com Slicing")
    print("-------------------------------")
    frase = input("Entre com uma frase: ").strip()
    frase_invertida = frase[::-1]
    
    print(f"Frase invertida: {frase_invertida}")

inverter_frase_com_slice()

def exibir_primeiros_e_ultimos_caracteres():
    """
    Lê uma frase do usuário e exibe os cinco primeiros e os cinco últimos caracteres
    utilizando o comando de manipulação de strings [::].

    Exemplo:
    Entrada: "eu gosto de programar"
    Saída: 
    "Cinco primeiros: eu go"
    "Cinco últimos: ramar"
    """
    print("\nQuestão 14: Cinco Primeiros e Últimos Caracteres")
    print("---------------------------------------------")
    frase = input("Entre com uma frase: ").strip()
    
    cinco_primeiros = frase[:5]
    cinco_ultimos = frase[-5:]
    
    print(f"Cinco primeiros: {cinco_primeiros}")
    print(f"Cinco últimos: {cinco_ultimos}")

exibir_primeiros_e_ultimos_caracteres()

def substituir_ponto_virgula():
    """
    Lê uma entrada do usuário e substitui o ";" por "," utilizando o comando "replace".

    Exemplo:
    Entrada: "1;Maria;1000"
    Saída: "1,Maria,1000"
    """
    print("\nQuestão 15: Substituir “;” por “,”")
    print("-----------------------------------")
    entrada = input("Entre com a entrada: ").strip()
    entrada_substituida = entrada.replace(';', ',')
    
    print(f"Saída: {entrada_substituida}")

substituir_ponto_virgula()

def calcular_media():
    """
    Lê dois números do usuário e mostra a média dos números lidos.
    Utiliza a formatação "f-strings" para a exibição da saída.

    Exemplo:
    Entrada: "5" e "7"
    Saída: "A média dos números 5 e 7 é 6.0"
    """
    print("\nQuestão 16: Cálculo de Média com f-strings")
    print("-----------------------")
    numero1 = float(input("Entre com o primeiro número: ").strip())
    numero2 = float(input("Entre com o segundo número: ").strip())
    
    media = (numero1 + numero2) / 2
    
    print(f"A média dos números {numero1} e {numero2} é {media}")

calcular_media()