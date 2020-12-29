from ShowMe import inference

from unittest import TestCase
import os

class TestPredict(TestCase):

    def test_predict(self):

        fname = "./ShowMe/images/1.jpg"
        assert(inference(fname) == 3.650930881500244)

        fname = "./ShowMe/images/2.jpg"
        assert(inference(fname) == 1.8613183498382568)


