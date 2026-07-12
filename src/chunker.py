import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class Chunker:

    def __init__(self, embedder):

        self.embedder = embedder
        self.docs = []
        self.doc_embs = None



    def chunk_text(self, text, max_len=500):

        if text is None:
            return []


        if not isinstance(text, str):
            text = str(text)



        sentences = (
            text
            .replace("\n", " ")
            .split(".")
        )


        chunks = []
        buffer = ""


        for sentence in sentences:

            sentence = sentence.strip()


            if not sentence:
                continue


            sentence += "."


            if len(buffer) + len(sentence) <= max_len:

                buffer += " " + sentence


            else:

                if buffer.strip():
                    chunks.append(
                        buffer.strip()
                    )


                buffer = sentence



        if buffer.strip():

            chunks.append(
                buffer.strip()
            )


        return chunks



    def index(self, text, max_len=500):

        self.docs = self.chunk_text(
            text,
            max_len
        )


        if not self.docs:

            self.doc_embs = None
            return



        self.doc_embs = self.embedder.encode(
            self.docs,
            normalize_embeddings=True
        )



    def retrieve(self, prompt, k=5):

        if not self.docs or self.doc_embs is None:

            return []



        query = self.embedder.encode(
            [prompt],
            normalize_embeddings=True
        )


        scores = cosine_similarity(
            query,
            self.doc_embs
        )[0]



        indexes = np.argsort(scores)[::-1][:k]



        return [

            {
                "text": self.docs[i],
                "score": float(scores[i])
            }

            for i in indexes

        ]