
from fb_post.interactors.storage_interfaces.post_interface import PostInterface
from fb_post.interactors.storage_interfaces.user_interface import UserInterface
from fb_post.exceptions.custom_exceptions import InvalidUserException
from fb_post.interactors.presenter_interfaces.get_posts_presenter_interface \
    import GetPostsPresenterInterface


class GetPostsInteractor:

    def __init__(self, post_storages: PostInterface, user_storage: UserInterface
                 , presenter: GetPostsPresenterInterface):
        self.post_storage = post_storages
        self.user_storage = user_storage
        self.presenter = presenter

    def get_posts_wrapper(self, user_id: int):
        try:
            return self.get_posts(
                user_id=user_id
            )
        except InvalidUserException:
            self.presenter.raise_exception_for_user_not_exist()

    def get_posts(self, user_id: int):
        is_user_exists = self.user_storage.check_is_user_exists(user_id)

        if not is_user_exists:
            raise InvalidUserException

        posts = self.post_storage.get_posts(user_id)
        list_of_post_id = [post.post_id for post in posts]

        reactions = self.post_storage.get_all_reactions(list_of_post_id)

        comments = self.post_storage.get_comments(list_of_post_id)
        list_of_comment_id = [comment.comment_id for comment in comments]

        reactions_on_comments = self.post_storage.get_reactions_on_comments(
            list_of_comment_id)

        replies_on_comment = self.post_storage.get_replies_on_comment(
            list_of_comment_id)

        posts_details_dto = PostDetailsDto(
            PostDtoList=posts,
            ReactionPostDtoList=reactions,
            CommentOnPostDtoList=comments,
            RepliesDtoList=replies_on_comment,
            ReactionOnCommentDto=reactions_on_comments
        )

        return self.presenter.get_all_post_of_user(
            posts_details_dto=posts_details_dto
        )










