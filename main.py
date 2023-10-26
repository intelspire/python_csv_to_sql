from fastapi import FastAPI, Request

import os
import pandas as pd
import chardet
import shutil
from pathlib import Path

import db_config

if not os.path.exists("processed"):
    os.mkdir("processed")


def process_data():
    base = Path("from")
    to = Path("processed")
    for folder in os.listdir(base):
        if not os.path.exists(to / folder):
            os.mkdir(to / folder)
        for file in os.listdir(base / folder):
            name = file.split(".")[0]
            ext = file.split(".")[1]
            if ext == "csv":
                with open(base / folder / file, "rb") as f:
                    enc = chardet.detect(f.read())
                    df = pd.read_csv(
                        base / folder / file, dtype=str, encoding=enc["encoding"]
                    )

                    try:
                        df.to_sql(
                            name,
                            con=db_config.engine,
                            index=False,
                            if_exists="append",
                        )
                    except:
                        pass
            else:
                pass
            shutil.move(src=base / folder / file, dst=to / folder)
        shutil.rmtree(base / folder)


app = FastAPI()


@app.get("/process")
async def process_csv(request: Request):
    process_data()


if __name__ == "__main__":
    process_data()
