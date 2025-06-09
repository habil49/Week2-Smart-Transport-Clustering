import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os

# Load sample data (mimics transport stop coordinates + usage)
df = pd.read_csv("data.csv")

print("📊 Sample data:")
print(df.head())

# Clustering with K-Means
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
df['cluster'] = kmeans.fit_predict(df[['latitude', 'longitude']])

# Evaluation metrics
inertia = kmeans.inertia_
sil_score = silhouette_score(df[['latitude', 'longitude']], df['cluster'])
print(f"🧠 Inertia: {inertia:.2f}")
print(f"🧠 Silhouette Score: {sil_score:.2f}")

# Ensure output directory exists
os.makedirs('output', exist_ok=True)

# Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x='longitude', y='latitude', hue='cluster', data=df, palette='Set1')
plt.title('K-Means Clustering of Transport Stops')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('output/clusters_plot.png')
plt.show()
