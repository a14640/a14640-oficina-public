Valor1 = float(input(Insira um numero: "))
Valor2 = float(input(Insira um numero: "))
print ("Resultado = Valor1 + Valor2")
if Resultado > menor
                     
 #EX0.1 
""" Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("Insira a sua idade: ");
nome = input("Insira o seu nome: ");
print(f"O meu nome é {nome} e tenho {idade} anos."  

#EX0.2: Output
print ("Ola mundo!");
fruta = ("morangos")
print (f"Eu gosto de {fruta}.") 

#EX0.3
nome = input (f"Poe aqui o teu nome: ");
print (f"Tudo bem {nome}? tem um bom dia");
valor = int(input("Insira um numero: "));
dobro = valor * 2 
print (f"O dobro de {valor} é {dobro}.")

 #Ex1.1
 print(f"\n  Bem-vindos a Python!")


      
#EX1.2
Nome = input("Insira o seu nome: ");
print(f"\n Olá {Nome}, Bem-vindos a Python!")



#Ex1.3

mensagem= "BIRU É LINDO"
print (mensagem)


 #Ex1.4
"""Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis."""

 nome = "Edu Silva" 
 idade = int("16")
 localidade = "São Martinho do Campo"
 print(f"O meu nome é {nome}, tenho {idade} anos e moro em {localidade}")

 #Ex1.5
 """Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem"""
   
linguagemdeprog = "Python"
nome = "Edu Silva"

print(f"O {nome} sabe programar no {linguagemdeprog}")

   
#Ex1.6
   
"""Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres."""

print(f"{'Left Aligned Text':<50}")
print(f"{'Center Aligned Text':^50}")
print (f"{'Right Aligned Text':>50}")


   #EX1.7
   """Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio."""

   raio = float(input("Digite o valor do raio: "))
   perímetro = 2 * 3,14 * raio
   area = 3,14*((raio)**2)
   print ("A circunferencia do",raio,"unidades.")
   print ("Tem um perimetro de",perímetro,"unidades.")
   print ("e area de",area,"unidades")



       
#EX1.8

   """Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
   
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
       """

from dataclasses import make_dataclass
import datetime
 x = datetime.datetime.now()
       dia = x.strftime("%d")
       mes = x.strftime("%m")
       ano = x.strftime("%y")
       hora = x.strftime("%H")
       minutos = x.strftime("%M")
       segundos = x.strftime("%S")
       print(f"{dia}-{mes}-{ano}")
       print(f"{dia}-{mes}-{ano} {hora}:{minutos}:{segundos}")
       print(f"{mes}-{dia}-{ano} {hora}:{minutos}:{segundos}")
       print(f"{mes}/{dia}/{ano}")
       print(f"{hora}:{minutos}:{segundos}")


 #EX1.9


"""Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
 O atleta número 12304 obteve 7.89 pontos."""

numero= input("Digite o numero do atleta: ")
Pontuação= input("Digite a pontuação final: ")
print (f"O atleta {numero} obteve {Pontuação}")


  nome = str(input('Qual é o teu nome? '))
 if nome == 'Biru':
  print('Que nome tao Biru!')
 else:
   print('O teu nome é tão banal')
   print('Bom dia, {}!'.format(nome))


 #D28
 import random 
segredo = int(random.randint(0,5))
"""print (f"o número secreto é:{segredo}")"""
 numeroescolhido = int (input("Insira um valor entre (0 e 5): "))
if numeroescolhido > segredo:
 print("O número inserido e maior que o meu!")
elif numeroescolhido < segredo:
print ("O número inserido é menor que o meu!")
else:
print("Acertaste!!!")

 #D29
import random 

 velocidade = int(random.randint(50,140))
multa = (velocidade - 120) * 7 
valor
"""print= (f"a sua velocidade é de: {velocidade}" )""
if velocidade = "< 120"
print ("Boa velocidade nao aceleres mais")
else velocidade = > 120
print ("OU, OU ALTO, excedeste a velocidade de 120 km/h porque andavas a {multa}! Tens que pagar )




 #FP1

"""Exercício FP1: Verificar se um número é positivo, negativo ou zero.
 Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
 Dica: Usa as estruturas condicionais if, elif e else.
 [consola]
 Introduza um número: 10
 O número é positivo."""

numero= int(input("Digite um numero: "))
if numero > 0:
print ("O teu numero é positivo.")
elif numero == 0:
print ("O teu numero é igual a zero.")
elif numero < 0:
print ("O teu numero é negativo.")


#FP2

"""Exercício FP2: Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %.

[consola]
Introduza um número: 7
O número é ímpar."""

                        
numero = int(input("Escolhe um numero: "))

x= numero
 y= 2 
res = x % y
resultado= res

if resultado == 0:
print ("O seu numero e par.")
else :
 print ("O seu numero e impar.")
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
 #FP3

"""Exercício FP3: Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:

Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"""


nota = int(input("Digite a sua nota: "))
if nota < 10:
  print ("Reprovado!")
elif  nota >= 10 and nota <= 14:
  print  ("Suficiente!")
elif nota >= 15 and  nota < 17:
  print ("Bom!")
else:
  print ("Muito Bom!")


  #FP04

  """Exercício FP4: Conversor de temperaturas.
  Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

  Fórmulas:

  Fahrenheit = Celsius * 9/5 + 32
  Kelvin = Celsius + 273.15

  [consola]
  Introduza a temperatura em Celsius: 25
  Deseja converter para (F) Fahrenheit ou (K) Kelvin? F
  A temperatura em Fahrenheit é: 77.0°F"""


  from types import EllipsisType


  Celsius = float(input("Introduza a temperatura em Celsius: "))

  Fahrenheit = (Celsius * 9/5) + 32
  Kelvin = Celsius + 273.15

  resultado = str(input("Deseja converter para Fahrenheit(F), Kelvin(K) ou Ambas (A): "))

  if resultado == "F":
    print (f"O valor em Fahrenheit é: {Fahrenheit}. ")
  elif resultado == "K":
    print (f"O valor em Kelvin é: {Kelvin}. ")
  elif resultado == "A":
    print (f"O valor em Fahrenheit é: {Fahrenheit}, e em Kelvin é: {Kelvin}")
  else:
    print ("Opção invalida")



  

#FP05

"""Exercício FP5: Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.

[consola]
Introduza o seu salário: 2500
Salário após impostos: 2000.0"""

salario = float(input("Insira o seu salario: "))
imposto1 = salario * 0.10
imposto2 = salario * 0.20
salarioimposto1 = salario - imposto1
salarioimposto2 = salario - imposto2
if salario <= 1000:
  print (f"O seu salario nao tem impostos! Fica com {salario} €!")
elif salario >= 1001 and salario <= 2000:
  print (f"O seu salario tem 10% de impostos, ou seja fica com {salarioimposto1} €!")
elif salario >= 2000:
  print (f"O seu salario tem 20% de impostos, ou seja fica com {salarioimposto2} €!")

  numeros= ["1-", "2-", "3-"]
  Turma1I = ["Brandão", "Edu", "Vides"]
  for x in Turma1I:
    for y in numeros:
      print(y,x)


  #Exercício FP6: Imprimir números de 1 a 10.
 """Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.

 [consola]
 1
 2
 3
...
 10"""
for x in range(11):
print (x)


"""#Exercício FP7: Soma de números de 1 a 100.
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.

  A soma de 1 a 100 é: 5050"""
               
soma=0 
 i=1
while i <= 100:
soma += i
i += 1
print(f"A soma de a 100 é: {soma}")

#Exercício FP8: Contagem de vogais numa string.
"""Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase."""


frase = input ("Insira uma frase: ")
vogais = 0

for letra in frase:
  if  letra == "a" or letra == "i" or letra == "e" or letra == "o" or letra == "u" or letra == "A" or letra == "  I" or letra == "E" or letra == "O" or letra == "U":
vogais +=1
print (f"Ha {vogais} vogais nesta frase.")


  #Exercício FP9: Listar múltiplos de 5.
  """Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50."""

  temporario = 0 
  for i in range (1,51):
    if temporario <= 49:
       temporario = i * 5
       print (temporario)

  #Exercício FP10: Média de uma lista de números
  """Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números."""

  notas=[]
  for i in range (1,6):
    num=int(input("escreva um numero inteiro: "))
    notas.append(num)
  print(notas)
  valor1 = notas[0]
  valor2 = notas[1]
  valor3 = notas[2]
  valor4 = notas[3]
  valor5 = notas[4]
  total = (valor1 + valor2 + valor3 + valor4 + valor5) /5
  print(f"A media é: {total}")



 #Exercício FP10: Média de uma lista de números
"""Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números."""

notas=[]
for i in range (0,5):
    numeros = int(input("Insira um valor: "))
    notas.append (numeros)
soma = sum (notas)
    x = len (notas)
media = (soma / x)
print(media)



 #Exercício FP11: Verificar se um número é primo.
 """Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número."""

    numero = int(input('Insira um numero: '))
    divisores = 0
    for i in range(1, numero + 1 ):
        if numero % i == 0: #verifica se o resultado da divisão é 0
            divisores += 1  #incrementa o contador de divisores
    if divisores  == 2:
        print(f"O {numero} é um número primo")
    else:
        print(f"O {numero} não é um número primo")






    #"Exercício FP12: Gerar uma lista de números pares.
    """Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista."""

    for x in range (0, 22, 2):
      print (f"{x}")





  #Exercício FP13: Inverter uma string.
  """Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida."""

  texto =   str(input("Insira um texto: ")) 
  textoinv = texto[::-1]
  print (textoinv)




 #Exercício FP14: Tabuada de multiplicação
"""Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10."""

num= int(input("Digite o seu numero: "))
for i in range(1,11):
mult = num * i 
print(f"{num} x {i} = {mult}")





