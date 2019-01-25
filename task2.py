import hashlib
from mydecorator import log_writer_with_path

@log_writer_with_path('C:\\Users\\semen\\Documents\\GitHub\\decorators\\')
def my_iter(file_path):
    with open(file_path) as f:
        for line in f:
            h = hashlib.md5(line.encode('utf-8'))
            yield h.hexdigest()


for item in my_iter('result_countries.txt'):
    print(item)
