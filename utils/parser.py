import pandas as pd


def read_file_to_df(path):
    # TODO check encodings and maybe add headings
    df = pd.read_csv(path, encoding="cp1251",
                     index_col=False, header=None)

    return df


def parse_file(path):
    df = read_file_to_df(path)

    datetimes = []
    messages = []
    authors = []
    for row in df.index:
        datetimes.append(df[0][row])
        messages.append(df[7][row])
        authors.append(df[8][row])

    return {"datetime": datetimes,
            "message": messages,
            "author": authors}
