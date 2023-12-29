'''

Para este desafio, vamos criar um loop que peçã para o usuário para 
digitar o nome de uma fruta. Se a fruta digitada não for "abacate", o
loop deve continuar. O loop só dever terminar se o usuário digitar 
"abacate".

'''
#Variavel fruta vazia
fruta = False

#While criado até que a fruta seja "Abacate".
while fruta != 'Abacate':
    #Entrada do usuário
    fruta = input('Digite um fruta: ').capitalize()

    #Condição de parada
    if fruta == 'Abacate':
        break

print("Parabéns você acertou a fruta!")