import os
import time
from flask import Flask, request, Response


RESPONSE_TIME = os.environ.get('RESPONSE_TIME', 1)

app = Flask(__name__)

@app.route('/mock', methods=['GET', 'POST'])
def receive_request():
    # Extracting method
    method = request.method
    
    # Extracting query parameters
    params = request.args.to_dict()
    
    # Extracting form data or JSON payload
    payload = request.get_json() if request.is_json else None
    
    # Printing the details
    print(f"Method: {method}")
    print(f"Params: {params}")
    print(f"Payload: {payload}")

    time.sleep(int(RESPONSE_TIME))
    
    return Response(status=201) if method == 'POST' else Response(status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

