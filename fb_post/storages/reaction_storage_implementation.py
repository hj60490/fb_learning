from typing import List

from fb_post.interactors.storage_interfaces.dtos import ReactionDTO
from fb_post.interactors.storage_interfaces.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post.models import React


class ReactionStorageImplementation(ReactionStorageInterface):

    def get_all_reactions(self, limit: int, offset: int) -> List[ReactionDTO]:
        reactions = React.objects.all()
        reactions = reactions[offset: limit + offset]
        reaction_dtos = [
            self._convert_reaction_to_reaction_dto(reaction)
            for reaction in reactions
        ]
        return reaction_dtos

    @staticmethod
    def _convert_reaction_to_reaction_dto(reaction: React) -> ReactionDTO:
        if reaction.post:
            reaction_dto = ReactionDTO(
                reacted_by_id=reaction.reacted_by_id,
                reaction=reaction.reaction,
                post_id=reaction.post_id,
                reaction_id=reaction.id,
                reacted_at=reaction.reacted_at,
                comment_id=None
            )
            return reaction_dto
        else:
            reaction_dto = ReactionDTO(
                reacted_by_id=reaction.reacted_by_id,
                reaction=reaction.reaction,
                comment_id=reaction.comment_id,
                reaction_id=reaction.id,
                reacted_at=reaction.reacted_at,
                post_id=None
            )
            return reaction_dto
