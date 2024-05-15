## Optimización de una Red de Sensorización en l'Eixample, Barcelona

### Descripción

Este proyecto optimiza la ubicación de sensores para captar el flujo de vehículos en las intersecciones más críticas de l'Eixample, Barcelona. Se busca maximizar la detección del flujo con un máximo de 15 sensores, respetando restricciones específicas.

### Objetivos

- **Ubicación óptima de sensores**: Colocar hasta 15 sensores en intersecciones para maximizar el flujo detectado.
- **Restricciones**:
  - Intersecciones obligatorias y prohibidas.
  - Distancia mínima de 300 metros entre sensores (solo en el apartado b).

### Herramientas

- **Modelado**: Programación lineal entera.
- **Software**: AMPL y solver CPLEX.

### Archivos

- **main.py**: Preprocesa datos y genera archivos `.dat`.
- **model_a.mod**, **model_b.mod**: Modelos para cada apartado.
- **model_a.dat**, **model_b.dat**: Datos para cada modelo.
- **model_a.run**, **model_b.run**: Ejecuta el modelo con CPLEX.

### Ejecución

1. Ejecutar `main.py` para generar archivos de datos.
2. En AMPL, ejecutar:
   - Apartado a: `include model_a.run;`
   - Apartado b: `include model_b.run;`

### Resultados

- **Apartado a**:
  - Flujo total: 350.734
  - Intersecciones con sensores: {5, 30, 78, 20349, 41633, 41967, 41977, 44494, 44609, 44628, 45173, 45481, 45555, 45787, 49180}

- **Apartado b**:
  - Flujo total: 350.178
  - Intersecciones con sensores: {5, 30, 78, 41633, 41653, 41979, 44522, 44609, 44628, 45173, 45481, 45555, 45787, 49180, 54858}

## Conclusión

El modelo optimizado maximiza la detección del flujo vehicular cumpliendo con las restricciones dadas. La restricción adicional en el apartado b) afecta ligeramente el flujo total captado.
