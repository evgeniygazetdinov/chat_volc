from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session

from chat_volc.models.models import User, PrivateChat

from chat_volc.settings import get_db

router = APIRouter(prefix="/private_chat", tags=["PrivateChats"])


@router.post("/")
async def create_chat(
    request: Request, db: Session = Depends(get_db), user_ids: str = None
):
    if request.method == "POST":
        user_ids_list = user_ids.split(",")
        user_one_id = user_ids_list[0]
        user_two_id = user_ids_list[1]
        first_user_exists = db.query(
            db.query(User).filter(User.id == user_one_id).exists()
        ).scalar()
        second_user_exists = db.query(
            db.query(User).filter(User.id == user_two_id).exists()
        ).scalar()
        if not first_user_exists or not second_user_exists:
            raise HTTPException(status_code=404, detail="one of users not found")
        new_chat = PrivateChat.create_chat(db, user_one_id, user_two_id)
        db.add(new_chat)
        db.commit()
        db.refresh(new_chat)
        return {"status": "private Chat created", "new_chat": new_chat}

    raise HTTPException(status_code=405, detail="Method not allowed")


@router.get("/{private_chat_id}")
async def get_chat(
    request: Request, private_chat_id: str, db: Session = Depends(get_db)
):
    if request.method == "GET":
        private_chat = (
            db.query(PrivateChat).filter(PrivateChat.id == private_chat_id).first()
        )
        if private_chat:
            return private_chat
        else:
            raise HTTPException(status_code=404, detail="private_chat not found")

@router.get("/{private_chat_id}/all_messages")
async def get_all_chat_messages(private_chat_id: str, db: Session = Depends(get_db)):
        private_chat = (
            db.query(PrivateChat).filter(PrivateChat.id == private_chat_id).first()
        )
        if private_chat:
            # sorted_messages = sorted(private_chat.messages, key=lambda x: x.created_at)
            return private_chat.messages
        else:
            raise HTTPException(status_code=404, detail="private_chat not found")


@router.delete("/{private_chat_id}")
async def delete_chat(
    request: Request, private_chat_id: str, db: Session = Depends(get_db)
):
    private_chat = (
        db.query(PrivateChat).filter(PrivateChat.id == private_chat_id).first()
    )
    if not private_chat:
        raise HTTPException(status_code=404, detail="private_chat not found")
    db.delete(private_chat)
    db.commit()
    return {"status": "private_chat deleted"}
