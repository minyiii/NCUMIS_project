from textrank4zh import TextRank4Keyword, TextRank4Sentence
import os

print('路徑: ',os.getcwd())

# 開啟檔案
with open('./loginSystem/text_sum/text_data/textrank4zh_data.txt','r', encoding='utf-8') as f:  #打开读取test.txt
    test_text = f.read()

# 抓取關鍵詞
def get_key_words(text, num=5):
    tr4w = TextRank4Keyword()
    tr4w.analyze(text, lower=True)
    key_words = tr4w.get_keywords(num)
    return [item.word for item in key_words]

# 抓取關鍵詞組
def get_key_phrases(text, num=20, win=2):
    tr4w = TextRank4Keyword()
    tr4w.analyze(text, lower=True, window=win)
    key_phrases = tr4w.get_keyphrases(keywords_num=num, min_occur_num=2)
    return key_phrases

# 抓取關鍵句，參數：文字、要最好的?句
def get_key_sent(text, sent_num=1):
    tr4s = TextRank4Sentence()
    tr4s.analyze(text = text, lower = True, source = 'all_filters')
    sent=[]
    for item in tr4s.get_key_sentences(num=sent_num):
        sent.append(item.sentence)
        # print(item.index, item.weight, item.sentence)
    return sent

get_key_words(test_text)
get_key_phrases(test_text)
get_key_sent(test_text)