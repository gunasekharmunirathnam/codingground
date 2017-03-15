

def main(argv):
    host = argv[0]
    type = argv[1]
    val = argv[2]

    ping = subprocess.call(['python main.py %s %s %s'%(host,type,val)],stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell=True)
    out = ping.communicate()[0]
    output = str(out)
    print output
#main(argv)

