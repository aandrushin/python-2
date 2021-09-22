from bs4 import BeautifulSoup
import codecs

# index_path = "C:\\Users\\aandry28\\Downloads\\python-2\\lesson1\\blank"

# with codecs.open("%s\index.html" %index_path,"r","utf-8") as file:
#     src = file.read()
# print(src)

with open("blank/index.html") as file:
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

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)

# for item in find_all_spans_in_user_info:
    # print(item.text)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_links)

# all_a = soup.find_all("a")
# for item in all_a:
#     item_url = item.get("href")
#     item_text = item.text
#     print(f"{item_text}: {item_url}")

# .find_parent() .find_parents()

# post_div = soup.find(class_="post__text").find_parent("div","user__post")
# print(post_div)

post_divs = soup.find(class_="post__text").find_parents()
print(post_divs)