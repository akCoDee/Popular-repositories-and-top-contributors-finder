import requests, json, sys
from operator import itemgetter
import socket

REMOTE_SERVER = "www.google.com"

def connected():
	try:
		host = socket.gethostbyname(REMOTE_SERVER)
		socket_connection = socket.create_connection((host, 80), 2)
		return True
	except:
		pass
	return False

def searchRepository( organization_name, n, m ):
	try:
		req = requests.get('https://api.github.com/search/repositories?q=user:'+organization_name+'&sort=forks&order=desc')
		if  req.ok:

			# JSON CONVERSION OF RESPONSE
			repositories = json.loads(req.content)

			# ACCESSING TOP 'N' REPOSITORY OF GIVEN ORGANIZATION
			for index,repository in enumerate( repositories['items'][ 0:int(n) ] ):
				print " ====================> Repository (" + str(index + 1) +")  " + str(repository['name']) + " | Fork Count => " + str(repository['forks_count'])
				
				print "------------------------------- Contributors ------------------------------- "
				# GET TOP 'M' CONTRIBUTORS OF THE REPOSITORY
				getTopContributors( repository['owner']['login'], repository['name'], m )
				
				print '''\n\n'''

		elif req.status_code == 404:
			print "Not Found!"
		
		else:
			print "Error (Status Code : ",req.status_code,") Response json -> ",json.loads(req.content)

	except Exception as e:
		print "Exception : ",str(e)

def getTopContributors( owner, repository, m ):
	try:
		# GET REPOSITORY STATS
		req = requests.get('https://api.github.com/repos/'+owner+'/'+repository+'/stats/contributors')
		if req.status_code == 200:

			# JSON CONVERSION OF RESPONSE
			contributors = json.loads(req.content)

			# SORT CONTRIBUTORS 
			contributors = sorted(contributors, key=itemgetter('total'), reverse=True)

			# PRINTING TOP 'M' CONTRIBUTORS IN A REPOSITORY
			for c_index in xrange( 0, int(m) ):
				print str(c_index+1),") Name : ",contributors[c_index]['author']['login'],"  Total Commits : ",contributors[c_index]['total']

		elif req.status_code == 202:
			print ".************ compiling statistics ************"
			print '''\n'''
			print '''
				Note -> Statistics compilaton is expensive operation, That's why server cached data. Unforutunatly given repository stats are not present in cache.
				a background job is also fired to start compiling these statistics. Give the job a few moments to complete and please try again later.
				  '''

		elif req.status_code == 404:
			print "Not Found."

		else:
			print "--------------------- Error (Status Code : " + str(req.status_code) + ") ----------------------------"
			print json.loads(req.content)
			print "------------------------------------------------------------------------------------------------------"

	except Exception as e:
		print "Exception : ",str(e)