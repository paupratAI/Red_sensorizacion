def read_and_generate_dat_file(input_filename, output_filename):
    # Diccionario para almacenar los datos extraídos
    data = {
        'INTERSECTIONS': [],
        'PATHS': [],
        'FIXED': [],
        'PROHIBITED': [],
        'path_flow': [],
        'path_intersections': [],
        'intersection_neighborhood': []
    }

    # Leer el archivo de entrada
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    current_key = None
    for line in lines:
        line = line.strip()
        if line in data:
            current_key = line
        elif current_key:
            # Agregar datos a la sección correspondiente
            data[current_key].append(line.split())

    # Escribir el archivo .dat para AMPL
    with open(output_filename, 'w') as file:
        for key, values in data.items():
            file.write(f"set {key} :=\n")
            for value in values:
                file.write(' '.join(value) + '\n')
            file.write(';\n\n')

# Ejemplo de uso
read_and_generate_dat_file('datos.txt', 'model_data.dat')
