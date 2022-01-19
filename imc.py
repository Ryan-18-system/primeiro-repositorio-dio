def calcular_imc(peso, altura):
  imc = peso / (altura * altura)
  if imc < 18.5:
    return "Magreza"
  elif imc == 18.5 or imc < 24.9:
    return "Normal"
  elif imc == 24.9 or imc < 30:
    return "sobrepeso"
  else:
    return "Obeso"


print(calcular_imc(85, 1.83))    

  