from fb_post.exceptions.custom_exceptions import InvalidLimitValue, \
    InvalidOffsetValue
from fb_post.interactors.storage_interfaces.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostInterface
from fb_post.interactors.presenter_interfaces.get_all_reaction_presenter_interface import GetAllReactionsPresenterInterface


class GetAllReactionsInteractor:
    def __init__(
            self, post_storage: PostInterface,
            reaction_storage: ReactionStorageInterface,
            comment_storage: CommentStorageInterface,
            presenter: GetAllReactionsPresenterInterface
    ):
        self.post_storage = post_storage
        self.reaction_storage = reaction_storage
        self.comment_storage = comment_storage
        self.presenter = presenter

    def get_all_reactions_wrapper(self, limit: int, offset: int):
        try:
            reaction_details = self.get_all_reactions(
              limit=limit, offset=offset
            )

            return self.presenter.get_response_for_all_reactions(
                reaction_details
            )
        except InvalidLimitValue:
            self.presenter.raise_exception_for_invalid_limit_length()
        except InvalidOffsetValue:
            self.presenter.raise_exception_for_invalid_limit_length()

    def get_all_reactions(
            self, limit: int, offset: int
    ):
        if limit < 0:
            raise InvalidLimitValue

        if offset < 0:
            raise InvalidOffsetValue

        reactions = self.reaction_storage.get_all_reactions()
        return reactions




