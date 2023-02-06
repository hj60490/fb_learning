from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.storages.user_storage_implementation import \
    UserStorageImplementation
from fb_post.presenters.get_posts_presenter_implementation import \
    GetPostsPresenterImplementation
from fb_post.interactors.get_posts_interactor import GetPostsInteractor
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user_id']

    # storge implementation
    user_storage = UserStorageImplementation()
    post_storage = PostStorageImplementation()

    # presenters Implementation
    presenter = GetPostsPresenterImplementation()

    # interactor implementation
    interactor = GetPostsInteractor(
        post_storages=post_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    post_details = interactor.get_posts_wrapper(user_id=user_id)

    data = json.dumps(post_details, sort_keys=True, default=str)

    return HttpResponse(data, status=200)
