#!/usr/bin/python3
""" This module is a index page """

from api.v1.views import app_views


@app_views.route('/status')
def statuspage():
    """method to return status"""
    sp = {"status": "OK"}
    return jsonify(sp)
