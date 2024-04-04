import assets
from assets.asset_package import getFullPath


def test_getFullPath():
    assert getFullPath([], "") == []
