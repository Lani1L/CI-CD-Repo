import sys
sys.path.append('src/')
from generate_site import generate_html
 

def test_generate_html():
    assert generate_html() == True
