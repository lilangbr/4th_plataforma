import numpy as np
import pandas as pd


def get_txt_to_df(src_file):
    df = pd.read_csv(src_file, sep = ';')
    time, heroe, lap, timelap, speed = df.columns
    return df
