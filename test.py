class MyExcepiton(Exception):

    def __init__(self, info):
        super(MyExcepiton, self).__init__()
        self.info = info

    def __str__(self):
        return self.info

if __name__ == '__main__':
    try:
        raise MyExcepiton('test my exception')
    except MyExcepiton as e:
        print(e)
