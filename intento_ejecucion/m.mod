# Conjuntos
set INTERSECTIONS;
set PATHS;
set FIXED;
set PROHIBITED;
set INTERSECTIONS_PATHS within {INTERSECTIONS, PATHS}; # Conjunto de intersecciones y caminos que están conectados

# Parámetros
param pf {i in PATHS};  # pf_i representa el flujo en el camino i. Utilizar pf[i] para acceder al valor de pf_i

# Variables
var x {i in INTERSECTIONS} binary;
var c {i in PATHS} binary;

# Función objetivo
maximize TotalFlow: sum {i in PATHS} c[i] * pf[i];

# Restricciones
subject to SensorCoverage {i in PATHS}:
    sum {(j,i) in INTERSECTIONS_PATHS} x[j] >= 2 * c[i];

subject to MaxSensors:
    sum {j in INTERSECTIONS} x[j] <= 15;

subject to SensorsFixed{j in FIXED}:
    x[j] = 1;

subject to SensorsProhibited{j in PROHIBITED}:
    x[j] = 0;