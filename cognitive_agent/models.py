from typing import List, Literal
from pydantic import BaseModel, Field

class Task(BaseModel):
    id: str
    title: str
    objective: str
    priority: Literal["low", "medium", "high", "critical"] = "medium"
    dependencies: List[str] = Field(default_factory=list)
    validation: str

class Plan(BaseModel):
    goal: str
    assumptions: List[str] = Field(default_factory=list)
    tasks: List[Task]
    risks: List[str] = Field(default_factory=list)
    success_criteria: List[str] = Field(default_factory=list)
