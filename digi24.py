def calculate(partial_word,complete_word):
    found=''
    for latter in partial_word:
        latter_found=False
        while complete_word and not latter_found:

            if latter  == complete_word[0]:
                 complete_word = complete_word[1:]
                 found+=latter
                 latter_found = True
            else:
                complete_word = complete_word[1:]
                latter_found = False

    if found == partial_word:
        return True
    else:
        return False

        

if __name__=="__main__":
    partial_word=input()
    complete_word=input()
    print(calculate(partial_word,complete_word))

   