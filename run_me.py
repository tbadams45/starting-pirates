import json
import os

def load_SCOWL_words(files):
	all_contents = []
	for file in files:
		with open(file) as word_file:
			contents = word_file.readlines()
			for line in contents:
				all_contents.append(line[:-1])
	return {i: 1 for i in all_contents}

def load_words():
    with open('words_dictionary.json') as word_file:
    	valid_words = json.load(word_file)
        #valid_words = set(word_file.read().split())

    return valid_words


def find_longer_words(all_words, base_word):
	characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	longer_words = []
	for char in characters:
			for index in range(0, len(base_word)+1):
					new_base = base_word[0:index] + char + base_word[index:]
					#print(new_base)
					if new_base in all_words:
						longer_words.append(new_base)

	return longer_words

def unique(non_unique_list):
	unique_list = []
	for elem in non_unique_list:
		if elem not in unique_list:
			unique_list.append(elem)

	return unique_list

def find_next_batch_of_longer_words(all_words, current_longest_word_list):
	list_of_longer_words = []
	length_of_words = len(current_longest_word_list[0]) + 1
	found_longer_words = False
	for word in current_longest_word_list:
		list_of_longer_words.extend(find_longer_words(all_words, word))

	if len(list_of_longer_words) > 0:
		found_longer_words = True

	return (found_longer_words, length_of_words, unique(list_of_longer_words))

def find_longest_riddle_word(all_words):
	longest_words = {1: ['a', 'i']}
	longest_length = 1
	found_longer_words = True
	while found_longer_words == True:
		(found_longer_words, longest_length, list_of_longer_words) = find_next_batch_of_longer_words(all_words, longest_words[longest_length])
		if found_longer_words == True:
			longest_words[longest_length] = list_of_longer_words
			print(longest_words[longest_length])
			print("longest_length" + str(longest_length))


	return longest_words

def find_next_smallest_word(all_words, test_word):
	smaller_words = []
	for index in range(len(test_word)):
		small_test = test_word[:index] + test_word[index+1:]
		if small_test in all_words:
			smaller_words.append(small_test)

	print(smaller_words)
	return smaller_words


if __name__ == '__main__':
    #english_words = load_words()
    #print(len(english_words.keys()))
    
    fp = os.path.join("SCOWL", "final")
    SCOWL_paths = [os.path.join(fp, "english-words.10"),
                   os.path.join(fp, "english-words.20"),
                   os.path.join(fp, "english-words.35"),
                   os.path.join(fp, "english-words.40"),
                   os.path.join(fp, "english-words.50"),
                   os.path.join(fp, "english-words.55"),
                   os.path.join(fp, "english-words.60"),
                   os.path.join(fp, "english-words.70"),
                   os.path.join(fp, "english-words.80"),
                   os.path.join(fp, "english-words.95")]
    SCOWL_words = load_SCOWL_words(SCOWL_paths)

    results = find_longest_riddle_word(SCOWL_words)
    # splittings!
