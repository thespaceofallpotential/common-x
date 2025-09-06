from sanitisation.markdown_links import strip_links
from sanitisation.stopwords import remove_stopwords
from sanitisation.string_helpers import (
    clean_str,
    periods_to_new_line,
    prepare_str,
    strip_frontmatter,
)


class SanitiserOptions:
    def __init__(self, stopwords: str | None = None) -> None:
        self.stopwords = stopwords

    clean: bool = True

    periods_to_new_line: bool = True

    prepare: bool = True

    stopwords: str | None

    strip_frontmatter: bool = True

    strip_links: bool = True


class Sanitiser:
    options: SanitiserOptions

    def __init__(self, options: SanitiserOptions) -> None:
        self.options = options

    def sanitise(self, content: str) -> str:
        _ = self.options
        x = content

        if _.prepare:
            x = prepare_str(x)

        if _.stopwords:
            x = remove_stopwords(x, _.stopwords)

        if _.strip_frontmatter:
            x = strip_frontmatter(x)

        if _.strip_links:
            x = strip_links(x)

        if _.periods_to_new_line:
            x = periods_to_new_line(x)

        # per line

        #   per word

        if _.clean:
            x = clean_str(x)

        return x


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
