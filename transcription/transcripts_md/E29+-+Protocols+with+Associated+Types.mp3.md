Chris Dzombak
I'm looking at the generics manifesto and looking at the section on, like, opening existentials, and this still looks clumsy. So I'm wondering, what does this look like in Haskell? But we don't have to cover that right now.

Soroush Khanlou
I think they're type classes.

Chris Dzombak
So protocols with associated type are called type classes in Haskell, which I feel like maybe a more useful way to think about it. We should probably start the show. Show.

Soroush Khanlou
Let's start the show. Hello and welcome to Fatal Error. This is episode 29. I'm, sirish. Khanlou.

Chris Dzombak
And I am Chris De Zomback.

Soroush Khanlou
So this is the last episode of our second season that will be public. There'll be one more private episode, Patreon only, which will come out next week. But this is the last public episode of the season. We'll be taking six weeks off after that next Patreon episode, and then we'll be back with season three. Maybe slightly different format, maybe different topics. Who knows? Could be anything.

Chris Dzombak
Yeah. Back when we decided to start doing this podcast, we pretty arbitrarily decided to do is it 20 week seasons that we landed on?

Soroush Khanlou
Yeah, it's 20 weeks on, six weeks off, which works out perfectly to a half a year. Right, so we can do two seasons per year.

Chris Dzombak
And we chose this just because I especially was a little bit skeptical of committing to doing this full time. And we figured that seasons would give us friendly stopping points if we ever wanted to stop. We're still planning to have a season three here.

Soroush Khanlou
We don't want to buy the lead. We hope there will be a season three. We're coming back.

Chris Dzombak
Yeah, absolutely. We'll be back. We're just taking a little bit of a break.

Soroush Khanlou
First season experiment was the podcast itself to see if anybody even liked it. And second season was this whole Patreon thing, which is almost making like $400 a month on Patreon, which is great. And so that's like covering our editing costs, which has been really nice. And season three, what are we going to do?

Chris Dzombak
Who knows?

Soroush Khanlou
It could be anything.

Chris Dzombak
Yeah. And on that note, if you, our listeners, have suggestions on what you would like to see us do in season three, if you want to see us continue to do more of the same, if you want to see us branch out into some different topics or different formats, please let us know. We're happy to hear from you.

Soroush Khanlou
Definitely. Absolutely. So, Chris, what do we want to talk about today?

Chris Dzombak
So today we thought that a nice, easy subject for us to cover.

Soroush Khanlou
Let's keep it real light. For our last episode would be protocols.

Chris Dzombak
With associated types, which are something that will be familiar to people who've been doing especially some more quote unquote, protocol oriented Swift programming because they come with some sharp edges that you run into pretty quickly. And we thought we'd kind of dive into this subject today.

Soroush Khanlou
Yeah, I feel like when you're writing Swift, in the beginning, you render a lot of errors. Most of the errors are fixable, but what is it? The protocol with associated types can't be.

Chris Dzombak
Used can only be used as a generic constraint.

Soroush Khanlou
Yeah, that's the one. You hit that and you're just like, well, I guess there's just nothing I can do here. I have to totally rearchitect everything.

Chris Dzombak
And it sucks because you kind of do like there's no fix it, there's no quick fix to apply there. It's not that you did anything wrong. Right.

Soroush Khanlou
Yeah. It's just stuck, I guess.

Chris Dzombak
A good place to start. And this is a subject that I think you, sirish, are a little bit more knowledgeable about and more comfortable with than I am. So do we want to start and let's maybe just cover briefly what a protocol with an associated type is.

Soroush Khanlou
Yes, that would be good. Do you want to take that or should I take a crack at it?

Chris Dzombak
I mean, I can take a crack at it. So this is a protocol which is somewhat different than normal protocols than you might write. And it's different than protocols you would write in objective C because it forces whatever conforms to the protocol, whatever class or struct conforms to this protocol, to have a type alias embedded in it. And that type alias is sort of a placeholder at the protocol level. But when you adopt the protocol, you have to assign this placeholder to be a specific type.

Soroush Khanlou
Right, exactly. The keyword that you use used to be type alias, which was insanely confusing, and now it's a different keyword. The different keyword is associated type.

Chris Dzombak
Oh, that's right.

Soroush Khanlou
So once you, let's say you create a protocol that has one of these associated types, when you sort of conform to that protocol, you can very explicitly write within your concrete class, you can write type alias. The name that the protocol expects equals the concrete type that conformance is providing. You can write that explicitly. Or if you just use it in the bodies of your functions with the actual concrete thing, it'll just kind of figure it out and it'll just work.

Chris Dzombak
Right. That's an important thing to note is that you can sort of implicitly declare what that associated type is.

Soroush Khanlou
Right, yeah, that's what I tend to do.

Chris Dzombak
Yeah. The place that this probably most comes up or most frequently comes out, would be the equatable protocol.

Soroush Khanlou
Yeah, this is definitely a big one.

Chris Dzombak
It's part of the Swift language. And at some point, you may well find yourself declaring that for some reason you want your protocol to also conform to equatable.

Soroush Khanlou
Right, right.

Chris Dzombak
And then you go to declare that something is an instance of your protocol and you get this error because equatable, the protocol has the associated type or has the associated type of self, which is just a placeholder for whatever concrete type is conforming to the equatable protocol.

Soroush Khanlou
Right. So far, so good.

Chris Dzombak
But that's still an associated type. And so you can't use a protocol that conforms to equatable just by itself. Like as a type for a variable in your program.

Soroush Khanlou
Yeah, exactly. So even though you're providing the conformance for equatable based on only the things that are provided in your protocol, the Swift type system doesn't really know that, and so you can't use it. I think with equatable, there's a slightly simpler construction of the problem that makes it more obvious. Okay, let's say you have a person object that's equatable, and you have a house object that's equatable, and then you want to assign one of them to a reference. That where the type is explicitly marked as just equatable. As soon as you do that, the system will crap out on you and say, hey, you can't do that.

Chris Dzombak
Right.

Soroush Khanlou
And the reason that you can't do that is because, let's say you have two of those equatable, two references to two equatable things. If you go to try to call equal equal on them, it won't know what equal equal implementation to use. Let's say one of those is a person, one of those is a house. It has no implementation to use because houses can't be equal to people, and so that function just doesn't even exist, and it just wouldn't be possible. So to prevent that from being an issue, the Swift sorry, the Swift type system just prevents you from being able to create references to something that is just equatable by itself.

Chris Dzombak
Right. And so I think right before the episode, I was kind of thinking along the lines that I know very little about Haskell, but Haskell calls protocols with associated types type classes. This represents the same concept. And as you were describing equatable here, this kind of intuitively makes sense. Like that name almost intuitively makes sense because equatable doesn't really describe a type on its own. It describes like, a family or like a class of types that have this property that they're equatable. Right, yeah. The associated type, that self requirement. If the only thing you know about something about two things are that they're equatable, you can't say that they're the same thing. All you know is that they're in the sort of equatable family or equatable type class.

Soroush Khanlou
Right, right.

Chris Dzombak
So I was thinking, like, in preparation for this episode, I was watching Alexis Gallagher's functional Swift conference talk about protocols with associated types, or pats, as he calls them. And one of the things that he mentioned was in Haskell, or a paper that he mentioned mentions that in Haskell these things are called type classes. And I think that is almost a more intuitive name.

Soroush Khanlou
Yeah, I have trouble with the Haskell, especially that name, because type is a thing already in the world we live in, and class is a thing. And what does that make type class?

Chris Dzombak
Family.

Soroush Khanlou
Yeah, that's not bad. I like that. But it's just like naming is hard.

Chris Dzombak
Types all the way down.

Soroush Khanlou
Yeah, it's just types all the way down. Yeah. So definitely that Alexis Gallagher talk. I think he really breaks down exactly what's going on with this problem. We're going to try to do a good job as well, but we tossed a link to that in the show notes and Alexis does an excellent job of breaking down what is going on with this.

Chris Dzombak
Absolutely.

Soroush Khanlou
With this problem. Another place that you might run into this, and probably the place I have the most experience with it is in the sequencing collection stuff. So if you ever try to you're working with some stuff, some arrays, and you're mapping and filtering and lazing and all that stuff over these arrays and you end up with some weird type and you're like, you know what, I don't really care that this is a lazy flat map sequence. What I do care about is that this is just some sequence and you would love to be able to write like this function returns a sequence and sequence is a type within the system. And so you go to write that and it says, well, hey, you can't do this because what's the error? Again, protocol XYZ can only be used as a generic constraint because it'll self or associated type requirements. The associated type requirements in sequences case are the iterator and then the iterator has its own associated type for the elements. And again, you can kind of imagine why this is a problem. If you just say, hey, I'm returning a sequence. You're not saying which sequence, you're returning a sequence of what? What are those objects going to be? And because you can't express that in the type system at this moment, you can't return a regular sequence. So you have to either transform it into an array or give it the actual concrete type or use something called a type eraser, which in this case would be called any sequence, which is a special concrete type that is generic.

Chris Dzombak
So what is a type eraser?

Soroush Khanlou
Right, I'm very glad you asked. There is also a good talk by a friend of the show, Gwendolyn Weston from Triswift last year, explaining type erasers. We should throw that in the show notes. But essentially the idea is type erasers are good for two things. One is if you have a really crazy nested type. Like you have a lazy flat map sequence of an element and let's say a string and a zipped sequence of an integer, and it's like this crazy long type. And it's that way because of implementation details and you want to hide that long thing and not have to type it out. You can do that. And the way that you do that is basically wrapping it in an any sequence which will it'll treat it as just a generic sequence and let you sort of return just that. Any sequence instead of the long complicated type that's use number one.

Chris Dzombak
How does that work? Like, what does any sequence actually look like?

Soroush Khanlou
So under the hood, what it does is and this is like the really messy part, and if you want to make your own type racer, you have to do this. But basically it has properties for each of the functions on the protocol. And when you initialize it with the sequence, it will copy the implementations of that sequence to its own property, which is like a block, and then it will execute that block when it's the right time. And that kind of just works.

Chris Dzombak
That's really messy. Like you end up duplicating the entire interface inside your eraser.

Soroush Khanlou
You sure do.

Chris Dzombak
Well, that's unfortunate.

Soroush Khanlou
Yeah, so it works really well. If there's very few, very few methods and properties on your associated type, that is a way that can work.

Chris Dzombak
Is this something you could code gen?

Soroush Khanlou
I was thinking the same thing. I think it's possible. I don't think it'll be easy. So, fortunately, a lot of the protocols that are baked into the system, such as sequence collection, bi directional collection, they have their own or like index as well, they have their own corresponding type erased things. So there's any sequence, any iterator, any bi directional collection, any collection, any index and so on, any hashable. I don't think there's any equator.

Chris Dzombak
Well, I was just going to say, I assume that this only exists for types in the standard library where it makes sense to have a type eraser. What would you do with a type eraser for equatable? Right.

Soroush Khanlou
You have to give it a concrete type of what the self is, so it wouldn't be that useful. Right. So you would say any equatable, and then in brackets, you'd put like house or person or whatever. And that's not that much better than just writing house or person. So kind of, who cares? So I think for protocols with self requirements, it's not a big deal. It's for protocols with associated type requirements that this is super useful. So any hashable, any iterator, all those things are kind of built in. They're already written for you, you can kind of take advantage of them. They can be a solution to this problem. Yeah, that's a type eraser. Okay, just to sum up, it's either to shorten some really complicated long type name that has a lot of nested stuff in it, or it's to basically be able to return a sequence. Like you can't do that before. So you return any sequence that is generic over the type that the sequence should be bending.

Chris Dzombak
Okay.

Soroush Khanlou
Those are the two uses.

Chris Dzombak
So things that you can do when you run into this error, you can use type erasers. If you're trying to use something that's a protocol that has an associated type, you end up needing to make the class or the structure that uses that protocol. It also ends up having to be generic. Right. And I guess you see that with type erasers because those end up being generic, right?

Soroush Khanlou
Yes.

Chris Dzombak
Okay, what else, if anything, can I do when I run into this problem?

Soroush Khanlou
There's two other approaches. One is, so protocols are essentially subtypes, right? They are either this or that. Swift has another system in place for doing subtypes, and that's enums, because enums know all of their concrete types at sort of compile time. They know everything that they can be. You can also use an enum. If you can switch up your protocol and replace it with an enum, then you know all the types of everything all the time, and you can just use that. That's one other option is switch out your protocol for an enum.

Chris Dzombak
So I want to call out a few things here. First, that solution assumes that you know what everything that conforms to your protocol is.

Soroush Khanlou
Yes.

Chris Dzombak
So protocols have the advantage, obviously, that anyone anywhere can adopt them. And so this isn't really a viable solution if you're building a library. It's a solution if you're building an application and you have some finite number of types that you wanted to conform to this protocol.

Soroush Khanlou
Yeah, exactly. So for example, you can conform to a protocol across module boundaries, but you can't add an extra enum case across module boundaries.

Chris Dzombak
Right.

Soroush Khanlou
And that's part of the reason this whole problem goes away, is because if you know everything that it can be, it's just easier to deal with all the types and stuff.

Chris Dzombak
The other thing that I wanted to call out was use the phrase some types, and we didn't define that term. So let's go ahead and define that.

Soroush Khanlou
Yeah, okay, cool. So basically there's some types and product types, and I'm not going to do a good job explaining this over the air. I think product types are like structs where the state space of a thing is all of the different possible values for each of the properties multiplied together. So if you had three booleans in a struct, like boolean A, bullying B, bullion C as three different properties, you would multiply two, because each boolean can be in two different states. Times two for the second one, times two for the third one, and you end up with a state space of eight different possibilities. That eight different states that this struct can be in.

Chris Dzombak
Okay.

Soroush Khanlou
On the other hand, if you have an enum, it's called a sum type because you can sum the potential different values. So if you had three different cases, each with an associated boolean, you would have six different potential states that this thing could be a two plus two plus two. So it can either be in case A, which case A of true, case A of false, case B of true, case B of false, or case C of true in case C of false. There's like these mathematical things. It's like an abstract data type and blah blah, and go read Brandon Williams blog and he'll teach you all that stuff. I'm not very good at it, but essentially it just represents this thing can be like this, or like this, or like this, or like this, whereas a product type is more like this thing and this thing and this thing and this thing.

Chris Dzombak
So as a type grows, a sum type grows with the product of different states that its properties can be in, and a sum type grows with the sum of the different states that it's say, like different cases and associated values can be in.

Soroush Khanlou
Yes, exactly. Okay, all right, so basically, Protocols and enums can kind of fill this role essentially the same way, so they both can act as some types. So if it's possible for you to switch away from protocols and towards enums, you could do that. That will solve your problem. I also forgot this. There's another system of some types within Swift which is subclassing. So if you use polymorphic inheritance and you just subclass stuff, that is also a subtype, because it's either of this type or of this type or of this type, and those don't run into the same generic, they run into different, slightly different generic problems, but they're not nearly as insurmountable as generic constraints as associated types, rather. Okay, you can use subclassing as well. So basically the first solution to using, like, if you run into this error is use a type eraser. Second solution is use a different subtype, either enums or Subcrossing. I literally almost forgot Subcrossing because I push it out of my head as an option at pretty much all times.

Chris Dzombak
Yeah, I tend to not use subclasses of things other than UI kit classes.

Soroush Khanlou
In switch programming, pretty much when you have to.

Chris Dzombak
Yeah.

Soroush Khanlou
Then there's one more thing you can do to deal with these errors, and it's kind of in the in error itself. It says protocol whatever, can only be used as a generic constraint because it has associated type requirements. So what is this generic constraint? So you can say when you're defining an extension, when you're defining a class, when you're defining a function, hey, I expect to be using this type and this type should have these qualifications or constraints. So that's like when you create a class and you have subject type like T, and you say where T is like this and T is like that, and T is like the other thing, and so you can actually use those to tell the type system. If you know that I'm working, let's say, with a sequence, and if you know that the items in that sequence are strings, then please make available this function. For example, this is really hard to talk about on a podcast. I think I could take a stab at it if you like. I have some concrete examples, but.

Chris Dzombak
We can take a stab. And if you can do it without just reading code at me.

Soroush Khanlou
Yeah, let me try here. So the way that I would approach for this approach, this is basically to say you can bridge the gap between these associated type constraints and true generic programming in Swift by using these where clauses. So, an example of this, I have one that I use, but it might be a little hard to explain.

Chris Dzombak
Eric, maybe if we can also come up with an example to put in the show notes, that would be good.

Soroush Khanlou
Yeah, I don't think I could reasonably explain this over a microphone. Essentially, the concept is that you change any of your associated type requirements into concrete requirements at compile time. So you basically say at compile time, you will know what this is and use a special generic version of this class or this function that is specialized for this version of the protocol.

Chris Dzombak
Okay, we should come up with an example to put in the show notes of that.

Soroush Khanlou
Yeah, I will try to think about a simplified example. It's a little bit tough to explain.

Chris Dzombak
Okay, let's move on from this right now and maybe talk for just a minute about why we have these protocols with associated types instead of having just like generic protocols that look a lot like generic classes in Swift. Right, because that is something that the language designers could have chosen.

Soroush Khanlou
Yeah, I don't have an answer for that, to be totally honest. Do you have an answer for that?

Chris Dzombak
I think I do, and I can try my best to explain it here.

Soroush Khanlou
Cool, hit me.

Chris Dzombak
So protocols are something that it's very possible that you may have multiple associated types on one protocol, right. And you may have a class or some function that deals with multiple protocols, right?

Soroush Khanlou
Right.

Chris Dzombak
Each of those protocols could also have one or more associated types. And so if those protocols were genericized in the way that classes are, everyone that tries to work with those protocols, like when you're trying to write your declaration that this function takes whatever generic protocol you're working with, you end up having to I don't know exactly what the right word is. You end up having to expose or having to deal with or almost to duplicate or to declare those generic constraints everywhere that you're declaring that, for example, you're writing a function that works with this type.

Soroush Khanlou
Right.

Chris Dzombak
And as you add more protocols and more associated types to those protocols, that gets really hairy really quickly. Going back to Alexis Gallagher's talk. He is a good example of what this looks like when this starts to blow up in Java and he compares it to what it looks like in I forget two other languages. One of which is haskell and one of which and C plus plus both of which have things that are kind of like protocols with associated types. And it looks generally better. It doesn't blow up in the same way. I also have an example which I'll add to the show Notes, which is a web page discussing Scala and it's a blog post. Just trying to answer the question, when should you use basically an associated type instead of generic type parameters? Because Scala will support both of these different approaches. And this also has an example of how things start to blow up pretty quickly when you're using the quote generic protocol approach.

Soroush Khanlou
Got you.

Chris Dzombak
Instead of associated types.

Soroush Khanlou
So a concrete example of this would be like if you wanted to make a, if you want to refer to a generic collection, you would have to define its index type, you would have to define its subsequence, its iterator, its iterator's element. You'd have to define all this stuff inside the brackets. And because that would be so messy, it's just like you're not allowed to do that.

Chris Dzombak
Yeah, it just would become fairly unusable pretty quickly. And again, I can't recommend enough for many reasons that our listeners go watch Alexis Gallagher's talk because he has some good examples of this.

Soroush Khanlou
Yeah, he really cracked open the whole thing.

Chris Dzombak
Really just stop listening to this episode and go watch that talk.

Soroush Khanlou
That's right. So if I could hit you with the softball question, is there anything in Swift's future that we could potentially use to solve this problem?

Chris Dzombak
Boy, I'm glad you asked. So in the Swift repository, there's a generics manifesto which covers features that are generics related that the Swift maintainers would like to add to the language at some point. And one of the features on this list is generalized existentials. And I don't really know what existentials mean exactly, but the idea here is that this feature would provide a way for you to declare, for example, one of the examples relates to sequences. You could say that you have a sequence where it's iterator element is string and you end up having to put some things in brackets, but this would still allow you to use these protocols that have associated types in the way that we think of normal protocols, which would be really nice.

Soroush Khanlou
Yeah, and they also have this nice little type alias down here of like maybe a future feature is that we could type alias this thing and get any sequence not as a struct, as a type eraser, but as really a true reference to that generic size exercise.

Chris Dzombak
And that would be really nice. This would remove a lot of boilerplate that comes along with implementing type erasers right now.

Soroush Khanlou
For sure.

Chris Dzombak
This is something I would love to see in the language. I don't think that we're going to see it in Swift Four, maybe Swift Five.

Soroush Khanlou
Swift Four is like coming out in four months, right?

Chris Dzombak
We would know. If this were coming in Swift Four, we would know. And it's not. But it would be really nice because this would allow you to declare what you kind of intuitively think you should be able to declare that this is a sequence, any sort of sequence of strings. Right. That makes a lot of sense.

Soroush Khanlou
Yeah, for sure. Just a little side note on this generics manifesto. I go back and reread this about every month or every six weeks, and I learned something new every time that I didn't catch on my first read through. And so I highly recommend, even if you've read it before, read it again. Read it again in a couple of months, and as you do more Swift, more of it will make sense to you, and I can't recommend it.

Chris Dzombak
Absolutely. Yeah. Every time I reread this, there's something else that I learned that I didn't get before. I still don't understand everything in this document, but it's good to read through and notice, oh, this kind of makes more sense than the last time I read this.

Soroush Khanlou
Yeah. Definitely something that it pays to reread it.

Chris Dzombak
Yeah. So let's see, what else did we want to cover?

Soroush Khanlou
That's pretty much all I wanted to cover.

Chris Dzombak
Yeah, I guess so. I guess I don't really have anything else to add. I have a few other links that I'd like to throw in the show notes that relate either to understanding associated types in more detail or relate to understanding type erasers in more detail. These are, I think, good references or good things to read through. If you're curious, if you want to try to understand this stuff a little bit more.

Soroush Khanlou
Nice. Yeah, toss them in. I'd like to read them.

Chris Dzombak
This is stuff that I come back and reread with some frequency because I'm still a little I guess I understand what's going on here, but I don't know. There's it's a little bit complicated. Like, it's like going back and rereading the generics manifesto, like, really wrapping your head around this and making sure that it stays fresh in your head is a little bit of a challenge.

Soroush Khanlou
Yeah, absolutely. I think that maybe wraps it up for this episode. It's a complex topic.

Chris Dzombak
Yeah, it's a complex topic. I hope that this podcast, or at least the show notes, are somewhat helpful for all of you, our listeners.

Soroush Khanlou
It's definitely worth knowing about. It's definitely worth learning about, because if you write Swift, I think I hit this within maybe two or three weeks of starting to write Swift. And I was like, what is this thing?

Chris Dzombak
Oh, yeah.

Soroush Khanlou
And yeah, you just hit it immediately. So it's good to know about it. It's good to know about the different things you can to avoid it. Yeah.

Chris Dzombak
Thank you so much for listening, everybody. It's been an exciting 29 episodes.

Soroush Khanlou
Yeah, it's been really great. We'll catch you in the next season. I'll talk to you soon, Chris.

Chris Dzombak
We'll see you later, sir.

