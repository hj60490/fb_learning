class ServiceAdapter:

    @property
    def users(self):
        from fb_post.adapters.user_service_adaptor import UserServiceAdaptor
        return UserServiceAdaptor()


def get_service_adapter():
    return ServiceAdapter()
