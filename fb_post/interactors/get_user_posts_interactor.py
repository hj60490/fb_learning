from fb_post.interactors.storage_interfaces.post_interface import PostInterface
from fb_post.interactors.storage_interfaces.user_interface import UserInterface
from fb_post.exceptions.custom_exceptions import InvalidUserException
from fb_post.interactors.presenter_interfaces.get_user_posts_presenter_interface \
    import GetPostsPresenterInterface
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto
from fb_post.interactors.storage_interfaces.dtos import ReactOnPostDto, \
    CommentOnPostDto, ReactionOnCommentDto, CommentOnCommentDto, UserDto, RequestsParametersDTO
from typing import List, Dict, Any


class GetUserPostsInteractor:

    def __init__(self, post_storages: PostInterface, user_storage: UserInterface
                 , presenter: GetPostsPresenterInterface):
        self.post_storage = post_storages
        self.user_storage = user_storage
        self.presenter = presenter

    def get_user_posts_wrapper(
            self, user_id: int, requests_parameters_dto: RequestsParametersDTO):
        try:
            posts_details = self.get_user_posts(
                user_id=user_id, requests_parameters_dto=requests_parameters_dto
            )

            return self.presenter.get_all_posts_of_user(
                posts_details_dto=posts_details
            )
        except InvalidUserException:
            self.presenter.raise_exception_for_user_not_exist()

    def _validate_user(self, user_id: int):
        is_user_exists = self.user_storage.check_is_user_exists(user_id)

        if not is_user_exists:
            raise InvalidUserException

    def get_user_posts(
            self, user_id: int, requests_parameters_dto: RequestsParametersDTO
    ) -> PostDetailsDto:
        self._validate_limit_or_offset(requests_parameters_dto)
        self._validate_user(user_id)
        user_ids = [user_id]

        posts_dtos = self.post_storage.get_posts(user_id)
        post_ids = [post.post_id for post in posts_dtos]

        reactions_dtos = self.post_storage.get_all_reactions(post_ids)
        user_ids.extend(self._get_user_id_from_reaction(reactions_dtos))

        dict_of_comments_and_replies = self._get_comments_for_posts(post_ids)
        user_ids.extend(self._get_user_id_from_comments(
            dict_of_comments_and_replies['comments']
        ))

        user_ids.extend(self._get_user_id_from_replies(
            dict_of_comments_and_replies["replies_on_comment_dtos"]))
        replies_ids = [comment.comment_id for comment in
                       dict_of_comments_and_replies["replies_on_comment_dtos"]]
        dict_of_comments_and_replies["post_comment_ids"].extend(replies_ids)

        # reaction on comments dtos
        reactions_on_comments_dtos = self.post_storage.get_reactions_on_comments(
            dict_of_comments_and_replies["post_comment_ids"])
        user_ids.extend(
            self._get_user_id_from_reaction_on_comment(
                reactions_on_comments_dtos))

        # user dtos
        user_dtos = self.user_storage.get_users_details(
            list(set(user_ids)))

        user_posts_details_dto = PostDetailsDto(
            users=user_dtos,
            posts=posts_dtos,
            reactions_on_posts=reactions_dtos,
            comments_on_post=dict_of_comments_and_replies["comments"],
            replies=dict_of_comments_and_replies["replies_for_comments"],
            reactions_on_comments=reactions_on_comments_dtos
        )
        return user_posts_details_dto

    def _validate_limit_or_offset(
            self, requests_parameters_dto: RequestsParametersDTO):
        offset = requests_parameters_dto.offset
        limit = requests_parameters_dto.limit

        if offset < 0:
            self.presenter.raise_exception_for_invalid_offset_length()
            return

        if limit < 0:
            self.presenter.raise_exception_for_invalid_limit_length()
            return

    @staticmethod
    def _get_user_id_from_reaction(
            reactions: List[ReactOnPostDto]) -> List[int]:
        list_of_user_ids = [
            react.reacted_by_id
            for react in reactions
        ]
        return list_of_user_ids

    @staticmethod
    def _get_user_id_from_comments(
            comments: List[CommentOnPostDto]) -> List[int]:
        list_of_user_ids = [
            comment.commented_by_id
            for comment in comments
        ]
        return list_of_user_ids

    @staticmethod
    def _get_user_id_from_replies(
            replies_on_comment: List[CommentOnCommentDto]) -> List[int]:
        list_of_user_ids = [
            comment.commented_by_id
            for comment in replies_on_comment
        ]
        return list_of_user_ids

    @staticmethod
    def _get_user_id_from_reaction_on_comment(
            reactions: List[ReactionOnCommentDto]) -> \
            List[int]:
        list_of_user_ids = [
            react.reacted_by_id
            for react in reactions
        ]
        return list_of_user_ids

    def _get_comments_for_posts(
            self, post_ids: List[int]) -> Dict[str, Any]:
        comments_dtos = self.post_storage.get_comments(post_ids)
        post_comment_ids = [
            comment.comment_id for comment in comments_dtos]

        replies_on_comment_dtos = self.post_storage.get_replies_on_comment(
            post_comment_ids)

        replies_ids = [comment.comment_id for comment in
                       replies_on_comment_dtos]
        post_comment_ids.extend(replies_ids)
        return {
            "comments": comments_dtos,
            "replies_for_comments": replies_on_comment_dtos,
            "post_comment_ids": post_comment_ids,
            "replies_on_comment_dtos":replies_on_comment_dtos
        }

