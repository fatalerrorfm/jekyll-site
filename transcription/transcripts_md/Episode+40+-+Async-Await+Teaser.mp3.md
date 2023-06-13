Speaker B
That being said, I do have a question for you, which is do you think that every Async function should be implicitly throws as well? They ask that in one of these headers.

Speaker C
Yeah, I forget exactly. I think that's maybe under Alternatives Considered.

Speaker B
It'S alternate syntax options, not quite the Alternatives Considered section, but it says make Async be a subtype of throws instead of orthogonal to it. I'm wondering what you think about that.

Speaker C
Yeah, I mean, that definitely would simplify things, but I don't know. There are a lot of Asynchronous things that just do something and basically won't fail.

Speaker B
Right?

Speaker C
Yeah, my gut feeling is that I don't like this.

Speaker B
Yeah, I think they should be separate as well. I think they should be orthogonal. I think there are plenty of things that happen Asynchronously that never fail. I would like to be able to model those and I would like to be able to do Async without having to do catch block every single time. And then you'd be like doing try bang Await because you know it's not going to fail. It would be horrible.

Speaker A
Yeah. If you want to hear the rest of this episode and all our even numbered episodes, you can subscribe to our Patreon. Subscribing to the Patreon gives you access to our entire back, catalog the rest of this episode and future private episodes. We use the money from Patreon to pay for things like editing costs, hosting costs and other incidentals. Our podcast is sponsor free and we'd really love to keep it that way. Details on how to become a supporter are in the show notes or you can visit us at fatalairrorrorror FM.

