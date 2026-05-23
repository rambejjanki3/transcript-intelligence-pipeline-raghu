from sentence_transformers import SentenceTransformer
import hdbscan
import pandas as pd


class TopicModeler:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.clusterer = hdbscan.HDBSCAN(
            min_cluster_size=5,
            metric='euclidean'
        )

    def generate_embeddings(self, texts):

        embeddings = self.model.encode(texts)

        return embeddings

    def cluster_texts(self, embeddings):

        clusters = self.clusterer.fit_predict(embeddings)

        return clusters


if __name__ == "__main__":

    sample_texts = [
        "Engineering review for architecture",
        "Customer escalation about billing",
        "Roadmap planning discussion"
    ]

    tm = TopicModeler()

    embeddings = tm.generate_embeddings(sample_texts)

    clusters = tm.cluster_texts(embeddings)

    print(clusters)