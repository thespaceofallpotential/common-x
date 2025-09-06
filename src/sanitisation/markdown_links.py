def strip_links(x: str) -> str:
    return x

# export const stripLinks = (value: string): string => {
#     let plain = "";
#     // let isLink = false;

#     const lines = value.split(NEWLINE);

#     const OPEN = "[[";
#     const CLOSE = "]]";

#     debug.out(value);

#     try {
#         for (let l = 0; l < lines.length; l++) {
#             let line = lines[l];

#             let start = line.indexOf(OPEN);

#             let max = 50;

#             while (start >= 0 && max-- > 0) {
#                 const end = line.indexOf(CLOSE, start);

#                 if (end === -1) break;

#                 let link = line.substring(start + 2, end);

#                 if (link.includes("|")) link = link.split("|")[1];

#                 const before = line.slice(0, start);
#                 const after = line.slice(end + 2);

#                 const parts = [before, link, after];

#                 debug.out(pretty(parts));

#                 line = parts.join("");

#                 lines[l] = line;

#                 start = line.indexOf(OPEN);
#             }
#         }
#     } catch (e) {
#         console.error(e);
#     }

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
