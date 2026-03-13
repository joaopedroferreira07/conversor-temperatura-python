# conversor de temperatura (Celsius/Fahrenheit/Kelvin)
resposta = input("Entre quais temperaturas você deseja fazer a conversão? C para F, F para C, C para K, K para C, F para K ou K para F?")
if resposta == "C para F":
  temperatura = float(input("Qual é a sua temperatura em celsius?"))
  conversor = (temperatura * 1.8 + 32)
  print("Sua temperatura é:" , conversor , "fahrenheits")

elif resposta == "F para C":
  temperatura = float(input("Qual é a sua temperatura em fahrenheits?"))
  conversor_2 = ((temperatura - 32) * 5 / 9)
  print("Sua temperatura é:" , conversor , "celsius")

elif resposta == "C para K":
  temperatura = float(input("Qual é a sua temperatura em celsius?"))
  conversor = (temperatura + 273.15)
  print("Sua tempertura é:" , conversor , "kelvin")

elif resposta == "K para C":
  temperatura = float(input("Qual é a sua temperatura em kelvin?"))
  conversor = (temperatura - 273.15)
  print("Sua tempertura é:" , conversor , "celsius")

elif resposta == "F para K":
  temperatura = float(input("Qual é a sua temperatura em fahrenheits?"))
  conversor = (((temperatura - 32) * 5 / 9) + 273.15)
  print("Sua temperatura é:" , conversor , "kelvin")

elif resposta == "K para F":
  temperatura = float(input("Qual é a sua temperatura em kelvin?"))
  conversor = (((temperatura - 273.15) * 9 / 5) + 32)
  print("Sua temperatura é:" , conversor , "fahrenheits")

else:
  print("Eita! A opção não é inválida, tente digitar exatamente como as opções sugeridas (ex: F para C).")
