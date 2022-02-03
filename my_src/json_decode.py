
import json


# str = '''
# [
# {"title": "<title>\u6f2b\u753b\u30fb\u30b3\u30df\u30c3\u30af\u30e9\u30f3\u30ad\u30f3\u30b0 - honto</title>"},
# {"title": "<title>\u6f2b\u753b\u30fb\u30b3\u30df\u30c3\u30af\u96fb\u5b50\u66f8\u7c4d\u30e9\u30f3\u30ad\u30f3\u30b0 - honto</title>"}
# ]'''

# print(json.dumps(str, ensure_ascii=False))

df = ""
with open("scrapy_test.json") as f:
    # print(f.read())
    df = json.load(f)
    print(df)
    
    



# 【参考】raw文字列
def raw_string_study():

    s = 'a\tb\nA\tB'
    print(s)
    # a b
    # A B
    
    # raw文字列はR""とするだけ
    raw_s = r'a\tb\nA\tB'
    print(raw_s)
    # a\tb\nA\tB
    
    # repr関数でraw文字列に変換できる
    print(repr(s))
    # 'a\tb\nA\tB'
    
    # raw文字列はエスケープを自動で追加する
    print(raw_s == 'a\\tb\\nA\\tB')
    # True
    
    # 使用例　Windowsのパス
    path = 'C:\\Windows\\system32\\cmd.exe'
    rpath = r'C:\Windows\system32\cmd.exe'
    print(path == rpath)
    # True
    
# raw_string_study()      



