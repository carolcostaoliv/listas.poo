'''#1036 – Fórmula de Bhaskara

a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4 * a * c

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (-b + delta**0.5) / (2 * a)
    r2 = (-b - delta**0.5) / (2 * a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")

#1044 – Múltiplos  

n1 = int(input())
n2 = int(input())
if n1 % n2 == 0 or n2 % n1 == 0:
    print ("São multiplos")
else:
    print ("Não são multiplos")

#1049 – Animal  

caracteristica1 = input()
caracteristica2 = input()
caracteristica3 = input()

if caracteristica1 == "vertebrado":
    if caracteristica2 == "ave":
        if caracteristica3 == "carnivoro":
            print("aguia")
        elif caracteristica3 == "onivoro":
            print("pomba")
    elif caracteristica2 == "mamifero":
        if caracteristica3 == "onivoro":
            print("homem")
        elif caracteristica3 == "herbivoro":
            print("vaca")
elif caracteristica1 == "invertebrado":
    if caracteristica2 == "inseto":
        if caracteristica3 == "hematofago":
            print("pulga")
        elif caracteristica3 == "herbivoro":
            print("lagarta")
    elif caracteristica2 == "anelideo":
        if caracteristica3 == "hematofago":
            print("sanguessuga")
        elif caracteristica3 == "onivoro":
            print("minhoca")

#1050 – DDD  

dic = {61:'Brasília', 71: 'Salvador', 11: 'São Paulo', 21: 'Rio de Janeiro', 32:'Juiz de Fora', 19: 'Campinas', 27: 'Vitória', 31: 'Belo Horizonte'}
ddd = int(input())
if ddd in dic:
    print(dic[ddd])
else:
    print("DDD não cadastrado")

#2424 – Tira-teima  

corx, cory = map(int, input().split())
if 0 <= corx <= 432 and 0 <= cory <= 468:
    print ("Dentro")
else:
    print("Fora")

#2670 – Máquina de Café 

a1 = int(input())
a2 = int(input())
a3 = int(input())

tempo1 = 0 * a1 + 2 * a2 + 4 * a3
tempo2 = 2 * a1 + 0 * a2 + 2 * a3
tempo3 = 4 * a1 + 2 * a2 + 0 * a3
print(min(tempo1, tempo2, tempo3))
#1059 – Números Pares  

for n in range(1, 101):
    print(n)

#1080 – Maior e Posição  

maior = 0
posicao = 0

for i in range(1, 101):
    num = int(input())
    if num > maior:
        maior = num
        posicao = i

print(maior)
print(posicao)

#1094 – Experiências 

testes = int(input())  # número de casos de teste

coelhos = 0
ratos = 0
sapos = 0

for u in range(testes):
    quantidade, animal = input().split()
    quantidade = int(quantidade)

    if animal == 'C':
        coelhos = coelhos + quantidade
    elif animal == 'R':
        ratos =ratos + quantidade
    elif animal == 'S':
        sapos = sapos + quantidade

total = coelhos + ratos + sapos

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos / total * 100:.2f} %")
print(f"Percentual de ratos: {ratos / total * 100:.2f} %")
print(f"Percentual de sapos: {sapos / total * 100:.2f} %")

#1114 – Senha Fixa 

correta = 2002
senha = int(input())
while senha != correta:
    print ("Senha Inválida")
    senha = int(input())
print("Acesso Permitido")

#1116 – Dividindo X por Y  

numeros = int(input())  # número de pares

for k in range(numeros):
    nu, me = map(int, input().split())
    
    if me == 0:
        print("divisao impossivel")
    else:
        resultado = nu / me
        print(f"{resultado:.1f}")'''

#1151 – Fibonacci Fácil  

f = int(input())
sequencia = [0, 1]

for i in range(2, f):
    proximo = sequencia[i-1] + sequencia[i-2]
    sequencia.append(proximo)

for i in range(f):
    if i == f - 1:
        print(sequencia[i])
    else:
        print(sequencia[i], end=' ')
