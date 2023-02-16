import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\baloo\\PycharmProjects\\HW1\\DataScience\\education_Data.csv",
                 usecols=["TIME", "GEO", "Value"], na_values=":").dropna()

country_list = ['Ireland', 'Germany (until 1990 former territory of the FRG)', 'Estonia', 'Czech Republic', 'Denmark',
                'Belgium', 'Bulgaria',
                'Latvia', 'Lithuania', 'Luxembourg', 'Hungary', 'Greece', 'Spain', 'France', 'Italy',
                'Cyprus',
                'Slovenia', 'Slovakia', 'Netherlands', 'Austria', 'Poland', 'Portugal', 'Romania',
                'Malta', 'Finland']

for country in country_list:
    print(country)

    print(df[df.GEO == country]["Value"].values)
