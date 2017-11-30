import sys

from srcs.lexer import *

def usage():
	print "python <filename>"
	sys.exit(1)

def processFile(fileaname):
	lexems = []
	# le mot cle 'with' est une bonne partique en python
	# en sortant tu 'with', le fichier est automatiquement et proprement ferme 
	with open(fileaname, 'r') as fd:
		i = 0
		for line in fd:
			lexems.append(lex(line, i))
			i += 1

	for lex in lexems:
		print lex

# Cette condition cheque juste le fait que c'est bien ce fichier qui a ete lancer par le shell
if __name__ == '__main__':
	if (len(sys.argv) != 2):
		usage()
	else:
		processFile(sys.argv[1])