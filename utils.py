import os
import numpy as np

# Create function for loading documents
def load_documents(dataset_paths):

    texts = []

    for folder in dataset_paths:

        for filename in os.listdir(folder):

            file_path = os.path.join(folder, filename)

            if not os.path.isfile(file_path):
                continue


            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()


            current_title = None
            current_body = []

            i = 0

            while i < len(lines):

                line = lines[i].strip()


                if (
                    line != ""
                    and i + 2 < len(lines)
                    and lines[i + 1].strip() == ""
                    and lines[i + 2].strip() != ""
                ):

                    if current_title is not None:

                        texts.append({
                            "title": current_title,
                            "text": "\n".join(current_body).strip()
                        })


                    current_title = line
                    current_body = []

                    i += 1
                    continue


                else:

                    if current_title is not None:
                        current_body.append(line)


                i += 1


            if current_title is not None:
                texts.append({
                    "title": current_title,
                    "text": "\n".join(current_body).strip()
                })


    return texts

# Create function for splitting documents into chunks
def chunk_text(article, chunk_size=200, overlap=50):
    title = article["title"]  # Extract the title from the document structure
    words = article["text"].split() # Split the text into individual words
    
    chunks = []

    # Calculate step size for creating overlapping chunks
    step = chunk_size - overlap

    for i in range(0, len(words), step):
        # Extract chunk of words from current position up to chunk_size
        chunk = words[i:i+chunk_size]

        # Check that the chunk contains enough words
        if len(chunk) >= 50:
            chunks.append({"title": title, "text": " ".join(chunk)})  # Add structured chunk to the list
    
    return chunks


# Get the current directory of the dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
dataset_paths = [
    os.path.join(current_dir, "dataset", "1of2"),
    os.path.join(current_dir, "dataset", "2of2")
    ]

# Load documents
texts = load_documents(dataset_paths)

for article in texts:
    if "Grand Theft Auto IV" in article["text"]:
        print("TITLE:", article["title"])
        print(article["text"][:400])
        break