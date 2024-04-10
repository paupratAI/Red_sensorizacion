# Conjuntos
set INTERSECTIONS;
set PATHS;
set FIXED;
set PROHIBITED;
set INTERSECTIONS_PATHS; # Conjunto de intersecciones y caminos que están conectados

# Parámetros
param pf {i in PATHS};  # pf_i representa el flujo en el camino i. Utilizar pf[i] para acceder al valor de pf_i

# Variables
var x {i in INTERSECTIONS} binary;
var c {i in PATHS} binary;

# Función objetivo
maximize TotalFlow: sum {i in PATHS} c[i] * pf[i];

# Restricciones
subject to SensorCoverage {i in PATHS}:
    sum {j in INTERSECTIONS : (j,i) in INTERSECTIONS_PATHS} x[j] >= 2 * c[i];

subject to MaxSensors:
    sum {j in INTERSECTIONS} x[j] <= 15;

subject to SensorsFixed:
    x[j] = 1 for {j in FIXED};

subject to SensorsProhibited:
    x[j] = 0 for {j in PROHIBITED};