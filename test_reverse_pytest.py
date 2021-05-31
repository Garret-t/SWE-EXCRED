from reverse import reverse_sent


class TestReverse():
    def test_correct(self):
        assert reverse_sent("My name is Garrett") == "Garrett is name My"

    def test_single(self):
        assert reverse_sent("Name") == "Name"
    
    def test_space(self):
        assert reverse_sent(" ") == " "
    
    def test_empty(self):
        assert reverse_sent("") == ""