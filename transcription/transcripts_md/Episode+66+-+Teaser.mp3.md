Speaker A
Yeah. This is something something that I'm kind of struggling with thinking about. Like thinking about your proposal or your pitch and thinking about this is that I don't have a this. These are such, like, fundamental parts of the standard library that I don't feel like I have a really good understanding for the breadth of how people may be using them in different code bases.

Speaker B
Yeah.

Speaker A
And like, the different pitfalls that that people may be experiencing.

Speaker B
Yeah.

Speaker A
Makes it really hard to evaluate these changes and also hard to evaluate how good is what we have now.

Speaker B
Yeah, I think that's right. I think until you get into the really nitty gritty of, like, you've defined a bunch of sequences and collections of your own, I think you have to kind of spend some time and think about it. It's pretty weird in terms of a system. Some people's proposal is go the other way and say, so the whole point of the sequence protocol is that anything that conforms to sequence, you can put it into a for in loop. Right. So some people say, okay, why don't we make iterators the things that are for inable? And then once we have that, then we always know iterators are single pass and then sequence can go to being multipass and then the rest of the hierarchy does its own thing.

Speaker A
That does seem to make sense, at least at the outset. Are there problems with that approach?

Speaker B
Yeah. So the problems that I see with it are if you have a type that is singly iterable.

Speaker A
If you want to hear the rest of this episode and all our even numbered episodes, you can subscribe to our Patreon. Subscribing to the Patreon gives you access to our Higher Back catalog, the rest of this episode, and future private episodes. We use the money from Patreon to pay for things like editing costs, hosting costs, and other incidentals. Our podcast is sponsor free and we'd really love to keep it that way. Details on how to become a supporter are in the show notes or you can visit us at fatalerorrorror FM.

