from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.interactors.create_post_interactor import CreatePostInteractor
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
# from fb_post.storages.user_storage_implementation import  \
#     UserStorageImplementation
from fb_post.presenters.create_post_presenter_implementation import \
    CreatePostPresenterImplementation
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    request_body = kwargs['request_data']
    content = request_body['content']
    user_id = request_body['user_id']

    # storage implementation
    post_storage = PostStorageImplementation()
    # user_storage = UserStorageImplementation()

    # presenter implementation
    presenter = CreatePostPresenterImplementation()

    # interactor implementation
    interactor = CreatePostInteractor(
        post_storage=post_storage,
        # user_storage=user_storage,
        presenter=presenter
    )

    interactor.create_post_wrapper(
        content=content, user_id=user_id
    )

    return HttpResponse(status=200)


