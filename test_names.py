from names import make_full_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name('william', 'osiakwan') == 'osiakwan william'


pytest.main(["-v", "--tb=line", "-rN", __file__])