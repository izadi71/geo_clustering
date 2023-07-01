from loguru import logger
from rich.progress import track

from src.config import REPORT_PATH


class ReportGenerator:
    def __init__(self, cluster_evaluator, cluster_visualizer):
        self.cluster_evaluator = cluster_evaluator
        self.cluster_visualizer = cluster_visualizer

    def generate_report(self):
        logger.info("Generating report...")
        scores, _ = self.cluster_evaluator.evaluate_clusters()
        with open(REPORT_PATH, 'w') as f:
            f.write("# Clustering Report\n\n")
            f.write("## Scores\n\n")
            for name, score in track(scores.items(), description="Writing..."):
                f.write(f"### {name}\n\n")
                for metric, value in score.items():
                    f.write(f"- {metric}: {value}\n")
                f.write("\n")
            f.write("## Plots\n\n")
            f.write("### Elbow Plot\n\n")
            f.write("The elbow plot shows the distortion (sum of squared distances to the nearest cluster center) for different values of the number of clusters for the KMeans algorithm. The optimal number of clusters is usually at the 'elbow' of the plot, where the distortion starts to decrease more slowly.\n\n")
            f.write(f"![Elbow Plot]({'reports/figures/png/elbow.png'})\n\n")
            f.write("### Dendrogram Plot\n\n")
            f.write("The dendrogram plot shows the hierarchical clustering of the data using the AgglomerativeClustering algorithm with Ward linkage. The x-axis shows the data points and the y-axis shows the distance between clusters. The horizontal lines represent the merging of two clusters. The optimal number of clusters can be determined by cutting the dendrogram at a specific height.\n\n")
            f.write(f"![Dendrogram Plot]({'reports/figures/png/dendrogram.png'})\n\n")
            for name in scores.keys():
                f.write(f"### {name}\n\n")
                f.write(f"#### Cluster Plot\n\n")
                f.write(f"The cluster plot shows the geographical distribution of the clusters for the {name} algorithm. Each color represents a different cluster.\n\n")
                f.write(f"![{name} Cluster Plot]({f'reports/figures/png/{name}.png'})\n\n")
                f.write(f"#### Cluster Counts Plot\n\n")
                f.write(f"The cluster counts plot shows the number of data points in each cluster for the {name} algorithm.\n\n")
                f.write(f"![{name} Cluster Counts Plot]({f'reports/figures/png/{name}_counts.png'})\n\n")
                f.write(f"#### Cluster Pie Chart\n\n")
                f.write(f"The cluster pie chart shows the proportion of data points in each cluster for the {name} algorithm.\n\n")
                f.write(f"![{name} Cluster Pie Chart]({f'reports/figures/png/{name}_pie.png'})\n\n")
        logger.info(f"Report generated at {REPORT_PATH}")
