num1 = float(input("Digite um numero: "))
if num1 % 2 == 0:
   print("Par")
else:
  print("Impar")
num1 = int(input("Digite um numero: "))
if num1 < 0:
  print("numero negativo")
elif num1 > 0:
  ("numero positivo")
else :
  print("numero zero")
letra = input('Digite uma letra: ').upper()
if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O'or letra == 'U':
  print("vogal")
else:
  print("cosoante")
Ec4
a = float(input("Digite o Numero do primeiro lado:"))
b = float(input("DIgite o Numero do segundo lado:"))
c = float(input("Digite o Numero do terceiro lado:"))
if a == b == c:
  print("Esse triangulo é Equilátero")
elif a != b != c:
  print("Esse triangulo é Escaleno")
elif a == b != c or a != b == c:
  print("Esse triangulo é Isósceles")
