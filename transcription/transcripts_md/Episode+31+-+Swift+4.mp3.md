Speaker A
So we've been off for a couple weeks.

Speaker B
That's true. We have. Right. About six weeks. I think this is scheduled to go up Monday, right? Yeah.

Speaker A
And we're back.

Speaker B
Yeah. So after six weeks, we're back. We've had I've had a pretty good start to my summer, sorous I hope you have as well.

Speaker A
I've had a crazy summer so far.

Speaker B
Yeah. Why? What's what's crazy about it?

Speaker A
Well, I feel like we're I don't want to bury the lead. There are several several interesting things have happened in these six weeks. Um, that's true. You have some news?

Speaker B
I do. We want to do my news. Okay. So I got a new job.

Speaker A
Cool. Congratulations. What are you working on?

Speaker B
Thank you. I'm working for a research group at the University of Michigan as a software developer working on their computer security and privacy related research projects. So this is notably not an iOS development job.

Speaker A
Despite the fact that it's not an iOS development job, I think there are going to be lots of super interesting topics that we're going to kind of come across as you discover all this new stuff in your new job.

Speaker B
I think so. I hope so. We've talked about a couple of episode ideas already, but we're hoping to continue talking about various software engineering, software development topics, which should remain broadly interesting. And as far as I know, you're continuing to write iOS code. So yes, we can keep talking about iOS.

Speaker A
Yes and no.

Speaker B
Oh, wow.

Speaker A
Yeah. So over the last six weeks, I was busy as well. I made an app. We kind of alluded to it in the last episode of season two where we talked about Swift on the server. So that app is now out.

Speaker B
That's right. And do you want to pitch this app quickly?

Speaker A
I would love to pitch this app. It's called beacon. We launched it for Dub Dub. We built it. Me and Ashley Nelson Hornstein built it in five weeks. And the idea is basically that you can post when you're available or if there's something that you want to do. And your friends will see that, and they'll be able to let you know that they want to go. So it kind of takes the pain out of texting and organizing and trying to figure out what you're up to. And we built the front end in Swift, and we built the back end in Swift. So, yes, I will be building iOS apps, but I will also be building other things as well.

Speaker B
That's awesome. I look forward to hearing more about your adventures in the server side Swift area too.

Speaker A
It's been very exciting, and I hope we have some cool server side Swift episodes coming up this season.

Speaker B
Hopefully. Yeah, I'm not doing any server side Swift. That's on you.

Speaker A
Yeah, it should be cool. Listeners, stay tuned.

Speaker B
So today, let's see. We were just talking about what we wanted to discuss on this episode, and it seemed like dub dub DC, and particularly changes in Swift Four were something that we could talk about.

Speaker A
Yeah, for sure. We took a six week break, basically, right at the eve of Apple's biggest developer thing, which is fine. It's cool.

Speaker B
Well, it was about halfway through our break.

Speaker A
Yeah. So there's like a ton of new stuff we could talk about there. That's like another big thing that happened over these six weeks that we were off. So we could start there if you want.

Speaker B
Sure, let's do it. I have read some about Swift Four, but not quite as much as I might have liked because of been for work related reasons, working on my Python and Go skills, which I definitely need to work on here. But one of the major changes is something that we talked about last season, which is that strings are now collections and work a lot more like you might expect. Right?

Speaker A
Yeah. It's an interesting set of changes because, like, you can just filter over a string now, and it will give you a set of characters, and you can decide if you want to keep it. And so you can end up with a thing on the other side. But because it's a collection, it doesn't necessarily behave how you might expect. Right. If you filter over a string, you might expect to get another string back, but you don't. You get an array of character objects.

Speaker B
Okay. And those characters are like Unicode graphene clusters, right?

Speaker A
They are, I believe that's right. They're Unicode.

Speaker B
Graphene Or I would hope that they are, because otherwise that seems like a sharp end.

Speaker A
So that's actually a new thing as well. They didn't used to be Unicode graphene clusters. It used to be that if you iterated over the family emoji of all four things, you would get four different if you iterated over their characters, you would get four or seven different things depending on if the zero joiner was included. But now it's true. Graphing clusters, which is actually solving, like, a big Unicode weirdness thing. And so you'll actually get one character of all four people in the family as one unit.

Speaker B
Awesome. And even, I mean, if you're working with a less complicated emoji, but you won't get, like, two broken characters that are each half of the emoji character that you're working with.

Speaker A
Yeah, exactly. And then the character counting also works more as expected. It's based on graphene just means for our listeners who don't do any linguistics or anything, just like one physical character of connected strokes that makes up sort of one character. So that's a graphium. And so it basically iterates over the graphenes rather than iterating over any set of bytes or any whatever else. They really papered over a lot of really interesting weird string issues in Swift Four.

Speaker B
What other issues have they papered over?

Speaker A
So there's one that I don't think and just for completeness's sake, we should say that if you have an array of these graphing clusters and you want to turn it back into a string, you can just pass it to the string initializer and it will just do the right thing and create a string out of that. So that's kind of how you get back to having a string. Okay, yeah, cool. Other weird things that they changed for strings, one weird one is now so you know how a string has many different views, right? It has its character view, Utf Eight view, Utf 16 view.

Speaker B
Right. Although character view has gone away. Right.

Speaker A
Character view is now just the string itself is the character view, which is great, but each of those views is basically like an Iterable collection and so they each had their own index in the past. So you'd have like string Utf eight index, string Utf 16 index. And so there is now a proposal for basically making the index of all of those collections be the same type. So you could take an index from the Utf Eight you could take an index from the Utf eight view and then just use it in the Utf 16 view and just get the right thing out of it.

Speaker B
What? How?

Speaker A
Voodoo magic.

Speaker B
But what if you have an index that is in between?

Speaker A
That's a great question. So I actually had the chance to kind of talk this out with one of the people who works on this stuff and he sort of talked me through the different options. So what are the different options? As far as you can imagine? Like, let's say you're in the Utf Eight view, you're split on a graphene and then you go to this default graphene view and you try to get something at that index. What could happen?

Speaker B
So you might return a broken or nonsensical character that's half of the graphene cluster. Right?

Speaker A
Right.

Speaker B
You could somehow detect that, although I'm not totally sure how you would detect that elegantly. And you either walk backward or forward to the next or the previous complete graphene cluster start.

Speaker A
And there's one more option, which is just like the joke answer, fatal Error. Also the title of the podcast. Yeah, exactly. So you could just trap and just explode, which is probably not the best thing to do, but it is an.

Speaker B
Option that seems like the wrong option. Yeah.

Speaker A
And then you can't quite return optional with the way things are structured at this point. But maybe in a theoretical world, if things were structured differently, you could return optional.

Speaker B
Yeah, but then you're going to end up having so many. Well, I guess string processing already has a lot of optionals.

Speaker A
Yeah, it's not pretty, but I think the answer that they're going to go with is basically walk backwards. Like, let's say you're splitting. Right. So like a flag emoji is basically two characters for the country codes. So the US flag is a U and an S. If you split that and your index is in between the U and the S, it will walk back to the U and it will give you the whole flag that's I think the thing they're going to go.

Speaker B
With, which that makes sense. But how do you detect in the general case, I mean, what if you land on a person who's in the middle of one of the complicated family emojis?

Speaker A
I don't think it would be an o of one operation for sure, but basically you would walk through and walk backward, right? Well, yeah. So you'd walk through and then if you go past the one that you were expecting because they have to be comparable, then you sort of take one step back and that's the character you return.

Speaker B
I see how that's the behavior people expect. That also has some just computational complexity complications.

Speaker A
Yeah. And that's the thing with strings, is they're not array.

Speaker B
It's really surprising how this stuff is just so much more complicated than anyone would think.

Speaker A
Yeah.

Speaker B
So, okay, that's about ten minutes about strings. What else is swift for?

Speaker A
Yeah, so Swift, for another really fun one that is very useful is multiline strings string literals. I should say so.

Speaker B
I saw this you can now have multiline string literals by using three double quotes to open and end the literal.

Speaker A
Exactly.

Speaker B
Okay. That's definitely useful.

Speaker A
Yeah. So one interesting thing with this that I thought was kind of notable is if you're inside that string literal block, you can use quotation marks freely without having to escape them, which is really nice.

Speaker B
Yeah, absolutely. Can you still do string interpolation in multiline literals?

Speaker A
That's a good question.

Speaker B
I would expect that you could.

Speaker A
I would hope that you could.

Speaker B
It would seem very out of line with Swift philosophy if you couldn't.

Speaker A
So one really interesting kind of edgy thing not edgy, but one component of this that I would not have expected to have to think about is your code is indented. Right. And that means that your multiline string literal is also going to be indented. So how do you know which of those indentations to strip out and which of them are important for the actual string itself?

Speaker B
Don't most programming languages that do this sort of thing just strip out all of the white space and assume it's fine?

Speaker A
I don't know the answer to that, but it's an actual question because that is a decision that you have to make and I never had considered that before.

Speaker B
Absolutely.

Speaker A
Yeah. So that's an interesting thing. What they end up doing is they figure out how far indented the first line is and they kind of subtract that indentation from every other line or something like that. Which is like kind of weird, but makes sense.

Speaker B
That's something where you have to kind of think about exactly what the result will be.

Speaker A
Yeah, exactly.

Speaker B
Although I guess you have to have some way to put white space in there. But we already have escape characters for things like tabs.

Speaker A
Right? Well, imagine if you're trying to generate like a Python program or something and that white space is actually important or Haskell program and the new lines have to be preserved. That's another thing. It's an interesting problem. I would not have expected it to be as complicated as it is, let's put it that way.

Speaker B
Yeah. Maybe I'm wrong about what most other languages do, I guess. I don't actually know.

Speaker A
They have to do something smart here.

Speaker B
I guess you would have to, yeah. It looks like you can do string interpolation inside multiline literals, which is good. Various languages have different behavior depending on what sort of string literal you're using, right. Whether they're single quotes or double quotes. And that's just so much like annoying complexity. Right?

Speaker A
There's languages that support both single quotes and double quotes and that determines what you can do on the inside of the string in terms of what you have to escape and what you don't.

Speaker B
Exactly.

Speaker A
I hate JavaScript so much.

Speaker B
Just subtweeting JavaScript really hard here.

Speaker A
I'm not even going to subtweet them, I'm going to fully call them out. JavaScript, your behavior is bad and you should feel bad.

Speaker B
So one of the other things in Swift Four that I was reading about is that there's some improvements to dictionaries and sets more collection improvements here. And I found the article that I was reading earlier about them. There's not a lot here that is, I think, really super, I don't know, super exciting, but it's definitely useful. You can make a dictionary from a sequence of key value pairs, right? So you want to merge two arrays into a dictionary. That's good.

Speaker A
All this stuff is like it's stuff that you could have written yourself, but the fact that it just wasn't in every project is just like so frustrating. So I think the canonical example of this is merging two dictionaries these values in this dictionary and those values in this dictionary, and I just want to put them in the same dictionary and maybe I want to define who overrides whom, however that works, but just please merge these two together. And it's just like having to copy and paste that between every project is so annoying. And this proposal resolves that. Filtering over dictionaries is another thing.

Speaker B
This default value syntax for getting items from dictionaries is going to remove like half of the no code lessons I ever wrote in Swift Three.

Speaker A
Absolutely. So that's another big one, is you can now in the subscript, provide your own default value. So let's say you're building something like a bag where you want to have items and the count of that item that you have. So you could say, like, for the default value return, zero, and then it will kind of handle that for you and you could just make a bag much more simply. Yeah. The proposal goes into a ton of detail about all the different things you might want to do and that this new set of functions and initializers and everything gives you. Being able to map and filter is really nice. Yeah, there's just a lot of good dictionary stuff and there's some really just like convenient things that you can do now. They have a new function called you init with some array and you group it by some key, like a function that takes the object in the array and then returns like a grouping key. Everybody's written that code before where you're just kind of sorting things into buckets, sort things by their first character. There's lots of little weird things you could do. There's a good article by Erica Sadun that I will put in the show notes called the Surprising Awesomeness of grouped Dictionaries. And so sort of cool. Yeah. Grouping things into sort of like different buckets of true and false sorting things by their first date. First character, first initial, like a name sorting by its first initial grouping people based on their city, let's say like people objects based on the city property. There's so much cool stuff you can do in it and this stuff will be really powerful. So I am looking forward to being able to use this as well.

Speaker B
Awesome.

Speaker A
Yeah. Some of this advanced stuff you may not be copying into your dictionaries into your own projects and then doing it manually and then you end up in a situation where you have messier code than you would ideally want just because you didn't want to make an extension for something or didn't think right. Yeah.

Speaker B
Another improvement. Another thing that we talked about last season. The file private is gone.

Speaker A
Yeah, file private is now gone. And Private is even weirder than it was before, I think.

Speaker B
Doesn't this just mean that private acts more or less like file private used to?

Speaker A
I may be wrong about this, but I think now private acts a little bit differently than it used to. And then file private does today.

Speaker B
Really?

Speaker A
Private. Yeah. So private now is private to the type private and it's like type and file private. So if you have the main body of the class up top and you have an extension in the same file, you can still access private things through that. But if you have some other object, it can't access a private member of that type unless it's within that type as an extension.

Speaker B
Okay, that totally makes sense. That's how I would expect private to work.

Speaker A
Not a bad solution to the problem.

Speaker B
I still feel kind of weird that we're still leaning on files as an abstraction for code organization, but I'll take it.

Speaker A
Yeah, pretty much. That's how I feel. And it's way also like I care about how this stuff looks and it just looks way less stupid than file private.

Speaker B
Yeah. And it looks like file private maybe actually is still around. But it allows crossing that type boundary then, is that right?

Speaker A
That might be right, yeah. Yes. It looks like that is the case.

Speaker B
Right.

Speaker A
Which is good. Nobody will be fine.

Speaker B
Yeah, clearly we're very prepared for this. Right. Okay. So file private now is the same and private means like private to within this type in this file. That's usually what you want, right? That's almost always what you want.

Speaker A
Yeah, pretty much.

Speaker B
All right, works for me. What else is new here?

Speaker A
I think yeah, there's some other stuff, one that they didn't talk about on stage partially because I kind of don't think that they're going to hit the target, but which, if they don't hit the target, I'll be very sad about, is conditional performances.

Speaker B
Oh, yeah.

Speaker A
It's supposed to come in swift four. It's approved. It's targeted for Swift Four. But is it going to make it? I don't know.

Speaker B
Was it one of the tasks that they were looking for someone from the community to help implement?

Speaker A
I would be very surprised because that seems like a real bag of hurt.

Speaker B
It really does. What were the proposals they were looking for help with, though?

Speaker A
I forget. I wouldn't know how to find that.

Speaker B
Yeah.

Speaker A
So let's do a crash course on what is conditional conformances.

Speaker B
Right. So to try to do this off the top of my head, this means you can write something like extension array to conform array to some protocol when that array contains a specific type, right?

Speaker A
Yes. Or when the array's types also conform to some protocol.

Speaker B
Okay, yeah. Wait. Yeah. Actually, the thing that I just said, I think you can do that somehow already in Swift Three, can't you?

Speaker A
Yes. But then you can't further conform that array to a protocol. You can say, I want to extend any arrays that only have people in them or person objects in them and go from there. But you can't say, I want to extend any array that has person objects in it to also be conformed to this protocol, conditionally conformed to this protocol.

Speaker B
Okay. Yeah.

Speaker A
So the canonical example of this is equatable. Right? Now array is not equatable because you don't know if the thing inside of it is equatable.

Speaker B
And this is the exact example I had in mind while I was trying to articulate what this meant is there's no way right now to express array is equatable when the things inside it are equatable.

Speaker A
Right. So they do all kinds of weird stuff like they will have a special overload for the equal equal operator that works with two arrays of T. And while that works and it makes life easy, it doesn't actually conform to equatable.

Speaker B
Right. And that's not something I mean, you can do that with equatable. There may be other cases where having a free function that works with these two generic types is way more clumsy than that right.

Speaker A
So arrays of optionals can't be equated with equilibrium operator. Arrays of arrays can't be anytime you nest this stuff, it just falls apart immediately because it can't build on Swift's internal structure of what equatable is.

Speaker B
So there's a proposal up for this.

Speaker A
So yes, there is a proposal. I have it in my history. It's let me.

Speaker B
Let'S throw that in the show notes because I'd definitely be interested to read this and maybe some of our listeners are too.

Speaker A
Yeah, and there's some interesting problems they bring up in the proposal, such as the kind of like diamond problem of like, okay, well, if you can get this function from this protocol conformance, or this protocol conformance, how do you know how to get it? So they talk about some of that stuff in here, but ultimately what this means is arrays of Equable will be equatable, arrays of JSON objects will be JSON objects, arrays of NS coding objects will be NS coding, stuff like that.

Speaker B
Yeah, that's cool. I'll definitely read over this after we finish recording.

Speaker A
Yeah, it's a pretty cool proposal. And it says status accepted. It doesn't say slated for Swift Four or whatever. This is going to really like, especially on the server, we do a lot of JSON stuff and this is going to make life so much easier.

Speaker B
Yeah, I can absolutely believe that.

Speaker A
Yeah. So I'm really looking forward to this specifically for JSON handling, which is a great segue into the next thing that Swift Four brings us. JSON handling.

Speaker B
That's right. So there are a couple different coding and archiving sort of improvements in Swift Four, right?

Speaker A
Yes.

Speaker B
And this stuff was coming out right when I was starting to switch. Really? Right when I was starting the process of switching jobs. So I'm really a little bit behind the times here. It's amazing how, I don't know, things change and I'm behind the times and I'm trying to get up, like, figure out what Idiomatic go is, learn the ins and outs of Python and starting.

Speaker A
A job and get going on new code bases.

Speaker B
Yeah. Which will be a future episode. Yeah, we're going to have to do that.

Speaker A
It's going to be fun.

Speaker B
Listeners, if you have tips for jumping into a new and unfamiliar code base, please send them and we'll cover those in this episode. And you'll help me out at my new job too. So JSON coding in Swift four.

Speaker A
JSON coding in Swift four. So basically NS coding in Swift Four got a major overhaul.

Speaker B
Right? I've read a little bit about this.

Speaker A
Yeah. So pretty much if you take a struct and you write colon for like conforms to and then you write codable, you're done.

Speaker B
Just magic happens under the hoods. It can be archived to data and unarchived done.

Speaker A
Just like that.

Speaker B
Beautiful. And that works with structs? Does that work with classes? Does it work with enum?

Speaker A
Yes, but typically when they give an example, they use Structs because you couldn't do that with Structs before because NS coding relied on NS object, which made it have to be an object.

Speaker B
Right. And the things that you're encoding and decoding probably should be usually data and not like, I don't know, not weirdly full blown classes.

Speaker A
Right, exactly. But of course if they're also codable, then it will like recursively, go down through the tree or whatever.

Speaker B
Sure.

Speaker A
Yeah. So there's a couple of interesting weird caveats here. So it sounds like you have a question first.

Speaker B
Oh, I was just going to say, does this lean on Swift, like on reflection in Swift, or does it lean on some other infrastructure that's been built into the language?

Speaker A
I believe it's more the latter than the former. Basically, if you conform to codeable, they will code gen a bunch of stuff for you under the hood that you will never see.

Speaker B
That makes sense.

Speaker A
Yeah. So they code gen a coding keys enum that sort of exists there and represents the keys of all the properties on that thing. You can then override that and then provide your own custom keys, which is a weird interesting kind of new Swift idiom that we really haven't had before. And then depending on how you want to encode the thing or decode the thing, you create something called an encoder. So you can create a JSON encoder or I believe you could do like a data encoder or some kind of other encoder, and that is the thing that will determine how it will be encoded. Currently you can only do JSON encoding, but later in the future there will be like ans coding encoder. Okay, yeah, that will work more like foundations, NS coding and like key archiver and stuff.

Speaker B
That's awesome. The code gen that you're describing sounds quite a lot like the code that we were either writing or code genning ourselves in Swift Three when we were dealing with JSON and dealing with storing data blobs in Yap database.

Speaker A
Yes, pretty much. And that's how we do use code gen in Urban Archive to make that work. And it works pretty well. I'm happy with it, but it'll be nice to have kind of first party support for this.

Speaker B
Awesome. Yeah, absolutely.

Speaker A
So the weird caveats here are if you want to do anything other than JSON encoding, you're kind of out of luck for now. If you want to have a custom strategy for encoding dates or encoding data, they give you some options for that. So you'll be able to say, well, my dates are in like ISO 6531 or whatever that ISO protocol is. Or you can say it's actually in seconds since the epoch or epic, however you say it milliseconds since the epic. Or you can say just use this custom date formatter which is also cool. And the interface for that is like an enum with an associated value of a date formatter, which is like a really nice Swift Idiom data has similar options. But if you want to do anything, like totally custom, like, let's say you get some data from the server and you want to turn into like a UI image, you have to completely re implement that init with coder method. And then for every property, write out a line of code of like, okay, decode this, decode this. And then when you get to the data one, decode this and turn into a UI image, it becomes much more kind of custom at that point. So you can't just override how one thing is parsed. You have to override the whole thing.

Speaker B
That's annoying. So the second you want to customize anything, you suddenly own all this stuff that you have to write and maintain.

Speaker A
Pretty much except for the specific keys. Like, if you do want to override just the keys, you can just choose the keys. But NetNet, it's better than what we had before. Oh, yeah, right.

Speaker B
Absolutely.

Speaker A
Maybe you'll have to do one, custom one, but the rest of them you'll get for free, which is like a little annoying, but not so bad. Yeah. Swift four crazy.

Speaker B
Absolutely. So one other thing. In Swift Four, there's some key value coding support in here now, finally, yeah.

Speaker A
This is a weird one, and it's.

Speaker B
Weird, but it's kind of neat. And like, this is implemented in a way that can be checked. And I think I like it. Although I never used key value coding that often in the Objective C days. Really? And I don't see myself using it very much in Swift either. Yeah, but maybe I'm just doing something wrong or doing something in a non idiomatic way.

Speaker A
Key value coding is a weird one. I've used it under the hood of things. So if you use interface builders, like user defined properties that will use key value coding under the hood, if you do like a JSON parser in Objective C, those are always key value coding under the hood.

Speaker B
Yeah, I guess that's true.

Speaker A
But this is like at compile time. Like, we know the key path to this property and then we're going to do something with that. One interesting thing is that there's no people were saying, well, maybe there should be like a map overload. So I want to map over an array and I want to pull out this property from this object. Why can't I do that? Why do I still have to create a closure? And so that's an interesting little tidbit about this thing. I don't think I'll use this very much. I think I'm with you. I can't see the value.

Speaker B
I can see there are cases when maybe you pass a closure to something that gets some value that you don't necessarily want to get right at the time. Although I guess you can still do that with a nice API with auto closure. So I don't know that this is. Really useful in that case, right?

Speaker A
Yeah, that's an interesting case.

Speaker B
Well, this is a thing that clearly people wanted, and I'm glad it's here.

Speaker A
So one cool thing that I have seen someone build with this, it's called Query, but with a K, so Kuery. And there's a GitHub project for it. It's by a gentleman named he helped organize Tri Swift, so I got to meet him in Japan. But the way that it works is you can kind of use these typesafe keypaths and these custom operators that he gives you to write a query for core data. And it's a typesafe query.

Speaker B
Interesting.

Speaker A
So you can say like slash person name equals Katsumi, which is his name, and person age is greater than 20, and it will convert that into an NS predicate and do all the stuff for you. But if you try to do person name is greater than 20, it won't compile, which is pretty wild.

Speaker B
Okay, that's pretty cool.

Speaker A
Yeah, it's really dope.

Speaker B
All right.

Speaker A
Yeah, that's cool.

Speaker B
I'll take it back. This is useful probably if you're writing, like you said, something that is using it under the hood to implement neat, almost metaprogramming features rather than something that you're going to write in day to day applications.

Speaker A
Yeah, for sure. He says at the bottom of his README, he says it currently relies on an unofficially available API to turn any given keypath into an NS predicate. And he has a Swift bug report to try to expose that so that we can build cool features with it, which would be really awesome.

Speaker B
Yeah, absolutely.

Speaker A
I can hear the excitement in your voice. It's cool.

Speaker B
Yeah, that's a cool idea. We don't use court data, but as we discussed last season but you could totally build something similar for pick your database system.

Speaker A
Yeah, for sure. And especially like on the server, I'd be really excited to use something like this.

Speaker B
There you go.

Speaker A
Yeah, there's a lot of cool stuff you could do.

Speaker B
So in a future episode, I really want to talk about your experiences building and launching beacon, especially during WDC. I have to imagine that was kind of a wild ride.

Speaker A
It was very hectic. It was fun, but it was super hectic.

Speaker B
Yeah. So unless you had anything else, I think that's most of the exciting stuff in Swift Four, although that's not even true. I mean refactoring.

Speaker A
Yeah, well, refactoring is like an Xcode component, but it's built in Swift and it's a whole thing. I'm so excited about it.

Speaker B
It leans on the Swift language infrastructure, though, the clang infrastructure.

Speaker A
Right. And there's just so much new, interesting, good tooling stuff that came out. I'm so excited about it.

Speaker B
That's really awesome. I was watching the keynote or the platform State of the Union and noted that the refactoring tools are available not just for Swift, but C, C and objective C. And one of the code bases I'm working on now is a C code base. Actually, a couple of them are C code bases, so maybe at some point I'll figure out how to get the Salt Building and Xcode and be able to use that as my IDE for at least the C code bases.

Speaker A
That'd be pretty awesome.

Speaker B
And use the refactoring tools. I don't know if there's much else to say about the refactoring tools besides, yay, they exist and they're way better than they ever were before.

Speaker A
Yeah, they're so good. We're using Xcode Nine in one of our projects and it's so good. It's like exactly how you want it to be. It's faster than it used to be. It's like all in line. Like, it's just beautiful. It's a nice thing.

Speaker B
That's really great. Anything else you were really excited about at WWDC? I think we should start wrapping up the pod. I think we're probably at around 30.

Speaker A
Minutes, but we're close that. So there was a lot of good tooling stuff that came out. Refactory is the biggest one. The other big one that I don't know if everyone caught was you can now debug wirelessly over WiFi.

Speaker B
Oh, yeah, I saw that.

Speaker A
So you can build from your computer and build onto your device over WiFi without ever plugging it in.

Speaker B
So I'm skeptical about how well this will work, honestly.

Speaker A
Yeah, it's one of those things where if they could deliver on it, then great, and if they can't, yeah, they tried.

Speaker B
So I realized, though, this is probably a killer feature, not necessarily for iPads and iPhones, but like Apple TV. Right. Thinking about my apartment, the Apple TV is in the other room, like 20ft from my computer here, and I'm not unplugging it from my home theater set up, quote unquote, home theater from my TV and speakers to drag it over to my TV and have to hook a monitor. Well, I guess you have the virtual monitor thing if it's plugged in, right? I think so, but I was thinking about that. That would make developing on actual Apple TV harder, way easier in my apartment.

Speaker A
That's a really good point. I didn't think about that.

Speaker B
And then wasn't there always some sort of wireless debugging or something supported for the watch?

Speaker A
I mean, there's no plug, so it has to be wireless, right? Yeah, I don't know.

Speaker B
So maybe they took this as an opportunity to make that faster and more reliable.

Speaker A
Yeah, something good there, but yeah, good. WWDC. A lot of promises. I want to see all those things be like fleshed out and see if they're all real, but very exciting stuff.

Speaker B
Yeah, I wasn't there, but I would say it was a good conference.

Speaker A
Yeah. So this is a kickoff for season three. Man.

Speaker B
Yeah, I guess. What do we want to say to our listeners? For those of you who are newer and maybe we didn't mention this, this is a weekly podcast. This is the first of what will be 20 episodes for season three. And half of those episodes, the even number episodes, will appear exclusively on our Patreon page and we'll have a link to that right in the show notes. And if you want to support us there, it's our Patreon supporters who make it possible for us to pay for the hosting and editing costs for the podcast.

Speaker A
Yes, I'm really excited about the season. I think we're going to have a lot of cool episodes.

Speaker B
I think so. I really hope so. We have a number of cool things planned. Thank you everyone for listening. Welcome back to season three and I hope you enjoy sweet.

Speaker A
I will talk to you next week.

Speaker B
Chris, I'll talk to you later. Bye.

