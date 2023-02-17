import abc
from abc import ABC


class GetAllReactionsPresenterInterface(ABC):

    @abc.abstractmethod
    def get_response_for_all_reactions(self, reactions_details):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_offset_length(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_limit_length(self):
        pass

