import tiktoken

enc = tiktoken.get_encoding("cl100k_base")


def build_prompt(paths, char_limit):
    buf = []
    for p in paths:
        txt = p.read_text(encoding="utf-8")[:char_limit]
        buf.append(f"## {p.relative_to(p.anchor)}\n\n{txt}")
    return "\n\n".join(buf)
