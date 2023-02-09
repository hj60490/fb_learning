
from abc import ABC


class CreatePostPresenterInterface(ABC):

    def raise_exception_for_user_not_exist(self):
        pass

    def raise_exception_for_invalid_content(self):
        pass






