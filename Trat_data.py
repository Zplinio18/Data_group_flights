import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('flights.csv')

print("=================AGRUPAMENTO DE DADOS=================")

print()
print("!AGRUPAMENTO POR ORIGEM E DESTINO (Passageiros)!")
grouped = df.groupby(['Origin', 'Destination'])
aggregated = grouped.agg({'Passengers': 'sum'})
sorted_values = aggregated.sort_values(by='Passengers', ascending=False)

print(sorted_values.head())
print()
print("!AGRUPAMENTO VOOS POR MES!")
df['Month'] = pd.to_datetime(df['Fly Date'], format='%Y%m').dt.to_period('M')
grouped = df.groupby('Month')
aggregated = grouped.agg({'Flights': 'sum'})
sorted_values = aggregated.sort_values(by='Month')

print(sorted_values.head())
print()

# 10 AEROPORTOS MAIS MOVIMENTADOS

print("=================10 AEROPORTOS MAIS MOVIMENTADOS=================")
print("window1()")
airport_traffic = df.groupby('Origin').agg({'Flights': 'sum'})
busiest_airports = airport_traffic.nlargest(10, 'Flights')

busiest_airports.plot(kind='bar', color='grey')
plt.title('10 aeroportos mais movimentados')
plt.xlabel('Aeroporto')
plt.ylabel('Voos')
plt.xticks(rotation=45) # Rotaciona os nomes dos aeroporto
plt.tight_layout() # Ajusta o layout
plt.show()


print("=================ROTAS MAIS MOVIMENTADAS=================")
print("window2()")
route_traffic = df.groupby(['Origin', 'Destination']).agg({'Passengers': 'sum'})
busiest_routes = route_traffic.nlargest(10, 'Passengers')

busiest_routes.plot(kind='bar', color='grey')
plt.title('10 rotas mais movimentadas')
plt.xlabel('Rota')
plt.ylabel('Passageiros')
plt.xticks(rotation=45) # Rotaciona os nomes dos aeroporto
plt.tight_layout() # Ajusta o layout
plt.show()
