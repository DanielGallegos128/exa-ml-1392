import sys
import os
import pandas as pd

# Permitir importar dicc-0777.py desde la subcarpeta hermana
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-1392')))
import dicc_1392

print("Daniel Gallegos Machine Learning pandas, NC 1392")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Daniel Gallegos Machine Learning pandas, NC 1392"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_1392.datos_planetas)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
import io
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Precio)
registrar("3. Estadísticas Generales de la Columna 'Lunas'", df['Lunas'].describe())

# 4. Ordenar Ascendente por Precio
df_asc_lunas = df.sort_values(by="Lunas", ascending=True)
registrar("4. Ordenar Ascendente por Lunas", df_asc_lunas)

# 5. Ordenar Descendente por Stock
df_desc_stock = df.sort_values(by="Distancia_sol", ascending=False)
registrar("5. Ordenar Descendente por Distancia_sol", df_desc_stock)

# 7. Guardar el archivo resultados-ml-0777.md dentro de resultados-0777
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-1392'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-1392.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Daniel Gallegos Machine Learning pandas, NC 1392")
