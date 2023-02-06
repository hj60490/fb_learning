from fb_post.interactors.storage_interfaces.user_interface import UserInterface
from fb_post.models.models import User
from typing import List
from fb_post.interactors.storage_interfaces.dtos import UserDto


class UserStorageImplementation(UserInterface):

    def check_is_user_exists(self, user_id: int) -> bool:
        return User.objects.filter(id=user_id).exists()

    def get_list_of_users(self, post_ids: List[int],
                          post_reactions_ids: List[int],
                          post_comment_ids: List[int],
                          reactions_on_comments_ids: List[int],
                          replies_ids: List[int]) -> List[UserDto]:

        all_reactions = []
        all_reactions.append(post_reactions_ids)
        all_reactions.append(reactions_on_comments_ids)
        union_list_of_all_reactions = list(set().union(*all_reactions))

        all_comments = []
        all_comments.append(post_comment_ids)
        all_comments.append(replies_ids)
        union_list_of_comments = list(set().union(*all_comments))
        users_for_post = User.objects.filter(post__id__in=post_ids,
                                    react__id__in=union_list_of_all_reactions,
                                    comment__id__in=union_list_of_comments)

        list_of_users = [
            self._convert_user_object_to_dto(user)
            for user in users_for_post
        ]

        return list_of_users

    @staticmethod
    def _convert_user_object_to_dto(user):
        user = UserDto(
            user_id=user.id,
            name=user.name,
            profile_pic=user.profile_pic
        )
        return user
