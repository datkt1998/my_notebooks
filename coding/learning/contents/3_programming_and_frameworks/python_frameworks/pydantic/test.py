import csv
import os
from typing import List

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    ValidationInfo,
    field_validator,
)

filedir = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(filedir, "data/testcase.csv")


class DataModel(BaseModel):
    name: str = Field(min_length=2, max_length=15)
    age: int = Field(ge=1, le=120)
    bank_account: float = Field(ge=0, default=0)

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str, info: ValidationInfo) -> str:
        return str(v).capitalize()


class ValidatedModels(BaseModel):
    validated: List[DataModel]


validated_rows = []

with open(FILE_NAME, "r") as f:
    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        try:
            validated_rows.append(DataModel(**row))
        except ValidationError as ve:
            error = ve.errors()[0]["msg"]
            print(error)
