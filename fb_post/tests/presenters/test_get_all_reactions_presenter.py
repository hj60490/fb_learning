import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest

from fb_post.constants.exception_messages import INVALID_OFFSET_LENGTH, \
    INVALID_LIMIT_LENGTH
from fb_post.interactors.storage_interfaces.dtos import ReactionDetailsDTO, \
    CommentDTO
from fb_post.presenters.get_all_reactions_presenter_implementation import \
    GetAllReactionsPresenterImplementation
from fb_post.tests.factories.models import PostFactory, ReactFactory
from fb_post.tests.factories.storage_dtos import UserDTOFactory, PostDTOFactory, \
    ReactDTOFactory, CommentDTOFactory


class TestsGetAllReactionsPresenter:

    def test_raise_exception_for_invalid_limit_value(self):
        exception_messages = INVALID_LIMIT_LENGTH[0]
        exception_res_status = INVALID_LIMIT_LENGTH[1]
        presenter = GetAllReactionsPresenterImplementation()

        with pytest.raises(BadRequest) as exception:
            presenter.raise_exception_for_invalid_limit_length()

        assert exception.value.message == exception_messages
        assert exception.value.res_status == exception_res_status

    def test_raise_exception_for_invalid_offset_value(self):
        exception_messages = INVALID_OFFSET_LENGTH[0]
        exception_res_status = INVALID_OFFSET_LENGTH[1]
        presenter = GetAllReactionsPresenterImplementation()

        with pytest.raises(BadRequest) as exception:
            presenter.raise_exception_for_invalid_offset_length()

        assert exception.value.message == exception_messages
        assert exception.value.res_status == exception_res_status

    def test_get_response_for_all_reactions_on_post(self, snapshot):
        user = [UserDTOFactory()]
        post = [PostDTOFactory()]
        react = [ReactDTOFactory(post_id=1)]
        reaction_details_dto = ReactionDetailsDTO(
            users=user,
            posts=post,
            reactions=react,
            comments=[]
        )
        presenter = GetAllReactionsPresenterImplementation()
        actual_output = presenter.get_response_for_all_reactions(
            reactions_details=reaction_details_dto
        )

        snapshot.assert_match(actual_output)

    def test_get_response_for_all_reactions_on_comment(self, snapshot):
        user = [UserDTOFactory()]
        post = [PostDTOFactory()]
        comment = [CommentDTOFactory()]
        react = [ReactDTOFactory(comment_id=1)]
        reaction_details_dto = ReactionDetailsDTO(
            users=user,
            posts=post,
            reactions=react,
            comments=comment
        )
        presenter = GetAllReactionsPresenterImplementation()
        actual_output = presenter.get_response_for_all_reactions(
            reactions_details=reaction_details_dto
        )

        snapshot.assert_match(actual_output)

    def test_get_response_for_all_reactions_on_reply(self, snapshot):
        user = [UserDTOFactory()]
        post = [PostDTOFactory()]
        comments = [CommentDTOFactory(), CommentDTOFactory(post_id=None, parent_comment_id=1, commented_by_id=1)]
        react = [ReactDTOFactory(comment_id=2)]
        reaction_details_dto = ReactionDetailsDTO(
            users=user,
            posts=post,
            reactions=react,
            comments=comments
        )
        presenter = GetAllReactionsPresenterImplementation()
        actual_output = presenter.get_response_for_all_reactions(
            reactions_details=reaction_details_dto
        )

        snapshot.assert_match(actual_output)

