# Geospatial Clustering

This project performs geospatial clustering on a dataset of latitude and longitude coordinates to identify clusters of points.


## Installation

To use this project, you will need to have Python 3 and `conda` installed on your computer. You can download Python 3 from the [official website](https://www.python.org/downloads/) and `conda` from the [official website](https://docs.conda.io/en/latest/miniconda.html).

Once you have installed Python 3 and `conda`, you can create an environment for this project by running the following command in the root directory of the project:

```sh
conda create --name geo_cluster python=3.9
```

This will create a new conda environment named geo_cluster with Python 3.9 installed. You can activate this environment by running the following command:

```sh
conda activate geo_cluster
```
Once you have activated the cancer_clf environment, you can install the necessary libraries for this project by running the following command in the root directory of the project:

```sh
pip install -r requirements.txt
```
This will install the libraries listed in the requirements.txt file using conda. Once you have installed these libraries, you can use this project as described in the Usage section.


## Usage

To use this project, you will need to set the `PYTHONPATH` environment variable to the root directory of the project. You can do this by running the following command in the root directory of the project:

```sh
export PYTHONPATH=${PWD}
```

Once you have set the `PYTHONPATH` environment variable, you can run the main script of the project by running the following command in the `src` directory of the project:

```sh
python src/main.py
```

This will load and preprocess the data, train the clustering models, evaluate their performance, visualize the clusters, and generate a report.

The report will be saved as a Markdown file in the `reports` directory. You can view the report using a Markdown viewer or convert it to another format such as HTML or PDF using a Markdown converter.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.