from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class DataLogger(ABC):
    button_type: str = None
    timestamp: datetime = None
    buttons = []

    @abstractmethod
    def log_event(self):
        pass


@dataclass
class ProfessorButton(DataLogger):
    count: int = 0
    button_type: str = "Professor"
    timestamp = None

    @classmethod
    def log_event(cls):
        """
    The log_event function takes the button type and timestamp of when it was pressed,
    and returns a string with that information.

    :param cls: Refer to the object itself
    :return: A string
    :doc-author: Trelent
    """
        cls.timestamp = datetime.now()
        cls.count += 1
        return f"{cls.button_type} button was pressed at {cls.timestamp}"

    def __repr__(self):
        """
    The __repr__ function is used to create a string representation of an object.
    This function is called when the print() function or str() are invoked on an object.
    The __repr__ method should return a string that would make sense to someone reading it,
    and could be used as code to recreate the same object.

    :param self: Refer to the object itself
    :return: A string representation of the object
    :doc-author: Trelent
    """
        return self.log_event()


@dataclass
class StudentButton(ProfessorButton):
    # This class is merely a template and represents the concept of StudentButton class
    button_type: str = "Student"


@dataclass
class VisitorButton(ProfessorButton):
    # This class is merely a template and represents the concept of StudentButton class
    button_type: str = "Visitor"
