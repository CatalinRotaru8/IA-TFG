"""Controller module"""

from src.utils.fbref import Fbref
from src.utils.downloader import get_big5_data
from src.utils.utils import clean_all_data, union_transfermarket_file
from src.config import (
    TransfermarktData,
    TransfermarketFiles,
    ProcessedData,
    FileName,
)
from src.utils.data_procesing import (
    sum_values_from_duplicate_player,
    merge_and_process_yearly_data,
    encode_columns_in_dataframes,
)


def download_clean_data():
    """Download and clean all the data"""
    get_big5_data(Fbref.stats_dict)
    clean_all_data()


def process_transfermarket_data():
    """Process the transfermarket data"""
    union_transfermarket_file(
        file_path=TransfermarktData.files_2016,
        output_name=TransfermarketFiles.files_2016,
    )
    union_transfermarket_file(
        file_path=TransfermarktData.files_2017,
        output_name=TransfermarketFiles.files_2017,
    )
    union_transfermarket_file(
        file_path=TransfermarktData.files_2018,
        output_name=TransfermarketFiles.files_2018,
    )
    union_transfermarket_file(
        file_path=TransfermarktData.files_2019,
        output_name=TransfermarketFiles.files_2019,
    )
    union_transfermarket_file(
        file_path=TransfermarktData.files_2020,
        output_name=TransfermarketFiles.files_2020,
    )
    union_transfermarket_file(
        file_path=TransfermarktData.files_2021,
        output_name=TransfermarketFiles.files_2021,
    )


def process_duplicate_players():
    """Process the duplicate players"""
    excluded_columns = ["País", "Posc", "Equipo", "Comp", "Edad", "Nacimiento"]

    sum_values_from_duplicate_player(
        file_path=ProcessedData.files_17_18,
        excluded_columns=excluded_columns,
    )

    sum_values_from_duplicate_player(
        file_path=ProcessedData.files_18_19,
        excluded_columns=excluded_columns,
    )

    sum_values_from_duplicate_player(
        file_path=ProcessedData.files_19_20,
        excluded_columns=excluded_columns,
    )
    sum_values_from_duplicate_player(
        file_path=ProcessedData.files_20_21,
        excluded_columns=excluded_columns,
    )
    sum_values_from_duplicate_player(
        file_path=ProcessedData.files_21_22,
        excluded_columns=excluded_columns,
    )
    sum_values_from_duplicate_player(
        file_path=ProcessedData.files_22_23,
        excluded_columns=excluded_columns,
    )


def process_merge_yearly_data():
    """Process the merge yearly data"""
    years = [
        "2017-2018",
        "2018-2019",
        "2019-2020",
        "2020-2021",
        "2021-2022",
        "2022-2023",
    ]
    merge_and_process_yearly_data(years, FileName.acciones_defensivas)
    merge_and_process_yearly_data(years, FileName.creacion_de_goles_y_tiros)
    merge_and_process_yearly_data(years, FileName.estadisticas_diversas)
    merge_and_process_yearly_data(years, FileName.estadisticas_estandar)
    merge_and_process_yearly_data(years, FileName.pases)
    merge_and_process_yearly_data(years, FileName.porteria_avanzada)
    merge_and_process_yearly_data(years, FileName.porteros)
    merge_and_process_yearly_data(years, FileName.posesion_del_balon)
    merge_and_process_yearly_data(years, FileName.tiempo_jugado)
    merge_and_process_yearly_data(years, FileName.tipos_de_pases)
    merge_and_process_yearly_data(years, FileName.tiros)


def process_encode_columns():
    """Process the encode columns"""
    file_names = [
        FileName.acciones_defensivas,
        FileName.creacion_de_goles_y_tiros,
        FileName.estadisticas_diversas,
        FileName.estadisticas_estandar,
        FileName.pases,
        FileName.porteria_avanzada,
        FileName.porteros,
        FileName.posesion_del_balon,
        FileName.tiempo_jugado,
        FileName.tipos_de_pases,
        FileName.tiros,
    ]

    columns_dict = {
        "pais": [
            "País2017-2018",
            "País2018-2019",
            "País2019-2020",
            "País2020-2021",
            "País2021-2022",
            "País2022-2023",
        ],
        "posicion": [
            "Posc2017-2018",
            "Posc2018-2019",
            "Posc2019-2020",
            "Posc2020-2021",
            "Posc2021-2022",
            "Posc2022-2023",
        ],
        "equipo": [
            "Equipo2017-2018",
            "Equipo2018-2019",
            "Equipo2019-2020",
            "Equipo2020-2021",
            "Equipo2021-2022",
            "Equipo2022-2023",
        ],
        "competicion": [
            "Comp2017-2018",
            "Comp2018-2019",
            "Comp2019-2020",
            "Comp2020-2021",
            "Comp2021-2022",
            "Comp2022-2023",
        ],
    }

    encode_columns_in_dataframes(file_names, columns_dict)
