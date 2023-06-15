Chris Dzombak
This is episode four, right?

Soroush Khanlou
This is episode four.

Chris Dzombak
Alright. Welcome listeners, to Fatal Error, episode four. I'm Krista Zomback.

Soroush Khanlou
And I'm Sirous Kamu.

Chris Dzombak
And today Sirush has promised to give me an overview of promises and and futures. So Sirush, what what's a promise?

Soroush Khanlou
First of all, a plus putty.

Chris Dzombak
Thank you. So I'll a plus. Same to you.

Soroush Khanlou
So Promise is a way to encapsulate some Asynchronous code and give the system information about how it completes and when it completes and what status it is when it completes. And if there's a system, if there's sort of an abstraction around this idea of completion, then you can do really, really interesting things. Because the thing knows what the shape of a completed object looks like, a completed Asynchronous task, what it looks like. You can do things really easily, like chaining. So when this is done, take the result of it and put it in here and run this next promise and then run this next one. And you can make a chain in that way. It'll also let you do many parallel tasks at once. And because it knows what they all look like when they complete, as soon as they're all complete, it can give you a single callback. All these different little abilities like being able to recover from failure. You say if this promise fails, recover by doing this thing and starting off this other promise. So for example, you might say like, oh, fetch from the network and if that fails, then fetch from the disk. That may not be the best example. I'm still trying to figure out what the best example for Promise recovery is.

Chris Dzombak
So to recap a promise is a nicer pattern for some common Asynchronous programming tasks. And it makes more generic the idea of doing some Asynchronous work and getting a result back, right?

Soroush Khanlou
Yeah, exactly.

Chris Dzombak
It's a little bit of a more formal interface than say, doing your own Asynchronous work with GCD directly, right?

Soroush Khanlou
Exactly. Or even you may not be interacting with GCD, but you're interacting with Nsurl session and you have a completion block and a failure block. This sort of formalizes that. So you can imagine that the canonical example of when a promises a slam dunk is if you have to perform three network requests in a row, right? So you perform one in this completion block of the second one, you perform the completion block of the first one, you perform the second one completion block of the second one, you perform the third one and this slowly turns into arrow code.

Chris Dzombak
Right. Or you have a very complicated NS operation queue based system just for making three network requests.

Soroush Khanlou
Exactly. And I would say that I think NS operations are a lot like promises, but they're a little more high ceremony to set up because you either have to make a subclass or make a special type of the block. And they also have a lot of details that most of the time you don't care about what queue the code runs on and stuff like that. And promises are just like a much nicer, easier way to work with that. You never have to subclass a promise, you just sort of have to define it. They're really nice to work with. I started working with them when I was writing the API for Backchannel. So the API is written in node, which while writing in JavaScript is not my favorite language, has tons and tons of support. And I was quickly finding that everything in node is Async. So if you have decrypt and you want to generate a new salt to hash a password, generating the salt is Async, and then hashing the password itself is also Async. And that doesn't even go into saving to the database Async. And so I quickly had all these callbacks and I quickly fell into this trap of, okay, well, every time there's a callback, you have to do if error check if there's an error, and if there's an error, you want to do some kind of special rejection and then kick off the next thing. And I had nested code that was like six and seven layers deep. At the very end of the line, you send a welcome email, which is another Asynchronous request, and you can finally say like, result, send JSON, which finalizes the request. And it became unwieldy within the first week or two of writing this code.

Chris Dzombak
Yeah, I mean, that's a huge problem in that sort of traditional Async callback closure based style of programming.

Soroush Khanlou
Yeah, for sure. I was like, I have heard these promises. I've heard they're really good and I know they can solve this problem, but they're like another thing to learn. I'm already learning all this node stuff and this new database and all these other things and I put it off in a method. I was like, I got to go into this because it's coded too messy. And I spent a day or two learning how they work and it makes the code dramatically better. So now, instead of there being a nested tree of callbacks, or a nested error code or a nested set of code, it's now flat. So as soon as one finishes, you tell it what the next one to start is and it works from there. And the JavaScript implementation is very weird. It's very tied to the way that JavaScript works. So basically, instead of success blocked, you have something called then. And then is an interesting function because you can return either a new promise, which will start waiting on that promise for the next thing that you add to the chain, and that'll be like the next thing. Or you can return just a value and it will automatically wrap that in a promise for you and immediately fulfill that promise so that you can continue or you can also throw from it, which will be the same as returning a rejected promise. And you can do all these little weird things, but you can kind of only get away with them because there's like a dynamic type system or yeah, dynamic type system, where it'll just check the type of whatever you return. And if it is quote unquote, untenable, which is sort of a generic term for anything that conforms to the Promise spec, then it will treat it as a promise. If it is not, then it'll wrap it in a Promise and it'll catch the errors and do all the other stuff. So JavaScript kind of has its own unique implementation of Promises that are really, really good for JavaScript. It's sort of built for the language.

Chris Dzombak
Okay, that makes sense. So if we move into something like Swift, then how does a Swift Promise implementation look different from this JavaScript implementation?

Soroush Khanlou
Yeah, so I wrote a Swift Promise implementation over the last few weeks and I published a couple of blog posts about it there in the show notes, there's a couple of differences. One big one that is always really satisfying is it's much easier to model in Swift because a Promise is basically a state machine. It's either pending, which means it's not done yet, or it's fulfilled, which means it's completed with some value, or it is rejected. So it had some error and it's no longer going to continue.

Chris Dzombak
And that sounds a lot like an enumeration with associated values.

Soroush Khanlou
Exactly. So you can just have an enumeration with three cases, one for pending, one for fulfilled, that has an associated value of the value that you've filled with, and one for rejected with the associated value of the error. And it means that you can never express the idea of having an error and being in the pending state at all. Not only can you not express it, the type system, the compiler won't allow you to compile them, but what would that code even look like? You just literally can't write that code and that is cool.

Chris Dzombak
Yay, type systems.

Soroush Khanlou
Type systems are cool. And so you can actually make this state enumeration generic over the type of the value and you can make it generic over the type of the error. And then with that you can also make the poll promise itself generic over the type of the value and optionally the type of the error.

Chris Dzombak
Okay, and so now I really see what you mean about the shape of the Promise type dictating what states it can be in and how you interact with it.

Soroush Khanlou
Yeah, exactly. So yeah, so there's this thing called Promises a plus, which is the JavaScript spec, and it only defines that you have to have a function called then and then has to be able to act in these specific ways. And as long as you do that, as long as you pass these tests, you are considered a venable and you are considered a fully fledged promise. And the reason that that's really cool is that once you have the Then function you can build all these other behaviors that I was talking about right off of that. So you get the chaining for free promise all, which is like, hey, finish these ten promises and let me know when they're all done. That becomes trivial to write, being able to retry, being able to recover, being able to zip two promises together and make like a third promise with the types of tax which is actually a really fun one because you can zip two promises and then get a tuple at the other side and the tuple still has types. So then Swift, you can actually maintain the types of the tuple even if you're trying to combine promises of different types like promise all, you have to have them all be the same type because otherwise how would it know what types are going to come out? And you could force it to work with any object or any but they all do have to be the same type. But with zipping you can do different types in the same promise combiner which is cool. So you can build all these awesome features on top of the Then function and so you can actually separate out the promise sugar and the goodies that come with it and the actual implementation of the Then function which is cool.

Chris Dzombak
And those features would just again, going back to our sort of definition of what promises are and what they do for us, these features make easier a lot of common patterns that we see in highly asynchronous programming.

Soroush Khanlou
Yeah, exactly.

Chris Dzombak
Okay, cool.

Soroush Khanlou
Yeah. So since they can be fulfilled once and they represent any asynchronous action, it becomes easier to say, well, my cache beforehand, it was synchronous because I didn't want to deal with the fact that it had a completion block and making that work with other code and nesting everything was kind of a pain in the butt. But now because I have promises, I'm more likely to say, well, I might as well just have this return of promise that I can chain off of and do other network requests off of rather than having to just return sensitively and potentially even block like even cause a single frame to stutter.

Chris Dzombak
Yeah, cool. That makes a lot of sense. So how do the how does the idea of promises relate to the I think fairly similar idea of futures.

Soroush Khanlou
So yeah, so my one line difference between what a future and what a promise is is basically a future is read only and a promise is read write. So essentially you have a promise. The promise sort of has a future attached to it and you can pass the future around knowing that the future cannot modify its own state and that it has to have its state modified through the promise. And then the promise is the thing that actually has a method on that's called, like, fulfill with this value or reject with this error. And so having that difference of this one is read only and this one is read. Write helps you maintain that separation through your app.

Chris Dzombak
Okay, so that's a way for you to expose a future value to clients without the possibility of clients breaking your API somehow by writing something into a promise that you weren't expecting.

Soroush Khanlou
Exactly.

Chris Dzombak
Okay, that makes sense.

Soroush Khanlou
And actually it's really cool. I think this distinction is not that useful, I guess, mostly because I work on really small code bases with small teams, but I feel like you would know if you were fulfilling a promise when you weren't supposed to. But if you want that guarantee, it is there. And one thing that I really liked is one of the libraries that implements this distinction between futures and Promises. The way that they do it is really cool. The Promise, like read methods and write methods are all exposed publicly, and the future has methods to read and write, but only the reading methods are exposed publicly. The write methods are internal. So the Promise can talk to the future internally and fulfill it, but nobody from outside of the module of the Bright Futures code can do that.

Chris Dzombak
Oh, cool. And so this is the Bright Futures library.

Soroush Khanlou
This is the Bright Futures library, which.

Chris Dzombak
Does show up in our show notes as well.

Soroush Khanlou
Yeah, so we'll definitely put that in the show notes. There are a few different options for if you want to use like, a promises library within your own app. So I've heard good things. I haven't used any of these. I've kind of played around with some of them. But there's Bright Futures, which is a really popular one. There's promise. Kit, which has been around since the Objective C days. And so Maxwell actually maintains a compatibility layer, layer called Any Promise so that you can touch it from Objective C without having to worry about the generics and all the other swifty features. There's also Future Kit, which is newer on the scene but also pretty good. And there's one I believe is called swift task. Or swifty task.

Chris Dzombak
Okay, I had only heard of Promise Kit, I think, before you started writing and talking about this.

Soroush Khanlou
Yeah, it's called swift task. They're all pretty good. They all have their slight differences. I'm sure if I knew more about the reactive stuff, it would be more like RX Swift versus Reactive Kit versus Reactive Coco. They're all like slightly different in the way they choose to do their implementations and the features they choose to add, but they're all basically pretty good. And I would say that they're all leaps and bounds. Better than managing your own success and failure blocks.

Chris Dzombak
Yeah, absolutely.

Soroush Khanlou
Yeah, for sure. So, yeah, so we have this idea of Promises. They're super useful. And so you would think if you were building a language for the future, you would want to include some ability to use these promises and maybe also some way to easily access, maybe some language, syntax and structure to make it a little bit easier to use these promises.

Chris Dzombak
And yet the current state of Swift is such that we now have an improved GCD API, which we can include in the show notes. Just for reference. But where do we stand on any future, any promise of any future?

Soroush Khanlou
The puns are ripe.

Chris Dzombak
I'm sorry I had to future Async programming improvements, so we don't have a.

Soroush Khanlou
Whole lot to go on. But in the Chris Lattner sort of retrospective of Swift Three, and looking forward to Swift Four post, he talks about they want to add, like, a native concurrency model to Swift. So he mentions a couple of things in there. Some of them make more sense, some of them are like, what exactly is this? He writes first class concurrency actors, Async Await, atomicity memory model and related topics. So in these, like, ten words, there's a lot to unpack. I don't know what they would want to do for actors. And I mean, I think atomicity makes sense. That's just sort of like making sure that you can write to something and it has its own lock around it or whatever. Memory model. If they want to change the memory model. I've heard whisperings they want to move to Rust, like lifetimes thing. I don't know about any of that stuff.

Chris Dzombak
I think that the Rust Lifetime memory model was proposed not as a replacement for the current sort of Arc model, but as an alternative that you could use if you were in a systems programming environment where you wanted more predictable gotcha behavior.

Soroush Khanlou
Interesting. Yeah, we'll have to throw a link into the show notes for that stuff, but yeah, absolutely. I don't think have you written any Rust yet?

Chris Dzombak
No, I've read about it and it seems interesting, but I still haven't found a good excuse to write anything significant.

Soroush Khanlou
Yeah, I'm basically in the same boat. But I think the most interesting one of these concurrency patterns that Chris Latner sort of hints at is this Async Await. And Async Await exists in, I would say, one and a half languages that.

Chris Dzombak
I know about one and a half.

Soroush Khanlou
One and a half. So the first one is C sharp, where I this is the first I've ever heard of it. I don't know if it was invented there or first came to mainstream popularity there, but it's also in the Es Seven, the JavaScript spec after Es Six. And so this is coming in JavaScript at some point, and there's like, transpilers that you can use. So you can use this feature now rather than having to wait for Es Seven. So kind of you can use it in JavaScript, but you have to jump through some hoops so that's the half.

Chris Dzombak
Okay.

Soroush Khanlou
Yeah. So Async Await basically the way that it works is in C Sharp they are known as tasks instead of promises. And so basically you have a function that returns a task and that task is generic over some type. You declare the method that returns that task as Async. In the same way that you would sort of decorate a method with throws, you can also decorate it with Async. And so you would say, like, async, get some integer. And the name of the function, like, get some integer async. And then you'd have a little arrow, and then the arrow would return a task of type int.

Chris Dzombak
And the task type that you're describing here, is this somewhat similar to a future which we discussed a little bit ago?

Soroush Khanlou
It seems basically more like a promise.

Chris Dzombak
Okay. Yeah, okay, I don't mean for this.

Soroush Khanlou
To well, yeah, I'm not sure if you can read to it or write to it. I don't know enough about the C Sharp stuff to say. But basically you define it with a block and that block runs on some background thread and at the end of the block you return some value and that value is your new result of your thing.

Chris Dzombak
That's really all I wanted to know is whether this is similar to what we've been discussing or whether it's something totally different.

Soroush Khanlou
Yeah, as far as I can tell it's very similar to the stuff we've been talking about but it doesn't have any concept of an error built in as far as I can tell. Maybe we have some C Sharp writers who are listening to this podcast who can tell us otherwise, but as far as I can tell, there's no error modeling inside of it. So then you have this function that returns a task and this function is labeled with the word Async. And then whenever you want to use this thing, instead of saying like call the method to get this promise future, deferred, whatever you want to call it task and then calling some function on it to add a completion block to it, you instead call it with the keyword await before it. And so what that will do is it will say to the compiler or will tell the system basically like, look, I'm actually done executing for now until this thing returns. So give me control over the thread when this thing is returned and put its value into this variable that I declare. So this line looks like int result equals await get integer, Async.

Chris Dzombak
Okay, so this is sort of a language not necessarily wrapper but first class language support, not just for this idea of Asynchronous work returning a result, but also does it always block the calling thread until that value is ready? Are there other ways to use Async.

Soroush Khanlou
Await so it doesn't block the calling thread, it just sort of yields control of execution until that thing is done. But the procedural list of execution does stop within that method. But the system can do other stuff like accept touches and handle other stuff while you wait for this task to finish.

Chris Dzombak
Okay, yeah. Interesting.

Soroush Khanlou
And I think if you don't finish that task, if that testing never returns, that would be a deadlock, basically. I don't know if you would call it a deadlock, but your code, that code would just not continue to write. So then you can imagine anything that you declare, any function that has the word await in it that also returns a type must also be async. Does that make sense?

Chris Dzombak
Yeah, I think so.

Soroush Khanlou
Let's say you call like you want to do something with let's say you have a network request. That network request is an awaitable. Or it's like an async method. You call that you await the result and then you want to parse the JSON and then you want to return like some parsed object. The method that returns that parse object also has to be Async. And so in this way, I think it's sort of like Swift's error model where you decorate your functions with these keywords and the compiler can sort of assure that anytime you have an Await that the function is going to be async. Anytime you have Async, you have to call a weight before you can use the result of that. It kind of parallels the memory model to some sense. And then you can also kind of imagine how you could combine the error model and the Async await model to make asynchronous errorable things. So you would write basically try await this thing and then if it fails, it will jump in the catch block and if it succeeds, it will continue execution in the way that it normally would.

Chris Dzombak
Yeah, I could see that happening.

Soroush Khanlou
Yeah, it's definitely an interesting solution to the problem and it's like should it be await, try do this thing, or should we try a wait, do this thing? How does it work? How do all the nuances and stuff work? But it seems like it could work. It seems like it could be pretty good.

Chris Dzombak
Cool.

Soroush Khanlou
Yeah. So that's sort of the future of this stuff.

Chris Dzombak
Future? So many puns in this episode.

Soroush Khanlou
No, it's great. So yeah, so that is the bulk of what a promise is. I think that if you are working with the network in any capacity, you should absolutely be returning promises instead of having success and completion blocks. It's a nice thing because you can have one method that returns that has success and failure blocks and you can have one method that returns a promise. So you can kind of choose which way you want to work with your network thing, especially as a transition from I'm transitioning app from completion blocks to promises. And so you can kind of transition using this, which is kind of nice. So that's pretty cool. But yeah, I think there will be point where you will have to do one network quest after another, and maybe a third and maybe a fourth. And at that point, you're going to wish you had Promises, or you'll have to do you'll have an array of things, and you'll want to call an API method on all those things and be informed when they're all done. And you'll start working with dispatch groups and you're like, you know what? I should have listened to Sirous, and I should have just put Promises in here from the beginning.

Chris Dzombak
Yeah. And I'll expand that to, say, any place that you find yourself writing the sort of repetitive completion block asynchronous API, maybe consider whether bringing one of these promise libraries that we mentioned the show notes into your project, is viable, because it really can clean up those interfaces into something that I think much better communicates the intent of that interface. Right, yeah.

Soroush Khanlou
For sure. You work at a slightly higher level of abstraction, which I really do like.

Chris Dzombak
Right, yeah, exactly.

Soroush Khanlou
Some of the promise libraries also come with sort of additional things which will make things so they come with additional packages that will like extensions on things that already exist in UI kit and foundation that will make them be promise based. So I think when you have UI view anime with duration and then you have a completion block on that, they will actually write an extension on UI kit where that UI view animate with duration will actually return a promise instead of having a completion block. And so if you wanted to include that in your chain, you could just do that. You can just make that happen.

Chris Dzombak
That's really nice.

Soroush Khanlou
Yeah, it's pretty sweet.

Chris Dzombak
Okay, so, Sarish, I know you recently actually wrote a Promises implementation. How did that go? Did that help provide you with some insight on how promises work and maybe get used to thinking to thinking in this way?

Soroush Khanlou
Yeah, so it was really interesting. I wanted to make the API kind of as simple to use as possible, and so that informs my decisions, and then that causes problems later because of the nature of the way the Swift is written and because of the nature of the type system and stuff like that. For one, it was super instructive because you really get to see, like, okay, how does this work and why does this work? And you can see the state of the promise, and you can see like, oh, well, it has a state variable and that holds on to, pending, fulfilled, or rejected. It has these callbacks, which is like an array of callbacks that will call back when it's done. And you can see you can start to see how this thing works.

Chris Dzombak
Right. It doesn't seem offhand like something that would be really difficult to implement, but I haven't implemented it.

Soroush Khanlou
Yeah. So there's interesting things. So one cool part is that when you write the signature for a Then function right. So then I tried to make follow the JavaScript model as much as possible. So it replaces flat, map or bind. It replaces Map and it also acts as tap, which I would just call like sort of tapping into the chain but not changing the state or the value of the chain which the JavaScript one doesn't do. If you don't return anything in JavaScript it'll replace it with a fulfilled value that is undefined. Like the value is undefined but it is a fulfilled promise. So you can keep chaining off of it, but you don't have your value anymore. Okay, so you have flat map which will let you return a new promise and then continue work. So that's called then. And then there's also Map which lets you change the value inside of the thing in a synchronous way. So you can imagine just like if you need to add to number, add a number to the result or like append a string to the result or something really simple, you wouldn't necessarily want to wrap that in a promise. And you could do that in sort of a mapping then block, but because the signatures of all these things are so similar, right, so when you write the signature you can immediately see like, okay, I have this function that returns a new promise. So I will have to call that and then somehow bind the result or failure of this new promise to this other promise that I'm about to return. And it's kind of elegant because it feels like there's almost only one way to write it and it's kind of nice. It's kind of nice when you write and you're like, yeah, this must be this way. And then you write some tests and you realize you actually made a, you had an error with threading and you're appending two things to an array from two different threads and then you go back and fix that and then it looks really, really elegant. But the other part of it is because the then function is overloaded, you sometimes have to add extra type hints to tell the, to tell the compiler, which then function you mean. And so that can be kind of annoying. Another thing that I learned about was like do you want to give the error a type or do you not want to give the error a type? Right?

Chris Dzombak
What do you mean by that?

Soroush Khanlou
So your promise is generic over the type of value, but you would also make your promise generic over the type of error, right? And so you just have to say, well, error is constrained to be an error type. But other than that, I'm saying specifically it's going to be this error type, it's going to be an API error. And so you can declare that as well. But then if you make it generic over that type as well, every time you want to declare a new promise or you want. To return a promise, you have to tell it which error is going to be returned. And if you get lazy, you can just say, oh, it's well, it's going to be an error type, and I'm not going to tell you which one. But if you want to be specific, you could say it's this kind of error and is kind of nice, but at the same time, I thought that would be a little bit too much.

Chris Dzombak
It doesn't seem like that lines up well with the current error handling philosophy in Swift.

Soroush Khanlou
That's right. Yeah. Although that has some pattern matching built in. But I guess you could just kind of build your own pattern matching on failure block, start using this promise library that I wrote in one of my apps, and while it for the most part works really well, especially in simple cases, it works great. There are definitely some cases where the type inference doesn't work as well. And there's also another case that I found where I actually want to return. I actually want to throw from inside of a then block because I have some condition, like, let's say I get some value back and from the network and a dictionary, I have to parse that dictionary and make sure that a certain key in that dictionary is there. If that dictionary key is not there, I really can't continue with my work, and so I have to signal error somehow. So you can return a failing promise, but then if it's a failing promise, you also have to return a succeeding promise. So if you just wanted to do a simple map instead of a flat map, now you have to change everything in the whole block. So the ability to just throw from inside of there would make things a lot easier. So that's like another thing that I'm going to have to have to write.

Chris Dzombak
If you throw from inside of there, though, is that going to get caught and turned into an error result for that promise?

Soroush Khanlou
Yes, exactly. Okay, exactly.

Chris Dzombak
That makes sense. Yeah.

Soroush Khanlou
The other interesting thing that I learned from writing my own implementation is you mentioned result. You could use the result micro framework, the antiypical result GitHub repo, and I think that's Rob Ricks.

Chris Dzombak
I believe so, yeah.

Soroush Khanlou
So you could use that one, but I looked at it a little bit and I didn't end up using it because you end up having to implement some of that stuff yourself anyway, because you have this state and the state can be pending. So you'd have like, state is either pending or fulfilled, and then the fulfilled value is a result that has two other values in it. And I felt like, well, if I'm already implementing the pending versus fulfilled part, I might as well just add one more case because it's not like the result type is very complicated.

Chris Dzombak
Right.

Soroush Khanlou
So I ended up opting not to use a pre built result type and opting to kind of just roll one of my own, partially because it was simple and partially because there was also some synchronization around threads that I had to do that was a little bit easier if I had my own type.

Chris Dzombak
Okay, that makes sense.

Soroush Khanlou
Yeah, there was definitely some learnings in there. I'm glad I did it. I'm not sure if I would use it over Promise Kit or one of these other more established libraries, but I definitely understand on a much deeper level, like how this thing works. And that's a good feeling. Cool.

Chris Dzombak
Yeah, that's awesome. So one thing that I want to call out here, as long as we're talking about, particularly about being able to chain and about being able to chain promises and transform results and that kind of thing, is that that's a really good way to start thinking about sort of data flow throughout your program, right. Rather than necessarily thinking just about control flow, which is sort of the more standard, imperative programming way to think about things, it can be really, really useful to think instead about how data and events flow through your application, what paths they take, how they're transformed, and how that data flow and how those events inform the control flow through your program.

Soroush Khanlou
So it sounds like you're saying that reactive programming is somehow related to promises. Is that what you're getting?

Chris Dzombak
Well, this is what I was getting at. So once you get used to thinking once you get used to thinking in this way thinking about not just if x do Y, if the sort of very standard, imperative paradigm once you get used to thinking about how data and events flowing through your application inform just sort of how the application flows and how it's structured. It can be useful to think not just about a promise that returns one value, but maybe you can take the concept of promises and expand this so that rather than returning one value and then completing, you could return some number of values, any number of values and then complete or error. And you could use that, you could imagine, to model all sorts of interactions with your user interface, to model any sort of ongoing Asynchronous work or just one asynchronous one unit of Asynchronous work, and really structure large parts of your application only in terms of this event and data flow.

Soroush Khanlou
Got you. So like in the same way that a promise would return once, that might work for, let's say, a UI alert view that has either like it has one of the buttons that are tapped and they can only be tapped once and then it has to be over. That is better model to the promise, but something like a button which might be used to build that alert view but might send out that completion more than once, right?

Chris Dzombak
A button might do this, a text view might do this. When someone is typing, you might want to get some sort of callback every time the value changes, and that's something that promises aren't really well suited to modeling, but you could imagine extending a promise library somehow to allow doing this. And as you mentioned, I'm now starting to pitch going what I see as one step further and thinking about reactive programming, which is a topic that we plan to cover in a future episode, because I think we're getting to about 30 minutes here.

Soroush Khanlou
Yeah. All right. Yeah, I think definitely we're going to have to do an episode on reactive stuff. We've got a lot to talk about with that. It's going to be great.

Chris Dzombak
It's going to be great.

Soroush Khanlou
So, yeah, promises are a crippled version of reactive signals.

Chris Dzombak
You heard it here first, and they're still very useful. Yeah.

Soroush Khanlou
So, yeah, we'll talk about reactive in the future, but I think as far as promises, there's not really anything else I want to add.

Chris Dzombak
No, I don't think I have anything to add, either. Cool.

Soroush Khanlou
Great. Well, as always, chris, it was great talking to you.

Chris Dzombak
Yeah, it was great talking to you, too. Have a good afternoon.

