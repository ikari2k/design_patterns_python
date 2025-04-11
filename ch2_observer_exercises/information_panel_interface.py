from abc import abstractmethod, ABC


class InformationPanel(ABC):

    @abstractmethod
    def get_info(self):
        pass