
# Clash Royale Gold Farm Bot

We all hate how p2w Clash Royale is, but nontheless what is the currency that allows us to upgrade cards? Gold, and how can we obtain gold? By mastering cards’ levels.

This project, thanks to autoclicking and image recognition, creates a bot that automatically plays matches and places cards in order to master them.

Special Thanks to [Kian Brose](https://www.youtube.com/@KianBrose/videos) because i took inspiration from his video about CR.

## How does it work

The program consists of 3 stages:

- in-lobby status, where the bot starts a new match in the events section
- in-match status, where the bot places troops in different positions of the field based on their importance
- after-match status, where the bot goes back to the lobby to start a new match

## What you need to make the script work:

- run Clash Ryale on Bluestacks on full screen mode
- screen should be a 1920x1080 one
- have a deck filled with 1 elixir card except for the one you want to master (not necessary but useful)

## Module used:

- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

## Coordinates to keep in mind

- left bridge: Point(x=954, y=489)
- right bridge: Point(x=1250, y=504)
- left tower: Point(x=905, y=704)
- right tower: Point(x=1285, y=751)
- position of the first card in the deck out of the first 4: Point(x=984, y=914)
- position of the troop to spawn in the deck: via script
## Acknowledgements

 - [Kian Brose YT channel](https://www.youtube.com/@KianBrose/videos)
 - [My GitHub profile](https://github.com/EsseFNC)
 - [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

![Logo](https://preview.redd.it/vregoku5h8bd1.jpeg?auto=webp&s=efdd6b206524a4417df62e095c84814b5c513307)
