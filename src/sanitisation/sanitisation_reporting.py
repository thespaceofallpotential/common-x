from sanitisation.sanitisation_regex import SanitisationTypes


REPORT = True

REPORT_TYPES = set(
    [
        # SanitisationTypes.STRUCTURED_MARKDOWN_EXTERNAL_LINK,
        # SanitisationTypes.STRUCTURED_MARKDOWN_INTERNAL_LINK,
        SanitisationTypes.STRUCTURED_PERIOD_SPACE,
        SanitisationTypes.STRUCTURED_WHITESPACE,
    ]
)
