from abc import ABC


class UserInterface(ABC):

    def check_is_user_exists(self, user_id: int) -> bool:
        pass


