class TestCase:
    def __init__(self, raw: str, expected, label: str = ""):
        self.raw = raw
        self.expected = expected
        self.label = label or raw