from chalice import Chalice
import urllib.parse

app = Chalice(app_name='palindrome')


@app.route('/{word}')
def is_palindrome(word):

    normalizaed = urllib.parse.unquote(word)
    normalizaed = normalizaed.lower()
    normalizaed = normalizaed.replace(' ', '')
    length = len(normalizaed)
    middle = round((len(normalizaed)/2))
    start = normalizaed[0:middle]
    end = normalizaed[length-middle:length]
    reverse_end = end[::-1]
    return True if start == reverse_end else False


@app.route('/recursive/{word}')
def is_palindrome_recursive(word):
    normalizaed = urllib.parse.unquote(word)
    normalizaed = normalizaed.lower()
    normalizaed = normalizaed.replace(' ', '')
    length = len(normalizaed)
    if length == 1 or length == 0:
        return True
    normalizaed[1::]
    if normalizaed[0] == normalizaed[-1]:
        return is_palindrome_recursive(normalizaed[1:length-1])
    else:
        return False

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
