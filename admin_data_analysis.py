import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download NLTK data if not already downloaded (Punkt tokenizer, stopwords and WordNet datasets)
resources = ["tokenizers/punkt", "corpora/stopwords", "corpora/wordnet"] # Define a list of resources to check and download if necessary

for resource in resources:  # Iterate through the resources and check/download them
    if not nltk.data.find(resource):
        nltk.download(resource)

# Read the CSV file from GitHub
url = "https://raw.githubusercontent.com/Oscar-Onam/your-repo-name/main/CSI%20Report%20for%20COs.csv"
df = pd.read_csv(url)

# Keep required columns only
df = df[["COUNTRY", "REGION", "CSI", "TARGET_RESPONSE", "ACTUAL_RESPONSE", "RSP_DP_REMARK"]]

# Data Cleaning
def clean_text(text):
    # Remove special characters and digits
    text = text.str.replace(r'[^a-zA-Z\s]', '').str.replace(r'\d', '')
    return text

# Tokenization
df["CSI"] = df["CSI"].apply(word_tokenize)
df["TARGET_RESPONSE"] = df["TARGET_RESPONSE"].apply(word_tokenize)
df["ACTUAL_RESPONSE"] = df["ACTUAL_RESPONSE"].apply(word_tokenize)
df["RSP_DP_REMARK"] = df["RSP_DP_REMARK"].apply(word_tokenize)

# Removing stopwords
stop_words = set(stopwords.words("english"))
df["CSI"] = df["CSI"].apply(lambda x: [word for word in x if word.lower() not in stop_words])
df["TARGET_RESPONSE"] = df["TARGET_RESPONSE"].apply(lambda x: [word for word in x if word.lower() not in stop_words])
df["ACTUAL_RESPONSE"] = df["ACTUAL_RESPONSE"].apply(lambda x: [word for word in x if word.lower() not in stop_words])
df["RSP_DP_REMARK"] = df["RSP_DP_REMARK"].apply(lambda x: [word for word in x if word.lower() not in stop_words])

# Stemming
stemmer = PorterStemmer()
df["CSI"] = df["CSI"].apply(lambda x: [stemmer.stem(word) for word in x])
df["TARGET_RESPONSE"] = df["TARGET_RESPONSE"].apply(lambda x: [stemmer.stem(word) for word in x])
df["ACTUAL_RESPONSE"] = df["ACTUAL_RESPONSE"].apply(lambda x: [stemmer.stem(word) for word in x])
df["RSP_DP_REMARK"] = df["RSP_DP_REMARK"].apply(lambda x: [stemmer.stem(word) for word in x])

# Lemmatization
lemmatizer = WordNetLemmatizer()
df["CSI"] = df["CSI"].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])
df["TARGET_RESPONSE"] = df["TARGET_RESPONSE"].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])
df["ACTUAL_RESPONSE"] = df["ACTUAL_RESPONSE"].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])
df["RSP_DP_REMARK"] = df["RSP_DP_REMARK"].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

# Print the cleaned and preprocessed DataFrame
print(df)
