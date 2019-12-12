line = 'love'
wordsLine = 'velo low vole lovee volvell lowly lower lover levo loved love lovee lowe lowes lovey lowan lowa evolve loves volvelle lowed love'

lineSet = set(line.rstrip())
wordsList = list(set(wordsLine.split()))

i = len(wordsList) - 1
counter = 0

while i >= 0:
    wordsList[i] = set(list(wordsList[i]))
    i = i - 1

for wordSet in wordsList:
    print(wordSet, lineSet)
    if wordSet == lineSet:
        counter = counter + 1

print(counter)

