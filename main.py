def parse_data(file_path):
    # Diccionarios para almacenar los datos
    intersections = []
    paths = []
    fixed = []
    prohibited = []
    path_flow = {}
    intersections_paths = []
    
    # Leer el archivo
    with open(file_path, 'r') as file:
        content = file.read()
        
    # Dividir los contenidos por secciones
    sections = content.split('\n\n')
    for section in sections:
        lines = section.split('\n')
        header = lines[0].strip()
        
        if 'INTERSECTIONS' in header:
            intersections = lines[1].split('\t')
        elif 'PATHS' in header:
            paths = lines[1].split('\t')
        elif 'FIXED' in header:
            fixed = lines[1].split()
        elif 'PROHIBITED' in header:
            prohibited = lines[1].split()
        elif 'path_flow' in header:
            for line in lines[1:]:
                path_id, flow = line.split()
                path_flow[path_id] = flow
        elif 'path_intersections' in header:
            for line in lines[1:]:
                path_id, intersection_id = line.split()
                intersections_paths.append(f'({intersection_id}, {path_id})')

    return intersections, paths, fixed, prohibited, path_flow, intersections_paths

def write_dat_file(intersections, paths, fixed, prohibited, path_flow, intersections_paths, dat_file_path):
    with open(dat_file_path, 'w') as file:
        file.write(f'set INTERSECTIONS := {" ".join(intersections)};\n')
        file.write(f'set PATHS := {" ".join(paths)};\n')
        file.write(f'set FIXED := {" ".join(fixed)};\n')
        file.write(f'set PROHIBITED := {" ".join(prohibited)};\n')
        file.write(f'set INTERSECTIONS_PATHS := {" ".join(intersections_paths)};\n')
        file.write('param pf :=\n')
        for path_id, flow in path_flow.items():
            file.write(f'  {path_id} {flow}\n')
        file.write(';\n')

# Ruta al archivo de entrada y salida
input_file_path = 'datos.txt'
output_dat_file_path = 'model.dat'

# Procesar los datos
data = parse_data(input_file_path)
# Escribir el archivo .dat
write_dat_file(*data, output_dat_file_path)
