from pydantic import BaseModel, EmailStr, Field
from typing import Optional
### pydantic is a data validation and settings management library for Python, based on type annotations. It allows you to define data models with type hints and provides automatic validation and parsing of input data.

class Customer(BaseModel):
    name: str = "anshu"
    age: Optional[int] = None
    email: EmailStr
    score:int =  Field(gt=0, lt=10, default = 3, description="Score must be between 0 and 10")

# new_customer = {"age": 54}
# new_customer = {"age": "54", "email": "anshue@xample.com", "score": 9.0}

#this is getting created as a pydantic object and we can convert to datatype as we prefer
new_customer = {"age": "54", "email": "anshue@xample.com"}

customer = Customer(**new_customer)

customer_dict = dict(customer)
customer_json = customer.model_dump_json()
print(customer_dict["name"])
print(customer_json)