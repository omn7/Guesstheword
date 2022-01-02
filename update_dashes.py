def update_dashes(word, dashes, guess):
	for i in range(len(word)):
		if word[i] == guess:
			dashes = dashes[:i] + guess + dashes[i+1:]
			
	return dashes
