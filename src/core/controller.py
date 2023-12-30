"""Controller module"""
from src.utils.fbref import Fbref
from src.utils.downloader import get_big5_data
from src.utils.utils import clean_all_data


def download_clean_data():
    """Download and clean all the data"""
    get_big5_data(Fbref.stats_dict)
    clean_all_data()
