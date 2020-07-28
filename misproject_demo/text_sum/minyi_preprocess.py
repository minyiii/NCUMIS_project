import re

# 取得資料
def get_md():
    # 下面這行之後應該是從資料庫抓，要再改
    fileread =  open('./misproject_demo/text_sum/text_data/經濟學 CH22 微觀經濟學.md','r', encoding="utf-8")
    lines = fileread.readlines() #逐行讀取
    # lines = [i.strip() for i in lines if i.strip()!=''] # 濾除換行字元，並去除空白字串
    lines_=[]
    for i in lines:
        i_ = pre_remove(i)
        if i_.strip()!='':
            lines_.append(i_.strip())
    return lines_

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
            elif re.match(r'(\d+)\.\s', sent):
                level = 'li'
            else :
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

# 前處理-斜、粗體、冒號、>；移除特殊char
def pre_remove(s):
    remove_chars = r'\*' # 適用於斜體(*)、粗體(**)
    # re.sub(哪些char要被換, 換成甚麼, 哪個字串)
    s_ = re.sub(remove_chars, '', s)
    s_ = s_.replace(':::', '')
    s_ = s_.replace('>','')

    pos = find_substr(s_, '~~')
    if pos:
        s_ = delete_subs(s_, pos[0], pos[1], len('~~'))

    return s_.strip()

# 找subs在s中的位置，return list
def find_substr(s, subs):
    num = s.count(subs)
    start = 0
    end = len(s)

    pos_list = []

    # print('num: ', num)
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

# 把header和list的數字都移除，因為之後要放進json檔裡
def remove_title(s):
    rem_chars = r'\#' # 移除井字號
    # re.sub(哪些char要被換, 換成甚麼, 哪個字串)
    s_ = re.sub(rem_chars, '', s)
    rem_chars_2 = r'(\d+)\.\s' # 移除'1. '、'2. '
    s_ = re.sub(rem_chars_2, '', s_)

    return s_.strip()

#--------------------------
'''test_str_2 = '早安各位，我*已經不想**做專題**，我太難了*真的，~~我想放假~~嗚嗚嗚'

test_str_2_r = remove(test_str_2)
p_list = find_substr(test_str_2_r, '~~')
# print(p_list)

test_str_2_d = delete_subs(test_str_2_r, p_list[0], p_list[1], len('~~'))

print('test_str_2: %s\ntest_str_2_r: %s\ntest_str_2_d: %s'
      % (test_str_2, test_str_2_r, test_str_2_d))
'''
# --------------------------
md_list = get_md()
print(md_list)
# --------------------------
print('-----------------------------------------')
level_index, level_text = get_certain_level(define_level(md_list), 'li')
print(level_index)
print(level_text)
# --------------------------

print('-----------------------------------------')
for sent in md_list:
    print(remove_title(sent))

# --------------------------
'''meta_name = 'MIS G6'
meta_author = 'author@gmail.com'
meta_ver = '0.2'

json_dict={
    'meta':{
        "name":meta_name,
        "author":meta_author,
        "version":meta_ver
    },
    'format':'node_tree',
    'data':''
}'''