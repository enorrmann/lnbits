# views_api.py is for you API endpoints that could be hit by another service

# add your dependencies here

# import json
# import requests

from flask import jsonify
from http import HTTPStatus

from lnbits.extensions.example import example_ext


# add your endpoints here


@example_ext.route("/api/v1/tools", methods=["GET"])
def api_example():
    """Try to add descriptions for others."""
    tools = [
        {
            "name": "Flask",
            "url": "https://flask.palletsprojects.com/",
            "language": "Python",
        },
        {
            "name": "Vue.js",
            "url": "https://vuejs.org/",
            "language": "JavaScript",
        },
        {
            "name": "Quasar Framework",
            "url": "https://quasar.dev/",
            "language": "JavaScript",
        },
    ]

    return jsonify(tools), HTTPStatus.OK
