# -*- coding: utf-8 -*-

# This file is part of 'hamster-flask-api'.
#
# 'hamster-flask-api' is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# 'hamster-flask-api' is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with 'hamster-flask-api'.  If not, see <http://www.gnu.org/licenses/>.
#
# (c) Eric Goller, contact@ninjaduck.solutions

from __future__ import absolute_import

from flask import Flask
from flask_restful import Api


from . import resources


def get_app():
    app = Flask(__name__)
    api = add_routes(app)
    return app


def add_routes(app):
    api = Api(app)
    api.add_resource(resources.Category, '/v1/categories/<int:pk>')
    api.add_resource(resources.CategoryList, '/v1/categories/')
    api.add_resource(resources.Fact, '/v1/facts/<int:pk>')
    api.add_resource(resources.FactList, '/v1/facts')
    return api


def run():
    app = get_app()
    app.run(debug=True)
