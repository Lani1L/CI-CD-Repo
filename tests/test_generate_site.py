import sys
sys.path.append('src/')
import generate_site.generate_html
 

def test_generate_html():
    assert generate_html() == True
