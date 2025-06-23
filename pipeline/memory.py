class Memory:
    def __init__(self):
        self.history = []

    def add(self, stage: str, content: str):
        self.history.append({"stage": stage, "content": content})

    def get_all(self):
        return self.history

    def get_by_stage(self, stage: str):
        return [entry for entry in self.history if entry["stage"] == stage]

    def clear(self):
        self.history = []