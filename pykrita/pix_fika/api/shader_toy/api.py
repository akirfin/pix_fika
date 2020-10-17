"""

Shadertoy API

Loading shaders & media from ShaderToy database.

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


_appkey = "NtHKWH"
_scheme = "https"
_netloc = "www.shadertoy.com"


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


def get_all_shaders():
    url = create_url(
            scheme=_scheme,
            netloc=_netloc,
            path="/api/v1/shaders",
            query=query_dct(key=_appkey))
    with urlopen(url) as f:
        response = json.load(f)
        return response["Results"]


def search_shaders(search, filter=None, order=None, start=None, count=None):
    if filter not in {None, "vr", "soundoutput", "soundinput", "webcam", "multipass", "musicstream"}:
        raise RuntimeError("Invalid filter. (did get: {filter})".format(**locals()))
    if order not in {None, "name", "love", "popular", "newest", "hot"}:
        raise RuntimeError("Invalid order. (did get: {order})".format(**locals()))
    if start is not None:
        start = int(start)
        if start < 0:
            raise RuntimeError("Invalid start. (did get: {start})".format(**locals()))
    if count is not None:
        count = int(count)
        if count < 0:
            raise RuntimeError("Invalid count. (did get: {count})".format(**locals()))
    query = query_dct(
            filter_=filter,
            sort_=order,
            from_=start,
            num=count,
            key=_appkey)
    url = create_url(
            scheme=_scheme,
            netloc=_netloc,
            path="/api/v1/shaders/query/{search}".format(search=search),
            query=query)
    with urlopen(url) as f:
        response = json.load(f)
        return response["Results"]


def get_shader(shader_id):
    url = create_url(
            scheme=_scheme,
            netloc=_netloc,
            path="/api/v1/shaders/{shader_id}".format(shader_id=shader_id),
            query=query_dct(key=_appkey))
    with urlopen(url) as f:
        response = json.load(f)
        return response


def get_thumbnail(shader_id):
    # url = create_url(
    #         scheme=_scheme,
    #         netloc=_netloc,
    #         path="/media/shaders/{shader_id}.jpg".format(shader_id=shader_id))
    url = create_url(
            scheme="http",
            netloc="reindernijhoff.net",
            path="/shadertoythumbs/{shader_id}.jpg".format(shader_id=shader_id))
    with urlopen(url) as f:
        response = json.load(f)
        return response


def get_media(media_src):
    url = create_url(
            scheme=_scheme,
            netloc=_netloc,
            path=media_src)
    with urlopen(url) as f:
        return f.read()
