from typing import Literal
from navigation.classificators.data.names import NAMES_DB

Gender = Literal["Female", "Male", "Not Nound"]

def get_gender_by_name(name: str) -> Gender:
    classification = NAMES_DB.get(name.strip().upper(), None)
    if classification == "M": return "Male"
    if classification == "F": return "Female"
    return "Not Found"
