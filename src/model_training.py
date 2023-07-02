from loguru import logger
from rich.progress import track
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from src.config import cluster_models

class ClusterTrainer:
    def __init__(self, data):
        self.data = data
        self.models = {}
    def train_clusters(self):
        for name, model in track(cluster_models.items(), description='Trainting...'):
                logger.info(f"Training {name}...")
                pipeline = Pipeline([
                    ('scaler', StandardScaler()),
                    ('cluster', model)
                ])
                pipeline.fit(self.data)
                self.models[name] = pipeline.named_steps['cluster']
                logger.info(f"{name} trained successfully!")
