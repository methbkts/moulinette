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

import pytest
import requests
import requests_mock

from moulinette.core import MoulinetteError
from moulinette.utils.network import download_json, download_text


def test_download(test_url):
    with requests_mock.Mocker() as mock:
        mock.register_uri("GET", test_url, text="some text")
        fetched_text = download_text(test_url)
    assert fetched_text == "some text"


def test_download_bad_url():
    with pytest.raises(MoulinetteError):
        download_text("Nowhere")


def test_download_404(test_url):
    with requests_mock.Mocker() as mock:
        mock.register_uri("GET", test_url, status_code=404)
        with pytest.raises(MoulinetteError):
            download_text(test_url)


def test_download_ssl_error(test_url):
    with requests_mock.Mocker() as mock:
        exception = requests.exceptions.SSLError
        mock.register_uri("GET", test_url, exc=exception)
        with pytest.raises(MoulinetteError):
            download_text(test_url)


def test_download_connection_error(test_url):
    with requests_mock.Mocker() as mock:
        exception = requests.exceptions.ConnectionError
        mock.register_uri("GET", test_url, exc=exception)
        with pytest.raises(MoulinetteError):
            download_text(test_url)


def test_download_timeout(test_url):
    with requests_mock.Mocker() as mock:
        exception = requests.exceptions.Timeout
        mock.register_uri("GET", test_url, exc=exception)
        with pytest.raises(MoulinetteError):
            download_text(test_url)


def test_download_json(test_url):
    with requests_mock.Mocker() as mock:
        mock.register_uri("GET", test_url, text='{"foo":"bar"}')
        fetched_json = download_json(test_url)
    assert "foo" in fetched_json.keys()
    assert fetched_json["foo"] == "bar"


def test_download_json_bad_json(test_url):
    with requests_mock.Mocker() as mock:
        mock.register_uri("GET", test_url, text="notjsonlol")
        with pytest.raises(MoulinetteError):
            download_json(test_url)
