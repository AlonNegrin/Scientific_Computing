import pandas as pd

car_data = pd.read_csv('car_barcelona.csv', encoding='unicode_escape')

car_data['Date'] = '2013-' + car_data['Mes de any'].apply(lambda x: str(x)) + '-' + car_data['Dia de mes'].apply(
    lambda x: str(x))

car_data['Date'] = pd.to_datetime(car_data['Date'])

values = df[df.GEO == country].values[:, 2]
