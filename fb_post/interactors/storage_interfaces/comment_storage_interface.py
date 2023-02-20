import abc
from abc import ABC
from typing import List

from fb_post.interactors.storage_interfaces.dtos import CommentDTO


class CommentStorageInterface(ABC):

    @abc.abstractmethod
    def get_comments_on_reactions(self, comments_ids: List[int]) -> \
            List[CommentDTO]:
        pass

    def get_parent_comment_for_reply(self, parent_comment_ids: List[int]) -> \
            List[CommentDTO]:
        pass
