print("\n CONVERSOR DE MONEDAS")

historial = []

Valor__dolar = float(input("Ingrese valor del dolar: "))

Valor_dolar = Valor__dolar

while True:
     print("1 - Pesos a Dolares")
     print("2 - Dolares a Pesos")
     print("3 - Ver historial")
     print("4 - salir")

     opcion = input("Elija una opcion:")

     if opcion == "1":
          monto = float(input("Ingrese monto en pesos: "))
          resultado = monto / Valor_dolar 
          historial.append(f"{monto} pesos -> {resultado} dolares")
          print("Equivale a", resultado,"Dolares")


     elif opcion == "2":
          dolares = float(input("Cantidad de dolares: "))
          pesos = dolares * Valor_dolar
          historial.append(f"{dolares} dolares -> {pesos} pesos")
          print("Equivale a", pesos, "Pesos")


     elif opcion == "3":
          for h in historial:
           print(h)
      
     elif opcion == "4":
          print("Saliendo...")
          break
     else:
          print("Opcion invalida")