from sentence_transformers import SentenceTransformer   

# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(chunks: list[str]):
    # Generate the embedding for the text chunks

    embedding = model.encode(chunks)
    return np.array(embedding, dtype="float32") 