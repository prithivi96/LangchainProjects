from langchain_community.embeddings import OpenAIEmbeddings
from langchain.utils import cosine_similarity
import pandas as pd

embedding = OpenAIEmbeddings()

# df = pd.read_excel("Data.xlsx")
#
# df["embeddings"] = df["Words"].apply(lambda x: embedding.embed_query(text=x))
# df.to_csv("word_embeddings.csv")
df = pd.read_csv("word_embeddings.csv")
our_text = "Cat"
our_txt_embedding = embedding.embed_query(our_text)
print(our_txt_embedding)
df["similarity_score"] = df["embeddings"].apply(lambda x: cosine_similarity(x,our_txt_embedding))
print(df)