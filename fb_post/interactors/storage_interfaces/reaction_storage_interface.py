import abc
from abc import ABC
from typing import List

from fb_post.interactors.storage_interfaces.dtos import ReactionDTO


class ReactionStorageInterface(ABC):

    @abc.abstractmethod
    def get_all_reactions(self, limit: int, offset: int) -> List[ReactionDTO]:
        pass

