from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Post:
    content: str
    posted_by: int
    posted_at: datetime
