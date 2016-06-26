import pandas as pd
import numpy as np

filename= "ps_w201606_allResultFileMd5NameTimeSize.txt"
demo="demo.txt"

def getDemo():
	outf=open(demo,"w")
	with open(filename) as f:
		for index,line in enumerate(f):
			if index>100000:
				break
			else:
				outf.write(line)
	return demo

def counter(group):
	result={}
	result["md5"]=group.iloc[0]["md5"]
	result["count_"]=len(group)

	result["size_"]=group.iloc[0]["size"]
	return pd.Series(result)
def statistic(group):
	data=group.groupby(["md5","size"]).apply(counter)

	all= np.sum(data.size_*data.count_)
	repeat=np.sum(data.size_ *(data.count_-1))
	return  repeat*1.0/all


def main(debug=False):
	if debug:
		getDemo()
		filename=demo

	start=r"2016\02\07 00:00:00"
	end=r"2016\02\07 24:00:00"

	df=pd.read_csv(filename,names=["md5","size","data"]).dropna()
	
	df=df[(df.data>=start) & (df.data<end)]

	df["period"]=df.data.str[11:13]
	print df.groupby("period").apply(statistic)
	
if __name__=="__main__":

	
	main(True)