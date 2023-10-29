from fastapi import FastAPI, Request, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session
from contextlib import asynccontextmanager

import os
import numpy as np
import pandas as pd
import chardet
import shutil
from pathlib import Path
import argparse
import asyncio

import db_config
from models import *
from inserts import (
    insert_toast_order_details,
    insert_toast_modifier_details,
    insert_cash_entries,
    insert_house_account_export,
    insert_toast_check_details,
    insert_toast_item_details,
    insert_toast_payment_details,
    insert_toast_time_entries,
)


def process_data(src: str, dst: str, session: Session):
    functions = {
        "OrderDetails": insert_toast_order_details,
        "ModifiersSelectionDetails": insert_toast_modifier_details,
        "CashEntries": insert_cash_entries,
        "HouseAccountExport": insert_house_account_export,
        "CheckDetails": insert_toast_check_details,
        "ItemSelectionDetails": insert_toast_item_details,
        "PaymentDetails": insert_toast_payment_details,
        "TimeEntries": insert_toast_time_entries,
    }

    if not os.path.exists(dst):
        os.makedirs(dst)

    src = Path(src)
    dst = Path(dst)

    for folder in os.listdir(src):
        if not os.path.exists(dst / folder):
            os.mkdir(dst / folder)
        for file in os.listdir(src / folder):
            name = file.split(".")[0]
            ext = file.split(".")[1]
            if ext == "csv":
                with open(src / folder / file, "rb") as f:
                    enc = chardet.detect(f.read())
                    df = pd.read_csv(
                        src / folder / file, dtype=str, encoding=enc["encoding"]
                    )
                    df.replace(np.nan, None, inplace=True)
                    functions[name](df, session)
            else:
                pass
            shutil.move(src=src / folder / file, dst=dst / folder)
        session.commit()
        shutil.rmtree(src / folder)


class Dirs(SQLModel):
    src: str = "from"
    dst: str = "processed"


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_config.init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/process")
async def process_csv(
    request: Request, dirs: Dirs, session: Session = Depends(db_config.get_session)
):
    try:
        process_data(src=dirs.src, dst=dirs.dst, session=session)
        return JSONResponse(
            content={"success": True, "message": "Data is inserted into the database"},
            status_code=status.HTTP_201_CREATED,
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to insert the data",
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--src", type=str, default="from")
    parser.add_argument("--dst", type=str, default="processed")

    args, _ = parser.parse_known_args()

    loop = asyncio.get_event_loop()
    coroutine = db_config.init_db()
    loop.run_until_complete(coroutine)

    with Session(db_config.engine, future=True) as session:
        try:
            process_data(src=args.src, dst=args.dst, session=session)
            print("Data is inserted into the datasrc")
        except:
            print("Failed to insert the data")
