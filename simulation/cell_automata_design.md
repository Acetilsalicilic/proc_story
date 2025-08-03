# Cellular automata
I'm now trying a new approach. Having some basic idea of how to do this thing and having a more or less solid logging and reporting approach, I may be now in the capacity of trying a better approach.

## Stuff
What I want to achieve with this simulation is the following:
- Generate places
- Generate people
- Above all, generate history
So, I must center my efforts into that. I will put down some basic story shape, and have the simulation determine what to do in that time.
I want to generate interesting stories. And for that, I'll have a timeline generated using some rules:
1. The raise and fall of civilizations.
2. We start with some civilizations with small amounts of population
3. Over time, civilizations start to grow according to the resources on their domains
4. When two civilizations encounter, if their size and wealth is similar, they'll trade. Otherwise, they'll fight
5. Civilizations always try to expand. So when figthing for resoruces and spaces, they'll have wars
6. Civilizations rise and rise, but in some point, they'll start to fall. And a new civilization will raise.

I really want to have detail into this 'cause it's getting damn complicated. Again.

## Civilizations
They are populations. They have:
- Population
- Wealth
- Military
- Lands
- Tensions
- Ideologies
Civilizations tend to grow, until internal tensions are strong enough to break them. When a civilization breaks, it separates in other smaller ones.
Think of this as empires breaking into smaller countries. As history advances, the civilizations develop new ways of stabilizing themselves, allowing to have the breaking point further in the population growth.

## Civilization breaking
The breaking point when a civil war or revolution ocurrs depends on the stability of the nation. Things that lowers it:
- Low wealth
- Low population/lands ration
- General population size compared to civilization "stage"
- Incompatible ideologies inside
- Wars

Things that increases it's stability:
- High wealth
- High population/lands ratio
- Margin of pop. size compared to stage
- Compatible ideologies

When a civilization breaks, it breaks following some rules:
- New nations have a more or less stable ideological groups
- New nations have less population
- Wealth is partitioned following the size rules

A revolution/civil war ocurrs for some reason. And whatever it is, new nations will form around ideologies. The bigger the ideology, the more land, wealth, adn population that nation gets. So if we have these ideologies, they'll get the following resources:

| Ideology | pop. ratio | resources ration |
|----------|------------|------------------|
| A        | 30%        | 30%              |
| B        | 40%        | 40%              |
| C        | 20%        | 20%              |
| D        | 10%        | 10%              |

Not really complex, although resources are not square like that. Small portions of ideologies will still be into those nations, so nations don't perfectly separate into homogeneous ideological bodies.

Land to population ratio doesn't grow equally. a ratio of 2:1 land to population isn't the same for a million population nation than for a hundrer million nation. Maybe for the smaller one, it's alright, but for the bigger one, it's not, and the growth of population pushes this nation to the breaking point.

Obviously, these new nations form around the lands with the most ideological similarity and presence in the territory.

## Ideologies
These have this traits:
- Radicality
- Values - wealth, war, intellect

The ideologies are not static. They change, and depending on some rules, their presence and stuff changes. They're not bound to national borders. The rules are the following:
- Ideologies travel faster to places with existing compatible ideologies
- The state of a nation/civilization determines what ideology gets attracted - if high wealth, according ideologies come, if unstable, more radical and violent ideologies come
- Near zones get the influence first
- Trade makes the process faster.

## Heroes
Every good story has a hero. Every war creates some heroes, at least one for ideology. These will be stored for later use in generated places.

## Wars
Wars between civilizations are tought. They can ocurr if two civilizations clash geographically. Not always, but if:
- The difference between sizes passes some threshold
- If one has some natural resource the other one needs - includes land

What determines the victory of a nation is some rules:
- If a critical place is taken by the other nation
- If wealth runs out
- If military size passes a threshold
- If a nation breaks, then war may continue with the smaller nations

When a nation wins over the other, it's land and population gets asimilated, and the opposing ideologies that powered that nation needs to go somewhere else. But if the new territory's ideologies are too different or too radical, a civil war may ocurr.