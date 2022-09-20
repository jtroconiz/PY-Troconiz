print('funcion año bisiesto, ingrese un año')

año=input("")
while not año.isdigit():
        año=input(f"{año} no es un año no valido, ingrese un numero valido: ")
año=int(año)
def año_bisiesto(a):
        
    if a%4==0 and (a%100!=0 or a%400==0):
        return True
    else:
        return False

if año_bisiesto(año)== True:  
    print(f"{año} es un año bisiesto")
elif año_bisiesto(año)==False:
    print(f"{año} no es un año bisiesto")