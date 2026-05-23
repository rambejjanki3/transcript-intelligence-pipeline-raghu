import matplotlib.pyplot as plt
import umap.umap_ as umap
import pandas as pd



def plot_sentiment_distribution(df):

    plt.figure(figsize=(8, 5))

    df["sentiment_score"].hist()

    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")

    plt.show()



def plot_cluster_distribution(df):

    plt.figure(figsize=(8, 5))

    df["cluster"].value_counts().plot(kind="bar")

    plt.title("Meetings per Cluster")
    plt.xlabel("Cluster")
    plt.ylabel("Count")

    plt.show()



def plot_umap(embeddings, clusters):

    reducer = umap.UMAP(random_state=42)

    projection = reducer.fit_transform(embeddings)

    plt.figure(figsize=(10, 8))

    plt.scatter(
        projection[:, 0],
        projection[:, 1],
        c=clusters
    )

    plt.title("Meeting Topic Clusters")

    plt.show()