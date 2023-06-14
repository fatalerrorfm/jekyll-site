Chris Dzombak
Swift is Swift string, and like, string in general is kind of a minefield of performance anyway. Maybe they just don't care.

Soroush Khanlou
Well, so as you were saying that, I realized that they don't say that swift that string will become a by a Random Access collection anywhere.

Chris Dzombak
Right. It becomes a bi directional collection, which I found weird. I thought it would probably be a regular collection before it would be a bi directional collection.

Soroush Khanlou
I mean, you can still walk forward and back in, what, linear time, right?

Chris Dzombak
Well, but you can't walk backwards because let's say you start with a character that's one byte, and then you want to go back one character. You don't know how many bytes that character is going to be before you.

Soroush Khanlou
Is it possible for it to just keep walking backward until you I guess.

Chris Dzombak
It'S hard to tell where complete a character. Yeah, you wouldn't know. But they do talk about string being bi directionally. Iterable I guess, and I don't know why that is. That stuck out to me as kind of odd.

Soroush Khanlou
Yeah, that definitely is odd. I'm realizing that my understanding here I was assuming that they were making a Random Access Collection, which right, just doesn't.

Soroush Khanlou
If you want to hear the rest of this episode and all our even numbered episodes, you can subscribe to our patreon. So subscribing to the Patreon gives you access to our entire back, catalog the rest of this episode, and future private episodes. We use the money from Patreon to pay for things like editing costs, hosting costs, and other incidentals. Our podcast is sponsor free, and we'd really love to keep it that way. Details on how to become a supporter are in the show notes. Or you can visit us at fatalairror FM.

