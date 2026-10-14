# Reporte de Análisis de Datos - Pandas

`Daniel Gallegos Machine Learning pandas, NC 1392`

## 1. DataFrame Convertido
```text
    Planeta  Distancia_sol  Lunas
0  Mercurio           57.9      0
1     Venus          108.2      0
2    Tierra          149.6      1
3     Marte          227.9      2
4   Júpiter          778.5     79
5   Saturno         1432.0     82
```

## 2.1 Primeras Filas (head)
```text
    Planeta  Distancia_sol  Lunas
0  Mercurio           57.9      0
1     Venus          108.2      0
```

## 2.2 Últimas Filas (tail)
```text
   Planeta  Distancia_sol  Lunas
4  Júpiter          778.5     79
5  Saturno         1432.0     82
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Planeta              str
Distancia_sol    float64
Lunas              int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Planeta        6 non-null      str    
 1   Distancia_sol  6 non-null      float64
 2   Lunas          6 non-null      int64  
dtypes: float64(1), int64(1), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Lunas'
```text
count     6.000000
mean     27.333333
std      41.200324
min       0.000000
25%       0.250000
50%       1.500000
75%      59.750000
max      82.000000
Name: Lunas, dtype: float64
```

## 4. Ordenar Ascendente por Lunas
```text
    Planeta  Distancia_sol  Lunas
0  Mercurio           57.9      0
1     Venus          108.2      0
2    Tierra          149.6      1
3     Marte          227.9      2
4   Júpiter          778.5     79
5   Saturno         1432.0     82
```

## 5. Ordenar Descendente por Distancia_sol
```text
    Planeta  Distancia_sol  Lunas
5   Saturno         1432.0     82
4   Júpiter          778.5     79
3     Marte          227.9      2
2    Tierra          149.6      1
1     Venus          108.2      0
0  Mercurio           57.9      0
```

`Daniel Gallegos Machine Learning pandas, NC 1392`