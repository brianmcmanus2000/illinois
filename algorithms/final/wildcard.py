# Python program for wild card matching using single
# traversal

def wildCard(txt, pat):
    n = len(txt)
    m = len(pat)
    i = 0
    j = 0
    startIndex = -1
    match = 0

    while i < n:

        # Characters match or '?' in pattern matches
        # any character.
        if j < m and (pat[j] == '?' or pat[j] == txt[i]):
            i += 1
            j += 1

        elif j < m and pat[j] == '*':

            # Wildcard character '*', mark the current
            # position in the pattern and the text as a
            # proper match.
            startIndex = j
            match = i
            j += 1

        elif startIndex != -1:

            # No match, but a previous wildcard was found.
            # Backtrack to the last '*' character position
            # and try for a different match.
            j = startIndex + 1
            match += 1
            i = match

        else:

            # If none of the above cases comply, the
            # pattern does not match.
            return False

    # Consume any remaining '*' characters in the given
    # pattern.
    while j < m and pat[j] == '*':
        j += 1

    # If we have reached the end of both the pattern and
    # the text, the pattern matches the text.
    return j == m

if __name__ == "__main__":
    txt = "SCHWABRAINCADBRANCH"
    pat = "ABR*CAD*BRA"
    print("true" if wildCard(txt, pat) else "false")