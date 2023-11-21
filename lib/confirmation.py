class Confirmation:
    def __init__(self, phone_num, message):
        self.phone_num = phone_num
        self.message = message

    def send_message(self, phone_num, message):
        # add here API from `twilio-python` package after we learn more about API's, for now it's mocked
        return True