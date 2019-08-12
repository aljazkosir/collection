import pytest

from ansible_collections.mynamespace.collection.plugins.modules import collection


class TestCollection:
    def test_module(self):
        assert True is True