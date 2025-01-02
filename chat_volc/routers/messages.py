from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session

from chat_volc.models.schemas import PrivateChat, Message
from chat_volc.settings import get_db

router = APIRouter(prefix="/private_chat/{private_chat_id}", tags=["messages"])


@router.post("/message")
async def create_message(
    request: Request,
    db: Session = Depends(get_db),
    private_chat_id: str = "",
):
    if request.method == "POST":
        chat_exists = db.query(
            db.query(PrivateChat).filter(PrivateChat.id == private_chat_id).exists()
        ).scalar()
        if not chat_exists:
            raise HTTPException(status_code=404, detail="Chat not found")
        new_message = Message.create_message(db, private_chat_id)
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return {"status": "Message created", "new_message": new_message}
    raise HTTPException(status_code=405, detail="Method not allowed")


@router.get("/{message_id}")
async def get_message_by_id(
    request: Request, message_id: str, db: Session = Depends(get_db)
):
    if request.method == "GET":
        # Read user details
        message = db.query(Message).filter(Message.id == message_id).first()
        if message:
            return message
        raise HTTPException(status_code=404, detail="Message not found")


@router.delete("/{message_id}")
async def delete_message_by_id(
    request: Request, message_id: str, db: Session = Depends(get_db)
):
    if request.method == "DELETE":
        message = db.query(Message).filter(Message.id == message_id).first()
        if not message:
            raise HTTPException(status_code=404, detail="Message not found")
        db.delete(message)
        db.commit()
        return {"status": "Message deleted"}

    raise HTTPException(status_code=405, detail="Method not allowed")
