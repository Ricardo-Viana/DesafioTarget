import json

def fibonacciSequence(number, penultimate_number, last_number, fibonnaci_value):
    if(number < fibonnaci_value):
        return "Não pertence a sequencia"
    elif(number == fibonnaci_value):
        return "Pertence a sequencia"
    else:
        fibonnaci_value = penultimate_number + last_number
        penultimate_number = last_number
        last_number = fibonnaci_value
        return fibonacciSequence(number, penultimate_number, last_number, fibonnaci_value)

print(fibonacciSequence(int(input("Digite um número para saber se ele pertence a sequencia de fibonnaci: ")), 0, 1, 0))

def questao1():
    indice = 13 
    soma = 0
    k = 0
    while k < indice:
        k = k + 1
        soma = soma + k
    print("Soma", soma)

questao1()

def analisar_faturamento(json_file):
    with open(json_file, 'r') as file:
        dados = json.load(file)

    faturamentos = [dia['faturamento'] for dia in dados if dia['faturamento'] > 0]

    if not faturamentos:
        return "Nenhum dado de faturamento válido encontrado."

    menor_valor = min(faturamentos)
    maior_valor = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)
    
    dias_acima_media = sum(1 for dia in faturamentos if dia > media_mensal)

    return{
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_media": dias_acima_media
    }

print(analisar_faturamento("faturamento.json"))

def percentual_faturamento():
    faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
    }

    faturamento_total = sum(faturamento.values())

    for estado, valor in faturamento.items():
        percentual = (valor / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}%")

percentual_faturamento()

def inverterCaractere(palavra):
    palavra_invertida = ""
    contador_caractere = len(palavra) - 1
    while(len(palavra_invertida) != len(palavra)):
        palavra_invertida = palavra_invertida + palavra[contador_caractere]
        contador_caractere = contador_caractere - 1
    return palavra_invertida

print("Palavra invertida: ", inverterCaractere(input("Digite a palavra que você quer inverter: ")))
