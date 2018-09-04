def search(STRING, PATTERN, flags=0):
    import re
    flags_table = {'i':re.I, 'I':re.I, 'm':re.M, 'M':re.M, 's':re.S, 'S':re.S, 'x':re.X, 'X':re.X, 'l':re.L, 'L':re.L, 'u':re.U, 'U':re.U} 
    if flags in flags_table:
        result = re.search(PATTERN, STRING, flags_table[flags])
    else:
        result = re.search(PATTERN, STRING)
    return result  
        
        
def substitute(STRING, PATTERN, REPLACEMENT, count=0, flags=0):
    import re
    if count == 'o' or count == 'O':
        count = 1
    else:
        count = 0
    flags_table = {'i':re.I, 'I':re.I, 'm':re.M, 'M':re.M, 's':re.S, 'S':re.S, 'x':re.X, 'X':re.X, 'l':re.L, 'L':re.L, 'u':re.U, 'U':re.U}  
    if flags in flags_table:
        result = re.sub(PATTERN, REPLACEMENT, STRING, count, flags_table[flags])
    else:
        result = re.sub(PATTERN, REPLACEMENT, STRING, count)
    return result
    

def translate(STRING, PATTERN, REPLACEMENT, DELETE=0, flags=0):
    import platform
    if list(str(platform.python_version()))[0] == '2':          #Python2 and Python3 are compatible
        from string import maketrans
        intab = PATTERN
        outtab = REPLACEMENT
        if flags == 'd' or flags == 'D':
            delete = DELETE
        else:
            delete = ''
        trantab = maketrans(intab, outtab)
        result = STRING.translate(trantab, delete)
    if list(str(platform.python_version()))[0] == '3':
        if flags == 'd' or flags == 'D':
            intab = PATTERN
            outtab = REPLACEMENT
            if flags == 'd' or flags == 'D':
                delete = DELETE
            else:
                delete = ''
            trantab = str.maketrans(intab, outtab, delete)
            result = STRING.translate(trantab)
    return result
    
"""
i re.I    取消大小写敏感性
I re.I 
m re.M    多行匹配，影响 ^ 和 $
M re.M
o count=1 替换只执行一次
O count=1
g count=0 替换所有匹配的字符串
G count=0
s re.S    使 . 匹配包括换行在内的所有字符
S re.S
x re.X    增加可读性，忽略空格和 # 后面的注释
X re.X
l re.L    表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
L re.L
u re.U    表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
U re.U
d	      删除所有指定字符
D
"""

#Some examples below

s = 'abcdefg1234567890'

p_m = 'a'

if search(s, p_m, 'i'):
    print('Yes!')
else:
    print('No!')

p_s = 'a'
r_s = '1'

s_s = substitute(s, p_s, r_s, 'g')
print(s_s)

p_t = 'abcd'
r_t = '1234'
d_t = 'efg'

s_t = translate(s, p_t, r_t, d_t, 'd')
print(s_t)