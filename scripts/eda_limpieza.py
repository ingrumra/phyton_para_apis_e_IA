


import pandas as pd
from src.app.core.cleaning import load_raw_csv, clean_dataframe, profile_missing

RAW = "data/raw/cancer_mama_piii_2023_raw.csv"
OUT = "data/processed/cancer_mama_piii_2023_clean.csv"

def main():
    df_raw = load_raw_csv(RAW)
    print("RAW shape:", df_raw.shape)

    df_clean = clean_dataframe(df_raw)
    print("CLEAN shape:", df_clean.shape)

    miss = profile_missing(df_clean)
    print("Missing per column (top 10):")
    top10 = sorted(miss.items(), key=lambda x: x[1], reverse=True)[:10]
    for k, v in top10:
        print(f"  {k}: {v}")

    df_clean.to_csv(OUT, index=False)
    print("Saved:", OUT)

if __name__ == "__main__":
    main()
    