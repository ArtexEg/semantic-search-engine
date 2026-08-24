import os
import pickle
import faiss

from sentence_transformers import SentenceTransformer
from transformers.utils.logging import disable_progress_bar

disable_progress_bar()

# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    local_files_only=True
)

current_dir = os.path.dirname(
    os.path.abspath(__file__)
)

# Load FAISS index
index = faiss.read_index(
    os.path.join(
        current_dir,
        "faiss",
        "index.faiss"
    )
)

# Load chunks
with open(
    os.path.join(
        current_dir,
        "embeddings",
        "chunks.pkl"
    ),
    "rb"
) as f:
    all_chunks = pickle.load(f)


def search():

    while True:

        query = input("Question: ")

        if query.lower() in ("exit", "quit"):
            break

        # Create embedding for query
        query_embedding = model.encode(
            query,
            convert_to_numpy=True
        ).reshape(1, -1)

        # Normalize query vector
        faiss.normalize_L2(query_embedding)

        # Search top-k results
        scores, indices = index.search(
            query_embedding,
            k=10
        )

        # Print results
        for rank, (score, idx) in enumerate(
            zip(scores[0], indices[0]),
            start=1
        ):

            if idx == -1:
                continue

            print("=" * 70)
            print(f"Similarity: {score:.4f}")
            print("-" * 70)
            print(all_chunks[idx]["text"])
            print()


search()