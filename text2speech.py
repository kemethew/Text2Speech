from chardet.universaldetector import UniversalDetector


file_name = 'sample file.txt'
def detect_encoding(file_name):
    detector = UniversalDetector()
    document = open(file_name, 'rb')
    for line in document:
        detector.feed(line)
    print(detector.result)
    detector.close()
   


print(detect_encoding(file_name))

# file = open(file_name, 'r')
# print(file.readlines()[3])