from message_class import Message

TEST_MESSAGE = Message("Test message.", "test")
TEST_MESSAGE.add_text("This is test text 1.")
TEST_MESSAGE.add_image("./messages/test_message/1.png")
TEST_MESSAGE.add_text("This is text 2.")
TEST_MESSAGE.add_image("./messages/test_message/2.png")
