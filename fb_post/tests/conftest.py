import pytest
from fb_post.interactors.storage_interfaces.dtos import RequestsParametersDTO, \
    UserDto


@pytest.fixture()
def get_requests_parameters_dto_with_invalid_offset():
    get_requests_parameters_dto = RequestsParametersDTO(
        offset=-1, limit=2, sort_order="", post_content="")
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_parameters_dto_with_invalid_limit():
    get_requests_parameters_dto = RequestsParametersDTO(
        offset=1, limit=-1, sort_order="", post_content="")
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_parameters_dto():
    get_requests_parameters_dto = RequestsParametersDTO(
        offset=0, limit=2, sort_order="", post_content="")
    return get_requests_parameters_dto


@pytest.fixture()
def get_user_dto():
    get_user_dto = UserDto(
        user_id=5,
        name="harsh",
        profile_pic="www.google.com"
    )
    return get_user_dto
