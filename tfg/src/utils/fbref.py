""" This module contains the constants used in the project. """


class Fbref:
    "Class to store the constants related to fbref.com"

    season_enumerate = enumerate(
        ["2017-2018", "2018-2019", "2019-2020", "2020-2021", "2021-2022", "2022-2023"]
    )

    stats_dict = {
        "Estadisticas_estandar": "jugadores",
        "Porteros": "keepers",
        "Portería_avanzada": "keepersadv",
        "Tiros": "shooting",
        "Pases": "passing",
        "Tipos_de_pases": "passing_types",
        "Creación_de_goles_y_tiros": "gca",
        "Acciones_defensivas": "defense",
        "Posesión_del_balón": "possession",
        "Tiempo_jugado": "playingtime",
        "Estadísticas_diversas": "misc",
    }
