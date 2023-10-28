"""Main module for the TFG project."""
from tfg.src.utils.fbref import Fbref
from tfg.src.utils.downloader import get_big5_data


def main():
    """
    Main function for the project
    """
    get_big5_data(Fbref.stats_dict)


if __name__ == "__main__":
    main()
