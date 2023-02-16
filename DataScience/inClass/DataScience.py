import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

river_lengths = pd.Series(data=[6300, 6650, 6275, 6400],
                          index=['Yangtze', 'Nile', 'Mississippi', 'Amazon'],
                          name='Length /km',
                          dtype=float)

edu = pd.read_csv('/DataScience/education_Data.csv',
                  na_values=":",
                  usecols=["TIME", "GEO", "Value"])


