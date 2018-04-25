tmpfile = 'russell.tmp'


fp = open(tmpfile, 'r')
columCompany = []
columTicker = []
company = []
ticker = []

content = fp.read().split('\f')
for elemnet in content[:-2]:
    colums = [line for line in elemnet.split('\n\n') if (('Company' not in line) and ('Ticker' not in line) and ('Russell ' not in line) and ('As of ' not in line) and len(line)>1)]
    columCompany += [line for index, line in enumerate(colums) if index % 2 == 0]
    columTicker += [line for index, line in enumerate(colums) if index % 2 != 0]

for item in columCompany:
    company += item.split('\n')

for item in columTicker:
    ticker +=item.split('\n')

company = [item.strip(' ') for item in company]
ticker = [item.strip(' ') for item in ticker]
print ticker

#instrum = dict(zip(ticker, company))
#print instrum
