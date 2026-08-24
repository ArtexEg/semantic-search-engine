import faiss
import os
import numpy as np
import pickle

current_dir = os.path.dirname(os.path.abspath(__file__))

# Load embeddings
embeddings = np.load(
    os.path.join(
        current_dir,
        "..",
        "embeddings",
        "embeddings.npy"
    )
)

# Normalize embeddings for cosine similarity
faiss.normalize_L2(embeddings)

# Load chunks
with open(
    os.path.join(
        current_dir,
        "..",
        "embeddings",
        "chunks.pkl"
    ),
    "rb"
) as f:
    all_chunks = pickle.load(f)

print(f"Embeddings shape: {embeddings.shape}")
print(f"Chunks count: {len(all_chunks)}")

# Check normalization
norms = np.linalg.norm(embeddings, axis=1)

print("First 10 norms:")
print(norms[:10])

print(f"Min norm: {norms.min()}")
print(f"Max norm: {norms.max()}")

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

print(f"Total vectors in index: {index.ntotal}")

# Save index
index_path = os.path.join(
    current_dir,
    "index.faiss"
)

faiss.write_index(index, index_path)

if os.path.isfile(index_path):
    print("FAISS index saved successfully.")