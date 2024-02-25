Obtenemos el fichero de datos de transpasos de la temporada 2022, esto significa lo siguiente:

He scrapeado Fbref hasta el año 2023, por lo que la columna de datos de esta temporada no se va a usar,
para realizar el entrenamiento, ya que son datos de la temporada "fuera de la muestra" (out of sample).

A este fichero se ha obtenido de:
https://github.com/saadism777/Transfermarkt-Data-Analysis
y se ha descargado el archivo transfermarket.csv

A este fichero hay que aplicarle un preprocesado, ya que hay columnas que no se van a usar,
en el caso de usar las columnas de equipo de origen y destino, habría que pasar las variables a numéricas.

De este fichero considero que las columnas que se van a usar son:
-Name
-Position
-Market Value
-Transfer Type
-Fee