from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.storages.comment_storage_implementation import \
    CommentStorageImplementation
from fb_post.storages.reaction_storage_implementation import \
    ReactionStorageImplementation
from fb_post.interactors.get_all_reactions_interactor import GetAllReactionsInteractor
from fb_post.presenters.get_all_reactions_presenter_implementation import \
    GetAllReactionsPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    query_params = kwargs['query_params']
    offset = query_params['offset']
    limit = query_params['limit']

    post_storage = PostStorageImplementation()
    comment_storage = CommentStorageImplementation()
    reaction_storage = ReactionStorageImplementation()
    presenter = GetAllReactionsPresenterImplementation()

    interactor = GetAllReactionsInteractor(
        post_storage=post_storage, comment_storage=comment_storage,
        reaction_storage=reaction_storage, presenter=presenter
    )

    interactor.get_all_reactions_wrapper(
        limit=limit, offset=offset
    )
