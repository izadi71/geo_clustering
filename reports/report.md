# Clustering Report

## Scores

### KMeans

- Silhouette: 0.5480409591312594
- Calinski-Harabasz: 12366.437407608277
- Davies-Bouldin: 0.7560107616412011

### AgglomerativeClustering_Ward

- Silhouette: 0.408255580204174
- Calinski-Harabasz: 10769.320427165258
- Davies-Bouldin: 0.9372969657937595

### AgglomerativeClustering_Average

- Silhouette: 0.5384075307113992
- Calinski-Harabasz: 8167.24126839105
- Davies-Bouldin: 0.6199587193568465

## Plots

### Elbow Plot

The elbow plot shows the distortion (sum of squared distances to the nearest cluster center) for different values of the number of clusters for the KMeans algorithm. The optimal number of clusters is usually at the 'elbow' of the plot, where the distortion starts to decrease more slowly.

![Elbow Plot](reports/figures/png/elbow.png)

### Dendrogram Plot

The dendrogram plot shows the hierarchical clustering of the data using the AgglomerativeClustering algorithm with Ward linkage. The x-axis shows the data points and the y-axis shows the distance between clusters. The horizontal lines represent the merging of two clusters. The optimal number of clusters can be determined by cutting the dendrogram at a specific height.

![Dendrogram Plot](reports/figures/png/dendrogram.png)

### KMeans

#### Cluster Plot

The cluster plot shows the geographical distribution of the clusters for the KMeans algorithm. Each color represents a different cluster.

![KMeans Cluster Plot](reports/figures/png/KMeans.png)

#### Cluster Counts Plot

The cluster counts plot shows the number of data points in each cluster for the KMeans algorithm.

![KMeans Cluster Counts Plot](reports/figures/png/KMeans_counts.png)

#### Cluster Pie Chart

The cluster pie chart shows the proportion of data points in each cluster for the KMeans algorithm.

![KMeans Cluster Pie Chart](reports/figures/png/KMeans_pie.png)

### AgglomerativeClustering_Ward

#### Cluster Plot

The cluster plot shows the geographical distribution of the clusters for the AgglomerativeClustering_Ward algorithm. Each color represents a different cluster.

![AgglomerativeClustering_Ward Cluster Plot](reports/figures/png/AgglomerativeClustering_Ward.png)

#### Cluster Counts Plot

The cluster counts plot shows the number of data points in each cluster for the AgglomerativeClustering_Ward algorithm.

![AgglomerativeClustering_Ward Cluster Counts Plot](reports/figures/png/AgglomerativeClustering_Ward_counts.png)

#### Cluster Pie Chart

The cluster pie chart shows the proportion of data points in each cluster for the AgglomerativeClustering_Ward algorithm.

![AgglomerativeClustering_Ward Cluster Pie Chart](reports/figures/png/AgglomerativeClustering_Ward_pie.png)

### AgglomerativeClustering_Average

#### Cluster Plot

The cluster plot shows the geographical distribution of the clusters for the AgglomerativeClustering_Average algorithm. Each color represents a different cluster.

![AgglomerativeClustering_Average Cluster Plot](reports/figures/png/AgglomerativeClustering_Average.png)

#### Cluster Counts Plot

The cluster counts plot shows the number of data points in each cluster for the AgglomerativeClustering_Average algorithm.

![AgglomerativeClustering_Average Cluster Counts Plot](reports/figures/png/AgglomerativeClustering_Average_counts.png)

#### Cluster Pie Chart

The cluster pie chart shows the proportion of data points in each cluster for the AgglomerativeClustering_Average algorithm.

![AgglomerativeClustering_Average Cluster Pie Chart](reports/figures/png/AgglomerativeClustering_Average_pie.png)

