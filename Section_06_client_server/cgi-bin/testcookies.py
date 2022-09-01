# cookies are vars stored in the browser
# example will store site's colour schema in cookies

import cgi
# for getting cookies
import http.cookies, os

# create a dictionary or an array of colours
dicColours = {'red': 'Red', 'green': 'Green', 'blue': 'Blue'}

# create a Storage and set the default value ("white")
r = cgi.FieldStorage()
colour = r.getvalue('colour', 'white')
bgColour = 'background-color: {0};'

if dicColours.get(colour):  # set cookie !!!!!!!!!
    bgColour = bgColour.format(colour)
    print("Set-cookie: colour="+colour)
else:  # read cookies !!!!!!!!!
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))  # simple cookie object
    if cookie:
        colour = cookie.get("colour").value
        if dicColours.get(colour):
            bgColour = bgColour.format(colour)
    else:  # first run
        bgColour = bgColour.format(colour)

# create a webpage in cgi-bin testcookies.py
print("Context-type: text/html; charset=utf-8")  # Header

print("")
# page body comes below
print("<html><head><title>Hello from my PY webpage</title>")
print("</head>")

print("<body style='text-align: center; " + bgColour + "'>")
print("<h1>Hi Vladimir</h1>")
print("<h2>Test Cookies</h2>")

# Show colours using GET
for key in dicColours:
    print("<h2><a href='?colour=" + key + "'>" + dicColours[key] + "</a></h2>")
# this will crate a html:
# <h2><a href='?colour=red'>Red</a></h2>
# <h2><a href='?colour=green'>Green</a></h2>
# <h2><a href='?colour=blue'>Blue</a></h2>
print(colour)  # test

# closing tags
print("</html></body>")
