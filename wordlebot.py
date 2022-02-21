import discord, random

client = discord.Client()
black = ":black_large_square:"
yellow = ":yellow_square:"
green = ":green_square:"
words = []
guess_count = 0

with open("probable_words.txt", "r") as f:
    for x in f:
        words.append(x[:-1])

current_word = random.choice(words)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global current_word, words, guess_count

    if message.author == client.user:
        return

    if message.channel.id != 945073984997847130:
        return

    if message.content == "wordle word" and message.author.id == 304686699621908490:
        await message.channel.send(current_word)

    if message.content.startswith("wordle "):
        if len(message.content.split(" ")) != 2:
            return
        
        guess = message.content.split(" ")[1]
        if len(guess) != 5:
            return

        good_word = False
        with open("possible_words.txt", "r") as f:
            for x in f:
                if guess in x:
                    good_word = True
                    break

        if not good_word:
            return

        guess_count += 1

        answer = ""
        squares = ""
        for letter in guess:
            answer += f":regional_indicator_{letter}: "
            if letter in current_word and current_word[guess.index(letter)] == letter:
                squares += green
            elif letter in current_word:
                squares += yellow
            else:
                squares += black
            squares += " "

        if guess == current_word:
            current_word = random.choice(words)

        await message.channel.send(f"Guess {guess_count}\n{answer}\n{squares}")








client.run('OTQ1MDY4OTg4NDkxMjU1ODM5.YhKyFQ.hOoeI_qdYMfH-WW8xyjrtKAxwfQ')