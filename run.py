from flask import Flask, request
from app import controller

app = Flask(__name__)

app.config['ENV'] = 'Development'
app.config['DEBUG'] = True


@app.route('/<path:string_route>', methods=['GET', 'POST'])
def get_route(string_route):
    return controller.get_response_for_route(string_route, request)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
