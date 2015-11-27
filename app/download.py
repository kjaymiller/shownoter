from flask import make_response
def download(data):
    file = re.sub('<br>','\\n', data, re.M)
    response = make_response(file)
    response.headers['Content-Disposition'] = 'attachment; filename=results.txt'
    response.content_type = 'text/plain'
    return response
