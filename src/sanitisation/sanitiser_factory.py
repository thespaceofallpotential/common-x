from sanitisation.sanitiser import Sanitiser, SanitiserOptions


class SanitiserFactory:
    def build(self, options: SanitiserOptions | None) -> Sanitiser:
        return Sanitiser(options)
