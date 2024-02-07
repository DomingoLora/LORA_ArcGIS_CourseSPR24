# PART 5: WORD GAME

letter_scores = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}

word = input("Enter a word: ").lower()
score = sum(score for letters, score in letter_scores.items() if any(char in letters for char in word))

print(f"Scrabble score for '{word}': {score}")
