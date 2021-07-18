import requests
from bs4 import BeautifulSoup
import json

class Player():
	def __init__(self, ID, language = 'Español'):
		self.languages = ('English', 'Español', 'Português', 'Português', 'Deutsche', 'Français', 'Italiano', 'Русский', '简体中文', '繁體中文', '日本語', '한국어', 'Indonesia', 'Suomi', 'Türkçe')
		self.dict_languages = {'English': 'en', 'Español': 'es', 'Português': 'br', 'Deutsche': 'de', 'Français': 'fr', 'Italiano': 'it', 'Русский': 'ru', '简体中文': 'zh', '繁體中文': 'tw', '日本語': 'ja', '한국어': 'ko', 'Indonesia': 'id', 'Suomi': 'fi', 'Türkçe': 'tr'}
		self.quality_level = {'1': 'common', '2': 'rare', '3': 'epic', '4': 'legendary'}
		self.countrys = ('Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Ascension Island', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Canary Islands', 'Cape Verde', 'Caribbean Netherlands', 'Cayman Islands', 'Central African Republic', 'Ceuta and Melilla', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo (DRC)', 'Congo (Republic)', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Côte d´Ivoire', 'Denmark', 'Diego Garcia', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard &amp; McDonald Islands', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia (FYROM)', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'North Korea', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Réunion', 'Saint Barthélemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre and Miquelon', 'Samoa', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Vincent &amp; Grenadines', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'São Tomé and Príncipe', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tristan da Cunha', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'U.S. Outlying Islands', 'U.S. Virgin Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe', 'Åland Islands')
		self.ID = ID

		self.select_language = self.dict_languages.get(language)
		if self.select_language == None:
			self.select_language = self.dict_languages.get('Español')

	def top(self, Type = 'current-season', Location = False, Level = False, Limit = 50):
		if isinstance(Limit, int) == False or Limit > 1000:
			raise Exception('Limit must be less than 1000')

		types = ('current-season', 'all-time', 'most-donations', 'most-cards-won', 'most-war-wins', 'most-war-cards', 'most-matches')
		countrys = {'Afghanistan': '57000007', 'Albania': '57000009', 'Algeria': '57000010', 'American Samoa': '57000011', 'Andorra': '57000012', 'Angola': '57000013', 'Anguilla': '57000014', 'Antarctica': '57000015', 'Antigua and Barbuda': '57000016', 'Argentina': '57000017', 'Armenia': '57000018', 'Aruba': '57000019', 'Ascension Island': '57000020', 'Australia': '57000021', 'Austria': '57000022', 'Azerbaijan': '57000023', 'Bahamas': '57000024', 'Bahrain': '57000025', 'Bangladesh': '57000026', 'Barbados': '57000027', 'Belarus': '57000028', 'Belgium': '57000029', 'Belize': '57000030', 'Benin': '57000031', 'Bermuda': '57000032', 'Bhutan': '57000033', 'Bolivia': '57000034', 'Bosnia and Herzegovina': '57000035', 'Botswana': '57000036', 'Bouvet Island': '57000037', 'Brazil': '57000038', 'British Indian Ocean Territory': '57000039', 'British Virgin Islands': '57000040', 'Brunei': '57000041', 'Bulgaria': '57000042', 'Burkina Faso': '57000043', 'Burundi': '57000044', 'Cambodia': '57000045', 'Cameroon': '57000046', 'Canada': '57000047', 'Canary Islands': '57000048', 'Cape Verde': '57000049', 'Caribbean Netherlands': '57000050', 'Cayman Islands': '57000051', 'Central African Republic': '57000052', 'Ceuta and Melilla': '57000053', 'Chad': '57000054', 'Chile': '57000055', 'China': '57000056', 'Christmas Island': '57000057', 'Cocos (Keeling) Islands': '57000058', 'Colombia': '57000059', 'Comoros': '57000060', 'Congo (DRC)': '57000061', 'Congo (Republic)': '57000062', 'Cook Islands': '57000063', 'Costa Rica': '57000064', 'Croatia': '57000066', 'Cuba': '57000067', 'Curaçao': '57000068', 'Cyprus': '57000069', 'Czech Republic': '57000070', 'Côte d´Ivoire': '57000065', 'Denmark': '57000071', 'Diego Garcia': '57000072', 'Djibouti': '57000073', 'Dominica': '57000074', 'Dominican Republic': '57000075', 'Ecuador': '57000076', 'Egypt': '57000077', 'El Salvador': '57000078', 'Equatorial Guinea': '57000079', 'Eritrea': '57000080', 'Estonia': '57000081', 'Ethiopia': '57000082', 'Falkland Islands': '57000083', 'Faroe Islands': '57000084', 'Fiji': '57000085', 'Finland': '57000086', 'France': '57000087', 'French Guiana': '57000088', 'French Polynesia': '57000089', 'French Southern Territories': '57000090', 'Gabon': '57000091', 'Gambia': '57000092', 'Georgia': '57000093', 'Germany': '57000094', 'Ghana': '57000095', 'Gibraltar': '57000096', 'Greece': '57000097', 'Greenland': '57000098', 'Grenada': '57000099', 'Guadeloupe': '57000100', 'Guam': '57000101', 'Guatemala': '57000102', 'Guernsey': '57000103', 'Guinea': '57000104', 'Guinea-Bissau': '57000105', 'Guyana': '57000106', 'Haiti': '57000107', 'Heard &amp; McDonald Islands': '57000108', 'Honduras': '57000109', 'Hong Kong': '57000110', 'Hungary': '57000111', 'Iceland': '57000112', 'India': '57000113', 'Indonesia': '57000114', 'Iran': '57000115', 'Iraq': '57000116', 'Ireland': '57000117', 'Isle of Man': '57000118', 'Israel': '57000119', 'Italy': '57000120', 'Jamaica': '57000121', 'Japan': '57000122', 'Jersey': '57000123', 'Jordan': '57000124', 'Kazakhstan': '57000125', 'Kenya': '57000126', 'Kiribati': '57000127', 'Kosovo': '57000128', 'Kuwait': '57000129', 'Kyrgyzstan': '57000130', 'Laos': '57000131', 'Latvia': '57000132', 'Lebanon': '57000133', 'Lesotho': '57000134', 'Liberia': '57000135', 'Libya': '57000136', 'Liechtenstein': '57000137', 'Lithuania': '57000138', 'Luxembourg': '57000139', 'Macau': '57000140', 'Macedonia (FYROM)': '57000141', 'Madagascar': '57000142', 'Malawi': '57000143', 'Malaysia': '57000144', 'Maldives': '57000145', 'Mali': '57000146', 'Malta': '57000147', 'Marshall Islands': '57000148', 'Martinique': '57000149', 'Mauritania': '57000150', 'Mauritius': '57000151', 'Mayotte': '57000152', 'Mexico': '57000153', 'Micronesia': '57000154', 'Moldova': '57000155', 'Monaco': '57000156', 'Mongolia': '57000157', 'Montenegro': '57000158', 'Montserrat': '57000159', 'Morocco': '57000160', 'Mozambique': '57000161', 'Myanmar (Burma)': '57000162', 'Namibia': '57000163', 'Nauru': '57000164', 'Nepal': '57000165', 'Netherlands': '57000166', 'New Caledonia': '57000167', 'New Zealand': '57000168', 'Nicaragua': '57000169', 'Niger': '57000170', 'Nigeria': '57000171', 'Niue': '57000172', 'Norfolk Island': '57000173', 'North Korea': '57000174', 'Northern Mariana Islands': '57000175', 'Norway': '57000176', 'Oman': '57000177', 'Pakistan': '57000178', 'Palau': '57000179', 'Palestine': '57000180', 'Panama': '57000181', 'Papua New Guinea': '57000182', 'Paraguay': '57000183', 'Peru': '57000184', 'Philippines': '57000185', 'Pitcairn Islands': '57000186', 'Poland': '57000187', 'Portugal': '57000188', 'Puerto Rico': '57000189', 'Qatar': '57000190', 'Romania': '57000192', 'Russia': '57000193', 'Rwanda': '57000194', 'Réunion': '57000191', 'Saint Barthélemy': '57000195', 'Saint Helena': '57000196', 'Saint Kitts and Nevis': '57000197', 'Saint Lucia': '57000198', 'Saint Martin': '57000199', 'Saint Pierre and Miquelon': '57000200', 'Samoa': '57000201', 'San Marino': '57000202', 'Saudi Arabia': '57000204', 'Senegal': '57000205', 'Serbia': '57000206', 'Seychelles': '57000207', 'Sierra Leone': '57000208', 'Singapore': '57000209', 'Sint Maarten': '57000210', 'Slovakia': '57000211', 'Slovenia': '57000212', 'Solomon Islands': '57000213', 'Somalia': '57000214', 'South Africa': '57000215', 'South Korea': '57000216', 'South Sudan': '57000217', 'Spain': '57000218', 'Sri Lanka': '57000219', 'St. Vincent &amp; Grenadines': '57000220', 'Sudan': '57000221', 'Suriname': '57000222', 'Svalbard and Jan Mayen': '57000223', 'Swaziland': '57000224', 'Sweden': '57000225', 'Switzerland': '57000226', 'Syria': '57000227', 'São Tomé and Príncipe': '57000203', 'Taiwan': '57000228', 'Tajikistan': '57000229', 'Tanzania': '57000230', 'Thailand': '57000231', 'Timor-Leste': '57000232', 'Togo': '57000233', 'Tokelau': '57000234', 'Tonga': '57000235', 'Trinidad and Tobago': '57000236', 'Tristan da Cunha': '57000237', 'Tunisia': '57000238', 'Turkey': '57000239', 'Turkmenistan': '57000240', 'Turks and Caicos Islands': '57000241', 'Tuvalu': '57000242', 'U.S. Outlying Islands': '57000243', 'U.S. Virgin Islands': '57000244', 'Uganda': '57000245', 'Ukraine': '57000246', 'United Arab Emirates': '57000247', 'United Kingdom': '57000248', 'United States': '57000249', 'Uruguay': '57000250', 'Uzbekistan': '57000251', 'Vanuatu': '57000252', 'Vatican City': '57000253', 'Venezuela': '57000254', 'Vietnam': '57000255', 'Wallis and Futuna': '57000256', 'Western Sahara': '57000257', 'Yemen': '57000258', 'Zambia': '57000259', 'Zimbabwe': '57000260', 'Åland Islands': '57000008'}

		if Type not in types:
			raise Exception("Type = 'current-season', 'all-time', 'most-donations', 'most-cards-won', 'most-war-wins', 'most-war-cards' or 'most-matches'")

		params = {
			'type': Type,
		}

		if Location:
			country_select = countrys.get(Location)
			if country_select:
				params['locationId'] = country_select
			else:
				raise Exception('view all countrys availibles with .countrys')

		if Level:
			params['level'] = str(Level)

		page = 1
		players = []

		while True:
			params['page'] = str(page)
			response = requests.get('https://statsroyale.com/{}/top/players'.format(self.select_language), params = params)
			soup = BeautifulSoup(response.content, 'html.parser')
			
			for player in soup.find_all('div', class_ = 'topPlayers__rowContainer'):
				if len(players) == Limit:
					return players

				ID = player.find('a', class_ = 'topPlayers__name').get('href').split('/')[-1]
				name = player.find('a', class_ = 'topPlayers__name').get_text()
				league = player.find('div', class_ = 'topPlayers__leagueContainer').find('div').get('class')[0].split('_')[-1]
		
				try:
					clan_ID = player.find('a', class_ = 'topPlayers__badge').get('href').split('/')[-1]
					clan_name = player.find('a', class_ = 'topPlayers__badge').get_text().strip()
					clan_badge = player.find('a', class_ = 'topPlayers__badge').find('img').get('src')
				except:
					clan_ID, clan_name, clan_badge = None, None, None

				players.append({'ID': ID, 'name': name, 'league': league, 'clan_ID': clan_ID, 'clan_name': clan_name, 'clan_badge': clan_badge})
				cups = player.find('div', class_ = 'topPlayers__cup')
				donations = player.find('div', class_ = 'topPlayers__cards')
				battles = player.find('div', class_ = 'topPlayers__battles')

				if cups:
					players[-1]['cups'] = cups.get_text()
				elif donations:
					players[-1]['donations'] = donations.get_Text()
				else:
					players[-1]['battles'] = battles.get_Text()
			page += 1

	def information(self):
		response = requests.get('https://statsroyale.com/{}/profile/'.format(self.select_language) + self.ID)
		soup = BeautifulSoup(response.content, 'html.parser')

		header = None
		Stats = []
		for column in soup.find('div', class_ = 'statistics__wrapper').findChildren('div', recursive = False):
			for divisor in column.findChildren('div', recursive = False):
				if 'statistics__subheader' in divisor.get('class'):
					header = divisor.get_text()
				else:
					Stats.append({divisor.find('div', class_ = 'ui__mediumText').get_text():divisor.find('div', class_ = 'statistics__metricCounter').get_text().strip(), 'parent': header})
		
		Last_Refresh = soup.find('div', class_ = 'refresh__time').get_text()
		Name = soup.find('span', class_ = 'profileHeader__nameCaption').get_text()
		Level = soup.find('span', class_ = 'profileHeader__userLevel').get_text()
		
		try:
			Clan_ID = soup.find('a', class_ = 'profileHeader__userClan').get('href').split('/')[-1]
			Clan_Name = soup.find('a', class_ = 'profileHeader__userClan').get_text().strip()
			Clan_Badge = soup.find('img', class_ = 'profileHeader__clanBadge').get('src')
		except:
			Clan_ID = None
			Clan_Name = None
			Clan_Badge = None

		Current_deck = [card.get('src') for card in soup.find('div', class_ = 'profile__currentDeckList').find_all('img')]
		Next_Chests = [{'chest': chest.get('class')[0].split('chests__')[1], 'lack': chest.find('span', class_ = 'chests__counter').get_text()} for chest in soup.find('div', class_ = 'chests__queue').findChildren('div', recursive = False)]
		
		return {'name': Name, 'stats': Stats, 'level': Level, 'clan_ID': Clan_ID, 'clan_name': Clan_Name, 'clan_badge': Clan_Badge, 'current_deck': Current_deck, 'upcomming_chests': Next_Chests, 'last_refresh': Last_Refresh}

	def battles(self):
		response = requests.get('https://statsroyale.com/{}/profile/{}/battles'.format(self.select_language, self.ID))
		soup = BeautifulSoup(response.content, 'html.parser')

		battles = []
		for battle in soup.find('div', class_ = 'profile__replays').findChildren('div', recursive = False):
			results = battle.find('div', class_ = 'replayLayout__resultValue').get_text().split(' - ')
			mode = battle.get('data-type')
			time = battle.find('div', class_ = 'replayLayout__footer__timestamp').get_text()
			players = []

			if len(battle.find_all('div', class_ = 'replayLayout__player')) != 2:
				results = results*3

			for player in battle.find_all('div', class_ = 'replayLayout__player'):
				point = results.pop(0)
				ID = player.find('a', class_ = 'replayPlayer__name').get('href').split('/')[-1]
				name = player.find('a', class_ = 'replayPlayer__name').get_text()
				cups = player.find('div', class_ = 'replayPlayer__trophiesMetric').get_text().strip()
				clan_ID = player.find('a', class_ = 'replayPlayer__badgeText').get('href').split('/')[-1]
				clan_name = player.find('a', class_ = 'replayPlayer__badgeText').get_text()
				clan_badge = player.find('img', class_ = 'replayPlayer__badgeImage').get('src')
				hitpoints = {x.find('div', class_ = 'ui__smallText').get_text(): x.find('div', class_ = 'ui__smallStrong').get_text() for x in player.find_all('div', class_ = 'replayPlayer__towerMetricHitsCell')}
				hitpoints['total'] = player.find('div', class_ = 'replayPlayer__towerIconContainer').find_all('div', class_ = 'ui__smallStrong')[-1].get_text()
				deck = [{'link' : card.get('href'), 'image': card.find('img').get('src'), 'level': card.get_text().strip()} for card in player.find('div', class_ = 'replayPlayer__decklist').find_all('a')]
				elixir_deck = player.find('div', class_ = 'replayPlayer__elixirCaption').get_text()
				link_deck = player.find('a', class_ = 'copyButton').get('href')
				players.append({'point': point, 'ID': ID, 'name': name, 'cups': cups, 'clan_ID': clan_ID, 'clan_name': clan_name, 'clan_badge': clan_badge, 'hitpoints': hitpoints, 'deck': deck, 'elixir_deck': elixir_deck, 'link_deck': link_deck})
			battles.append({'mode': mode, 'time': time, 'players': players})
		return battles

	def decks(self):
		response = requests.get('https://statsroyale.com/{}/profile/{}/decks'.format(self.select_language, self.ID))
		soup = BeautifulSoup(response.content, 'html.parser')
		list_decks = []

		for deck in soup.find_all('div', class_ = 'decks__container'):
			cards = [{'link_deck': card.get('href'), 'image': card.find('img').get('src')} for card in deck.find('div', class_ = 'decks__decklist').find_all('a')]
			stats = [{stat.find('div', class_ = 'decks__metricName').get_text(): stat.find('div', class_ = 'decks__metricValue').get_text()} for stat in deck.find_all('div', class_ = 'decks__metric')]
			time  = deck.find('div', class_ = 'decks__footer').find('div', class_ = 'decks__meta').get_text().split(':')[-1]
			link_deck = deck.find('div', class_ = 'decks__footer').find('a').get('href')
			
			list_decks.append({'cards': cards, 'stats': stats, 'time': time, 'link_deck': link_deck})
		return list_decks

	def cards(self):
		response = requests.get('https://statsroyale.com/{}/profile/{}/cards'.format(self.select_language, self.ID))
		soup = BeautifulSoup(response.content, 'html.parser')
		list_cards = []

		upgrade_cost = {cost.get_text(): cost.get('value') for cost in soup.find('select', id = 'cards-summary-upgrade').find_all('option')}
		account_value = soup.find('div', class_ = 'cardsSummary__cost').get_text().strip().split(' ')[0]
		cards = [{'name': card.find('div', class_ = 'cards__tooltip').get_text(), 'rarity': self.quality_level.get(card.get('data-rarity')[0]),'elixir': card.get('data-elixir'), 'level': card.find('span', class_ = 'profileCards__level').get_text().split(';')[-1], 'link': card.find('a').get('href'), 'image': card.find('img').get('src'), 'amount': card.find('div', class_ = 'profileCards__meter__numbers').get_text()} for card in soup.find_all('div', class_ = 'profileCards__card') if card.get('data-level')!= '0']
		
		return {'upgrade_cost': upgrade_cost, 'account_value': account_value, 'cards': cards}

	def refresh(self):
		response = requests.get('https://statsroyale.com/profile/{}/refresh'.format(self.ID))
		Json = json.loads(response.text)
		return Json['success']


class Clan():
	def __init__(self, ID, language = 'Español'):
		self.ID = ID
		self.languages = ('English', 'Español', 'Português', 'Português', 'Deutsche', 'Français', 'Italiano', 'Русский', '简体中文', '繁體中文', '日本語', '한국어', 'Indonesia', 'Suomi', 'Türkçe')
		self.dict_languages = {'English': 'en', 'Español': 'es', 'Português': 'br', 'Deutsche': 'de', 'Français': 'fr', 'Italiano': 'it', 'Русский': 'ru', '简体中文': 'zh', '繁體中文': 'tw', '日本語': 'ja', '한국어': 'ko', 'Indonesia': 'id', 'Suomi': 'fi', 'Türkçe': 'tr'}
		self.countrys = ('Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Ascension Island', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Canary Islands', 'Cape Verde', 'Caribbean Netherlands', 'Cayman Islands', 'Central African Republic', 'Ceuta and Melilla', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo (DRC)', 'Congo (Republic)', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Côte d´Ivoire', 'Denmark', 'Diego Garcia', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard &amp; McDonald Islands', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia (FYROM)', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'North Korea', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Réunion', 'Saint Barthélemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre and Miquelon', 'Samoa', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Vincent &amp; Grenadines', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'São Tomé and Príncipe', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tristan da Cunha', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'U.S. Outlying Islands', 'U.S. Virgin Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe', 'Åland Islands')

		self.select_language = self.dict_languages.get(language)
		if self.select_language == None:
			self.select_language = self.dict_languages.get('Español')

	def search(self, name):
		params = {'name': name}
		response = requests.get('https://statsroyale.com/{}/clan/search/'.format(self.select_language), params = params)
		soup = BeautifulSoup(response.content, 'html.parser')
		clans = []

		for clan in soup.find_all('a', class_ = 'clanSearch__cell'):
			ID = clan.get('href').split('/')[-1]
			Nombre = clan.find('div', class_ = 'ui__blueLink').get_text()
			Badge = clan.find('img', class_ = 'clanSearch__badge').get('src')
			Cups = clan.find('div', class_ = 'clanSearch__cup').get_text()
			Members = clan.find('span', class_ = 'clanSearch__full').get_text()
			Country = clan.find_all('div', class_ = 'clanSearch__row')[-1].get_text().strip()
			Country_Flag = clan.find('img', class_ = 'clanSearch__flag')

			if Country_Flag:
				Country_Flag = Country_Flag.get('src')
			else:
				Country_Flag = None

			clans.append({'ID': ID, 'Nombre': Nombre, 'Badge': Badge, 'Cups': Cups, 'Members': Members, 'Country': Country, 'Country_Flag': Country_Flag})
		return clans
	
	def refresh(self):
		response = requests.get('https://statsroyale.com/clan/{}/refresh'.format(self.ID))
		Json = json.loads(response.text)
		return Json['success']

	def information(self):
		response = requests.get('https://statsroyale.com/{}/clan/{}'.format(self.select_language, self.ID))
		soup = BeautifulSoup(response.content, 'html.parser')
		Name = soup.find('div', class_ = 'clan__clanName').get_text().strip()
		Description = soup.find('div', class_ = 'clan__clanInfo').find('div', class_ = 'ui__mediumText').get_text().strip()
		Badge = soup.find('img', class_ = 'clan__clanWarBadge').get('src')
		Last_Refresh = soup.find('div', id = 'refresh-clan').find('div', class_ = 'clan__tip ui__smallText ui__greyText').get_text().strip()
		Stats = {Stat.find('div', class_ = 'ui__mediumText').get_text():Stat.find('div', class_ = 'ui__headerMedium').get_text() for Stat in soup.find('div', class_ = 'clan__statistics').findChildren('div', recursive = False)}
		Players = [{'ID': player.find('a', class_ = 'ui__blueLink').get('href').split('/')[-1], 'name': player.find('a', class_ = 'ui__blueLink').get_text(), 'cups': player.find('div', class_ = 'clan__cup').get_text(), 'level': player.find('span', class_ = 'clan__playerLevel').get_text(), 'donations': player.find('div', class_ = 'clan__donation').get_text(), 'last_seen': player.find('div', class_ = 'clan__lastSeenInner').get_text(), 'Role': player.find('div', class_ = 'clan__memberRoleInner').get_text()} for player in soup.find('div', class_ = 'clan__table').find_all('div', class_ = 'clan__rowContainer')]
		return {'Name': Name, 'Description': Description, 'Badge': Badge, 'Last Refresh': Last_Refresh, 'Stats': Stats, 'Players': Players}

	def top(self, Type, Location = False):
		types = ('clans', 'clanwars', 'supercellcreators')
		countrys = {'Afghanistan': '57000007', 'Albania': '57000009', 'Algeria': '57000010', 'American Samoa': '57000011', 'Andorra': '57000012', 'Angola': '57000013', 'Anguilla': '57000014', 'Antarctica': '57000015', 'Antigua and Barbuda': '57000016', 'Argentina': '57000017', 'Armenia': '57000018', 'Aruba': '57000019', 'Ascension Island': '57000020', 'Australia': '57000021', 'Austria': '57000022', 'Azerbaijan': '57000023', 'Bahamas': '57000024', 'Bahrain': '57000025', 'Bangladesh': '57000026', 'Barbados': '57000027', 'Belarus': '57000028', 'Belgium': '57000029', 'Belize': '57000030', 'Benin': '57000031', 'Bermuda': '57000032', 'Bhutan': '57000033', 'Bolivia': '57000034', 'Bosnia and Herzegovina': '57000035', 'Botswana': '57000036', 'Bouvet Island': '57000037', 'Brazil': '57000038', 'British Indian Ocean Territory': '57000039', 'British Virgin Islands': '57000040', 'Brunei': '57000041', 'Bulgaria': '57000042', 'Burkina Faso': '57000043', 'Burundi': '57000044', 'Cambodia': '57000045', 'Cameroon': '57000046', 'Canada': '57000047', 'Canary Islands': '57000048', 'Cape Verde': '57000049', 'Caribbean Netherlands': '57000050', 'Cayman Islands': '57000051', 'Central African Republic': '57000052', 'Ceuta and Melilla': '57000053', 'Chad': '57000054', 'Chile': '57000055', 'China': '57000056', 'Christmas Island': '57000057', 'Cocos (Keeling) Islands': '57000058', 'Colombia': '57000059', 'Comoros': '57000060', 'Congo (DRC)': '57000061', 'Congo (Republic)': '57000062', 'Cook Islands': '57000063', 'Costa Rica': '57000064', 'Croatia': '57000066', 'Cuba': '57000067', 'Curaçao': '57000068', 'Cyprus': '57000069', 'Czech Republic': '57000070', 'Côte d´Ivoire': '57000065', 'Denmark': '57000071', 'Diego Garcia': '57000072', 'Djibouti': '57000073', 'Dominica': '57000074', 'Dominican Republic': '57000075', 'Ecuador': '57000076', 'Egypt': '57000077', 'El Salvador': '57000078', 'Equatorial Guinea': '57000079', 'Eritrea': '57000080', 'Estonia': '57000081', 'Ethiopia': '57000082', 'Falkland Islands': '57000083', 'Faroe Islands': '57000084', 'Fiji': '57000085', 'Finland': '57000086', 'France': '57000087', 'French Guiana': '57000088', 'French Polynesia': '57000089', 'French Southern Territories': '57000090', 'Gabon': '57000091', 'Gambia': '57000092', 'Georgia': '57000093', 'Germany': '57000094', 'Ghana': '57000095', 'Gibraltar': '57000096', 'Greece': '57000097', 'Greenland': '57000098', 'Grenada': '57000099', 'Guadeloupe': '57000100', 'Guam': '57000101', 'Guatemala': '57000102', 'Guernsey': '57000103', 'Guinea': '57000104', 'Guinea-Bissau': '57000105', 'Guyana': '57000106', 'Haiti': '57000107', 'Heard &amp; McDonald Islands': '57000108', 'Honduras': '57000109', 'Hong Kong': '57000110', 'Hungary': '57000111', 'Iceland': '57000112', 'India': '57000113', 'Indonesia': '57000114', 'Iran': '57000115', 'Iraq': '57000116', 'Ireland': '57000117', 'Isle of Man': '57000118', 'Israel': '57000119', 'Italy': '57000120', 'Jamaica': '57000121', 'Japan': '57000122', 'Jersey': '57000123', 'Jordan': '57000124', 'Kazakhstan': '57000125', 'Kenya': '57000126', 'Kiribati': '57000127', 'Kosovo': '57000128', 'Kuwait': '57000129', 'Kyrgyzstan': '57000130', 'Laos': '57000131', 'Latvia': '57000132', 'Lebanon': '57000133', 'Lesotho': '57000134', 'Liberia': '57000135', 'Libya': '57000136', 'Liechtenstein': '57000137', 'Lithuania': '57000138', 'Luxembourg': '57000139', 'Macau': '57000140', 'Macedonia (FYROM)': '57000141', 'Madagascar': '57000142', 'Malawi': '57000143', 'Malaysia': '57000144', 'Maldives': '57000145', 'Mali': '57000146', 'Malta': '57000147', 'Marshall Islands': '57000148', 'Martinique': '57000149', 'Mauritania': '57000150', 'Mauritius': '57000151', 'Mayotte': '57000152', 'Mexico': '57000153', 'Micronesia': '57000154', 'Moldova': '57000155', 'Monaco': '57000156', 'Mongolia': '57000157', 'Montenegro': '57000158', 'Montserrat': '57000159', 'Morocco': '57000160', 'Mozambique': '57000161', 'Myanmar (Burma)': '57000162', 'Namibia': '57000163', 'Nauru': '57000164', 'Nepal': '57000165', 'Netherlands': '57000166', 'New Caledonia': '57000167', 'New Zealand': '57000168', 'Nicaragua': '57000169', 'Niger': '57000170', 'Nigeria': '57000171', 'Niue': '57000172', 'Norfolk Island': '57000173', 'North Korea': '57000174', 'Northern Mariana Islands': '57000175', 'Norway': '57000176', 'Oman': '57000177', 'Pakistan': '57000178', 'Palau': '57000179', 'Palestine': '57000180', 'Panama': '57000181', 'Papua New Guinea': '57000182', 'Paraguay': '57000183', 'Peru': '57000184', 'Philippines': '57000185', 'Pitcairn Islands': '57000186', 'Poland': '57000187', 'Portugal': '57000188', 'Puerto Rico': '57000189', 'Qatar': '57000190', 'Romania': '57000192', 'Russia': '57000193', 'Rwanda': '57000194', 'Réunion': '57000191', 'Saint Barthélemy': '57000195', 'Saint Helena': '57000196', 'Saint Kitts and Nevis': '57000197', 'Saint Lucia': '57000198', 'Saint Martin': '57000199', 'Saint Pierre and Miquelon': '57000200', 'Samoa': '57000201', 'San Marino': '57000202', 'Saudi Arabia': '57000204', 'Senegal': '57000205', 'Serbia': '57000206', 'Seychelles': '57000207', 'Sierra Leone': '57000208', 'Singapore': '57000209', 'Sint Maarten': '57000210', 'Slovakia': '57000211', 'Slovenia': '57000212', 'Solomon Islands': '57000213', 'Somalia': '57000214', 'South Africa': '57000215', 'South Korea': '57000216', 'South Sudan': '57000217', 'Spain': '57000218', 'Sri Lanka': '57000219', 'St. Vincent &amp; Grenadines': '57000220', 'Sudan': '57000221', 'Suriname': '57000222', 'Svalbard and Jan Mayen': '57000223', 'Swaziland': '57000224', 'Sweden': '57000225', 'Switzerland': '57000226', 'Syria': '57000227', 'São Tomé and Príncipe': '57000203', 'Taiwan': '57000228', 'Tajikistan': '57000229', 'Tanzania': '57000230', 'Thailand': '57000231', 'Timor-Leste': '57000232', 'Togo': '57000233', 'Tokelau': '57000234', 'Tonga': '57000235', 'Trinidad and Tobago': '57000236', 'Tristan da Cunha': '57000237', 'Tunisia': '57000238', 'Turkey': '57000239', 'Turkmenistan': '57000240', 'Turks and Caicos Islands': '57000241', 'Tuvalu': '57000242', 'U.S. Outlying Islands': '57000243', 'U.S. Virgin Islands': '57000244', 'Uganda': '57000245', 'Ukraine': '57000246', 'United Arab Emirates': '57000247', 'United Kingdom': '57000248', 'United States': '57000249', 'Uruguay': '57000250', 'Uzbekistan': '57000251', 'Vanuatu': '57000252', 'Vatican City': '57000253', 'Venezuela': '57000254', 'Vietnam': '57000255', 'Wallis and Futuna': '57000256', 'Western Sahara': '57000257', 'Yemen': '57000258', 'Zambia': '57000259', 'Zimbabwe': '57000260', 'Åland Islands': '57000008'}

		if Type not in types:
			raise Exception("Type = 'clans', 'clanwars' or 'supercellcreators'")

		params = {
			'type': Type
		}

		if Location:
			country_select = countrys.get(Location)
			if country_select:
				params['locationId'] = country_select
			else:
				raise Exception('view all countrys availibles with .countrys')

		response = requests.get('https://statsroyale.com/{}/top/clans'.format(self.select_language), params = params)
		soup = BeautifulSoup(response.content, 'html.parser')
		clans = []

		for clan in soup.find_all('a', class_ = 'clanSearch__cell'):
			ID = clan.get('href').split('/')[-1]
			Nombre = clan.find('div', class_ = 'ui__blueLink').get_text()
			Badge = clan.find('img', class_ = 'clanSearch__badge').get('src')
			Cups = clan.find('div', class_ = 'clanSearch__cup').get_text()
			Members = clan.find('span', class_ = 'clanSearch__full').get_text()
			Country = clan.find_all('div', class_ = 'clanSearch__row')[-1].get_text().strip()
			Country_Flag = clan.find('img', class_ = 'clanSearch__flag').get('src')
			clans.append({'ID': ID, 'name': Nombre, 'badge': Badge, 'cups': Cups, 'members': Members, 'country': Country, 'country_flag': Country_Flag})
		return clans


	def war(self):
		response = requests.get('https://statsroyale.com/{}/clan/{}/war'.format(self.select_language, self.ID))
		soup = BeautifulSoup(response.content, 'html.parser')
		
		Stats = {Stat.find('div', class_ = 'ui__mediumText').get_text():Stat.find('div', class_ = 'ui__headerMedium').get_text() for Stat in soup.find('div', class_ = 'clan__warStats').findChildren('div', recursive = False)}
		Leaderboard = [{'name': clan.find_all('div', class_ = 'clanWar__row')[1].find('a', class_ = 'ui__blueLink').get_text(), 'link': clan.find_all('div', class_ = 'clanWar__row')[1].find('a', class_ = 'ui__blueLink').get('href'), 'image': clan.find_all('div', class_ = 'clanWar__row')[1].find('img').get('src'), 'trophies': clan.find('div', class_ = 'clanWar__trophies').get_text(), 'medals': clan.find('div', class_ = 'clanWar__battle').get_text(), 'repair': clan.find('div', class_ = 'clanWar__wins').get_text()} for clan in soup.find_all('div', class_ = 'clanWar__cell')]
		Participants = [{'name': clan.find_all('div', class_ = 'clanParticipants__row')[1].find('a', class_ = 'ui__blueLink').get_text(), 'link': clan.find_all('div', class_ = 'clanParticipants__row')[1].find('a', class_ = 'ui__blueLink').get('href'), 'Decks used': clan.find_all('div', class_ = 'clanParticipants__row')[2].get_text().strip(), 'Boat Attacks': clan.find_all('div', class_ = 'clanParticipants__row')[3].get_text().strip(), 'Repair': clan.find_all('div', class_ = 'clanParticipants__row')[4].get_text().strip(), 'Medals': clan.find_all('div', class_ = 'clanParticipants__row')[5].get_text().strip()} for clan in soup.find_all('div', class_ = 'clanParticipants__rowContainer')]
		return {'stats': Stats, 'leaderboard': Leaderboard, 'participants': Participants}

	def war_history(self):
		response = requests.get('https://statsroyale.com/{}/clan/{}/war/history'.format(self.select_language, self.ID))
		soup = BeautifulSoup(response.content, 'html.parser')
		Seasons = []

		for season in soup.find_all('div', class_ = 'clanWarHistory__season'):
			War_season = season.find('div', class_ = 'clanWarHistory__leaderboard').get_text().split(' ')[-1]
			Time = season.find('div', class_ = 'clanWarHistory__createdTime').get_text().split(' ')[-1]

			Clans = [{'name': clan.find_all('div', class_ = 'clanWar__row')[1].find('a', class_ = 'ui__blueLink').get_text(), 'link': clan.find_all('div', class_ = 'clanWar__row')[1].find('a', class_ = 'ui__blueLink').get('href'), 'image': clan.find_all('div', class_ = 'clanWar__row')[1].find('img').get('src'), 'trophies': clan.find('div', class_ = 'clanWarHistory__trophies').get_text(), 'medals': clan.find('div', class_ = 'clanWarHistory__wins').get_text(), 'repair': clan.find('div', class_ = 'clanWar__wins').get_text()} for clan in season.find_all('div', class_ = 'clanWarHistory__cell')]
			Seasons.append({'war_season': War_season, 'time': Time, 'clans': Clans})

		for contadorseason, season in enumerate(soup.find_all('div', class_ = 'clanWarHistory__modalOverlay')):
			season = season.find('div', class_ = 'clanWar__table')
			contador = -1
			participants = []

			for tag in season.findChildren(recursive = False):
				if tag.name == 'h1':
					Seasons[contadorseason]['clans'][contador]['participants'] = participants
					participants = []
					contador += 1
				else:
					try:
						Name = tag.find_all('div', class_ = 'clanParticipants__row')[1].get_text().strip()
					except:
						continue

					Link = tag.find_all('div', class_ = 'clanParticipants__row')[1].find('a').get('href').strip()
					Decks_used = tag.find_all('div', class_ = 'clanParticipants__row')[2].get_text().strip()
					Boat_Attacks = tag.find_all('div', class_ = 'clanParticipants__row')[3].get_text().strip()
					Repair = tag.find_all('div', class_ = 'clanParticipants__row')[4].get_text().strip()
					Wins = tag.find_all('div', class_ = 'clanParticipants__row')[5].get_text().strip()
					participants.append({'Name': Name, 'Link': Link, 'Decks used': Decks_used, 'Boat Attacks': Boat_Attacks, 'Repair': Repair, 'Wins': Wins})
			Seasons[contadorseason]['clans'][contador]['participants'] = participants

		return Seasons

class StatsRoyale():
	def __init__(self, language = 'Español'):
		self.languages = ('English', 'Español', 'Português', 'Português', 'Deutsche', 'Français', 'Italiano', 'Русский', '简体中文', '繁體中文', '日本語', '한국어', 'Indonesia', 'Suomi', 'Türkçe')
		self.dict_languages = {'English': 'en', 'Español': 'es', 'Português': 'br', 'Deutsche': 'de', 'Français': 'fr', 'Italiano': 'it', 'Русский': 'ru', '简体中文': 'zh', '繁體中文': 'tw', '日本語': 'ja', '한국어': 'ko', 'Indonesia': 'id', 'Suomi': 'fi', 'Türkçe': 'tr'}
		self.quality_level = {'1': 'common', '2': 'rare', '3': 'epic', '4': 'legendary'}

		self.select_language = self.dict_languages.get(language)
		if self.select_language == None:
			self.select_language = self.dict_languages.get('Español')


	def popular_decks(self, Type = 'ladder', Arena = None):
		params = {
			'type': Type
		}
		{'ladder': 'ladder', 'tournament': 'tournament', 'casual2v2': 'casual2v2', 'grand_challenge': '65000000', 'classic_challenge': '65000001'}


		if Arena:
			params['arena'] = Arena

		response = requests.get('https://statsroyale.com/{}/decks/popular'.format(self.select_language), params = params)
		soup = BeautifulSoup(response.content, 'html.parser')

		decks = [{'cards': [{'link_card': card.get('href'), 'image': card.find('img').get('src')} for card in deck.find('div', class_ = 'popularDecks__decklist').find_all('a')], 'crowns per game': deck.get('data-stars'), 'amount': deck.get('data-count'), 'winp': deck.get('data-winp')} for deck in soup.find_all('div', class_ = 'popularDecks__deck')]
		return decks

	def cards(self):
		response = requests.get('https://statsroyale.com/en/cards')
		soup = BeautifulSoup(response.content, 'html.parser')
		list_cards = []

		for card in soup.find_all('div', class_ = 'cards__card'):
			name = card.get_text().strip()
			elixir = card.get('data-elixir')
			quality = card.get('data-rarity')
			image = card.find('img').get('src')
			page_info = card.find('a').get('href')
			list_cards.append({'name': name, 'elixir': elixir, 'quality': self.quality_level.get(quality), 'image': image, 'link': page_info})
		return list_cards

	def card(self, card_link):
		response = requests.get(card_link)
		soup = BeautifulSoup(response.content, 'html.parser')
		info_general = soup.find('div', class_ ='card__header')
		info_usually = soup.find('div', class_ ='card__pairings')
		info_statics = soup.find('div', class_ ='card__statistics')

		imagen = info_general.find('img').get('src')
		name = info_general.find('div', class_ = 'card__cardName').get_text()
		rarity = info_general.find('div', class_ = 'card__rarity').get_text(strip = True)
		description = info_general.find('div', class_ = 'card__description').get_text(strip = True)[:-len(rarity)-1].replace('\xa0', ' ')
		Type = rarity.split(', ')[0]
		arena = rarity.split(', ')[1].replace('\xa0', ' ').split(' ')[-1]

		card_metrics = info_general.find('div', class_ = 'card__metrics')
		try:
			metrics = {x.get_text().strip().replace(' ', '').split('\n')[0]: x.get_text().strip().replace(' ', '').split('\n')[2] for x in card_metrics.findChildren('div', recursive = False) if len(x.get_text().strip().replace(' ', '').split('\n')) == 3}
		except:
			metrics = {}

		combination = [{'page_info': x.get('href'), 'image': x.find('img').get('src')} for x in soup.find('div', class_ = 'card__pairingsCards').find_all('a')]
		decks = [{'cards': [{'link': card.get('href'), 'image': card.find('img').get('src')} for card in deck.find('div', class_ = 'deckBuilderDeck__decklist').find_all('a')],'trophy': deck.find('div', class_ = 'deckBuilderDeck__trophyContainer').find('span').get_text(), 'elixir': deck.find('div', class_ = 'deckBuilderDeck__elixir').find('span').get_text()} for deck in soup.find_all('div', class_ = 'deckBuilderDeck')]
		info = {'image': imagen, 'name': name, 'description': description, 'type': Type, 'arena': arena, 'metrics': metrics, 'decks': decks}
		return info