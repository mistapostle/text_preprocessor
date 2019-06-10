from bs4 import BeautifulSoup
import re 

htmfile = 'test.html'
html = open(htmfile, 'r', encoding='utf-8')
htmlpage = html.read()

soup = BeautifulSoup(htmlpage.strip(), 'html.parser')

[s.extract() for s in soup(['script', 'iframe', 'style' ,'a' ]) ]

print(soup.text)

s = soup.text.lower()

re_url =re.compile(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?' ,re.IGNORECASE)
s = re_url.sub('',s )

re_mail=re.compile(r'\w+@([0-9a-zA-Z]+[-0-9a-zA-Z]*)(\.[0-9a-zA-Z]+[-0-9a-zA-Z]*)+',re.IGNORECASE)
s = re_mail.sub('',s )
   

re_validchars=re.compile('[^a-z ]+')

s= re_validchars.sub('',s)
ss= [  x for x in re.compile('\\s+').split(s) if x  ] 
print( "after strip:" + s)
print(str(ss))
