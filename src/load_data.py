import os
import json
import pandas as pd


def load_meetings(data_dir):
    """
    Load all meeting folders into a single dataframe.
    """

    rows = []

    folders = os.listdir(data_dir)

    for folder in folders:

        folder_path = os.path.join(data_dir, folder)

        try:
            with open(os.path.join(folder_path, "summary.json")) as f:
                summary = json.load(f)

            with open(os.path.join(folder_path, "meeting-info.json")) as f:
                info = json.load(f)

            rows.append({
                "meeting_id": info.get("meetingId"),
                "title": info.get("title"),
                "summary": summary.get("summary"),
                "topics": summary.get("topics"),
                "sentiment_score": summary.get("sentimentScore"),
                "overall_sentiment": summary.get("overallSentiment"),
                "duration": info.get("duration"),
                "start_time": info.get("startTime"),
                "end_time": info.get("endTime")
            })

        except Exception as e:
            print(f"ERROR processing {folder}: {e}")

    return pd.DataFrame(rows)


if __name__ == "__main__":

    df = load_meetings("../data/raw")

    print(df.head())
    print(df.shape)