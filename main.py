# Required libraries
import requests
import secrets
import threading

# Ask the user how many memes they want to scrape with a maximum limit of 50.
print('How many memes do you want to scrape? [Max 50]')
amount = int(input('> '))

# Ensure the user does not request more than 50 memes.
if amount > 50:
    print("You can only request up to 50 memes.")
    amount = 50

# Ask the user for the name of the subreddit they want to scrape from.
print('Which subreddit do you want to scrape from?')
subreddit = input('> ')

# This function is responsible for downloading the meme from its URL and saving it locally.
def downloadMeme(meme):
    # Request the meme using its URL
    requestContent = requests.get(meme['url']).content

    # Save the meme in the 'Memes' directory with a random file name.
    # 'secrets.token_hex(20)' generates a random filename.
    with open(f'Memes/{secrets.token_hex(20)}.png', 'wb') as file:
        file.write(requestContent)
    
    # Print the URL of the meme that was just downloaded.
    print('Got a new meme! URL: {}'.format(meme['url']))

# Send a request to the meme API to get memes from the specified subreddit.
r = requests.get(f'https://meme-api.herokuapp.com/gimme/{subreddit}/{amount}')

# For each meme in the response, start a new thread to download the meme.
# This is done to speed up the download process by downloading multiple memes concurrently.
for meme in r.json()['memes'][:amount]:  # Ensure we only process the user-specified amount of memes
    threading.Thread(target=downloadMeme, args=(meme,)).start()
