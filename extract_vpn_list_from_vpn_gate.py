# This Python file uses the following encoding: utf-8
__author__ = 'VDTConstructor'
import re
import logging

from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)


def get_open_vpn_configure_url(vpn_gate_htm_file):
	html_doc = open(vpn_gate_htm_file, 'r')
	soup = BeautifulSoup(html_doc)
	logging.debug('the html is %s \n', soup.prettify())
	table = [t for t in soup.findAll("table")]
	logging.debug('the table length is %d\n', len(table))
	title_initialed = False
	title = {}
	all_vpn_list = []
	for t in table:
		row_list = [r for r in t.findAll('tr')]
		# print len(row_list)
		logging.debug('the row length is %d', len(row_list))
		for tr in row_list:
			td_list = [td for td in tr.findAll('td')]
			if len(td_list) == 10:
				logging.debug('the td length is %d', len(td_list))
				if not title_initialed:
					for td in td_list:
						title[td.get_text()] = len(title)
					title_initialed = True
				else:
					vpn = []
					for td in td_list:
						vpn.append(td)
						logging.debug('%s', td.get_text())
					all_vpn_list.append(vpn)
	for t in title:
		logging.info('%s', t)
	logging.info('%d', title[u'''国家 / 地区(物理位置)'''])
	logging.info('%d', title[u'''DDNS 主机名IP 地址(ISP 主机名)'''])
	logging.info('%d', title[u'''VPN 会话数运行时间累计用户数'''])
	logging.info('%d', title[u'''线路质量吞吐量和 Ping累积转移日志策略'''])
	logging.info('%d', title[u'''SSL-VPNWindows(合适的)'''])
	logging.info('%d', title[u'''L2TP/IPsecWindows, Mac,iPhone, Android无需 VPN 客户端'''])
	logging.info('%d', title[u'''OpenVPNWindows, Mac,iPhone, Android'''])
	logging.info('%d', title[u'''MS-SSTPWindows Vista,7, 8, RT无需 VPN 客户端'''])
	logging.info('%d', title[u'''志愿者操作员的名字(+ 操作员的消息)'''])
	logging.info('%d', title[u'''总分(质量)'''])

	open_vpn_list = []
	for vpn in all_vpn_list:
		if vpn[title[u'''OpenVPNWindows, Mac,iPhone, Android''']].a:
			logging.debug('%s', vpn[title[u'''OpenVPNWindows, Mac,iPhone, Android''']].a['href'])
			open_vpn_list.append(vpn[title[u'''OpenVPNWindows, Mac,iPhone, Android''']].a['href'])
	logging.info('all_vpn_list length %d', len(all_vpn_list))
	logging.info('open_vpn_list length %d', len(open_vpn_list))

	return open_vpn_list


def get_open_vpn_configure_files(open_vpn_url_file):
	html_doc = open(open_vpn_url_file, 'r')
	soup = BeautifulSoup(html_doc)
	href_list = [a['href'] for a in soup.findAll('a')]
	ovpn_re = re.compile(u'''.ovpn''')
	for hr in href_list:
		if ovpn_re.findall(hr):
			logging.info('%s', hr)


def main():
	vpn_gate_htm_file = 'VPNGate.htm'
	open_vpn_list = get_open_vpn_configure_url(vpn_gate_htm_file)
	for vpn in open_vpn_list:
		logging.debug(vpn)

	ovpn_file = 'ovpn.htm'
	get_open_vpn_configure_files(ovpn_file)


if __name__ == '__main__':
	main()

