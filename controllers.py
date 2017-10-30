import abc

@abc.abstractproperty
class AbstractController:

    @abc.abstractmethod
    def update_view(self):
        ...



class Controller(AbstractController):

    def __init__(self):
        ...

    def update_view(self):
        ...