import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
from loguru import logger
from rich.progress import track
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans


class ClusterVisualizer:
    def __init__(self, data, cluster_trainer):
        self.data = data
        self.cluster_trainer = cluster_trainer
        sns.set()

    def plot_elbow(self):
        logger.info("\n Plotting elbow method for KMeans...")
        distortions = []
        for i in track(range(3, 17), description="Plotting..."):
            kmeans = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300, random_state=0)
            kmeans.fit(self.data)
            distortions.append(kmeans.inertia_)
        fig = px.line(x=range(3, 17), y=distortions, labels={'x': 'Number of Clusters', 'y': 'Distortion'})
        fig.write_html('reports/figures/html/elbow.html')
        fig.write_image('reports/figures/png/elbow.png')


    def plot_dendrogram(self):
        logger.info("\n Plotting dendrogram for AgglomerativeClustering...")
        Z = linkage(self.data, method='ward')
        dendrogram(Z)
        plt.savefig('reports/figures/png/dendrogram.png')


    def plot_clusters(self):
        for name, model in track(self.cluster_trainer.models.items(), description="Plotting..."):
            logger.info(f"Plotting clusters for {name}...")
            labels = model.labels_
            fig = px.scatter_mapbox(self.data, lat='Lat', lon='Long', color=labels,
                                    color_discrete_sequence=px.colors.qualitative.Plotly,
                                    mapbox_style="carto-positron",
                                    zoom=3, center={"lat": 47.5260, "lon": 14.2551},
                                    width=900, height=700)
            fig.update_layout(legend_title_text='Cluster')
        
            fig.write_html(f'reports/figures/html/{name}.html')
            fig.write_image(f'reports/figures/png/{name}.png')

    def plot_cluster_counts(self):
        for name, model in track(self.cluster_trainer.models.items(), description="Plotting..."):
            logger.info(f"\n Plotting cluster counts for {name}...")
            labels = pd.Series(model.labels_, name='Cluster')
            counts = labels.value_counts()
            fig = px.bar(counts, labels={'index': 'Cluster', 'value': 'Count'})
            fig.write_html(f'reports/figures/html/{name}_counts.html')
            fig.write_image(f'reports/figures/png/{name}_counts.png')

    def plot_cluster_pie(self):
        for name, model in track(self.cluster_trainer.models.items(), description="Plotting..."):
            logger.info(f"\n Plotting cluster pie chart for {name}...")
            labels = pd.Series(model.labels_, name='Cluster')
            fig = px.pie(labels, values='Cluster', names='Cluster')
            fig.write_html(f'reports/figures/html/{name}_pie.html')
            fig.write_image(f'reports/figures/png/{name}_pie.png')
            
    
