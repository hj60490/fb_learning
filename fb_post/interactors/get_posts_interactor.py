from fb_post.interactors.storage_interfaces.post_interface import PostInterface
from fb_post.interactors.storage_interfaces.user_interface import UserInterface
from fb_post.exceptions.custom_exceptions import InvalidUserException
from fb_post.interactors.presenter_interfaces.get_posts_presenter_interface \
    import GetPostsPresenterInterface
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto


class GetUserPostsInteractor:

    def __init__(self, post_storages: PostInterface, user_storage: UserInterface
                 , presenter: GetPostsPresenterInterface):
        self.post_storage = post_storages
        self.user_storage = user_storage
        self.presenter = presenter

    def get_user_posts_wrapper(self, user_id: int):
        try:
            posts_details = self.get_user_posts(
                user_id=user_id
            )

            return self.presenter.get_all_post_of_user(
                posts_details_dto=posts_details
            )
        except InvalidUserException:
            self.presenter.raise_exception_for_user_not_exist()

    def get_user_posts(self, user_id: int):
        is_user_exists = self.user_storage.check_is_user_exists(user_id)

        if not is_user_exists:
            raise InvalidUserException

        posts = self.post_storage.get_posts(user_id)
        post_ids = [post.post_id for post in posts]

        reactions = self.post_storage.get_all_reactions(post_ids)
        post_reactions_ids = [reaction.reaction_id for reaction in reactions]

        comments = self.post_storage.get_comments(post_ids)
        post_comment_ids = [comment.comment_id for comment in comments]

        reactions_on_comments = self.post_storage.get_reactions_on_comments(
            post_comment_ids)
        reactions_on_comments_ids = [
            reaction.reaction_id
            for reaction in reactions_on_comments
        ]

        replies_on_comment = self.post_storage.get_replies_on_comment(
            post_comment_ids)
        replies_ids = [reply.comment_id for reply in replies_on_comment]

        list_of_users = self.user_storage.get_list_of_users(
            post_ids, post_reactions_ids, post_comment_ids,
            reactions_on_comments_ids, replies_ids)

        user_posts_details = self._get_user_post_details_dto(list_of_users,
                                                             posts, reactions,
                                                             comments,
                                                             replies_on_comment,
                                                             reactions_on_comments)

        return user_posts_details

    @staticmethod
    def _get_user_post_details_dto(list_of_users, posts, reactions, comments,
                                   replies_on_comment, reactions_on_comments):
        posts_details_dto = PostDetailsDto(
            users=list_of_users,
            posts=posts,
            reactions_on_posts=reactions,
            comments_on_post=comments,
            replies=replies_on_comment,
            reactions_on_comments=reactions_on_comments
        )
        return posts_details_dto
