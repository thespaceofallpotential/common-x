from sanitisation.sanitiser import Sanitiser, SanitiserOptions


class SanitiserFactory:
    def build(self, options: SanitiserOptions) -> Sanitiser:
        return Sanitiser(options)


def build_sanitiser(options: SanitiserOptions):
    sanitiser_factory = SanitiserFactory()

    sanitiser = sanitiser_factory.build(options)

    return sanitiser
