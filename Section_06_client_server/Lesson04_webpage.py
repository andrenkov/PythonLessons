import http.server

server_address = ('', 8080)
# create http listener
httpSrv = http.server.HTTPServer(server_address, http.server.CGIHTTPRequestHandler)
# run server
# httpSrv.serve_forever()  # test call http://127.0.0.1:8080/ just shows the dir of the Section_06 folder

# add cgi-bin folder with file index.py into the Section_06 to serve as index.html response
httpSrv.serve_forever()  # test call http://127.0.0.1:8080/cgi-bin/index.py show the webpage
