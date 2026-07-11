from html_extract import extract_from_url
from chunker import Chunker
from optimization import rm_stopwords


from sentence_transformers import SentenceTransformer
from ddgs import DDGS

embedder = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


chunker = Chunker(embedder)



def retrieval(url, prompt):

    print("\nURL:", url)


    text = extract_from_url(url)


    print(
        "TEXT TYPE:",
        type(text)
    )


    if not text:

        print(
            "FAILED EXTRACTION:",
            url
        )

        return ""



    print(
        "TEXT PREVIEW:",
        text[:200]
    )



    chunker.index(
        text,
        max_len=500
    )




    results = chunker.retrieve(
        prompt,
        k=5
    )



    retrieved_text = "\n\n".join(
        result["text"]
        for result in results
    )



    for result in results:

        print(
            "\n--- CHUNK ---"
        )

        print(
            result["score"]
        )

        print(
            result["text"]
        )



    return retrieved_text





def search_url(prompt):

    final_text = ""


    with DDGS() as ddgs:

        results = ddgs.text(
            prompt,
            max_results=10
        )


        for r in results:

            url = r["href"]


            retrieved = retrieval(
                url
                , prompt
            )


            if retrieved:

                final_text += (
                    "\n\n"
                    "================= NEW SOURCE ================="
                    "\n\n"
                    + retrieved
                )

    final_text = rm_stopwords(final_text)

    return final_text
