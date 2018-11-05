from bs4 import BeautifulSoup

class Rich():
    """Rich class for forbes"""

    def __init__(self, name, worth, rank,age, source, country):
        self.name = name
        self.worth = worth
        self.rank = rank
        self.age = age
        self.source = source
        self.country = country

    def __str__(self):
        return str(self.rank + " -- " + self.name + " " + self.worth)


with open('forbes.html', 'r') as _file:
    file = _file.read()
    soup = BeautifulSoup(file, "html")
    peoples = soup.findAll("tr", class_="data")

    richs = list()
    for people in peoples:
        colums = people.findAll("td")
        counter = 0
        for colum in colums:
            if counter == 0:
                pass
            elif counter == 1:
                rank = colum.text.replace("#","")
            elif counter == 2:
                name = colum.text
            elif counter == 3:
                worth = colum.text
            elif counter == 4:
                age = colum.text
            elif counter == 5:
                source = [text.strip() for text in colum.text.split(",")]
            elif counter == 6:
                country = colum.text
            counter += 1
        richs.append(Rich(name, worth, rank, age, source, country))

    for rich in richs:
        print(rich)