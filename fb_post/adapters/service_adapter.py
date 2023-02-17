class ServiceAdapter:

    @property
    def fb_post_auth(self):
        from fb_post.adapters.fb_post_auth_service_adaptor import FbPostAuthServiceAdaptor
        return FbPostAuthServiceAdaptor()


def get_service_adapter():
    return ServiceAdapter()
