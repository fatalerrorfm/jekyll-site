Chris Dzombak
Man I drank almost all my whiskey that I'd poured welcome to Fatal Error, episode 45.

Soroush Khanlou
Is this the show?

Chris Dzombak
Sure I am. Chris and I'm, sirous, and today we wanted to continue a discussion that we had started back in, I think, episode 42.

Soroush Khanlou
Yeah, I think that's right. When we talked about the actor model in right.

Chris Dzombak
The concurrency proposal manifesto, the proposed actor model in Chris Latner's draft of a possible concurrency manifesto for Swift, I do feel like we should be a little bit clear that this is definitely not a done deal, right?

Soroush Khanlou
No, definitely not even close.

Chris Dzombak
The fact that it's coming from Chris, I think, means that it is something that the Swift team probably has talked about before.

Soroush Khanlou
Right. It also seems like something that this isn't Chris Latinor's first language and he's probably thought about these problems a lot. And so this is kind of his brain dump of all the stuff he's been thinking about for a long time. Not to say that it's necessarily right, but just to say that it is the product of a lot of thought.

Chris Dzombak
Well, he and other people have thought about this quite a lot and have landed on kind of similar solutions. And that's what I wanted to talk about today. So this past weekend, I stumbled across a bookmark that I hadn't read that was in my pin board unread queue from 2013.

Soroush Khanlou
Oh, wow.

Chris Dzombak
Yeah. But the queue is now empty, so that's good. And this was talking about it was a post talking about concurrent and distributed programming with Erlang and Elixir. For those of you who might not be familiar with this, erlang is a programming language and virtual machine which was developed back in the 1980s at Ericsson Like telephone company to provide a highly parallel, highly concurrent and highly fault tolerant programming language for use in telecom applications. And Elixir is a more modern, more Ruby esque language that's built on the same like, built on top of Erlang. It runs on the Erlang virtual machine. And we'll include some interesting reading about this in the show notes as well. But that's really what you need to know for this episode, or that's almost what you need to know for this episode. The other thing you need to know for this episode is that the way Erlang provides this highly concurrent, distributed and fault tolerant programming environment is with something that looks very, very similar to the actor model in general. Not necessarily super similar to the actor model, as Chris has proposed in Swift. But Erlang provides these properties which seem like very good properties, and which we know can be used to build large, distributed and highly concurrent, very reliable systems. They do it with the actor model. And in the last episode, or in episode 42, we talked about how, in the sort of, quote unquote reliable actors model that Chris proposes, how an application or how the runtime should handle an actor failing or an actor crashing. And I got thinking over this weekend about Erling has handled this problem and deals with it, and I assume deals with it in a fairly successful way. And so I thought that it may be interesting to look at what lessons we may be able to take from the Erlang world when thinking about what should happen when a reliable actor crashes in Swift.

Soroush Khanlou
So I didn't know much about Erlang before you sent me all this homework to do. And there are a couple of things I thought were really notable that I think are worth talking about. One is that almost every single one of the blog posts that I found about Erlang, and specifically about actors in Erlang started off the exact same way, which is like, Moore's Law used to be really good, but now it's kind of letting us down. And instead of adding more clock speed, we're going to be adding more cores.

Chris Dzombak
Okay.

Soroush Khanlou
There's thousands of cores per processor, and therefore we need a highly scalable, concurrent programming. And it was like all of them started exactly like that. Without fail. Like the first three paragraphs were about, we're going to have more cores, we're going to need concurrency, we're going to need parallelism. And Erlang brings it to us. And then they would go into the definition not to say that that's wrong or bad, but just to say it was really funny. They were all exactly like that.

Chris Dzombak
I'm just going to call out that I really enjoyed the voice that you were using.

Soroush Khanlou
Yeah, we got to bring that voice back.

Chris Dzombak
More cores. Two cores, too. Furious.

Soroush Khanlou
Yeah. That's my morning zoo voice. Or maybe my monster truck announcer voice. Sunday, Sunday, Sunday. The other thing I thought was really cool and notable is that Erlink supports hot swapping code while the process is running.

Chris Dzombak
How wild is that?

Soroush Khanlou
Yeah, completely bananas. And so the whole idea is that the whole system never goes down even though you're making upgrades to parts of it, which is pretty amazing.

Chris Dzombak
And that totally makes sense when you consider the origins. That means that you can continue to upgrade your system while still not dropping telephone calls.

Soroush Khanlou
Right? Exactly. And of course, the telephone calls may be happening while you update the code.

Chris Dzombak
Right. It's completely nuts, right? Yeah. I say this not actually having written any Erlang, but it's a really cool language. I guess the other notable thing to call out about it is it's a pure functional language. It's not object oriented at all.

Soroush Khanlou
Well, I think the actors are objects.

Chris Dzombak
Well, the actors are. Let's dive in here. While I was reading all this, I made a few notes and you just touched on something that is the first bullet point in my notes. So let's dive in.

Soroush Khanlou
So I'm really, really interested to hear where the bullet point is. I also have a broad actor model thing I want to touch on so you tell me where that fits in.

Chris Dzombak
I don't know what your broad actor model thing is, so I don't know where it is.

Soroush Khanlou
You do. Your first bullet point. I'll fold my thing in.

Chris Dzombak
So my first bullet point is that in Erlang, it's cheap to create processes much cheaper than creating a new process on a conventional operating system. We're talking about processes in the Erling VM. These processes are isolated. They don't have any shared state. They communicate solely via message passing. That message passing is abstracted so that it can work via the network. So you can have distributed processes. And these processes can fail independently. And that works because they don't have any shared state. So one process can fail or can crash. And that sounds a whole lot like actors, and particularly reliable actors that were proposed in Chris's manifesto here.

Soroush Khanlou
Right.

Chris Dzombak
And so that's where I guess although you don't have Erling isn't like object oriented in that you're creating like an object hierarchy. You have processes that you pass messages between. And these processes are purely functional.

Soroush Khanlou
Right? Well, they do have state in the sense that you basically get to say, the next time I get a message, my current local state should look like this. Right?

Chris Dzombak
Yeah, I guess that's true. Okay, so that's kind of where I'm at with my first bullet point. Erlang has these quote unquote processes that look and feel a whole lot like actors and can even be distributed over the network.

Soroush Khanlou
Right. Yes. One of the posts I was reading, I think it's the fifth one in our show notes as of right now, it's the rocketeer be one. It's called concurrency. And Erling and scholar the actor model. And I don't know what happened, but while I was reading this, I had a serious light bulb moment where I think I finally actually understood what the actor model is.

Chris Dzombak
Really?

Soroush Khanlou
Yeah.

Chris Dzombak
That's awesome.

Soroush Khanlou
So we talked last time about how the term object oriented programming has kind of been overloaded. And the thing that we do in Java, while that's the most canonical or the default thing people think about when they think about object oriented programming with the inherent hierarchies and the shared mutable memory and everything, that's what people think about when they think about objection oriented programming. But it's not really true to the original whatever. The original thing was about message passing. The original thing was about by the.

Chris Dzombak
Original whatever, you mean like Alan K's sort of original object oriented message passing small talky. Exactly.

Soroush Khanlou
Right. And he wanted those objects to each kind of be their own little computer and to kind of each have their own little state. And the thing that clicked for me was they talk about a different way of concurrency and they talk with the actor model and they say, this is the problem with threads. And it's like, well, we have to do this threading thing because we want execution to happen over here versus over here, then we don't want to have lost updates where two things read something and then one writes and then the other one writes and then one of those writes is lost. And then so we introduce locks and then introduce deadlocking. And it's like the whole solution to this problem is that it's completely bananas that we allow an object's internal state to be mutated by another object on another thread and you can really see.

Chris Dzombak
That as just an artifact of the effectively C based heritage of a lot of modern programming languages right. Where totally, you just have a giant array of memory and a bunch of shit operating on that array. And that's not at all like small talky object oriented programming.

Soroush Khanlou
No. And if you think about well so if you take the functional Haskelly approach you avoid mutating shared state by basically making the state immutable in this you avoid mutating shared state by making the state not shared. So you take away the other side of the problem and it equally solves the same thing. And there was like this just elegant, dimorphism, whatever you would call it, an elegant parallel structure that I saw. And then just like the whole thing just kind of clicked for me. And I realized the fact that in objective C or in Swift today, you can write code where you're writing one thing that mutates your own internal state, and then you call something that has a completion block, and then that completion block then fires on any thread. It can just happen anywhere in the system. It's completely bananas.

Chris Dzombak
It is.

Soroush Khanlou
It's crazy. And then the Erlang way of doing this is basically you pass yourself as an actor and then you get called back with a message and it's your responsibility to handle that message. And that is just like so much better of a system because you never have to share your state with anybody. All you have to do is make sure that your boundaries are defined well. And that was a real light bulb.

Chris Dzombak
Moment for me and I'm going to posit here. One of the benefits of having well defined boundaries always is testability. For sure.

Soroush Khanlou
Totally.

Chris Dzombak
I know nothing about unit testing. Erlang, I'm guessing, erlang process fairly testable.

Soroush Khanlou
Yeah, because you don't have to worry about Asynchronous City. You don't have to worry about what the object is. Everything is loosely typed. So it's probably a really chill test.

Chris Dzombak
Probably, yeah. As long as we're talking about the fifth article on Show Notes concurrency in Erling and Scala the Actor model, I'll note that that article also talks about Scala where you don't even necessarily have to pass yourself as an actor to whoever you're passing a message to. Scala's Actors library has some functionality built in to let you reply simply without having to pass yourself as an actor all the time. And so that's a nice bonus too.

Soroush Khanlou
Right? So I actually didn't like that as much. Just because it can cause Deadlocks, where if two actors are waiting on each other to reply, then it'll just lock up. That seems bad.

Chris Dzombak
That's not because it automatically will pass you and let you reply. That has to do with Scala's ability to let you do synchronous calls to other actors.

Soroush Khanlou
Right. And it just seems like you should disallow that if it means you'll never have deadlocks.

Chris Dzombak
Yeah. Although that is kind of going back to Scala's more like kind of object oriented, kind of functional, super pragmatic philosophy. But that's not part of the Swift proposal, so I kind of want to exclude it from discussion right now.

Soroush Khanlou
Yeah, that seems fair. Yeah. Just we're noting that Scala has the ability to reply, to handle the reply.

Chris Dzombak
Basically well, to handle it synchronously instead of asynchronously.

Soroush Khanlou
Right?

Chris Dzombak
Yeah. Interested readers encourage you to read all of the links in our show notes, but especially this one that discusses Erlang and Scala. So where do we go from here? In Erlang, we have these actors which are in Erlang are called processes. They're isolated, they can fail independently. What happens when one fails?

Soroush Khanlou
Right. You need some sort of way to bring it back in a lot of cases, right?

Chris Dzombak
Yeah. So, crucially, this is going back to our discussion between option one and option two for dealing in Swift with.

Soroush Khanlou
Right. Remind me, what are the options again?

Chris Dzombak
So, option one was that you have the opportunity to register, sort of at the application level, a failure handler for when an actor fails or when an actor crashes.

Soroush Khanlou
Right.

Chris Dzombak
Option two was to make every method on a reliable actor throw with the semantics that it will throw if that actor has crashed.

Soroush Khanlou
Right.

Chris Dzombak
Having thought about this, having read about how Erlang and about how Erlang handles this, option one, something like option one is clearly the right choice. Option two is horrible. Don't sound dramatic. Option two is a very, very bad choice.

Soroush Khanlou
Yeah.

Chris Dzombak
So the way that Erlang handles this is you have other kinds of actors, other kinds of processes, which are called supervisors. Now, this isn't any sort of like magic god actor that the runtime provides or that the language provides. These are just other actors, but they're processes that just have the responsibility to watch over one or more other processes and restart them when something goes wrong. So there are a few crucial takeaways here that I want to note. First of all is that this is fairly similar to option one in the Swift manifesto, in Chris's Swift manifesto, which is that it's more of an application level failure handler for when something goes wrong. It's not something that we don't push this responsibility out to the call sites within actors, like I think I might have said in the last episode, and, like, I definitely believe now, option two just pushes way too much. Responsibility out into various other parts of your application, and you're probably going to end up delegating a lot of that responsibility back up to some central object, like a supervisor, anyway. So supervisors in Erlang just process or an actor like any other that watch some other processes and restart them when something goes wrong. And so there are a few things to note. Feel like I'm talking in circles. Few other things to note here. A supervisor is responsible for starting its workers in this way. You end up building kind of a tree of supervisors and workers in your early application. So a supervisor may be responsible for some number of workers that just do something and some number of other supervisors which themselves could fail and need to be restarted depending on how you've structured your application. And these supervisors can be things that you write yourself that are really simple or the I don't know if this is the language or if it's a standard library like thing, or if it's a project that is a standard open source library to include in an Erlang project. But something called OTP, I don't even know what that stands for offhand I used to know but I've forgotten, provides some sort of stock supervisors that will do useful things for you out of the box. And that's something that I would like to talk about here. Does this all make sense so far? Should I keep talking? Do you want to interject at all?

Soroush Khanlou
So I have one thing that's not totally clear to me. So, first of all, OTP stands for Open Telecom platform. And it's a framework that basically contains a bunch of things that you will probably want in the course of your development of your system. A number of ready to use components.

Chris Dzombak
They say, okay, cool.

Soroush Khanlou
Yeah. My question that is not clear to me is, is a supervisor something special that's provided by the system, or could I just write my own supervisor as write my own actor and make it work as a supervisor? Is it like a lowercase s supervisor or an uppercase s supervisor?

Chris Dzombak
It's not something that is magical and built into the system. And this is kind of cool. And I think it could line up really nicely with Swiss very standard library, heavy philosophy. It's something that you can totally build from scratch yourself using primitives in the language, using languages, concurrency primitives, and I think that's cool. So you can build one yourself or you can use something from OTP that does something useful out of the box.

Soroush Khanlou
That makes total sense. Okay.

Chris Dzombak
I want to talk a little bit about how I think this sort of thing could fit really nicely into Swift in the manifesto that could that Chris has written. But I want to go over just a couple of those useful things that the OTP supervisors can do for you. First of all, you can tell one of these supervisors only try to restart your child processes, or your child process three times or so many times, implement some sort of limit, implement some sort of timeout, and if they keep failing after that, then you yourself should crash. Right. You yourself should fail.

Soroush Khanlou
Right.

Chris Dzombak
And you can see where any number of cases where that behavior might be useful, particularly in a networked sort of application where your actors are distributed, which I think is where Chris is angling in the long term with this manifesto. Right?

Soroush Khanlou
Right.

Chris Dzombak
There are also some different restart strategies that you can choose. So you can imagine a case where a supervisor is responsible for some number of workers, and if one of them crashes, you want to just restart that one worker. That makes sense. That's sort of the trivial case, right?

Soroush Khanlou
Yes.

Chris Dzombak
You can imagine a case where maybe there are some dependencies between these worker processes and it depends what order they're started in. So OTP provides a supervisor that will implement this strategy where if one process dies, if one of its child actors dies, it'll restart that one and everything that was started after it. So that allows you to maintain whatever dependencies you had going on. Right. That lets you maintain that graph. There are a few others, if I'm remembering right, there's one where if one child process dies, you can just kill and restart all of your workers. Like, maybe you know that all those workers depend on some common resource, and if one of them dies, screw it, just restart everything. And so you can see where these seem like useful models for dealing with failures of one of these fairly independent actors. Right?

Soroush Khanlou
Right. So you need some method. I kind of see this as living between options one and two, where it's not that every method throws and it's not that there's some global handler that you install, but each worker. That's one of the things I don't know if you mentioned this that's one of the things they talk about is like it's either a worker or a supervisor. And that like, semantic difference helps you keep things clean. Each worker basically has a parent, and that parent registers. Like, I think in this sense, it sends a signal, which is like a low level Posixy type thing. But I think you could implement that with higher level, some sort of higher level communication pattern, and you would just say, like, hey, when this thing fails, let me know when that thing failed, how that thing failed. And then from that I can build my behavior of my supervisor. For which things should I restart?

Chris Dzombak
Yeah. And so I think it's important to call out here that this isn't exactly option one. This isn't exactly like implementing an application wide handler for when an actor fails. I think that if you're opting into this reliable actor model, let's remember that we're talking totally in the context of, quote, unquote, reliable actors that have these special failure semantics, normal actors, which would be more like standard objects in your application, if one crashes, takes down the application, right?

Soroush Khanlou
Yeah.

Chris Dzombak
But these reliable actors, I think it probably makes sense, having thought a little bit about how you might use these, about what kinds of things a reliable actor might represent. I think it makes sense to be able to specify some sort of handler per actor about what happens when one fails. And this is where I think the Swift like a very standard library heavy, not putting too much in, really, language, primitives philosophy can really come into play. Maybe at a language level, you do just get some sort of callback when an actor has failed. And maybe I haven't thought this through at all. Maybe you have some special kind of reference to that actor that only lets you do certain operations that we know are going to be safe, given that that actor's memory space might be in some weird state. Right, so maybe you have some special kind of reference to this actor that actually lets you do things. Then maybe the standard library can provide some supervisor like mechanisms for building out this dependency tree, where you can specify which actors depend on which other actors, or maybe which actors start which other actors. It seems like there's room here for the standard library to provide some sort of functionality that lets you opt into different behaviors for reliable actor failure. Because having thought about this a little more, I don't think there's one right answer right there's. Replace one actor when one dies. That's not necessarily right. Maybe it's something that can't even be restarted, but sometimes it is. So this really has to be up to the application. But I think there's a lot of room for the minimum language level features that are needed to let the standard library implement some of these common options for what people will actually want to do. Does this make sense?

Soroush Khanlou
Yeah, it makes total sense. And we talked a little bit about this in the other episode where we said sort of that there are different types of actors and they would need different type of restart strategies. So one we said was like, okay, if you had a big web server and you need a bunch of actors to handle requests, those requests, like, if one dies, you could just respond, it doesn't matter. But then if you have a different situation, like one connection to this database that might need a slightly different strategy for restarting, where maybe you restart your.

Chris Dzombak
Actor that has a connection to the database and also restart any actors that are depending on that database connection.

Soroush Khanlou
Exactly. Yeah, totally.

Chris Dzombak
And this is something I'm really, really liking the philosophy, where this isn't something that you necessarily have to implement totally in your application, but where the standard library gives you the tools to say, hey, all these requests are depending on this actor, and there's some sort of policy in place for when this database actor fails, right.

Soroush Khanlou
For the listener. If you want to follow along with stuff we're talking about right now, the who supervises the supervisors articles, the third thing in the Show Notes has really good diagrams of how each of these restart strategies works and how these dependency trees might work.

Chris Dzombak
Yeah. Honestly, I really feel like you, the listener, just read all of the especially the Erlang processes, supervisors fault tolerance and erlang, scala related articles in the Show Notes. It's going to be really interesting. It'll take less than an hour of your time. Maybe an hour of your time.

Soroush Khanlou
Yeah, I think an hour of time is right. If the articles are really interesting, we will talk about them here. We'll tell you which ones are which. But in particular, I wanted to call that up because the images do help while you're listening to us talk about it.

Chris Dzombak
Yeah. And I've been thinking a lot about this for the last few days, so I apologize if I'm saying something that seems clear to me, but I'm not articulating. Well, I'm sure I'm doing that.

Soroush Khanlou
No, I think you're doing a good job. I think you're definitely on the right track here. I think both the solution of everything has to throw and the solution of everything has to have a global handler. Both are kind of distasteful in their own ways, and this one bridges that gap a little bit where you say, well, some things need to know about if this fails, but other things don't.

Chris Dzombak
Right. It's like we need a per actor handler, but that's not enough. We need tooling to implement different behaviors, to implement different policies in that per actor handler. And that's where I think the standard library comes into play.

Soroush Khanlou
Yeah. Now, one question that I have is in Erlang, any message that you send is not guaranteed to be received by the actor. It may just kind of get lost in transmission. I believe that's right now, the question is, let's say you have an actor that is reliable, so it is marked as reliable, and that means that it can fail, which I still think that's a little backwards, but whatever.

Chris Dzombak
Yeah. Naming is weird in a few places.

Soroush Khanlou
Right. So let's say you have that actor and you call a method on it and you're awaiting that method, right. While you're awaiting that method, that actor may go down because of some other thing that's completely unrelated to what you wanted to do, but because it's a serial queue, your message couldn't get executed. Until the other message gets executed, that fails and there's no method to restart the thing. If you're expecting a value back, like, let's say you're expecting a non optional user object, your code can't continue.

Chris Dzombak
Yeah. I guess you have no option but to crash in that case. Right.

Soroush Khanlou
So you have a couple of options. One is everything that is returned from a reliable actor could be forced to be optional that's one. Or provide some default value in case it fails. So like maybe if it's a boolean, you don't necessarily want to return optional, you want to return false. There was some way to do that.

Chris Dzombak
Don't like that.

Soroush Khanlou
Well, it's the null object pattern basically. But whatever. Yeah, something, some way to say this thing didn't go through. And here's basically so we're giving you nil.

Chris Dzombak
I'm going to call out that false as a default boolean value is the worst possible illustration of the null object pattern.

Soroush Khanlou
I think the user would choose whatever they wanted for that particular thing. You could imagine it as just doing like question mark, question mark and then putting a default value at the end. Just the point is either returning nil or some other value that could represent like, hey, this failed. It could be an empty array, it could be whatever you want it to be. You could have that just it was an idea. It's not important to the core of the thing.

Chris Dzombak
Yeah.

Soroush Khanlou
So you could either have it crash the app, you could have it terminate execution at that point and just terminate the code routine.

Chris Dzombak
Right. It doesn't necessarily have to crash the app. It is to crash that actor.

Soroush Khanlou
Well, but even if it's in the main apps actor, you could terminate that code routine and then terminate the coroutine that calls that all the way up until you hit a begin async terminate that and then you're good. That's one option. I'm not saying it's good, I'm just saying it's one option and then the other option is to go back to everything throws.

Chris Dzombak
Yeah, that's true. So I hadn't really thought about yeah. Is there any requirement that things that call into reliable actors also themselves have to be reliable actors?

Soroush Khanlou
I don't know, some way of catching that error.

Chris Dzombak
Yeah.

Soroush Khanlou
So actually kind of now that I think about it, it does make some sense that all of the reliable actor methods throw because they represent something that is going to take a while to get is across some kind of network boundary. There are myriad things that can go wrong when that happens. Not just the actor went down, but also connection is weak, timed out, database line, hard line got cut, all that.

Chris Dzombak
What do you do when that throw? Okay, so it throws because the other actor crashed. I mean, what do you do from there?

Soroush Khanlou
Same thing as we do anywhere, which is nothing. Just quote, unquote, handle the error.

Chris Dzombak
Or fatal error. Yeah, basically. No, I think that having not thought this through very much yet, I think that the right thing to do is if you're like awaiting on if you're awaiting on a message from a reliable actor and that reliable actor crashes, I think you crash too. And if you're not a reliable actor, then the entire application crashes. If you. Are a liable actor, then you have crashed. And maybe whoever is supervising your particular chain of dependencies restarts you in a sane way, or maybe not. And that's right.

Soroush Khanlou
Yeah. To be totally clear, I do think that what I'm getting at is some combination of every method throws and installing.

Chris Dzombak
I don't think every method should throw, I really don't.

Soroush Khanlou
But how do you handle the case where the actor got torn down before your message got fired and now your Coroutine is hanging? Do you do the optional do you do the throws? Do you do the terminate the code routine or do you crash? I don't think you have any other options. You have to pick one or you say every reliable actor has to be brought up eventually or something.

Chris Dzombak
Given that scenario, I think you crash. Now, I'm curious about how do you know when you're waiting on a message from something that has crashed?

Soroush Khanlou
Oh, that's a funny idea. There's maybe some kind of mechanism with how weak works, like it will get nailed out. Not necessarily, no doubt, but something would message it and put it through the system.

Chris Dzombak
Yeah, I think there must be. I mean, if it would be possible to throw, which is one of the options, then it must be possible to exactly.

Soroush Khanlou
There's some way crap. Or you could switch to a system where every message is truly asynchronous and truly what do they call like send once or whatever and you don't hear back. You may just never hear back. And you have to set up your own time at Handlers or whatever.

Chris Dzombak
That's going to be hard for people to start using.

Soroush Khanlou
Yeah, I mean, I think that's true, but that's kind of where I'm getting at is like with a reliable actor, you have to have something for those messages that can't be executed.

Chris Dzombak
Yeah. Then you crash.

Soroush Khanlou
You can't just crash. You have to have so you're saying then what's the point of having reliable actor if it goes down, everything's just going to crash that's waiting on it?

Chris Dzombak
Well, no, not every well, everything that's waiting on it, because what else is going to happen? Everything that's waiting on it is going to return nil and send an error back, one or the other. Maybe you crash and whatever restart policy is applied to your database controller realizes, oh, this database controller crashed, all these things are waiting on it. I'm going to restart all of those at the same time I restart my database actor right. And you get a couple of chances to try again. And if that doesn't work, then the crash goes up the chain and maybe the server just like stops routing requests for a little while while you're waiting for the database to come back.

Soroush Khanlou
This kind of lands me in that same place of that we talked about. The top of the show of this is like it's just object oriented programming implemented poorly and when you implement it poorly and you have, let's say, a message that isn't actually a message, but it's actually a function call that you can await the results of, you end up in a sticky situation.

Chris Dzombak
Yeah. So I will admit I'm a little bit fuzzy on exactly what the semantics should be here in Swift. Like what this looks like in the language. I'm mostly trying to look at the big picture kind of ideas here for what we can take away. I don't know exactly what it looks like to specify some sort of policy that says when the database server fails, these other actors need to be restarted. I don't know exactly what it looks like to establish that relationship, but I think it's important that we be able to establish that relationship.

Soroush Khanlou
Yeah, I agree with you. I think that's right. And I think having a parent for an actor approach is the right approach for handling restarts, but I don't know.

Chris Dzombak
If it's enough well, remember, for handling restarts, or if you've tried enough times and can't restart or crashing itself, and whatever is above that does the same thing.

Soroush Khanlou
Yeah.

Chris Dzombak
One other question that I have about what this looks like in Swift. What do references to reliable actors look like? Particularly reliable actors that are distributed that you're talking to over the network? Is this just like a memory address that has some sort of proxy object that handles the that's like half runtime magic that handles this interaction over the network? Or like, what does that look like?

Soroush Khanlou
That is actually a great, great point, Chris, because what is that the memory.

Chris Dzombak
Address underneath one of these references?

Soroush Khanlou
So, yeah, some kind of proxy definitely has to exist there. But you know how you can mark something in Swift as weak and if it's weak, it has to be optional?

Chris Dzombak
Yeah.

Soroush Khanlou
What if any reference to a reliable actor had to be optional? And then any message you call on it, you call with optional chaining, and that's your error handling is if it comes back as nil, then you know that your actor doesn't exist.

Chris Dzombak
This is the same as forcing everything to throw and then forcing everything that touches one of these to deal with a possible failure. That feels wrong to me, but the.

Soroush Khanlou
Fact is that those things can fail, and they can fail at any time, and they can even fail on messages that you didn't even ask for.

Chris Dzombak
And so maybe if you expect them to possibly fail, then you represent your reference to this actor as an optional.

Soroush Khanlou
But isn't that what reliable means, is that I expect this to fail at some point in the future?

Chris Dzombak
Not necessarily. I think you have things that you expect might fail and there are things that if it fails, you're in kind of an oh my God, this failed, what is happening state.

Soroush Khanlou
Right.

Chris Dzombak
There are things that fail sometimes and that's fine. And there are things like fail sometimes and when it fails it means half of your data center is on fire.

Soroush Khanlou
Yeah. So what you could do with that is if you expect, hey, if this thing goes down, like my whole option go down then you just do like my actor exclamation point. The method that you want to call.

Chris Dzombak
In it yeah.

Soroush Khanlou
That mechanism exists in the language.

Chris Dzombak
Yeah. Feels messy. But does that mechanism still allow for specifying any restart policies and possibly custom supervisors?

Soroush Khanlou
Yeah, I would say I would want that and I would want the system where you have a signal for the thing went down and I want to handle a restart and maybe ideally if the restart could happen before the thing returns an optional that would be ideal and then that message just gets resent. But I think the true thing that I actually want is like you shouldn't be able to return anything from an actor.

Chris Dzombak
Well you're going to have to be able to return things from well you're going to have to be able to get data from an actor from actor A to actor B back to actor A.

Soroush Khanlou
Right. I want true message passing is what I want. And I want so you're saying you.

Chris Dzombak
Want like actor B to have to pass a message back to actor A?

Soroush Khanlou
Either that or like it does that and that just is the coroutine.

Chris Dzombak
I mean that can happen under the hood. That's fine. You can use Async Await syntax and the compiler can separate this into the right messages that go back and forth and then the other coroutine A continues. That's fine.

Soroush Khanlou
Yeah.

Chris Dzombak
Compiler magic. Thank you compiler developers.

Soroush Khanlou
All right, so we're running a bit long here. All these episodes have been pretty long, which has been fun to do. It's been so much fun outside of our wheelhouse.

Chris Dzombak
Yeah, it definitely has been a little bit outside, I mean, certainly outside of my wheelhouse. If any of you, our listeners, have feedback, positive or negative, if I've gotten anything horribly wrong, well I mean, like.

Soroush Khanlou
The long episodes versus if you prefer the short ones, let us know.

Chris Dzombak
Yeah, let us know what you think about just about this episode in general.

Soroush Khanlou
Yeah, for sure. Cool. Chris, as always, it was great to talk to you.

Chris Dzombak
Yeah, it was great to talk to you as well. This has been a fun discussion which I'm sure we'll revisit and thank you to all of our listeners. We hope you enjoyed this episode.

Soroush Khanlou
Pay for our Patreon so you can get access to the other episodes about Async Await and actors.

Chris Dzombak
Yeah, I was just going to call out. We do have a Patreon and our Patreon supporters are paying for production costs, editing costs, hosting costs and we really appreciate the support, it really does mean a lot to us and thank you to those of us who are supporting us on Patreon. There will be a link for that in the show notes. And it is eleven at night, so I think I'm going to go to bed.

Soroush Khanlou
Sounds good, Chris. I'll talk to you next week.

Chris Dzombak
Bye, sir. Bye.

