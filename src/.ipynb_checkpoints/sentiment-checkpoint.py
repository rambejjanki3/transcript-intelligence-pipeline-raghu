import pandas as pd



def sentiment_summary(df):

    summary = {
        "average_sentiment": df["sentiment_score"].mean(),
        "max_sentiment": df["sentiment_score"].max(),
        "min_sentiment": df["sentiment_score"].min()
    }

    return summary



def sentiment_by_cluster(df):

    cluster_sentiment = (
        df.groupby("cluster")["sentiment_score"]
        .mean()
        .reset_index()
    )

    return cluster_sentiment