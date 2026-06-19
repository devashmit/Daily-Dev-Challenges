"""Todo CRUD API — Day 21 FastAPI | Author: devashmit"""
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Todo CRUD API")

class TC(BaseModel): title:str; description:Optional[str]=None; completed:bool=False
class TU(BaseModel): title:Optional[str]=None; description:Optional[str]=None; completed:Optional[bool]=None
class TO(BaseModel): id:int; title:str; description:Optional[str]; completed:bool

_db:dict[int,dict]={}; _n=1

def _get(tid):
    if tid not in _db: raise HTTPException(404,"Todo not found")
    return _db[tid]

@app.get("/todos",response_model=list[TO])
def list_todos(): return list(_db.values())

@app.get("/todos/{tid}",response_model=TO)
def get_todo(tid:int): return _get(tid)

@app.post("/todos",response_model=TO,status_code=201)
def create(b:TC):
    global _n; todo={"id":_n,**b.model_dump()}; _db[_n]=todo; _n+=1; return todo

@app.put("/todos/{tid}",response_model=TO)
def update(tid:int,b:TU):
    todo=_get(tid)
    for k,v in b.model_dump(exclude_unset=True).items(): todo[k]=v
    return todo

@app.delete("/todos/{tid}",status_code=204)
def delete(tid:int): _get(tid); del _db[tid]
