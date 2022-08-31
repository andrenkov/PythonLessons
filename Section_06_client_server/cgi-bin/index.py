# for web form
import cgi
import html

r = cgi.FieldStorage()
a = html.escape(r.getvalue("param-a", ""))
# "" is the default. html.escape() is to remove all spec chars to avoid script attack
b = html.escape(r.getvalue("param-b", ""))

result = 0
message = ""

try:
    result = float(a) + float(b)
    result = "<p> Sum is : " + str(result) + "</p>"
except ValueError:
    message = "<p style='color: red;'> You didn't enter numbers</p>"

# this index file has to have the Header and the Body separated by an empty line
print("Context-type: text/html; charset=utf-8")  # Header

print("")
# page body comes below
print("<html><head><title>Hello from my PY webpage</title>")
print("<link rel='icon' href='data:,'>")
print("</head>")

print("<body style='text-align: center'>")
print("<h1>Hi Vladimir</h1>")
print("<h2>My text</h2>")

# web form
print('''
<form name="form" style="margin: 0 auto; action="cgi-bin/index.py" method="post" >
    <h2>Sum two numbers</h2>
    ''' + message +
      '''
    <label>Number #1:</label>
    <input type="text" name="param-a" value="''' + a + '''" />
    <br />
    <br />
    <label>Number #2:</label>
    <input type="text" name="param-b" value="''' + b + '''" />
    <br />
    <br />
    <input type="submit" value="Calculate"></input>
    <br />
    ''' + str(result) +
      '''
</form>
''')

# print("a:", a)
# print("b:", b)

# closing tags
print("</html></body>")
