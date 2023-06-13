Speaker A
Hey, man.

Speaker B
Hey, how's it going?

Speaker A
Not too bad, not too bad. How's your week?

Speaker B
It's been good. It's been busy. I don't really have anything interesting to report from a software development standpoint, but, yeah, it's been good. How about you? I mean, just to dive in. You got back from Techie Con in Atlanta, right?

Speaker A
Yeah. Went to Techie con. It was super nice. I got back on Wednesday.

Speaker B
Okay.

Speaker A
It was a cool conference.

Speaker B
Can you remind me, is it an iOS focused conference or software development in general?

Speaker A
It was iOS focused. Yeah. A large number of the talks were actually one of the themes of the conference was, like, architecture stuff. Interesting architecture app. Yeah, that was pretty cool. I thought you would like that. There was, I think, three of the maybe ten talks. Three of them were all about architecture and what patterns you should use, what.

Speaker B
Kinds of architecture were covered. Did it go from kind of standard Apple style MVC to more exotic things? Was it all exotic things?

Speaker A
Okay, so two of them basically were like, MVVM is the way to go. MVVM maybe plus a little reactive. It was like that kind of that approach. So Shushtof gave one talk oh, cool. On architecture. So he did like an MVVM plus reactive, plus flow coordinators. That was his. There was somebody else who I've never met before, but his name is Michael Ayres, and he was also suggesting a bunch of different architecture patterns that you could do. And he was primarily pushing MVVM, but also saying, you got to figure out the pattern that works best for yourself. And getting all that, that is something.

Speaker B
That I think gets lost in discussions like this is depending on the app, depending on the project, depending on the size of your team, depending on who you're working with. Different architectures. Different architectures make sense for different projects. There's not really a one size fits all right answer, I would say.

Speaker A
Yeah, I think that's definitely right. One of the things I do think is important is whatever architecture you do pick, stay consistent within that app.

Speaker B
Yeah, I think that's definitely I think.

Speaker A
That could be really good. So once you learn the pattern for one or two screens, you can kind of use that knowledge of that pattern to kind of get a sense of every other screen and how it's how it's sort of laid out and set up. The third architecture talk, which was the most interesting to me was Dave DeLong did an architecture talk, and he was basically saying he said a bunch of really interesting things. His approach was essentially treat UI view controllers as though they are UI views. Basically never subclass UI view. If you need some special, the only time you should subclass UI view is if you're overwriting draw rect. If you're drawing, then you can use a view. Otherwise, everything happens in a view controller. Like, if you want to group a bunch of views together. That happens in a view controller.

Speaker B
Okay.

Speaker A
And then your view controller serves such data as well. You have your model layer that doesn't change. And then he was basically saying, add another layer, the controller layer, that basically tells everything what to do. And what I really like that about that approach is that it was a really new way of thinking about, okay, what is a view controller really do? He was like, MVVM. People say, oh, yeah, your view controller is in the view layer. He really committed and said, like, no, this really is the view layer. And then that way you can do traditional MVC. And if you remember traditional MVC, there's three parts, and all three parts have a bi directional arrow. So not only does the view controller in the view talk or the controller in the view talk, the model in the controller talk, but also the view in the model talk. And nobody ever wants to commit and do that part of it, that extra line.

Speaker B
So, I mean, what does that look.

Speaker A
Well, that looks like your view controller holding on to whatever models it's bound to.

Speaker B
And what is the communication I mean, if it's a bi directional arrow, what is the communication from the view controller, which we're considering as part of the view layer back to the model look.

Speaker A
Like the view mutates the model.

Speaker B
Okay. What does the controller do then?

Speaker A
The controller handles touch input and events and stuff.

Speaker B
Interesting.

Speaker A
Yeah. Now that I'm thinking about it, I'm not really sure how the view would need to update the model if it's not going through a user action.

Speaker B
Right, yeah. So I'm trying to figure out here, a, what advantages this gives us, and B, really how it differs from MVVM. I guess it differs from MVVM based on what you've told me so far in the view and the model are allowed to communicate. I'm a little bit unclear on what that gets us, I would say, but yeah. What are the advantages of doing things this way?

Speaker A
What it gets you is I'm not Dave, so I don't think I could do this quite the justice that it deserves. There's a couple of differences. So one is that in MVVM, the view controller is still the boss. The view controller knows about the view model, and the view model knows about the model, but the view model doesn't directly know about the view controller. Right. So that relationship is like a delegate relationship or a block relationship or a signal relationship. Sure. And so the view controller is still the boss there. But I think that part of what Dave's proposing is that the view controller is not that anymore. The controller truly lives above the view controller in that it knows about the view controller, but the view controller doesn't know about it. I think that's part of it. And then you're asking about the connection between the model and the view? Well, the model and the view are connected because of the view needs to be able to display the model. So that's one link, but I don't know if the link goes back the other way, so I don't know if I can answer that part of it.

Speaker B
And what does that link look like? Do you want to use any sort of, like, reactive or binding sort of technology here?

Speaker A
So I think it doesn't prescribe anything in that department. I would just use something simpler. Delegates, whatever. Maybe if you like reactive, you could do reactive. But there is a connection there, basically.

Speaker B
Do you know if talks from this conference are going to be put online anywhere?

Speaker A
Yeah, they were recorded and they will be online. I just don't know when.

Speaker B
Okay.

Speaker A
I'm sure they'll trickle around the Internet.

Speaker B
Yeah, I'd be curious to watch to watch Dave's talk in particular.

Speaker A
I should also say that I'm kind of putting my twist on Dave's talk based on what I understood about it. But it's possible that Dave, like, if you listen that talk directly, you'll get something slightly different.

Speaker B
I think that's true anytime we try to summarize the talk.

Speaker A
Yeah, I think that's basically right.

Speaker B
Okay.

Speaker A
Yeah. I have the original small talk MVC paper on my computer. And I should really read this.

Speaker B
I guess I should too.

Speaker A
Let's throw in the show notes. Maybe that could be aspirational.

Speaker B
Yeah, I have that saved somewhere here. Oh, there's a link in the show notes. Cool. So what else happened at this conference? There are some talks about MVVM, about actual MVC. Right. You gave a talk. How did your talk go?

Speaker A
My talk was pretty good. I think it was the best version of the you deserve nice things talk that I've given so far.

Speaker B
Nice.

Speaker A
So I'm pretty happy about that. One of the things I was doing in my previous versions of the talk was, like, if there was a concept that I needed to illustrate, I would, like, use my hands. So I'd say, like, oh, if you're reversing an array, like, this object goes over here, and I'm, like, swinging my hands around wildly on stage. And I realized, like, I have slides, and those slides can have animations, and I'm allowed to use those animations. And so what I ended up doing was for this version of the talk, I fleshed out a lot of those animations a lot better so that it made more sense and so that you could see the clean animations, like showing you exactly what I wanted you to see. And I think those came out really good. I'm pretty happy with how that ended up happening.

Speaker B
Cool. I'm glad to hear it. I'll have to go and rewatch this version of your talk again once videos from this conference make their way onto the Internet.

Speaker A
Yeah, it should be good. I think it came out good. And then I added a couple of extra examples here and there. And I also added one more thing, which I haven't done in previous versions, which is essentially this is a patriot episode, so I can tell you all my secrets. There are these common objections that are raised every time you suggest that something should be an extension. And they're basically like, this is too Esoteric, nobody would ever use this. This is too specific, which is a little bit different, which is sort of like, this is behavior that won't be used frequently enough. I think I'm having a tough time distinguishing Esoteric and specific, but I think they're different. And then, of course, this is too simple. We don't need this to be in the standard library because I can just write this myself. And I basically go through and I find examples from the standard library of each that you would raise those objections about each of those things, but because they're already in the standard library, I think we kind of have a little bit of status quo bias. And so we say, oh, well, you know what? Maybe it's actually okay that some things are in there that we aren't going to use every day. Yeah, okay, cool. My example for the most Esoteric was lexicographically proceeds, which is a function on sequence that takes another sequence or kind of compares two sequences. And you can sort of think about it as if you compare a string comparison except for it's not localaware, it's just based on if the elements are comparable. Yeah, that sort of sorting strings is its own challenge.

Speaker B
Yeah, that seems like a weird name for compared. Tell me if this comes before this other thing.

Speaker A
Right, but it's like for the whole array, it's very strange. So it compares each element pair wise, but also it depends, like, who has more elements, who has less elements.

Speaker B
Weird.

Speaker A
It's real weird. And I've never had a chance to use it. I've always wanted to. I have no clue when you would want to use it. Boggles the mind, but it's in there and I know that if I ever need it, it's going to be there ready for me to use.

Speaker B
Yeah, well, and then you have it.

Speaker A
Yeah. There is a usage note here. This method implements the mathematical notion of lexicographical ordering, which has no connection to Unicode. If you are sorting strings to present to the end user use the string APIs that perform localized comparison.

Speaker B
This generalization looking at Wikipedia consists primarily in defining a total order over the sequences of elements of a finite, totally ordered set, often called an alphabet.

Speaker A
That is very confusing, but this has.

Speaker B
Nothing to do with strings.

Speaker A
Right? Well, I think it basically is the same thing as string ordering, but it does. Yeah. String ordering, if you do it correctly, is much more complicated. Yeah, right. Like if you have a bunch of numbers at the beginning of your strings. You want to put one, two, three, and then ten, but if you just compare the individual letters, you'll get one, then ten, then two, which you're not supposed to get, stuff like that. And then different languages have different alphabets and orders of letters and stuff like that.

Speaker B
Yeah. Okay. We're pretty in the weeds here.

Speaker A
I love the weeds.

Speaker B
Anything else? Well, that's true. Anything else from the conference that I don't know, that really struck you or that you really enjoyed?

Speaker A
It was really nice. It was a first time conference, and they did a great job with putting it together and making sure everything worked great. There was, like, this cool luau that rented out a tiki bar. It was all Tiki themed. It was good. It was a really nice conference.

Speaker B
Fun. Did you have a chance to get out into Atlanta in general at all? I've never been to Atlanta, so I have no idea what it's like.

Speaker A
So I did a little bit on the last day. I went to the aquarium with some friends, and the Georgia Aquarium is apparently one of the best aquariums in the world, aquaria. And someone who was with us was from California, and she said that it's better than the Monterey Aquarium.

Speaker B
Whoa.

Speaker A
So that's pretty high praise.

Speaker B
Yeah.

Speaker A
They have a giant tank there that has a whale shark in it, and I'm not sure if you know what a whale shark is. It's not a whale or a shark.

Speaker B
It's just no. Okay.

Speaker A
But they're really big. They are huge.

Speaker B
Really?

Speaker A
Yeah. Maybe like, the size of a really big pickup truck. More than that.

Speaker B
That is huge.

Speaker A
They're really big. They're huge. Yeah, they're enormous. They're the largest fish in the sea, which is a fact that I learned while I was there.

Speaker B
Now, that's distinct from being so they're still smaller than, like, whales, though, right? Because whales are mammals, not fish.

Speaker A
Right. And they're also I'm not sure if they're if sharks are also fish.

Speaker B
I'm like no sharks. 80, 90% sure they are.

Speaker A
Yeah, sharks are fish. And the lotus is the whale shark. 18 meters long.

Speaker B
16Ft. So it is a kind of shark.

Speaker A
It is a kind of shark. I was mistaken about that. Yeah, it's not a whale.

Speaker B
Does it eat the same things that sharks do? Like, does it eat other I don't know, other fish? Does it have big teeth?

Speaker A
So in a twist, it actually eats the same thing as whales. It eats, like, krill and it has, like, filter. It has plankton and eats plankton and that kind of thing.

Speaker B
Weird, but it's a fish, not massive.

Speaker A
Yeah. The name whale shark refers to the fish's size being as large as some species of whales and also to its being a filter feeder, like baleen whales.

Speaker B
That is really weird.

Speaker A
That's super strange.

Speaker B
How does that happen? Like, you end up with a filter at the same way as something that is a mammal and is not even related.

Speaker A
Convergent evolution.

Speaker B
Yeah.

Speaker A
Convergent evolution. Yeah. They diverged at some point, and then they converged again at another point.

Speaker B
That's wild.

Speaker A
There were giant man arrays there which are also very large. The biggest ones of those are like, I don't know, 2020 5ft from tipped from left side to right side, like laterally. Those are huge. There were some very cute otters. There were sea lions. There were dolphins that were trained to do tricks and stuff. It was a cool aquarium.

Speaker B
Cool.

Speaker A
It's really all I got to do in Atlanta, but it was worth it.

Speaker B
That sounds like fun all the same. My time in Atlanta has been limited to the Atlanta airport.

Speaker A
Jackson yeah.

Speaker B
Which is less fun.

Speaker A
Yeah, it's a hell of an airport.

Speaker B
Yeah. So do we want to pivot here and talk about something else that you've been working on?

Speaker A
Main topic?

Speaker B
Yeah, main topic. 17 minutes into the show.

Speaker A
That's right. 17 minutes into a 30 minutes show. We are ready to talk about the real thing.

Speaker B
Let's do it.

Speaker A
You want to talk about so I have been messing around with big NUM.

Speaker B
Okay. With big numbers.

Speaker A
Yeah. So imagine you want to work with an integer that is bigger than 64 bits. What do you do?

Speaker B
Well, I think I would import a big NUM library and use that to represent that integer.

Speaker A
Yeah, pretty much. Essentially the way that it works is, imagine if you wanted to represent 128 bit number, you could represent that with 264 bit numbers, right. And you would put one of them would be sort of the low byte and one of them would be the high byte, essentially. So one of them would store the numbers from zero to 9 quintillion. And then once you hit 9 quintillion, whatever two to the 64th is and one then the high byte, the value of it becomes one. And then the value of the other part resets down to zero. And then you start incrementing up again. So you have a lot more space than 128 bits, but even that sometimes is not enough. And so what you can do is instead of storing 264 bit numbers, you store N 64 bit numbers.

Speaker B
Okay. That makes sense.

Speaker A
Right. So essentially what that means is you store an array of numbers and that array can be pretty much any size. The easiest way to think about this is if you had a type that represented the numbers zero through nine, and you put a bunch of those next to each other in an array as though each one represented a digit. Right. So as soon as you're incrementing, you go from zero all the way to nine in your first position in the array. The array only has one element. As soon as you hit nine and you add one to it, then you need a second element in your array. The first element goes down to zero and then the second element ticks up to one. So now you're at ten and you can keep doing that as much as.

Speaker B
You want, so that makes sense. So this is something that you are trying to implement in Swift just for fun?

Speaker A
Kind of, yes. So there is a Big int implementation in the Swift GitHub repo, but it's not in the standard library. So one of the cool little things about the Swift GitHub repo is that there's a section in there under the folder test called prototypes. And the prototypes are like all kinds of really weird things that they don't want to commit to having in the standard library yet, but they do want to maybe test it, make sure it continues to compile. They want to keep it somewhere, but they don't necessarily want to have it around. Cool. To commit to it being public.

Speaker B
Okay.

Speaker A
Put a link to that in the show notes and essentially BigInt is in there. So this, I believe, is mostly written by Nate Cook, although I'm not 100% sure that could be wrong. So essentially the way it works is it actually gives you the option, it's generic over the type that's in that array, which is really interesting. So you can put uint 64 in there, you can put uint eight, which is I think that's like a nice choice because it's easy to think about things in base 256 as opposed to base 9 quintillion or whatever.

Speaker B
If you're targeting an architecture that doesn't support 64 bit integers natively, for some reason, you wouldn't want to use 64 bit INTs as your sort of underlying type for big int.

Speaker A
Yep. Checks out. Yeah. So and then there's also one other thing you can use, which is you can do it basically with a bit array. So with an array of yes. No, true. False.

Speaker B
Oh, cool.

Speaker A
So that's like a giant binary number, right?

Speaker B
Yeah.

Speaker A
So if you're incrementing, you start with no elements in the array, then you have a one in the array in the first place and then you increment again and then you end up with a zero in the ones place and then a one in the twos place. Right. Because it's base two. So it's a ones place, a twos place, a fours place and eight place, which is pretty interesting. So there's also a version of it in there that is sort of a bit implementation, essentially, which is pretty cool. Yeah. So that's pretty tight. So that's basically how Big NUM works. And it's actually really interesting because let's say you want to implement adding. So I actually implemented some of this stuff in the service of implementing something bigger because big int already exists. I want to do something slightly more interesting than that.

Speaker B
Okay.

Speaker A
Which is the ultimate goal is to implement big decimal. So I want to have a number that is infinitely precise and supports numbers less than one. Okay, right, cool.

Speaker B
Yeah.

Speaker A
So that's the ultimate goal. But to do that, you have to do a bunch of the big int stuff first. So imagine, okay, let's say you want to add two big int numbers that are, let's say, just for the sake of argument, backed by uint eight. Right. They can go from zero to 255 and share values for each array place.

Speaker B
Yeah. So you want to add those how arithmetic with these numbers looks and works.

Speaker A
Yeah, very carefully is the answer. Okay. So let's say you have two one digit numbers, and remember, each of those digits is base 256. So each of those digits is zero to 255. Let's say you're adding 202 hundred. Right. If you try to add those normally, what's going to happen?

Speaker B
You'll overflow.

Speaker A
Yeah, you overflow. And so Swift, I think, traps if you overflow an energy, yes, it crashes. There's also an ampersand plus, which will unchecked crash. So it's like a little bit faster because it won't check, but you're not guaranteed to get valid memory.

Speaker B
Wait, does that unchecked crash or does that add but allow overflow to happen?

Speaker A
I think it allows overflow to happen and then eventually it ends up crashing or something.

Speaker B
I don't think it actually ends up crashing if I'm remembering my Swift stuff. Right. That is the equivalent, like amphersand plus is the equivalent of how plus works in C, C plus plus a bunch of other languages where it just silently overflows.

Speaker A
Interesting.

Speaker B
We should double check this.

Speaker A
Yeah. All the overflow operators begin with an ampersand. However, when you specifically want an overflow condition to truncate the number of available bits, you can opt into this behavior rather than trigger an error. Okay, so you're totally right about this.

Speaker B
Yeah. So I think it's still safe in terms of memory safety. Maybe not. If you're doing this, you know, that you may allow overflows in arithmetic, but.

Speaker A
It'S not going to crash, which could cause other bugs. You could always assume that adding A plus B is always going to give you a number bigger than A and B, but you can end up with one smaller.

Speaker B
Right. And that's why Swift normally would trap and you have to opt out of that behavior specifically.

Speaker A
Yeah, very reasonable. Okay, cool. Thank you for checking me on that. So those are two of the ways you can add, but it turns out there's a third way that you can add, and there's a function called adding reporting overflow. And so what that will do is it will return a tuple.

Speaker B
There's a function on integer or on.

Speaker A
It'S on is it a binary integer.

Speaker B
Okay.

Speaker A
So that's like the protocol that represents int eight and 64 and 32 and so on. Right. So when you go to add, it returns a tuple, and the tuple has the overflowed value and then a true or false for if you need to carry into the next bit or into the next digit.

Speaker B
Okay.

Speaker A
So the way that works, if you add 202 hundred, you end up with 400 and subtract out 256. So you're ending up with I think like 134, 144 or something like that.

Speaker B
And this tells you that there's an overflow.

Speaker A
Has overflowed kind of spot. And so when that happens, then you know you need to go to the next array position and tick that up by one.

Speaker B
Totally.

Speaker A
Is that cool?

Speaker B
Yeah, that makes a lot of sense. And this seems like it would make implementing like big int actually pretty straightforward.

Speaker A
Yeah, it's actually not so bad. Division is weird and we'll get to it. But yeah, multiplication, addition, subtraction are all pretty straightforward. They kind of work the way you expect.

Speaker B
How does division work then?

Speaker A
Yeah, real quick. So subtraction gives there's a function that reports overflow and that's actually reports like if you need to borrow from the next column, essentially you do minus one. Multiplication returns to a high bit and a low bit. So multiplying two U into eight can never be bigger than a U into 16. So it'll give you the low byte and high byte. Does that make sense?

Speaker B
Yeah.

Speaker A
And then division got division. I actually have not figured out division yet. Part of it is because I've been trying to write big numb and big decimal at the same time. This is where I got stuck, essentially. And this is where I need help.

Speaker B
Okay.

Speaker A
So big numb, pretty straightforward big division, sorry, big int. Division is not crazy. So what you do is you say, okay, well, if I'm divided by zero, fatal error. If I'm divided by one, return the divisor or whatever. And if I'm being divided by something bigger than me, return zero. Those are the easy cases you can catch really fast.

Speaker B
Yeah.

Speaker A
Once you have caught those, then you got to do weird stuff. So you basically have to do long division. Let's say you want to divide the number 250 by five, right? So you try to divide this is.

Speaker B
In our hypothetical eight bit unsigned.

Speaker A
Imagine it as decimals. So imagine that you have base ten, you have an array of zero, five and two. So two is the hundreds place, five is the tens place and zero is the other place, the ones place. And you're dividing by five. So the first thing you have to do is you have to divide your first, your most significant bit, which is your hundreds place by the number that you're dividing by divisor, I think. And then you'll see that that is less than. So you add another bit to it and then you try to divide that. Yeah, see, this is where I get broken. Because your numbers are U int, you can't divide a U int by two. Oh, that's right. You can pass it for division. You can pass it a high bit and a low bit, I think for the dividing reporting overflow function.

Speaker B
Okay.

Speaker A
Or dividing full width is what they call it. Dividing full width.

Speaker B
Dividing full width. All right.

Speaker A
Yeah. So this gets real weird. Yeah. So you pass it a high and a low bit and that way it knows where it can borrow from basically. And then it will return to you a quotient, which is the result of the division operation, and a remainder, which is good. So then once you've done that, then you have to multiply them back together, multiply the quotient and the divisor together, subtract that from those two places and then you're left with zero. And so, you know, I'm not going to do long division on a podcast. It's crazy.

Speaker B
Yeah.

Speaker A
The point is it's really, really hard.

Speaker B
Yeah. I'm looking at the implementation in BigAnt Swift now and yeah, this is going to take me a little bit of thinking to work through what this is doing. Exactly.

Speaker A
Yeah. So the function is called it's like dividing internal divide or something.

Speaker B
I'm just looking at something called mutating.

Speaker A
Funk divide that I think is a different type.

Speaker B
I mean, I'm looking at a word.

Speaker A
The word that you're looking at is a word that so word is what Nate uses to mean like, each element in the array. So you can have a word of size eight, which is like a unit eight, a word of size one, which is a bit or a word of size 64. Right. And so he has additional implementations for words that are non standard sizes so that he can use like bit arrays and stuff.

Speaker B
Okay, but if you look for a.

Speaker A
Function called internal divide, that's the function that actually does the division and it is like bit shifting and like crazy stuff that I do not understand.

Speaker B
Yeah, I was looking at an implementation for a different word type, I think.

Speaker A
Yeah. So this is like crazy, crazy stuff at this point. You want to talk about weeds? This is the weeds. It is very wild stuff that happens here. So then there's like all this bit shifting that I don't really understand. Like temp RHS shift equals one. I don't know. It is crazy. I have not figured out division yet. And then to throw a monkey wrench in things, if you want to divide with the decimal places and you also have signs, let's not forget about signs. Right. If you multiply two positives, you get a positive. Multiply positive and negative, you get a negative. Multiply two negatives, you get a positive. So you have to handle that as well. That stuff's actually not so bad. I did that. But then when it came time to do this, I realized I'm storing things at base 256 and I was storing basically like an offset for where the decimal should go.

Speaker B
Okay.

Speaker A
And the problem is that let's say you want to represent a pretty normal number, like zero one. You can't represent zero one in base 256 without an infinitely repeating. Decimal place.

Speaker B
Sure. And this is a fairly common I mean, this is a common problem, right. Can you represent 0.1 even in base ten?

Speaker A
Base ten?

Speaker B
You can well, base in base two. No, there's some really just not unusual numbers that you just can't represent precisely in a floating point number. And that's just how it is.

Speaker A
Yeah, exactly. So one way to think about this is you can't represent one third in base ten without repeating numbers. Anything that's not evenly divisible by the base can't be represented without infinitely repeating decimals.

Speaker B
Right.

Speaker A
So then I was like, okay, well, that sucks. And then I kind of just started spinning my wheels. I was like, well, I could just store it out to 50 places. That's like probably more precision than anybody ever needs. I think that's like the amount of precision that that crazy, like, gravitational wave detector thing had, like just stored out to however many places that the precision is so accurate that could never possibly matter for any purpose that any human had that's one idea, or like and then parameterize that is the other idea. So that users could come in and say, okay, well, I actually want a big decimal that's parameterized out to 100 places because an array of 100 elements is not that it's not crazy. Yeah, that's fine.

Speaker B
So you're working your way here to implementing an arbitrary fixed precision sort of you choose your precision decimal type.

Speaker A
Right. One option was, okay, like, fine, it's going to be infinitely repeating, I'll just deal with it and just have a bunch of places out. So that wasn't really appealing. Then one option was like, what if I made an enum that had cases for zero through nine and then I conformed that to binary integer and I implemented like add reporting overflow and all that stuff on that because that'd be pretty easy, right? If you got like, you have a big switch statement and you say, if my two addition operands are eight and eight, then I would return a six, right, because it's 16 and I would report overflow, like, that's not so bad, I can implement that. But then each function needs like 100 lines in each switch statement because you have a grid of 100 by 100 or a ten by ten.

Speaker B
Right? Yeah.

Speaker A
So that implementation started getting really hairy really fast and I was like, can I code gen this with sorcery and.

Speaker B
That was the next question.

Speaker A
Yeah, so that was another crazy thing and eventually I was just like, this is crazy, what are you doing? So that's kind of where I am now.

Speaker B
Interesting. Okay, so I have a couple of questions. How are you testing this as you go along and as you work just unit tests?

Speaker A
Okay, this is actually a slam dunk case for unit tests, I think, because totally, yeah, you have a bunch of cases that you don't want to break while you solve new ones. So let's say my addition at first didn't handle positives and negatives. Once I added that behavior in, I was able to make sure my old tests still passed and my new ones passed, too, and it was, like, perfect for TDD.

Speaker B
Yeah, that seems like a textbook use case.

Speaker A
Absolutely. I'm dark. The one thing that you can't do is you can't test division, because that crashes. Can't test anything that crashes?

Speaker B
Yeah. Well, yeah. Once you get an implementation that doesn't crash, you can start testing it.

Speaker A
That's right. Well, but what I mean is, like, if you want to divide by zero, you want it to crash, and you can never confirm that that behavior always crashes.

Speaker B
Yeah, that's a good point.

Speaker A
So you could wrap it in a function that throws and make that, like, a testable function or, like, something internal, I guess. And then your externally visible public thing would crash whenever there's a throw. You know what I mean? Yeah, that's one option. But it's tough. That's a tough thing to hit with.

Speaker B
Testing testing things that actually throw fatal errors. Ding in swift is got you. There we go. Thank you. Is hard there's? Really not. I feel like a while ago, I had read an article somewhere where it might have been Mike Ash or someone equally smart, crazy went through how you can actually catch those catch things like fatal error or a precondition failure in tests and verify them. That's pretty cool.

Speaker A
If you find that, definitely send that to me.

Speaker B
Yeah, I'll look around for it. Maybe not while we're recording here, but I'll try to find that for you. And if I find it, I'll throw it in the show notes. The second thing that I wanted to note is not immediately related to Swift, but, you know, the origin story of OpenSSL, the cryptography library that a large part of the Internet relies on wasn't.

Speaker A
It made by some college kid? Is, like, just a project for fun or something?

Speaker B
I don't remember a college kid, but it originated because the guy or guys behind it wanted to play with big integer math.

Speaker A
Really?

Speaker B
Yeah. That is why this thing exists.

Speaker A
That is so funny.

Speaker B
Let's see here.

Speaker A
So clearly, my next step is to write a cryptography library.

Speaker B
Please don't.

Speaker A
Obviously.

Speaker B
At least that's the lore that I've heard. The Wikipedia article on opening cell project history is pretty sparse.

Speaker A
Well, if you find a source for that, that's really cool.

Speaker B
I'll bet I can find a source for that.

Speaker A
Yeah, that's cool, man. So my last idea on implementing decimal division is, what if I represented my number? Like, what if my big decimal were just a big int wrapped in use Nate's big int and wrap it and give it a decimal place in tens. Right. Decimal means ten.

Speaker B
Okay.

Speaker A
What that would do then is because the bigot knows how to represent itself as decimal, because that's also actually really hard to do if you have a base 256 number. Like if your word size is eight bits, one byte, you're printing out a base ten numbers. Really hard. That was like the first thing I tried to do. And then I realized actually really hard.

Speaker B
Yeah.

Speaker A
What you end up doing is dividing by ten repeatedly to get the remainders, and those remainders become your digits.

Speaker B
Yeah.

Speaker A
Wild.

Speaker B
And that's how you do it. There's no other way to do that.

Speaker A
There's no other way to do it. And so I was thinking I could treat Big Int as a black box that to me holds a decimal number, even though internally it can be implemented however it wants. And then I would store a decimal offset. And then adding is easy because you just need to add a bunch of zeros onto the end to make your decimal offsets line up. Right. So then once they add up, then you could just add them. Pretty straightforward dividing. Sorry, subtracting is equally easy. Multiplying, if I remember from grade school, you just multiply them as though they're integers and then add up the number of decimal places that you're offsetting.

Speaker B
Yeah, that's pretty straightforward.

Speaker A
And then division I can't remember what the rule is.

Speaker B
Yeah. Honestly.

Speaker A
And I got stuck there, too.

Speaker B
Yeah. Honestly. If you gave me like a pad of paper right now and asked me to do long division, the way I learned in what, like, fourth grade, you should try it.

Speaker A
You should really try it.

Speaker B
It seems like something I should be able to do.

Speaker A
Yeah, well, not only that, but it's just like it's in there. It's clanking around in your brain.

Speaker B
Yeah.

Speaker A
But you just haven't used it in 25 years or whatever.

Speaker B
Five into, say, 250. All right, I'll work on that after the show.

Speaker A
Yeah, there you go. And then with those decimal place, I just don't know what to do. So then maybe what I could do is big decimal could just be a big wrapper on big int and then done. You just have to keep track of the decimal place.

Speaker B
Yeah, I think could work. That makes sense. That could work. Yeah. It wouldn't be totally your own implementation, but there's no problem with it just building on code that works and is tested from someone else.

Speaker A
Yeah. And if I really wanted to be pure about it, I could say, okay, fine then. Now that I know that this strategy works, I'm going to finish my big gnome implementation, and then that way I will have written it and then wrap it for big decimal.

Speaker B
Yeah.

Speaker A
It's a bunch of really interesting problems. It is. I don't have any practical use for it, I guess, except for my fledgling.

Speaker B
Cryptography library, which, by the way, I found a source. Now, this is on the blog of a guy named Matthew Green, who's a cryptographer at he's really good, right? Yeah, he's really good. In the footnotes he says that the original version of this post repeated a story that a guy named Eric Young wrote OpenSSL as a way to learn C. In fact, he wrote it as a way to learn Big Numb division.

Speaker A
That's so funny. I respect that.

Speaker B
You're following in some great footsteps here.

Speaker A
All right, matthew T. Green will put him in the show notes.

Speaker B
Yeah. Sorry to interrupt. I'll throw a link in the show notes.

Speaker A
Yes, you should. That's really funny. That's great, man. Yeah. So that's basically all I have on big numb. I wanted to throw in one last thing, which is I can't say his name. The pinboard guy. Macha Shagweski.

Speaker B
Yeah. We all know and love him.

Speaker A
That's right. He basically said he didn't know anything about crypto, and so he went in and did this challenge. And so it's cryptopals.com, and it's provided by this company that does crypto stuff. And basically the first tier is, like, you have to implement Zor and you have to implement base 64 encryption, and you have to implement all these things. And then there's eight sets of eight problems, and you just do all of cryptography, like hashing, diffie, healthman, randomness, all of it.

Speaker B
Oh, this seems really cool.

Speaker A
So it might be really fun if I finish this Big Numb library to be able to then turn around to use that to solve these, because these have been on my list to do for, like, five years and I've never done them. I started them in Python.

Speaker B
Yeah, I remember seeing this a while ago, but never actually started them. I probably should because yeah, it's been a while since my undergrad security class where I learned about diffiehelman and RSA and even the internals of how hash algorithms work.

Speaker A
Yeah, I think it would be really useful because I did probably five of the first problems, like, five of the first eight, and I didn't really know how base 64 encoding worked. I know now because I wrote it.

Speaker B
Yeah. Well, that's a way to learn.

Speaker A
Yeah.

Speaker B
But yeah, this definitely seems yeah, I really should brush up on this.

Speaker A
Yeah. So maybe this could be, like, a little challenge and we could do this once a week or something.

Speaker B
Yeah, that could be fun.

Speaker A
Yeah, something like that. Maybe two problems a week. That could be a new podcast. Yeah, that's actually a really good idea for podcast.

Speaker B
It might be. Or we may end up talking through our implementations of, say, AES in ECB mode.

Speaker A
Well, we can talk about why that's useful. I don't really know why that's useful, so I don't know. Could be cool. Maybe we should talk about that.

Speaker B
Yeah.

Speaker A
Other than that. Yeah, that's what I want to talk about. About big NUMS.

Speaker B
That sounds like a fun project and definitely good learning experience.

Speaker A
Yeah.

Speaker B
I'm curious to hear I'm curious to see how the rest of this goes. Are you planning to put the source up anywhere once you get this all working or is this purely like a.

Speaker A
Personal the source is up.

Speaker B
Okay, cool.

Speaker A
It's my GitHub handle plus big decimal, but it's not working. It's like division obviously is not implemented and I think multiplication mostly works. Oh, I was doing multiplication with I was starting to solve the decimal offset problems. Like, I can do normal integer multiplication, but I was handling the decimal offsets. That doesn't work yet and the division is not done at all. Adding and subtracting should be good. Equatability should be good. I need a bunch of helpers, like convert to and from the normal types that we traffic in and like integer literals and float literals and stuff like that. Converting from floats to infinite precision. Decimals can be really hard.

Speaker B
Yeah. Do you mean infinite precision or like arbitrary precision? Like you pick your whatever precision you need.

Speaker A
I don't know the difference, to be totally honest with you.

Speaker B
Well, so if I want to convert a float to whatever type you're designing, do I need to say, like, I want to convert this to I want this number and I want it precise to N, like places or are you trying for an exact representation?

Speaker A
I think I'm trying for a representation that's so exact, obviously it can be infinite because you can't store infinity, infinity threes if you want to store one third, but so precise that nobody would ever want anything more precise that's a.

Speaker B
64K would be enough for anyone.

Speaker A
But there is some level of precision that's like, okay, this is actually enough, isn't it? Like 30 digits of pi is enough to calculate the circumference of the universe to a golf ball or whatever.

Speaker B
I can't say I've ever heard that specifically, but who knows?

Speaker A
Digits of pi to calculate the circumference of the universe? I have a siren. Yeah, if you have 39 digits of pi, you can calculate the circumference of the observable universe to a hydrogen atom. Do we really need more precision than that?

Speaker B
Well, it depends what you're doing.

Speaker A
Yeah, that's true.

Speaker B
Maybe if you want to calculate the circumference of the universe to within a quark, you're going to need a lot more decimals.

Speaker A
Yeah, that's true. One thing I really like is you know how GPS numbers have like something after the decimal place?

Speaker B
You mean coordinates?

Speaker A
Yeah. Sorry. GPS numbers.

Speaker B
Just want to make sure we're on the same page. Yeah.

Speaker A
So GPS coordinates have like a decimal bit, right? Part of it's in decimal. And so the thing that it's actually really intuitive once I thought about it, but I hadn't thought about it. So if you have five places, it's enough to be precise to like 30 meters. If you add a 6th place, that means you're ten times more precise. That means you're down to 3 meters. I'm making these numbers up, but it.

Speaker B
I was going to say, I think five decimal places way more precise than 30 meters, but yes, I take your point.

Speaker A
Yeah. And then if you have seven decimal places, it goes from 3 meters to 30 is a foot. And then if you go ten more than that, it's 3 CM. You almost never need more position than that. Like, if you're driving a car, you don't need seven digits of GPS coordinates.

Speaker B
It depends. Autonomous cars, right?

Speaker A
No, I think the military has really precise versions of GPS that are important to be. Here we go. If you have six decimal places, that's precise to 111 mm. So 10 CM for six decimal places. Five decimal places is 1.1 meter. Four decimal places is 11 meters. But obviously it makes sense that if you add one more digit with ten units of precision, you're going to get ten times more accurate. But I hadn't really thought about that. I thought that was pretty cool.

Speaker B
I do always laugh when you go to I think even Google Maps at least used to do this. But you go to like, a Map something, or you use an API to geocode an address or something, and it gives you the answer out to like, 15 decimal places. That's awfully precise. Identify the position of a speck of dirt on the roof of my house.

Speaker A
So the point is, how much precision do we really need? 50 enough, I think 50 is probably enough.

Speaker B
For this project. It's probably enough, yeah.

Speaker A
If you have eight decimal digits of precision for your coordinate, you can measure things down to 1. It's good for specialized surveying, such as Tectonic plate mapping.

Speaker B
Yeah, there's some interesting techniques that they use to get GPS to down to that level of precision. Actually Google, I think. Waas wide area augmentation system. Yeah. Anyway, look at those.

Speaker A
Well, that's homework for next time.

Speaker B
Yes, this is homework for next time. Oh, and then you have Laas local area Augmentation system as well. So these are things that we use, I guess, mainly in aviation to give airplanes and aircraft with very precise position information.

Speaker A
Interesting.

Speaker B
Including very precise instrument landing capability. Anyway, it's cool stuff. Thank you very much, Patreon people, for your support.

Speaker A
Yes, we do appreciate it.

Speaker B
We appreciate it. And we'll talk to you next week.

Speaker A
See you, Chris.

Speaker B
Bye, sirish.

