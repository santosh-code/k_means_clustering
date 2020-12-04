import numpy as np
import pandas as pd
import matplotlib.pylab as plt 
from sklearn.cluster import KMeans
airlines = pd.read_csv("C:/Users/USER/Desktop/k_means_clust/EastWestAirlines.csv")
airlines=airlines.iloc[:,1:]

def norm_func(i):
    x = (i-i.min())	/	(i.max()	-	i.min())
    return (x)
df_norm=norm_func(airlines)


twss=[]
k=list(range(2,8))

for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    twss.append(kmeans.inertia_)
    twss

plt.plot(k,twss,'ro-');plt.xlabel("no of cluster");plt.ylabel("twss")

########in elbow curve k=5 shows optimial clusters
model=KMeans(n_clusters=5)
pred=model.fit_predict(df_norm)

airlines['cluster']=pred

