import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import math

# car accidents data in barcelona
car_data = pd.read_csv('car_barcelona.csv', encoding='unicode_escape')

car_data['Date'] = '2013-' + car_data['Mes de any'].apply(lambda x: str(x)) + '-' + car_data['Dia de mes'].apply(
    lambda x: str(x))

car_data['Date'] = pd.to_datetime(car_data['Date'])

print(car_data['Date'].head(10))

accidents = car_data.groupby(['Date']).size()
print("Mean:", accidents.mean(), "std:", accidents.std())
fig, ax = plt.subplots(1, 1, figsize=(15, 5))
acc = np.array(accidents)
plt.plot(range(0, 365), acc, 'b-o', lw=1.2, alpha=0.9)
plt.plot(range(0, 365), [acc.mean()] * 365, 'r-', lw=1.2, alpha=0.9)
plt.xlabel('day')
plt.ylabel('num of acc')

plt.show()
