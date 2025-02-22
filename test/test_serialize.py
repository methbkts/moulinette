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

from datetime import datetime as dt
from moulinette.interfaces import JSONExtendedEncoder


def test_json_extended_encoder(caplog):
    encoder = JSONExtendedEncoder()

    assert encoder.default({1, 2, 3}) == [1, 2, 3]

    assert encoder.default(dt(1917, 3, 8)) == "1917-03-08T00:00:00+00:00"

    assert encoder.default(None) == "None"
    for message in caplog.messages:
        assert "cannot properly encode in JSON" in message
