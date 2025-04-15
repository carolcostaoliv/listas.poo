#exercício 1

nome = input("Digite o seu nome completo:")
print ("Bem-vindo(a) ao Python,", nome.split()[0])

#exercício 2

nota1 = int(input("Digite a nota do primeiro bimestre da disciplina:\n"))
nota2 = int(input("Digite a nota do segundo bimestre da disciplina:\n"))

while not (0<= nota1 <=100) and (0<= nota2 <=100):
    nota1 = int(input("Digite a nota do primeiro bimestre da disciplina:"))
    nota2 = int(input("Digite a nota do segundo bimestre da disciplina:"))

media = (nota1*2 + nota2*3) // 5
print(f"Média parcial = {media}")

#exercício 3

print("Digite a base e a altura do retângulo")
base = int(input())
altura = int (input())
area = base * altura
perimetro = base * 2 + altura * 2
diagonal = (base**2 + altura**2)**(1/2)
print(f'Área = {area:.2f} - Perímetro = {perimetro:.2f} - Diagonal = {diagonal:.2f}')

#exercício 4

frase = input("Digite uma frase: ")
print (frase[frase.rindex(" ") + 1:])