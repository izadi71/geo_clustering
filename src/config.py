from hdbscan import HDBSCAN
from sklearn.cluster import AgglomerativeClustering, KMeans
from data import DATA_DIR
from reports import REPORT_DIR

# File paths
DATA_PATH = DATA_DIR / 'LatLong.csv'
FIGURES_PATH = REPORT_DIR / 'figures'
REPORT_PATH = REPORT_DIR / 'report.md'

RANDOM_STATE = 0

#clusters
cluster_models = {
    'KMeans': KMeans(
        n_clusters=8, 
        init='k-means++', 
        n_init=10, 
        max_iter=300, 
        random_state=0
        ),
    'AgglomerativeClustering_Ward': AgglomerativeClustering(
        n_clusters=8, 
        affinity='euclidean', 
        linkage='ward'
        ),
    'AgglomerativeClustering_Average': AgglomerativeClustering(
        n_clusters=8, 
        affinity='euclidean', 
        linkage='average'
        ),
}
