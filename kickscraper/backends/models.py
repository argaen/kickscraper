import abc


class BaseProject(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def uid(self):
        pass

    @property
    @abc.abstractmethod
    def title(self):
        pass

    @property
    @abc.abstractmethod
    def photo(self):
        pass

    @property
    @abc.abstractmethod
    def pledged(self):
        pass

    @property
    @abc.abstractmethod
    def goal(self):
        pass

    @property
    @abc.abstractmethod
    def state(self):
        pass

    @property
    @abc.abstractmethod
    def currency(self):
        pass

    @property
    @abc.abstractmethod
    def launched(self):
        pass

    @property
    @abc.abstractmethod
    def deadline(self):
        pass

    @property
    @abc.abstractmethod
    def backers_count(self):
        pass

    @property
    @abc.abstractmethod
    def rewards(self):
        pass

    @property
    @abc.abstractmethod
    def early_birds(self):
        pass
