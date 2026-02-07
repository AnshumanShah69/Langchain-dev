from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int
    classroom: str

max : Student = {"name": "Maxine", "age":20, "classroom": "10A"}
print(max["name"])