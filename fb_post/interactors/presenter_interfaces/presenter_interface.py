import abc
from abc import ABC


class CreatePostPresenterInterface(ABC):

    @abc.abstractmethod
    def raise_exception_for_user_not_exist(self):
        pass







