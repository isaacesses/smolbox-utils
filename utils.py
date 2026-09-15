from re import fullmatch
from num2words import num2words

#Valida que la estructura del RFC sea valida (3-4 letras al inicio, fecha de 6 números, y 3 caracteres al final)
def validar_rfc(rfc):
    try:
        # Eliminar espacios vacios al principio y al final
        rfc = rfc.strip()
    except:
        # Si no es un string
        print("Tipo de entrada invalido.")
        return False

    # Convertir a mayusculas
    rfc = rfc.upper()

    # Verificar que cumpla con el patron
    pattern = r"^[A-Z]{3,4}\d{6}[A-Z0-9]{3}$"
    if not bool(fullmatch(pattern, rfc)):
        return False
    else:
        return True


# Formatear moneda en el formato $XX,XXX.XX
def formatear_moneda(monto):
    errorMessage = "El monto debe ser número entero o decimal."
    # Verificar que no sea booleana
    if isinstance(monto, bool):
        print(errorMessage)
        return
    
    # Convertir a float y verificar que se pueda
    try:
        monto = float(monto)
    except ValueError:
         print(errorMessage)
         return


    # Redondear a 2 decimales
    monto = round(monto, 2)

    # Agrega separador de miles y asegura que sean 2 decimales
    return(f"${monto:,.2f}")



def numero_a_letras(monto):
    no_a_letras = {0:"CERO", 1:"UN", 2:"DOS", 3:"TRES", 4:"CUATRO", 5:"CINCO", 6:"SEIS", 7:"SIETE", 8:"OCHO", 9:"NUEVE",
                   10:"DIEZ", 11:"ONCE", 12:"DOCE", 13:"TRECE", 14:"CATORCE", 15:"QUINCE", 20:"VEINTE", 30:"TREINTA", 40:"CUARENTA", 50:"CINCUENTA", 60:"SESENTA", 70:"SETENTA", 80:"OCHENTA", 90:"NOVENTA", 100:"CIEN"}

    # Verificar que esté dentro del rango y sea del tipo correcto
    if monto is isinstance(monto, bool):
            print("Tipo invalido. asegurate de ingresar un número entero o decimal entre 0 y 100.")
            return
    try:
        if monto > 100 or monto < 0:
            print("Monto fuera del rango. Para montos mayores a 100 utilize la funcion no_grande_a_letras.")
            return
    except TypeError:
            print("Tipo invalido. asegurate de ingresar un número mayor a 100.")
            return

    # Si el monto es 1, 100, o algun número que no sea combinación de 2
    if monto == 1:
        return(f"{no_a_letras[monto]} PESO 00/100 MXN")
    elif monto >= 0 and monto < 16 or monto == 100:
        if monto % 1 == 0:
            return(f"{no_a_letras[monto]} PESOS 00/100 MXN")
        else:
            decimales = int(round((monto % 1) * 100))
            return(f"{no_a_letras[monto // 1]} PESOS {decimales}/100 MXN")

            
    # Si el monto tiene decenas
    else:
        monto_entero = monto // 1
        decena = no_a_letras[(monto_entero // 10) * 10] 
        entero = no_a_letras[monto_entero % 10]

        if monto % 1 == 0:
            #En caso que sea veintialgo
            if monto > 20 and monto < 30:
                return(f"VEINTI{entero} PESOS 00/100 MXN")
            else:
                return(f"{decena} Y {entero} PESOS 00/100 MXN")
        else:
            decimal = int(round((monto % 1) * 100))
            if monto > 20 and monto < 30:
                return(f"VEINTI{entero} PESOS {decimal}/100 MXN")
            else:
                return(f"{decena} Y {entero} PESOS {decimal}/100 MXN")


# Usando libreria externa para montos mayores que 100
def no_grande_a_letras(monto):
    if monto is isinstance(monto, bool):
            print("Tipo invalido. asegurate de ingresar un número mayor a 100.")
            return
    try:
        if monto < 100:
            print("Monto es menor o igual a 100. Para montos entre 0 y 100 utilize la funcion numero_a_letras.")
            return
    except TypeError:
        print("Tipo invalido. asegurate de ingresar un número mayor a 100.")
        return


    if monto % 1 == 0:
        return(f"{num2words(monto, lang='es').upper()} PESOS 00/100 MXN")
    else:
        decimales = int(round((monto % 1) * 100))
        return(f"{num2words(monto // 1, lang='es').upper()} PESOS {decimales}/100 MXN")
