from urlparse import urlparse

def extractLex(urlToExt):
	lex={}
	result=urlparse(urlToExt)
	print(result)
	sumDomain=sumPath=maxPath=maxDomain=maxQuery=sumQuery=0

	netlocation=result.netloc.split(".")
	path=result.path.split("/")[1:]
	query=result.query.replace("."," ").replace("?"," ").replace("/"," ").replace("="," ").replace("-"," ").replace("_"," ").split(" ")
	query=filter(None,query)

	print ("query")
	print query
	lex['domainTC']=len(netlocation)
	lex['pathTC']=len(path)
	lex['queryTC']=len(query)

	for eachdomain in netlocation:
		sumDomain+=len(eachdomain)
		if(len(eachdomain)>maxDomain):
			maxDomain=len(eachdomain)
	for eachPath in path:
		sumPath+=len(eachPath)
		if(len(eachPath)>maxPath):
			maxPath=len(eachPath)
	for eachQuery in query:
		sumQuery+=len(eachQuery)
		if(len(eachQuery)>maxQuery):
			maxQuery=len(eachQuery)

	lex['domainTL']="{:.9f}".format(float(sumDomain)/lex['domainTC'])
	lex['pathTL']="{:.9f}".format(float(sumPath)/lex['pathTC'])	
	lex['queryTL']="{:.9f}".format(float(sumQuery)/lex['queryTC'])

	lex['domainML']=maxDomain
	lex['pathML']=maxPath
	lex['quryML']=maxQuery

	return lex

def main():
	lexdict=extractLex("https://www.google.co.in/search?site=&source=hp&q=what+is+worng&oq=what+is+worng&gs_l=hp.3...4582.9082.0.9471.14.14.0.0.0.0.417.1263.2-2j1j1.4.0....0...1c.1.64.hp..11.3.984.0.myGrkStHE7k")
	print(lexdict)

if __name__ == '__main__':
	main()
