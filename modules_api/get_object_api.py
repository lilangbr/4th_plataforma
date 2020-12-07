import numpy as np
import pandas as pd


def get_txt_to_df(src_file):
    df = pd.read_csv(src_file, sep = ';', skiprows=1, header=None, names = ['Time', 'Heroe', 'Lap', 'TimeLap', 'Speed'])
    return df
