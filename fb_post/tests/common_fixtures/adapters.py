def check_user_exists_or_not_mocker(mocker):
    mock_obj = mocker.patch("fb_post.adapters.fb_post_auth_service_adaptor."
                 "FbPostAuthServiceAdaptor.check_user_exists_or_not")

    return mock_obj


def get_users_dtos_mocker(mocker):
    mock_obj = mocker.patch("fb_post.adapters.fb_post_auth_service_adaptor."
                            "FbPostAuthServiceAdaptor.get_users_dtos")

    return mock_obj