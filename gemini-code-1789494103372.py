# 1. Importamos las "herramientas" que necesitamos
import pandas as pd               # Para manejar tablas de datos (como Excel)
import matplotlib.pyplot as plt   # Para dibujar gráficos

# 2. Leemos el archivo original (asumimos que usamos el CSV)
print("Leyendo el archivo de datos...")
df = pd.read_csv('TIC_100_estudiantes.csv')

# 3. Procesamos los datos: Creamos una tabla resumen con el promedio de las notas y horas
tabla_resumen = df.describe()

# 4. Creamos un gráfico: Relación entre Horas de estudio y Nota final
plt.figure(figsize=(8, 5))
plt.scatter(df['Horas_estudio_semana'], df['Nota_final'], color='blue', alpha=0.6)
plt.title('Relación entre Horas de Estudio y Nota Final')
plt.xlabel('Horas de estudio a la semana')
plt.ylabel('Nota Final')
plt.grid(True)

# 5. GUARDAMOS EXACTAMENTE TRES ARCHIVOS FINALES (En la carpeta 03_salidas)

# Archivo final 1: Guardamos el gráfico como imagen (.png)
plt.savefig('grafico_relacion_notas.png')
print("¡Archivo 1 guardado: grafico_relacion_notas.png!")

# Archivo final 2: Guardamos la tabla resumen en un nuevo CSV
tabla_resumen.to_csv('tabla_estadisticas_resumen.csv')
print("¡Archivo 2 guardado: tabla_estadisticas_resumen.csv!")

# Archivo final 3: Filtramos solo a los estudiantes que aprobaron (nota mayor a 10) y los guardamos
estudiantes_aprobados = df[df['Nota_final'] >= 10.5]
estudiantes_aprobados.to_csv('estudiantes_aprobados.csv', index=False)
print("¡Archivo 3 guardado: estudiantes_aprobados.csv!")

print("¡Proceso terminado con éxito!")