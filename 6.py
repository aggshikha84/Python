import pickle
import urllib.request

res = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
#file = res.read()

#h = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

#print(file)

unload = pickle.load(res)

for i in unload:
    print("".join([k * v for k, v in i]))





      

