import json
import pandas as pd
import re
from pathlib import Path


CSV_PATH= Path("chapternames1.csv")
JSON_PATH=Path("../chapters2.json")
TITLE_COL= 0

def slugify(title:str)-> str:
    slug=title.lower().strip()
    slug= re.sub(r"\s+", "-", slug)
    slug= re.sub(r"-+","-",slug)
    return slug

def main()->None:
    records =  []
    df = pd.read_csv("chapternames1.csv")
    for title in df.iloc[:, 0].astype(str):
        slug = slugify(title)
        records.append({
            "title": title,
            "slug":slug,
            "file":f"{slug}.jpg",
            "notes":""
        })

    JSON_PATH.write_text(json.dumps(records, indent=2, ensure_ascii=False))
    print(f"Wrote {len(records)}")

if __name__=="__main__":
    main()

