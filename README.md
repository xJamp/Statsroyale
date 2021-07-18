# [Statsroyale](https://statsroyale.com/) Scraping

## Use      
### 1. [Player](#1-player)
1. [Information](#1-information)
2. [Battles](#2-battles)
3. [Decks](#3-decks)
4. [Cards](#4-cards)
5. [Refresh](#5-refresh)
6. [Top](#6-top)
7. [Countrys](#7-countrys)
### 2. [Clan](#1-clan)
1. [Search](#1-search)
2. [Information](#2-information)
3. [War](#3-war)
4. [War History](#4-warhistory)
5. [Top](#5-top)
6. [Refresh](#6-refresh)

### 3. [StatsRoyale](#1-trends)
1. [Cards](#1-cards)
2. [Card info](#2-cardinfo)
3. [decks_popular](#3-deckspopular)


- - -
## Dependencies
- [requests] - send the requests
- [BeautifulSoup] - process html
- [json] - load objects
- - -
## Uso general
```sh
from StatsRoyale import Player, Clan, StatsRoyale
Object1 = Player(ID)
Object2 = Clan(ID)
Object3 = StatsRoyale()
```
# `1. Player`
#### `1. Information`
- Nothing params
```sh
Object.information()
```
#### `2. Battles`
- Nothing params
```sh
Object.battles()
```
#### `3. Decks`
- Nothing params
```sh
Object.decks()
```
#### `4. Cards`
- Nothing params

```sh
Object.cards()
```
#### `5. Refresh`
- Nothing params
```sh
Object.refresh() # return True if work
```
#### `6. Top`
- Type: string - optional - filter - values: ('current-season', 'all-time', 'most-donations', 'most-cards-won', 'most-war-wins', 'most-war-cards' or 'most-matches')
- Location: string - optional - filter country - [values](#7-countrys)
- Level: string - optional - between 1 and 13
- Limit: int - optional - between 1 and 1000
```sh
Object.top()
```
#### `7. Countrys`
```sh
Object.countrys
```

# `2. Clan`
#### `1. Search`
- name: string - required
```sh
Object.search(name = 'Team Queso')
```
#### `2. Information`
- Nothing params
```sh
Object.information()
```
#### `3. War`
- Nothing params

```sh
Object.war()
```
#### `4. War history`
- Nothing params

```sh
Object.war_history(')
```
#### `5. Top`
- Type: string - optional - filter - values: ('clans', 'clanwars', 'supercellcreators')
- Location: string - optional - filter country - [values](#7-countrys)
```sh
Object.top()
```
#### `6. Refresh`
- Nothing params

```sh
Object.refresh()
```

# `3. StatsRoyale`
#### `1. Cards`
- Nothin params
```sh
Object.cards()
```
#### `2. Card`
- Card_link: string - required - with this link return information of the card
```sh
Object.card(card_link = 'https://statsroyale.com/card/P.E.K.K.A')
```
#### `3. Popular Decks`
- Type: string - optional - values: ('ladder', 'tournament', 'casual2v2', 'grandchallenge' 'classic_challenge')
- Location: string - optional - filter country - values
- Arena: string - optional - between 1 and 13
```sh
Object.popular_decks()
```

## License
MIT


   [requests]: <https://docs.python-requests.org/en/master/>
   [json]: <https://docs.python.org/3/library/json.html>
