# whirl backend data and views
# brunston poon

import numpy as np
import pandas as pd
from sys import exit

"""
This will contain all our data, as well as any functions we want to use to
explore that data, eg creating views on our primary data dataframes
"""
class Whirl(object):

    def __init__(self, data_dir="", filenames=[]):
        if filenames == [] or data_dir == "":
            raise FileNotFoundError("Need data filenames and/or data directory")

        p_old = data_dir + filenames["park_old"]
        p_new = data_dir + filenames["park_new"]
        library = data_dir + filenames["library"]

        self.parkold_df = pd.read_csv(p_old)
        self.parknew_df = pd.read_csv(p_new)
        self.library_df = pd.read_csv(library)

        self.library_df = self.library_df.dropna(subset=["Supervisor District"])
        self.libmean_df = self.library_df.groupby(["Supervisor District"]).mean()

        # Ok, so we know there will be some data that we will want to see
        # again and again. Let's create datasets that show that data so
        # that we don't have to do those operations all the time.

        # let's create a combined park dataset with features we care about
        self.parkcom_df = pd.merge(self.parkold_df, self.parknew_df, on="Park")
        # combined park data, grouped by supervisor district
        self.parkgrp_df = self.parkcom_df.groupby(["Supervisor District"])

        self.sd_capital = pd.DataFrame(
                                data={
                                    'fin': [74668, 105509, 43513, 77376, 67331,
                                            37431, 94121, 95930, 67989, 55487,
                                            71504],
                                    'edu': [55,78,46,45,63,43,62,71,40,28,28],
                                    'i2': ["SD1", "SD2", "SD3", "SD4", "SD5", "SD6",
                                "SD7", "SD8", "SD9", "SD10", "SD11"],
                                },
                                index=
                                ["SD 1", "SD 2", "SD 3", "SD 4", "SD 5", "SD 6",
                                "SD 7", "SD 8", "SD 9", "SD 10", "SD 11"],
                                )
                         # source: SF Board of Supervisors
 # http://sfbos.org/sites/default/files/FileCenter/Documents/45523-BLA.Socioeconomic%20Equity.nav.pdf
                         # Socioeconomic Equity in the City of San Francisco
                         # "Do things that don't scale" - Paul Graham
                         # (in the context of starting something)

def mean(df):
    return df.mean()


if __name__=='__main__':
    print("Run app.py, not this file.")
    exit()
