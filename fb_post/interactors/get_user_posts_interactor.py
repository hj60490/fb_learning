from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostInterface
from fb_post.exceptions.custom_exceptions import InvalidUserException, \
    InvalidOffsetValue, InvalidLimitValue
from fb_post.interactors.presenter_interfaces.get_user_posts_presenter_interface \
    import GetPostsPresenterInterface
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto
from fb_post.interactors.storage_interfaces.dtos import ReactOnPostDto, \
    CommentOnPostDto, ReactionOnCommentDto, CommentOnCommentDto, UserDto, \
    RequestsParametersDTO
from fb_post.adapters.service_adapter import get_service_adapter
from typing import List, Dict, Any


class GetUserPostsInteractor:

    def __init__(
            self, post_storages: PostInterface,
            presenter: GetPostsPresenterInterface
    ):
        self.post_storage = post_storages
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
        except InvalidOffsetValue:
            self.presenter.raise_exception_for_invalid_offset_length()
        except InvalidLimitValue:
            self.presenter.raise_exception_for_invalid_limit_length()

    @staticmethod
    def _validate_user(user_id: int):
        adaptor = get_service_adapter()
        is_user_exists = adaptor.fb_post_auth.check_user_exists_or_not(user_id)

        if not is_user_exists:
            raise InvalidUserException

    def get_user_posts(
            self, user_id: int, requests_parameters_dto: RequestsParametersDTO
    ) -> PostDetailsDto:
        self._validate_limit_and_offset(requests_parameters_dto)
        self._validate_user(user_id)
        user_ids = [user_id]

        posts_dtos = self.post_storage.get_posts(
            user_id, requests_parameters_dto)
        post_ids = [post.post_id for post in posts_dtos]

        reactions_dtos = self.post_storage.get_all_reactions(post_ids)
        user_ids.extend(self._get_user_id_from_reaction(reactions_dtos))

        comments_dtos = self.post_storage.get_comments(post_ids)
        user_ids.extend([
            comment.commented_by_id
            for comment in comments_dtos
        ])
        comments_ids = [
            comment.comment_id
            for comment in comments_dtos
        ]

        # reaction on comments dtos
        reactions_on_comments_dtos = self.post_storage.get_reactions_on_comments(
            comments_ids
        )

        user_ids.extend(
            self._get_user_id_from_reaction_on_comment(
                reactions_on_comments_dtos))

        # user dtos
        adaptor = get_service_adapter()
        user_dtos = adaptor.fb_post_auth.get_users_dtos(list(set(user_ids)))

        user_posts_details_dto = PostDetailsDto(
            users=user_dtos,
            posts=posts_dtos,
            reactions_on_posts=reactions_dtos,
            comments=comments_dtos,
            reactions_on_comments=reactions_on_comments_dtos
        )
        return user_posts_details_dto

    @staticmethod
    def _validate_limit_and_offset(
            requests_parameters_dto: RequestsParametersDTO):
        offset = requests_parameters_dto.offset
        limit = requests_parameters_dto.limit

        if offset < 0:
            raise InvalidOffsetValue

        if limit < 0:
            raise InvalidLimitValue

    @staticmethod
    def _get_user_id_from_reaction(
            reactions: List[ReactOnPostDto]) -> List[int]:
        list_of_user_ids = [
            react.reacted_by_id
            for react in reactions
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

