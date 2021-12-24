import string
import win32clipboard as clip


def rot13(s):
    s = list(s)
    for i, letter in enumerate(s):
        letter: str
        if not letter.isalpha():
            continue
        alphabet = (
            string.ascii_lowercase if letter.islower() else string.ascii_uppercase
        )
        j = alphabet.find(letter)
        j = (j + 13) % 26
        s[i] = alphabet[j]
    return "".join(s)


clip.OpenClipboard()
s = clip.GetClipboardData(clip.CF_UNICODETEXT)
s = rot13(s)
clip.EmptyClipboard()
clip.SetClipboardText(s, clip.CF_UNICODETEXT)
clip.CloseClipboard()
