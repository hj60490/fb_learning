from abc import ABC
from typing import List
from fb_post.interactors.storage_interfaces.dtos import UserDto


class UserInterface(ABC):

    def check_is_user_exists(self, user_id: int) -> bool:
        pass

    def get_list_of_users(self, post_ids: List[int],
                          post_reactions_ids: List[int],
                          post_comment_ids: List[int],
                          reactions_on_comments_ids: List[int],
                          replies_ids: List[int]) -> List[UserDto]:
        pass



