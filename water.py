class Water:
    
    def __init__(self):
        self.is_marked = False
    
    def mark(self):
        self.is_marked = True
    
    def __str__(self):
        if self.is_marked: 
            return "{}".format('🌊')
        else:
            return "{}".format(' ')
