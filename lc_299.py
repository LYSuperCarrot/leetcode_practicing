secret = "1807", guess = "7810"

def secretAndGuess(secret, guess):
    bulls = 0
    cows = 0
    diff = [0] * 10
    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            if diff[ord(g) - ord('0')] > 0:
                cows += 1
            if diff[ord(s) - ord('0')] < 0:
                cows -= 1
            diff[ord(g) - ord('0')] -= 1
            diff[ord(s) - ord('0')] += 1
    return f'{bulls}A{cows}B'