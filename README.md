# discordTCG
discordTCG is a fully-functional trading card game which works inside Discord. It includes numerous interesting game functions, (currently) over 100 cards, trading, collecting, packs, deck building, etc.

If you have suggestions for cards or mechanics, feel free to message me on Discord - Pazda#6899

# Usage

## Invite to existing server
1. [Click this to invite your bot](https://discordapp.com/api/oauth2/authorize?client_id=545701080047026176&permissions=0&scope=bot)
2. Use the =help and =tutorial commands to learn how to play the game!

## Create your own instance of the bot (with your own cards)
1. Fork/download this
2. In config.py, add your bot key that the Discord Developer section should grant
3. Run matchFunctions.py

## Potential features
- Multiple triggers per Node
- Trigger cleanup
- Integrations with other bots
- Analytics

## Refactoring todo 
- Make decorator for checking whether a player is registered
- Abstract triggers out, as well as start/end of turn effects
- Rework trade monolith function?

To add cards, use the New Card.py file and "fill in the blanks". 
[Custom Card Documentation](https://github.com/Pazda/discordTCG/wiki)
To add nodes, do the same with New Node.py.
