import csv
import random

# Função para ler os resultados do arquivo CSV
def ler_resultados(file_path):
    resultados = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for linha in reader:
            resultados.append([int(numero) for numero in linha])
    return resultados

# Função para contar a frequência dos números nos resultados
def contar_frequencia(resultados):
    frequencia = {}
    for linha in resultados:
        for numero in linha:
            if numero in frequencia:
                frequencia[numero] += 1
            else:
                frequencia[numero] = 1
    return frequencia

# Função para gerar um jogo quente (números mais sorteados, excluindo os já sorteados)
def gerar_jogo_quente(resultados):
    frequencia = contar_frequencia(resultados)
    numeros_sorteio = [numero for numero, _ in sorted(frequencia.items(), key=lambda x: x[1], reverse=True)]

    jogo_quente = random.sample(numeros_sorteio, 6)

    return sorted(jogo_quente)

# Função para gerar um jogo frio (números menos sorteados, excluindo os já sorteados)
def gerar_jogo_frio(resultados):
    frequencia = contar_frequencia(resultados)
    numeros_sorteio = [numero for numero, _ in sorted(frequencia.items(), key=lambda x: x[1])]

    jogo_frio = random.sample(numeros_sorteio, 6)

    return sorted(jogo_frio)

# Função para gerar um jogo da virada (mistura de quente e frio, excluindo os já sorteados)
def gerar_jogo_da_virada(resultados):
    jogo_quente = gerar_jogo_quente(resultados)
    jogo_frio = gerar_jogo_frio(resultados)
    jogo_da_virada = jogo_frio[:3] + jogo_quente[:3]
    random.shuffle(jogo_da_virada)
    return sorted(jogo_da_virada)

# Caminho para o arquivo resultado.csv
caminho_arquivo = 'resultados.csv'

# Ler os resultados do arquivo CSV
resultados = ler_resultados(caminho_arquivo)

# Exibir os jogos gerados
while True:
    input("Pressione Enter para gerar novos números:")

    # Gerar os jogos
    jogo_quente = gerar_jogo_quente(resultados)
    jogo_frio = gerar_jogo_frio(resultados)
    jogo_da_virada = gerar_jogo_da_virada(resultados)

    # Exibir os jogos gerados
    print(f"Jogo Quente: {jogo_quente}")
    print(f"Jogo Frio: {jogo_frio}")
    print(f"Jogo da Virada: {jogo_da_virada}")
