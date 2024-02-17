"""Controller module"""

from src.utils.fbref import Fbref
from src.utils.downloader import get_big5_data
from src.utils.utils import clean_all_data, union_transfermarket_file
from src.config import TransfermarktData, TransfermarketFiles


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
    print("2016")
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
