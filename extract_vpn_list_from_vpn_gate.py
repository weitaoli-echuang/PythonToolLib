# This Python file uses the following encoding: utf-8
__author__ = 'VDTConstructor'
import re
import logging
import os
import subprocess

from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)


def delete_files(del_dir):
	filelist = os.listdir(del_dir)
	for f in filelist:
		filepath = os.path.join(del_dir, f)
		if os.path.isfile(filepath):
			os.remove(filepath)


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
						title[td.get_text().lower()] = len(title)
					title_initialed = True
				else:
					vpn = []
					for td in td_list:
						vpn.append(td)
						logging.debug('%s', td.get_text())
					all_vpn_list.append(vpn)
	for t in title:
		logging.info('%s', t)
	# logging.info('%d', title[u'''国家 / 地区(物理位置)'''])
	# logging.info('%d', title[u'''ddns 主机名ip 地址(isp 主机名)'''])
	# logging.info('%d', title[u'''vpn 会话数运行时间累计用户数'''])
	# logging.info('%d', title[u'''线路质量吞吐量和 ping累积转移日志策略'''])
	# logging.info('%d', title[u'''ssl-vpnwindows(合适的)'''])
	# logging.info('%d', title[u'''l2tp/ipsecwindows, mac,iphone, android无需 vpn 客户端'''])
	# logging.info('%d', title[u'''openvpnwindows, mac,iphone, android'''])
	# logging.info('%d', title[u'''ms-sstpwindows vista,7, 8, rt无需 vpn 客户端'''])
	# logging.info('%d', title[u'''志愿者操作员的名字(+ 操作员的消息)'''])
	# logging.info('%d', title[u'''总分(质量)'''])

	open_vpn_list = []
	for vpn in all_vpn_list:
		if vpn[title[u'''openvpnwindows, mac,iphone, android''']].a:
			logging.debug('%s', vpn[title[u'''openvpnwindows, mac,iphone, android''']].a['href'])
			open_vpn_list.append(vpn[title[u'''openvpnwindows, mac,iphone, android''']].a['href'])
	logging.info('all_vpn_list length %d', len(all_vpn_list))
	logging.info('open_vpn_list length %d', len(open_vpn_list))

	return open_vpn_list


def get_open_vpn_configure_files(open_vpn_url_file):
	# html_doc = open(open_vpn_url_file, 'r')
	# soup = BeautifulSoup(html_doc)
	soup = BeautifulSoup(open_vpn_url_file)
	logging.debug('the html is %s \n', soup.prettify())
	href_list = [a['href'] for a in soup.findAll('a') if a and a is not None]
	ovpn_re = re.compile(u'''.ovpn''')
	for hr in href_list:
		if ovpn_re.findall(hr):
			logging.info('%s', hr)


def get_fqdn(fqdn_text):
	paras = re.split('''&''', fqdn_text)
	dict_fqdn = {}
	for p in paras:
		p_s = re.split(u'''=''', p)
		if len(p_s) == 2 and p_s[1] != u'':
			dict_fqdn[p_s[0]] = p_s[1]
	return dict_fqdn


def form_fqdn(fqdn_dict):
	fqdn = 'sid=' + fqdn_dict['sid'] + '&tcp=1' + '&host=' + fqdn_dict['ip'] + '&port=' + fqdn_dict['tcp'] + '&hid=' + \
	       fqdn_dict['hid'] + '&/vpngate_' + fqdn_dict['ip'] + '_tcp_' + fqdn_dict['tcp'] + '.ovpn'
	return fqdn


def form_open_vpn_configure_file_download_address(vpn_url_text_list):
	open_vpn_tcp_configure_list = [get_fqdn(vpn) for vpn in vpn_url_text_list]
	return open_vpn_tcp_configure_list


def main():
	vpn_gate_download_web_prefix = 'http://112.173.79.56:45964/common/openvpn_download.aspx?'
	vpn_gate_htm_file = 'VPNGate.htm'
	open_vpn_list = get_open_vpn_configure_url(vpn_gate_htm_file)
	for vpn in open_vpn_list:
		logging.debug(vpn)

	configure_dir = 'vpn_config'
	download_file_list = 'configures_file'
	if os.path.isdir(configure_dir):
		delete_files(configure_dir)
	else:
		os.mkdir(configure_dir)
	os.chdir(configure_dir)

	logging.info('getting the download address of open vpn configure files')
	with open(download_file_list, 'w') as fp:
		open_vpn_tcp_configure_lis = form_open_vpn_configure_file_download_address(open_vpn_list)
		download_url_list = [vpn_gate_download_web_prefix + form_fqdn(p) for p in open_vpn_tcp_configure_lis if
		                     p['tcp'] != u'0']
		fp.write('\n'.join(download_url_list))
	logging.info('finish the download')
	logging.info('the tcp length is %d', len(download_url_list))
	subprocess.call(['ping', 'localhost'])


if __name__ == '__main__':
	main()

