Speaker A
Hi everyone. Welcome to Fatal Error. I'm Krista Zomback.

Speaker B
And I'm Siresh Khanlou.

Speaker A
And this week we decided we were going to talk about the Ownership Manifesto. Sirous.

Speaker B
What's?

Speaker A
The ownership manifesto?

Speaker B
Oh boy, you're just going to throw me right into the fire on this one. So we gave ourselves homework to read the Ownership Manifesto and try to understand the Ownership Manifesto. I was marginally successful, so okay, so.

Speaker A
Really high level, what is the Ownership Manifesto? Right, this is a document that the Swift language team put out. When did they release this? Like months ago. This is not a very new document.

Speaker B
Yeah, it's a bit old. It's I think about a little less than a year old.

Speaker A
Yeah, I think that sounds right. So it outlines the Swift team's plans or thoughts about adding a different approach to memory management in Swift that you can opt into for certain kinds of programming where the sort of reference counting model doesn't quite cut it. That's a fair description, I think.

Speaker B
Yeah, I think so. There are a lot of parts of it that I didn't understand. The parts that I did understand were basically we write this code and we don't have that much control over when the retains and releases get inserted. And especially, I think when working with collections and stuff like that, you end up having two owners of the same object. And when you have two owners of the same object, you may end up creating a copy when you don't actually need to. And so this is about basically giving hints to the type system and to the compilers to say, hey, this is just a certain kind of reference and it doesn't necessarily need to make a full copy because of X, Y and Z reasons.

Speaker A
Yeah, I think that's that's generally it. If can I can I take a stab at defining the problem too? For sure. So right now, the way that Swift and the way objective C works, at least with Arc, right, is it assumes that anytime you're using an object, anytime you have a pointer to some object in objective C, anytime you have a reference to some type in Swift that you have what I would call an ownership interest in that object, Meaning Swift will keep it alive for you. Swift assumes that you are an owner of this object and does that by incrementing reference count while your reference to it is alive is in scope.

Speaker B
Right, right.

Speaker A
And in some cases, I mean, especially with value types, that involves not that's not actually what happens because it's not reference counted. Like you end up making extra copies of Structs because the compiler and the optimizer have to assume that you might do something that requires your own copy of this value. It has to assume that you do actually want some sort of ownership of this value and it has to very conservatively copy things and very conservatively increment reference counts. Right.

Speaker B
Yeah. It can't know otherwise.

Speaker A
Yeah. So I'm glad that you mentioned you had some trouble reading this, you're understanding this full document because I did too. I read various parts of this document several times and still came away a little bit fuzzy on some of the details. And I think that's because it's a pretty in the Weeds language and compiler sort of engineering document, I think there are a lot of details and I don't think that it actually does a great job of introducing high level concepts. So can I go over two things that really helped me get, I think, some of the higher level concepts here?

Speaker B
Yes, absolutely.

Speaker A
So in some Googling earlier today, I found someone whose GitHub handle isner yeah, Alexisner, I'm so sorry. Put together a really nice TLDR on the Ownership Manifesto that I think distills some of the important high level points and some of the important details into something that's way easier to understand. And I actually went through and I haven't really used Rust very much at all, but I went through the Rust Programming Languages manual and read the section on ownership and on borrows, which is Rust's approach to solving the same problem. And that did a really good job of going through the problem and going through the sort of core concepts and going through the Rust languages solution in a good amount of detail, but in an understandable way. And then I was able to go back to the Ownership Manifesto and then go back to this TLDR and kind of have a better idea what's going on. And we'll include links to all of these in the show notes. But if you're really trying to understand this like I was and like I still am, I definitely recommend this approach. Like, read through chapter four of the the Rust Language manual that we'll put in show notes and then go ahead and read the Swift Ownership Manifesto.

Speaker B
So for a little bit of context, how much Rust have you written?

Speaker A
I've written approximately maybe five lines of Rust.

Speaker B
Okay, cool.

Speaker A
Yeah.

Speaker B
It may be the kind of thing where if you don't write any Rust, because I remember trying to read this back in the day when there were just whisperings of like, oh, Swift is going to do a new memory management model based on Rust. So I tried to go back and read that stuff and it was completely inscrutable to me. It might help to read some to be able to read and write a little bit of Rust before you read that.

Speaker A
Maybe. Although it says in a red box here, I'm reading a draft of the next edition of the Rust Programming Language, so maybe things have gotten better.

Speaker B
Got you.

Speaker A
I know that the Rust community has been putting a lot of effort into documentation and into really helpful compiler error messages. And if you're reading through this manual, you'll see some of those error messages and it's really nice. So right, backing up if you're reading this, you'll see, like, Rust doesn't use reference counting the way that Swift does. Rust pretty much just has values and objects that are on the stack or that are partly on the stack and have pointers to memory in the heap and everything in Rust is managed through this ownership model. Do we want to try to do a high level overview of what an ownership model actually is and how that contrasts with reference counting?

Speaker B
Yeah, I think that makes sense.

Speaker A
So, like I said earlier, with reference counting and with the way that Swift handles value types with fairly conservative and pessimistic copying of value types under the hood as values get passed from scope to scope and fairly conservative reference increments as references to objects are passed from scope to scope. That obviously can be inefficient depending on what you're doing. And it's possible with Rust and under the strategy outlined in the Ownership Manifesto for you to more directly tell the compiler and the optimizer what code sort of owns a piece of data at any given time. And that means that that code is the code that's responsible for getting rid of that data, de allocating that data, or deallocating the underlying memory if that's necessary. Or if we're talking about a file handle, like closing that file handle at some point in the future. And we do that by or this proposal suggests doing that by adding a few keywords to the language, mainly that you don't have to use. But if you're writing code that can benefit from this sort of thing, you can use to say, hey, I'm giving this other function this piece of data and sharing it, but I'm retaining ownership. Or a function can say, hey, I take a piece of data in and I take ownership of this data from the code that is giving it to me. And there are some requirements that come along with that that we'll talk about. This is the law of exclusivity that they mentioned. But that's sort of the overall idea is just to let you be more explicit about what piece of code, about what scope owns underlying data or underlying memory or some shared resource at any given time. And that lets the compiler and the optimizer not make these conservative assumptions that may result in a lot of reference counting overhead or a lot of copying values overhead. That's a lot of talking. Did that make any sense?

Speaker B
No, it definitely made sense. I'm curious about one thing, which let's just dive in. They have this shared keyword and you can describe a function argument as shared, right? You can say, when you give something to me here, it should be shared. Is that kind of like an unsafe reference? It's like, I'm going to work with this code, but I'm not the owner of this thing.

Speaker A
No, it's not like an unsafe reference because if you pass something to a function that takes a shared parameter, then that thing is immutable. So that function can't mutate that shared parameter at all.

Speaker B
Got you.

Speaker A
And in fact, the code that is sharing that, that is like retaining ownership, but sharing that value or that reference.

Speaker B
Also can't mutate it.

Speaker A
Also can't mutate it. And that goes to this law of exclusivity that they described fairly early in the document.

Speaker B
Got you. We should definitely come back to the law of exclusivity. But definitely. So there's basically owned, which is the default of every parameter, is basically owned. You could write it explicitly, but you don't have to. Then there's shared, which means I'll read from this, but I won't write to it. Right. And then there's also in out, which continues to behave the same way as in out does today, which is not only will I maybe mutate this thing and need my own copy of it, but I also may mutate this like the reference itself.

Speaker A
Exactly. Yeah. So in out still behaves as before, and owned is just like how everything in Swift works today. More or less.

Speaker B
Got you. Yeah. And then shared is just I promise I won't mutate this, I just want to look at it. So one example they give in here is if you're defining equal, equal for two values, you can describe that as shared because you don't need to do anything but look at it.

Speaker A
Right. And in fact, it's not just that you promise you won't modify it while someone else has a handle to it, the compiler and the runtime will actually enforce that immutability property.

Speaker B
Right, that makes sense. Yeah.

Speaker A
So now that we're sort of dancing around the edge of this, do you want to go over the law of exclusivity briefly?

Speaker B
Yeah, I think that's really important.

Speaker A
So they propose adding this law to Swift that will apply to all Swift code, but will really only affect it will only negatively affect very little Swift code that exists today. To let this notion of ownership play nicely with the existing Swift language, they have a law of exclusivity which is a little bit uses phrases like storage, reference, expression, and basically what it means. If you have like a reference or a value, then either exactly one object can be able to write to that at any time and no one can read from it. Or as many people as you want, as many objects as you want can read from this reference. Or there's a third leg of this.

Speaker B
Right, well, I think that TLDR gist that you brought up has a really good example of the law of exclusivity. So they're kind of close to the top of the TLDR. They give an example. It's a function called foo, and the first parameter is an in out x. So it's like ampersand x and then with closure, and that closure also modifies x. And so because you can have both the closure and the in out modifying that reference, and you can see how that could possibly corrupt some memory or do something really bad. Dazzle is not allowed anymore.

Speaker A
Yeah, I think that's right.

Speaker B
Yeah. So basically, if you try to pass the same thing to a function twice in a mutating way, whether that's via a closure or via an in out parameter, it will just say, no, you can't do this because you're messing with too much stuff. And nobody really writes code like that right now anyway. Right, fine.

Speaker A
I think some in this document, they call out that most of the code that exists, that currently that violates this law, because it's not a law yet, is probably wrong in some way. Right.

Speaker B
I can't imagine a situation where you'd ever actually want to write this code.

Speaker A
Yeah. So the sort of intuition here is that anytime you have multiple accesses to the same variable, the same bit of memory going on, those all have to be reads. And if you ever want to write to something, there has to be one possible writer and no possible readers, and that'll be enforced again for just across all of Swift, not just for code that's using these ownership features, but that probably won't affect you.

Speaker B
Yeah. And they say it's both static and dynamic enforcement. So it'll check it at compile time, and if it's not sure about it at compile time and it runs and you try to touch the same thing twice, it'll just crash.

Speaker A
Yeah, exactly. And somewhere they call out that while that dynamic enforcement might catch things like concurrency bugs and data races, it's not guaranteed to do that. That's not really what we're trying to do here. So it's worth drawing a distinction here that we're not talking about these things like magically taking care of concurrency bugs. You still have to write correct concurrent code, and this isn't going to help you a ton while you're doing that.

Speaker B
Right. I feel like I understand this a lot better now.

Speaker A
I'm glad. I feel like I kind of have somewhat intuitive understanding about it now, but I'm really flailing trying to articulate it.

Speaker B
Yeah. No, the thing that was good for me was saying when something is shared, it just means it's immutable and read only.

Speaker A
Yeah. And it's like the reference count doesn't get incremented or if it's a struct, it doesn't get copied. Right, right.

Speaker B
It just doesn't need to be.

Speaker A
Exactly. Yeah.

Speaker B
Because the external scope ensures that it stays a valid reference, and the internal scope is knowledge. Change it or read from it or do anything but read from it.

Speaker A
Yeah. So that's really what we're talking about here. That's I think the biggest takeaway. Yeah. So later in the document, they get into non copyable values, which are something that doesn't exist in Swift at all today and something which I'm a little bit fuzzy on still, but I can try to take a stab at this.

Speaker B
Yeah, go for it.

Speaker A
So you might have something that represents let's go back to say, a file handle, right, or represents access to some resource where there actually is only one of this resource. Unlike a struct or even an instance of a class, it doesn't make a lot of sense to copy that. Like might happen in Swift today, where you might pass your file handle class or an instance of your file handle class into some other function. And now both functions have an ownership interest in that instance of the class, right? That doesn't really make really intuitive sense. And now it may be a little bit ambiguous, like who's responsible for making sure this file handle goes away right, or gets properly closed out. And so they propose adding non copyable values. So these would be just at a really high level, like values or structures or classes, like types that can't be used with Swift's normal ownership model today. They can only be used with these new ownership semantics that we're talking about introducing. So if you have a type that's not copyable, you can't just pass it to another function that implicitly tries to copy it or implicitly tries to increment its reference count. You have to explicitly say, I'm sharing this in an immutable fashion, or I'm passing ownership of this to this other piece of code now. And so the manifesto proposes adding this sort of type with a few special keywords and proposes adding a few global functions to help deal with these kind of semantics. And this is like, I don't really have that much, don't have that much else to say. That's another thing that is discussed in this manifesto.

Speaker B
Yeah, the way that they do that stuff is they kind of like, define a function that takes a t and returns a t so it just works with any value. And they call it move or they call it copy or whatever and they add secret extra semantics to it within the compiler itself, which I kind of think is a bit of an inelegant solution. Yeah, that was one thing that I saw. I was like, yeah, if you're going to add a keyword, that's fine, it's clear that you're operating at the language level. But if you're going to add a function that just tells the compiler magic stuff, I think we have that right now. We have like numeric Bitcast or whatever. We have other functions that kind of just do weird stuff. They're just pre functions, they just chill out. But it just seemed a little bit like not fully baked yet, this part of the document.

Speaker A
Well, I'm not sure, I mean, it seemed weird when I was reading it, but like, thinking about this, how else do we implement something that tells, again, the compiler and the reference counter ownership checker and the optimizer? Now this instance or this value is being moved elsewhere, like ownership of this thing is being transferred. That's not really a standard library sort of thing. That's something that affects compiler behavior, it affects the code that gets output.

Speaker B
Right, I don't disagree with that, I don't think it should be in the standard library. But I also like a magic function in the compiler secretly understands when you're working with the keyword, you know, this is clearly a language level thing because I'm working with a weird keyword. But if you're working with just a function that just has special semantics struck me as a little bit weird, it's not necessarily the worst thing in the world because I think 999 out of 1000 actual application developers will never touch this stuff.

Speaker A
Oh absolutely. I think this is pretty clearly a step toward their stated goal of Swift being able to be used for sort of lower level and high performance computing.

Speaker B
Well I think they're going to use it in the standard library, for example. I think it'll make sense there to make let's say if equal gets a little bit faster because you can remove two retains and releases, then that could make a lot of things a lot more fast.

Speaker A
I mean that's a good point. Yeah. Your applications will certainly benefit from this once this is actually built into the language without you necessarily knowing about it at all, which is kind of cool.

Speaker B
So you're kind of asking how else can you handle this stuff if you don't want to add sort of a function that the compiler knows to add special semantics to?

Speaker A
Yeah, basically I kind of can see what you're saying. I guess if you're just saying that it's weird that there are things that look like normal functions that have different semantics.

Speaker B
Right, yeah. Can I talk about a highly academic language that actually may shed some light on some of this stuff?

Speaker A
Yeah, absolutely.

Speaker B
It's called Pony and they actually had a lot of this stuff and actually maybe even a little bit more powerful stuff like maybe a year and a half, two years ago and I think Russ had this stuff back then but it was definitely very academic and there were papers about it and stuff. But the way that it works is that every reference that you make, you kind of have to declare it as with kind of a capability. And that capability is like ISO for isolated or there's like six of them total, I think one of them is Tag, one of them is Val. And each of these sort of keywords are they call them reference capabilities. And they tell you what you can do with a specific reference, whether you can read to it, right to it or neither, and whether you can do that locally or globally. So there's six of them if you make that like cross product and so if you build that into the language, their claim is you can never have a data race, you can never have like a deadlock you can never have basically any of these concurrency bugs that we're so used to having. They just are inexpressible because the type system will see like, hey, you're going to be mutating this thing from two places globally. I'm just not going to let you compile that.

Speaker A
So this is interesting for a couple of reasons and I read the specific article that you sent earlier, which we'll throw in the show notes as well. Firstly, it's worth noting pony is an actor based programming languages, or an actor model programming language. So it's designed from the outset for this sort of highly concurrent programming. And so it makes sense that the type system and the compiler and its system of references takes us into account. And so I was obviously trying to read this article pretty quickly right before we recorded this episode and don't have any familiarity with the Pony programming language. But I got kind of lost trying to keep track of the different use cases and different reference types in my head while I was reading. And I think it's important here to call out that while you can get more and more wins in terms of correctness by basically shifting more I don't know if complexity is quite the right word, but shifting more complexity into the type system, that also makes the language a bit less approachable and a bit harder to learn.

Speaker B
Yeah, a little bit.

Speaker A
And it does that right from the outset, right? And Swift is first trying to do this and maintain backward compatibility and trying to do the whole progressive disclosure, right?

Speaker B
I'm not saying Swift should do it like this. And Swift did have its own things where it kind of pushed the limits of what normal program is expected, such as like optionals.

Speaker A
Oh, yeah, absolutely.

Speaker B
And I mean, I think you only have a certain budget for that and Swift spent it on optionals generics enums with associated values, stuff like that. But if you did want to go a step further, you could look at something like Pony. And I think the way they handle is pretty interesting. There are six of these and I don't necessarily understand all of the sort of reference capabilities, but there are some that are really obvious, right? So like ISO means isolated and it just means I'm going to read and write to this and nobody else is allowed to touch it. Right? And if that's the case, you know that it will always be safe because it can't be touched by anybody else and you're the only person who's ever touching it. And then another one that's interesting is what they call tag, which you can't read to or write from, which is crazy, but it basically means that all you can access is the identity of the data. That's the only thing that you're allowed to know. So all you can basically check is like is this thing, that thing, and so if that's all you need from the reference, then a lot of different things can touch that data without having to worry about it. And then there is a similar thing to the sort of shared thing that we talked about where multiple global and local readers can occur, but writing is not allowed. And so as long as you make sure that you don't attempt any operation on a reference that doesn't have that capability, then you know you're going to be fine. And the compiler, of course, won't let you do that. So it's an interesting approach and I think it's like a more hardcore version of the ownership manifesto is what it feels like. Absolutely ownership manifesto, but with everything and.

Speaker A
Even perhaps even a little bit harder to understand at the outset than Russ.

Speaker B
But you could imagine a world where now we look back on the days of like anything could be optional and you just had to deal with Null all the time and you never knew if something was Null or not. And you could look back on that and be like, oh, you were just allowed to mutate data from any thread and your compiler just let you do that. It's the kind of thing that it'll show up in academic programming languages first, and then hopefully it'll trickle down to your sort of more mainstream languages and we'll really be able to run true analysis on some of this. More crazy concurrent code where it seems really hard to be able to tell what the code is actually doing or what it can do and make states that we don't want to be in, such as databases not expressible anymore.

Speaker A
So I think that this ownership model in particular could help add some features and some analysis capabilities like that to Swift in the future if and when they get around to introducing a proper concurrency model to the language.

Speaker B
Right, right.

Speaker A
You can imagine, for example, if they do a C sharp style async await sort of method of running code asynchronously and waiting for some sort of result that maybe values their objects that get passed into something. Running asynchronously have to be shared. Right. At that point we'll have the tools to enforce this immutability property, to enforce the law of exclusivity there. And maybe this plays into that somehow. I haven't really thought about that in much detail at all.

Speaker B
It could and if you think about it, Swift does have some of these things already. Like if you have a private let, there's nothing I think one of the things that Pony also guarantees is that any actor only has one thread to work on.

Speaker A
Well, right, I mean, that's just how actors you have an actor and that's a thread and it does things and passes messages to other actors that do other things.

Speaker B
Right, yeah. And then Joe yes. The way that we got here was basically we were wondering how do you basically change one of these reference capabilities to another reference capability. And so this blog post I linked in the show Notes has a really good example of that, where they have a string to string dictionary and it's an ISO variable and then they mutate it a little bit and then they pass it into a TRN variable, which means some other thing. And then they use the function consume on that. So that consumes that variable and makes it so you can't use the original one anymore and converts it to a variable of this new type. So it's kind of like in Swift, like maybe you make a struct, like a VAR at first, so you can mutate it and then you assign it to a let and then it's like sealed and then you can't change it anymore. Swift does have some stuff like that. It's just like that, but more intense.

Speaker A
Yeah, absolutely. And the more I think about it, I think that this blog post we're talking about with Pony is just an example of how their type system enforces the concurrency model that they use for actors in that language.

Speaker B
Yeah, it would be a cool thing.

Speaker A
It's cool to bring it full circle to like, okay, how do we think about converting between these between these different reference types? And yeah, I'm still a little bit fuzzy on how that works potentially in Swift. I don't know if that's really super outlined in the ownership manifesto. It probably is, and I just missed it somehow.

Speaker B
Oh, I think that's what move is for.

Speaker A
I think that move is somewhat subtly different.

Speaker B
It may be a move function can be used to request an explicit move of a copyable type. The copying stuff is different.

Speaker A
Yeah, but that ruins the or not ruin that unsets the original reference. I think you just can't maybe yeah, I guess in a lot of cases it would just make sense that you couldn't. Well, I think that maybe you would use copy in this case right. If you have something that actually is copyable.

Speaker B
Well, but right. I guess that you can copy it to a new reference and the external scope doesn't need to know that you've copied it.

Speaker A
Yeah. So it's worth noting that I feel like this manifesto is a little fuzzy on these special functions and what they actually do.

Speaker B
Yeah. One cool thing I would like to call out is one of the most practical ways I think developers are going to get advantage of even if they don't have to deal with it. Is like when you are mapping. Over an array right now. What it does is it will get that value out of the array, make a copy of it, pass it to you. You mutate that copy or, no, you don't mutate that copy, but you return a new value based on that copy, and then it'll stick that new copy into a new array. Right.

Speaker A
Right.

Speaker B
But with these new semantics. Basically it'll pass that to you as shared and it won't basically make that extra copy before you do your thing with the map because it goes, I am a non escaping block. I'm going to pass it to you and then you're going to do something with it, but you're not going to be able to mutate it because it's already like it's a function parameter, so it's not mutable. And so you won't have to do that extra copy and things will be faster. Just for mapping, let's say.

Speaker A
Yeah, especially if you are dealing with arrays with nontrivial structs in them. There's a lot of copying going on if you map a large array with structs of some significant size.

Speaker B
Right.

Speaker A
Because again the compiler and the optimizer just have to be conservative and this will let them be less conservative and things will be faster.

Speaker B
Yeah, should be cool. I'm interested to see once this lands if I'll ever actually write this in my code.

Speaker A
Me too. Yeah. I have to think that there will be cases when it will be useful.

Speaker B
Maybe like a sequence extension. Yeah, you'll copy the implementation out of the standard library like let's say you want count where we pass a block and it tells you how many items in the sequence pass that test and you might want to share it for that just for a little more correctness.

Speaker A
Maybe if you're rewriting the audio engine in your podcast app or something like that. Right, yeah, that's right. Again, that sort of situation where you're maybe dealing with a lot of data and somewhat kind of a performance sensitive situation, that's really the case where thinking about this in more detail is really going to be useful. And again, like the common case, just whatever swift code you've been writing is probably fine and the optimizer does well enough and things generally work.

Speaker B
Right.

Speaker A
This is something that you don't have to use and I mean, it's here if you need it or will be.

Speaker B
Here if you need it, hopefully soon. Yeah, it's a pretty complex topic. I'm really glad that we had a chance to sit down and you walk me through some of it.

Speaker A
Yeah, I mean, I'm hoping it is kind of a complex topic to wrap your head around. I'm really hoping that I did an okay job of explaining it. Again, I really recommend reading through the resources that we've thrown, especially the first couple of links in the show notes. I really did find these resources very helpful in understanding what's going on and worse comes to worse, you just listened to this podcast for 35 minutes and it wasn't too helpful. But eventually when this gets added to the language, someone will write something that's actually useful about it.

Speaker B
I think it's worth noting like the Generics Manifesto. The first time I read it I understood some of them but not all of them. And every few months I go back and reread it and I get a little bit more out of it each time. And I think that's just like, these are complex topics that you're not going to get them right the first time, so you're going to have to kind of pound at them to get them right. And hopefully this podcast is one of those strikes of the hammer.

Speaker A
Hopefully. Yeah. And I mean, I'll come back and read this, I'm sure, in a couple of months and realize that I said some wrong things on this podcast and that's just how it goes.

Speaker B
I think it's fine.

Speaker A
On that note, do we want to wrap up?

Speaker B
Yeah, I think that's good. Thank you, everyone, for listening to our podcast. If you subscribe to our patreon, we have extra episodes, one extra episode for every public episode. So if you're wondering where all the even numbered episodes have run off to, they're in the patreon. We would love it if you become a supporter and you can get access to all those episodes there.

Speaker A
And that link will be in the show notes. Thank you very much for listening and serious. I'll talk to you soon.

Speaker B
Yep, can't wait.

