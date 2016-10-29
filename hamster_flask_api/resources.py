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


from flask_restful import Resource, reqparse

from helpers import category_to_json

from hamster_lib import HamsterControl
import hamster_lib

config = {
    'store': 'sqlalchemy',
    'db_engine': 'sqlite',
    'db_path': '/tmp/hamster-flask-api.sqlite',
}


controller = HamsterControl(config)

category_parser = reqparse.RequestParser()
category_parser.add_argument('name', type=str, required=True, help="Name of the category.")


class CategoryList(Resource):
    def get(self):
        result = controller.categories.get_all()
        return [category_to_json(category) for category in result]

    def put(self):
        args = category_parser.parse_args(strict=True)
        category = hamster_lib.Category(args['name'])
        try:
            result = controller.categories.save(category)
        except ValueError as err:
            result = {'error': 'ValueError'}
        else:
            result = category_to_json(category)
        return result


class Category(Resource):
    def get(self, pk):
        try:
            result = controller.categories.get(pk)
        except KeyError:
            result = None
        else:
            # [FIXME]
            # Maybe it would be more maintainable to provide a dedicated
            # json encoder/serialization method.
            result = category_to_json(result)
        return result

    def delete(self, pk):
        # [FIXME]
        # Due to the fact that the manager method expects a full instance we
        # need create a mocked one. In effect only the pk will be used anyway.
        # This clearly is nonesence and is addressed by LIB-227.
        category = hamster_lib.Category('foobar', pk=pk)
        try:
            result = controller.categories.remove(category)
        except KeyError:
            result = {'error': "No such PK found."}
        return result

    def post(self, pk):
        args = category_parser.parse_args(strict=True)
        category = hamster_lib.Category(args['name'], pk=pk)
        try:
            result = controller.categories.save(category)
        except KeyError:
            result = {'error': 'No such PK found.'}
        except ValueError:
            result = {'error': 'Name already used.'}
        else:
            result = category_to_json(result)
        return result


class FactList(Resource):
    def get(self):
        return controller.facts.get_all()

class Fact(Resource):
    def get(self, pk):
        try:
            result = controller.facts.get(pk)
        except KeyError:
            result = None
        return result
