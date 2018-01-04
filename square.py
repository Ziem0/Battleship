class Square:

    def __init__(self):
        self.is_marked = False
        self.is_hidden = False

    def mark(self):
        self.is_marked = True

    def hide(self):
        self.is_marked = True

    def __str__(self):
        #if not self.is_hidden:
        if self.is_marked:
            return "{}".format('▣')
        else:
            return "{}".format('▢')
        #else:
            #return "{}".format(" ")
