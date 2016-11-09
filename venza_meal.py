import requests
from lxml import html

webpage = 'http://studentskejedalne.sk'


class venzaException(Exception):
    pass


def main():
    response = requests.get(webpage)

    if not response.ok:
        raise venzaException("An error occured...")

    mealPath = "//div[@id='venzadiv']/table/tr/td/text()"
    meals = html.fromstring(response.content).xpath(mealPath)

    if ("Špagety" in i for i in meals):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
