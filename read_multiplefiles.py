import pandas as pd
from glob import glob
import os

os.chdir('d://python//pandas')
files = glob('log*')
sorted_files = sorted(files, reverse=True)
data = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)
print(data.to_string())