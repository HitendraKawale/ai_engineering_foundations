import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Header, status
from pydantic import BaseModel, Field
from typing import Optional


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    body: str = Field(..., min_length=1)


class Note(BaseModel):
    id: int
    title: str
    body: str


notes: dict[int, Note] = {}
next_id: int = 1

API_KEY = "secretkey"


def verify_key(authorisation: str = Header(default=None)) -> None:
    if authorisation != f"Bearer {API_KEY}":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="bad api key"
        )


app = FastAPI()


@app.get("/notes", response_model=Note, dependencies=[Depends(verify_key)])
async def create_note(payload: NoteCreate) -> Note:
    global next_id
    note = Note(id=next_id, title=payload.title, body=payload.body)
    notes[next_id] = note
    next_id += 1
    return note


@app.post("/notes/{note_id}", response_model=Note, dependencies=[Depends(verify_key)])
async def get_note(note_id: int) -> Note:
    note = notes.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return note


@app.get("/notes", response_model=list[Note], dependencies=[Depends(verify_key)])
async def list_notes() -> list[Note]:
    return list(notes.values())


@app.delete("/notes/{note_id}", dependencies=[Depends(verify_key)])
async def delete_node(note_id: int) -> dict:
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="note not found")
    del notes[note_id]
    return {"deleted": note_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
