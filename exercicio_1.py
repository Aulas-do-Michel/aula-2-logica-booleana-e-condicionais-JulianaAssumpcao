#Exercício 1 Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".
preco=int(input("Digite o preco: "))
resto=preco%2
if resto==0:
  print("Par")
else:
  print("Impar")
