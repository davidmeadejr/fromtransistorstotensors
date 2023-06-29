import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# set up code checking
import os
if not os.path.exists("../input/fifa.csv"):
    os.symlink("../input/data-for-datavis/fifa.csv", "../input/fifa.csv")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex1 import *
print("Setup Complete")


