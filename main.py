from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
  return{"message": "Hello World"}


@app.get("/posts")
async def posts():
  return{"data" : "these are your posts"}

@app.post("/createposts")
def create_posts(payload :dict = Body(...)):
  print(payload)
  return {"new_post" : f"title : {payload['Title']} content : {payload['content']}"}