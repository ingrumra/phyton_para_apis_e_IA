
from flask import Flask, request, jsonify
import pandas as pd

from app.core.cleaning import clean_dataframe

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.post("/echo")
def echo():
    payload = request.get_json(force=True, silent=False)
    return jsonify(payload)

@app.post("/clean")
def clean():
    payload = request.get_json(force=True, silent=False)
    records = payload.get("records", [])
    df = pd.DataFrame(records)
    df_clean = clean_dataframe(df)

    return jsonify({
        "n": int(len(df_clean)),
        "records": df_clean.to_dict(orient="records")
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)