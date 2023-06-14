Soroush Khanlou
Yeah, shape of water. She does fall in love with the fish. I come back and I look at my computer, and the tests are stuck at 18%. So they've just been running for two and a half hours, and they're just stuck.

Chris Dzombak
Wait, but you said that you would run the tests before this, too, right?

Soroush Khanlou
So clearly.

Chris Dzombak
How long did that take?

Soroush Khanlou
I don't know, 20 minutes?

Chris Dzombak
How exactly did you break this test?

Soroush Khanlou
What I did was, if you look at the implementation, you see how it returns in any sequence of result, which is like the array that it's built up. I just returned an any sequence of an empty array.

Soroush Khanlou
Weird.

Soroush Khanlou
Okay, so what it did is, because the tests themselves are written in swift, it broke something somewhere such that the tests couldn't actually complete, which is good in a sense. It means that I can effectively break these tests, right? Like, you want to know that there are tests covering the thing, that you might change it to my implementation. And then no tests failed. That could mean that my implementation if you want to hear the rest of this episode and all of our even numbered episodes, you can subscribe to our Patreon. Subscribing to the Patreon gives you access to our entire back, catalog the rest of this episode and future private episodes. We use the money from the Patreon to pay for things like editing costs, hosting costs, and other incidentals. Our podcast is sponsor free, and we'd really love to keep it that way. Details on how to become a supporter are in the show notes, or you can visit Fatalairror FM.

