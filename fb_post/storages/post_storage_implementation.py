from fb_post.interactors.storage_interfaces.post_interface import PostInterface
from fb_post.models.models import Post


class PostStorageImplementation(PostInterface):

    def create_post(self, content: str, user_id: int):
        Post.objects.create(content=content, posted_by_id=user_id)
        return



