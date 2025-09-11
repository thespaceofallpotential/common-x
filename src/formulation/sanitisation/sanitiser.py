import abc

from core.strings import EMPTY
from formulation.sanitisation.sanitiser_options import SanitiserOptions
from utils.custom_exception import CustomException


class SanitiserResult:
    content: str = EMPTY
    frontmatter: str | None = None


class ISanitiser(metaclass=abc.ABCMeta):
    options: SanitiserOptions

    def __init__(self, options: SanitiserOptions) -> None:
        self.options = options

    @abc.abstractmethod
    def sanitise(self, content: str, i: int | None = None) -> SanitiserResult:
        raise CustomException("NOT IMPLEMENTED")
