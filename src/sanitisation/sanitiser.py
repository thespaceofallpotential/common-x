from sanitisation.markdown_helpers import strip_markdown
from sanitisation.stopwords import remove_stopwords
from sanitisation.string_helpers import (
    clean_str,
    get_frontmatter,
    pad_new_lines,
    periods_to_new_line,
    prepare_str,
    shrink_whitespace,
    strip_frontmatter,
)
from core.strings import EMPTY


class SanitiserOptions:
    def __init__(self, stopwords: str | None = None) -> None:
        self.stopwords = stopwords

    clean: bool = True

    pad_new_line: bool = True

    periods_to_new_line: bool = True

    prepare: bool = True

    stopwords: str | None

    strip_frontmatter: bool = True

    strip_links: bool = True

    strip_callouts: bool = True

    strip_any_numeric: bool = True


class SanitiserResult:
    content: str = EMPTY
    frontmatter: str | None = None


class Sanitiser:
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
