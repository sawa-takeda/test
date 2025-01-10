from typing import Optional

from pydantic import BaseModel, Field

from datetime import date,datetime


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    due_date:datetime = Field(None)
 
class TaskCreate(TaskBase):
     due_date: datetime = Field(None,example="2000-01-01")
     class Config:
        orm_mode = True
 
class TaskCreateResponse(TaskCreate):
    id: int
    due_date: datetime =Field(None)
    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")
 
    class Config:
        orm_mode = True