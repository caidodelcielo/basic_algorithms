def start_liangs_algorithm():
    processWords()

def processWords():
    with open('liangs_algorithm/liang_pattern.txt') as f:
        patterns = [word for line in f for word in line.split()]

    with open('liangs_algorithm/liang_word_list.txt') as f1:
        words = [word for line in f1 for word in line.split()]

    for word in words:
        finalDict = {}

        for pattern in patterns:
            patternWithout = ''.join(c for c in pattern if not c.isdigit())
            patternDotIndex = patternWithout.find('.')
            patternWithoutDot = patternWithout.replace('.', '')
            patternWithNumWithoutDot = pattern.replace('.', '')
            foundIndex = False

            if patternDotIndex != -1:
                if patternDotIndex == 0:
                    foundIndex = word.startswith(patternWithoutDot)
                else:
                    foundIndex = word.endswith(patternWithoutDot)
            else:
                found = word.find(patternWithoutDot)
                if found != -1:
                    foundIndex = True

            if foundIndex:
                patternIndex = word.find(patternWithoutDot)

                for idx, letter in enumerate(patternWithNumWithoutDot):
                    if letter.isdigit():
                        indexToAdd = 0
                        numbersToAdd = ''

                        if patternWithNumWithoutDot.startswith(letter):
                            indexToAdd = patternIndex-1
                            numbersToAdd = letter
                            #print(patternWithNumWithoutDot)
                        elif patternWithNumWithoutDot.endswith(letter):
                            indexToAdd = patternIndex + len(patternWithoutDot) - 1
                            numbersToAdd = letter
                            #print(patternWithNumWithoutDot)
                        else:
                            searchString = patternWithNumWithoutDot[idx-1] + patternWithNumWithoutDot[idx+1]
                            searchStringIndex = word.find(searchString, patternIndex)
                            indexToAdd = searchStringIndex
                            numbersToAdd = letter
                            #print(patternWithNumWithoutDot)

                        if (str(indexToAdd) in finalDict):
                            if (finalDict[str(indexToAdd)] < int(numbersToAdd)):
                                finalDict[str(indexToAdd)] = int(numbersToAdd)
                        else:
                            finalDict[str(indexToAdd)] = int(numbersToAdd)

        #print(finalDict)

        finalWord = []
        for idx, value in enumerate(word):
            finalWord.append(value)
            if (str(idx) in finalDict):
                if (is_odd(finalDict[str(idx)])):
                    finalWord.append('-')

        print(''.join([str(x) for x in finalWord]))

    print('Finished')


def is_odd(num):
    return num & 0x1
