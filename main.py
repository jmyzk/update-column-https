import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'sheet_id' in request_json and 'email' in request_json:
        sheet_id = request_json['sheet_id']
        email = request_json['email']
    elif request_args and 'sheet_id' in request_args and 'email' in request_args:
        sheet_id = request_args['sheet_id']
        email = request_args['email']
    else:
        sheet_id = 'None'
        email = 'None'
    return 'sheet_id = {} email = {}'.format(sheet_id, email)
