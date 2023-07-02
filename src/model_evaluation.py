from loguru import logger
from rich.progress import track
from sklearn.metrics import (calinski_harabasz_score, davies_bouldin_score,
                             silhouette_score)
import pandas as pd

class ClusterEvaluator:
    def __init__(self, data, cluster_trainer):
        self.data = data
        self.cluster_trainer = cluster_trainer

    def evaluate_clusters(self):
        scores = {}
        for name, model in track(self.cluster_trainer.models.items(), description="Evaluating..."):
            logger.info(f"Evaluating {name}...")
            labels = model.labels_
            silhouette = silhouette_score(self.data, labels)
            calinski_harabasz = calinski_harabasz_score(self.data, labels)
            davies_bouldin = davies_bouldin_score(self.data, labels)
            scores[name] = {
                'Silhouette': silhouette,
                'Calinski-Harabasz': calinski_harabasz,
                'Davies-Bouldin': davies_bouldin
            }
            logger.info(f"Scores for {name}: {scores[name]}")
        scores_df = pd.DataFrame(scores).T
        return scores, scores_df
