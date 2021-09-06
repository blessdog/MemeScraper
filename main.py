import requests, string, threading, secrets

print('How many memes do you want to scrape? [Max 50]')
amount = int(input('> '))

print('Which subreddit do you want to scrape from?')
subreddit = input('> ')

def downloadMeme(meme):
    requestContent = requests.get(meme['url']).content
    open(f'Memes/{secrets.token_hex(20)))}.png', 'wb').write(requestContent)
    print('Got a new meme! URL: {}'.format(meme['url']))

r = requests.get(f'https://meme-api.herokuapp.com/gimme/{subreddit}/50')
for meme in r.json()['memes']:
    threading.Thread(target=downloadMeme, args=(meme,)).start()
