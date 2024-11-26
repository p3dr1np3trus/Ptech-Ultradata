class RoundList:
    def __init__(self, content: list):
        self.content = content

    def getvalue(self, value):
        if value <= len(self.content):
            return self.content[value]
        discard = value % (len(self.content))
        return self.content[discard]
