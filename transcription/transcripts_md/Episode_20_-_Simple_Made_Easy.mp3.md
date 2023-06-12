Speaker A
Welcome to Fatal Error. I'm Sirish.

Speaker B
And I'm Chris.

Speaker A
And today we're going to be talking about the rich. Hickey. Talk simple, made easy. We'll put a link in the show notes of the talk if you want to listen to it before you listen to our episode about it, there's an info cue page where you can watch the video and the slides at the same time. And we aren't sure if we have differing opinions on Simple Made Easy, so we're going to find out exactly where we land on this potentially contentious topic. So, Chris, do you want to give us an intro of what Simple Made Easy is all about?

Speaker B
Sure. So the sort of thesis, I think, for this talk, one of the core ideas is that simple and easy are actually not the same thing. It kind of seems like they should be almost intuitively. But when we're talking about software, when we're trying to evaluate the decisions that go into making software, into building a software system, it's important to keep in mind that these are different concepts and to think about them almost independently, if that makes sense. Are you with me so far?

Speaker A
I think so, yeah. I think I need a little bit more concrete of an example of what you think is something that's simple versus what you think is something that's easy.

Speaker B
Well, let me talk about it abstractly, just for a little bit more, and then maybe we can try to think of some concrete examples. But maybe looking at the origins of the words or looking at the words simple and easy, like what are the opposites of simple and what's the opposite of easy? The opposite of simple would be complex. The opposite of easy would be hard. And are complex and hard really the same thing? Those seem like they're not synonyms in the same way that it might seem like simple and easy are. Right?

Speaker A
Right. Sure.

Speaker B
So if the opposites are different from different concepts from each other, I think it stands to reason that simple and easy are really not exactly the same thing. So if we talk about simplicity, thinking about something that's simple, really what that means, or the definition that Rich puts forward as what it means for something to be simple, is there's one role or one task or one concept or one dimension here? And really it's about a lack of interleaving, something with other parts of the system. So it's some role or concept that really stands on its own that isn't heavily dependent or heavily interleaved with the rest of the system.

Speaker A
So while I like that from an abstract point of view, kind of one of the things we talked about in the single responsibility principle episode is that you can't just say one task, because a task could be so many things, and it's really hard to nail down. Exactly, hey, this is one unit, and it does one thing, but at some point, it does have to get interleaved with something else. Is that one task doing the interleaving? So that's where he starts to lose me, I think.

Speaker B
So. Whether or not you can come up with a sort of absolute definition of one task, I think it may be enough for this discussion for you to think about a spectrum of simplicity or spectrum of interleaving. Right?

Speaker A
Okay. I can work with that.

Speaker B
Something like an orm like an object relational model like database layer, I think we probably agree is pretty complex, pretty interleaved internally. Right. You have your model layer is pretty tied with the database, and it's a behemoth of a system. Right.

Speaker A
Even the most simple assumption about it, which is that every table maps to one class is a huge, huge assumption. And you can't separate those two things at all.

Speaker B
Exactly. So there are a whole lot of sort of interleaved concepts there. And what would be, I don't know, something like a key value store that is its own database. And then we have simple values in our model layer that we write to that database that seems simpler. Like you can isolate more it's less interleaved. You can isolate concepts more easily with that model. Right?

Speaker A
Right. Yeah.

Speaker B
So the thing to note here, if we're talking about simplicity as this lack of interleaving is it's an objective notion, right? This doesn't depend on the programmer. You can look at something and tell whether it's more or less interleaved, more or less complex than something else.

Speaker A
Yeah, I do like that distinction that he draws, that simple is objective and easy is subjective. Like easy depends on who you are, where simple doesn't depend on who you are.

Speaker B
Right. So that's where I was leading with this, is that the idea of something that's easy, it's something that is like, that's familiar, that you have at hand, that you already understand.

Speaker A
It's easy for you.

Speaker B
Right. And it's totally a subjective idea. So that's one of the first points that he makes in this talk, is that basically simplicity is objective and ease is subjective. You're with me so far?

Speaker A
Yeah, I feel you on that.

Speaker B
Okay. So in a lot of decisions that we make when we're building software, programmers and I mean, I do this all the time, tend to focus on the experience of using a tool or what Rich calls a construct, which is just some idea, a tool or an architectural pattern.

Speaker A
Right. Sort of thinking about the API of the thing rather than thinking about how the thing works internally.

Speaker B
Right? Yeah, I think that's probably a fair statement. And so Rich argues that it's really the way to evaluate a software system that we're building is the long term results of using our tools, of using our constructs, rather than the experience of programmer ease. That's a more like subjective and immediate thing to evaluate.

Speaker A
We talked about this a little bit on the not invented here. Crossover episode with Runtime as well, where we talked about how something like SV Progress HUD has a very simple API on the inside. But as soon as you start to do more complex stuff, you have to start building your own wrappers and your own things around it, because it doesn't have the capacity for those things.

Speaker B
I would say that SV progress HUD has an easy API, right? It is easy to use. It's near at hand. It's very familiar, it's one line of code. But there are corner cases that you can get into depending on how your UI is structured, where maybe assumptions that SV Progress HUD makes under the hood don't hold. And because it's an easy API, but the implementation isn't necessarily simple. Right. You have sort of a singleton instance, and it will find I don't know how it works internally, but it finds a window or like a view controller to present itself on. That's not simple. That's pretty interleaved with some assumptions about how the application works. Right?

Speaker A
I don't know, maybe I'm just taking semantic issue at this point. But it is simple to just say there's one SV Progress HUD. You only ever are allowed to use one. You can present it and you can dismiss it, and that's it. And that on some level is simple.

Speaker B
Well, I think that's easy. You have one and you know how to use it. What did you say? You have one and you present and dismiss it. Well, what do you present and dismiss it on? Right.

Speaker A
No, I agree with that, and I agree that there is interleaving there. But like I said, I think I'm just taking a semantic issue with the name simple versus the name easy.

Speaker B
Well, we're talking about semantics, I guess. So let me give you another example that I think is kind of a neat example of simple versus easy. Although I haven't thought too much about how well this holds in practice.

Speaker A
Let's figure it out together.

Speaker B
Let's do it. Cocoa Pods is designed to be easy, right? It's designed to be easy to integrate. You add some pods to a list and type a command, and boom, they appear in your project and it's ready to use. That's easy, I think, right?

Speaker A
Okay.

Speaker B
It's absolutely not simple. You've used cocoa pods and I've used cocoa pods for years. And I don't at all mean to pick on Cocoa Pods because that's a valid design goal for a tool, is to be easy.

Speaker A
Right?

Speaker B
But it's absolutely not simple. Right? First of all, it handles a whole bunch of things, downloading dependencies and integrating them into an Xcode project and resolving dependency conflicts or flagging dependency conflicts for you. Right? It's doing a lot of things and it's very tightly interleaved. Right.

Speaker A
I would say it almost guaranteed a brittleness well.

Speaker B
Right. And so that's one of the sort of trade offs that you make if you choose something easy over something that's simple, right?

Speaker A
Right.

Speaker B
Is that the ease often comes with some complexity or some hidden intertwinedness, for lack of a better term. Some hidden interleaving.

Speaker A
Right. So what would be an example of a package manager that is simple?

Speaker B
So I haven't used Carthage as much as I have used cocoa pods, but I think that Carthaged is designed much more in the simple realm. Right. It doesn't do quite as much for you, but it doesn't integrate things into your Xcode project for you. But with that simplicity it's also maybe a little bit like it's not quite as trivial to use you're integrating these libraries into your Xcode Project yourself, but it's a much simpler tool and in a lot of ways it actually turns out to be easier down the road when maybe initial integration is a little bit more work. But as you run into some odd corner case with some dependency, or as you maybe want to customize how something is integrated into the project, that simplicity, that less interleaving really does pay off down the road. And that's a point that Rich makes in his talk. A little ways into the talk, there's a completely non scientific graph on one of his slides, but that's basically saying, look, if you're choosing easy solutions, then it's faster to deliver things upfront. But as the complexity sort of mounts, because often the easier solutions try to just hide balls of complexity and as that complexity mounts, you will slow down over time. Whereas if you're really trying to architect a system with simplicity in mind, this requires design work and design thought and some upfront work that maybe isn't going to go over too well in a super agile startup. E kind. Of way because you're not going to deliver things quite as quickly right up front. But it pays off over time as you avoid growing these big interleaved systems that it's really kind of impossible to understand after a while.

Speaker A
Right. I do like this graph. This graph really does speak to my experience with running and working with older code bases and stuff like that. It does feel right.

Speaker B
And we'll screenshot, we'll add that graph to the show notes too.

Speaker A
Yeah. So this idea that can you have something that's kind of both simple and easy, where when you start out, you can you can, you know, invoke simple things or you can invoke things that you want to do really quickly. But if you need more complexity, you can kind of dig in a little bit, down a couple of layers and do the stuff that the simple invocation does. Do it yourself and gain that sort of flexibility back. I'm reminded of an article that I can't find about it's like the Python File Open API, which is this blog post where it describes like if you want to just read a file, you can just use the open free function and it will just do the right thing and it'll just give you something. But if you want more data or like if you want more information or more control over exactly how it works, you can dig in and do the same thing that the open API is doing, but do it yourself and then you're given all this extra control and you're given all this extra ability. And sort of like Chris Latner has said, that Swift works like this as well, where if you want to just write hello world, it's one line. But if you want to write a whole complex mac application, you can do that too. And the thing is that the tool gives you the ability to sort of scale up from the very beginner quite a simple thing. Like when you call print on some level, that is not simple. That is talking to buffers. That is assuming a whole runtime. It is assuming knowledge about a whole set of string APIs and how they work Variatic parameters. Just tons of stuff that happens when you call a simple thing like print, but you can slowly crack into it and say, well, I don't actually want you to print this way. I want you to print that way. Or I want the line Separator to be like this and not like that. And so is there a space for something that does that? Progressive disclosure in rich's, simple, made easy world?

Speaker B
I don't know if he talks about this in the talk directly, but I think there absolutely is. Right? I mean, we've done this with one of our internal libraries at work that's used by a few different iOS teams. It's a library that handles login and purchasing and that kind of stuff with our ecommerce system and our whole site wide login system.

Speaker A
So it's sort of your API layer, right?

Speaker B
Well, it's one of our API layers. Right, right. And that's something where there's kind of a lot going on there. Like we have the ability to log in with the username and password or with Google or Facebook. You could be subscribed to one of any number of different packages that we sell or have sold over the years, like different subscription levels. You might have subscribed through itunes, not through our website. So there's like quite a lot of quite a lot to handle there. But we didn't want to build a library that was just a whole ball of yarn that it was impossible to untangle. And so ahead of time, we did a whole lot of work in really thinking about, okay, what constructs are here, what responsibilities does this library have and how can we tease these threads apart into discrete pieces of behavior and discrete pieces of data? And then we wrote those discrete pieces of behavior and discrete pieces of data and then as it turned out, those are something that it's useful to have around. And I mean, certainly it's nice to be able to work on some discrete piece of this library when you're adding a feature or fixing a bug. But that's kind of a pain to use for a client application in most use cases. So then we also added a I guess you could call it kind of a coordinator object that ties all these pieces together in a pretty typical way that most of our applications would want to use these pieces. And you still have the opportunity to pull out one of these pieces and use it directly if you want to do something that the coordinator doesn't handle. But in that way, this library provides kind of an easy API for common use cases and lets you pick out pieces and use them almost independently or customize them independently if you need something that the easy wrapper doesn't provide. And I think that's a useful pattern. And the only thing that I would point out is that you still have to do the simple design work up front. You're not going to build an easy API and then expose simplicity. Right. You're going to build a simple system and then maybe add some sugar that you can use to add ease of use to it if you want.

Speaker A
Right. Well, the other way, I think, is also complex or is also difficult to manage, let's say, in order to not overload our terms here. The other way is also tough because you start with an API that is your ideal, and you want to try to make the system, the software system behave, and you want to be able to get access to the things you need access to, even though you want to limit yourself to kind of this original API. So the other way, I don't think either of the ways is less challenging in terms of developer effort. Does that make sense?

Speaker B
Do you mean from the perspective of implementing a library or yeah, let's say.

Speaker A
You'Re building an API and Alice wants to make a simple API and Bob wants to make an easy API. They're both going to put in a good amount of work to achieve those goals. They're both goals. Neither of them comes for free.

Speaker B
Neither of them comes from free. I do think that designing the simple API first is going to if you don't design the simple API first, then you're very likely to end up with a very interleaved system in your library. And it's going to be hard to tease that apart and expose simple parts of that functionality for use.

Speaker A
So I don't disagree with that. I think Bob doesn't care about the interleaving. Bob doesn't care about the in richest terms, complexity. He just wants he only wants an easy API. And I'm just saying, like, you don't get that for free. You have to try for that as well.

Speaker B
We've been talking about, I think, sort of implicit in the discussion we've had so far is that simplicity is hard and complexity is easy. Right. And I don't think that that is necessarily true either. I think that's kind of a false dichotomy. It's possible to build something that is both simple to both simple, like it's not heavily interleaved and that is easy to understand. And you achieve that just by really teasing apart the different sort of threads in your application and creating appropriate abstractions and using in Swift protocols, but using like polymorphism and things like that to avoid mixing these abstractions. And that's something that takes a whole lot more effort or a whole lot more effort than building just something that's easy from the outset. But I do want to call out that easy does not necessarily imply complexity and simplicity doesn't necessarily imply that something is hard.

Speaker A
Right? Okay. I do think that's one of the big things that is tough to swallow about his talk is it sounds like he's just saying, well, easy is just useless and we should just throw it down the river and everything should be simple and hard, basically.

Speaker B
I don't think that's what Rich is arguing at all here. And toward the end of the talk, he has a slide which, if I'm remembering correctly, is entitled Simplicity Made Easy. And I want to scroll down to that in the transcript here and we.

Speaker A
Put a transcript in the show notes, if that's helpful for anyone.

Speaker B
Right. I do highly recommend that you take a lunch hour and watch this talk. It is a really great talk. So, Simplicity made Easy choose simple constructs over complexity generating constructs. Earlier in the talk. Rich spends a whole lot of time going over what simple constructs are versus what similar constructs are that generate complexity. So that's kind of a throwback to earlier in the talk. Keep in mind that we're not necessarily trying to evaluate how easy it is to author this code. We're trying to evaluate whether it's possible to understand the artifacts, whether it's possible to understand the code that's been written months or years down the road. It's not going to be you maintaining this code. In all likelihood, can somebody else look at this and understand what's going on? Create abstractions that have simplicity as a basis earlier in the talk? Again, Rich goes into quite a bit of detail about how to tease apart what the right abstractions are when you're really trying to take simplicity into account. He notes that simplicity often means making more things, not fewer. And this is really throwback to our single responsibility episode where, yes, okay, we maybe don't know how to say exactly what a responsibility is with absolute precision, but we can tell when something has more responsibilities and when something has fewer responsibilities, right.

Speaker A
And you know that that means you're going to have to create more types to spread those responsibilities out thinner and make them reusable.

Speaker B
Right? So create types to represent these responsibilities or these abstractions. Use protocols, use polymorphism so that you don't end up having a network of types that all just depend on other concrete types. Right, that certainly helps, but it doesn't really get you all the way. It doesn't get you everything that you could have and then simplify the problem space before you start and that's just really think about the problem you're solving before you start writing code to solve that problem.

Speaker A
Right, right. I mean, I think a lot of these conclusions are easy to agree with, but in practice, obviously, yes, create abstractions that are simple. Like that is the ideal. And ideally, those abstractions don't leak and you can just reuse them all over the place and they're great. But in practice, you end up having a tough time with some of those. So, for example, one really practical thing is I think that simple versus easy sometimes stands in for the functional versus object oriented divide. And so especially when we're talking about iOS code, that ends up looking something like, well, should you use signals or reactive programming of some sense, and that is simple but hard versus should you use something more traditional, delegates, blocks, whatever. And I would actually, probably, as much as I love promises, probably lump promises in with signals in this case, because in some sense they're not really simple like promises. Like, I've written a library and it does really interleave the idea of asynchronous work. It interleaves the idea of what queue you're firing on the concept of this thing being delayed over some period of time. Signals. Add to that the interleaving of how to decide how to merge two signals and all those components. So simple made easy is fine in the abstract, but when you get down to the concrete of it, we're making complicated apps. And something like a signals implementation like that is an abstraction that can work over many different things, but it's definitely not simple. It's definitely got a lot of complexity and ins and outs and things that work together that can't be separate. And again, promises, I think, are the same way. If you use a promise abstraction, you can't cancel things like you have to use something else for that part of it. It makes the call site much more powerful, but it also makes that internal implementation is definitely not what I would call simple.

Speaker B
So boy, okay, let's see. I have a lot of thoughts here to respond to something that you said at first. I think that sometimes the simple versus easy argument distinction is overloaded to mean like an object oriented versus functional sort of distinction.

Speaker A
Right?

Speaker B
I don't think that that's really true or valid. Rich certainly isn't arguing that here, although he does have some tables that compare constructs that are complex versus constructs that are simple. And some of the more sort of functional ideas do end up on the simple side.

Speaker A
Well, and the complex ideas ends up on the object oriented side. Like he talks about inheritance, he says this is inherently complexed. He talks about versus identity and that's complicated, right.

Speaker B
But something like protocols versus inheritance protocols is something we use in object oriented programming, especially in Swift. And that's something that Rich uses as an idea of a way to achieve simplicity right. Is heavy. So of protocols for your types. I don't think it's really valid to say that simple versus easy is about functional versus object oriented because we can absolutely describe interchangeable abstractions and we can avoid a lot of complexity in object oriented programming. Some of the other constructs that Rich uses an example as examples of things that let you get simplicity. Things like queues, like we use queues with GCD, right? Queues are a nice way to avoid some complexity that comes with, say, thread based concurrent systems. Right?

Speaker A
Yeah. I would say queues are very simple.

Speaker B
Right. So let's talk about promises. Let's talk about promises right now. I feel like they actually simplify. They simplify things versus an older way versus doing something with the sort of traditional cocoa callback blocks. Right. Because the way I haven't thought this argument through, but hear me out here. The way that you might write something that handles something that calls in asynchronous API and hands it a callback block and then you get that callback block, you're sort of really interleaving the idea of time with the rest of your code here, right? Like, you know, this callback block will be called in the future and it's going to do some things and there are probably going to be some assumptions like this object is still going to be or the object that called this API is still going to be around. And so you're sort of writing imperative code here that's jumping back and forth across time. And that is kind of interleaving the concept of data and time. And Rich specifically mentions that state interleaves or complex is the word he uses. But the idea just of mutable state really interleaves the idea of a value in time. And that is really kind of what we're doing. Often if you call an asynchronous function and hand it a callback block is the code that you're writing is sort of jumping back and forth across time. And that's kind of hard to manage. I mean, you can get used to it, but it is still a little bit complex to keep in your head what's being called and what's being touched in this run loop iteration versus sometime in the future. And promises take that and say, okay, you are no longer worrying about this. You can write a chain of almost like declarative data processing or data manipulation, right. And the library is going to take care of all the time stuff for you. And you're left with just a type that represents that represents a future value. Right. It's still true that asynchronous work may happen and there is still maybe some complexity there, but it's taking this sort of very interleaved concept of time that you're writing into code and extracting some of that interleaving. Right. It's untangling things a little bit.

Speaker A
So my only problem with the way that you're laying things out is my understanding was that easy was about making APIs that were simple versus implementations that were complex and simple is about making APIs that have more stuff in them. Like the interface has more stuff in it, but the actual implementation of the thing is simpler. And that's, I think, not what's going on here, because the implementation is so complex and the API is so simple. So I think we are ending up more in an easy place than a complex place or than a simple place. Sorry.

Speaker B
The way that I'm thinking about this is taking the resulting system as a whole, and this kind of includes implementation concerns and an interface concerns of your code and of the libraries that your code is using with something like an Orm. There's a whole lot of complexity there, and that complexity is going to leak out almost necessarily into your code just via its API, via the assumptions that are embedded in using an Orm.

Speaker A
Yeah, I think anybody who's used core data can agree with that.

Speaker B
Right. So are simple and easy the same thing?

Speaker A
No, they're not. But I will add the caveat that things that people think are simple and things that people think are easy don't often agree.

Speaker B
Oh, you mean that different people think different things are simple? Exactly.

Speaker A
People think different things based on your political ideology of programming rather than your rather than anything objective, then I'm thinking.

Speaker B
Maybe I did a poor job at trying to explain what simplicity I don't know.

Speaker A
Or maybe Rich Hickey is wrong.

Speaker B
No, I don't think Rich Hickey is wrong.

Speaker A
I don't think that can't be right. That doesn't seem right.

Speaker B
What's the fallacy argument from authority?

Speaker A
Something like that.

Speaker B
Appeal to authority.

Speaker A
There you go.

Speaker B
Yeah, Richiki said it, therefore it's true.

Speaker A
Yeah.

Speaker B
No, I mean, like interleaving is objective and complex and ease of use is subjective. Yeah, well, and Richiki says so it's true.

Speaker A
I would just say a lot fewer startups would exist if they had to write their or if they had to write their Crud apps in Haskell instead of Ruby or whatever.

Speaker B
I'm not saying anyone has to write a Crud app in Haskell. I'm saying that you're writing this in Ruby. Really consider what objects you're creating and what interfaces you're creating.

Speaker A
Like, Active Record Base is the complex Complexor in the world. Like it's the worst.

Speaker B
Yeah, it does everything not great.

Speaker A
No.

Speaker B
But it's kind of easy.

Speaker A
It is definitely easy. And I think that's what Richard Key is really railing against. And even I have a I couldn't disagree that Active Record Base is very complex and very complex and it is easy. So it does fall into that sort of that quadrant of. The two by two grid.

Speaker B
So this seems like as good a place as any to leave it.

Speaker A
Yeah, it seems right to me.

Speaker B
Thank you to all our listeners. Again, we've really been blown away by the level of support that we've gotten from everybody, and we really appreciate you listening to us talk for 30 minutes a week.

Speaker A
Yeah, much appreciated. Thanks, folks.

