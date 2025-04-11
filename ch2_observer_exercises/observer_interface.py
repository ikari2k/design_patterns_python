from abc import abstractmethod, ABC


class Observer(ABC):

    @abstractmethod
    def update(self):
        pass

    def __repr__(self):
        return self.__class__.__name__
