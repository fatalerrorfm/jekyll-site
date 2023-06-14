Soroush Khanlou
Welcome to Fatal Error. I'm Sirous.

Chris Dzombak
And I'm Chris.

Soroush Khanlou
And today, Chris and I are going to talk about error handling in Swift. When you should use things like Fatal Error, when you should use Swift's built in error handling, when you should use something like a result type or some other abstraction, when those things are where those things have their strengths and where they have their weaknesses. So we're literally going to be talking about fatal errors on Fatal Error.

Chris Dzombak
Oh, the irony.

Soroush Khanlou
The irony, yeah. So Swift ships with a default error handling model, and it's a very type Systemy one, I would say if a function is going to throw an error, it has to be declared as throws. And any context that calls that function needs to handle that in some way, either by saying if there was an error, you should crash, or if there was an error, give me an optional value, or handle it explicitly and saying, I want the error, I want to handle it and do something with it.

Chris Dzombak
Right. And so some interesting things to note about Swift's error handling approach, which we'll add a link to some documentation about that in the Show Notes, but we'll kind of assume that most listeners are at least somewhat familiar with it here. Interesting things to note are that unlike with something like exceptions, this isn't quite like an exception handling mechanism. Exceptions aren't going to propagate automatically. You're going to have to propagate an error up the chain manually if you want something to propagate. And really a better way to think about Swift's throwing errors is almost more like just another like adding an error return type to a function. So a function can return either whatever value it was going to return before or an error. It really is just some almost syntactic sugar and type system sugar around having an error of return type. That makes sense.

Soroush Khanlou
Yeah, totally. And you'll note that blocks that you handle hand to defer will get called whether you throw to exit the function or whether you return to exit the function. So it really is just a different type of returning.

Chris Dzombak
Right. And that's kind of a key distinction.

Soroush Khanlou
Yeah. So a blog post that I really like is Matt Gallagher's post Values and Errors. Part one results in Swift. You might know Matt Gallagher better as the Cocoa with Love guy, and we'll put the article in the Show Notes, but he puts the problem with Swift's error handling really succinctly. He says if you want to handle errors across asynchronous boundaries or store value error results for later processing, then Swift error handling won't help. The best alternative is a common pattern called a result type. It stores a value error subtype either one or the other and can be used between any two arbitrary execution contexts. So another way to think about this is like it's like an optional but instead of the nil case you describe why it's Nil.

Chris Dzombak
Right. That makes a lot of sense. So this is another approach to allow something to return either a value or an error, right. Just rather than using the sort of sugar that's built into Swift to do that, we introduce this new type called result, which, as you note, contains as an associated value either the resulting value or the error that comes out of this function.

Soroush Khanlou
Right, exactly. And the most common result framework to use is the Roberts's antipical result. We talk about that library on the show probably, I think, more than anything else. But Results has its places where it's really powerful and Swift error handling, while it can be frustrating in specific contexts like asynchronous handling, it has its strengths as well. And we're also, I think, going to talk a little bit about Promise error handling and fatal error as we get a little deeper into the show. Cool. So there is another blog post that shows swift error handling being used to great effect. We'll put it in the show as well. It's called swift. Two error handling in practice. And it came out pretty much right after Swift Two was announced, like back in WWDC 2015.

Chris Dzombak
And Swift Two, just for historical reference, is when this throwing error handling model was introduced to Swift, right?

Soroush Khanlou
Exactly. Yeah. And the author has a system where they have like a robot arm and they need to call like, move up or move over, move down. And they have all these calls that happen in succession. And the old code was written with objective C, sort of like error pointers. And so there would be a lot of boilerplate around. Okay, well, here's the error. If you have an error, you got to check that and then you got to return nil and bail early. And so there ends up being a lot of boilerplate. And when the author switched it over to use the Swift error handling because it sort of reroutes the code path automatically for you when you try something and it fails, it cut his boilerplate down a lot. And I had a tough time trying to figure out why is Swift's error handling so good and so obviously good in this case and why am I having such a tough time using it. Well, and I think the difference between it is that there's a little bit of overhead involved with using try and handling the error correctly. So you have to have the do statement, you have to actually call a function with the try keyword, you have to have the catch statement, you have to bind the error to something, and then you have to handle the error. So something that ended up that was originally one line of code that may be returned optional ends up being five lines of code. And that overhead really starts to pay off when you have multiple function calls that all throw. And so in this person's, case, like, since move up and move over and move down were all different calls, setting up that framework of like, okay, handle the error in this way ends up being you get much more bang for your buck, basically. And so I think that if you're returning one particular value, it may make more sense to use Result just because it's one line of code and then you can chain off of it and do what you need to do and handle that error way down the road. Whereas if you're calling multiple things all at once, it may make more sense to use the Swift error handling model.

Chris Dzombak
Okay. I mean, that in and of itself kind of ties your choice what am I trying to say? That ties the signature for whatever you're writing, the type of whatever you're writing to its implementation.

Soroush Khanlou
Yeah. How it's going to be used.

Chris Dzombak
Right. Which seems a little unfortunate. I wonder if there's some other better case to be made one way or another.

Soroush Khanlou
Yeah. Ultimately, whatever error handling you decide is going to have to be reflected in its type signature. And so implementers or people that want to call that function are going to have to handle that in the way that you specify, not in a way that they want.

Chris Dzombak
Right.

Soroush Khanlou
Although there are helper functions that can help you get from one to the other, like Result to Swift's Error handling and back with libraries like Result.

Chris Dzombak
True.

Soroush Khanlou
I found that swift's error handling since it's best when you have a bunch of different calls that can all throw is best for stuff like JSON Parsing, where instead of saying, okay, guard that this key exists and that it's this type guard that this key exists, and it's this type. And then set all that stuff you can do all that stuff in one line of code with try and it ends up being much, much shorter. And you have one initializer that throws, and then you can use a protocol extension to add another initializer that just returns an optional if that's what you want, and you end up with a system that ends up with much more succinct code than you would have before. So there are definitely certain cases where try and do and catch are just way more succinct and way more powerful than something like a Result type.

Chris Dzombak
Okay, that makes a lot of sense. So do we want to go over, then, some cases where you do want to use a Result type?

Soroush Khanlou
Yeah. So I'm interested to know how you guys because you have basically a brand new app that was written in Swift from the ground up, how do you approach error handling? How do you handle that stuff?

Chris Dzombak
Yeah, let's see. In a lot of our model layer, where there's JSON parsing and that kind of thing, we are using, as you note, we're using Swift's error handling model for throwing and catching errors. There are also some cases where we're just returning nil, right? We make things return an optional. And I think that that's mostly useful in places where there's not a whole lot that you can do or report back with the extra information that an error object would come with. I'm trying to think of a good example. I can't think of one offhand, but there are a lot of cases where it's not really useful to have the extra information that comes along with an error. You just want to try and see if something works and get back an optional. If it doesn't, I guess that you can still do that by calling something with try question mark. But then if it's just used in one place, you end up creating an error and throwing it and then just throwing it away by converting it to.

Soroush Khanlou
An optional anyway and having the extra like try question mark. I mean, it's only five characters but with the space but I don't know, it just like already a long line. It feels like it makes it much worse.

Chris Dzombak
Yeah, I'm thinking that maybe, I don't know, maybe we should try to move a little bit more toward that. We are all still fairly new Swift programmers, right? And so I'm curious to see what other people are doing or what patterns sort of emerge. I haven't looked at very many other large open source Swift code bases and so I'd be very curious to hear what and to see what other people are doing. Because this is one area where, like I mentioned in an earlier episode, I think I don't have very strong feelings one way or another and I'm curious to see what's out there.

Soroush Khanlou
Yeah, there's definitely a lot of different things that pop up. I have never really understood why they didn't just give us the actual result type and just add the tries and throws and whatever to be just syntax sugar around that.

Chris Dzombak
I do have a post bookmarked from the Swift Evolution mailing list which we'll add to the show notes discussing why they didn't add a result type internally.

Soroush Khanlou
Right. One interesting context in which another interesting context in which the Swift error handling is really, really nice is inside of stuff like promises and reactive stuff. So if your promise or reactive type is error parameterized, as in you know exactly what kind of error it's going to be, you can't use this trick, but if you have, it just be of type error. That just generic error. Then you can call your little callback functions like they're then with promises or map and flat map and all that stuff on different reactive signals. You can make those functions throwable and if you throw from there then the promise or the reactive signal will actually handle that internally and just route it to the right place. And so if you're in an environment like a promise then block where you can just freely throw and it will just be handled for you. It makes handling something a lot easier. Like for example, if something's an optional you might normally do like guard let thing equal optional thing else return nil or whatever. But if you're in a context where you can throw, you can add let's say a function to optional called unwrap that if the thing is nil, it'll throw and if it's not nil, it'll return the actual thing. And with that then you can just do like let thing equal thing unwrap and it will unwrap for you, it'll handle the throwing for you. And then you can just go about your business as though you're on the sort of happy path and you don't have to think anymore about like, oh, what am I going to do if this thing is nil? It'll just go to be an error and you can use the line in the file like keywords to make it tell you exactly where that error was thrown with the default parameters. You can do all kinds of cool tricks like that. And so if you're in a context where you can freely throw swift's error handling and throwing is actually super nice. It's just that most contexts don't really let you throw. Okay, now you all made your own observable type for this new project. How is the error handling handled in there? Is it type parameterized or is it just it could be any error.

Chris Dzombak
I don't even remember that offhand because it's been a while since I looked at that and we're really only using that still to bind views to our view models. And so we haven't really had a need to add really any extensive error handling capability to that. Interesting, the plan was always to move to Reactive Cocoa or RX Swift or Reactive Swift, which is now the reactive.

Soroush Khanlou
Part of Reactive Cocoa but written in Swift.

Chris Dzombak
But written in swift, right? The plan was always to move to a more capable reactive library. Once we got everyone on the team kind of comfortable with the core concept of observables, we haven't actually switched that implementation out yet. Not because I think that the team isn't ready for it. The team totally could handle it at this point. Everyone's used to these concepts, right? But we just haven't gotten around to it. This works and I don't know, we're happily using this to bind view models and nice, that's where we are.

Soroush Khanlou
Yeah, that's an interesting idea of just a signal that doesn't even need error handling because it always has a valid value, right? Yeah, got you.

Chris Dzombak
So you mentioned a couple of things that are interesting here. First of all, you mentioned the concept of errors that are parameterized to a specific type, which as you note, you can do with the result type, but you can't do with swift's error handling. So in something like Java, you can declare you I think should declare or it's idiomatic to declare what exceptions may be thrown from a function, right? And Swift doesn't let you do that. And the sort of theory behind that is as articulated by the Swift team is that in Java or C sharp or languages with checked exceptions like that, people very rarely handle different kinds of exceptions differently. And a lot of people just will end up writing type signatures that say throws exception, the like root class of all exceptions anyway, right? And so adding sort of type checked exceptions adds a lot of complexity for very little extra safety in the real world, the way that programmers seem to write code. I was very against this design decision back when they introduced this in Swift two. I still have somewhat mixed feelings about it because I think there are some cases where it is nice to know what may be thrown so that you know that you can handle it, right? I would be interested in some sort of approach that at least lets you declare in the type system what errors can be thrown so that that's sort of the documentation so that you know what you can catch or you can just catch all the errors anyway.

Soroush Khanlou
Well, and it means that you can be exhaustive in your switch statement and you don't have to have a final catch that just catches any old error. Like if you expect these three types and you have to handle those three types especially, you will always have to add a special catch all at the end. And like if you had parameterized errors, you wouldn't need that. The other nice thing with parameterized errors is you can do like a no error enum with no cases that can't be initialized so you know that you never have to handle that.

Chris Dzombak
So one other thing that's important to note is that the Swift team decided against sort of type checked error, throws type checked errors. Because if you have an API that throws and that calls other APIs that throw, then suddenly your API has to declare that it throws not just whatever errors you might throw, but whatever errors that the API that you call might throw. And that means that future for relatively small API updates have the potential to change the type signature that you have to declare. And that is a valid concern. The count argument, I think, is that if the API that you're calling introduces a new type of error that it can throw, well, then, yeah, that is.

Soroush Khanlou
An API change and you probably want to know about that, right? If it changed the type that it returned, you would definitely want to know about that, right?

Chris Dzombak
That's why I'm so split on this. On the other hand, there's a lot of evidence that in fact programmers don't care and just treat all errors as equal, right? There was an error, this didn't work.

Soroush Khanlou
And print and return or whatever, right?

Chris Dzombak
Recover or just fail yeah.

Soroush Khanlou
There is a blog post that covers a paper and it's about Java exception handling and we'll put it in the show notes. But the punchline is most programmers ignore Java's carefully thought out exception hierarchy and simply catch exception 78% or throwable 84% rather than any of their subclasses. So a vast majority, like five and six people basically are just ignoring the fact that they could be throwing and catching the very specific errors and just throw and catch super generic ones instead.

Chris Dzombak
Right?

Soroush Khanlou
Yeah. It feels like it's very frustrating to use it. And I've used promise libraries where you do have to declare the error type and you can't bridge between domains very easily. I had a situation where I was trying to do a promise that would present, like a View controller because it has a completion block and then do a network request immediately after. But because the error type of the View controller presentation was no error, because it can't fail, I had to map the error to a different domain so that then I could chain off of it and then I would have to map it again to a different domain to do a third thing. The chaining only works if you stay in the same sort of domain, like network errors, art network errors, or whatever.

Chris Dzombak
Yeah. One other note that I would like to see from the Swift language on the sort of type checked errors topic. It would be nice if you could hint that a certain error is possible to be thrown without that needing to be an exhaustive list of errors that can be thrown, like in Java or C sharp.

Soroush Khanlou
Right, right.

Chris Dzombak
So if you are in the case where you're calling something that can throw, but you know that you're going to throw whatever the thing you're calling throws, plus a disk full error, it would be nice to be able to hint in the type of this function, hey, this throws. And one of the possible things is a diskful error that at least gives you some indication when you're calling it, like what errors you might be particularly important or interesting to check for without forcing you to make a whole comprehensive list.

Soroush Khanlou
Yeah. You end up having to rely on either extensive testing or on documentation to know what errors are going to be thrown. And a lot of cases you're not going to test, what if the disk is full? You're not going to test that.

Chris Dzombak
Right.

Soroush Khanlou
And you'll never know that it throws that specific kind of error and how are you going to handle it, what's the right thing to do? And documentation falls out of sync all the time or they just forget to put it in there and if it's not open source and you can't check it yourself, I mean right. What are you supposed to do?

Chris Dzombak
Yeah, exactly.

Soroush Khanlou
It's such a tough question. Yeah.

Chris Dzombak
I have no idea if that's been proposed or if that's likely to happen, I would love to have some indication that doesn't revolve around someone remembering to update a comment about what things like what errors may be interesting or useful to check for.

Soroush Khanlou
Yeah, I mean, that's the whole reason we have a type system, is so we don't have to rely on comments for like, oh, it takes these parameters and these are optional and these have default values or whatever.

Chris Dzombak
Right. So changing topics slightly. The result type is also really useful if you're doing Asynchronous programming. We're all very familiar with passing one or two blocks to some Asynchronous API and then maybe one gets called if there's an error and the other gets called if it's a success. Or maybe you pass one block and it gives you two pointers and you see which one is non null and then assume whether something was successful based on that. What a result type means is that you can have an Asynchronous API and you give it a callback block and that block takes a result as a parameter. So suddenly you have one callback block. Like you don't have the weird case where if you have code that you have to run for both success and failure, it's not duplicated between two callback blocks.

Soroush Khanlou
Right.

Chris Dzombak
And a result type provides a really nice way to wrap up a result for Asynchronous APIs. So that's one thing to note.

Soroush Khanlou
Yeah. One trick that I do want to mention, but I think it's kind of an anti pattern, is that one way that people get around the fact that Swift's error handling system can't be used asynchronously is that in asynchronous completion block, they will pass back a function that throws. And it's your job to try calling the function and then handling the results. Have you seen this before? No, I have never seen a canonical blog post. But yeah, you can imagine like it passes you a function.

Chris Dzombak
Sounds sketchy.

Soroush Khanlou
I mean, it works.

Chris Dzombak
I guess.

Soroush Khanlou
I'll try to find a blog post. I don't know if there's like a canonical blog post. It is a little bit sketchy.

Chris Dzombak
Yeah, I've never thought about this that'll work, but I had never thought about doing that.

Soroush Khanlou
Yeah, here it is. Olivier Allegon has a blog post about it. So we'll put that nice in the show notes. Yeah, like I said, it works, but it's kind of kind of whack. Which I think is why it's not really used in practice. It's much easier to just make your own result type. But the problem that he brings up, even if you don't bring in a library for it, having like enum result case success and the type and then case error and the type, that's four lines. You could just put that in your wrap right now and you would have it. So it's not too expensive. But the problem that it does solve both result and this thing, this hack where you pass back a function that you can call that will throw the problem they solve is very real, which is that a lot of the APIs that, let's say you want to talk to an S URL session and you get a completion block from that you have to handle, like, basically it returns to you three things data response and error. And they're all optional. And the documentation tells you that if error is not nil, like if there's a value for error, then data and response will be nil and vice versa. The other way around where if data and response are both not nil, then error will be nil, which is like you can encode that in the type system with something that is like call it a subtype or call it an enum or whatever, where it's either this way or it's that way. And it's way nicer when you don't have to check, okay, you have to unwrap this and this in these cases, but then in this other case you have to unwrap this thing. And so I can just wrap that up in a result or something. And that way, you know, if this succeeds, I will have both a data and a response. And if it doesn't succeed, I will have an error and that's all I'll have. Yeah, so I wrap the Nsurl session APIs for promise stuff. And that's what I do, is I unwrap data and response and if they're both not null, then I call like fulfill and then I unwrap error. And if that one has a value, then I call reject with that value. And then if any of those two cases are not true, then I fatal Error. And I think the fatal error message is like something horrible has happened because it should never happen, but it might happen. Like, I trust Apple's code to not fail me like that, but you never know. And so that brings up the question of when do you fatal error?

Chris Dzombak
I was just going to make that same segue so relevant given that I'm surprised it took us this long on the podcast called Fatal Error to talk about this.

Soroush Khanlou
Yeah, exactly.

Chris Dzombak
So I guess I'll go first. So there are a number of fatal error calls scattered throughout our code base. They're mostly in places where this is something that something very unexpected that really should not happen has happened and we don't really know where to go from here. Right, right. So as one example, we build a path in our application support directory to put a database. And that's something where the path APIs, like appending paths to a URL can fail. I forget whether they return optionals or.

Soroush Khanlou
Throw they return optionals.

Chris Dzombak
Okay, so that is something that can fail. This is something that technically does return an optional. But given that we have a local path and we're appending a path component to it that really should never return nil, I can't imagine why that would return Nil.

Soroush Khanlou
The reason that that API returns Nil is for mail to URLs, because you can't mail to URL. So you're pretty confident that that thing is not going to fail.

Chris Dzombak
Exactly. If I'm appending it to like, a path to a file system URL. Right. So in that case, we say guardlet the cache. URL is like this application support URL, append this database name else fatal error with like, couldn't build path in the application support directory. Right. So cases like that are where I say it's okay to use a Fatal Error call, which is just like, look, I don't know what's going on or how to recover from this, but something's very wrong.

Soroush Khanlou
Right. And that's when you choose to Fatal Error out.

Chris Dzombak
Right.

Soroush Khanlou
Now, I have a question for you, which is you can do guardlet thing equal optional thing, else fatal error, or you can just do optional thing bang.

Chris Dzombak
Yeah, I mean, I get that those are functionally pretty much exactly the same. I have this just sort of maybe irrational hatred of exclamation points of bangs in Swift code. And we'll also note that at least with Fatal Error, we can attach a nice message that's like, hey, we couldn't build a path in the application support directory. Something's really not right. And maybe include other helpful if there's other helpful information, like maybe the path that we were trying to append to, which doesn't happen if your app quit because of a bang there. But you're right, functionally. And given that we're very unlikely ever to hit this code path, you could just as well add a bang there, right?

Soroush Khanlou
I don't do the bang either. And the reason is because I really want to feel the pain of, like, I'm writing out the words Fatal Error. Like, the app is going to crash if I'm wrong about this. It's a little bit longer and you're really feeling the pain of like it doesn't like, sometimes I feel like a bang can kind of hide away in the code and you might not see it, but a Fatal Error is just very explicit. It's like, this is going to crash if you're wrong about this.

Chris Dzombak
Right. It's also nothing is ever going to suggest that you add a Fatal Error call. Unlike sometimes it'll suggest that you can use an exclamation point to unwrap an optional it's clearly an intentional decision. Right?

Soroush Khanlou
Right, exactly. Now, one other cool thing that we should note is that Fatal Error is a function that returns a never, which is another degenerate type of like an enum with no cases. And so it can never be instantiated and you can never have it. That's why it's called never. And you can make your own functions that return never and that call fatal Error internally. So if you want to add, like, friend of the show Caleb Davenport has a function called not implemented. And it's for like, if you have in it. With coder or whatever, and internally it prints a nice message and then fatal errors in a nice way to say, hey, this thing is not implemented. So you can add your own to have a little more semantic meaning.

Chris Dzombak
Cool. Yeah. I'd forgotten that that type existed, but I just found the documentation on Apple's site and added that to the show notes.

Soroush Khanlou
Perfect. Nice.

Chris Dzombak
So, before we wrap up, there is one more thing that I wanted to mention really briefly about the result type, which is cool. I really like the result type. You can't tell there's a style of error handling and functional programming which I forget exactly what it's called, but for sort of colloquially like railroad style error handling.

Soroush Khanlou
Sorry. It's called railway oriented programming. There's a couple of talks about it.

Chris Dzombak
And there we go.

Soroush Khanlou
Google that. You will find all the relevant information. We'll put some of it in the show notes.

Chris Dzombak
Yeah. And we're running a little long, so I don't really want to get into this, but this would be something to look into. If you're writing, like, applying a series of functions that transform data and an error might occur at some step, this is a useful pattern for you to look for and do some more reading about. Yeah.

Soroush Khanlou
And you can use this with result types, you can use this with promise types, you can use this with reactive signal types. And it just kind of just pretty much not always, but almost always just does the right thing.

Chris Dzombak
Yeah. It's a fairly elegant way to handle certain, again, sort of like applying a sequence of things to data operations.

Soroush Khanlou
Exactly. Yeah. In as much as you can. I would try using the highest level abstraction that you can. Like if you're just doing local things that don't necessarily need an error but are a chain. You might want to use optional flatmap if you're using something a little bit more complicated that is still asynchronous but needs more detail on the errors, you might use result flatmap. If you know it's asynchronous but it only calls once. You might want to use Promise flatmap or Promise then. And using the highest form of abstraction that you have, it lets you write the best, most succinct code that you can.

Chris Dzombak
Abstractions are good, use them. Otherwise, if you have something where an abstraction would fit, but you're not using it, you're probably, like, rewriting that abstraction in your own code anyway.

Soroush Khanlou
Yeah. Maybe writing a worse version of it.

Chris Dzombak
Yeah, maybe.

Soroush Khanlou
That'S an episode about error handling.

Chris Dzombak
Yeah. This is probably a good point to wrap up. I think we're a little over 30 minutes at this point.

Soroush Khanlou
Yeah. Cool. Well, as always, Chris, it was a pleasure.

Chris Dzombak
Yeah. Always fun to talk to you. And thank you very much to our listeners. And we'll talk to you next week.

Soroush Khanlou
All right, later.

