"""

GLSL Sandbox API

Loading shaders & media from GLSL Sandbox database.

"""

import json
from collections import OrderedDict as oDict

from urllib.parse import (
        urlparse,
        urlunparse,
        urlencode,
        ParseResult)

from urllib.request import (
        urlopen, )


_scheme = "https"
_netloc = "www.glslsandbox.com"


def query_dct(**key_value):
    """
    stript "_" from keys, and skip items value == None
    """
    return oDict([(k.strip("_"), v) for k, v in key_value.items() if v is not None])


def create_url(scheme="", netloc="", path="", params="", query=None, fragment=""):
    query = dict() if query is None else query
    return urlunparse(ParseResult(
            scheme=scheme,
            netloc=netloc,
            path=path,
            params=params,
            query=urlencode(query),
            fragment=fragment))


def get_shaders(page=None):
    """
    parse shaders from resulting html...
    """
    page = 0 if page is None else int(page)
    query = query_dct(
            page=page)
    url = create_url(
            scheme=_scheme,
            netloc=_netloc,
            path="/",
            query=query)
    with urlopen(url) as f:
        response = json.load(f)
        return response["Results"]


def get_shader(shader_id):
    url = create_url(
            scheme=_scheme,
            netloc=_netloc,
            path="/e#{shader_id}.{shader_version}".format(shader_id=shader_id))
    with urlopen(url) as f:
        response = json.load(f)
        return response


def get_thumbnail(shader_id):
    """
    needs thinking...
    """
    url = create_url(
            scheme="http",
            netloc="",
            path="{shader_id}.jpg".format(shader_id=shader_id))
    with urlopen(url) as f:
        response = json.load(f)
        return response
