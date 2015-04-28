__author__ = 'VDTConstructor'

import logging

from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)


def main():
	html_doc = open('VPNGate.htm', 'r')
	soup = BeautifulSoup(html_doc)
	logging.debug('the html is %s \n', soup.prettify())
	table = [t for t in soup.findAll("table")]
	logging.info('the table length is %d\n', len(table))
	for t in table:
		row_list = [r for r in t.findAll('tr')]
		# print len(row_list)
		logging.info('the row length is %d', len(row_list))
		for tr in row_list:
			td_list = [td for td in tr.findAll('td')]
			logging.info('the td length is %d', len(td_list))


if __name__ == '__main__':
	main()


