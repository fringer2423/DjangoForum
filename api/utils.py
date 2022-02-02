class Sum:
    def __init__(self, params):
        self.val_1 = params.get("val_1")
        self.val_2 = params.get("val_2")

    def call(self):
        return {"result ": self.val_1 + self.val_2}
