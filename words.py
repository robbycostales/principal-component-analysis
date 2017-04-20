import pandas as pd
import python_pca as pca
import numpy as np
# df = pd.read_csv("./assoc_press/assoc_pressMat.csv")
# df.as_matrix()

df=pd.read_csv("./assoc_press/assoc_pressMat.csv", sep=',',header=None)
#print(df)

y_pre = df.values

y = [j[1:] for j in y_pre[1:]] # data

for i in range(len(y)):
    for j in range(len(y[i])):
        y[i][j] = int(y[i][j])

data = []
for i in range(len(y)):
    row = []
    for j in range(len(y[i])):
        row.append(y[i][j])
    data.append(row)

labels = y_pre[0][1:]

pca.pca(data, 1, True)
