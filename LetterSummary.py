
# Letter Summary

any_word = input(
    "Enter any word to tally how many times each letter in the alphabet was used in the word: ").lower()
word_output = {x: any_word.count(x) for x in any_word}
print(word_output)
