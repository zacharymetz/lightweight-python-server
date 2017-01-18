# this is the MAP file for the application and will contain the routes
# to the actions and views

#import the script that renders the html page
from renderHtml import renderPage

#import actions


#this functions contains all the "maps and will have the index map as an example"

def mapRequest(request,variables=""):
	
	# example of a map that maps path /index to index.html
	if "/index" == request or "/" == request:
		return renderPage("index",variables)
	
	elif "/test" == request:
		return renderPage("variables_test",variables)
		
	else:
		return renderPage("error",variables)
