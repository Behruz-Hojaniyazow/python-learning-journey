from typing import TypedDict

class StudentData(TypedDict):
    name: str
    course: int
    score: int | float