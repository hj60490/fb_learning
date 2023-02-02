from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.interactors.create_post_interactor import CreatePostInteractor
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.storages.user_storage_implementation import  \
    UserStorageImplementation
from fb_post.presenters.presenter_implementation import PresenterImplementation
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    content = kwargs['content']
    user_id = kwargs['user_id']

    # storage implementation
    post_storage = PostStorageImplementation()
    user_storage = UserStorageImplementation()

    # presenter implementation
    presenter = PresenterImplementation()

    # interactor implementation
    interactor = CreatePostInteractor(
        post_storage=post_storage,
        user_storage=user_storage,
        presenter=presenter
    )

    post_obj = interactor.create_post(
        content=content, user_id=user_id
    )

    data = json.dumps(post_obj)
    return HttpResponse(data, status=200)


