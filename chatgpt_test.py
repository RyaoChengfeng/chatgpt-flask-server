from main import chat, get_cf_shit
import unittest


class TestChat(unittest.TestCase):
    def test_chat(self):
        msg = "你是谁"
        ret = chat(msg)
        print(ret)
