#gunicorn -w 4 --reload -b localhost:5005 "app.testApp:app"
#gunicorn --reload -c "./gunicorn.conf.py" "app.testApp:app" >>> when gunicorn config file is in a different directory
#gunicorn --reload "app.testApp:app" >>> when gunicorn config file is in the same directory

def app(environ, start_response):
    """Simplest possible application object"""
    data = b'Hello, World! I am ankesh\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])