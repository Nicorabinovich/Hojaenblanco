import pandas as pd
import numpy as np

article_read = pd.read_csv('residencias-otorgadas-1T-2019.csv', delimiter=',', names = ['Provincia','Transitoria','Temporaria','Permanente','Total'])

article_read.head()

# Get the series
Provincia = article_read['Provincia']
#print (Provincia)
CantidadProvincias = len(Provincia) - 1
print(CantidadProvincias)


Transitoria = article_read["Transitoria"] #me tira todas las residencias transitorias incluyendo el titulo
Temporaria = article_read["Temporaria"]
Permanente = article_read["Permanente"]

print(Transitoria)
print(Temporaria)
print(Permanente)


quit()


# Filtering
#Cordoba = article_read[article_read == "CORDOBA"]

print(article_read)

CantidadTransitorias = sum(Transitoria)
print(CantidadTransitorias)

#print(Cordoba)
# you get the point....


import numpy as np
import matplotlib.pyplot as plt
N = CantidadProvincias
TransitoriaMeans = (Transitoria)
TemporariaMeans = (Temporaria)
PermanenteMeans= (Permanente)
ind = np.arange(N) #the x locations for the groups
width = 0.35 #ancho de las barras

p1 = plt.bar(ind,TransitoriaMeans,width,yerr=None)
p2 = plt.bar(ind,TemporariaMeans,width,yerr=None)
p3 = plt.bar(ind,PermanenteMeans,width,yerr=None)

