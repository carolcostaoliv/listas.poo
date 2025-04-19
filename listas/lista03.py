#1004 – Produto Simples

numero1 = float(input())
numero2 = float(input())
produto = numero1 * numero2
print(f"PROD = {produto:.0f}")

#1005 – Média 1 

nota1 = float(input())
nota2 = float(input())
nota1 = float(f"{nota1:.1f}")
nota2 = float(f"{nota2:.1f}")
media = (nota1 * 3.5 + nota2 * 7.5) / 11
print (f"MEDIA = {media:.5f}")

#1011 – Esfera  

raio = float(input())
volume = (4/3) * 3.14159 * raio**3
print(f"VOLUME = {volume:.3f3}")

#2416 – Corrida 

corrida = float(input())
pista = float (input())
agua = corrida % pista
agua = int(f"{agua:.0f}")
print (agua)

#1015 – Distância Entre Dois Pontos 

cordenadas1 = input().split()
x1 = float(f"{float(cordenadas1[0]):.1f}")
y1 = float(f"{float(cordenadas1[1]):.1f}")

cordenadas2 = input().split()
x2 = float(f"{float(cordenadas2[0]):.1f}")
y2 = float(f"{float(cordenadas2[1]):.1f}")

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"{distancia:.4f}")

#1930 – Tomadas  

tomadas = list(map(int, input().split()))
dispositivos = sum(tomadas) - 3
print (dispositivos)