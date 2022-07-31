import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
appleStock = []
appleDates = []
appleProductdates = []
appleProducts = {"2007-06-29": "iPhone 1", "2008-07-11": "iPhone 3G", "2009-06-19": "iPhone 3GS", "2010-04-30": "iPad 1", "2010-06-24": "iPhone 4", "2011-03-11": "iPad 2", "2011-10-14": "iPhone 4S", "2012-03-16": "iPad 3", "2012-09-21": "iPhone 5", "2012-11-02": "iPad Mini & 4", "2013-09-20": "iPhone 5C & 5S", "2013-11-01": "iPad Air", "2013-11-12": "iPad Mini 2", "2014-09-19": "iPhone 6", "2014-10-22": "iPad Air 2 & Mini 3", "2015-09-09": "iPad Mini 4", "2015-09-25": "iPhone 6S", "2015-11-11": "iPad Pro 12.9 2015", "2016-03-31": "iPhone SE & iPad Pro 9.7 2016", "2016-09-07": "iPad Air 2", "2016-09-16": "iPhone 7", "2017-03-24": "iPad 2017", "2017-06-05": "iPad Pro 12.9 2017 & iPad Pro 10.5", "2017-09-22": "iPhone 8", "2017-11-03": "iPhone X", "2018-03-27": "iPad 2018", "2018-09-21": "iPhone XS", "2018-10-26": "iPhone XR", "2018-11-07": "iPad Pro 11 & 12.9 2018", "2019-03-18": "iPad Air 3 & Mini 5"}
appleProductsonly = []
for i in appleProducts:
  appleProductsonly.append(appleProducts[i])
microsoftStock = []
amazonStock = []
googleStock = []
facebookStock = []
f = open("big_five_stocks.csv", encoding = "utf-8")
reader = csv.DictReader(f)
for row in reader:
  if row["name"] == "AAPL":
    appleStock.append(float(row["high"]))
    appleDates.append(row["date"])
  elif row["name"] == "MSFT":
    microsoftStock.append(float(row["high"]))
  elif row["name"] == "GOOGL":
    googleStock.append(float(row["high"]))
  elif row["name"] == "AMZN":
    amazonStock.append(float(row["high"]))
  elif row["name"] == "FB":
    facebookStock.append(float(row["high"]))
f.close()
for i in range(0, (len(appleDates) - 1)):
  if appleDates[i] in appleProducts:
    appleProductdates.append(appleStock[i + 5] - appleStock[i])
appleLength = range(len(appleStock))
microsoftLength = range(len(microsoftStock))
googleLength = range(len(googleStock))
amazonLength = range(len(amazonStock))
facebookLength = range(len(facebookStock))
date = pd.date_range(start = appleDates[0], end = appleDates[len(appleDates) - 1], freq = "B")
graph = sns.lineplot(appleLength, appleStock)
graph.set(title = "Apple's Evolution", xlabel = "Length", ylabel = "Daily High")
plt.savefig("appleline.png")
plt.clf()
graph = sns.lineplot(microsoftLength, microsoftStock)
graph.set(title = "Microsoft's Evolution", xlabel = "Length", ylabel = "Daily High")
plt.savefig("microsoftline.png")
plt.clf()
graph = sns.lineplot(googleLength, googleStock)
graph.set(title = "Google's Evolution", xlabel = "Length", ylabel = "Daily High")
plt.savefig("googleline.png")
plt.clf()
graph = sns.lineplot(amazonLength, amazonStock)
graph.set(title = "Amazon's Evolution", xlabel = "Length", ylabel = "Daily High")
plt.savefig("amazonline.png")
plt.clf()
graph = sns.lineplot(facebookLength, facebookStock)
graph.set(title = "Facebook's Evolution", xlabel = "Length", ylabel = "Daily High")
plt.savefig("facebookline.png")
plt.clf()
graph = sns.lineplot(appleLength, appleStock)
graph = sns.lineplot(microsoftLength, microsoftStock)
graph = sns.lineplot(googleLength, googleStock)
graph = sns.lineplot(amazonLength, amazonStock)
graph = sns.lineplot(facebookLength, facebookStock)
graph.set(title = "Stocks of Companies", xlabel = "Length", ylabel = "Daily High")
plt.savefig("lines.png")
plt.clf()
graph = sns.barplot(appleProductdates, appleProductsonly)
graph.set(title = "Apple Stock after Products", xlabel = "Stock Comparison after 1 Week", ylabel = "Apple Products")
plt.savefig("applebar.png")
plt.clf()