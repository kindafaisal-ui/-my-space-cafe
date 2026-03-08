import os
import markdown

def load_markdown_file(filepath: str) -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        raw_text = f.read()
    html_content = markdown.markdown(raw_text)
    return {
        "filename": os.path.basename(filepath),
        "filepath": filepath,
        "raw_text": raw_text,
        "html": html_content,
    }

def load_knowledge_base(folder_path: str) -> list:
    documents = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                doc = load_markdown_file(filepath)
                documents.append(doc)
                print(f"  ✅ Loaded: {filepath}")
    return documents

def combine_documents(documents: list) -> str:
    combined = ""
    for doc in documents:
        combined += f"\n\n--- {doc['filename']} ---\n"
        combined += doc["raw_text"]
    return combined
