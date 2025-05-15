while True:
   #dados do usuario
   print("DADOS DO USUÁRIO")
   nome = str(input("digite seu nome: "))
   idade = int(input("digite sua idade: "))
   altura = float(input("digite sua altura: "))
   peso = int(input("digite seu peso: "))

   print()

   #tabela IMC
   print("Classificação IMC")
   print("Menor que 18.5 Magreza")
   print("18.5 a 24.9 Normal")
   print("25 a 29.9 Sobrepeso")
   print("30 a 34.9 Obesidade grau I")
   print("35 a 39.9 Obesidade grau II")
   print("Maior que 40 Obesidade grau III")

   print()

   #calculo imc
   calculo_imc = float (format (peso/(altura*altura),'.1f'))
   
   print("seu IMC é de:", calculo_imc)

   if calculo_imc <= 18.5:
      print("você está em estado de magreza")
   elif calculo_imc >= 18.5 and calculo_imc <= 24.9:
      print("você está em estado normal")
   elif calculo_imc >= 25 and calculo_imc <= 29.9:
      print("você está em estado de sobrepeso")
   elif calculo_imc >= 30 and calculo_imc <= 34.9:
      print("você está em estado de obesidade grau I")
   elif calculo_imc >= 35 and calculo_imc <= 39.9:
      print("você está em estado de obesidade grau II")
   else:
      print("você está em estado de obesidade grau III")

   print()

   #fechar o programa

   user_input = input("Deseja fechar o programa? (y/n): ")
   if user_input.lower() == "y":
      exit()
   elif user_input.lower() == "n":
      print("O programa permanecerá aberto.")
   else:
      print("Entrada inválida. Por favor, insira 'y' para fechar ou 'n' para continuar.")
