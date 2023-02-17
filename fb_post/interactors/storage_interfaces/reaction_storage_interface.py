from abc import ABC
from typing import List

from fb_post.interactors.storage_interfaces.dtos import ReactionDTO


class ReactionStorageInterface(ABC):

    def get_all_reactions(self) -> List[ReactionDTO]:
        pass

