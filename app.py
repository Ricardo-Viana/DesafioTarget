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

print(fibonacciSequence(int(input("Digite um número para saber se ele pertecen a sequencia de fibonnaci: ")), 0, 1, 0))

def findA(palavra):
    cont = 0
    for letra in palavra:
        if letra.lower() == 'a':
            cont += 1
    return cont

print(findA(input("Digite a palavra que queira ver a quantidade de As: ")))

def questao3():
    indice = 12
    soma = 0
    k = 1
    while k < indice:
        k = k + 1
        soma = soma + k
    return soma

print(questao3())