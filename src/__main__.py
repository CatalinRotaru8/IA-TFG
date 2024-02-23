"""Main module for the TFG project."""

from src.utils.utils import get_file_path
from src.config import ProcessedData, FileName
from src.core.controller import process_merge_yearly_data
import pandas as pd


def main():
    """
    Main function for the project
    """
    process_merge_yearly_data()
    # acc_def_17_18 = pd.read_csv(
    #     get_file_path(ProcessedData.files_17_18, FileName.acciones_defensivas)
    # )
    # acc_def_18_19 = pd.read_csv(
    #     get_file_path(ProcessedData.files_18_19, FileName.acciones_defensivas)
    # )
    # acc_def_19_20 = pd.read_csv(
    #     get_file_path(ProcessedData.files_19_20, FileName.acciones_defensivas)
    # )
    # acc_def_20_21 = pd.read_csv(
    #     get_file_path(ProcessedData.files_20_21, FileName.acciones_defensivas)
    # )
    # acc_def_21_22 = pd.read_csv(
    #     get_file_path(ProcessedData.files_21_22, FileName.acciones_defensivas)
    # )
    # acc_def_22_23 = pd.read_csv(
    #     get_file_path(ProcessedData.files_22_23, FileName.acciones_defensivas)
    # )

    # acc_def_17_18.rename(columns={"Jugador2017-2018": "Jugador"}, inplace=True)
    # acc_def_18_19.rename(columns={"Jugador2018-2019": "Jugador"}, inplace=True)
    # acc_def_19_20.rename(columns={"Jugador2019-2020": "Jugador"}, inplace=True)
    # acc_def_20_21.rename(columns={"Jugador2020-2021": "Jugador"}, inplace=True)
    # acc_def_21_22.rename(columns={"Jugador2021-2022": "Jugador"}, inplace=True)
    # acc_def_22_23.rename(columns={"Jugador2022-2023": "Jugador"}, inplace=True)

    # result = pd.merge(
    #     acc_def_17_18, acc_def_18_19, on="Jugador", how="outer", validate="one_to_one"
    # )
    # result.drop(
    #     columns=["País2018-2019", "Nacimiento2018-2019", "RL2017-2018"],
    #     axis=1,
    #     inplace=True,
    # )

    # result = pd.merge(
    #     result, acc_def_19_20, on="Jugador", how="outer", validate="one_to_one"
    # )
    # result.drop(
    #     columns=["País2019-2020", "Nacimiento2019-2020", "RL2019-2020"],
    #     axis=1,
    #     inplace=True,
    # )

    # result = pd.merge(
    #     result, acc_def_20_21, on="Jugador", how="outer", validate="one_to_one"
    # )
    # result.drop(
    #     columns=["País2020-2021", "Nacimiento2020-2021", "RL2020-2021"],
    #     axis=1,
    #     inplace=True,
    # )

    # result = pd.merge(
    #     result, acc_def_21_22, on="Jugador", how="outer", validate="one_to_one"
    # )
    # result.drop(
    #     columns=["País2021-2022", "Nacimiento2021-2022", "RL2021-2022"],
    #     axis=1,
    #     inplace=True,
    # )

    # result = pd.merge(
    #     result, acc_def_22_23, on="Jugador", how="outer", validate="one_to_one"
    # )
    # result.drop(
    #     columns=["País2022-2023", "Nacimiento2022-2023", "RL2022-2023"],
    #     axis=1,
    #     inplace=True,
    # )

    # result.fillna(0, inplace=True)
    # result.to_csv(
    #     get_file_path(ProcessedData.all_years, FileName.acciones_defensivas),
    #     index=False,
    # )


if __name__ == "__main__":
    main()
