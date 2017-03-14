from functions import * 

# CHECK IF CLIENT MACHINE HAS ACTIVE INTERNET CONNECTION OR NOT
if not connected():
	print "Program requires internet connection. Please connect to internet and try again later."
	sys.exit()
	
print '''
                ============================================ INFORMATION ================================================
                        
            . Program supports command line argument E.g. - python file_name.py user/organization_name n m .(Where n is most
              forked n number of repositories from user/organization and m is top m number of contributor of the repository)

            	Note - Program can also be run with zero inputs. Default input would be organization name=google, n=4, m=2.

            .	Contributor list may or may not be present at first. Computing repository statistics is an expensive operation,
            	so github server try to return cached data whenever possible. If the data hasn't been cached when you query a 
            	repository's statistics you'll receive a 202 response(Accepted) which means a background job is also fired to 
              start compiling these statistics. Give the job a few moments to complete, and then submit the request again. 
              If the job has completed, that request will receive a 200 response(Success) with the statistics in the response 
              body.

                =========================================================================================================
      '''

organization = "google"
n,m = 4,2
argument_length = len(sys.argv)


try:
  if argument_length == 2:
  	organization = str(sys.argv[1])

  elif argument_length == 3:
  	organization = str(sys.argv[1])
  	n = int(sys.argv[2])

  elif argument_length >= 4:
  	organization = str(sys.argv[1])	
  	n   = int(sys.argv[2])
  	m   = int(sys.argv[3])

except Exception as e:
  print "Exception : ",str(e)
  print "Invalid inputs! Runnign with default input values( google, 4, 2 )."
  print '''\n\n'''

searchRepository( organization, n, m )
