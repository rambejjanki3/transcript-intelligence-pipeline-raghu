import re



def clean_text(text):
    """
    Basic text cleaning.
    """

    if not isinstance(text, str):
        return ""

    text = text.lower()

    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()



def preprocess_dataframe(df):

    df["clean_summary"] = df["summary"].apply(clean_text)

    return df