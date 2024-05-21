import random

# Dado funcional
def dado():  # Número da pergunta (1.Soma/subtração, 2.Multiplicação, 3.Divisão) na qual vai cair, lembrando que cai aleatóriamente o número da questão.
  valor = random.randint(1, 3)
  return valor

# Dado de teste
def dado_t():  # (1.Soma/subtração, 2.Multiplicação, 3.Divisão)
  valor = 3
  return valor

def som_sub():  # Valor aleatório de 1.Soma/subtração. Valores de 'a' e 'b' podem ser de -100 a 100 aleatóriamente para cada valor.
  a = random.randint(-100, 100)
  b = random.randint(-100, 100)
  while (a == 0 or b == 0) or (abs(a) == 1 or abs(b) == 1):
    # 'a == 0' e 'b == 0' verifica se vai ter um valor 0 na conta.
    # 'abs(a) == 1' e 'abs(b)== 1' verifica se o valor absoluto de 'a' e 'b' é 1.
    # // ANOTAÇÃO: 'abs()' faz com que mesmo que -x e +x seja o resultado, ele volte com valor absoluto de x ignorando o sinal. //
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
  valor = a, b
  return valor

def mul():  # Valor aleatório de 2.Multiplicação. Valor de 'c' sendo -10 até 10 e valor de 'd' sendo de -100 até 100.
  c = random.randint(-10, 10)
  d = random.randint(-100, 100)
  while c * d == 0 or (abs(c) == 1 or abs(d) == 1):
    # 'c * d == 0' verifica se o resultado é igual a 0.
    # 'abs(c) == 1' e 'abs(d) == 1' verifica se um dos números multiplicáveis vai ser 1.
    # // ANOTAÇÃO: 'abs()' faz com que mesmo que -x e +x seja o resultado, ele volte com valor absoluto de x ignorando o sinal. //
    c = random.randint(-10, 10)
    d = random.randint(-100, 100)
  valor = c, d
  return valor

def div():  # Valor aleatório de 3.Divisão. Valor de 'e' sendo -320 até 320 e valor de 'b' sendo de -100 até 100.
  e = random.randint(-320, 320)
  f = random.randint(-100, 100)
  while f == 0 or abs(f) == 1 or e == 0 or e == -f or e == f or e % f != 0 or e % f != 50 and (e / f == 2 or e / f == -2):
    # 'f == 0' verifica se 'f' não é zero
    # '(f == 1' e 'f == -1)' garantem que 'f' não seja 1 ou -1
    # 'e == 0' verifica se 'e' não é zero
    # 'e == -f' garante que 'e' não seja o oposto de 'f' com sinais diferentes.
    # 'e == f' garante que 'e' não seja igual a 'f' com sinais iguais.
    # 'e % f != 0' garante que a divisão de e por 'f' não produza um número inteiro.
    # 'e % f != 50' garante que a divisão de e por 'f' não produza um número com um decimal correspondente a 0,5.
    # '(e / f == 2 or e / f == -2)' garante que 'e' e 'f' não são o oposto um do outro em relação a divisão.
    e = random.randint(-320, 320)
    f = random.randint(-100, 100)
  valor = e, f
  return valor


# Função dos cálculos 
# 1.Soma/subtração
def soma_subtracao(a, b): 
  resultado = a + b # Conta.
  quest = input(f"Qual é o resultado de ({a}) + ({b}) (ou digite 's' para sair): ") # Mostra a conta e uma opção para saída do loop.
  if quest == 's': # Quebra de loop
    return True
  quest = int(quest) # int permite uma resposta na qual esteja no conjunto dos números inteiros (..., -3, -2, -1, 0 , 1, 2, 3 ,4, ...).
  if quest == resultado:
    print(f"Correto! O resultado é: {resultado}.") # Afirma que o resultado estava certo, e repete a sua reposta.
  else:
    print(f"Errado, o resultado de ({a}) + ({b}) é: {resultado}.") # Afirma que o resultado está errado, e mostra novamente a conta com a reposta certa.

# 2.Multiplicação
def multiplicacao(c, d): 
  resultado = c * d # Conta.
  quest = input(f"Qual é o resultado de ({c}) x ({d}) (ou digite 's' para sair): ") # Mostra a conta e uma opção para saída do loop.
  if quest == 's': # Quebra de loop
    return True 
  quest = int(quest) # int permite uma resposta na qual esteja no conjunto dos números inteiros (..., -3, -2, -1, 0 , 1, 2, 3 ,4, ...).
  if quest == resultado:
    print(f"Correto! O resultado é: {resultado}.") # Afirma que o resultado estava certo, e repete a sua reposta.
  else:
    print(f"Errado, o resultado de ({c}) x ({d}) é: {resultado}.") # Afirma que o resultado está errado, e mostra novamente a conta com a reposta certa.

# 3.Divisão // PROBLEMA: aqui o código parece estar certo, deve ser nos valores aleatórios o problema. //
def divisao(e, f):
  resultado = e / f # Conta.
  quest = input(f"Qual é o resultado de ({e}) / ({f}) (ou digite 's' para sair): ") # Mostra a conta e uma opção para saída do loop.
  if quest == 's': # Quebra de loop
    return True
  quest = int(quest) # int permite uma resposta na qual esteja no conjunto dos números inteiros (..., -3, -2, -1, 0 , 1, 2, 3 ,4, ...).
  if quest == resultado:
    print(f"Correto! O resultado é: {resultado}.") # Afirma que o resultado estava certo, e repete a sua reposta.
  else:
    print(f"Errado, o resultado de ({e}) / ({f}) é: {resultado}.") # Afirma que o resultado está errado, e mostra novamente a conta com a reposta certa.

while True: # Output final com loop, e com opção de sáida dentro das funções de cálculo para quebra do loop.
  a, b = som_sub() # Armazena os valores aleatórios para que seja pego pelas funções de cálculo 1.Soma/subtração.
  c, d = mul() # Armazena os valores aleatórios para que seja pego pelas funções de cálculo 2.Multiplicação.
  e, f = div() # Armazena os valores aleatórios para que seja pego pelas funções de cálculo 3.Divisão.
  num_quest = dado() # Armazena-se o número no qual vai cair que tipo da função de cálculo.
  if num_quest == 1:
    if soma_subtracao(a, b): 
      break
  elif num_quest == 2:
    if multiplicacao(c, d):
      break
  elif num_quest == 3:
    if divisao(e, f):
      break
  print() # Espaço para que os conjuntos de perguntas e respostas fiquem longe dos mesmos, deixando melhor na visualização do momento.
