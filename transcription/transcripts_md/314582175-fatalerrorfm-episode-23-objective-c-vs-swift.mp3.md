Soroush Khanlou
Welcome to Fatal Error episode 23 I'm, Sirush. Khanlou.

Chris Dzombak
And I'm Chris De Zomback.

Soroush Khanlou
Before we get started with our topic today, we just want to let everybody know and ask politely. We have a patreon, and if you support the patreon, it's $5 a month. You get extra episodes. So if you've only been seeing odd numbered episodes in your feed, the reason for that is all the even numbered episodes are in patreon. So if you want double the Fail error, you can do that. It's $5 a month. You'll get access to the whole back catalog and you get caught up on all the interesting things that we've been talking about over there.

Chris Dzombak
Yeah, we'll put a link in the show notes. This is just a way for us to start recouping a lot of the costs that we've been paying in terms of editing and equipment to put this podcast together. And in a little bit of a change from season one, we've been recording one episode every week and only posting episodes on the main public feed that you may be subscribed to every other week. So you're missing out on half the episodes we've recorded. Now, we would like to keep the podcast itself ad free, and this is a way to help us do that.

Soroush Khanlou
Also, to our patreon supporters and those who decide to back us, we really appreciate it. You are the ones who make this podcast possible. And yeah, it just means a lot to us that you would fork over your hardearned money.

Chris Dzombak
Yeah, thank you. We really do appreciate it. So on to today's topic, which is one that's been sitting in our episode ideas list for quite a while, and that is Objective C versus Swift.

Soroush Khanlou
It's been sitting in our episode ideas file for so long that I think Chris forgot what exactly it was we were going to talk about.

Chris Dzombak
I think that there was some sort of argument or disagreement, and so we decided to put this on the list and then I've completely forgotten what it was.

Soroush Khanlou
I don't remember the exact thing that we were disagreeing about. I do that there's a thing that I see in the community, which I think is where our discussion started, which is that Objective C is over. Objective C is the old way. Swift is better than Objective C in every way. And I think with any broad, sweeping, categorical statements like that in programming, there's going to be cases where it's wrong. And so some of the stuff that I'd like to talk about with this is like, where does Objective C shine versus where does Swift shine, how do we write Swift code to be Swifty? And how do we write Objective C code to be objective cesque?

Chris Dzombak
All right, so I was wondering if you're going to try to say objective ce. I'm glad you came up with objective CES.

Soroush Khanlou
Nice little detouristic there.

Chris Dzombak
Yeah. So I guess let's dive right in. Then. So I've been writing Swift full time for the last year or so at this point.

Soroush Khanlou
Yeah, I think a year and a half for me, a little under a year and a half.

Chris Dzombak
So maybe where do we want to start here? Things that Swift excels at or things that Swift brings to the table?

Soroush Khanlou
Let's talk about metaprogramming. Okay, so no then what is your feeling on metaprogramming?

Chris Dzombak
I think metaprogramming is a useful and powerful tool. I think that it can be done safely. I think that Objective C's model for metaprogramming comes with some sharp edges that we need to be aware of.

Soroush Khanlou
Yeah, I think that's pretty much true. Right when Swiss started to become popular is right around when I started learning about those rough edges, those sharp edges rather of Objective C and starting to use them kind of to my advantage and taking situations where I would take some API response, which would be like a string, sort of like an enum. And I would map that into a class and I would initialize that class. And so I'd have like a really rich polymorphic object with a protocol that would say, like, this is like it was like a richer enum. It objectively. We only had C based enums. It's kind of like a rich way to do enums. And then it was like a metaprogramming way to get from just the string that the API would respond with to an actual class that I could instantiate. And it was a nice little trick and it saves a little bit of code here and there. And I really was starting to get used to it and starting to like it. And then along came Swift. And Swift totally upended a lot of that stuff.

Chris Dzombak
That's definitely true. We do lose some convenient or neat tricks like that that we could play in Objective C when we moved to Swift.

Soroush Khanlou
I'm curious, did you ever write any metaprogramming stuff in Objective C? Anything basically involving like NS selector from string, maybe perform selector, although that can sometimes be not that metaprogramming NS classroom string, that's a big one. Or like instance where you can get implementations for specific selectors.

Chris Dzombak
Yeah, I have done some of that. I forget exactly what my use case was because this was a few years ago, but I've worked pretty extensively with the forwarding machinery or message forwarding machinery that Objective C has. So yeah, I mean, I can definitely appreciate some of the use cases that there are for this sort of rich metaprogramming support.

Soroush Khanlou
Yeah. And that stuff I really do think that it changes the way that you write code. Like if you have a Ruby developer, ruby has very rich metaphor. And if you ask a Ruby developer to solve a problem, and you ask a Swift developer to solve a problem, you're going to end up with depending on the actual problem itself. But like something like an enum that comes down from the API as a string. Like the Ruby developer might try to do some kind of like class based instantiation based on its name. And the Swift developer will probably make a string representable, enum and map it that way and it really changes the way that you solve problems, I think.

Chris Dzombak
I think that's definitely true, although there weren't a lot of cases. I feel like in most Objective C code bases where you actually solve problems this way, where you usually would reach for these tools.

Soroush Khanlou
Yeah, I would say the biggest one was any JSON mapping, which JSON mapping solved problems. But yeah, there was, like, Mantle and JayZ object mapper. And I even wrote my own. I think tons of people wrote their own, where basically it would loop through the keys of your JSON dictionary, figure out which keys that corresponded to on your destination object, and then use key value coding to say, assign this value for this key with this name, and it would set that property for you.

Chris Dzombak
Yeah. So what are the disadvantages of having this kind of power and of writing code like that in Objective C?

Soroush Khanlou
The big one is you don't know if you did something wrong until runtime. Even if you are pretty good at programming and you don't ship any bugs, you still will never catch a bug before it hits the runtime because you're kind of programming at the level of the runtime rather than programming at the level of code. I got into a big disagreement on Twitter about what exactly metaprogramming is, which is kind of it's a tough thing to answer.

Chris Dzombak
Yeah.

Soroush Khanlou
So I don't want to get too deep in that discussion, but basically you're programming the runtime directly rather than programming in the language which generates that runtime. And so you're not going to be able to figure out anything until that code actually runs and you see what happens. So your loop is a little bit looser in terms of like you just don't know if you did wrong until the program actually gets just run. There are sharp edges of like if you try to assign a property to a value that is not the right type, the runtime won't complain. It'll happily assign that value and then when you go to use it, you'll realize, oh no, I have done the wrong thing here.

Chris Dzombak
And that crash, you will probably notice, is often far away in the code base from where this bug actually exists.

Soroush Khanlou
Exactly. One of the things I really do appreciate about Swift is it has a very early crash, early mentality of just like, if something's not going to work, it's not going to work at some start point, rather at some crazy endpoint.

Chris Dzombak
Right. Or it won't compile, which is even.

Soroush Khanlou
Before a start point, which is even nicer. And so none of that is to say that well, because that stuff's impossible in Swift. And then I reject Swift or whatever. It's just to say that a problem such as JSON parsing that I would solve with metaprogramming in objective C. The derrigier solution for it now is basically using type inference and basically throwing errors and using that to write really concise code that describes how to map from your JSON object space to your domain object space.

Chris Dzombak
I'm not convinced that doing that explicitly is a bad thing, honestly.

Soroush Khanlou
Can you expand on that a little bit? What do you mean by explicitly, like.

Chris Dzombak
Having to write, like writing out that this property gets gets populated from this field in JSON.

Soroush Khanlou
Right. So the objective C way you would have like a dictionary would be like a class property that would like map between your JSON keypaths and your objects property path, right?

Chris Dzombak
Yeah, I guess.

Soroush Khanlou
Do you have that code? You have to have that code somewhere. Let me ask you this. Java has the ability to have they call them annotations. So each property you can say like, if you're working with JSON, this thing is going to have a key. Let's say it's a Latitude property. The key might be Lat L-A-T. And so you use that basically to not necessarily generate code but work with properties and you can enumerate them and then get all their annotations and find specific annotations to do specific things. Do you consider that as explicit as the Swift way or as metaprogramming as the objective C way or somewhere in the middle?

Chris Dzombak
That seems more like the objective C metaprogramming approach to me because if you squint, it kind of looks it all kind of looks more or less the same.

Soroush Khanlou
Very blurry, I think.

Chris Dzombak
Well, in the Swift model, these things can get like these things can be type checked ahead of time.

Soroush Khanlou
Right, right. Everything except for like the actual JSON part of it.

Chris Dzombak
Right.

Soroush Khanlou
If you are missing a key or if you have a key and you expect it to be a string but it's actually an integer, that stuff will mess up.

Chris Dzombak
I don't know. I guess that's weird, right? Yeah. Maybe these aren't like if you're already writing a dictionary to map JSON keys to your properties.

Soroush Khanlou
Right.

Chris Dzombak
This is just like an implementation. It's a different implementation.

Soroush Khanlou
Right, right. And whether you choose to write that implementation in terms of basically a dictionary that maps those things or code that maps those things is kind of up to you. The benefit of the metaprogramming way is also you get code to go backwards for free back to a dictionary, which is not that useful, but that depends.

Chris Dzombak
On your use case. In a lot of cases, like, you never transform one of your domain objects back into JSON and send it up to a server. You're probably calling some API endpoint that does specific things with other properties that you pass up.

Soroush Khanlou
Yeah.

Chris Dzombak
One thing that doing it the sort of Swift way gets you is that if you're initializing like an object or a struct with things that you expect to get from JSON, it's not possible. Or you will catch earlier the case where something that you expected to be in JSON isn't there, right?

Soroush Khanlou
Not necessarily, no. Right. So you could write the Objective C code such that if the I don't know if you have access to the types at this level, but you could basically say if this key is missing, just crash. Right? You could say stuff like that, that's dependent sort of on the implementation of how your object mapper works, I guess.

Chris Dzombak
So now you're annotating now you're writing this metadata that says map this JSON field to this property. And this has to be like this is not optional. And at this point this is looking more and more like you're, more and more similar to what you'd write in Swift.

Soroush Khanlou
Yeah, that's a great point. That's a great point is in Objective C we never really had a way to say at least the object member I wrote I don't know what other people wrote, but you didn't have a way to say, and this key, if it's not there, do this thing, or if it is there, do this other thing.

Chris Dzombak
Right. It's been so long since I looked at any object mappers in Objective C. I feel like there may be some way to in some of them you may be able to add like a hook that runs after it reads or doesn't read. So what were we going to disagree on in this episode?

Soroush Khanlou
I'm not sure. Objective metaprogram was always really weird because you couldn't do everything right. In Ruby you can generate brand new functions that you could call because those functions don't need to exist at compile time. So on Active Record base for Active Record in Rails, if you have a property called Title, you get a class method called Find by Title for free. So as long as you have this property, you get this method for free. You can call that method from anywhere and it's fine. But Objective C you can't do that because at compile time that function won't exist. And so you won't be able to even compile a program that calls it. But what you could do is you could do the opposite, where basically you would say at Runtime, I'm going to generate this selector, I'm going to generate this function, name this message and send it to this object. And the object being basically the programmer can choose whether or not to implement that message and respond to it. And if they do, I'll use that, and if not, I'll fall back to some default.

Chris Dzombak
And this is where the really sharp edges come in. There's just so much room for error here that can't be checked ahead of time.

Soroush Khanlou
Would you be surprised to know that core data does its very thing?

Chris Dzombak
No, not at all. I know. Yeah.

Soroush Khanlou
So core data is validators, where they basically pass you a property and I think it's in out, and they also pass you an error, lets you if you choose to implement, let's say again, you have a core data object with a title on it. If you implement the method validate title and they'll pass you, let's say, the string for the title and an error, you can choose to do whatever you want there. So you can choose to populate that error with something, at which point, like, the save will fail. I think, I don't know, coordinated that well. Or you can choose, I think, to even update the title. So if the title comes in not long enough, you could pad it or something. That's a bad example. I don't know, something. But there was code that did this, and I also wrote code to do this for configuring table cells. I had this very metaprogramming table view controller. I know some of the folks who had to work with that after I left, and I deeply apologize to them. But the code seemed like a really good idea at the time.

Chris Dzombak
So I'm glad that you mentioned you deeply apologize to them because this brings up another concern, which I have, which is the maintainability over the long term of code that's written like this in this style, in the core data example, you have the name of a validator function that is tied to the name of a property. And if for some reason the name of that property changes and the name of the validator function doesn't change, nothing's going to catch that until something blows up way later because an invalid name got into the system somehow. It's almost like stringly typed programming. Right. They're just tying things together just because something else happens to exist that has the right name. Just seems so fragile to me.

Soroush Khanlou
Yeah, it's a very great point, and.

Chris Dzombak
It may be something that you'll remember when you're maintaining this system, but the poor developer who inherits this system three years later and has to maintain it, having all that sort of magic in the code base, frankly, is just hard to explore and maintain.

Soroush Khanlou
Yeah, it's interesting that you call it magic. There's that quote about how basically magic is the opposite of boilerplate and if you increase one, you decrease the other. Right? Yeah. And part of the point of the library that I had written to do all this like metaprogramming magic with table views and stuff was to decrease the boilerplate. And it worked. It was good. But again, magic, like it was doing some stuff down there.

Chris Dzombak
Yeah.

Soroush Khanlou
I had been working a lot with Rails developers at the time that I wrote this. This library is open source. It's called instacoco. Anybody can look at it.

Chris Dzombak
Oh, I remember that.

Soroush Khanlou
Yeah. And that has the object mapper in it that has all the table view of metaprogramming magic. I was working with Rails developers. And I was like, they have something that lets them do tons of interesting things with very little code, and we can debate simple versus easy again. But it just seemed like objective C never got that. And I tried to write something that would fill that role, and it did to some degree. My hope, though, was that it would have any kind of traction that people would actually want to use it. And if I think the community is more familiar with that kind of thing, then it's not so weird to have code like that. And this was also all before Swift when I wrote this thing.

Chris Dzombak
So this is something that I was just going to say that I hadn't really thought about until now. Part of the reason probably for this is not language idioms, necessarily, but community idioms in the Rails world. Rails developers, even fairly new Rails developers, know and learn about what sort of magic happens and where the magic is and how to use that magic to their advantage. And it's very much like almost a community standard, right? Whereas we don't have any sort of standard like that from any code samples from Apple, any tutorials from Apple, which are where most people at least start learning about iOS. There aren't really any commonly accepted, like idioms or patterns. Very relatively few objective C frameworks make use of this kind of stuff. And maybe that's part of the reason that when you do come across this in an objective C code base, it feels more like a mysterious magical maintenance nightmare, at least to me, than it would in the Rails world. Although I also, as a as an inexperienced, very inexperienced Rails developer, I always, like, kind of struggle whenever I'm thrown into a Rails code base.

Soroush Khanlou
Yeah, I think that's an absolutely fair point. Part of my feeling with this whole library was like, we shouldn't be afraid of metaprogramming. There's another tool that we can use, and in as much as we can use it to write less code. Like, if you can write a table view that's right, that's correct. Once, yeah, it will have sharp edges that first time you write it, but theoretically, if that abstraction is solid, you can reuse that same with an object mapper or anything else. But yeah, I absolutely feel you that it was just like your community. I think map was very similar as well. I was four, I think was when blocks came out. Nobody knew what map was, even if there were people in other programming disciplines who are very familiar with it. For us it was weird. And it's only, I think once, really, once Swift came out. And it was like a part of the standard library that people felt much more comfortable, like, working with that stuff and writing that stuff. I remember when I saw it, I was like, this is voodoo magic nonsense that I do not need. And now to try to correct code without it would be, I mean, impossible.

Chris Dzombak
Yeah, absolutely. So one thing that I think we both wanted to mention, going back to the example of the validators, maybe validators yeah. Is that some of the things that we would achieve with metaprogramming, we can sort of achieve with code generation, with tools like Sorcery that provide us with some magic in the form of just automatically generated method implementations. Right. Automatically generated interfaces in some cases. And those come with the advantage that they get checked at compile time. So if you have made some error, then the compiler is much more likely to catch it. Right. And yet it's still not something that you have to go in and write a whole lot of boilerplate yourself. That's one sort of compromise that you can make along the spectrum of boilerplate versus magic.

Soroush Khanlou
Yeah, absolutely. I think Sorcery goes a long way in papering over that particular distance between objective scene Swift.

Chris Dzombak
Yeah.

Soroush Khanlou
I am a big fan. I don't ever want to go back to the world without sorcery it's really nice.

Chris Dzombak
Yeah, we're using it fairly extensively at this point in our app, at least for hashable and equatable implementations and for a couple of other things as well.

Soroush Khanlou
Yeah, I really also like that it draws a distinction between here now, right now I'm writing template code and right now I'm writing real code. Whereas in Objective C it was always and Ruby, it's very blurry. I mean, it's all just ruby. Like you're just writing methods and they're just doing stuff in objective C. It's at least it's like some of it's C, but then some of it's also like objective C. I think responsive selector and perform selector are just objective C messages. But to create a selector that's like a C function that just is free floating and I really like that. It really draws a sharp distinction between here you're writing template code and here you're writing Swift code. I think that part of it's really nice as well.

Chris Dzombak
Absolutely.

Soroush Khanlou
Yeah.

Chris Dzombak
So a while ago in the Swift community, there was a whole lot of grumbling about how Swift took away Objective C's dynamicism.

Soroush Khanlou
I think that's right.

Chris Dzombak
And this was a terrible thing and was the end of the world. And I'm being a little bit dramatic here, clearly, but I haven't heard so much of that lately and I'm not sure if maybe I tuned out of some part of the community accidentally or if we're really hearing less of that as people get more used to writing things in idiomatic. Swift, do you have any thoughts on which one of those things happened?

Soroush Khanlou
Yeah, I think it was a little bit of a fever pitch just because a lot of people were talking about it. And I think the Swift core team or whatever did a good job of saying like, look, these features are here. You can bridge them from Objective C if you use the objective C runtime, it's not any less swifty, it's still swift and sort of like we want to add these features back. They're just not priorities right now. I don't think they're all going to come back. I don't think we're going to get like a fully message passing dynamic dispatch language, which to me is a shame. I mean, I think dynamic dispatch is really good, but a lot of this stuff I think we are going to get back. I think we're going to get really good reflection. We have okay reflection right now. I think we're going to get better reflection. You talked about macros a couple of times, which I think functions similarly to how we think of sorcery templates.

Chris Dzombak
Yeah, I think that when they say macros, they don't mean like, see macros.

Soroush Khanlou
Yeah.

Chris Dzombak
One of the things that you said was you think dynamic dispatch is really good and I kind of want to dig into because that's one of the things that came up again and again was the distinction between static and dynamic dispatch. And this is something that I think the Swift team argued and this is something that I don't fully understand. Why is dynamic dispatch in and of itself a feature that you're looking for? Is that really what's important or is being able to achieve certain higher level patterns really what you're looking for here?

Soroush Khanlou
For me, I mean, I don't need to implement a responder chain. Like UI kit will have to do that and they'll figure out how to make it work. I don't need to implement button tapping and stuff. UI kit will figure that stuff out for me and provide a good pattern. The thing that bothers me about the dynamic dispatch thing is that as far as I'm concerned, dynamic dispatch is the right answer. Because it lets you think of the thing that you're sending a message to as an entity, not as a thing that has many faces. And depending on what face is pointing at you, that's the response you're going to get. Does that make sense? Like, let's say you have a class that conforms to a protocol and then that class is subclassed with dynamic dispatch. No matter if you have a reference to that object as a protocol or as the superclass or as a subclass, you're always going to get the same response. You just have the thing. You don't know what the thing is, but you have the thing. And as far as I'm concerned, making it static or V table dispatch is fine, but that's basically an optimization on that. So if you know the class is final and you know that no protocol is going to override anything, then great. Go ahead and optimize the way that dynamic dispatch call inline it. Do whatever you want, but don't make it so that if I have a reference to the object as a protocol, I'm going to get some totally different response to if I have the object as its concrete class. That is the thing that Swift does right now, and it's super confusing. It causes bugs all the time and I find really frustrating. And that to me is a bug rather than just like an unimplemented feature or whatever.

Chris Dzombak
What do you mean I might be missing something here. What do you mean you get a different response if you have a okay, so imagine this.

Soroush Khanlou
There's a good blog post about this. I'll have to find it.

Chris Dzombak
Is this the thing where if you have a protocol that has a default implementation yes. Then.

Soroush Khanlou
For the listener. If you have a protocol where there's a function on the protocol called foo and the function is just in the default implementation and not in the protocol body itself, then if you override that function on the conforming type like a class. If you call Foo, the behavior of it depends on if you have a reference to the object as the protocol. Because that's statically dispatched. So at compile time, it only knows that it's the protocol thing, so it can only send it as a protocol. Or you might have it as the object itself, you know, that you have that concrete type, and so it will statically dispatch to that thing. And so because of that, and then if you subclass, it gets even more complicated. Please don't subclass.

Chris Dzombak
I kind of feel like you're maybe not confusing you're complecting the implementation detail versus the behavior of the language. Right. Given this exact same scenario, what would you expect to behave differently if you, Swift were entirely dynamically dispatched?

Soroush Khanlou
Yeah.

Chris Dzombak
The reason there's still two competing implementations for this method, right? One on the protocol and one on the class.

Soroush Khanlou
Right. The thing is that if you do declare the function signature within the protocol itself, not just in the extension, it is completely unambiguous, which one it calls it's not undefined behavior. It's very defined. It always calls the one you declared basically after, which would be the one in the concrete type, which is the one you want, because the concrete type is specializing the abstract type.

Chris Dzombak
Right.

Soroush Khanlou
I think that's the correct behavior in every case. The problem is that if you remove that function signature from the protocol, then a totally different thing happens. And yeah, that is kind of mixing up behavior for implementation. But I don't know what to call that behavior other than by the name of its implementation, which is dynamic dispatch. Call it message passing, if you like. I want to know that I have a thing, and then no matter how I send a message, I think I'm going to get the same response.

Chris Dzombak
If the Swift team wanted to solve this somehow and implemented and changed some dispatches under the hood to be dynamically dispatched, like, fine. But I don't know, it kind of feels just weird to say that you really want dynamic dispatch. When what you really want is like this specific behavior of the language to be more consistent behavior.

Soroush Khanlou
That kind of makes sense. Yeah, that's fair. Yeah, I think thinking about it in terms of you're always passing a message and if that message happens to be and if the code for that message happens to be inline, great. But that's like an optimization. That is not the concern of the developer. But with optimizations it has to behave correctly 100% of the time. You can't behave correctly 99.9% of the time, like 1000 do something totally weird. And thinking about it as message passing with optimizations to me makes more sense than like well, sometimes we're dynamic, sometimes we're static, sometimes we're v table.

Chris Dzombak
My point is just that it's possible to want consistent and sort of easy to understand behavior without even knowing the reason that under the hood that this behavior is different. Right?

Soroush Khanlou
I don't disagree with that all. And if Swift were just structs, it wouldn't matter. There were no protocols, there were no subclasses, it was just final classes and structs. It wouldn't matter what kind of dispatch you have because you always know what kind of objects you have. But because we have those things, we need behavior that we can reason about. Another issue that we ran into with static dispatch, this one's a little bit harder because it's related to operators. And operators kind of have to be statically dispatched rather than messages passed to a specific object to take another object. And what basically was going on was we were trying to compare two sequences to see if they're the same. And that function, it's called elements equal, uses the not equal operator to determine if anything is not equal. And it also makes sure if one runs out before the other fine. So what was going on is we had two sequences of NS objects and with NS object, the equal equal operator is designed to forward to the is equal function. The receiver is the left hand side and then the first parameter is the right hand side. The issue is that we didn't know that. So what you're supposed to do with an NS object is you're supposed to override is equal, the function on the thing itself. But we overrode the equal equal because we're trying to be swifty, trying to be cool. And we needed NS coding, right? So we're trying to be swifty, we're trying to be cool, we override equal equal. And the implementation of not equal the operator is statically dispatched to equal equal. So this sequence thought it had a bunch of NS objects. And those NS objects, their static equal equal operator pointed to the equal equal or the is equal implementation for the object itself, which was based on pointer equality. So while if the function that we were calling this like element equal had used the equal equal operator, everything we would find, but it used the not equal operator, which forwarded to the equal operator, and then it negated it, and then that forwarded to the is equal thing, which we hadn't implemented.

Chris Dzombak
So the thing that you implemented, the equal equal operator for your custom NS Object subclass was never even getting called.

Soroush Khanlou
Exactly. And so it would give us these weird errors where we were trying to diff two arrays or something and it was just like garbage was coming out. We couldn't figure out what it was. So we dug into it and it turns out that basically, if you have a reference to the objects as NS objects, equal equal would do one thing. And if you had a reference to the objects as the actual type that they were, equal would do a totally different thing. And it was confusing. That is really what and how am I supposed to know that? It's not in the Swift book. It's not in any blog posts.

Chris Dzombak
Yeah, I don't know where it's documented what you're supposed to do for Swift to implement equality for NS Object.

Soroush Khanlou
Right. And so I wrote up a bug, I put it on bugs at Swift, and Jordan Rose responded like, hey, this is intended behavior. Like, this is how it works. And he's right, it is how it works. But it doesn't stop it from being any less confusing. And it doesn't help me because I don't know how it's like I don't know how it's supposed to know that it works that way.

Chris Dzombak
Yeah, that's such a just pit of complexity, especially for someone who are newer to that language that would just be mind bending.

Soroush Khanlou
I was working with someone who's newer language and they were having a tough time figuring out what's going on, and I ended up having to dig in and we teased the part what was going on. So when I say dynamic dispatch be the default, it's not that it's about dynamic dispatch. It's about a dispatch model that makes sense to people that use it. Okay. Without these pitfalls.

Chris Dzombak
Can I rephrase dynamic dispatch in what you're saying? That okay, let me try really hard here. Dispatch that I don't have to worry about, but that always seems to do the right thing.

Soroush Khanlou
Yeah, I don't like that definition because I worry that it's just like, oh, just do magically do the right thing. And it's like, well, in a lot.

Chris Dzombak
Of cases, that is kind of what Swift is aiming for, right?

Soroush Khanlou
That's true.

Chris Dzombak
I feel like that's a and they do a good job.

Soroush Khanlou
It adds a lot of complexity, but they do a pretty good job of having a pretty stained model for everything else.

Chris Dzombak
Yeah, generally speaking, they do.

Soroush Khanlou
Yeah. You can send quote unquote messages to Structs as though they were objects and it just kind of works. You don't have to think about it, but yeah, I don't know. It's a hairy problem and I just don't know how to fix it other than just like, give me a dispatch model that I can understand, and then you optimize away anything you think you can fully optimize away, like, 100% cleanly. Otherwise, please don't mess with the model that I have in my head of how this works.

Chris Dzombak
All right. I think that's fair. Yeah. So one of the favorite things that kept coming up over and over in the community was, how would we possibly model a responder chain like thing in Swift without objective C's like method forwarding? Fun times, funtime h. Funtime h. What were your thoughts on this discussion?

Soroush Khanlou
I think the instructive thing is not necessarily responder chains, but rather NS coding. With NS coding, you need a way to have a string of a class name, and you need the class itself, basically need a huge table of strings to classes. It so happens that that exists already by default in the objectives you runtime. So you get it for free. Doesn't exist in the Swift runtime. So they built it. They needed it. So they built it. Yeah. You're going to be able to do NS coding in pure Swift. It's like a weird function called underscore classroom name or something. So another way to think about it is a lot of the objective C 2.0 features came because they were needed. Like, the at dynamic keyword for properties came because they were needed in core data. Like, if the first party vendors need something, they're going to implement the thing that they need. I don't think we have any worry that a responder chain is not going to be possible.

Chris Dzombak
I feel like you could probably model a responder chain like thing in pure Swift, like, fairly straightforwardly.

Soroush Khanlou
I forget what the problem even is with the responder chain.

Chris Dzombak
Yeah, me too. Because I'm thinking about how you could implement a protocol with some default implementations and things would look pretty sane, I think.

Soroush Khanlou
Yeah. And you do need you might have.

Chris Dzombak
To add one thing to your class's.

Soroush Khanlou
Layout, which you need anyway, because every UI responder has to subclass from UI responder.

Chris Dzombak
So you have to have all those elements anyway. I think in a perfect world, it wouldn't be a subclass, right.

Soroush Khanlou
It would be a protocol.

Chris Dzombak
Yeah.

Soroush Khanlou
Which is I mean, that seems right to me, but I don't know. I don't know if it would be impossible. Like, again, dynamic dispatch comes into play. You can't static dispatch into a responder.

Chris Dzombak
Chain and implementation details. Long as I can call methods on things and they happen exactly fine.

Soroush Khanlou
Right. I've also never understood how to inject things into the responder chain. Like, I have things I would like to be able to respond to things in the responder chain.

Chris Dzombak
Yeah, it's a little somebody emailed me.

Soroush Khanlou
Tell me how to do that.

Chris Dzombak
Oh, man, I haven't done this in a little while. In an app, once I added something into the responder chain to pass events from table view cells up to a view controller. And that seemed like kind of a sane way to do this. It always seemed kind of weird to have a bunch of blocks floating around or have each cell have a reference back to back to some delegate.

Soroush Khanlou
Yeah, it's all built in anyway. Why don't you use that?

Chris Dzombak
Yeah, I really feel like something like the responder chain could be really powerful on iOS if it had a little bit more flexibility even. And if we actually used it.

Soroush Khanlou
Yeah, I think it'll be coordinator stuff. Simpler too, where the coordinator ideally would be in the responder chain as well. And as you get a touch message sent up, catch this touch message and send up a more domain friendly message of like, this thing happened with this data.

Chris Dzombak
That could be really cool.

Soroush Khanlou
Yeah.

Chris Dzombak
If I remember right, the thing that I did also, I had a category method on UI events, and there were some associated objects. As long as you're doing this, something insane go all the way.

Soroush Khanlou
Speaking of fun times, h.

Chris Dzombak
So what are our takeaways from today?

Soroush Khanlou
The point I was trying to make was that objective C is good at objective C things. Swift is good at Swift things. When you write code in the language, you should write like the language wants you to. But we didn't talk about any of that. We just talked about a lot more interesting things about metaprogramming and whatnot. I just want to be really clear that that was a lot of fun.

Chris Dzombak
But a lot of yeah, fun time. H. So takeaways are metaprogramming is useful and good. Yes, there are some things we can't do exactly right now in Swift. But actually a lot of the common things that we might have done with Metaprogramming and objective C are possible in Swift with maybe a little bit more boilerplate and with tools like sorcery I think a takeaway is that if Apple has promised to enable more sort of dynamic e kind of things in Swift. And they're probably going to implement them, because, as you noted, first party vendor, if they want first party vendor is going to first party vendor.

Soroush Khanlou
That's exactly right. They're going to first party vend.

Chris Dzombak
Vend. Yeah, that would be the verb. And I don't know, I still feel like a lot of the initial concern about losing dynamicism in Swift is maybe a little bit overblown.

Soroush Khanlou
A little bit. This podcast is like a year later. I know, but yeah, there are legitimately things that you cannot do in Swift, I think, even with Sorcery, that might not be right, but even with Sorcery, there totally are.

Chris Dzombak
Let's go back to method forwarding, like sharp edges that are like things that are hard to check and hard to maintain. And honestly, I'm fine with that.

Soroush Khanlou
Yeah, at the end of the day, it ends up being fine. And if there's something that's a real pain point, like, I think one of the things. One of the old objectives the diehards brought up was there was a time when every event had to be passed basically via an enum through one method. And then you had to do giant switch in this method to switch between your enum and the function of the behavior that you wanted it to do, which sounds horrible. That sounds terrible. And being able to send a message via a selector or whatever is just better. But as you can see, even since then, I think we got pound selector and pound key pass. Those are a little bit type safer. They enable the same behavior. I don't think we're going to go back to that dark world of everything being static dispatch. No, but yeah, all right.

Chris Dzombak
That's all I've got.

Soroush Khanlou
Yeah, that's all I've got. It's going to be fine, I guess, is the answer.

Chris Dzombak
Everything's going to be fine.

Soroush Khanlou
Everything's going to be fine. You heard it here first from Christmas.

Chris Dzombak
Thanks for listening, and we'll talk to you next week.

Soroush Khanlou
Later. Bye.

