from document_processor import load_knowledge_base, combine_documents

class KnowledgeBase:
    def __init__(self, primary_path: str, secondary_path: str):
        print("📚 Loading Knowledge Bases...")
        print("\n[Primary Knowledge Base]")
        self.primary_docs = load_knowledge_base(primary_path)
        print("\n[Secondary Knowledge Base]")
        self.secondary_docs = load_knowledge_base(secondary_path)
        print(f"\n✅ Ready! {len(self.primary_docs)} primary + {len(self.secondary_docs)} secondary docs loaded.")

    def get_primary_context(self) -> str:
        return combine_documents(self.primary_docs)

    def get_secondary_context(self) -> str:
        return combine_documents(self.secondary_docs)

    def get_full_context(self) -> str:
        return combine_documents(self.primary_docs + self.secondary_docs)
