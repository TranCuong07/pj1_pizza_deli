from fastapi import APIRouter,status,Depends,HTTPException
from fastapi.responses import RedirectResponse
from database import get_db
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import session
from datetime import datetime, timedelta
from schemas import WebhookData

webhook_routes = APIRouter()

async def insert_transaction(data: WebhookData,db: session = Depends(get_db)):
    amount_in = 0
    amount_out = 0

    if data.tranferType == "in":
        amount_in = data.transferAmount
    elif data.tranferType == "out":
        amount_out = data.transferAmount
    
    transaction = Transaction(
        gateway = data.gateway,
        transaction_date = data.transaction_date,
        accountNumber = data.accountNumber,
        account_number = data.account_number,
        sub_account = data.sub_account,
        amount_in = data.amount_in,
        amount_out = data.amount_out,
        accumulated = data.accumulated,
        code = data.code,
        transaction_content = data.transaction_content,
        reference_number = data.reference_number,
        body = data.body,
        created_at= data.created_at
    )

    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)

@webhook_routes.post('/webhook',status_code=status.HTTP_201_CREATED)
async def handle_webhook(data: WebhookData,db: session = Depends(get_db)):
    try:
        await insert_transaction(db,data)
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=400, detail= f"Webhook handlling error: {str(e)}")

