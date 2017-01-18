#import the weezey template engine for the frame work
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader
#for tracking render time
import time



#this function take in a view's name and creates it
def renderPage(view,required):
	#Start by taking the ammount of time it take to render the page
	#print "Template engine running......."
	
	
	millis = (time.time())
	
	#set the path it searches for the template views 
	searchpath = ['Views']
	engine = Engine( loader=FileLoader(searchpath), extensions=[CoreExtension()])
	
	#choose the html template we want to use 
	template = engine.get_template( view + '.html')
	
	# render and save the html page (for now it all save to the same html file becasue im testing)
	Html_file= open("rendered.html","w")
	Html_file.write(template.render(required))
	Html_file.close()
	
	millis = time.time() - millis
	
	
	#give info about request
	print "Render time in seconds for " + view 
	print str(round(millis,4)) + "s"
	#print "Html render done for " + view
	print ""
	
	#return the rendered page to the controller
	return template.render(required)

	





