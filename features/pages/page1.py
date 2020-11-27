from selenium import webdriver


class page1():

    instance = None
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = page1()
        return cls.instance

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test(self,number):
        self.driver.get('https://xxxlutz.at')
        print(number)


page1 = page1.get_instance()
