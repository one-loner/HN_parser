
from bs4 import BeautifulSoup
import requests
result=""
searchrequest=input("Enter word or phrase for search  [github]: ")
n=input("Enter depth of parsing (Integer number 0 or more) [0]: ")
if searchrequest == "":
  searchrequest="github"
for i in range(int(n)):
  try:
    if i==0:
       url = "https://news.ycombinator.com/"
    else:
       url = "https://news.ycombinator.com/news?p=" + str(i)
    request = requests.get(url)
  except:
    contine
  soup = BeautifulSoup(request.text, "html.parser")

  teme = soup.find_all("td", class_="title")


  for temes in teme:
    if temes is not None and searchrequest in str(temes):
     sublink = temes.find_all("a", class_="titlelink")
     tem=str(temes.text)
     tem=tem.replace('\n','')
     subl=str(sublink)
     subl=subl.replace('[<a class="titlelink" href="','')
     subl=subl.replace('[]','')
     s=subl.split('">')
     result=result+"\n"+tem+"\n"+str(s[0])+"\n"+"================================="
print(result)
print("\n")
print("Enter name of file to saving the results, then press Enter.")
outfile = input("Or just press Enter to exit without saving the results: ")
if outfile=="":
   quit()
else:
   result=result+"\n"
   f=open(outfile,'w')
   f.write(result)
   f.close
   quit()
