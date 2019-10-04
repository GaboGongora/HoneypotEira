import re
import time
from decimal import Decimal

import numpy as np
import pandas as pd
from sklearn import cross_validation, neighbors




########################################################################################################################

archivo = r"access.log.1"
regla = '("(.*?)"(.*?))'
lista = []
with open(archivo, "r") as file:
    for lineas in file:
        for acierto in re.finditer(regla, lineas, re.S):
            texto = acierto.group()
            lista.append(texto)
frecuencia = []
for w in lista:
    frecuencia.append(lista.count(w))

log = np.asmatrix (lista, dtype=object)
frecuencia_de_palabra = np.asmatrix(frecuencia, dtype=int)
PrimeraColumna = pd.DataFrame(log)
SegundaColumna = pd.DataFrame(frecuencia_de_palabra)
PrimeraTabla= PrimeraColumna.transpose()
PrimeraTabla.columns = ["SENTENCIA_LOG"]
PrimeraTabla["FRECUENCIA_LOG"] =SegundaColumna.transpose()

PrimeraTabla.drop_duplicates(subset ="SENTENCIA_LOG", inplace = True)

#PrimeraTabla["CLASIFICACION"] = PrimeraTabla.SENTENCIA_LOG.str.contains('Mozilla/5.0','POST').astype(int)

ColumnaBinario=[]
ColumnaDecimal=[]
for PrimeraTabla.Rows in PrimeraTabla.SENTENCIA_LOG:
    Binario="".join(['0'*(8-len(bin(ord(i))[2:]))+(bin(ord(i))[2:]) for i in PrimeraTabla.Rows])
    ColumnaBinario.append(Binario)
    if Binario == 'x':
        exit();
    else:
        decimal = int(Binario, 2);
        DecimalBinario = Decimal(decimal)
    ColumnaDecimal.append(DecimalBinario)
ColumnaBinario = np.asmatrix(ColumnaBinario)
ColumnaDecimal = np.asmatrix(ColumnaDecimal)
Binarios = pd.DataFrame(ColumnaBinario)
Decimales = pd.DataFrame(ColumnaDecimal, dtype=float)
PrimeraTabla["BINARIO"]=Binarios.transpose()
PrimeraTabla["DECIMAL"]=Decimales.transpose()

PrimeraTabla= PrimeraTabla.replace(np.inf, np.nan)

SegundaTabla= PrimeraTabla

SegundaTabla = SegundaTabla.dropna(axis = 0, how ='any')

# pos = np.where(y.flatten()==1)
# neg = np.where(y.flatten()==0)
#
# pl.scatter(X[pos,0], X[pos,1])
# pl.scatter(X[neg,0], X[neg,1])
# pl.show()

#print SegundaTabla
# Primero habian 406

########################################################################################################################
ColumnaPrediccion = []
ColumnaMensaje =[]
for i in SegundaTabla['DECIMAL']:

    Prediccion = clasificacion.predict(i)
    if Prediccion == 1:
        Mensaje ="Se detecto un Ataque"
    else:
        Mensaje ="Ningun Ataque"
    ColumnaMensaje.append(Mensaje)
    ColumnaPrediccion.append(Prediccion)

ColumnaPrediccion = np.asmatrix(ColumnaPrediccion)
ColumnaMensaje = np.asmatrix(ColumnaMensaje)
PrediccionFinal = pd.DataFrame(ColumnaPrediccion)
MensajeFinal = pd.DataFrame(ColumnaMensaje)

TerceraTabla = SegundaTabla
TerceraTabla["PREDICCION"] = PrediccionFinal
TerceraTabla["ALERTA"] =MensajeFinal.transpose()

print TerceraTabla
Log_Del_Ataque = TerceraTabla[TerceraTabla['ALERTA'].str.contains('Se detecto un Ataque', regex=False, case=False, na=False)]
print Log_Del_Ataque




