def vowel_remover(string):
    list_str = list(string)
    list_new = []
    for i in list_str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            pass
        else:
            list_new.append(i)
    vomit = ''
    for i in list_new:
        vomit += i
    return(vomit)
print(vowel_remover('Like wut?'))