# discordTCG
discordTCG is a fully-functional trading card game which works inside Discord. It includes numerous interesting game functions, (currently) over 100 cards, trading, collecting, packs, deck building, etc.

If you have suggestions for cards or mechanics, feel free to open an Issue!

# Usage

## Invite to existing server
1. [Click this to invite my bot to your server](https://discordapp.com/api/oauth2/authorize?client_id=545701080047026176&permissions=0&scope=bot)
(the bot is not always up so it will probably be offline)
2. Use the =help and =tutorial commands to learn how to play the game!

## Create your own instance of the bot (with your own cards)
1. Fork/download this
2. Run pip install discord.py
3. In config.py, add your private bot key that the Discord Developer section should grant
4. If you're not using them, delete `cards/New Card.py` and `nodes/New Node.py`. Keeping them in will break things - they're just there for reference.
5. Run matchFunctions.py

## Potential features
- Multiple triggers per Node
- Integrations with other bots
- Analytics
- Automatic testing

## Refactoring todo 
- Rework trade monolith function?

To add cards, use the New Card.py file and "fill in the blanks". 

[Custom Card Documentation](https://github.com/Pazda/discordTCG/wiki)

To add nodes, do the same with New Node.py.
