# Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text.

any_word = input(
    "Enter any word to tally how many times each letter in the alphabet was used in the word: ")
word_split = any_word.split(' ')
i = {a: any_word.count(a) for a in word_split}
print(i)
