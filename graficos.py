import matplotlib.pyplot as plt
import pandas as pd

print("=======Bem-vindo a Interface de Geração de Gráficos======= \nEscolha a pergunta que deseja visualizar as respostas e gerar um gráfico:")
print(''' 
    0 | Encerrar programa.
    1) Com que frequência você escuta música?
    2) Quais gêneros musicais você mais gosta?
    3) Onde você costuma ouvir música?
    4) Qual plataforma de streaming você mais utiliza?
    5) Você prefere ouvir músicas novas ou clássicas?
    6) Você assistiu a um show ao vivo nos últimos 12 meses?
    7) Qual desses fatores mais influencia na sua escolha de música?
    8) Com qual dessas frases você mais se identifica?
    9) Você toca algum instrumento musical?
    10)Você costuma criar playlists personalizadas?
    ''')

# Variavel para encerrar o loop | Encerrar programa
encerrar = True

while encerrar:
    # Escolha do usuário:
    escolha = int(input("Digite o número da questão desejada: "))

    # Coleta de dados e criação de Dataframe:2
    if escolha != 0 and escolha <= 10:
        escolha = str(escolha)
        df = pd.read_csv(f"DadosFormulario/pergunta{escolha}.csv")
        alternativas = df['ALT'].to_list()
        respostas = df['Resposta'].to_list()

    # Encerramento do programa 
    elif escolha == 0:
        print("\nPrograma encerrado.")
        break


    # Tratamento de erro de digitação do usuário:
    else:
        print("\n========[valor invalido, tente novamente]========\n")
        continue

    # Definindo tamanho da janela de exibição dos gráficos:
    plt.figure(figsize=(12, 7))

   
    # Geração de gráficos
    match escolha:
        # Estrutura dentro do Match-Case
            # Titulo do gráfico
            # Tipo de gráfico
            # Configurações do gráfico
        case '1':
            plt.title("Com que frequência você escuta música?")
            plt.pie(respostas, labels = alternativas, autopct='%1.1f%%')

        case '2':
            plt.title("Quais gêneros musicais você mais gosta?")
            plt.barh(alternativas, respostas)
            plt.gca().invert_yaxis()
            # .gca = get current axys | invert_yaxis | -> inverter a orientação do eixo y
            plt.xticks(range(0, max(respostas) +5, 5))
            # xticks | define o intervalo de valores nos eixos.

        case '3':
            plt.title("Onde você costuma ouvir música?")
            plt.bar(alternativas, respostas)
            plt.yticks(range(0, max(respostas) +5, 5))
        case '4':
            plt.title("Qual plataforma de streaming você mais utiliza?")
            plt.pie(respostas, labels = alternativas, autopct='%1.1f%%')

        case '5':
            plt.title("Você prefere ouvir músicas novas ou clássicas?")
            plt.pie(respostas, labels = alternativas, autopct='%1.1f%%')

        case '6':
            plt.title("Você assistiu a um show ao vivo nos últimos 12 meses?")
            plt.barh(alternativas, respostas)
            plt.gca().invert_yaxis()
            plt.xticks(range(0, max(respostas) +5, 5))

        case '7':
            plt.title("Qual desses fatores mais influencia na sua escolha de música?")
            plt.barh(alternativas, respostas)
            plt.gca().invert_yaxis()
            plt.xticks(range(0, max(respostas) +5, 5))

        case '8':
            plt.title("Com qual dessas frases você mais se identifica?")
            plt.bar(alternativas, respostas)
            plt.yticks(range(0, max(respostas) +5, 5))

        case '9':
            plt.title("Você toca algum instrumento musical?")
            plt.bar(alternativas, respostas)
            plt.yticks(range(0, max(respostas) +5, 5))

        case '10':
            plt.title("Você costuma criar playlists personalizadas?")
            plt.pie(respostas, labels = alternativas, autopct='%1.1f%%')

    plt.show()
