from bs4 import BeautifulSoup
import csv


with open('baby1990.html') as f:
	soup = BeautifulSoup(f, 'lxml')

tr_list = soup.find_all('tr', attrs={ 'align':'right' })

td_list =[]

for tr in tr_list:
	td_list.append(tr.contents)

rank = []
male_name = []
female_name = []

for item in td_list:
	rank.append(item[0].get_text())
	male_name.append(item[1].get_text())
	female_name.append(item[2].get_text())

with open('baby1990.csv', 'w', newline='') as f:
	fieldnames = ['Ranking', 'Male Name', 'Female Name']
	thewrither = csv.DictWriter(f, fieldnames=fieldnames)

	thewrither.writeheader()
	for pos in range(len(rank)):
		thewrither.writerow({
			'Ranking': rank[pos],
			'Male Name': male_name[pos],
			'Female Name': female_name[pos]
			})