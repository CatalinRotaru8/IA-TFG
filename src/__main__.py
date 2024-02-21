"""Main module for the TFG project."""

from src.utils.utils import get_file_path
from src.config import ProcessedData, FileName
from src.core import controller

import pandas as pd


def main():
    """
    Main function for the project
    """
    controller.process_duplicate_players()

    # orginal_df = pd.read_csv(
    #     get_file_path(ProcessedData.files_17_18, FileName.estadisticas_estandar)
    # )
    # columnas_excluidas = ["País", "Posc", "Equipo", "Comp", "Edad", "Nacimiento"]
    # df_numeric = orginal_df[orginal_df.columns.difference(columnas_excluidas)]

    # # Lista de columnas a convertir(todas menos 'Jugador' que es string)
    # cols_to_convert = df_numeric.columns.difference(["Jugador"])

    # # Convertir las columnas a numéricas
    # for col in cols_to_convert:
    #     df_numeric.loc[:, col] = pd.to_numeric(df_numeric[col], errors="coerce")
    # # convert to numeric
    # # df_numeric.loc[:, "PJ"] = pd.to_numeric(df_numeric["PJ"], errors="coerce").fillna(0)

    # df_sum = df_numeric.groupby("Jugador").sum().reset_index()

    # df_excluded = orginal_df[columnas_excluidas + ["Jugador"]].drop_duplicates(
    #     "Jugador"
    # )
    # # Asegurarse de que 'Jugador' es del mismo tipo en ambos dataframes
    # df_excluded["Jugador"] = df_excluded["Jugador"].astype(str)
    # df_sum["Jugador"] = df_sum["Jugador"].astype(str)

    # processed_df = pd.merge(
    #     df_excluded,
    #     df_sum,
    #     on="Jugador",
    #     how="left",
    #     validate="one_to_one",
    # )
    # processed_df = processed_df.reindex(columns=orginal_df.columns).rename(
    #     columns=lambda x: x + "_17-18"
    # )
    # processed_df.to_csv("processed_data.csv", index=False)


if __name__ == "__main__":
    main()
