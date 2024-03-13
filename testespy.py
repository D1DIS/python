'''nome = input ('qual o seu nome? ')
print ('é um prazer conhecer voce ', nome)'''

'''larg = float(input('largura da parede: '))
altura = float(input('altura da parede: '))
area = larg * altura
print ('a parede tem a dimensao de {} x {} e a sua area é de {}m quadrados'.format(larg,altura, area))

tinta = area / 2
print('para pintar essa parede vai ser preciso {} litros de tinta'.format(tinta))'''
 

'''largura = float(input('qual a largura da sua parede? '))
altura = float(input('qual a altura da sua parede? '))
area = largura * altura
print ('com base nos dados coletados é possivel dizer que a parede tem uma dimensao de {} x {} e a sua area total é de {}m2'.format(largura,altura,area))

tinta = area / 2 
print('para poder pintar a parede por completo sera preciso {}L de tinta'.format(tinta))'''

'''preço = float (input('qual é o preço do produto? R$ '))
novo = preço-(preço*5/100)
print ('o produto que antes custava R${} agora com a promoção vai custar R${}'.format(preço,novo))'''

'''salario = float(input('digite o valor do seu salario atual: R$'))
novo = salario+(salario*15/100)
print ('parabens!! o seu aumento foi efetuado , agora o seu salario que antes era R${:.2f} agora passa a ser R${:.2f} !!'.format(salario,novo))'''


'''cel = float(input ('quantos graus  Celsius estão fazendo atualmente na sua localidade? '))
GrausC = cel
grausF = (cel * 1.8)+32
Conversao= print('sabemos que 1 grau Celsius equivale a 33.8 Fahrenheit. Fazendo a conversão sabe-se que na sua localização atual esta fazendo: \n {} Graus Celsius \n {} Graus Fahrenheit'.format(GrausC,grausF))'''

'''km = int(input('quantos km esse veiculo alugado percorreu? '))
dias = int(input('por quantos dias ele foi alugado? '))
valorkm = km * 0.15
valordias = dias * 60
valortotal = valorkm + valordias
valor = float(input(' o valor total pelos dias percorridos é de: R${} \n o valor total pelos km percorridos é de: R${} \n o total a pagar é:R${}'.format(valordias,valorkm,valortotal)))'''

'''from math import sqrt, floor
num = int (input("digite um nomero: "))
raiz = sqrt(num)
print('a raiz de {} é igual a {}'.format(num,floor(raiz)))'''

'''# Solicita ao usuário que digite um número real
numero_real = float(input("Digite um número real: "))

# Obtém a parte inteira do número usando a função int()
parte_inteira = int(numero_real)

# Mostra na tela a parte inteira do número digitado
print(f"A parte inteira de {numero_real} é: {parte_inteira}")'''

'''import math

num = float(input('digite um numero: '))
print ('o valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))'''

'''num = float(input('digite um numero: '))
print ('o valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''


'''CO = float(input('digite o valor do cateto oposto de um triangulo retangulo: '))
CA = float(input('digite o valor do cateto adjacente triangulo retangulo: '))
H = (CO**2 + CA**2) ** (1/2)

print ('a hipotenusa vai valer {}'.format(H))'''

import math

CO = float(input('digite o valor do cateto: '))
CA = float(input('digite o valor do adjacente: '))
H = math.hypot(CO , CA)
print ('a hipotenusa vai ser {:.2f}'.format(H))

print (' eduardo lactose')

