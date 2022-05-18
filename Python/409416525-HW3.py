#定義一個函式來尋找字元偏移後的值
def lasso_letter( letter, shift_amount ):
    #ord()可以把char變為ascii word
    #把值存到letter_code
    letter_code = ord(letter.lower())
    
    #字元'a'的ascii word
    a_ascii = ord('a')

    #共26個字母
    alphabet_size = 26

    #解碼，順便處理超出範圍的結果
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)

    #把ascii word轉為char
    decoded_letter = chr(true_letter_code)

    #回傳已解碼的字元
    return decoded_letter

#定義一個函式來尋找字串偏移後的值
def lasso_word( word, shift_amount ):

    #把decoded_word的值初始化
    decoded_word = ""

    #檢查每個字串中的字元
    for letter in word:
        
        #decode字元，並把結果存進decoded_letter
        decoded_letter = lasso_letter(letter, shift_amount)

        #把decoded_letter的值加到decoded_word裡面
        decoded_word = decoded_word + decoded_letter

    # 回傳已解碼的字串
    return decoded_word

#那一段隱藏寶藏的位置和日期
print(lasso_word( "Ncevy", 13 ) )
print(lasso_word( "gpvsui", 25 ) )
print(lasso_word( "ugflgkg", -18 ) )
print(lasso_word( "wjmmf", -1 ) )