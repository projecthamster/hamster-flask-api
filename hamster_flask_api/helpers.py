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

# [FIXME]
# Once LIB-228 has been closed, this should no longer be needed.
def category_to_json(category):
    return {
        'pk': category.pk,
        'name': category.name,
    }
