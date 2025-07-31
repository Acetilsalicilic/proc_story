# What's this

This is supposed to be a silly CLI game, text based, using some _textual_ framework to do fanci UI. But, at it's heart, is just a silly game inspired by dwarf fortress.

## The premise (plot)
is an adventure game. You're an adventurer. You can choose from different races, and have a name generated and a history, with different characteristics depending on the background of your character.

You then go through a multi-chapter history, hopefully infinite until you die, where you can encounter people, talk to them, and stuff, do actions, have some conbat and explore.

## Modes
These are modes available all time in game.
- Explore
- Converse
- Fight

### Explore
In explore mode, basically you can move around and interact with stuff. Not so complex, but you have a basic list of stuff that you can see and interact with. Mainly, people and furniture.

### Converse
Well, you can talk to people.

### Fight
You enter fight mode when facing a hostile enemy. Hopefully, this will implement some vision detection and stuff, but for now, just world and story are generated.

## Races
We have the following:
- Human
- Elf
- Dwarf
- Demon

## Procedural generation
What will be procedurally generated?

Well, everything. But seriously, mainly story and characters. We'll see about other stuff later, but for this first version, I'd like to generate story for characters and NPCs so you can talk with them and see their thoughts, character, and feelings.

### What does an NPC have?
Well, I think of these:
- Personality
- Thoughts
- Relationships
- Skills
- Description
- Belongings
- Name
- Gender
- Age

All these must be generated initialy, and will evolve with gameplay, maybe with the exception of personality. We'll see.

#### NPC generation process
These are more or less the steps to generate an npc:
1. Basically, we must first simulate a family tree. Starting from parents, we'll have some children randomly generated with names alleatory and gender based on some prob tables, as well as number of children. Then, we'll just redo all the work, maybe spawning some partners for these creatures so we don't have incest (maybe some incest for first versions is good)