while True:
  print("/Opções da calculadora/")
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")
  try:
    opção = int(input("Opção: "))
    print()
    if opção in [1, 2, 3, 4]:
      a, b = float(input("Valor de A: ")), float(input("Valor de B: "))
      operações = {1: a + b, 2: a - b, 3: a * b, 4: a / b}
      print(f"Resultado: {operações[opção]}")
      break
    else:
      print("Opção inválida. Por favor, escolha uma opção válida.")
  except ValueError:
    print("Digite umas das opções que está entre aspas: '1', '2', '3' e '4'.")
    print()