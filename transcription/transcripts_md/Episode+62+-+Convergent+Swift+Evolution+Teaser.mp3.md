Chris Dzombak
Yeah.

Soroush Khanlou
So I think it's still safe in.

Chris Dzombak
Terms of memory safety. Maybe not. If you're doing this, you know, that you may allow overflows in your arithmetic, but it's not going to crash, which.

Soroush Khanlou
Could cause other bugs. You could always assume that adding A plus B is always going to give you a number bigger than A and B, but you can end up with one smaller.

Chris Dzombak
Right. And that's why Swift normally would trap and you have to opt out of that behavior specifically.

Soroush Khanlou
We yeah, very reasonable. Okay, cool. Thank you for checking me on that. So those are two of the ways you can add, but it turns out there's a third way that you can add and there's a function called adding reporting overflow. And so what that will do is it will return a Tuple.

Chris Dzombak
There's a function on integer or on.

Soroush Khanlou
It'S on is it a binary integer.

Chris Dzombak
Okay.

Soroush Khanlou
So that's like the protocol that represents int eight and 64 and 32 and so on. Right. So when you go to add, it returns a Tuple and the Tuple has the overflowed value and then a true or false for if you need to carry into the next bit or into the next digit.

Chris Dzombak
Okay. If you want to hear the rest of this episode and all our even numbered episodes, you can subscribe to our Patreon. Subscribing to the Patreon gives you access to our entire back, catalog the rest of this episode and future private episodes. We use the money from Patreon to pay for things like editing costs, hosting costs and other incidentals. Our podcast is sponsor free and we'd really love to keep it that way. Details on how to become a supporter are in the Show notes or you can visit us at fatalairror FM.

