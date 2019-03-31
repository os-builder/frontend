from flask import Flask, send_file, send_from_directory
from flask_graphql import GraphQLView
from .schema import schema


app = Flask('b4rti')


@app.route('/')
def send_index():
    return send_file('./dist/index.html')

@app.route('/favicon.ico')
def send_favicon():
    return send_file('./dist/favicon.ico')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./dist/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./dist/css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('./dist/img', path)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)
