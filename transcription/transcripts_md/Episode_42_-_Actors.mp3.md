Speaker A
I'm so excited about actors.

Speaker B
This is gonna be a great episode.

Speaker A
I think so. Welcome to Fatal Error.

Speaker B
I'm sirous.

Speaker A
I'm Chris.

Speaker B
We reversed the order that time.

Speaker A
You got to switch it up.

Speaker B
That's right.

Speaker A
Today we're talking about part two of the concurrency manifesto or the draft of the Swift concurrency manifesto, which Chris Lattner posted a few weeks ago. And part two is is yeah.

Speaker B
So we talked about Async Await last week and Actors two weeks ago. Right? Two weeks ago. This is also a patreon episode. Shoutouts patreon, people. You're the best.

Speaker A
You're the best. Thanks for your support. We really appreciate it. You're making the show possible and cool.

Speaker B
Should we just dive in?

Speaker A
I really think we should. I'm so excited about this.

Speaker B
Yeah, this is going to be good. So we're going to assume that the listener have read the concurrency manifesto. If you haven't, you probably should. If not, maybe you'll just enjoy the one and a half jokes we put per episode.

Speaker A
Yeah, we're just ripping. Okay, cool. So Actors, Chris, in this manifesto, was proposing adding actors as a way, like at the sort of higher level concurrency tool to the Swift language natively. And it's something that would build on top of and interact really well and so elegantly with Async Await and with some of the other stuff that they're planning for the language, with the move semantics and that alternative ownership model which we've talked about previously. It's so cool and so nice how all this stuff actually works. It all comes together and works together and it's like all these puzzle pieces fit together perfectly. It's so good.

Speaker B
So I already have so many questions for you.

Speaker A
Let's do that.

Speaker B
You seem so excited. You're talking faster than I've ever heard you talk before, which is great. Okay, so first question. Have you ever used a language with Actors in it?

Speaker A
No.

Speaker B
Have you used Aka? Have you used any, like, Scala, I think has some actor model stuff in it? Nothing?

Speaker A
No, I haven't. I've never used actor related stuff in Scala. I think there's an actor thing for Objective C that's maybe called Actor Kit, which has been on my list of stuff to forever. But both you and I have written things that are kind of like actors in iOS apps before.

Speaker B
What kinds of things are you thinking of?

Speaker A
So you've used the pattern, I assume, where you have some class and it receives messages, because that's how message passing is how things work, at least in Objective C and kind of sort of in some parts of Swift.

Speaker B
Right, right.

Speaker A
And you've probably done the thing where you have some state that's private and internal to that class. And to make the class thread safe, you have an internal serial queue and sort of serialize acting on that internal state when people pass messages to you, to this class, and you dispatch to your serial queue and wait and do whatever you want to do with your state and return your result. That's a really common pattern in iOS, like concurrent iOS programming at least, right?

Speaker B
Yeah, totally. And I think even in some really broad generic sense, every object in the classical Allen KS definition acts as a cell, accepts messages and sends messages to other objects, which in this case are very similarly defined to actors. And also I know what you mean, I have done the thing where you have private internal state, you synchronize it with a queue and that's essentially what he is suggesting here. He says something like iOS programmers would best know how to can best think of this as basically a class with a serial queue that you can access state on, but the state can't leave the class.

Speaker A
Yeah, the exact sentence just to read right from this manifesto, as a Swift programmer, it is easiest to think of an actor as a combination of a dispatch queue, the data that the queue protects and messages, it can be run on that queue. Which sounds a lot like that thing that we've all written just manually rather than the system providing these properties.

Speaker B
Right, yeah. So I'm also curious to know when you say like, oh, this is a very elegant, like coming together of a bunch of different ideas in Swift, what ideas are you talking about there?

Speaker A
So, first of all, this plays really nicely with Async Await, which we've discussed previously and which would be the sort of first language level concurrency feature to be added under this manifesto and under the actual proposal that actually exists. Right. So it plays nicely with Async Await functions on an actor that are marked with the actor keyword, which are like the not exactly public because they could still be declared internal or private. But those are the methods on that actor that can be called by other objects and that can be called in a concurrent fashion. Those are implicitly async So that has a few implications. Like when you call an actor, you will have to call it Await and wait for it to get some value back to you. And that takes care of where previously you're just calling a random method you don't know exactly that might block. But when something is marked as actor, you know that you're calling it, it will run asynchronously you're going to sort of yield control from your run loop from potentially the actor that you're working within and then come back to it later. So this just dovetails really nicely with the Async Await stuff that has been proposed, I guess if I Dephrase it in a sentence, just because that provides us with the necessary semantics to call methods on actors and let things run asynchronously really elegantly, so that part of it is solved.

Speaker B
So one of the really crucial things here, I think, and this does play really nicely with a lot of Swift stuff is that data that comes into and goes out of actors has to be value types.

Speaker A
Right, and that totally makes sense. Right? You wouldn't want to passing reference types between things that are you would want.

Speaker B
To expose internal immutable stuff, right? Yeah.

Speaker A
So there's one thing that I'll call out while we're talking about classes. This proposal or this manifesto proposes introducing a new protocol which basically means which basically allows.

Speaker B
Is this the value type of value semantical?

Speaker A
Which is maybe well, I think it's intentionally ridiculous because otherwise we'll bike shed the name here, right? So he proposes introducing that and this would define a single function which basically returns a copy of self. So it's like a new instance of the same reference type that is a copy with value semantics. So this method should guarantee that there aren't any internal references, any pointers between these two objects, they're not relying on the same underlying stories. Right. So you actually can under this proposal, you can pass classes, you can pass reference types into these actor methods, even though those aren't value types, but as.

Speaker B
Long as they're value semantical.

Speaker A
Right, as long as they're value semantical. I forget exactly what it says here, but maybe when you pass a value semantical reference type to an actor to do something, the compiler under the hood inserts a call to the value semantic copy so you end up with a copy. So you can use this with reference types. It just has to be possible to like you couldn't do this with something that represents a thing that's actually a singleton, right? Like a file handle. It has to be something that you like that is fundamentally right, exactly. Yeah.

Speaker B
And I like that. He notes that he says a number of classes in Cocoa are already semantically immutable such as UI Image is a really good example of this and UI Image for the value semantical copy function would just return self, I think, because you can't mutate it. So it's just totally fine to just pass it around.

Speaker A
Right, and in a lot of cases this implementing that value semantical protocol will be just trivial. Right, and that's good because we have a lot of classes that are like kind of sort of value types.

Speaker B
Yeah, for sure.

Speaker A
So the other thing that I wanted to call out, which Chris discusses here very briefly is that this works really well. So let's say that you're using structs and you're using value types and you want to pass these things to actors. Well, in a program that's written using this new paradigm, you may be passing things between a lot of different actors. You might have actors that represent the documents that are open. You may have an actor that's like the quote unquote main actor and that basically represents the UI thread or the combination of the user interface, which is sort of a bucket of mutable state and methods that operate on the user interface. And so you're going to be passing things between actors a lot. And one of the cool things that Chris notes is that we already have copy and write value types. We have really efficient copy and write semantics under the hood for arrays and for dictionaries. And the other thing that is going to really help with this is we have move semantics on the way from the ownership manifesto.

Speaker B
Right, right.

Speaker A
And so this means that this provides you with a lot of different options for dealing with passing things between actors efficiently. And in the common case, this isn't something that you're probably going to have to worry about. But in the case where you do have to worry about this, where you're doing something really performance sensitive and really want to move ownership of some value out to some other actor for it to do something with the move, semantics from the ownership manifesto will solve that. Really. This all just comes together so elegantly and I'm so happy about it.

Speaker B
Yeah, I now see what you're saying between basically async between awaiting and having value types and having all the ownership manifesto stuff, you end up with a situation where you don't have to make that many copies. You can do it efficiently, but you can also get all the guarantees that you want to get.

Speaker A
Yeah, I'm also really excited, although I've never used actors, I've never used a language where actors are a first class concept. Right. I think that they seem like I mean, I've written a number of things that look and feel a whole lot like actors and I think that this just really is a really nice way to wrap up a lot of or to solve a lot of the common problems that we face when writing concurrent iOS code. It seems like a really nice, really elegant abstraction that can be applied in a lot of different situations and I think that will make things a lot easier.

Speaker B
So I don't want to get too philosophical. Sorry, that's why I absolutely want to get really philosophical. People argue about object oriented programming a lot, but I think what Alan K.

Speaker A
This is a super object oriented solution.

Speaker B
To this is like concurrent actors, I think, are what Alan Kay meant when he was talking about message passing, when he was talking about basically like, this message could exist on another machine, which we'll talk about distributed actors. I'm really excited to get to that part of it, but this object exists somewhere else and I can basically do RPC to get data to and from the thing. And I think this is what if you want to talk about what object oriented programming is, it's not about inheritance, it is about polymorphism to some degree. But primarily it's about this idea of there's messages and you can send messages to other objects and the objects can respond and send messages of their own, pretty much. And so I think now I feel enlightened in that when next time I get into a discussion about like, oh, functional programming is like this and object oriented programming is like this, it's like, well, just replace whatever you think your definition of object oriented programming is with actors. And then let's start the conversation there in the same way that functional programming lovers will say, replace whatever you think a function is with a pure function, and let's start from there.

Speaker A
Yeah.

Speaker B
Now, the big, big question that raises to me is, like, how in the hell do you test this?

Speaker A
What do you mean?

Speaker B
I think you how do you write a unit test for, let's say, an actor that talks to another actor?

Speaker A
The same way you test a class that talks to another class. You have injection, possibly. Yeah. I don't see this as inherently something that's more difficult to test, aside from maybe the fact that it's more like Asynchronous. But we deal with testing asynchronous code already, and we'll deal with testing async await. I haven't really thought there are test implications, but there's a good chance that that may make should make testing easier. Right, yeah.

Speaker B
In the same way that you can throw from a test right now, like a test function, you could write just throws and then you could just freely throw from there and throws it fail. I think you could just easily make a test function async and then so I think that part of it's easy, but it's like, well, how does I.

Speaker A
Mean, an actor provides an API that does something. You verify that the API does what it says on the tin.

Speaker B
But can you wrap an actor in a protocol? Can you stub an actor?

Speaker A
We're getting into fairly this is weedsy.

Speaker B
But I think it's really important. This is a big change, the way we write code. So let's say there's some code that touches this main actor UI actor, as Chris Liner wants to call it. Is there a way to say, okay, when you're running this code in this context, replace the UI actor with this stub. How can we test that? I don't know. And I don't think there's any answers. And I'm not sure that you can pass an actor to another actor's initializer. Would that work?

Speaker A
So we don't know from this proposal whether actors can conform to protocols, whether exactly in what cases actors can be used. Although there's the alternative design heading that discusses whether actors should be just a special kind of class.

Speaker B
Yeah. Which we should also definitely talk about.

Speaker A
This implies to me that you'll test these things much like you do regular classes.

Speaker B
Yeah.

Speaker A
You'll use them and pass them around in your past references to them, rather around in your application, much like you do regular classes. That's kind of the other cool thing about this is it's clearly a fundamental language change, but in terms of conceptual, it's not a big conceptual leap from what we know it's not now.

Speaker B
It's basically a class with more limitations. And that seems really good to me, pretty much.

Speaker A
And those limitations let the compiler provide machinery for helping you write concurrent code.

Speaker B
Right, right, exactly.

Speaker A
Or correct concurrent code.

Speaker B
So I just want to highlight one of the examples. In the example actor Design for Swift section, he straight up has an actor called Table Model that takes an actor, the main actor in its initializer and just keeps a reference to it. And that's just how it works. So clearly you can pass them around. Obviously at that point you need to stub the main actor or something, some protocols, some sort of fake.

Speaker A
Right. And maybe your main actor conforms to some number of protocols depending on what different things need to interact with it. Swift is super protocol oriented and it's not uncommon to have a class which is extended to conform to a huge number of protocols for the purposes of testing dependency injection, slowly refactoring something into different disparate parts. Right.

Speaker B
I think if we got actors, I maybe would never write another class.

Speaker A
There certainly are still going to be things that aren't really first class, like your classes that are kind of sort of data, but you still want to have reference semantics for maybe there's still going to be a number of cases where you don't want the overhead or the limitations that come with something being an actor.

Speaker B
So in particular I'm thinking like right now, I haven't intentionally subclassed something like making an abstract supertype and then subclassing it for its polymorphic reasons since I started writing Swift. Like, I've done an objective C because that's really the only way to get polymorphic enums that have separate data in them. But I have not subclassed anything in Swift except in the cases where you obviously have to like UI view, UI view controller, that kind of thing, and you just don't really need it because protocols are so good, because structures are so good, you just don't need it. And so I'm thinking that if this lands, I can think of very few cases, almost every reference type, quote, unquote in my app acts kind of like an actor. And I think actor is also a better way to think about what a like, think about the difference between this is something that does work versus this is something that stores data, like structures versus actors. And I think that distinction is so clean and clear that I cannot right now think of a single object that I would write that would stay a class. Obviously the ones that have to be classes, UIV controller, whatever. But in terms of the code that I write, I just am having a tough time imagining well, and you could.

Speaker A
Imagine some maybe not UIV controller, but some of the examples here. Think about the main thread or the UI thread as being an actor. Right. And so there will be some interaction between UI kit and the actor based world. I don't have any iOS code handy on this computer right now. I'm guessing that if I did, I could pull something up and find an example of something that would still be a class. Yeah, there are things that aren't like.

Speaker B
Big, but actors don't have to be big. That's the thing is like the example that he gives actor table model let.

Speaker A
Me finish my sentence there. And things that are like big isn't the right term, but that really define data and things that act on that data. There are classes that just I don't know, there are simpler classes that don't need this, basically.

Speaker B
Yeah. Let me put it a slightly different way then. I can imagine that there is a class, but I think the fact that neither you or nor I can think of one right now suggests that it's going to be pretty rare to make classes in the new actor world.

Speaker A
That might be true.

Speaker B
Yeah. Again, I could be wrong, obviously, but my thinking right now is like, this subsumes almost everything I want to reference site for.

Speaker A
Yeah, I think that's I mean, that's a good that's a good intuition. You're probably writing really good classes right now. I'm so proud because that's true. That indicates that to me.

Speaker B
I hope so.

Speaker A
I hope that's kind of related to this. Under the actors as classes like alternative design discussion, there's a big question. Is subclassing of actors desirable? Is that something that should be supported?

Speaker B
I am so jazzed talk about this. I absolutely do not think that that should be allowed. I think there is no sense follow up, no reason follow up.

Speaker A
Do you think that subclassing of classes should be allowed setting like UIV controller thing?

Speaker B
Right. The only reason I think that subclassing should be allowed in Swift is to basically like because Coco requires it. If cocoa were designed in a different way, I would just say absolutely not. There's no reason to make like subclassing. Go has zero subclassing. I mean, you've been writing Go.

Speaker A
What do you think Go is? Super? I don't think that bringing Go into this. Go is a really different language from Swift and this is neither a good nor bad thing, but it's a really different language. And I don't think that Go is discussing Go in the context of whether actors should be subclassed is a useful discussion.

Speaker B
My only point is it's very possible to make a language that does have subclassing. And it's fine, it has tons of usage and everything is okay. There are certain cases in Swift where I have philosophy. Yeah. I have seen people pull off like subcrossing in like a really nice and elegant way. A good example is the Promise implementation that I think John Sundell, the Swift by Sundell guy wrote. And that is like a really elegant thing where it's like the future is the superclass and it's immutable and then the promise is the subclass and it's mutable because it has access to the state in the future that external things can't sort of access. And I think that that's like a really elegant thing. I would probably never do that, but it is nice to be able to do that. That being said, so rarely do I want a subclassic class. Like I said, I've never done it in Swift. That I just don't think there's any reason to allow subclassic of actors. I do think it is a little weird in that if you conform an actor to a protocol, will you get those protocol methods? Is that a way to share code between actors? Maybe TBD? If that's not possible, then maybe you do want subclassing. But just like I just never want to have to deal with the fragile based class ever again. That's the thing that I'm after here. That's totally and I will do as many workarounds as I need to to not have to have that problem.

Speaker A
Yeah.

Speaker B
So what do you think? What do you think about the subclassing situation?

Speaker A
I don't know if I have a really fully formed opinion on this. I think that honestly, as long as we're fitting actors as a reference type into Swift, I think that it probably makes sense to allow subclassing just because that fits in with the sort of philosophy that exists for Swift's reference types. I think that actually subclassing actors in a modern Swift application should be just as rare as actually subclassing classes. That is to say rare because protocols I don't know if there's any discussion of protocols in here. I'm I'm making a big assumption that actors can can conform to protocols, but I that seems like a safe assumption.

Speaker B
Yeah, I think they've got to do something there. But it's a real open question because the semantics of a regular function and an actor function are so different that I kind of don't know how it work. Would it just work or would it be like certain functions in the protocol have to be marked as actor functions and then what happens if you check them from that second structure? It would be really weird. And maybe that's something that we should bring up on the mailing list.

Speaker A
Yeah, I mean, there are a lot of open questions here. Yeah, I think that it maybe makes sense to wait on that discussion until we get closer to there being an actual actor's proposal.

Speaker B
Yeah, I think that's right. Definitely something to think about though.

Speaker A
Yeah. Oh, for sure. Yeah. If there has been any discussion about this and we've just missed it that any of our listeners are aware of, please do send it our way. I'd really appreciate reading anything about this.

Speaker B
Yeah, for sure.

Speaker A
Yeah.

Speaker B
I'm really looking forward to discourse forums for the with evolution so I can actually try to keep up with it. The mailing list is just like so hard to keep up with.

Speaker A
It really is.

Speaker B
And I think we're not far from discourse, hopefully.

Speaker A
Yeah, I'll pay more attention to the evolution mailing list then.

Speaker B
All right, so there's two really big things I want to make sure we hit. One of them is how actors fail and the other one, which is tied into that is distributed actors. All right, let's talk about failure first. This is really interesting, right? Because if an actor fails, what happens to the data that it's kind of protecting? What happens to the things that have a reference to it, basically, how does failure work?

Speaker A
So it kind of depends what you mean by failure here. If you just mean there's some maybe recoverable thing that's gone wrong that should be handled the same as you handle it in a class like methods will be able to throw across async await boundaries and that'll all work. And maybe your actor is left in some weird state and you're starting to throw errors out of it rather than providing useful answers. But that's kind of something for your application to handle. If you mean a harder error, like a fatal error, for example, then I think we're moving on to part three of this document, which kind of talks about what happens if you fatal error inside an actor, right? And you can imagine some interesting cases here, like what if a server is spawning actors to deal with client requests and one of these actors encounters some unrecoverable error?

Speaker B
That's the particular case that I'm interested in here.

Speaker A
I thought it might be because our previous episodes about Swift on the server.

Speaker B
Yeah, I think an actor makes total sense for spin up a thing, has access to its own local thread, its own local data, and can talk to other actors for the database or talk to other actors for the network, et cetera. But fundamentally, you spin up one actor and you live in that actor. And I think that model is really good and it provides the reliability of saying, hey, if this crashes, it doesn't have to bring down the whole process. And so, given that that's super important, especially for the server, but also on the client side, how do we handle that?

Speaker A
Yeah, right. So the idea here is that there'd be some way for an actor and maybe not all actors, hashtag not all actors, but just actors who want these sort of guarantees. Maybe the runtime just like never sends responses back to things that are waiting on that actor, which could introduce deadlocks or introduce various things that just all sorts of other weird program state. So that seems wrong. There are a couple of solutions that this document discusses. One is provide a standard library API to register failure handlers for actors. And that seems kind of clumsy, but also actors that have this in this proposal or this manifesto, it's called this reliability property. Meaning that I guess the actor itself can crash and they'll take down the rest of the system.

Speaker B
Right, right.

Speaker A
And maybe like use cases for this will be far and few between enough that that's actually fine. Because the other solution that's here is forcing all actor methods to throw and that with the semantics that they only throw if the actor is crashed. And that seems like that's going to just put a lot of sort of boilerplate error handling code into force it into callers of things that want to wait on some result from this actor. And that seems really messy. And I think the common case where your actor is handling a queue of client requests or is handling database interactions registering some higher level failure handlers actually seems much better than everything that touches your database has to handle the case where the database has crashed.

Speaker B
Right? Right. So my thinking on this is essentially like okay, say you're on the server and one example of a case where your local invariance inside your actor just totally failed is like somebody literally unplugs the database. The database is hardwired to the network and so it just unplugs it and you just can't access it anymore. That seems like your invariants are really messed up. The thing should crash and you just can't recover from that in any way.

Speaker A
Yeah, although I mean, talking about the specific case where a database is inaccessible is not the best example here because your database like whoever's talking to your database should be able to handle errors because they may be transient. Maybe it'll come back in 2 seconds because networks are weird. But let's continue with this example discussion.

Speaker B
That's why you have to be able to handle it. And your server can't just crash if there's just suddenly no database. It just can't happen that way. So my feeling is basically, number one, actors should basically have a DNIT or like an on failure and they should use that to clean themselves up. So if they've opened a file handle, they should try to close it if they have like if they're like partway through a transaction.

Speaker A
So the two problems that come to mind immediately if something has really crashed, like going back to the situation where maybe there was a left fatal error in an actor, you don't know what state that the thing is in enough to try to run DNIT like de initializers. And this is discussed a little bit in this section, but depending on exactly what has gone wrong, it may not be safe to run DNIT like cleanup methods that have been deferred or like a class's DNIT method. My second problem with this is that handling this crash isn't the responsibility of the thing that crashed. Like let's say your database actor crashed. What is it going to do to clean up from that? Cleaning up is the responsibility of whoever's using this resource. Because that's the level where you're going to have to do whatever you do when your database dies, like connect you to a backup data or whatever. But that's like a more application level concern. Like, your database actor is concerned with dealing with the database, and when that fails, it's not concerned with like, what does the application do now? It fails. And that's kind of where its story ends. And now it's the app's responsibility to do something about that.

Speaker B
Yeah. Where I'm coming from is like, the actor is the only one that knows the internal implementation details of what it needs to clean up, whereas the outside caller is just like, yeah, I'm just asking for a sequel. I don't know what's happening in there.

Speaker A
I think we're talking about actors failing in this case, not just because there's some resource went missing and now we're going to clean ourselves up gracefully and be done. That seems like something where you just start throwing when things try to call your methods and provide some signal to the application that things are not okay and you need to do something. I think this is much more like something like really crashed hard.

Speaker B
Yeah, but this could happen even in the case of array out of bounds. Let's say you're responding to a request and you do an accidental array out of bounds and the whole thing just comes tumbling down.

Speaker A
Yeah, sure. I mean, that's different from the database not being available.

Speaker B
Right.

Speaker A
Yeah. It's like a pretty serious area. And you now no longer know what state this actor is in. And there's nothing speaking in the abstract. There's nothing that the language or the runtime knows is safe to do other than like, this entire actor is defunct.

Speaker B
Yeah. But then also doing nothing is also unsafe.

Speaker A
Yeah. That's what makes it really hard.

Speaker B
Yeah, I'll agree with that.

Speaker A
But you don't know enough to safely clean up from that. And I'm kind of arguing the side that I think Chris Lattner is arguing in this.

Speaker B
He says, I advocate for a design where no cleanup is performed.

Speaker A
Right. And I mean, he's right. Granted, there may be, like, common cases where you would know enough to clean up if you were just given the chance. But if your actor encounters some failure that you know enough to clean up from, like, you should write the code that detects this failure case, throws an error back to the client and cleans up from it.

Speaker B
Right. One interesting case that he brings up is like a transaction where you are like opening a connection to a database where the database may have a limited number of connections available, and if you open one and then that increases some counter or whatever and then crash. I really feel like you want to clean that up.

Speaker A
I mean, that's going to be something. It does exist, this specific case that the database is going to enforce. The number of connections that are possible.

Speaker B
Right. But you'll just have open ones. And if it's like any kind of cascading failure to use up all your connections and you won't be able to connect to database anymore and then everything will go crumbling and it'll be horrible.

Speaker A
Yeah.

Speaker B
I don't know, maybe you're right. Yeah. I see where coming from.

Speaker A
I mean, in that case, connections on your database server are getting used up and not closed properly because you have a pretty bad programming error in your database client that's causing it to causing it not to clean up because you're trying to access memory out of bounds first. Your database server probably should handle that somewhat gracefully, at least for some amount of time. But also yeah, that's bad. But also, we don't know if maybe your array of open database connections is broken now and you don't know that you can iterate through it to close things up gracefully.

Speaker B
Right. Because you don't even know if you'll have access to the database at all. The hard line may be cut or whatever.

Speaker A
Yeah, cut the hard line.

Speaker B
Cut the hard line.

Speaker A
I watched The Matrix for the first time the other day.

Speaker B
Really? Never seen it.

Speaker A
I'd never seen it. I've seen various bits and pieces and I knew all of the plot points.

Speaker B
Everybody knows what happens to the Matrix. Yeah.

Speaker A
Right to the point where there are various scenes where I can mouth the words along because it's just like common knowledge. But it was fun. Really enjoyed it.

Speaker B
Yeah. It's just in our cultural psyche. In our collective cultural psyche. I was thinking I think The Matrix is very off topic. I think The Matrix is maybe the movie that the most people in our generation have seen and can like and know about.

Speaker A
You think?

Speaker B
What else?

Speaker A
Yeah, that could be right. It's it's certainly up there.

Speaker B
Yeah. Just crazy. If you think about it. Almost everybody knows what the Matrix is. Exactly what happens in it. Who the characters are. Yeah.

Speaker A
All the twists.

Speaker B
All the twists.

Speaker A
Yeah. All the good lines.

Speaker B
That's right. Action moves. Yeah, all the lines.

Speaker A
So that's actors failing.

Speaker B
That's actors failing. And then so the other part of it is basically, should the actor register some global handler or should it basically should every what is it?

Speaker A
Should every actor method, at least in a reliable actor, be throwing?

Speaker B
Right? Well, I think a reliable actor just has no throwing. No concept of throwing.

Speaker A
Wait, really?

Speaker B
Why isn't that right? No, because a reliable actor you're saying, I'm opting in and saying this can never fail and I will always work. Oh, no, that's not what he says at all.

Speaker A
Yeah, no, that's very different from yeah.

Speaker B
Provide standard library API to register failure handlers for all actors at a high level or force all actor methods to throw with the semantics that they already throw if the actors crashed.

Speaker A
Having thought more about this because you.

Speaker B
Have messages in queued that haven't fired yet and then the actor crashes and you just can't do anything with those messages.

Speaker A
Yeah, I can see like pros and cons for each of these. We may not solve this tonight.

Speaker B
I don't know, Chris. I think if we do maybe another two or 3 hours of this podcast, I think we can get there.

Speaker A
Welcome to Fatal Error.

Speaker B
Really tough problem.

Speaker A
Yeah. I see an argument for sort of centralizing this failure logic at a high level in the application. But then your application is going to have to track what things may be waiting on this actor and go deal with that. And number two, let me force more boilerplate. But also that means your application has to track less state potentially and understand and doesn't have to work backwards through its dependency graph when something crashes.

Speaker B
Right. And I feel like there's different kinds of actors as well. I think the model of if you want your server to be responding to requests and spinning off a new actor for each one, I feel like it's really fine because that already works at a pretty high level to register some global handler. This thing failed. Return a 500, who cares? But if you're deep in an iOS app and you're like five screens in and you're trying to get like they have this table actor above and you're trying to get like, oh, what happens if I access a ray out of bounds here? I don't want to get that in the app delegate. I don't want to get that to very top. That's a very different kind of actor.

Speaker A
In this particular case, the right answer is probably still your application should crash.

Speaker B
Probably, yeah. What I was thinking is like reliable means, hey, this just doesn't crash. You can't guarantee that. Or if this does crash, like bring down the whole system.

Speaker A
I think it means like, faults are like crashes are isolated and expected and expected. Right. And you have some guarantee about what happens when an actor crashes.

Speaker B
But I want to be able to write the type of actor that doesn't have to worry about that. And if it does, I'm comfortable with bringing down the whole system. Like if my table actor or whatever, my model actor.

Speaker A
That makes sense in the majority of cases. But there will be cases where if you're structuring some really large concurrent, again, thinking like server side program, you want parts of it to be able to deal with failures because things are complicated and fail.

Speaker B
Right, for sure. I'm not saying no failures. I'm just saying I want to be able to write certain actors where I'm just like, hey, this is just not going to crash. If it does, I'm fine saying they bring down the whole system. Basically, I'm drawing a distinction between something like server spinning up new actors for each incoming request and something like an actor that keeps track of a cache, let's say on a server.

Speaker A
Yeah.

Speaker B
Like a data fetching actor where it's like, oh, either talk to this cache and that's really important because you can only access that cache on the serial queue. And I have a cache like this on the server that I've written. It's basically a serial queue wrapped around a dictionary. I want to be able to say, hey, that's not the same kind of failure that you're thinking about and I do want it to bring down the whole system.

Speaker A
And that's totally fair. And you just write that as an actor that's not marked as reliable.

Speaker B
Right?

Speaker A
Yeah.

Speaker B
So last thing I want to hit is distributed actors. We've kind of talked about this in this concept of which ones can fail and how reliable are they and do they database.

Speaker A
So for those of you following along in the Task based Concurrency manifesto draft, this would be part four, improving System architecture.

Speaker B
Right. And my feeling on this is like, this feature is beautiful and I cannot wait until it happens.

Speaker A
Yeah. My feeling on this, and especially the next section where it's like, whatever it's called, the bright and shiny future.

Speaker B
Yeah. The crazy and brilliant future.

Speaker A
Yeah. This seems like so far off. It seems like a really good goal to reach for, a good thing to keep in mind as what we're potentially hopefully working toward. This is so far away that I don't know if I'm even super interested in discussing it right now. I do think that right. As long as we have this really nice actor model for dealing with concurrency as long as we have this concept of reliable actors for dealing with things that maybe fail because things are unreliable and computers and networks are complicated then extending things to be further away like out using this for out of process or for inner process communication. Totally makes sense. I just doubt that we're going to get there in a little while, right?

Speaker B
Yeah, I think that's basically right. I mean, we talked with Kelvin last week about Swift Eight or whatever, and we were joking about Swift Eight is going to come. I don't see any future where that doesn't happen. And there's this part in here, I can't really find it. Maybe it's in the crazy brilliant future part, but he's just like, you just don't have to worry about JSON anymore because it's like you're talking to a swift actor that is on your server, and then you're on your client, and you just say, hey, give me this thing. And you just await it. And it just shows up. And you can just write your code. And letting the language just polish all that stuff and just make me not worry about it is just amazing.

Speaker A
So it's worth noting here that the proposal for the theory here that Chris puts forth for distributed actors, marking an actor as distributed only means two things. It means it's, quote, unquote, reliable. Because things that return because again, this is doing IPC. So things are fragile and things may fail. This actor may go down for some reason.

Speaker B
You may go into a tunnel.

Speaker A
Right. And it notes that arguments and results for these actor methods have to conform to codable because you don't have access necessarily to the same types anymore because you're crossing this process boundary.

Speaker B
You're no longer in your program.

Speaker A
Right.

Speaker B
And this goes to your point about everything fitting together really nicely.

Speaker A
Right. This fits together nicely with codable. This fits nicely into, like it's a nice generalization of what we've talked about so far with actors. And as Chris notes correctly, all the parts are there. The hardest part here is actually implementing this on the framework side, because you have to actually build the mechanisms to communicate across IPC that these actors will use, and you have to deal with underlying something has to handle this codable transformation on each side. Right, yeah. But totally. That seems like something that's really great for us to shoot for in the long term, for sure.

Speaker B
And maybe when we talk about Swift on the server for Swift eight or nine or whatever, it's not even going to be Http. It's just going to be I just wrote some actors and I deployed them to wherever, and now I have this Identifier for them and I just can talk to it.

Speaker A
Right, and maybe that as a distributed actor. Exactly. Yeah. Pretty wild if we're using codeable. Like, maybe it's Http under the hood with JSON, or maybe it's some totally new network protocol because we know how to encode things in other ways, too.

Speaker B
Yeah. I also want to add here that this is the first time I realized that Apple might actually make a cloud where you deploy these actors to. And I want this on the record, because I would absolutely not be surprised if, like, in five to ten years, you can just write Swift code as an actor, deploy it to who even knows where, and then just hit it from your iOS apps.

Speaker A
Yeah, Apple does like Heroku, and you can just push code to it from Xcode with a button. Totally.

Speaker B
So I want that on the record here.

Speaker A
If you want to automate that, like a button, push from Xcode to push things up to the cloud. It's super complicated and hacky and you have to use undocumented APIs.

Speaker B
But yeah, you're going to need to sign the code. It's going to be a beautiful future. If you're listening to this in the far future.

Speaker A
Hello.

Speaker B
Hi. It's nice to hello from you. 2017. And we were right. Email us.

Speaker A
Yeah, please do tweeted us if Twitter is still a thing.

Speaker B
Yeah, Twitter is definitely going to still be a thing.

Speaker A
You think they're not making money, are they?

Speaker B
I don't think you'll be able to edit Tweets still, but I think it's still going to be. I do. I do think it'll still be there.

Speaker A
And yeah, we'll be on whatever design we're on after everything is rounded.

Speaker B
That's right. On sharp edges. All right, Chris, this was great.

Speaker A
This has been fun.

Speaker B
Yeah. Cool.

Speaker A
Thanks for yeah, thanks for chatting. Maybe this is talking through the I was more excited about the actor stuff than the Async Await stuff, in all honesty, just because everything comes together so nicely.

Speaker B
Yeah. I actually hadn't considered that. The actor model does really bring together a lot of Swift components in a really nice and elegant way. And when you put it that way, that makes a ton of sense. Async Await is going to be here sooner, and I'm really excited about that. But actors are going to be a beautiful future.

Speaker A
Yeah. And it just builds on so much of this stuff that maybe seems kind of weird or it's not necessarily totally clear why this Swift team has chosen X alternative over any of the other choices, but this all comes together so nicely. I have to think that the Swift team had this sort of thought in the back of their heads and have been making some design decisions with this in mind.

Speaker B
For sure. For sure.

Speaker A
Yeah.

Speaker B
It's going to be a beautiful future.

Speaker A
I'm so excited.

Speaker B
Cool. As always, great to talk to you, Chris.

Speaker A
It's great to talk to you. Thank you so much, everyone, for listening. And thank you for your support. We really appreciate it. This has been a really long episode, so we will talk to you next week.

Speaker B
Later y'all.

