import threading

class sszpThread:
    def __init__(self, func):
        self.sszpthread = threading.Thread(target=func)
    def start(self):
        self.sszpthread.start()
    def join(self):
        self.sszpthread.join()
