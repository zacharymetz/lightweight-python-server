#Bit server start and requesr handiling file

# there will be a peice of updated code that get parameteters from the path
from urlparse import urlparse

#Import the map file
from map import mapRequest
#import the scripts needed to run the http server request
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler



# this function gets the parameters from a get request
# it returns a dictionary with the parameters names and their data
def getParams(path):
	if path.find('?') != -1:
		query = urlparse(path).query
		print query
		return dict(qc.split("=") for qc in query.split("&"))
		
	return ""

def withoutParams(path):
	if path.find('?') != -1:
		return path[0:(path.find('?'))]
	else:
		return path

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		
		
		# this if statement sees if the index of the project has been
		# requested by asking for the root
		if self.path == "/":
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			
			#get the right rought from the map file and render the page
			self.wfile.write(mapRequest(withoutParams(self.path),getParams(self.path)))
		
		#this control statement chatches if the browser requests for the favicon 
		# and since the project does not have on yet we will ignore this request
		# other wise this is the normal request
		elif self.path != "/favicon.ico":
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			
			#get the right template and send the right parameters to the par requester
			self.wfile.write(mapRequest(withoutParams(self.path),getParams(self.path)))
	def do_PUT(self):
		print "----- SOMETHING WAS PUT!! ------"
		print self.headers
		length = int(self.headers['Content-Length'])
		content = self.rfile.read(length)
		self.send_response(200)
		print content
httpd = SocketServer.TCPServer(("10.0.1.5", 80), MyHandler)
sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()


