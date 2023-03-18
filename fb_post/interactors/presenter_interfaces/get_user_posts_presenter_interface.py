from abc import ABC
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto
from django.http import response


class GetPostsPresenterInterface(ABC):

    def raise_exception_for_user_not_exist(self):
        pass

    def get_all_posts_of_user(self, posts_details_dto: PostDetailsDto):
        pass

