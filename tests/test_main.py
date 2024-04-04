import os
from assets.asset_package import get_root_path


os.chdir("../.")  # sets chdir to root


def test_getFullPath():
    assert get_root_path([], "") == []
