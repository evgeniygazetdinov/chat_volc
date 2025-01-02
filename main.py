from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
app = FastAPI()
from chat_volc.models.models import User, PrivateChat, Message
import uuid
from chat_volc.settings import SessionLocal, get_db
from chat_volc.models.schemas import UserCreate
from fastapi import Request


@app.get("/healf_check")
async def healf_check():
   return {"message": "Hello World"}


@app.api_route("/user/", methods=["POST"], response_model=UserCreate)
async def create_user(request: Request, db: Session = Depends(get_db), username: str = None):
   if request.method == "POST":
      new_user = User(uid=str(uuid.uuid4()), username=username)
      db.add(new_user)
      db.commit()
      db.refresh(new_user)
      return {"status": "User created", "user": new_user}

   raise HTTPException(status_code=405, detail="Method not allowed")

@app.api_route("/user/{user_id}", methods=["POST", "GET", "PUT", "DELETE"], response_model=UserCreate)
async def manage_user(user_id: str, db: Session = Depends(get_db), username: str = None):
   if app.request.method == "GET":
      user = db.query(User).filter(User.id == user_id).first()
      if user:
         return user
      raise HTTPException(status_code=404, detail="User not found")

   elif app.request.method == "PUT":
      user = db.query(User).filter(User.id == user_id).first()
      if not user:
         raise HTTPException(status_code=404, detail="User not found")
      if username:
         user.username = username
      db.commit()
      return {"status": "User updated", "user": user}

   elif app.request.method == "DELETE":
      user = db.query(User).filter(User.id == user_id).first()
      if not user:
            raise HTTPException(status_code=404, detail="User not found")
      db.delete(user)
      db.commit()
      return {"status": "User deleted"}

   raise HTTPException(status_code=405, detail="Method not allowed")


@app.api_route("/private_chat/{private_chat_id}", methods=["POST", "GET", "DELETE"])
async def manage_chat(private_chat_id: str, user_ids: str, db: Session = Depends(get_db)):
   if app.request.method == "POST":
      user_ids_list = user_ids.split(",")
      user_one_id = user_ids_list[0]
      user_two_id = user_ids_list[1]
      first_user = db.query(User).filter(User.id == user_one_id).exists()
      second_user = db.query(User).filter(User.id == user_two_id).exists()
      if not first_user or not second_user:
         raise HTTPException(status_code=404, detail="User not found")
      new_chat = PrivateChat.create_chat(db, user_one_id, user_two_id)
      db.add(new_chat)
      db.commit()
      db.refresh(new_chat)
      return {"status": "privateChat created", "new_chat": new_chat}
      
   elif app.request.method == "GET":
      # Read user details
      private_chat = db.query(PrivateChat).filter(PrivateChat.id == private_chat_id).first()
      if private_chat:
            return private_chat
      raise HTTPException(status_code=404, detail="private_chat not found")

   # TODO update that condition on next release
   # elif app.request.method == "PUT":
   #    # Update user details
   #    user = db.query(User).filter(User.id == user_id).first()
   #    if not user:
   #          raise HTTPException(status_code=404, detail="User not found")
   #    if username:
   #          user.username = username
   #    db.commit()
   #    return {"status": "User updated", "user": user}

   elif app.request.method == "DELETE":
      # Delete user
      private_chat = db.query(PrivateChat).filter(PrivateChat.id == private_chat_id).first()
      if not private_chat:
            raise HTTPException(status_code=404, detail="private_chat not found")
      db.delete(private_chat)
      db.commit()
      return {"status": "private_chat deleted"}

   raise HTTPException(status_code=405, detail="Method not allowed")

@app.api_route("/private_chat/{private_chat_id}/{message_id}", methods=["POST", "GET", "PUT", "DELETE"])
def manage_message(private_chat_id: str, message_id: str, db: Session = Depends(get_db)):
   if app.request.method == "POST":
      chat_exists = db.query(PrivateChat).filter(PrivateChat.id == private_chat_id).exists()
      if not chat_exists:
         raise HTTPException(status_code=404, detail="Chat not found")
      new_message = Message.create_message(db, private_chat_id, message_id)
      db.add(new_message)
      db.commit()
      db.refresh(new_message)
      return {"status": "Message created", "new_message": new_message}
   elif app.request.method == "GET":
      # Read user details
      message = db.query(Message).filter(Message.id == message_id).first()
      if message:
            return message
      raise HTTPException(status_code=404, detail="Message not found")
   elif app.request.method == "DELETE":
      # Delete user
      message = db.query(Message).filter(Message.id == message_id).first()
      if not message:
            raise HTTPException(status_code=404, detail="Message not found")
      db.delete(message)
      db.commit()
      return {"status": "Message deleted"}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8009, reload=True)