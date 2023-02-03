from abc import ABC
from .dtos import Post


class PostInterface(ABC):

    def create_post_object(self, content: str, user_id: int):
        pass

