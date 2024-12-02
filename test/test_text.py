#!/usr/bin/env python3
#
# Copyright (c) 2024 YunoHost Contributors
#
# This file is part of YunoHost (see https://yunohost.org)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from moulinette.utils.text import search, searchf, prependlines, random_ascii


def test_search():
    assert search("a", "a a a") == ["a", "a", "a"]
    assert search("a", "a a a", count=2) == ["a", "a"]
    assert search("a", "a a a", count=-1) == "a"
    assert not search("a", "c c d")


def test_searchf(test_file):
    assert searchf("bar", str(test_file)) == ["bar"]
    assert not searchf("baz", str(test_file))


def test_prependlines():
    assert prependlines("abc\nedf\nghi", "XXX") == "XXXabc\nXXXedf\nXXXghi"
    assert prependlines("", "XXX") == "XXX"


def test_random_ascii():
    assert isinstance(random_ascii(length=2), str)
    assert len(random_ascii(length=10)) == 10
