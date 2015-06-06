import sys
class progress_bar:
    def __init__(self, total_count):
        self.total_count=total_count*1.0
    def draw(self, value):
        sys.stdout.write('\rFinish: %f%%'%(100.0*value/self.total_count))
        sys.stdout.flush()
        if value>=self.total_count:
            sys.stdout.write('\n')
            sys.stdout.flush()
