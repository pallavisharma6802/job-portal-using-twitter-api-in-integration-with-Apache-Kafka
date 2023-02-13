
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


data1=pd.read_csv('data.csv')
data=data1[['likes','retweet']]
data.head()


sc=StandardScaler()
data=sc.fit_transform(data)
print(len(data))


inertias = []

for i in range(1,15):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)


plt.plot(range(1,15), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=2,random_state=0)
kmeans.fit(data)
clusters = kmeans.labels_.tolist()
print(clusters)




indexes=[]
for i in range(len(clusters)):
    if clusters[i]==0:
        indexes.append(i)
print(indexes)



final_df=data1.iloc[indexes]
final_df.to_csv("filtered_data.csv")
count=0


with open('/Users/pallavisharma/Desktop/job_portal/filtered_twitter_data.txt', 'w') as f:
    dfAsString = final_df.to_string(header=False, index=False)
    f.write(f'\n{dfAsString}')




