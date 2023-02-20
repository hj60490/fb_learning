import abc
from abc import ABC
from typing import List

from fb_post.interactors.storage_interfaces.dtos import CommentDTO


class CommentStorageInterface(ABC):

    @abc.abstractmethod
    def get_comments(self, comments_ids: List[int]) -> \
            List[CommentDTO]:
        pass
