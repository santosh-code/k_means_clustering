import numpy as np
import pandas as pd
import matplotlib.pylab as plt 
from sklearn.cluster import KMeans
crime_data = pd.read_csv("C:/Users/USER/Desktop/k_means_clust/crime_data.csv")

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/	(i.max()	-	i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(crime_data.iloc[:,1:])

twiss=[]
k=list(range(2,8))

for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    twiss.append(kmeans.inertia_)
    
twiss

plt.plot(k,twiss,'ro-');plt.xlabel("no of cluster");plt.ylabel("twss")

model=KMeans(n_clusters=4)
y_pred=model.fit_predict(df_norm)    
y_pred

crime_data['cluster']=y_pred

