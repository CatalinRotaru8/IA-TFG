"""File to store the configuration of the project."""

import os
from pathlib import Path


class Directories:
    """Class to make it easier to access the project folders."""

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    def get_project_root(self) -> str:
        """
        Get the project root folder.

        Returns:
            str: Project root folder.
        """
        return str(Path(__file__).parent.parent)


class OriginalData:
    """Class to store the paths of the data folders."""

    files = "/data/original_data/"
    # Path to the year folders where the data is stored
    files_17_18 = "/data/original_data/2017-2018/"
    files_18_19 = "/data/original_data/2018-2019/"
    files_19_20 = "/data/original_data/2019-2020/"
    files_20_21 = "/data/original_data/2020-2021/"
    files_21_22 = "/data/original_data/2021-2022/"
    files_22_23 = "/data/original_data/2022-2023/"


class CleanData:
    """Class to store the paths of the clean data folders."""

    # Path to the year folders where the data is stored
    files_17_18 = "/data/clean_data/2017-2018/"
    files_18_19 = "/data/clean_data/2018-2019/"
    files_19_20 = "/data/clean_data/2019-2020/"
    files_20_21 = "/data/clean_data/2020-2021/"
    files_21_22 = "/data/clean_data/2021-2022/"
    files_22_23 = "/data/clean_data/2022-2023/"


class ProcessedData:
    """Class to store the paths of the processed data folders."""

    files_17_18 = "/data/processed_data/2017-2018/"
    files_18_19 = "/data/processed_data/2018-2019/"
    files_19_20 = "/data/processed_data/2019-2020/"
    files_20_21 = "/data/processed_data/2020-2021/"
    files_21_22 = "/data/processed_data/2021-2022/"
    files_22_23 = "/data/processed_data/2022-2023/"
    all_years = "/data/processed_data/all_years/"


class InputData:
    """Class to store the paths of the input data folders."""


class TransfermarktData:
    """Class to store the paths of the processed data folders."""

    files_2016 = "/data/TransferMarket/player_transfers/2016/"
    files_2017 = "/data/TransferMarket/player_transfers/2017/"
    files_2018 = "/data/TransferMarket/player_transfers/2018/"
    files_2019 = "/data/TransferMarket/player_transfers/2019/"
    files_2020 = "/data/TransferMarket/player_transfers/2020/"
    files_2021 = "/data/TransferMarket/player_transfers/2021/"


class TransfermarketFiles:
    """Class to store the names of the files."""

    files_2016 = "2016.csv"
    files_2017 = "2017.csv"
    files_2018 = "2018.csv"
    files_2019 = "2019.csv"
    files_2020 = "2020.csv"
    files_2021 = "2021.csv"


class TransferMarketFilesOriginalData:
    """Class to store the names of the files."""

    bundesliga = "1-bundesliga.csv"
    eredivisie = "eredivisie.csv"
    juliper_pro_league = "jupiler_pro_league.csv"
    la_liga = "la_liga.csv"
    ligue_1 = "ligue_1.csv"
    premier_league = "premier_league.csv"
    premier_liga = "premier_liga.csv"
    primeira_liga = "primeira_liga.csv"
    scottish_premiership = "scottish_premiership.csv"
    serie_a = "serie_a.csv"


class DeleteLines:
    """Class to store the lines to delete from the data."""

    # pylint = "pylint: disable=line-too-long"
    acciones_defensivas = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,90 s,Tkl,TklG,3.º def.,3.º cent.,3.º ataq.,Tkl,Att,Tkl%,Pérdida,Bloqueos,Dis,Pases,Int,Tkl+Int,Desp.,Err,Partidos"
    creacion_de_goles_y_tiros = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,90 s,ACT,SCA90,PassLive,PassDead,HASTA,Dis,FR,Def,ACG,GCA90,PassLive,PassDead,HASTA,Dis,FR,Def,Partidos"
    estadisticas_diversas = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,90 s,TA,TR,2a amarilla,Fls,FR,PA,Pcz,Int,TklG,Penal ejecutado,Penal concedido,GC,Recup.,Ganados,Perdidos,% de ganados,Partidos"
    estadisticas_estandar = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,PJ,Titular,Mín,90 s,Gls.,Ass,G+A,G-TP,TP,TPint,TA,TR,xG,npxG,xAG,npxG+xAG,PrgC,PrgP,PrgR,Gls.,Ast,G+A,G-TP,G+A-TP,xG,xAG,xG+xAG,npxG,npxG+xAG"
    pases = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,90 s,Cmp,Int.,% Cmp,Dist. tot.,Dist. prg.,Cmp,Int.,% Cmp,Cmp,Int.,% Cmp,Cmp,Int.,% Cmp,Ass,xAG,xA,A-xAG,PC,1/3,PPA,CrAP,PrgP,Partidos"
    porteria_avanzada = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,90 s,GC,PD,TL,TE,GC.1,PSxG,PSxG/SoT,PSxG+/-,/90,Cmp,Int.,% Cmp,Int.,TI,%deLanzamientos,Long. prom.,Int.,%deLanzamientos,Long. prom.,Opp,Stp,% de Stp,Núm. de OPA,Núm. de OPA/90,DistProm.,Partidos"
    porteros = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,PJ,Titular,Mín,90 s,GC,GC90,DaPC,Salvadas,% Salvadas,PG,PE,PP,PaC,PaC%,TPint,PD,PD.1,PC,% Salvadas,Partidos"
    posesion_del_balon = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,90 s,Toques,Def. pen.,3.º def.,3.º cent.,3.º ataq.,Ataq. pen.,Balón vivo,Att,Succ,Exitosa%,Tkld,Tkld%,Transportes,Dist. tot.,Dist. prg.,PrgC,1/3,TAP,Errores de control,Des,Rec,PrgR,Partidos"
    tiempo_jugado = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,PJ,Mín,Mn/PJ,% min,90 s,Titular,Mn/arranque,Compl,Sup,Mn/Sust,Partidos como sustituto,PPP,onG,onGA,+/-,+/-90,Dentro-Fuera,onxG,onxGA,xG+/-,xG+/-90,Dentro-Fuera,Partidos"
    tipos_de_pases = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,90 s,Int.,Balón vivo,Balón muerto,FK,PL,Camb.,Pcz,Lanz.,SE,Dentro,Fuera,Rect.,Cmp,PA,Bloqueos,Partidos"
    tiros = "RL,Jugador,País,Posc,Equipo,Comp,Edad,Nacimiento,90 s,Gls.,Dis,DaP,% de TT,T/90,TalArc/90,G/T,G/TalArc,Dist,FK,TP,TPint,xG,npxG,npxG/Sh,G-xG,np:G-xG,Partidos"


class FileName:
    """Class to store the names of the files."""

    acciones_defensivas = "Acciones_defensivas.csv"
    creacion_de_goles_y_tiros = "Creación_de_goles_y_tiros.csv"
    estadisticas_diversas = "Estadísticas_diversas.csv"
    estadisticas_estandar = "Estadisticas_estandar.csv"
    pases = "Pases.csv"
    porteria_avanzada = "Portería_avanzada.csv"
    porteros = "Porteros.csv"
    posesion_del_balon = "Posesión_del_balón.csv"
    tiempo_jugado = "Tiempo_jugado.csv"
    tipos_de_pases = "Tipos_de_pases.csv"
    tiros = "Tiros.csv"
