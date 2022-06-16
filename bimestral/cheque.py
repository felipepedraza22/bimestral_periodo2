"""Programa para cambiar de bonos a dinero de 100,2000,10000"""

print("------------------------------")
print("-------- Cambiar cheque-------")
print("------------------------------")

#Entrada

Valor_del_cheque = int (input ('Ingresa el valor'))
total_monedas_de_100=0
total_billetes_de_10000=0
total_billetes_de_2000=0

#Processing
while Valor_del_cheque !=0:
    monedas_de_100=Valor_del_cheque
    billetes_de_10000=(monedas_de_100-monedas_de_100%10000)//10000
    monedas_de_100=monedas_de_100%10000
    billetes_de_2000=(monedas_de_100-monedas_de_100%2000)//2000
    monedas_de_100=monedas_de_100%2000
    monedas_de_100=(monedas_de_100-monedas_de_100%100)//100
    monedas_de_100=monedas_de_100%100   
    print ('Valor de billetes de 10000: ' + repr (billetes_de_10000))
    print ('Valor de billetes de 2000: ' + repr (billetes_de_2000))
    print ('Valor de monedas de 100: ' + repr (monedas_de_100))
    total_monedas_de_100=total_monedas_de_100 + monedas_de_100
    total_billetes_de_10000=total_billetes_de_10000 + billetes_de_10000
    total_billetes_de_2000=total_billetes_de_2000 + billetes_de_2000
    Valor_del_cheque = int (input ('Ingresa el valor'))


else:
    print("Fin de ingreso de datos")

#output

print("El total de billetes de  diez mil fue" + str(total_billetes_de_10000))
print("El total de billetes de  dos mil fue de " + str(total_billetes_de_2000))
print("El total de monedas de 100 fue de " + str(total_monedas_de_100))
