# Higher Lower Game

Simple Python game that allows user to play Higher Lower Game.\
Rules:
- player has to guess which instagram profile has more followers(data is stored in list with dictionaries with informations about one specific profile)
- each profile in database can be chosen only onec
- game starts with two random profiles - current profile 1 and current profile 2
- after right answer current profile 2 becomes current profile 1 and new profile(which hasn't been compared) is randomly chosen to become current profile 2 
- player can see displayed infromations about profile: name, description and country and has to guess which profile has more followers on instagram based on this informations
- if player guess right their good answer score is increased by 1 and they move on to another question, if player guess wrong game ends
