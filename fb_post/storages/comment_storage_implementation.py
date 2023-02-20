from typing import List

from fb_post.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from fb_post.interactors.storage_interfaces.dtos import CommentDTO
from fb_post.models import Comment


class CommentStorageImplementation(CommentStorageInterface):

    def get_comments(self, comments_ids: List[int]) -> \
            List[CommentDTO]:
        comments = Comment.objects.filter(comment_id__in=comments_ids)
        comment_dtos = [
            self._convert_comment_to_comment_dto(comment)
            for comment in comments
        ]
        return comment_dtos

    @staticmethod
    def _convert_comment_to_comment_dto(comment: Comment) -> CommentDTO:
        if comment.parent_comment:
            comment_dto = CommentDTO(
                comment_id=comment.id,
                content=comment.content,
                parent_comment_id=comment.parent_comment_id,
                commented_by_id=comment.commented_by_id,
                commented_at=comment.commented_at
            )
            return comment_dto
        else:
            comment_dto = CommentDTO(
                comment_id=comment.id,
                content=comment.content,
                post_id=comment.post_id,
                commented_by_id=comment.commented_by_id,
                commented_at=comment.commented_at
            )
            return comment_dto

