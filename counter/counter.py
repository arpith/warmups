def counter(letters):
    letter_counts = {}
    for l in letters:
        if (l != ' '):
            if l not in letter_counts:
                letter_counts[l] = 1
            else:
                letter_counts[l] += 1
    return letter_counts
