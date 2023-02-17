import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post_auth.interactors.get_all_users_interactor import GetUsersInteractor

from fb_post_auth.presenters.get_all_users_presenter_implementation import \
    GetUsersPresenterImplementation
from fb_post_auth.storages.user_storage_implementation import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # print("********************")
    # print(kwargs)
    query_params = kwargs['query_params']
    limit = query_params['limit']
    offset = query_params['offset']

    user_storage = UserStorageImplementation()
    presenter = GetUsersPresenterImplementation()
    interactor = GetUsersInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    users_dict = interactor.get_all_users_wrapper(
        offset=offset, limit=limit,
    )
    data = json.dumps(users_dict)

    return HttpResponse(data, status=200)
