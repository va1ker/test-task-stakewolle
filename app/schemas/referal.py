from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Referal(BaseModel):
    referal_code: Optional[str]
    expiration_time: Optional[datetime]

class ReferalUser(BaseModel):
    referal_data: str
    user_id: int