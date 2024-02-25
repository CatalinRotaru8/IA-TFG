"""Main module for the TFG project."""

from src.utils.utils import get_file_path
from src.config import ProcessedData, FileName
from src.core.controller import process_merge_yearly_data, process_encode_columns
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from src.utils.data_procesing import encode_columns_in_dataframes


def main():
    """
    Main function for the project
    """
    process_encode_columns()
    # file_names = [
    #     FileName.acciones_defensivas,
    #     FileName.creacion_de_goles_y_tiros,
    #     FileName.estadisticas_diversas,
    #     FileName.estadisticas_estandar,
    #     FileName.pases,
    #     FileName.porteria_avanzada,
    #     FileName.porteros,
    #     FileName.posesion_del_balon,
    #     FileName.tiempo_jugado,
    #     FileName.tipos_de_pases,
    #     FileName.tiros,
    # ]

    # columns_to_encode = [
    #     "País2017-2018",
    #     "País2018-2019",
    #     "País2019-2020",
    #     "País2020-2021",
    #     "País2021-2022",
    #     "País2022-2023",
    # ]

    # encode_columns_in_dataframes(file_names, columns_to_encode)


# df_acciones_defensivas = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.acciones_defensivas), dtype=str
# )
# df_creacion_goles_tiros = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.creacion_de_goles_y_tiros),
#     dtype=str,
# )
# df_est_diversas = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.estadisticas_diversas),
#     dtype=str,
# )
# df_est_estandard = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.estadisticas_estandar),
#     dtype=str,
# )
# df_pases = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.pases), dtype=str
# )
# df_porteria_avanzada = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.porteria_avanzada), dtype=str
# )
# df_porteros = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.porteros), dtype=str
# )
# df_posesion_del_balon = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.posesion_del_balon), dtype=str
# )
# df_tiempo_jugado = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.tiempo_jugado), dtype=str
# )
# df_tipos_de_pases = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.tipos_de_pases), dtype=str
# )
# df_tiros = pd.read_csv(
#     get_file_path(ProcessedData.all_years, FileName.tiros), dtype=str
# )

# columnas = [
#     "País2017-2018",
#     "País2018-2019",
#     "País2019-2020",
#     "País2020-2021",
#     "País2021-2022",
#     "País2022-2023",
# ]

# le = LabelEncoder()
# dataframes = [
#     df_acciones_defensivas,
#     df_creacion_goles_tiros,
#     df_est_diversas,
#     df_est_estandard,
#     df_pases,
#     df_porteria_avanzada,
#     df_porteros,
#     df_posesion_del_balon,
#     df_tiempo_jugado,
#     df_tipos_de_pases,
#     df_tiros,
# ]
# # Entrenamos el label encoder con todos los datos unicos de las columnas de las columnas que nos interesan
# todos_los_datos = pd.concat(
#     [df[col] for df in dataframes for col in columnas if col in df]
# ).unique()
# le.fit(todos_los_datos)

# # Transformamos los datos de las columnas que nos interesan usando el mismo label encoder
# for df in dataframes:
#     for col in columnas:
#         if col in df:
#             df[col] = le.transform(df[col])

# nombres_archivos = [
#     "acciones_defensivas.csv",
#     "creacion_de_goles_y_tiros.csv",
#     "estadisticas_diversas.csv",
#     "estadisticas_estandar.csv",
#     "pases.csv",
#     "porteria_avanzada.csv",
#     "porteros.csv",
#     "posesion_del_balon.csv",
#     "tiempo_jugado.csv",
#     "tipos_de_pases.csv",
#     "tiros.csv",
# ]

# for df, nombre in zip(dataframes, nombres_archivos):
#     df.to_csv(nombre, index=False)


if __name__ == "__main__":
    main()
