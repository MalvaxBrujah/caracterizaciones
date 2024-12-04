# -*- coding: utf-8 -*-

import os
from rdkit import Chem
from mordred import Calculator, descriptors
import pandas as pd

def process_sdf_files():
    # Obtener el directorio donde se encuentra el script de Python
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Inicializar el calculador de descriptores
    calc = Calculator(descriptors, ignore_3D=True)

    # Recorrer todos los archivos en el directorio actual
    for filename in os.listdir(current_directory):
        if filename.endswith('.sdf'):
            # Ruta completa al archivo SDF
            sdf_file = os.path.join(current_directory, filename)
            
            # Cargar las moléculas desde el archivo SDF
            suppl = Chem.SDMolSupplier(sdf_file)
            mols = [mol for mol in suppl if mol is not None]
            
            # Calcular los descriptores para las moléculas en el archivo SDF
            if mols:
                descriptors_df = calc.pandas(mols, nproc=1)
                
                # Nombre del archivo de salida CSV
                output_file = os.path.join(current_directory, f"{os.path.splitext(filename)[0]}.csv")
                
                # Guardar los descriptores en un archivo CSV
                descriptors_df.to_csv(output_file, index=False)
                
                print(f"Descriptores guardados en {output_file}")

    print("Procesamiento completado.")

if __name__ == "__main__":
    process_sdf_files()
