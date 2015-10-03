from flask import make_response

def download(download_file):
    result = ''
    for line in download_file:
        result += line + '\n'

    response = make_response(result)
    response.headers['Content-Disposition'] = 'attachment; filename=results.txt'
    response.content_type = 'text/plain'
    return response