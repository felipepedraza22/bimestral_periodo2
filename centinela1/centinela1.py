"""Programa para 
calcular e imprima el código y la nota final de cada estudiante"""


print("----------------------")
print("------NOTAS Y CODIGO FINAL-------")
print("----------------------")

# imput
cod= int (input("Ingrese el codigo del estudiante: "))
if cod!=0:
    Nota1 = float(input("Ingrese la nota de la evaluacion N.1: "))
    Nota2 = float(input("Ingrese la nota de la evaluacion N.2: "))
    Nota3 = float(input("Ingrese la nota de la evaluacion N.3: "))
    Nota4 = float(input("Ingrese la nota de la evaluacion N.4: "))
    Nota5 = float(input("Ingrese la nota de la evaluacion N.5: "))


else :
    print("Final de los datos de entrada")

# Processing
reprobados=0

while cod != 0:
    Nota_defenitiva = (Nota1 + Nota2 + Nota3 + Nota4 + Nota5)/5
    print("El estudiante de código " + str(cod) + " obtuvo una nota definitiva de " + str(Nota_defenitiva))
    cod = int(input("Digite el código del estudiante: "))
if cod!=0:
    Nota1 = float(input("Ingrese la nota de la evaluacion N.1: "))
    Nota2 = float(input("Ingrese la nota de la evaluacion N.2: "))
    Nota3 = float(input("Ingrese la nota de la evaluacion N.3: "))
    Nota4 = float(input("Ingrese la nota de la evaluacion N.4: "))
    Nota5 = float(input("Ingrese la nota de la evaluacion N.5: "))

else:
    print("Fin de los datos de entrada")
if Nota_defenitiva < 3:
    print("reprobo")
    reprobados = reprobados +1

#output
print(str(reprobados)+ "Reprobado la asignatura")