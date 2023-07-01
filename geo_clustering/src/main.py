from src.data_preprocessing import DataPreprocessor
from src.model_training import ClusterTrainer
from src.model_evaluation import ClusterEvaluator
from src.visualization import ClusterVisualizer
from src.generate_report import ReportGenerator
from src.config import DATA_PATH


def main():
    # Load and preprocess data
    preprocessor = DataPreprocessor(DATA_PATH)
    data = preprocessor.cleaned_data

    # Train clustering models
    trainer = ClusterTrainer(data)
    trainer.train_clusters()

    # Evaluate clustering models
    evaluator = ClusterEvaluator(data, trainer)
    scores, scores_df = evaluator.evaluate_clusters()

    # Visualize clusters
    visualizer = ClusterVisualizer(data, trainer)
    visualizer.plot_elbow()
    visualizer.plot_dendrogram()
    visualizer.plot_clusters()
    visualizer.plot_cluster_counts()
    visualizer.plot_cluster_pie()

    # Generate report
    report_generator = ReportGenerator(evaluator, visualizer)
    report_generator.generate_report()


if __name__ == '__main__':
    main()
