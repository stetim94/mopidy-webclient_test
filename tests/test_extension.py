from __future__ import unicode_literals

from mopidy_webclient_test import Extension, frontend as frontend_lib


def test_get_default_config():
    ext = Extension()

    config = ext.get_default_config()

    assert '[webclient_test]' in config
    assert 'enabled = true' in config


def test_get_config_schema():
    ext = Extension()

    schema = ext.get_config_schema()

    # TODO Test the content of your config schema
    #assert 'username' in schema
    #assert 'password' in schema


# TODO Write more tests
