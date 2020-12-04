import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.cluster import KMeans

insurance_data = pd.read_csv("C:/Users/USER/Desktop/k_means_clust/Insurance Dataset.csv")

def norm_func(i):
    x = (i-i.min())	/	(i.max()	-	i.min())
    return (x)

norm_df=norm_func(insurance_data ) 

####elbow plot
twss=[]
k=list(range(2,8))

for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(norm_df)
    twss.append(kmeans.inertia_)
twss

plt.plot(k,twss,'ro-');plt.xlabel("no of cluster");plt.ylabel("twss")
#######in elbow plot there is bend at k=4,hence 4 clusters could give proper result
model=KMeans(n_clusters=4)
pred=model.fit_predict(norm_df)
pred

insurance_data['cluster']=pred
insurance_data=insurance_data.iloc[:,[5,0,1,2,3,4]]
