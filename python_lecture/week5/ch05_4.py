word = input("Input alphabet:")


if word.isalpha() :
    if word == 'a' or word == 'b' or word == 'c' or word == 'd' or word == 'e':
        print("\"", word, "\"","is vowel")
    elif word == 'A' or word == 'B' or word == 'C' or word == 'D' or word == 'E':
        print("\"", word, "\"","is vowel")
    elif len(word) >= 2:
        print("Error")
    else :
        print("\"", word, "\"","is consonant")
else :
    print("Error")

    
