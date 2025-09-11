from formulation.sanitisation.dev.dev_markdown_helpers import strip_markdown
from formulation.sanitisation.stopwords import remove_stopwords
from formulation.sanitisation.string_helpers import (
    clean_str,
    get_frontmatter,
    pad_new_lines,
    periods_to_new_line,
    prepare_str,
    shrink_whitespace,
    strip_frontmatter,
)
from formulation.sanitisation.common import (
    ISanitiser,
    SanitiserOptions,
    SanitiserResult,
)


class Sanitiser(ISanitiser):
    options: SanitiserOptions

    def __init__(self, options: SanitiserOptions) -> None:
        self.options = options

    def sanitise(self, content: str) -> SanitiserResult:
        _ = self.options

        x = content

        result = SanitiserResult()

        if _.strip_frontmatter:
            frontmatter = get_frontmatter(x)

            if frontmatter is not None:
                result.frontmatter = frontmatter

                x = strip_frontmatter(x)

        if _.strip_links or _.strip_callouts:
            x = strip_markdown(x)
            # TODO: simplify this...

        if _.prepare:
            x = prepare_str(x)

        if _.stopwords:
            x = remove_stopwords(x, _.stopwords)

        if _.strip_links:
            x = strip_markdown(x)

        if _.periods_to_new_line:
            x = periods_to_new_line(x)

        # per line

        #   per word

        if _.clean:
            x = clean_str(x)

        if _.pad_new_line:
            x = pad_new_lines(x)

        result.content = shrink_whitespace(x)

        return result


# const lines = value.split(NEWLINE);
# for (let i = 0; i < lines.length; i++) {
#     let line = lines[i];
#     line = tokens.stripTokens(line);
#     line = this.clean(line);
#     let words = line.split(SPACE);
#     words = tokens.stripNumbers(words);
#     if (options.aggressiveSanitisation && words.length < options.minSequence) {
#         lines[i] = EMPTY;
#         continue;
#     }
#     words = tokens.stripWords(words);
#     line = words.join(SPACE);
#     line = tokens.stripPhrases(line);
#     line = shrinkWhitespace(line);
#     // // TODO: count space characters...
#     if (options.aggressiveSanitisation && line.split(SPACE).length < options.minSequence) {
#         lines[i] = EMPTY;
#     } else {
#         lines[i] = line;
#     }
# }
# value = lines.join(NEWLINE);
