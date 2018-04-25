tmpfp = 'russell.tmp'


fp = open(tmpfile, 'r')
#content = fp.read().split('\n')
#content = fp.read().strip(' \CR\LF')
content = fp.read().split('Russell Indexes.')
for elemnet in content:
    index = 0
    elemnet = content[index]
    test = elemnet.split('\n')
    print test