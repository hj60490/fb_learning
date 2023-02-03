from fb_post.interactors.presenter_interfaces.get_posts_presenter_interface \
    import GetPostsPresenterInterface
from django_swagger_utils.drf_server.exceptions import (
    BadRequest
)
from fb_post.constants.exception_messages import INVALID_USER_ID


class GetPostsPresenterImplementation(GetPostsPresenterInterface):

    def raise_exception_for_user_not_exist(self):
        return BadRequest(*INVALID_USER_ID)



