import re

# 前處理-斜、粗體；移除特殊char
def remove(s):
    remove_chars = r'\*' # 適用於斜體(*)、粗體(**)
    # re.sub(哪些char要被換, 換成甚麼, 哪個字串)
    return re.sub(remove_chars, '', s)


# (暫時不需要)前處理ver2-粗體；取代
def str_replace(s):
    s = s.replace('**', '')
    s = s.replace('')
    return s

# 找subs在s中的位置，return list
def find_substr(s, subs):
    num = s.count(subs)
    start = 0
    end = len(s)

    pos_list = []

    print('num: ', num)
    while num>0:
        l_pos = s.find(subs, start, end)   # 從頭開始找在string中第1個出現子字串的位置，找不到會回傳-1
        r_pos = s.find(subs, l_pos+1, end)

        print('l_pos: ' + str(l_pos) + ', r_pos: ' + str(r_pos))
        num = num - 2

        if l_pos>0 and r_pos>0: # 有成對才會append
            pos_list.append(l_pos)
            pos_list.append(r_pos)

        start = r_pos+1

    return pos_list

# 前處理-刪除縣；以位置刪除子字串
def delete_subs(s, l_pos, r_pos, length=1):
    return s[:l_pos]+s[r_pos+length:]

# -------------------------
test_str = '4. 經過BERT的預訓練model後，得到**每個[CLS]標記的向量Ti**，做為**每個句子的特徵向量** 5. 做Fine-tuning(上圖下方再繼續疊)'

'''new_str = remove(test_str)
print(test_str_2)'''

#--------------------------
test_str_2 = '早安各位，我*已經不想**做專題**，我太難了*真的，~~我想放假~~嗚嗚嗚'

test_str_2_r = remove(test_str_2)
p_list = find_substr(test_str_2_r, '~~')
# print(p_list)

test_str_2_d = delete_subs(test_str_2_r, p_list[0], p_list[1], len('~~'))

print('test_str_2: %s\ntest_str_2_r: %s\ntest_str_2_d: %s'
      % (test_str_2, test_str_2_r, test_str_2_d))