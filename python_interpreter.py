import sys

try:
    f = open(str(sys.argv[1]), 'r')
    data = f.read()
    f.close()
    data.split('\n')
    for line in data:
        exec(line)
except:
    try:
        exec(sys.argv[1])
    except:
        print('failed')
