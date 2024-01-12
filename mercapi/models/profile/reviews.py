from dataclasses import dataclass
from datetime import datetime
from typing import List

from mercapi.models.base import ResponseModel

@dataclass
class Review(ResponseModel):
    @dataclass
    class User(ResponseModel):
        id_: str    
        name: str
        photo_url: str
        photo_thumbnail_url: str

    subject: str
    fame: str
    message: str
    created: datetime
    user: User

@dataclass
class Reviews(ResponseModel):
    reviews: List[Review]
