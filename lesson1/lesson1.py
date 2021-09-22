from bs4 import BeautifulSoup
import codecs

with codecs.open("blank/index.html","r","utf-8") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title

# print(title)
# print(title.text)
# print(title.string)

# page_h1 = soup.find("h1")
#print(page_h1)
# page_h1_all = soup.find_all("h1")
# print(page_h1_all)
# for item in page_h1_all:
    # print(item.text)

# username = soup.find("div", class_="user__name" )
# print(username.text.stip())

# username = soup.find_all(class_="user__name")
# print(username)

# username = soup.find ("div", {"class": "user__name", "id": "aaa"}).find("span").text
# print(username)

find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
print(find_all_spans_in_user_info)

for item in find_all_spans_in_user_info:
    print(item.text)