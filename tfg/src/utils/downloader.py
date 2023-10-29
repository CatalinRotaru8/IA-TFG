""" Module to download data from fbref.com """
import os
import pandas as pd
from src.utils.fbref import Fbref
from src.config import OriginalData


def make_url(season: str, stats: str) -> str:
    """Create url for season."""

    if season == "":
        # 2022-2023
        return f"https://fbref.com/es/comps/Big5/stats/{stats}/Estadisticas-de-Las-5-grandes-ligas-europeas"  # pylint: disable=line-too-long
    else:
        return f"https://fbref.com/es/comps/Big5/{season}/{stats}/jugadores/Estadisticas-{season}-Las-5-grandes-ligas-europeas"  # pylint: disable=line-too-long


def get_big5_data(stats: dict) -> pd.DataFrame:
    """Get data from season."""
    all_data = []  # List to store all data

    for season in Fbref.season_enumerate:
        print(f"{season[1]}")
        season_data = []  # List to store data from season

        for key, stat in stats.items():
            print(f"Downloading {key} from {season[1]}")
            url = make_url(season[1], stat)
            # print(url)
            data = pd.read_html(url)[0]
            save_data(data, season[1], key)
        all_data.append(season_data)

    return data


def save_data(data: pd.DataFrame, season: str, stat: str) -> None:
    """Save data to csv."""
    folder_path = os.path.join(os.getcwd() + OriginalData.files, f"{season}")
    os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
    file_path = os.path.join(folder_path, f"{stat}.csv")
    data.to_csv(file_path, index=False)
