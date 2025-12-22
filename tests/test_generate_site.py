sys.path.append('src/')
import generate_html
 

def test_generate_html():
    assert generate_html() == True
