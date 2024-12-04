import os
import pandas as pd

# Directorio donde están los archivos CSV
input_directory = os.path.dirname(os.path.realpath(__file__))
output_file = os.path.join(input_directory, "combined_descriptors.csv")

# Lista para almacenar los DataFrames de cada archivo CSV
dfs = []

# Iterar sobre los archivos CSV en el directorio
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_directory, filename)
        try:
            # Leer el archivo CSV
            df = pd.read_csv(file_path)
            # Añadir una columna con el nombre del archivo (por si quieres identificar de dónde provienen los datos)
            df['source_file'] = filename
            dfs.append(df)
        except Exception as e:
            print(f"Error leyendo {filename}: {e}")

# Combinar todos los DataFrames en uno solo
if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    # Guardar el archivo combinado
    combined_df.to_csv(output_file, index=False)
    print(f"Archivos combinados guardados en {output_file}")
else:
    print("No se encontraron archivos CSV para combinar.")
