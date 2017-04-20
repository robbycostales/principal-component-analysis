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
print("data", len(data), len(data[0]))


data = pca.pca(data, 4, False)[2]


for i in range(len(data)):
    print(i)
    points = []
    for j in range(len(data[i])):
        if data[i][j] > 1:
            points.append((data[i][j], y_pre[0][j]))
    points.sort()
    for k in points[-20:]:
        print(k)

# Article 1:
# About drugs (smuggled, office, pistol, men)

# Article 2:
# About Bush's relationship with colombia?
# "PAYMENTS", "INVESTORS", "DIVORCE?????"

# Article 3:
# We see "bush" again

# These articles must have been from a time when Bush was in office
