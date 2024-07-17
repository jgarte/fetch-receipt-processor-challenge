from uuid import UUID

from fastapi import FastAPI, HTTPException

from .models import Receipt
from .receipt_rules import (
    calculate_points,
    generate_receipt_id,
    is_between_two_and_four,
    is_round_dollar_amount,
    is_multiple_of_quarter,
    trimmed_length_is_multiple_of_three,
    purchase_date_is_odd,
)


app = FastAPI()
receipts: dict[str, Receipt] = {}


@app.get("/receipts/debug")
async def debug_receipts():
    return {"receipts": receipts}


@app.post("/receipts/process")
async def process_receipts(receipt: Receipt):
    receipt_id = generate_receipt_id()
    receipts[receipt_id] = receipt
    return {"id": receipt_id}


@app.get("/receipts/{receipt_id}/points")
async def get_points(receipt_id: str):
    receipt = receipts[receipt_id]
    points = calculate_points(receipt)
    return {"points": points}
    # raise HTTPException(status_code=403, detail="Receipt not found")
