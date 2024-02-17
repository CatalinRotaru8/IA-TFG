"""Main module for the TFG project."""

import pandas as pd
from src.config import (
    InputData,
    ProcessedData,
    FileName,
    TransfermarketFiles,
    TransfermarktData,
)
from src.utils.utils import get_file_path
from src.core.controller import process_transfermarket_data


def main():
    """
    Main function for the project
    """
    # process_transfermarket_data()  # descomentar los años que se quieran procesar de la funcion
    df_estadisticas = pd.read_csv(
        get_file_path(ProcessedData.files_17_18, FileName.estadisticas_estandar)
    )
    df_transpasos = pd.read_csv(
        get_file_path(TransfermarktData.files_2016, TransfermarketFiles.files_2016)
    )

    # df_transpasos.to_csv("transpasos.csv", index=False)
    # df_transpasos = df_transpasos.query("movement == 'in'")
    # df_transpasos = df_transpasos.query("window == 'summer'")
    df_transpasos = df_transpasos.drop_duplicates()

    df_union = pd.merge(
        df_estadisticas,
        df_transpasos,
        left_on=["Jugador"],
        right_on=["name"],
        how="inner",
        validate="many_to_many",
    )
    print(df_union.shape)

    output_file_path = InputData.files_2016 + FileName.estadisticas_estandar
    print(output_file_path)

    df_union.to_csv(
        get_file_path(InputData.files_2016, FileName.estadisticas_estandar),
        index=False,
    )
    # hacer unique a los ficheros de los fichajes de transfermarkt


if __name__ == "__main__":
    main()


# # # # # # def main():
# # # # # #     """
# # # # # #     Main function for the project
# # # # # #     """
# # # # # #     # process_transfermarket_data()  descomentar los años que se quieran procesar de la funcion
# # # # # #     df_estadisticas = pd.read_csv(
# # # # # #         get_file_path(ProcessedData.files_17_18, FileName.estadisticas_estandar)
# # # # # #     )
# # # # # #     df_transpasos = pd.read_csv(
# # # # # #         get_file_path(TransfermarktData.files_2016, TransfermarketFiles.files_2016)
# # # # # #     )
# # # # # #     # columnas_deseadas = [
# # # # # #     #     "name",
# # # # # #     #     "window",
# # # # # #     #     "team_in",
# # # # # #     #     "team_out",
# # # # # #     #     "value",
# # # # # #     #     "fee",
# # # # # #     #     "date",
# # # # # #     # ]
# # # # # #     # df_transpasos = df_transpasos.unique(["club", "name"])
# # # # # #     # unique_values = df_transpasos[["club", "name", "dealing_club"]].drop_duplicates()
# # # # # #     # print(unique_values)

# # # # # #     # df_transpasos.to_csv("transpasos.csv", index=False)
# # # # # #     df_transpasos = df_transpasos.drop_duplicates()
# # # # # #     df_transpasos = df_transpasos.query("window == 'summer'")

# # # # # #     df_union = pd.merge(
# # # # # #         df_estadisticas,
# # # # # #         df_transpasos,  # unique_values, y ver que pasa
# # # # # #         left_on=["Jugador"],
# # # # # #         right_on=["name"],
# # # # # #         how="inner",
# # # # # #         validate="many_to_many",
# # # # # #     )
# # # # # #     print(df_union.shape)

# # # # # #     output_file_path = InputData.files_2016 + FileName.estadisticas_estandar
# # # # # #     print(output_file_path)

# # # # # #     df_union.to_csv(
# # # # # #         get_file_path(InputData.files_2016, FileName.estadisticas_estandar),
# # # # # #         index=False,
# # # # # #     )
# # # # # #     # hacer unique a los ficheros de los fichajes de transfermarkt


# # # # # # if __name__ == "__main__":
# # # # # #     main()
