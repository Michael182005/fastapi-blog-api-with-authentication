# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel



# app = FastAPI()



# @app.get("/blog")
# def index(limit = 10, published : bool = True, sort : Optional[str] = None):
    
    
#     if published:
#         return {"data" : f"{limit} published blogs from the db"}
    
#     else:
        
#         return { "data" : f"{limit} blogs from the db"}
        
    
    
# @app.get("/blog/{id}")
# def index(id : int):
    
#     return {"data" : "blogs form the db"}

# @app.get("/blog/unpublished")
# def unpublished():
    
#     return {"data" : "unpublished blogs"}


# class Blog(BaseModel):
    
#     title : str
#     body : str
#     published : Optional[bool]



# @app.post("/blog")
# def create_blog(blog : Blog):
    
#     return { "data" : f"blog has created with the title as {blog.title}"}