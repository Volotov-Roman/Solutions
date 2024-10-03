import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('iris_data.csv')
sp=list(df["Species"])
k=0
l=0
m=0
for i in sp:
    if i=="Iris-setosa":
        k+=1
    elif i=="Iris-versicolor":
        l+=1
    elif i=="Iris-virginica":
        m+=1
plt.pie([k,l,m], labels=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
plt.title('Виды ирисов')
plt.show()