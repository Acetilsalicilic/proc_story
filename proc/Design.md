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

## NPC stuff
### Relationsips
There are complicated. But there are mainly two kinds of relationships:
- Family, that are created when one is born and won't ever change
- Arbitrary, like everything else like lovers, friends, rivals, etc. These change and evolve, are created dynamically and independant on family relationships.
These two types are independant, at least, they don't depend directly, but maybe social rules and stuff can make so cousins won't want to be partners too.

One must generate the two types of relations on the simulation.

Family is easy, just static analysis of the genealogical tree to determine, when an NPC is born, the relationships it has.

_**Every NPC has a Gen tree. No one appears from nowhere, except maybe GenTree founders, Adan and Eva**_

On the other hand, dynamic relationships are the interesting and fun part.