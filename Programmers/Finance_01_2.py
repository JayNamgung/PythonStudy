from pandas_datareader import wb

wb.search('gdp.*capita.*const')

code = "NY.GDP.PCAP.PP.KD"
matches = wb.search('gdp.*capita.*const')
data = wb.download(indicator=code, country=['JPN', 'KOR'], start=2011, end=2018)
data = data.reset_index(drp=False)
sns.lineplot(x="year", y=code, hue="country", data=data)