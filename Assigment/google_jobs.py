import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# read the data set using pandas .read_csv() method
df_job_skills = pd.read_csv('google.csv')
# print the top 5 row from the dataframe
#df_job_skills.head()

print(df_job_skills.columns)

print(df_job_skills.groupby(df_job_skills['Category']))




x = np.linspace(-6, 6, num = 1000)
plt.figure(figsize = (12,8))
plt.plot(x, 1 / (1 + np.exp(-x)))
plt.title("Sigmoid Function")
plt.show()
