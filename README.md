# Trivia Lab

This lab serves as a refresher for loops, classes, and lists (After students return from the summer)
and as an intro to coding on the Raspberry Pi (with hardware output).

# Play

Run 'python3 game.py arg' to play!

The 'arg' represents which view type will be selected. For the first part of the lab we will be using 'TerminalView' and for the hardware section we will be using 'PiView'.

To select `TerminalView` run `python3 game.py t`
To select `PiView` run `python3 game.py p`

## Trivia.txt

The trivia questions and answers are stored in `trivia.txt`. There are two question types: fill in the blank and multiple choice. There is no limit for how many prompts can be stored.

The format for a fill in the blank question is as follows...
```
Question:
What is 2+2?
Answer:
4
```

The format for a multiple choices question is as follows.
```
Question:
What is 2+2?
Answer:
2,5,9
```
The program stores the potential answers as a list and stores the first potential answer in the list as the correct answer.


## Testing
To run the test scripts, use:

```shell
python3 test.py
```

To run a single test script for one of the functions, use one of the following:

```shell
python3 -k test.py guess

python3 -k test.py choices

python3 -k test.py game
```
