import pandas as pd
# import matplotlib.pyplot as plt


# ! Crear el DataFrame inicial

data = {
    "Marcas": ["Postobon", "Cocacola", "Glacial", "Colombiana", "Cuatro"],
    "Ventas": [1200, 1500, 900, 1800, 1300],  
    "Calorias": [150, 140, 100, 120, 110]     
}

# Generar el DataFrame
df = pd.DataFrame(data)

# ! 1. Imprimir el DataFrame

# print("\n--- 1 DataFrame Inicial ---\n")
# print(df)


# ! 2. Añadir nuevos elementos al DataFrame

# nuevo_dato = pd.DataFrame([{"Marcas": "Pepsi", "Ventas": 1250, "Calorias": 130}])
# * "ignore_index" ignora los índices originales de los datos que se agregan y genera un nuevo índice secuencial.
# df = pd.concat([df, nuevo_dato], ignore_index=True)
# print("\n---  2 DataFrame despues de colocar un nuevo elemento ---\n")
# print(df)

# * Calcular los totales por columna (para las columnas numéricas)
# totales = df[["Ventas", "Calorias"]].sum()

# * Agregar una nueva fila con los totales
# df.loc["Total"] = totales
# * Mostrar dataFrame con valores totales
# print(df)

# ! 3. Localizar una columna específica

# print("\n---  3 Columna 'Ventas' ---\n")
# print(df["Ventas"])

# ! 4. Localizar uno o varios elementos

# print("\n--- 4 Datos de la marca 'Cocacola' ---\n")
# print(df[df["Marcas"] == "Cocacola"])

# * Ventas mayores a 1000
# resultado = df[df["Ventas"] > 1000]
# print(resultado)

# * Por indice
# resultado = df.iloc[0]
# print(resultado)


# ! 5. Editar un dato "Cambiar las ventas de "Cocacola" a 1700"

# df.loc[df["Marcas"] == "Cocacola", "Ventas"] = 1700
# print(df)


# ! 6. Eliminar un elemento del DataFrame

# * Eliminamos la fila donde "Marcas" es "Glacial"
# df = df[df["Marcas"] != "Glacial"]
# print("\n--- 5 DataFrame despues de eliminar la marca 'Glacial' ---\n")
# print(df)

# ! 7. Calcular la moda, media y mediana de la columna "Ventas"

# print("\n--- Estadisticas de la columna 'Ventas' ---\n")
# print("Moda:", df["Ventas"].mode()[0])
# print("Media:", df["Ventas"].mean())
# print("Mediana:", df["Ventas"].median())
# * Generar cuartiles, datos min y max, desviacion estandar
# print(df.describe()) # * columnas con datos numericos


# ! 8. Escribir el DataFrame a un archivo CSV

# df.to_csv("gaseosas.csv", index=False)
# * Con index=False, el archivo CSV solo tendrá las columnas de datos (sin la columna de índice).
# print("\n--- DataFrame guardado en 'gaseosas.csv' ---")

# ! Generar graficos

# ! 9. Generar un gráfico simple de barras para las Ventas por Marca

# df.plot(kind='bar', x='Marcas', y='Ventas', legend=False, color='skyblue')
# plt.title('Ventas por Marca')
# plt.xlabel('Marcas')
# plt.ylabel('Ventas')

# * Guardar el gráfico como un archivo PNG
# plt.savefig('ventas.png')
# plt.show()


# ! 10. Generar grafico circular de las calorías
 
# plt.figure(figsize=(8, 8))
# plt.pie(df["Calorias"], labels=df["Marcas"], autopct='%1.1f%%', startangle=90)
# plt.title("Distribución de Calorías por Marca")
# plt.show()
