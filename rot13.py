import win32clipboard as clip


def rot13(s: str):
    rotted = []
    offset_lowercase = ord("a")
    offset_uppercase = ord("A")
    for c in s:
        if not c.isalpha():
            rotted.append(c)
            continue

        offset = offset_lowercase if c.islower() else offset_uppercase
        i = (ord(c) - offset + 13) % 26
        rotted.append(chr(i + offset))

    return "".join(rotted)


clip.OpenClipboard()
s = clip.GetClipboardData(clip.CF_UNICODETEXT)
s = rot13(s)
clip.EmptyClipboard()
clip.SetClipboardText(s, clip.CF_UNICODETEXT)
clip.CloseClipboard()
