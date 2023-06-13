Speaker A
Oh, yeah. That's a weird noise.

Speaker B
It's just so strange. You think we could do 30 minutes on on the different ringtones and different VoIP services?

Speaker A
I would not bet against us. Welcome to Fatal Hair episode 40 where we review Ringtone.

Speaker B
This is our Ringtone reviewing podcast.

Speaker A
Remember when we talked about programming?

Speaker B
Yeah. Those are the days. Hello and welcome to Fatal Error episode 40. I'm Siresh Khanlou.

Speaker A
And I'm Chris De Zomback. Before we start, when I give a shout out to all of you who are supporting us on Patreon, you the supporters, make this podcast possible. You pay for our editing and hosting costs and help keep the podcast sponsor free. And we really appreciate your support.

Speaker B
Yeah, we're starting to look at some new gear, maybe some better microphones and some boom mics and stuff. So we might be able to get some better audio quality. But ultimately I think there's also what is it? A PEPC problem exists between keyboard and chair.

Speaker A
Yeah. What's yours means that he's still learning to use a microphone.

Speaker B
Do I talking to this part or over here?

Speaker A
How does it work? Classic.

Speaker B
Yeah. Today we want to talk about okay, there's mine. I've got my seltzer.

Speaker A
I don't I'm out of seltzer.

Speaker B
I don't actually like seltzer very much. Fun fact. So I don't really drink. I drink water is pretty good.

Speaker A
I have just normal water here with me today. We thought we would talk about the concrete or no? Well, talk about concurrency and swift concurrency, which means that Siri and I are just going to talk over each other and occasionally out of order for the remainder of this episode.

Speaker B
Keeping the threading jokes real.

Speaker A
That's right.

Speaker B
So the way to solve that problem is just do everything on a serial queue. You don't need concurrent queues. It's fine. Or just get rid of mutable state. I mean, you just get rid of the whole program. We don't need any of it.

Speaker A
Yeah. Your whole UI is mutable state though, right?

Speaker B
Yeah.

Speaker A
So why are we talking about this?

Speaker B
Okay, so Chris Lattner accepted a job at Google Brain, but I guess in his time off, he wrote this like 10,000 word manifesto about concurrency and swift, and he published it and made a big brouhaha. And so we're going to talk about it.

Speaker A
Yeah. So we'll include a link to this in the show notes. The title is concurrency and swift. One possible approach.

Speaker B
Yeah. I think at a high level, it's like way more approachable than the ownership manifesto. And even the string manifesto is a little bit in the nitty gritty. But concurrency, especially for iOS apps, is just like, people want to do acing stuff all the time and it's a super important part of what we do. And so it's like, actually we understand the problems of it very thoroughly. We understand what we want from such a system, like a really deep level. And so it's really approachable if you've been avoiding manifestos because they're like, too hard to get into. Check this one out. It's pretty good.

Speaker A
Yeah, it's pretty approachable. And it's something that right. As you said, sirous, like a lot of iOS developers are going to be familiar with the sort of problems that we're trying to solve here already. This isn't something like the Ownership Manifesto where we're bringing totally new concepts, trying to solve fairly unfamiliar problems.

Speaker B
Right, right. One thing that doesn't make much sense to me is that nine people have forked this gist.

Speaker A
Why doesn't that make sense? Like, only nine or I think nine.

Speaker B
Is way too many. What are they doing?

Speaker A
I don't know.

Speaker B
I guess this one. I'm literally looking at how you can have a revision history on the commits. They're just like, kind of changing some of the language and fixing some spacing issues. It's very strange.

Speaker A
Forking gists always seemed a little bit weird to me because there's no way to move to collaborate backward, pull requests.

Speaker B
Back into the original, go upstream.

Speaker A
So especially for something like this. I don't know. Well, whatever. I printed out as a PDF and then highlighted things in preview app on my computer because nice. That's how I roll, apparently. So we have a lot to talk about, so let's try to dive in here.

Speaker B
Let's do it. So I think sort of like, basically the two big things in this is one is Asynchronous and two is actors.

Speaker A
Yeah, I think that's true. Taking a step, a quick step back here, there are some goals and non goals that Chris sets forward here. They're focusing on task based concurrency. So things like what GCD and thread solve. Right.

Speaker B
Kind of I do think the problem is bigger than that. Sorry, more focused than that. It's specifically for tasks that complete in a discrete way, whereas, like, well, for Async await, at least you might have a longer lived thread or queue that you use for data isolation or whatever. But at least the first part of this doesn't really touch that. It's kind of like, I have a task and it completes at a certain point, and when it completes, the progress of the thing can continue, basically.

Speaker A
I mean, it feels like you're brushing up against actors, which we'll get to in the second part of the proposal. Right.

Speaker B
For the manifesto, yeah, it's definitely let's stay focused.

Speaker A
So a few other goals that jumped out at me right away. There should be a structured right way to achieve most tasks. Right. We want to make sure that there's sort of one clear way to bar from Python. There's like, one obvious way to do something.

Speaker B
Do you think that holds true for the rest of Swift?

Speaker A
I think generally, yeah. We've removed the plus plus operator to increment something and you have to use the for in syntax or some other, like, more structured loop syntax. Right, right.

Speaker B
But even even enumerating over something you can either use for in or you can use for each, I guess.

Speaker A
But those solve different problems, right?

Speaker B
Only a little bit, I would say for each, the only thing that it gives you is that it lets you chain off the end of a off the end of like a map filter, whatever chain. And four, in doesn't really lend itself to that.

Speaker A
Also, they're different structures, they're different constructions, may be the same thing, but they're useful in different cases.

Speaker B
Right? Yeah. I thought this part was actually pretty surprising because I don't think of Swift as a very like, there's one right way to write this code and the other ways are discouraged, especially when it comes to sequences and collections. There's a really good Erica Suduon blog post where she wants to create an array of five new UI views and she doesn't want to have to write like UI view, UI view, UI view, UI view. She wants to simplify it somehow. So it's like, do you map over a range? Do you create an iterator and then create a sequence out of that and do a prefix of the first five? Do you do the repeating API that doesn't work because actually has five references to the same UI view. I'll pull that up and pull it in show notes. But that in particular stuck out to me as something like I don't think Swift is particularly good at making sure that there's one right way to do things and the other ways are possible but not recommended. Let's take maybe roughly 8 hours to go through this manifesto by going point by point and really getting into so.

Speaker A
Those were a couple of goals that jumped out at me anyway as being interesting. The only other thing that jumped out immediately was that it's harder to maintain code that's GCD heavy because you don't always know right away what data is protected by which queue. Right. Like which GCD queue you have to touch some piece of data on. And because completion handlers don't like, there's no consistency in terms of what completion handlers get called on which queues. It's effectively random depending on who happened to design the API that you're using. And then the other thing that jumped out is error handling is really ugly across GCD boundaries, across Asynchronous boundaries in Swift right now. Right?

Speaker B
Yeah.

Speaker A
It's not good.

Speaker B
There was a notable thing in here that kind of bugged me, where he says error handling is particularly ugly because Swift's natural error handling mechanism cannot yeah. And it's like it's not really natural. Like you designed it.

Speaker A
So this isn't like a natural truth that we're just sort of deriving here.

Speaker B
Right? Exactly. It's like you made the thing you could have made it work with async errors you chose not to, which is.

Speaker A
Fine, was designed this way and we do this and a lot of people said this going in. It specifically rejected a result type or something that would have I'm still a little bit bitter about this, but yeah, okay. We can quibble with the phrasing there, I think, right.

Speaker B
No, but the ultimate point is right. The system that we have does not work for Async.

Speaker A
Yeah. So looking forward, indeed, he also described at sort of the introduction, he described a pretty utopian view of the world where developers can build, like, every part of their system in Swift, and it all runs kind of distributed via some of these mechanisms that he's laying out. And we eliminate a lot of the complexity dealing with particularly the network boundary. Right. And this seems like it's pretty far reaching. I think maybe for the purpose of this discussion, we want to talk just about sort of Async Await and about actors.

Speaker B
I think it's a beautiful future if you can run Swift on every box in your server and on every client and every remote call just looks like a call to another distributed actor and it just all kind of works that's like, very far in the future. And I think it's a beautiful goal to try to get to. But right now we have Swift. Five is like a thing that we're working on and we should think about that.

Speaker A
Yeah. So this brings us I'm sort of just like scrolling through my notes on the manifesto here. This brings us to the design of Async Await for Swift. Now, Chris Latner describes this in terms of coroutines, and I have quite kind of a vague, hand wavy idea about what exactly that means. Do you have a good can you try to explain it to me somehow?

Speaker B
Yeah, I can give it a shot. I've never used a coroutine, but my understanding is basically it's a function that can be basically paused in the middle of it and maintains its state. So if you have a python generator, when you call yield to return some value out of that generator, that function stops and stays exactly the way it is until you call the function again and then it continues from where that yield had started. Basically, it doesn't seem like it would be related to Async awaiting, but it kind of is in that when you await something, you're basically saying, I'm going to pause this function, other stuff will happen, the state of the function will stay the same, and then at some point later, this function will resume.

Speaker A
Right. I think the idea is that you have coroutines running in almost a sort of run loop. Right. And a coroutine can be paused and transfer control flow out to some other to something else that's running right and then can get data back and be reawakened later.

Speaker B
Yeah. The thing that was surprising me is I kind of assumed the way that it would work is that it would kind of make a completion block for you and kind of just indent your code and do all the stuff it would need to do to make that all work. And I think that's something called continuation passing style, but I don't really know what continuation passing style is. I was hoping maybe you knew and you could explain this one to me.

Speaker A
I can try to take a stab at this, I'm not sure whether I totally understand it, but I think the idea is that say with GCD you kick off some asynchronous task and hand it a block that basically tells that asynchronous task how to continue the work that you're doing.

Speaker B
Right, right.

Speaker A
And I think that kind of method of managing concurrent managing control flow in concurrent code is more or less at least as one example of continuation passing style. Like you pass some sort of completion block or some sort of closure, some sort of context that ends up being used to continue control flow in the caller.

Speaker B
That sounds pretty much right to my understanding, which is basically from Wikipedia, which says a function written in continuation passing style takes an extra argument, an explicit continuation, a function of one argument and then it says programs can automatically be transformed from direct style to CPS. So I kind of figured when you use a weight it would kind of just make it so that your code.

Speaker A
Would be well, I think that maybe not in this manifesto but in the concrete proposal for concurrency and Swift, which Chris also posted a draft of, I think he dives into that in a little more detail. I think that that was at least kind of how he proposed implementing that under the hood. Right. So he proposes introducing coroutines. Oh, and here we go. He writes you can think of it as Synctactic sugar for completion handlers. This means that the introduction of coroutines would not change the queues that completion handlers are called on. And he also talks a little bit later in the concrete proposal about how functions that currently deal in completion handlers could be transformed to work with async await and therefore with the proposed coroutine structure. Pretty straightforwardly. So my feeling is that that is sort of how this works under the hood.

Speaker B
Let me dial it back 1 second, ask you a quick question. Does that mean that the same function, something that looks like it's a direct like I'm writing this code, then this code, then this code like procedural style code can actually run on more than one queue?

Speaker A
What do you mean exactly? You could call it on whatever queue?

Speaker B
Well, there was a thing that you said where you said that and I wasn't clear on if it was part of this document or part of another document, but you said that it basically transforms it into a completion block which then will run on whatever that completion block was fired on.

Speaker A
I don't know if I know what you're asking. It sounds like I didn't say something clearly to start with.

Speaker B
Okay, so I'm caught up now. So here in the concrete proposal, which is formatted more like a Swiss evolution proposal, he says, as you quoted earlier, you can think of it as syntactic.

Speaker A
Sure.

Speaker B
For completion handlers. We'll also throw this in the show notes. Of course, this means the introduction of coroutines would not change the queues that completion handlers are called on. And what that means to me is if you have a function that you're writing where you're like, okay, do this data, do this, handle this data in line, and then async this thing to send it to the network and then get this result. Everything below that could actually happen on a different queue. So you could have one function that looks like it's just line, line with no blocks, no anything that actually executes on two different threads.

Speaker A
That sounds horrible. I'm not sure exactly what is meant by introduction of coroutines would not change the queues that completion handlers are called.

Speaker B
On, as happens in other systems.

Speaker A
Yeah, I don't know. I think what that might mean is not that there would literally be no change. I think that maybe that means that the queues that coroutines call things on are the same queues that your code is already running on with GCD or whatever.

Speaker B
Right. That does make sense. And that is how it is today, right? When you call a function, you'll get a completion callback on some queue. It's a queue that you can access. It's maybe a queue that your code put together, but it's not necessarily the main queue, and it's not necessarily the same queue as the code that you're running originally.

Speaker A
Okay, yeah, I mean, that's true. And I think what this is saying is coroutines aren't necessarily going to change that.

Speaker B
Right. And a necessary consequence of that is that the same function or what looks like the same function, the body of the same function can actually run on two or more different queues.

Speaker A
Yeah, and that's true. I mean, that's true now, too, isn't it? With GCD, like, whatever block you give it, if you're touching function, local, state, like, you have no idea yes.

Speaker B
What's going to today, I think we kind of know that we're passing in a block, and that block because it could run anywhere. But the idea that you could have a function that looks like it's synchronous run two totally different queues is bananas to me.

Speaker A
Well, this seems weird, and I'm wondering if I'm missing something really important here.

Speaker B
Yeah, me too.

Speaker A
Which is very possible.

Speaker B
Well, and so there's this other idea here as well as this function of async coroutine. Again, this is still in the concrete proposal, like Swift evolution proposal. And then when you call the async coroutine function, what it does is it actually switches the thread that you're on. So the example he gives is do some stuff, await, dispatch Q main async coroutine, which switches you to the main thread and then he calls a function called do some stuff on the main thread and then await background queue async code routine. And then that does some stuff in the background again. And now that I look at it, maybe it's just not that bad. Maybe it's fine.

Speaker A
Yeah. You're looking at an example here that is talking about how I guess how you'd implement. Yeah. Okay.

Speaker B
It kind of looks more like an assert where you're just like yes, this part runs on the main thread and then you're like, okay, now this part runs on the background thread and it kind of looks better. Maybe I'm down for this.

Speaker A
And I mean, this is decorated with the Async or with the Await keyword. Right. And the function is marked Async. So it's not like you can really say that this function looks like a normal synchronous function. Right? It doesn't.

Speaker B
That's right. That's true.

Speaker A
It's clear that weird things are happening.

Speaker B
Yeah. And this code is very explicit about the fact that it is changing queues. Whereas some code might not look like it's going to be switching jumping queues around, but it actually is.

Speaker A
Right? Yeah. Or even worse, like changes in other code can influence whether like changes in the code that you're calling can influence whether your function continues on the same thread or on the same queue. Or on the same queue.

Speaker B
Exactly.

Speaker A
So one thing that I was wondering here, so we add this Async Await syntax to the compiler and we haven't really defined that. I think we're assuming that people are generally people listening are generally familiar with that syntax. Really just really briefly, it basically lets you from inside some function, kick off semi synchronous work and call some code on a different queue and wait for it to give you a result back.

Speaker B
Without blocking the rest of the program from continuing to run.

Speaker A
Without blocking the rest of the queue that you're waiting on. Yeah.

Speaker B
Right.

Speaker A
So we add this magic to the compiler. And again, I think in the concrete proposal for Async semantics, which I'm looking at here, mainly because this goes into a lot more detail about implementation, the manifesto kind of really only looks at this at a very high level because this proposal document also exists right somewhere in here. Chris notes that this isn't necessarily tied to right. It's completely concurrency runtime agnostic. It works just as well the GCD as with P threads or any other API.

Speaker B
Right.

Speaker A
I guess it just chooses an implementation based on which operating system it's building for. Is that how that works? I mean, I guess right now you can't use GCD on Linux, correct?

Speaker B
That's not quite right. Okay, so you can use GCD on Linux, but you actually don't have to do anything special to get it anymore. It's just part of the thing. You try import dispatch and you can use it exactly as you would on iOS.

Speaker A
Oh, cool.

Speaker B
The only difference is, and I need to write a blog post about this, but the only real difference is that you can't really use the main queue because it's usually blocked so that the program doesn't end.

Speaker A
That makes sense.

Speaker B
Yeah.

Speaker A
Pretty chuck. And that maybe has more to do with like that's just how the style of application that you're writing is structured.

Speaker B
That's right, that's right. So anywhere that you have Swift right now, you do have dispatch. I think he's just saying that. I think one way to think about this is that threads are one level of abstraction. On top of that, we built something that we call queues or that we call dispatch more broadly, and that is a whole different level of abstraction that makes it a little bit easier to think about stuff and makes it a little bit easier to work with those threads. Then on top of that, we build a third level of abstraction that's Async Await or actors. And the point of that next level of abstraction is to hide the fact that you're using dispatch under the hood. And because you've done that, you can then reimplement Async Await as built on top of P threads or built on top of Posit locks or wherever. Yeah, something like that, I think is what he means.

Speaker A
Yeah. Okay, that makes more sense. So Runtime agnostic just means we're not tying this to any implementation at Runtime or any specific concurrency library in this performance.

Speaker B
That's right. Yeah. I think he's just saying it's agnostic to that.

Speaker A
Okay. Which is literally what that says. Okay. One other thing that I found interesting in this concrete proposal for Async semantics, which you, the listener, really should go and read through this proposal. It's interesting, it's not too hairy to read. It's pretty understandable, I think. And there's a good amount of code, and we're not going to just read code at you while you're listening because that's terrible to listen to. Chris provides a sort of proof of concept example of what a future type implementation might look like using Async Await, and that was a nice example of the sort of thing that this syntax makes so much easier and how using this language feature might look. I was also amused because the future contains its own definition of a result enum. And I had to laugh there because as previously discussed, that's something that I think should be built into language.

Speaker B
And even worse is he makes it then an optional result, which just add an extra case for pending because you're defining the it's a private email, it's only used inside the future. So just add one more case for pending and then you don't have to and you could just say private VAR results is a result that's not optional, equals pending and you're done.

Speaker A
Yeah.

Speaker B
What do I know? I'm just a lowly Swift programmer. So this actually gives an answer to one big question that I have, which is, let's say I have two completely independent Async tasks and I need the results of both of them before I can continue and do my work.

Speaker A
But they can run concurrently. Independently.

Speaker B
Exactly. Because they're independent. They're completely independent. They could run concurrently.

Speaker A
Yeah.

Speaker B
With naive Async await syntax, I would have to write await the first thing and then await the second thing. And it would happen in serial, which is problematic. Not problematic, but like, not ideal.

Speaker A
This was one of my questions reading through the manifesto as well.

Speaker B
Yeah. So I would implement this basically like, promise zip. You take two promises, zip them together, and it yields one promise with a tuple of the results of the first promise and then the results of the second promise. And how do you make this work with Async await? And it seems like the answer that he's giving is just make a future and then fulfill it with an awaited value and then add completion blocks to the future that he calls awaiters a waiter. There's a fly in my queue.

Speaker A
Some people pay extra for that.

Speaker B
Sorry, I don't get that joke.

Speaker A
Oh, I mean, that's kind of the classic, the waiter, there's a fly in my soup. Don't tell everyone, otherwise everyone else will want some.

Speaker B
Oh, you know, I never got that joke.

Speaker A
It's not a good joke.

Speaker B
No, it's a really extremely funny joke. I'm glad my ignorance is only beared to our patreon listeners, who I trust implicitly.

Speaker A
Have I mentioned I'm changing jobs again? I'm doing stand up now.

Speaker B
You can catch Chris at the chuckle factory all week.

Speaker A
Remember to tip your servers.

Speaker B
Right, so basically you just end up back in the completion block world and then you could write a zip function that takes two it doesn't even have.

Speaker A
To take two futures. It just takes two things and you wait on those two things to be available. It's a very nice syntax.

Speaker B
And then you just call like get and get as an Async function that will return the value when it's done.

Speaker A
One thing that I really like about this, looking at the futures example, is that it really where previously GCD code often looked very side effecty, right? Like, you're very imperatively saying, like, do this work on this queue and I need this result and it's going to go here. Like, it was very sort of clunky and imperative. This makes it very clear that the goal of this block is to do some work and produce some value and return it. It's so much clearer what's going on. This just looks so much less side effecty and reads so much better to my eye.

Speaker B
Right?

Speaker A
I'm looking at this and thinking it just looks very clean and functional because you're just saying, this resource is a future that will go fetch this file for me. And this resource is a future that represents the potential future value of this other file. And once we have those, I'll do something with these two files. It reads more declaratively.

Speaker B
Yeah, well, and it's interesting that you say it that way, because to me, procedural and imperative are sometimes conflated, even though they're not really the same thing. And we're staying in a procedural world, but because of these abstractions, we're able to lift ourselves into a slightly more declarative. Like, it's less imperative and more declarative, even though it stays procedural.

Speaker A
Yeah. And I think this is an important note about taxonomy. Right. In my view, you have sort of imperative and declarative are two ends of the same spectrum. And then, like, procedural versus maybe functional is maybe a different spectrum entirely.

Speaker B
Maybe procedural versus descriptive. I don't know. We don't need to reinvent the syntax here.

Speaker A
Yeah, no, it's not procedural. Okay. Yeah, I take it back. I take it back.

Speaker B
It's the procedural versus don't have something.

Speaker A
But anyway, declarative and imperative are the objects that I want here.

Speaker B
Yeah, exactly. So the next interesting thing in this concrete proposal, special proposal, is that he's proposing having functions either be automatically or manually translated from completion block type functions to async type functions. And this is basically a pretty good idea. They did this with throws for all of the APIs that return NS error. But one of the things that they brought up on the mailing list that was actually a very interesting point, was there are functions that return a meaningful value in addition to having a completion block. So a good example of this is Nsurl session. When you send off a request, you get back something that you can call cancel on, you can manipulate, you can read the in iOS ten, you'll be able to read an NS progress off of it. But then also you have this completion block. So which one are they going to pick? Are they going to pick a big? Are they going to make a tuple? Would a tuple make any sense? Will you get back one object that you then call send on? And then that actually is the thing that's awaitable?

Speaker A
I mean, I think this is an interesting question. I don't think it's really core to async await semantics for Swift.

Speaker B
You think it's kind of an implementation detail, I think.

Speaker A
Exactly. Yeah. We know we'll import these APIs nicely somehow. I assume that they'll take into account the common pattern where something returns a boolean. That's a separate thing, I guess.

Speaker B
Well, but they did handle that for error. So it's a really good point. The bullying represents success or failure, and then you check the error if it's failure.

Speaker A
Right. We've crossed this bridge before. I'm sure we'll encapsulate common patterns and give you back a tuple in cases where it's not obviously one of the common patterns. That's fine.

Speaker B
And they mentioned in the proposal, in fairness, they say what should happen with non void returning completion handler function. E g and URL session.

Speaker A
Right, sure. Maybe I'll figure it out. Yeah. One thing that you may be really interested to read about if you scroll all the way down to the concrete proposal for Async semantics and swift down to the header fix, Q hopping Objective C completion handlers. Now this is something that we talked about earlier and identified as a potential problem. So he doesn't really go into detail here since this is under potential future directions. So maybe not like immediately in scope when this gets implemented, but here, Chris has called this out as a potential problem and suggests that this could at least be fixed in the Objective C importer. I don't know, that's one thing to note and just to be aware that that's being considered.

Speaker B
Yeah, definitely. I think that syntax of Async code routine or whatever, or insure main queue or something like that, where you would say mainq ensure her Asynchronously or something, so you would say like, I don't care if I'm on the main queue already, I really, really want to be on the main queue, make sure I'm on that. And it reads almost like an assert, it reads almost like a precondition, but it just does the right thing and then your code can just continue to operate. Yeah, which I think is super nice.

Speaker A
Yeah. What else do we want to note about this proposal?

Speaker B
Oh boy, I have a lot of thoughts.

Speaker A
Okay, I'll call out briefly, just since we mentioned error handling, that now that we have nice syntax for Async Await, at least in this proposal, throwing works perfectly across this boundary because they'll build compiler support. So the quote unquote natural swift error handling will work nicely with this syntax. Which is good.

Speaker B
Yeah, this is something that I wrote a blog post about Async Await sometime last year, September of last year, and I talked about how oh actually if you do have Async Await that makes try and throws and all that stuff kind of work really nicely. So I think that is definitely going to be a component that will make this a lot more palatable and it will make having written code somewhere so on the server everything's synchronous and then try becomes awesome when everything's synchronous and you do have errors that are coming back from various processes. So once we can take advantage of that on a client, I think it's going to be really nice. That being said, I do have a question for you, which is do you think that every Async function should be implicitly throws as well? They ask that in one of these headers.

Speaker A
Yeah, I forget exactly. I think that's maybe under Alternatives Considered.

Speaker B
It'S alternate syntax options, not quite the Alternatives Considered section, but it says make Async be a subtype of throws instead of orthogonal to it. I'm wondering what you think about that.

Speaker A
Yeah, I mean, that definitely would simplify things, but I don't know there are a lot of Asynchronous things that just do something and basically won't fail.

Speaker B
Right?

Speaker A
Yeah. My gut feeling is that I don't like this.

Speaker B
Yeah. I think they should be separate as well. I think they should be orthogonal. I think there are plenty of things that happen Asynchronously that never fail. I would like to be able to model those and I would like to be able to do async without having to do catch block every single time. And then you'd be like doing try bang await because you know it's not going to fail. It would be horrible.

Speaker A
Yeah, that would be really messy. So my only thought here is that we're adding a lot of especially with the actors that are proposed in the concurrency manifesto, and I think we'll probably talk about actors in a future episode.

Speaker B
That makes sense given that we're like 40 minutes.

Speaker A
Yeah, we're adding a lot of keywords here, and we're adding a lot of maybe not complexity, but we're adding a lot of stuff here and there are a lot of details here. And maybe just async things are always throwing would be a simplification that's worth making, if only to reduce the sort of cognitive overload or the cognitive effort that comes with introducing all this.

Speaker B
I've kind of come around on this. If you want to make a language that has a lot of really rich features, you just need a shitload of keywords. There's kind of no way around it. It kind of sucks. But also I would rather have the language, have the features that were like the ship of make this as elegant as haskell sailed like two and a half years ago. It's not going to happen.

Speaker A
Right. When the air handling model got adopted.

Speaker B
Basically, like, it added throws, throw, rethrows, try tribang, try question mark, do catch, and like, it's fine, it's fine, it sucks, but it's also fine.

Speaker A
Just hearing you list all those, I cringed a little bit because I still think result plus some magic plus pattern matching would have been a lot nicer.

Speaker B
I don't think I disagree with you on that. Or at least they say we have a result type, but it's just under the hood. It's unnamed. You can't touch it, you can't access it. Let us access it. But that being said, do catch is nicer than flat map. Flat map. Flat map in a lot of cases.

Speaker A
Yeah. No, that's true. All right, we can stop beating the error handling horse here.

Speaker B
I mean, I don't think that one is ever going to be dead.

Speaker A
Have we done a podcast on it? We'll throw an episode in the show Notes.

Speaker B
We did one episode about how we handle errors. Okay, that was a good one.

Speaker A
We'll throw it in the show notes.

Speaker B
I still have more thoughts, though. So another thing that I think is interesting about this proposal is he proposes begin Async and suspend async. So the idea is that begin async is a regular function that takes a function where the inside can be async but the outside doesn't have to be async. And my feeling on this is if a function is void then it should just be it shouldn't.

Speaker A
Well, the problem this is solving is that if you call something that's async if your function calls await something, then your function has to be marked Async because it also is a coroutine that will need to be suspended at some point. And so whatever calls that is going to need to be async.

Speaker B
Yes.

Speaker A
And at some point something up the chain is not Async, but is going to have to kick off this process.

Speaker B
Right, so my feeling on this is it should be baked into the return type. If your return type is void then the outer function doesn't need to wait for it because there's no value there.

Speaker A
Oh, that's interesting.

Speaker B
Or if it does then and maybe it prints like hey, I'm done, then that function then doesn't need to be async at all because you know that nobody cares what its return value is so it should just immediately return.

Speaker A
That's interesting.

Speaker B
Yeah, you could say I care about side effects but then maybe you return that's a weird one. If you care about like you do an async thing then you perform a side effect and then you want to know when that side effect is done, but you don't care what the side effect is.

Speaker A
Well, and you may also like you still need this because you may want to call something async but still return a value, right?

Speaker B
Yeah. So if yours value then great.

Speaker A
So just having a void return type can't be the only way to start to get into the async world.

Speaker B
Why not?

Speaker A
Because what if you want to return something from there too?

Speaker B
Well then it has to be async because otherwise how could it?

Speaker A
Okay, well then something has to call that, right?

Speaker B
Which is fine, something will call it and then that's something we'll return immediately and then the async world will be kicked off and do its solid async stuff. Okay, it's async all the way down or all the way up depending on how you want to look at it.

Speaker A
Yeah.

Speaker B
So I think you can roll it into the void type and just say if it's void, then you don't need to wait on me or you can't even wait on me. That does again pose a problem if you want to know that it completed but don't care what it completed with sucks. But it seems simpler than having to nest one layer deeper and having this extra set of functions begin async and suspend async.

Speaker A
If you really wanted to do that, you could pass in some sort of signaling method, right? There are ways of collaboration that you could use to communicate across that boundary.

Speaker B
Or just return a bool, return some dumb value, it doesn't mean that much.

Speaker A
But return like an empty struct. Right.

Speaker B
Which is what void is, essentially. So you would make, like, wait on me. Wait on me. The name of the struct. Yeah. So that's what I think. I think it'd be fine if we didn't have this begin async and suspend async just because it's more nesting. Who needs it? It's more keywords, it's more free functions, just simpler to not have it at all.

Speaker A
Yeah. I have to find this here and look and see. Are there other problems that having this begin async? Are there other problems that this solves?

Speaker B
Well, something has to be not async and kick off the async flow.

Speaker A
Right.

Speaker B
And that's what it has to be there.

Speaker A
Yeah. Okay. Yeah. You have to have a way to begin a coroutine.

Speaker B
Right.

Speaker A
Suspend, the current coroutine suspending.

Speaker B
I don't really understand how that would work because it's already kind of out of your hands.

Speaker A
Right, well, that's part of how continuation gets implemented. Right.

Speaker B
I don't know.

Speaker A
I think that part of the suspend async functions here are a way to bridge between completion handler blocks that you write and the sort of state machine, the coroutine mechanics. I think that probably is still necessary, if only because that's like okay. Down below there's an example. The suspend async is used to wrap a callback based API as an async coroutine API. Is that something that where this is useful. Yeah. So look at going back to your point about begin async, though the example that Chris gives here is an IB action that's the UI calls, and he basically wraps the actions this button does in the begin async call, which kicks off a coroutine.

Speaker B
Right, right.

Speaker A
But IB actions are side effecty and return void. So this whole thing were just implicitly async.

Speaker B
Yeah. If you did want to still wait on the value of avoid returning async process, you could. And as long as you return something at the end of that function and make the outer function be async and you're good.

Speaker A
Yeah.

Speaker B
It would just work as you would expect.

Speaker A
Yeah. That's interesting.

Speaker B
I'm kind of convinced. Maybe I'll write in I'll email this.

Speaker A
Yeah. Is this something that you've seen on the email list before, or is this totally is this Sabrush original?

Speaker B
I've been keeping up with the mail list a little bit, but not, like, very much. I've been kind of busy with code writing stuff this week, but I will check it out, and if it's not mentioned already, because it seems obvious to me, so it must be obvious to someone else as well.

Speaker A
Yeah. Okay. What were your other thoughts about the wait?

Speaker B
So the first option under or the first subheading under? Alternatives considered include future or other coordination abstractions in this proposal. So to me, this is the equivalent of should we include results in the error model or not? And I think the answer is good. God, yes, please.

Speaker A
Yeah. Because otherwise we're going to have a bazillion, like, half baked coordination abstractions in every application.

Speaker B
Almost everybody's just going to copy the one that's in this proposal, just letter for letter. They're just going to paste it in their project and use it if they don't give it to us. Well, maybe we could let every time.

Speaker A
Maybe we could let Roberts write one.

Speaker B
For us, and then we'll all use that one. That's right. It'll be on version three at some point, because it's apparently very complicated and has breaking changes.

Speaker A
Hi, Rob. We love you.

Speaker B
We should put results in the show notes.

Speaker A
We will do that.

Speaker B
And then the very next one is, have Async calls always return a future. That also seems really good to me. You should just be able to await on anything that returns a future. And then if you want to just mutate the future or fold it in with other futures or do whatever it is you want to do, you can. But if you want to get the syntax trigger of Async and await, you also can do that. This is what I wrote in my blog post, essentially, so I don't want to rehash myself too much, but it just seems obvious. Give us all the tools, and then on top of the tools, give us essentially the syntactic sugar on top of that, so that we can choose to use the syntactic sugar, but then drop down to the level of manipulating objects when we need to.

Speaker A
Yeah, that makes a lot of sense to me. And this, I think, kind of ideologically mirrors the debate about error handling, whether you want absolutely. Does syntactic sugar magic rather than, like, objects?

Speaker B
Yeah. And I do want syntactic sugar magic. It's awesome. It's really fun, and it makes the code really nice to write. If I do use optional without syntactic sugar magic, I would hate it. But I do like that I can add a function to the optional type and lift it, let's say, to an error.

Speaker A
Yeah. I mean, you want to be able to use the underlying tools, too.

Speaker B
Yeah, exactly.

Speaker A
Yeah. This is something that I was thinking about, too, when I was reading this proposal. I see a pretty strong argument for Async calls always returning a future, which you can then just let execute concurrently. And you have better control over when you do the waiting.

Speaker B
Right, right. And that way you would be able to stay in concurrent synchronous land. Sorry. You can sing Synchronous land as long as you want, or you can enter Asynchronous land whenever you want because you have the option.

Speaker A
Yeah.

Speaker B
I love at the bottom of the proposal, it's, like, 16,000 words here. This proposal has been kept intentionally minimal, but there are many possible ways to expand in the future. Yeah, really great.

Speaker A
Yeah. Well, there's a lot to talk about. This is not a small subject.

Speaker B
No, it's not. This has been a long episode. I've really enjoyed it.

Speaker A
Yeah, I guess we should probably wrap up. I was just scrolling through to see if I had anything else that was really interesting that I'd highlighted, and I don't think so. I think we've talked about this pretty thoroughly.

Speaker B
Yeah. I would also add, like, if you've read the manifesto great. I would also check out the proposal itself. There's a lot of good thoughts in there that really clear up a lot of what's going on.

Speaker A
Yeah, absolutely. The sort of concrete proposal goes into a lot more detail and really clarifies some of the things that the manifesto glosses over.

Speaker B
Yeah. And we'll have to record about actors and about other stuff in the future. I think that's probably for the best just because actors is going to be such a big topic as well.

Speaker A
Yeah.

Speaker B
This is good, though. I hope the Patreon people like our little extra long episode.

Speaker A
Yeah, absolutely. I hope this was interesting. I hope that this probably is most useful if you've read the manifesto already, which I'll assume that a lot of our listeners probably have.

Speaker B
Yeah, I think so. I hope so.

Speaker A
Yeah.

Speaker B
And if you haven't by this point, I mean, you know all about it.

Speaker A
Yeah. You should probably still go skim it. And some of the stuff that we've said will make more sense after you've done that.

Speaker B
We should have said this at the beginning, I think.

Speaker A
Yeah. Well, hindsight is 2020.

Speaker B
Can't win them all. You have to say Hindsight is 1080p. Sorry, hindsight is 4K.

Speaker A
What?

Speaker B
I don't know. Just ring the bell because 2020 is a clear, very clear sight. And this 4K is like but it's like for millennials.

Speaker A
I think. I get it, but it just isn't funny, as we said at the beginning of the episode. Thank you, everybody, so much for your support. It really means a lot to us. And we'll talk to you next week.

