import re

# 取得資料
def get_md():
    # 下面這行之後應該是從資料庫抓，要再改
    fileread =  open('./misproject_demo/text_sum/text_data/經濟學 CH22 微觀經濟學.md','r', encoding="utf-8")
    # char = fileread.read() # 逐字讀取
    lines = fileread.readlines() #逐行讀取
    lines = [i.strip() for i in lines if i.strip()!=''] # 濾除換行字元，並去除空白字串
    return lines

# 定義每句的level(目前header都可，其他level若需要可再加)
def define_level(md_list):
    md_level = []
    if md_list!=[]:
        # md_list_pre = md_preprocess(md_list)
        for sent in md_list:
            # 判斷是h幾
            if(sent[0]=='#'):
                count = 0
                while sent[count]=='#':
                    count+=1
                level = 'h'+str(count)
            else:
                level='not h'
            md_level.append(level)
    return md_level

# 輸入特定level名稱，會return所有該level的元素index及內容(如果想要去掉header的結果我再改)
def get_certain_level(data_list, level_name):
    start = 0
    level_index = []
    level_text = []
    while level_name in data_list[start:]:
        index = data_list.index(level_name, start)
        level_index.append(index)
        level_text.append(md_list[index])
        start = index+1
    return level_index, level_text

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

# 對list前處理
'''def md_preprocess(md_list):
    for sent in md_list:
        # 判斷是h幾
        count = 0
        while sent[count]=='#':
            count+=1
        level = 'h'+str(count)


    return md_list_pre'''


'''# -------------------------
test_str = '4. 經過BERT的預訓練model後，得到**每個[CLS]標記的向量Ti**，做為**每個句子的特徵向量** 5. 做Fine-tuning(上圖下方再繼續疊)'

new_str = remove(test_str)
print(test_str_2)

#--------------------------
test_str_2 = '早安各位，我*已經不想**做專題**，我太難了*真的，~~我想放假~~嗚嗚嗚'

test_str_2_r = remove(test_str_2)
p_list = find_substr(test_str_2_r, '~~')
# print(p_list)

test_str_2_d = delete_subs(test_str_2_r, p_list[0], p_list[1], len('~~'))

print('test_str_2: %s\ntest_str_2_r: %s\ntest_str_2_d: %s'
      % (test_str_2, test_str_2_r, test_str_2_d))
'''
# --------------------------
md_list = get_md()
# print(md_list)
# --------------------------
level_index, level_text = get_certain_level(define_level(md_list), 'h2')
print(level_index)
print(level_text)