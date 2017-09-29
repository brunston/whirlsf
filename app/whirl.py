# whirl backend data and views
# brunston poon

import numpy as np
import pandas as pd

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

        # Ok, so we know there will be some data that we will want to see
        # again and again. Let's create datasets that show that data so
        # that we don't have to do those operations all the time.

        # let's create a combined park dataset with features we care about
        self.parkcom_df = pd.merge(self.parkold_df, self.parknew_df, on="Park")
        # combined park data, grouped by supervisor district
        self.parkgrp_df = self.parkcom_df.groupby(["Supervisor District"])
