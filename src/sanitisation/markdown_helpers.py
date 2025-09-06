from core.strings import (
    BAR,
    CLOSE_CALLOUT,
    EMPTY,
    NEWLINE,
    OPEN_CALLOUT,
    OPEN_SQUARE_BRACKET_PAIR as OPEN_PAIR,
    CLOSE_SQUARE_BRACKET_PAIR as CLOSE_PAIR,
    OPEN_SQUARE_BRACKET,
    MIDDLE_BRACKET_PAIR,
    CLOSE_BRACKET,
)
from core.types import index_withoutexception


def get_internal_link_text(link: str):
    parts = link.split(BAR)
    text = parts[0] if len(parts) == 1 else parts[1]
    return text


def parse_internal_links(line: str) -> str:
    i_start = index_withoutexception(line, OPEN_PAIR)

    if i_start < 0:
        return line

    line_parts: list[str] = []

    while i_start > 0:
        i_end = index_withoutexception(line, CLOSE_PAIR, i_start)

        if i_end < 0:
            line_parts.append(line)
            break

        before = line[:i_start]

        link_value = line[i_start + len(OPEN_PAIR) : i_end]

        link_text = get_internal_link_text(link_value)

        after = line[i_end + len(CLOSE_PAIR) :]

        i_start = index_withoutexception(after, OPEN_PAIR)

        line_parts.extend([before, link_text])

        if i_start < 0:
            line_parts.append(after)
            break

        line = after

    return str.join(EMPTY, line_parts)


def get_external_link_text(link: str):
    parts = link.split(MIDDLE_BRACKET_PAIR)
    text = parts[0]
    return text


def parse_externals_links(line: str) -> str:
    i_start = index_withoutexception(line, OPEN_SQUARE_BRACKET)

    if i_start < 0:
        return line

    line_parts: list[str] = []

    while i_start > 0:
        i_middle = index_withoutexception(line, MIDDLE_BRACKET_PAIR, i_start)
        i_end = index_withoutexception(line, CLOSE_BRACKET, i_middle)

        if i_end < 0:
            line_parts.append(line)
            break

        before = line[:i_start]

        link_value = line[i_start + len(OPEN_SQUARE_BRACKET) : i_end]

        link_text = get_external_link_text(link_value)

        after = line[i_end + len(CLOSE_BRACKET) :]

        i_start = index_withoutexception(after, OPEN_SQUARE_BRACKET)

        line_parts.extend([before, link_text])

        if i_start < 0:
            line_parts.append(after)
            break

        line = after

    return str.join(EMPTY, line_parts)


def parse_callouts(line: str) -> str:
    if not line.startswith(OPEN_CALLOUT):
        return line

    i_end = index_withoutexception(line, CLOSE_CALLOUT, len(OPEN_CALLOUT))

    if i_end < 0:
        return line

    # after = line[i_end + len(CLOSE_CALLOUT) :]

    return EMPTY


def strip_markdown(x: str) -> str:
    lines = x.split(NEWLINE)

    parts: list[str] = []

    for line in lines:
        parsed = parse_internal_links(line)

        parsed = parse_externals_links(parsed)

        parsed = parse_callouts(parsed)

        parts.append(parsed)

    x = str.join(NEWLINE, parts)

    return x


# export const stripLinks = (value: string): string => {
#     let plain = "";
#     value = lines.join(NEWLINE);

#     for (let l = 0; l < lines.length; l++) {
#         let line = lines[l];

#         let s = line.indexOf("[");

#         let max = 5;

#         while (s >= 0 && max-- > 0) {
#             if (s > 0 && line.at(s - 1) === "^") {
#                 s = line.indexOf("[", s + 1);

#                 continue;
#             }

#             const m = line.indexOf("](", s);
#             const e = line.indexOf(")", m);

#             if (m < 0 || e < 0) break;

#             let link = line.substring(s + 1, e);

#             if (link.includes("](")) link = link.split("](")[0];

#             const before = line.slice(0, s);
#             const after = line.slice(e + 1);

#             const parts = [before, link, after];

#             debug.out(pretty(parts));

#             line = parts.join("");

#             lines[l] = line;

#             s = line.indexOf("[");
#         }
#     }

#     value = lines.join(NEWLINE);

#     debug.out(value);

#     // for (let i = 0; i < value.length; i++) {
#     //     const a = value[i];

#     //     if (!isLink && a === "[") {
#     //         isLink = !isLink;
#     //         i++;
#     //     } else {
#     //         if (!isLink) {
#     //             plain = plain + a;
#     //         } else {
#     //             let link = "";

#     //             for (let h = i; h < value.length; h++) {
#     //                 const b = value[h];

#     //                 if (isLink && b === "]") {
#     //                     isLink = !isLink;
#     //                     h++;
#     //                     i = h;
#     //                     break;
#     //                 } else {
#     //                     link = link + b;
#     //                 }
#     //             }

#     //             const parts = link.split("|");

#     //             plain = plain + (parts.length === 1 ? parts[0] : parts[1]);
#     //         }
#     //     }
#     // }

#     plain = value;

#     debug.out("mid:" + plain);

#     return plain.trim();
# };
