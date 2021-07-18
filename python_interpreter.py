import sys
try:
    f = open(str(sys.argv[1]), 'r')
    data = f.read()
    f.close()
    exec(data)
except:
    try:
        exec(sys.argv[1])
    except:
        print('failed')
