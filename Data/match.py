class Match:
    def __init__(self, match_list):
        self.red = list()
        self.blue = list()
        for r in match_list:
            self.red.append(r) if r.alliance == 'Red' else self.blue.append(r)
