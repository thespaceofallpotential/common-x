from formulation.sanitisation.sanitiser import (
    ISanitiser,
    SanitiserOptions,
)
from formulation.sanitisation.markdown.markdown_sanitiser import MarkdownSanitiser
from formulation.analysis.elemental_curator import ElementalCurator
from formulation.sanitisation.basic_sanitiser import BasicSanitiser
from formulation.sanitisation.stopword_sanitiser import StopwordSanitiser
from formulation.sanitisation.sanitiser_kind import SanitiserKind
from utils.custom_exception import CustomException


class SanitiserFactory:
    def build(self, curator: ElementalCurator, options: SanitiserOptions) -> ISanitiser:
        kind: SanitiserKind = (
            options.sanitiser_kind
            if options.sanitiser_kind is not None
            else SanitiserKind.BASIC
        )

        match kind.value:
            case SanitiserKind.BASIC.value:
                return BasicSanitiser(options)

            case SanitiserKind.MARKDOWN.value:
                return MarkdownSanitiser(curator, options)

            case SanitiserKind.STOPWORD.value:
                return StopwordSanitiser(options)

        raise CustomException(f"sanitiser factory: {type} not implemented error")


def build_sanitiser(curator: ElementalCurator, options: SanitiserOptions):
    sanitiser_factory = SanitiserFactory()

    sanitiser = sanitiser_factory.build(curator, options)

    return sanitiser
