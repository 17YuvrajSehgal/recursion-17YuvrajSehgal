import reverseString as rv

def test_reverse():
    string = "2P08 Intro to Python and Data Structures"
    excepted_string = "serutcurtS ataD dna nohtyP ot ortnI 80P2"
    rev_string = rv.reverse(string)
    assert excepted_string == rev_string