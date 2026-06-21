from flask import Flask, render_template, request
import os

app = Flask(__name__)

CORPUS_DIR = "corpus"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():

    query = request.args.get("query", "").strip().lower()

    results = []

    if query:

        for filename in os.listdir(CORPUS_DIR):

            if filename.endswith(".txt"):

                path = os.path.join(CORPUS_DIR, filename)

                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()

                words = text.split()

                for i, word in enumerate(words):

                    if query in word.lower():

                        left = " ".join(words[max(0, i-5):i])
                        right = " ".join(words[i+1:i+6])

                        results.append({
                            "file": filename,
                            "left": left,
                            "keyword": word,
                            "right": right
                        })

    return render_template(
        "results.html",
        query=query,
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)
