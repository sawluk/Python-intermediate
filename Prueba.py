# Ejemplos basico de lectura de un archivo en Pandas

import pandas as pd
import numpy as np


# Leyendo y creando un dashboard para archivo

print("Dashboard basico con errores \n")
df = pd.read_csv('hotel-booking-data.txt')
# "head" muestra las primeras cinco filas del DataFrame, útil para obtener una vista rápida de los datos
print(df.head())


# Correccion en el archivo y instrucciones
'''
print("Dashboard mejorado con separaciones \n")
df = pd.read_csv('hotel-booking-data.txt', delimiter='\t')
print(df.head())

print("\n--------Estadistica descriptiva-----------\n")
# "describe" genera las estadisticas descriptivas de campos en el daata frame
print(df.describe())

print("\n--------Contando valores-----------\n")
# "value_counts" se utiliza para contar cuántas veces aparece cada valor en la columna especificada
print(df['Company'].value_counts())

print("\n--------Eliminando errores-----------\n")
# "dropna" se encarga de remover filas que contienen valores nulos en el DataFrame
# Como tal esto seria para generar un nuevo dataframe, no corrige el original
print(df.dropna())

print("\n--------Operando una columna-----------\n")
# Columnas con valores numericos pueden operarse si se desean y crearse como nuevas
df['2xRoom'] = df['Room number'] * 2
print(df)
'''

# Ejemplo de copiar y poner otro dataframe
'''
print("\nCreando otro dashboard con corecciones \n")
df = pd.read_csv('hotel-booking-data.txt', delimiter='\t')
df2 = df.dropna()
print(df2.head())
'''



# Mas funcionalidades
'''
print("\nCreando otro dashboard con para pruebas \n")
df = pd.read_csv('hotel-booking-data.txt', delimiter='\t')
print(df.head())


print("\nObservando donde hay valores NA \n")
# "isna" se utiliza para identificar valores nulos (NA) marcandolos como true o false, la columna se especifica
print(df["Room number"].isna())

print("\nProceso de corrección de datos\n")

# Paso 1: Reemplazo de valores NA
print("\nPaso 1: Reemplazo de valores NA\n")
# Creamos una máscara para identificar valores nulos en la columna 'Room number'.
mask = df["Room number"].isna()
# Con "where" se agsina los valores de la columna 'Date' a 'Text Value' donde hay valores nulos en 'Room number'.
# Si no hay valores nulos, se asigna el valor encontrado a 'Text Value'.
df['Text Value'] = np.where(mask, df['Date'], np.nan)
print(df.head())

# Paso 2: Relleno y limpieza de datos
print("\nPaso 2: Eliminacion de valores NA y relleno adecuado\n")
# "fillna" se usa junto 'bfill' para llenar valores nulos en 'Text Value' 
# con el siguiente valor no nulo disponible. Ayudda completar datos sin perder información útil.
df['Text Value'] = df['Text Value'].bfill()
df.dropna(inplace=True)
print(df.head())

'''