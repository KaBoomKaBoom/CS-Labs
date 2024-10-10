class AnalyzeFrequency():

    def __init__(self, data):
        self.data = data
    
    def get_frequency(self):
        frequency = {}
        for item in self.data:
            if item in "abcdefghijklmnopqrstuvwxyz":
                if item in frequency:
                    frequency[item] += 1
                else:
                    frequency[item] = 1
        return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

