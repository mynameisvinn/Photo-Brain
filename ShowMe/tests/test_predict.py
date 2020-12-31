from ShowMe import inference

from unittest import TestCase
import os

class TestPredict(TestCase):

    def test_predict(self):

        fname = "./ShowMe/images/1.jpg"
        assert(round(inference(fname), 2) == 3.65)

        fname = "./ShowMe/images/2.jpg"
        assert(round(inference(fname), 2) == 1.86)


