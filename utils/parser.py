import pandas as pd
from datetime import datetime as dt


def read_file_to_df(path):
    # TODO check encodings and maybe add headings
    df = pd.read_csv(path, encoding="cp1251",
                     index_col=False, header=None)

    return df


def parse_file(path):
    df = read_file_to_df(path)
    # TODO add location and chat type parsing
    datetimes = []
    chat_types = []
    coordinates = []

    messages = []
    authors = []

    for row in df.index:

        datetimes.append(dt.strptime(df[0][row], "%m/%d/%Y %H:%M:%S.%f"))
        chat_types.append(df[1][row])
        coordinates.append((df[4][row], df[5][row]))
        messages.append(df[7][row])
        authors.append(df[8][row])

    return {"datetime": datetimes,
            "chat_types": chat_types,
            "coordinates": coordinates,
            "message": messages,
            "author": authors}
