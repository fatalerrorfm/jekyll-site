Chris Dzombak
Um, let's see season four I'm gonna create oh, you already it looks like.

Soroush Khanlou
You already did it here.

Chris Dzombak
56 what do we want to talk about today?

Soroush Khanlou
I don't know. How was your, how was your week? What you, what'd you get up to?

Chris Dzombak
My week was alright. What did I get up to? You know, pretty much Python stuff. I mean yeah. Yeah.

Soroush Khanlou
Nice. What, what kind of stuff are you doing day to day with the Python?

Chris Dzombak
So right now the stuff that we're working on is like, taking this website, which is a web application that was developed originally mainly for research. It's a research tool. People use it to answer researchy kind of questions and adding features around it. Like, I think I might have mentioned last week, like billing and multi user team management and all these kind of features like that. So there's just kind of a whole lot of work to be done around that.

Soroush Khanlou
So it's kind of like a lot of administrative stuff of billing.

Chris Dzombak
Yeah. It's all the stuff that is really necessary, but also not super interesting to work on from an engineering standpoint.

Soroush Khanlou
Right. Especially when you go from a perspective of like, I'm doing research and on the cutting edge of this tool. And then now you're doing all the boring startupy stuff of like, how do we charge people's credit cards?

Chris Dzombak
Yeah, exactly.

Soroush Khanlou
We need user accounts.

Chris Dzombak
Yeah, it's all necessary stuff and we'll get back to doing really product focused feature development really soon. Just in the meantime, just kind of keep it on writing your standard, like, startup web app admin back end stuff in Python.

Soroush Khanlou
Yeah. Checks out. Are you using Django?

Chris Dzombak
We are not. We're using a web framework called Pyramid.

Soroush Khanlou
Pyramid, okay.

Chris Dzombak
Yeah. Which is definitely not as widely used as Django. So django is more like analogous to ruby on rails.

Soroush Khanlou
Right, right.

Chris Dzombak
So Pyramid has a lot less of a, like a lot less opinion and a lot less convention around how you structure your app and it leaves a lot more decisions to yourself.

Soroush Khanlou
Is it kind of like Flask or Sinatra?

Chris Dzombak
So it also provides more like it provides more structure than Flask. Sinatra express that class of sort of like really simple handle this request framework. So it's kind of a middle ground between the pretty heavyweight, pretty opinionated frameworks like Django and Ruby and Rails and those really simple frameworks that give you basically a way to respond to Http requests and not much else.

Soroush Khanlou
Right. I heard about like a Sinatra alternative that I think was called Cuba.

Chris Dzombak
Spelled like the country.

Soroush Khanlou
Yes, spelled like the country. What's cool about it is I think it's 300 lines of code.

Chris Dzombak
Whoa, that's a small framework.

Soroush Khanlou
Yeah. Isn't that wild? I think it functions a lot like the sort of we mentioned, like Sinatra and Flask and stuff, but obviously very micro in terms of its size.

Chris Dzombak
Sure, yeah. Pretty cool. Which language is that?

Soroush Khanlou
Written in that's ruby.

Chris Dzombak
Okay, cool.

Soroush Khanlou
Yeah. I believe this is the one that I heard of. Yeah, it's supposed to be very small, which is crazy. Yeah. I'm looking at the GitHub now. 410 lines for Cuba RB, and then they have a couple of other small helper files. So it looks like maybe under 1000 total, which is pretty unreal.

Chris Dzombak
Okay, interesting.

Soroush Khanlou
Yeah. And the idea that what I heard about I can't remember what context this was in. I think it was like a Twitter thread or something. But basically they were trying to make a decision at a startup about what to use. And they could have used something like Sinatra or they could use something like Rails, but the developers all wanted to use something like Cuba because it was so small and so simple. And so they knew they could build whatever things they need to build on top of it. And, like, if Cuba ever went out development, it's 400 lines of code. Anybody can maintain 400 lines of code.

Chris Dzombak
Well, depends on the 400 lines.

Soroush Khanlou
No, that's very true. It's 400 lines of perl. You're on your own.

Chris Dzombak
400 lines of a web framework written in Bash, which exists, I forget, like, years ago.

Soroush Khanlou
Really?

Chris Dzombak
Yeah, I remember reading I mean, it's not like something you use in production, but I'll try to find a link. But it's like a web framework written like Flask or Sinatra or Express, but in Bash, like shell scripting.

Soroush Khanlou
Just googling here. There's a couple of things. One's called Lol, and it's a Bash web framework. And the other one is called Bash on Balls.

Chris Dzombak
Okay. I think Bash on Balls is the one that I heard about.

Soroush Khanlou
Yeah.

Chris Dzombak
I mean, let's commit May 2013. It's clearly not something that is actually used.

Soroush Khanlou
Right. Any open issues we got here? Let's see.

Chris Dzombak
What do we have?

Soroush Khanlou
One issue on August 2015.

Chris Dzombak
Missing a template doesn't really work on OS Ten.

Soroush Khanlou
Nice. Framework needs a task runner. Let's add some more features to it.

Chris Dzombak
Oh, man.

Soroush Khanlou
Written in bash. Bash on balls.

Chris Dzombak
Yeah. So there you go. You can do that if you want.

Soroush Khanlou
Web framework of anything.

Chris Dzombak
Looks like the Lol web framework is, oh, last minute. April 2016. So that's a little more read, a little more modern. Yeah, the README has a GIF of a cat playing a toy piano, so that's pretty professional.

Soroush Khanlou
Speaking of web frameworks, I think Vapor Three is starting to get into a more finalized situation. And I was trying to find some summary of how much is changing in Vapor Three because I knew they were, like, kind of moving away from the synchronous model that they had, where you get a function to handle, and that function has to return synchronously. And I knew they were moving away from that, but I didn't know how much and how much things were going to change. And somebody in one of these slacks sent me a very useful article that I'll throw in the show notes that kind of explains what they're doing, and essentially everything is going to move towards being future based. And so if you want to hit the database, that's a future. If you want to hit the network, obviously future instead of the way it was in vapor One and two, where those things were all just synchronous and your request handling thread would just be blocked until that came back.

Chris Dzombak
So this is a huge architectural change right. Both in how the server works and in how applications written on Vapor work.

Soroush Khanlou
Yes.

Chris Dzombak
This will require really big changes to applications which are currently using Vapor.

Soroush Khanlou
I remember doing the Vapor One to Two migration for Beacon, and that was like a day, day and a half, two days of work.

Chris Dzombak
Okay.

Soroush Khanlou
You can't even write the same code in this. I feel like you would really have to ground up change almost everything about every single function.

Chris Dzombak
It's almost moving from a Rails or Django sort of execution model to nodes. Right?

Soroush Khanlou
Yeah. Where it's like callback based. Well, essentially it's promise based.

Chris Dzombak
Right, right, exactly. Which works.

Soroush Khanlou
And I mean, I think it'll be good, but just switching to it will be pretty tough.

Chris Dzombak
So Vapor, of course, is a web framework for Swift. What futures are they rolling? Their own sort of Futures or Promises library? Or is there a popular implementation that they're going to use or has that not been decided yet?

Soroush Khanlou
No, I think it's almost all written. I don't know when it's coming out. I think they're kind of in the beta testing, try it out, get us some bugs and kind of let us know what's going on phase of the project. But no, I think it's pretty set how it's going to work. One thing I'm pretty sure about, I kind of want to dig into the actual branches and see what's out there. But one of the things I'm pretty sure of is that the future is not going to be error parameterized.

Chris Dzombak
Okay.

Soroush Khanlou
So if you have a promise of, I guess, a future value, it's going to be failable, but it's not going to tell you what type that failure comes in.

Chris Dzombak
I mean, that's kind of in line with the Swift philosophy of how errors get typed or don't, which we talked about before. We've talked about once or twice.

Soroush Khanlou
Yeah.

Chris Dzombak
Interesting. Okay.

Soroush Khanlou
I still don't know where I land on typed errors. I know I chose to do not error parameterized promises for my promise library just because it was a real pain in the ass to use. So I think they made the right decision here. And then I talked to one of their people, logan in a slack, and he was saying, basically, this is going to be a really rough transition, but it's going to be worth it in the long run. Because once Async await lands in Swift, the change there will be very simple and we're already going to be thinking in this future model of everything, So we're kind of like moving. We're skating to where the puck will be is essentially what his argument was.

Chris Dzombak
Right. And that totally makes sense. And that probably is why they're using things like errors that aren't parameterized on the type.

Soroush Khanlou
Right. Because Swift doesn't support that and it's like try and throw and stuff.

Chris Dzombak
Exactly. Yeah. So that totally makes sense. Okay, cool. Do you have any projects that you want to try in Vapor Three?

Soroush Khanlou
No. Beacon is kind of on the back burner for a little while.

Chris Dzombak
Okay.

Soroush Khanlou
I think we'll bring it back for WWDC, but I don't think it's necessarily like a viable product. So it doesn't have a lot of value for us to pour much time into.

Chris Dzombak
Do you have people using it now or has it kind of like no.

Soroush Khanlou
It'S pretty much fallen off.

Chris Dzombak
Okay.

Soroush Khanlou
It works best when it happens with an event, and we saw good results with that, with like 360 IDEV and WWDC, but trying to push the product out there and try to convince conference organizers and stuff to use it was tough.

Chris Dzombak
Sure. Yeah.

Soroush Khanlou
And we didn't really see that much of a future in it. And so we're just like, you know what, maybe this can just be like a service that we provide to the iOS and Mac and greater Apple community for WWDC, basically because it was successful there and it doesn't cost us much to run it. Heroku is pretty cheap, so we'll probably fix a bunch of bugs in the April and May and June time frame and then have that out for Dubdub this year.

Chris Dzombak
Cool.

Soroush Khanlou
And I don't think I'm going to be upgrading to Vapor Three for that. I think Vapor Two is good enough.

Chris Dzombak
And yeah, I mean, if you didn't see performance or scalability issues, will Vapor Two continue to be supported at all? Or is it kind of going to be like you're on your own?

Soroush Khanlou
Well, since when I download the code, I can run it for a while. I don't know how much support there will be in terms of answering questions and stuff, but I can kind of run it for a very long time. So I'm not super worried about that because we're not hosted on the vapor cloud or anything like that.

Chris Dzombak
I'm thinking more like security updates, that kind of support.

Soroush Khanlou
Yeah, that's a good point. I don't know what's going to happen with that. That's a very good open question.

Chris Dzombak
Okay.

Soroush Khanlou
Yeah. So maybe when Vapor Three comes out, decide it's really nice, I will want to kind of switch everything over. But for now, I think I'm good. It kind of makes me think that maybe this isn't the right time to do this transition. Because if they waited until, let's say, Async Await comes out in Swift Five, if they waited until Async Await came out, then all you'd have to do is add a weight in front of all of your function calls and everything would just kind of work. Right. And it would tell you, hey, this function needs to be awaited. So you would upgrade to this new version of vapor that's Async Ready and Swift Five at the same time, add the word Async to everything, and it would just kind of work. Whereas now you have to like because the language doesn't have Async Await. You have to use blocks. And so you're ending up tabbing your code in. You're adding flat maps everywhere to transform from one promise to the next, like chain from one to the next. They should have waited.

Chris Dzombak
So the idea is that this transition from Vapor Two to three is going to be really disruptive. And then the move to from Vapor Three to something that uses Async Await is going to be largely moving to code. That looks more like what you had with Vapor Two.

Soroush Khanlou
Yeah, that's my thinking.

Chris Dzombak
Yeah. That's an interesting problem. Do we know at all that Async Await is actually going to be part of Swift Five? I haven't really been following Swift development that closely, but my impression was that concurrency features are still quite a ways off.

Soroush Khanlou
Yeah. Now that I think about it. So Swift 4.1 is supposed to be out in the spring, which is like in a month or two.

Chris Dzombak
Yeah.

Soroush Khanlou
And I know they wanted to get to Async Await for Swift Five. Maybe they pushed it off. I know abi stability is very important and they said, whatever abi we end up with for Swift Five, is that's it? That's all it's going to be.

Chris Dzombak
What's in the Abi is in the abi?

Soroush Khanlou
Yeah, whatever's in the Abi is in the abi. Because they think Await is really just sugar around this kind of exact same block style of code. So I don't think maybe it won't make it for Swift Five.

Chris Dzombak
Now, do we want to talk about Swift 4.1? Since you mentioned it?

Soroush Khanlou
Yeah, we can. That'd be cool. It's a real grab bag of an episode.

Chris Dzombak
It is. But we're going to cover some interesting stuff. I also have a note on a heroku related thing we can maybe circle back to.

Soroush Khanlou
Oh, cool. Yeah.

Chris Dzombak
So Swift 4.1, what are the big, like, the big bullet points here? I think we have to note conditional conformances.

Soroush Khanlou
Right. That is like the elephant in the room. That is the thing that Swift 4.1 is going to bring.

Chris Dzombak
Yeah, I think we're all very excited about that.

Soroush Khanlou
We'll talk about conditional conformances in more depth in a second. But I think the only other thing I've heard about you know what, actually it looks like there is a couple of things. So one thing I heard about was that there was going to be a key transformation strategy for codable. That's like a sentence that would not have made much sense two years ago, basically, if all of your API uses snake case. Right. So it's like Word underscore second word. You can just say the transformation strategy for these coding keys is always going to be snake case to regular Camel case, and it'll just handle it for you. So you have to retype all those things. That's pretty cool.

Chris Dzombak
Yeah. Where previously the JSON keys had to what? Had to match property names, otherwise you had to define your own mapping, basically.

Soroush Khanlou
Right, exactly. And they had to map every single key. Had to map exactly or else you would have to define everything, I think.

Chris Dzombak
And so now every key can map exactly but via the transformation strategy, which can be snake case or like camel case.

Soroush Khanlou
Right, exactly. And then you can provide your own transformation strategies as well.

Chris Dzombak
Oh, nice. So that's a way that you can so if you have just one or two keys that don't conform to something standard, that's a way that you can still have something that isn't super repetitive.

Soroush Khanlou
Yeah, that's a really interesting idea because I assume the way that the custom transformation strategy thing works is you just give it a block and it transforms a string to another string. But yeah, you could just say, like, if the string is this, change, it this. If it's this, change to this, otherwise otherwise fall back to this other strategy. Or just fall back to leaving it alone.

Chris Dzombak
Yeah, or write your own little snake case transformation.

Soroush Khanlou
Right, okay.

Chris Dzombak
That's cool. I think that was the other big Swift 4.1 feature, which at least I'm aware of. But I mean, conditional conformance really is the really big news, I think.

Soroush Khanlou
Yeah. That really changes like, what kind of code you can write really fundamentally. One other quick thing I want to add is I'm reading an article and I think synthesized equatable and hashable is also going to be in 4.1.

Chris Dzombak
Really? Okay.

Soroush Khanlou
Yeah.

Chris Dzombak
Synthesized equatable and hash. Oh, so you don't have to implement this yourself or realistically, this is yet another Sorcery feature which Apple is sherlocking into the Swift language.

Soroush Khanlou
Well, they're kind of manually adding each of these sorcery these things that we use Sorcery for, but it's like just give us Sorcery. Like, let us just do this.

Chris Dzombak
Yeah, well, I mean, it's like clearly nice to have first class language support and first class tool chain support for all this. Right. I mean, Sorcery is great, but it is something that you have to put into your tool chain yourself.

Soroush Khanlou
Right. What I'm saying is, like, if they gave us some kind of tool to build these little components ourselves, then we would be less reliant on having to automatically like having to build each of these features one by one or wait for these features to trickle out one by one from Apple.

Chris Dzombak
I mean, I think that's true, but also I don't know if I'm struggling to come with a good argument here, but I don't think that this is something that the same group that writes your programming language and compiler. And everything needs to provide you with effectively, code generation tools. They've provided you already with Source kit, right? With the tools that you need to build tools like sorcery.

Soroush Khanlou
Yeah, that's a fair point. And I think one of the best counterarguments to why you should use Sorcery is like, what do you really need it for? And the big answers are synthesizing equatable, synthesizing hashable, and synthesizing, like, all cases for an enum. And it's like, well, if you can just kind of get this from the compiler, it's fine.

Chris Dzombak
Right, and there surely are more unique or more advanced transformations and code generation tasks. And for that, the team provides like, first class support for tools that would need to deal with the syntax tree.

Soroush Khanlou
Right, right. Yeah. So synthesize, equitable hash roll. Pretty cool. Yeah, but yeah, it's a big bombshell. Conditional conformance.

Chris Dzombak
Conditional conformance.

Soroush Khanlou
Huge.

Chris Dzombak
Which one of us wants to take a stab at explaining conditional conformance?

Soroush Khanlou
I say go for it.

Chris Dzombak
All right, I'll do my best. Let's remember writing Python, which doesn't have conditional anything, doesn't have well, it has conditionals, I guess. It doesn't have conformance, doesn't have generics. So in Swift, up until now, there has not been a way to add protocol conformance to some, you know, to a class or to some type only in certain cases, like if the clif if the class has a certain associated type. Right. Are they still called associated types?

Soroush Khanlou
Is that the well, it also works for generics.

Chris Dzombak
Right, okay.

Soroush Khanlou
Maybe it only works for generics, actually. And you can use associated types to get to generics.

Chris Dzombak
Right. Associated types have like a complex but fairly close relationship with generics. Right. So conditional conformance is a way to write basically that, say, an array or say a collection conforms to some protocol when the members of the collection conform to some protocol.

Soroush Khanlou
Right, right. So what's a good example of this?

Chris Dzombak
I think equality. I think equatable is a textbook example.

Soroush Khanlou
Right, yeah, totally.

Chris Dzombak
So let's say you have some collection and you want this collection to be comparable with some other collection. Only in the case where the collection members are equatable or comparable. Whatever we're concerned about conditional conformance lets us add this in an elegant way as opposed to what we've been doing previously with things like arrays, which is defining a whole lot of operators outside of the array class that let you make equality checks on arrays of various types, which breaks down in a number of interesting cases.

Soroush Khanlou
Yeah, that sounds 100% right. I have one quick thing I want to ask you about, which is you mentioned comparable, and I know strings are basically collections that are comparable, but what does it mean for an array to be less than another array?

Chris Dzombak
Well, okay, so I said comparable where I really meant equatable. I'm just trying to I'm trying to think of other examples that are not equatable just to throw something different out.

Soroush Khanlou
I wasn't trying to do like a gotcha or anything. I am curious because you can do comparable to two strings, and strings are basically collections. So why can't you do is there a case where you would have two.

Chris Dzombak
Arrays and you'd strings have a kind of messy definition of comparable that it depends on Unicode and a lot of sort of domain knowledge about what a string is a collection of. Right. I don't think you can come up with a useful general case definition of comparable for a collection period.

Soroush Khanlou
Right. But if you can define comparable for two characters, which I think you can, then you could say imagine a generic comparable algorithm over a collection that falls back to its elements, in which case that would be the character.

Chris Dzombak
Sure, okay. Yeah. And that would be something that you could apply to strings as a collection of characters or to some other array where you have some notion of individual elements being comparable.

Soroush Khanlou
Right. Would that ever be useful?

Chris Dzombak
I guess you could probably come up with something right.

Soroush Khanlou
If you had like an array of version components. My app is version 2.0.1, and you wanted to compare those, like, pairwise there's currently in the standard library, there's operators for tuples of Arity up to six, I think. So if you can make a tuple out of your version, then you can compare them.

Chris Dzombak
Right.

Soroush Khanlou
But this would allow arbitrary lengths to be compared with arbitrary lengths, which would be kind of cool.

Chris Dzombak
Yeah, it would be.

Soroush Khanlou
Other than that, I can't think of anything.

Chris Dzombak
Okay. So sort of going down that same path, I can't think of a specific example right now, but there definitely are other cases where you want to sort things by, where you want to sort like, decimal numbers or lists of decimal numbers by, like, okay, sort the most significant or you sort the largest digit right. And then the next largest, and so on and so forth.

Soroush Khanlou
Right.

Chris Dzombak
Or not digit. But note, let's say you want to sort a list of IP addresses or something like that. Right, yeah. That makes total sense for whatever reason you might want to do that. So there was a good episode, if I'm remembering it, there was a good episode of Swift Unwrapped a little while ago where they discussed conditional conformance and maybe other Swift 4.1 stuff. I don't remember exactly.

Soroush Khanlou
We should put that in the show.

Chris Dzombak
Notes, but we'll definitely throw that in the show notes. Swift Unwrapped in general is a great show if you want to dive into what's going on in the Swift sort of language development world.

Soroush Khanlou
Yeah. They go in a little bit deeper and on a little bit more specific set of topics than we do, I would say.

Chris Dzombak
Yeah, definitely. And I think they know what they're talking about a little more than I.

Soroush Khanlou
Do, I think than both of us.

Chris Dzombak
Fair. Yeah.

Soroush Khanlou
So other things that conditional conformance is good for. So you mentioned equatable, it's good for hashable. So an array is hashable if its elements are hashable.

Chris Dzombak
That's a really good and that's something that applies probably more often than equatable.

Soroush Khanlou
Even one thing that I heard, I found a tweet about this, I think from Slava, but he was saying that the two features in 4.1 don't actually work together yet. So if you have something that synthesizes a hashable conformance, you can't use that with conditional conformances yet, which is really funny. I'll try to find that tweet for the show notes.

Chris Dzombak
I'm sure that'll get this happens with software that's in development.

Soroush Khanlou
Yeah, that's right. I found the tweet. Yeah, the joker from Slava. But I don't know if anybody's specifically responsible for this, but Swift four point's biggest features, conditional performance and automatic equatable synthesis won't work together. So we'll toss that in show notes too, which is pretty funny. But computers are hard.

Chris Dzombak
Computers are hard, yeah.

Soroush Khanlou
Conditional performance is also useful for codable. So an array is codable if all of its elements are codable, although somehow they're kind of doing that already. I don't really know how they're doing it, but there have been situations where I tried to write my own kind of codable thing and I would say, okay, I have this object storage and this object storage is generic over some type and found at some location on disk. And then when I want to save and write, when I want to read and write those things to and from the disk, I would have to have a separate set of methods for arrays because I couldn't express to the compiler, I want an object storage of an array of, let's say, locations. Can't express that without conditional performances because not all arrays are going to be encodable. Some of them are going to be encodable because they have encodable elements, but the other ones aren't going to have that, so they won't be encodable in any way. So you end up having to make some kind of sacrifice somewhere. They're getting around that in the codable protocol itself somehow. Because you can do in Swift 4.0, you can say, I want you to decode a type of array of locations self like that type, and you can get away with it and it works somehow. I don't know how they make it work, but they make it work.

Chris Dzombak
I don't know much about this either. I'll just note that in general, the way that stuff like this kind of works now is by the definition of generic functions outside of the protocol or outside of the type that they're concerned with and specialized to some case. And that often involves some code generation or something like that.

Soroush Khanlou
Yeah. So basically if you want to write a lot of your own constructs around codable and stuff, you will be able to get that with these with conditional performance. Or like one thing I've always wanted is basically this concept of like a JSON value. I want to be able to express that numbers, boolean, strings and null are all JSON values. Optionals are JSON values only if their contents are JSON values. Arrays are JSON values only if their contents are JSON values. And then dictionaries are only JSON values if their keys are strings and their values are JSON values. And then once you have that, then you can kind of bridge a little bit and you could say, okay, well, now I want to describe something called JSON convertible so that now a date can be converted into something that's a JSON value. And then that way I can use a date in a dictionary and pass it to some part of my app, and then that app automatically knows how to convert it to JSON. And you can't do those last three critical components. The optional is only a JSON value if it's contents or optional or JSON values and so on if you don't have conditional conformances. So there's a lot of really cool, weird stuff you can write with conditional conformances. It's going to be huge.

Chris Dzombak
Yeah, it'll be huge. And also, I mean, it'll work kind of intuitively. Right. This has been one of the counterintuitive parts of Swift generics for quite a long time, is that I can't say this collection is hashable if its elements are hashable.

Soroush Khanlou
Right, right, exactly. And I feel like everybody who learns Swift hits that point where they're like, I want to express this, but I don't know what keys to hit to make it look right to the compiler.

Chris Dzombak
Right.

Soroush Khanlou
And then you go and Google and then you learn about this fundamental flaw.

Chris Dzombak
But limitation.

Soroush Khanlou
Yeah, temporary limitation that's going away hopefully in a few months.

Chris Dzombak
Yeah. And I'm really glad that it's going away. That's really exciting.

Soroush Khanlou
Yeah. And I think they've kind of been tweeting here and there about how many lines of code the standard library has actually dropped and how much of the boilerplate generation stuff they've dropped because of conditional performance.

Chris Dzombak
It's something like a 5% reduction in code size, if I'm remembering.

Soroush Khanlou
Pretty tight.

Chris Dzombak
Yeah. I think I probably got that number from Swift Unwrapped.

Soroush Khanlou
There's a Swift blog post about it from the Swift official blog, and I'll put that in the show notes as well.

Chris Dzombak
Oh, that's right. Yeah. I'd forgotten about that blog post. Yeah, this is a good read.

Soroush Khanlou
Yeah, it is, for sure. And they explain why they need it and what they can use it for. So I think we're going to be able to make some really powerful things with performances. You want to hit me with that thing about Heroku curious.

Chris Dzombak
Now this is something which I learned about recently from a friend of the show, Andrew, who also coworker of mine. Andrew. Hi Andrew. This is a little project called Daku. D-O-K-U which is, according to the language statistics here, a bunch of shell scripts or a bunch of, like, shell related shell script related tools and a little bit of little go little Python, which you can deploy to a virtual machine somewhere and which gives you a heroku like experience for deploying and running an application. So if you set this up on, say, a VM at DigitalOcean or Linode, you can then push code to it and it reads the same I don't know that much about Heroku, but it'll read the same little files that describe how this application gets deployed and run, and it'll run it on that VM for you.

Soroush Khanlou
This is amazing.

Chris Dzombak
Isn't that a cool idea?

Soroush Khanlou
I was literally in the elevator, like, two days ago, being like, it would be so cool if I could just have my own mini Heroku I could just deploy to and not have to worry about any of the nonsense of, like, bank roku or dealing with this.

Chris Dzombak
Is so I have got some good news for you.

Soroush Khanlou
Tell me. Tell me the good news.

Chris Dzombak
It's that this exists and you can have your little personal Heroku. This is really so I haven't actually tried this, mostly because I can't come up with a good excuse. Like, I don't have anything that I want to deploy that isn't already deployed.

Soroush Khanlou
Right. Well, maybe you could just deploy something for fun.

Chris Dzombak
Yeah, I mean, maybe I should, and I get yeah, it doesn't have to be something that lives forever. So I've never tried this personally, but apparently it works.

Soroush Khanlou
The configuration files that define how Heroku works are their build packs. There's, like, an app JSON file and then something called a proxy.

Chris Dzombak
Apparently, this was compatible with those Heroku build packs.

Soroush Khanlou
That is so cool. That is awesome. I'm, like, maybe just going to move everything over to this.

Chris Dzombak
I mean, the caveat here is that you're responsible for maintaining this now instead of Heroku, but that's why you lose.

Soroush Khanlou
This new Linode instance that I got. Linode. Linode. Whatever it is. I'm paying, like, $4 a month for it. It's, like, unreal how cheap it is.

Chris Dzombak
Oh, yeah.

Soroush Khanlou
And I was paying $40 a month of rack space for the exact same thing.

Chris Dzombak
What?

Soroush Khanlou
Yeah.

Chris Dzombak
Wow.

Soroush Khanlou
I know.

Chris Dzombak
That is absurd. I haven't paid $40 a month for a VM ever.

Soroush Khanlou
And I think we're paying $16 a month to Heroku just for beacon. Yeah. And so if I could get this to support, like, postgres, or I could just keep my postgres on Heroku if I want, but basically, if I get this to support Postgres, I can just deploy everything.

Chris Dzombak
This definitely supports postgres.

Soroush Khanlou
Yeah. I could run everything for probably $10 a month cheaper than any one of the things I had before.

Chris Dzombak
Yeah. So, okay, let's say I want to set this up for myself and deploy something. What should I deploy?

Soroush Khanlou
You should make a vapor app. Make a Vapor app that do you.

Chris Dzombak
Think this supports Vapor?

Soroush Khanlou
Yeah, because there's Vapor build packs. Yeah.

Chris Dzombak
I'm going to look into this.

Soroush Khanlou
Yeah, make a Vapor app that has an endpoint that every time you give it some text, it spits back the text. It sorts the text? Yeah, like spits back pig Latin. Or it does some kind of transformation on the text and then it gives it back to you.

Chris Dzombak
Okay, cool.

Soroush Khanlou
Do that.

Chris Dzombak
Yeah.

Soroush Khanlou
Now we can play with Vapor, and you can play with this docker thing.

Chris Dzombak
And you can does this actually support Swift deployment? Because oh, my God, if it does.

Soroush Khanlou
So build packs are just bash scripts and, like, docker containers are just bash bash scripts. Everything's just bash scripts. So, like, if you're thinking run bash scripts probably gonna work for you. This is so freaking cool. 15,000 stars, too. People know about this. This is a real thing.

Chris Dzombak
Always that loud noise outside. I'm going to go look out my window for a second.

Soroush Khanlou
Oh, boy. This is how serial killer movie starts.

Chris Dzombak
I don't know. I think it's just I don't see a car accident outside, so I don't.

Soroush Khanlou
Know if you're I didn't hear I don't know if your microphone picked it up, but I'm glad you're safe.

Chris Dzombak
I was listening.

Soroush Khanlou
I was really worried you were going.

Chris Dzombak
To I was on headphone wander off.

Soroush Khanlou
And I was going to hear a Chris shaped scream and a Chris shaped scream. Title name. My new novel. OOH, I do like that for that. Cool. This is fun.

Chris Dzombak
Nice. Yeah. I will start looking and seeing if I can deploy Swift with this.

Soroush Khanlou
This is cool, man. This is really cool.

Chris Dzombak
Well, I'm glad that I could blow your mind with this.

Soroush Khanlou
Yeah, I really appreciate it. This is fucking cool.

Chris Dzombak
Are we allowed to swear on the show?

Soroush Khanlou
It's patreon man we can do anything we want.

Chris Dzombak
Oh, that's right.

Soroush Khanlou
Hey, Patreon. People.

Chris Dzombak
Hell yeah.

Soroush Khanlou
Love you. All right, should we wrap up?

Chris Dzombak
Yeah. Since you mentioned this, Patreon, as always, or as we've forgotten to say last couple of episodes, because we have a less formal format, thank you a lot for your support. You are making the show possible, and we appreciate that.

Soroush Khanlou
Yeah, we think you're great. We think you're just great.

Chris Dzombak
We think you are great. On that note, I don't know much else to add. We didn't really cover much from the topic ideas list. Maybe next week we'll discuss Swift Evolution 195 Dynamic member lookup, maybe we'll discuss Marco's end of the Conference era blog post. Maybe we'll discuss more about Android and Kotlin. Oh, I want to hear more about your Belkin and Wimo adventure.

Soroush Khanlou
Actually, there are some huge updates on the Belkin front and huge to hear those.

Chris Dzombak
Tune in next week on Fatal Error.

Soroush Khanlou
Sweet. Eat. Talk to you soon, Chris.

Chris Dzombak
Bye, sir.

