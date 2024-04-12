def parse_data(file_path, version):
    # Inicialización de todas las listas y diccionarios
    intersections = []
    paths = []
    fixed = []
    prohibited = []
    path_flow = {}
    intersections_paths = []
    intersection_neighborhood = []

    with open(file_path, 'r') as file:
        content = file.read()

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
        elif 'intersection_neighborhood' in header and version == 'b':
            for line in lines[1:]:
                i1, i2 = line.split()
                intersection_neighborhood.append(f'({i1}, {i2})')

    return (intersections, paths, fixed, prohibited, path_flow, intersections_paths, intersection_neighborhood)

def write_dat_file(intersections, paths, fixed, prohibited, path_flow, intersections_paths, dat_file_path, version, intersection_neighborhood=None):
    with open(dat_file_path, 'w') as file:
        file.write(f'set INTERSECTIONS := {" ".join(intersections)};\n')
        file.write(f'set PATHS := {" ".join(paths)};\n')
        file.write(f'set FIXED := {" ".join(fixed)};\n')
        file.write(f'set PROHIBITED := {" ".join(prohibited)};\n')
        file.write(f'set INTERSECTIONS_PATHS := {" ".join(intersections_paths)};\n')
        if version == 'b':
            file.write(f'set NEIGHBORHOOD := {" ".join(intersection_neighborhood)};\n')
        file.write('param pf :=\n')
        for path_id, flow in path_flow.items():
            file.write(f'  {path_id} {flow}\n')
        file.write(';\n')

# Preguntar que
version = input("Ingrese 'a' para generar el archivo model_a.dat perteneciente al primer apartado, o 'b' para generar el archivo model_b.dat, correspondiente al segundo apartado: ").lower()
input_file_path = 'datos.txt'
output_dat_file_path = 'model_a.dat' if version == 'a' else 'model_b.dat'

data = parse_data(input_file_path, version)

# Llamada a la función con los argumentos adecuados
if version == 'a':
    write_dat_file(*data[:6], output_dat_file_path, version)
else:
    write_dat_file(*data[:6], output_dat_file_path, version, data[6])
