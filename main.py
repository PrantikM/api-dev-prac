from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()

class post(BaseModel):
  Title : str
  content : str
  published : bool = True
  rating : Optional[int] = None


my_posts = [{"title" : "title of post 1", "content" : "content of post 1", "id" : 1},
{"title" : "favourite foods", "content" : "i like pizza" , "id" : 2}] 

def findpost(id):
  for p in my_posts:
    if p["id"] == id:
      return p

@app.get("/")
async def root():
  return{"message": "Hello World"}


@app.get("/posts")
async def posts():
  return{"data" : my_posts}

@app.post("/posts")
async def create_posts(new_post :post):
  post_dict = new_post.dict()
  post_dict["id"] = randrange(0,10000000)
  my_posts.append(post_dict)
  return {"data" : post_dict}


@app.get("/posts/{id}")
async def get_post(id : int):
  post = findpost(id)
  return{"post_detail" : post}
