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

def inverterCaractere(palavra):
    palavra_invertida = ""
    contador_caractere = len(palavra) - 1
    while(len(palavra_invertida) != len(palavra)):
        palavra_invertida = palavra_invertida + palavra[contador_caractere]
        contador_caractere = contador_caractere - 1
    return palavra_invertida

print("Palavra invertida: ", inverterCaractere(input("Digite a palavra que você quer inverter: ")))