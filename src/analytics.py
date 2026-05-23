from collections import Counter



def most_common_topics(df, top_n=10):

    topics = []

    for topic_list in df["topics"]:

        if isinstance(topic_list, list):
            topics.extend(topic_list)

    return Counter(topics).most_common(top_n)



def average_meeting_duration(df):

    return df["duration"].mean()



def meetings_per_cluster(df):

    return df["cluster"].value_counts()