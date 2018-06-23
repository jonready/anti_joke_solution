with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
ending = "is"
reslst = []
for i in valid_words:
	if i[0] == 'p' and i[-2:] == "is":		
		reslst.append(i)

thefile = open('results.txt', 'w')
for item in reslst:
  thefile.write("%s\n" % item)
print len(reslst)