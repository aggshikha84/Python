# url = http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
import urllib.request
baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
dynamicNum = "12345"
for i in range(400):
    url = baseurl+dynamicNum
    response = urllib.request.urlopen(url)
    file = response.read().decode("utf-8")
    dynamicNum = (file.split(" ")[-1])
    if dynamicNum.isalpha():
        print(dynamicNum)
  
