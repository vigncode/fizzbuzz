import re
import os
import sys

def formatting_file(file_path):
    with open(file_path,"r") as f1:

        file_text = f1.read()
        file_text= file_text.replace('\n',' ')
        file_word_list=file_text.split(" ")
        [file_word_list.remove('') for i in range(0,file_word_list.count(''))]
        [file_word_list[count].strip() for count in range(0,len(file_word_list))]
    return(file_word_list)

def unique_words(file_path):
    file_word_list=formatting_file(file_path)
    unique_word_set= set(file_word_list)
    unique_word_tuple=tuple(unique_word_set)
    return(unique_word_tuple)

def count_the_articles(file_path):
    """     f1= open(file_path,"r")
    file_text = f1.read()
    file_text= file_text.replace('\n',' ')
    file_word_list=file_text.split(" ")
    [file_word_list.remove('') for i in range(0,file_word_list.count(''))]
    [file_word_list[count].strip() for count in range(0,len(file_word_list))] """
    file_word_list=formatting_file(file_path)

    article_list =["a", "the", "at", "run", "to","and","are","or","for","an","this"]
    article_list_count = []
    for article in article_list:
        article_list_count.append(file_word_list.count(article))
    total_article=sum(article_list_count)
    return total_article

def sorted_words(file_path):
    """     f1= open(file_path,"r")
    file_text = f1.read()
    file_text= file_text.replace('\n',' ')
    file_word_list=file_text.split(" ")
    [file_word_list.remove('') for i in range(0,file_word_list.count(''))]
    [file_word_list[count].strip() for count in range(0,len(file_word_list))] """
    file_word_list=formatting_file(file_path)

    word_len_list = [len(word) for word in file_word_list]

    dictionary = {}
    dictionary =dictionary.fromkeys(set(file_word_list),0)
    for word in list(dictionary.keys()):
        for word2 in file_word_list:
            if word2 == word:
                dictionary[word]=dictionary[word]+1
    
    #[print(f'{word}:{count}') for word, count in zip(dictionary.keys(),dictionary.values)]
    #[print(f'{word}:{count}') for word, count in zip(list(dictionary.keys()),list(dictionary.values()))]
    word_set=list(set(file_word_list))
    word_len=[len(word) for word in word_set]
    word_rep_count = [word_set.count(i) for i in word_set]
    len_dict ={}
    for word,word_len_count in zip(word_set,word_len):
        if word_len_count in len_dict:
            len_dict[word_len_count].append(word)
        else:
            len_dict[word_len_count]=[word]
    #print(len_dict)
    len_dict_sort={}
    sorted_keys =list(len_dict.keys())
    sorted_keys.sort(reverse = True)
    sorted_word_list=[]
    for i in sorted_keys:
        len_dict_sort[i]=len_dict[i]
        for wrd in len_dict_sort[i]:
            sorted_word_list.append(wrd)
    
    #sorted_word_list =list(len_dict_sort.values())
    #print(sorted_word_list)
    return(sorted_word_list)
    #[print(f'''list of words with word length {word_len} :  {",".join(word_list)}\n''') for word_len,word_list in zip(len_dict_sort.keys(),len_dict_sort.values()) ]


def character_word_count(file_path):
    """     f1= open(file_path,"r")
    file_text = f1.read()
    file_text= file_text.replace('\n',' ')
    file_word_list=file_text.split(" ")
    [file_word_list.remove('') for i in range(0,file_word_list.count(''))]
    [file_word_list[count].strip() for count in range(0,len(file_word_list))] """

    file_word_list=formatting_file(file_path)
    word_len_list = [len(word) for word in file_word_list]

    dictionary = {}
    dictionary =dictionary.fromkeys(set(file_word_list),0)
    for word in list(dictionary.keys()):
        for word2 in file_word_list:
            if word2 == word:
                dictionary[word]=dictionary[word]+1
    
    #[print(f'{word}:{count}') for word, count in zip(dictionary.keys(),dictionary.values)]
    #[print(f'{word}:{count}') for word, count in zip(list(dictionary.keys()),list(dictionary.values()))]
    word_set=list(set(file_word_list))
    word_len=[len(word) for word in word_set]
    word_rep_count = [word_set.count(i) for i in word_set]
    word_dict ={}
    for word,word_len_count in zip(word_set,word_len):
        if word in word_dict.keys():
            continue
        else:
            #print(word)
            word_dict[word]=word_len_count

            
    return(word_dict)

def starts_with_vow(file_path):
    """     f1= open(file_path,"r")
    file_text = f1.read()
    file_text= file_text.replace('\n',' ')
    file_word_list=file_text.split(" ")
    [file_word_list.remove('') for i in range(0,file_word_list.count(''))]
    [file_word_list[count].strip() for count in range(0,len(file_word_list))] """
    file_word_list=formatting_file(file_path)

    word_len_list = [len(word) for word in file_word_list]
    word_set=list(set(file_word_list))
    count = 0
    for word in word_set:
        if re.search(r'^[aeiou]',word):
            count=count+1
    return(count)

def rare_words(book_path,dict_path):
    """     f1= open(book_path,"r")
    f2 = open(dict_path,"r")
    file_text = f1.read()
    dict_test=f2.read()
    file_text= file_text.replace('\n',' ')
    file_word_list=file_text.split(" ")
    [file_word_list.remove('') for i in range(0,file_word_list.count(''))]
    [file_word_list[count].strip() for count in range(0,len(file_word_list))] """
    file_word_list=formatting_file(book_path)
    with open(dict_path,"r") as f2:
        dict_test=f2.read()


    word_set=list(set(file_word_list))
    rare_words_list=[]
    for word in word_set:
        if word not in dict_test:
            rare_words_list.append(word)
    return(rare_words_list)

def unused_word(book1_path,book2_path,book3_path,dict_path):
    """    f1= open(book1_path,"r")
    f2= open(book2_path,"r")
    f3= open(book3_path,"r")

    f4 = open(dict_path,"r")
    file1_text = f1.read()
    file2_text = f2.read()
    file3_text = f3.read()
    dict_test = f4.read()

    file1_text= file1_text.replace('\n',' ')
    file1_word_list=file1_text.split(" ")
    [file1_word_list.remove('') for i in range(0,file1_word_list.count(''))]
    [file1_word_list[count].strip() for count in range(0,len(file1_word_list))]
    word_set1=set(file1_word_list)


    file2_text= file1_text.replace('\n',' ')
    file2_word_list=file1_text.split(" ")
    [file2_word_list.remove('') for i in range(0,file2_word_list.count(''))]
    [file2_word_list[count].strip() for count in range(0,len(file2_word_list))]
    word_set2=set(file2_word_list)

    file3_text= file1_text.replace('\n',' ')
    file3_word_list=file1_text.split(" ")
    [file3_word_list.remove('') for i in range(0,file3_word_list.count(''))]
    [file3_word_list[count].strip() for count in range(0,len(file3_word_list))]
    word_set3=set(file3_word_list)

    dict_test= dict_test.replace('\n',' ')
    dict_test_list=dict_test.split("\n")
    [dict_test_list.remove('') for i in range(0,dict_test_list.count(''))]
    [dict_test_list[count].strip() for count in range(0,len(dict_test_list))]
    """   
    file1_word_list=formatting_file(book1_path)
    file2_word_list=formatting_file(book2_path)
    file3_word_list=formatting_file(book3_path)
    dict_test_list=formatting_file(dict_path)

    word_set1=set(file1_word_list)
    word_set2=set(file2_word_list)
    word_set3=set(file3_word_list)

    dict_set=set(dict_test_list)

    unused_words_set=dict_set.difference(word_set1,word_set2,word_set3)
    unused_words_list = list(unused_words_set)
    return(unused_words_list)

    


program_path =os.path.split(sys.argv[0])
program_folder= program_path[0]
book1_path = os.path.join(program_folder,"Book1.txt")
book2_path = os.path.join(program_folder,"Book2.txt")
book3_path = os.path.join(program_folder,"Book3.txt")
dict_path = os.path.join(program_folder,"20k.txt")
unique_words_book1 = unique_words(book1_path)
#{print(word) for word in unique_words_book1}
print(f'unique words list is : {unique_words_book1}\n')

count_article = count_the_articles(book1_path)
print(f'article count is : {count_article}\n')

word_sort_book1=sorted_words(book1_path)
print(f'sorted word list in book1 is : {word_sort_book1}\n')

char_count_book1=character_word_count(book1_path)
print(f'charecter count of words in book1: {char_count_book1}\n')

vowel_word_count_book1=starts_with_vow(book1_path)
print(f'vowel word count in book1: {vowel_word_count_book1}\n')

rare_words_book1 =rare_words(book1_path,dict_path)
print(f'rare words in book1 is : {rare_words_book1}\n')

rare_words_book2 =rare_words(book2_path,dict_path)
print(f'rare words in book2 is : {rare_words_book2}\n')

rare_words_book3 =rare_words(book3_path,dict_path)
print(f'rare words in book3 is : {rare_words_book3}\n')

words_not_used = unused_word(book1_path,book2_path,book3_path,dict_path)
print(f'unused words in book1 is : {words_not_used}\n')


