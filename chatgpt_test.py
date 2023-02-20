import chatgpt
import unittest


class TestChat(unittest.TestCase):
    def test_chat(self):
        msg = "你是谁"
        ret = chatgpt.chat(msg)
        print(ret)
