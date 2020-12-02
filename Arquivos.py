def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    print('Quantidade de palavras: ', len(wordList))
    print('Quantidade de caracteres: ', len(content))

readFile('text.txt')

