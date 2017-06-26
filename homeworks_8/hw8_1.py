class MyIterator(object):
    def __init__(self, filename):
        self.fd = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.fd.readline()
        if line != '':
            line = line.rstrip('\n')
            return line.upper()
        raise StopIteration
file_date = MyIterator('test.txt')

for item in file_date:
    print(item)