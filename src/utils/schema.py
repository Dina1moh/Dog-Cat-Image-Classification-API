from pydantic import BaseModel

class prediction_result(BaseModel):
    class_index: int
    class_name: str
    confidence: float
    