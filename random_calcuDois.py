import random

def conta(): # Função de 1.Soma/Subtração, 3.Multiplicação , 4.Divisão
  a, b = random.randint(-320, 320), random.randint(-100, 100) # Número aleatório de A e b
  dado = random.randint(1, 3) # Número no qual vai cair o tipo de cálculo
  sinal = {1: "+", 2: "x", 3: "/"} # Sinal que será mostrado conforme o tipo de conta
  if dado == 1: # 1.SOMA/SUBTRAÇÃO
    while (a == 0 or b == 0) or (abs(a) == 1 or abs(b) == 1) or(abs(a) > 100 or abs(b) > 100): # Condições que A e B não dever ser
      a, b = random.randint(-320, 320), random.randint(-100, 100) # Número aleatório de A e B até não ser uma das condições do while
    resultado = a + b # Guarda o valor sobre a execução da conta com A e B
  elif dado == 2: # 2.MULTIPLICAÇÃO
    while a * b == 0 or (abs(a) == 1 or abs(b) == 1) or (abs(a) > 100 or abs(b) > 10): 
      a, b = random.randint(-320, 320), random.randint(-100, 100) # Número aleatório de A e B até não ser uma das condições do while
    resultado = a * b 
  elif dado == 3: # 3.DIVISÃO
    while a == 0 or abs(b) == 1 or b == 0 or a == -b or a == b or a % b != 0 or (a / b == 2 or a / b == -2): 
      a, b = random.randint(-320, 320), random.randint(-100, 100) # Número aleatório de A e B até não ser uma das condições do while
    resultado = a / b
 
  resposta = input(f'Qual é o resultado de ({a}) {sinal[dado]} ({b}) (ou digite "s" para sair): ').lower() # Local aonde o usuário vai responder a questão matemática
  if resposta == 's': # Caso reposda com "s", ele encerra o programa
    return True
  try: # Se responder com um número vai executar isso.
    resposta = float(resposta) # A mesma pergunta só que agora com float(números inteiros 0.1, 25.7, 1.4 e assim por diante)
    if resposta == resultado:  # Caso 
      print(f'Correto, o resultado é: {resultado}') 
    else: 
      print(f'Errado, o resultado de ({a}) {sinal[dado]} ({b}) é: {resultado}')
  except ValueError:
    print("Entrada inválida. Por favor, digite um número ou 's' para sair.")
  return False

print()
while True:
  if conta():
    break
  print()
