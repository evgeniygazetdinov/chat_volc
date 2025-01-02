from fastapi import FastAPI
app = FastAPI()



@app.get("/")
async def index():
   return {"message": "Hello World"}

@app.get("/healf_check")
async def healf_check():
   return {"message": "Hello World"}

@app.get("/get_instance")
async def get_instance():
   return {"message": "Hello World"}
