import math

def words_check(text: str):
    listOfText = text.split()
    goodWord = []
    print(listOfText)
    for i in listOfText:
        lenghtOfWord = len(i)
        countOfBadWord = 0
        correctWord = ""
        for j in i:
            if ((ord(j) >= 65 and
                ord(j) <= 90) or
                ord(j) >= 90 and
                ord(j) <= 122):
                continue
            else:
                countOfBadWord += 1
                correctWord = i.replace(j, "")

        print(i, countOfBadWord, math.ceil(lenghtOfWord/2))
        if (countOfBadWord < math.ceil(lenghtOfWord/2)):
            if (len(correctWord) != 0):
                goodWord.append(correctWord)
            else:
                goodWord.append(i)
    
    lengthOfGoodWord = len(goodWord)
    for i in range(0, lengthOfGoodWord):
        goodWord[i] = goodWord[i][0].upper() +  goodWord[i][1:].lower()
        
    return goodWord

print(words_check("hEllO My FriEnDs!!! thIS i$s A tE%sT For your #p#r#o#b#l#e#m a"))

