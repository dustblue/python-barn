import requests


def to_num(w):
    n = ""
    for c in w:
        n = n + str(ord(c) - 97)
    return n


print("Hello")

url = "http://www.facade.com/legacy/amiinpi/?thenum="

choice = raw_input("** Search in PI **\nNumber (n) or Word (w) ? ")

if choice == 'n':
    num = raw_input("Enter your number : ")
    url = url + num
elif choice == 'w':
    word = raw_input("Enter your word : ")
    tm = to_num(word)
    print("Your word '{}' is encoded to {}".format(word, tm))
    url = url + tm
else:
    print("-_-")

r = requests.get(url=url)
data = r.content

response = "Not found in pi :("

for lines in data.split("\n"):
    if "I found" in lines:
        response = lines.strip()

print response.replace('<bold>', '')\
    .replace('</bold>', '')\
    .replace('<p>', '')
