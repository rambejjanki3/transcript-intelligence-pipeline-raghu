# Transcript Intelligence Analysis Pipeline

## Project Overview

This project analyzes 100 meeting transcripts to identify recurring themes, sentiment trends, and operational insights.

The system transforms raw meeting transcript data into structured organizational intelligence using a hybrid NLP pipeline based on semantic embeddings, clustering, and sentiment analysis.

The goal of the project is to demonstrate how conversational data can be analyzed at scale to provide visibility into organizational behavior, meeting dynamics, and operational trends.

---

# Business Problem

Organizations generate large amounts of conversational data through internal meetings, customer calls, escalation reviews, and planning discussions.

However, this information is often:
- difficult to search
- fragmented across systems
- manually analyzed
- lacking organizational visibility

Leadership teams typically cannot easily answer questions such as:
- What topics are teams discussing most frequently?
- Which meeting types show negative sentiment trends?
- Are escalation discussions increasing?
- What operational risks appear repeatedly?

This project explores how NLP and clustering techniques can transform raw meeting transcripts into actionable insights.

---

# Installation

Clone the repository:

```bash
git clone <your-github-repo>
cd transcript-intelligence
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Recommended execution order:

1. 01_exploration.ipynb
2. 02_topic_clustering.ipynb
3. 03_sentiment_analysis.ipynb
4. 04_final_insights.ipynb

---

# Topic Clustering

Meeting summaries were converted into semantic embeddings using Sentence Transformers.

HDBSCAN clustering was then used to identify semantically related meeting groups.

Example discovered categories:
- Engineering Reviews
- Customer Escalations
- Product Planning
- Security & Compliance

---

# Sentiment Analysis

Sentiment scores were analyzed across meeting categories to identify behavioral and operational trends.

Example findings:
- Escalation-oriented meetings showed lower sentiment
- Product planning meetings were generally more positive
- Longer meetings trended toward neutral sentiment

---

# Visualization

The project includes:
- Topic distribution charts
- UMAP cluster visualizations
- Sentiment trend analysis
- Meeting duration analysis

UMAP was used to reduce embedding vectors from 384 dimensions into 2D visual space while preserving semantic similarity relationships.

---

# Additional Opportunities

Potential future enhancements include:
- Speaker dominance analysis
- Risk keyword detection
- Decision velocity tracking
- Organizational collaboration analysis
- Real-time transcript processing
- RAG-based semantic meeting search

---

# Limitations

Current limitations include:
- relatively small dataset size
- manual interpretation of clusters
- limited speaker-level analytics
- dependence on summary quality

---

# Technologies Used

- Python
- Pandas
- Sentence Transformers
- HDBSCAN
- Scikit-learn
- UMAP
- Matplotlib
- Jupyter Notebook
