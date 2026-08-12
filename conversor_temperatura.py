# Conversor de temperatura (Celsius/Fahrenheit/Kelvin)

resposta = input("Entre quais temperaturas você deseja fazer a conversão? C para F, F para C, C para K, K para C, F para K ou K para F?").strip().upper()

if resposta == "C PARA F":
  temperatura = float(input("Qual é a sua temperatura em celsius?"))
  conversor = (temperatura * 1.8 + 32)
  print(f"Sua temperatura em fahrenheits é: {conversor:.2f}")

elif resposta == "F PARA C":
  temperatura = float(input("Qual é a sua temperatura em fahrenheits?"))
  conversor = ((temperatura - 32) * 5 / 9)
  print(f"Sua temperatura em celsius é: {conversor:.2f}")

elif resposta == "C PARA K":
  temperatura = float(input("Qual é a sua temperatura em celsius?"))
  conversor = (temperatura + 273.15)
  print(f"Sua tempertura em kelvin é: {conversor:.2f}")

elif resposta == "K PARA C":
  temperatura = float(input("Qual é a sua temperatura em kelvin?"))
  conversor = (temperatura - 273.15)
  print(f"Sua tempertura em celsius é: {conversor:.2f}")

elif resposta == "F PARA K":
  temperatura = float(input("Qual é a sua temperatura em fahrenheits?"))
  conversor = (((temperatura - 32) * 5 / 9) + 273.15)
  print(f"Sua tempertura em kelvin é: {conversor:.2f}")

elif resposta == "K PARA F":
  temperatura = float(input("Qual é a sua temperatura em kelvin?"))
  conversor = (((temperatura - 273.15) * 9 / 5) + 32)
  print(f"Sua tempertura em fahrenheits é: {conversor:.2f}")

else:
  print("Eita! A opção digitada é inválida. Tente digitar exatamente como as opções sugeridas (ex: F para C).")
