from datetime import datetime as dt
from pathlib import Path
from io import StringIO

import pandas as pd

from config.parser_config import LOG_FILES_DIR, LOG_FILE_EXTENSION


def get_last_file_path():
    """
    Getting the path of the last
    edited file in specified directory
    """
    log_files = Path(LOG_FILES_DIR).glob(LOG_FILE_EXTENSION)
    latest_file_path = max(log_files, key=lambda p: p.stat().st_ctime)

    return latest_file_path


def read_file_to_df(content: str):
    """
    Making a dataframe object from given content

    :param content: string object with content which will be parsed to dataframe object
    """
    content_io = StringIO(content)
    dataframe = pd.read_csv(content_io, encoding="cp1251", index_col=False, header=None)

    return dataframe


def parse_file_content(content):
    """
    Parsing all necessary information from given content

    :param content: string object with content which will be parsed
    """
    dataframe = read_file_to_df(content)

    datetimes = []
    chat_types = []
    coordinates = []

    messages = []
    authors = []

    for row in dataframe.index:
        datetimes.append(dt.strptime(dataframe[0][row], "%m/%d/%Y %H:%M:%S.%f"))
        chat_types.append(dataframe[1][row])
        coordinates.append((dataframe[4][row], dataframe[5][row]))
        messages.append(dataframe[7][row])
        authors.append(dataframe[8][row])

    return {"datetime": datetimes,
            "chat_types": chat_types,
            "coordinates": coordinates,
            "message": messages,
            "author": authors}
