# #1

def maior(x,y):
    if x > y:
        return (x)
    else:
        return (y)

numero1 = float(input())
numero2 = float(input())

M = maior(numero1, numero2)
print("O maior número é:", M)

#2

def maior(x,y,z):
    if x > y and x > z:
        return (x)
    if y > x and y > z:
        return (y)
    else:
        return (z)

numero1 = float(input())
numero2 = float(input())
numero3 = float(input())

m = maior(numero1, numero2, numero3)
print("O maior número é:", m)
4

# 3

def iniciais(nome):
    palavras = nome.split()
    letras = [] 
    
    for palavra in palavras:
        primeira_letra = palavra[0]
        letra_maiuscula = primeira_letra.upper()
        letras.append(letra_maiuscula)
    
    iniciais = ''.join(letras)
    return iniciais

nome = input()
print(iniciais(nome))

# 4

def aprovado(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media >= 60

nota1 = float(input())
nota2 = float(input())

if aprovado(nota1,nota2):
    print ("Aprovado")
else:
    print("Reprovado")

#5

def formatar_nome(nome):
    partes = nome.lower().split()
    nome_formatado = []
    
    for palavra in partes:
        if palavra:
            primeira_letra = palavra[0].upper()
            resto = palavra[1:]
            nome_formatado.append(primeira_letra + resto)
    
    return ' '.join(nome_formatado)

nome = input("Digite seu nome: ")
print("Nome formatado:", formatar_nome(nome))