Soroush Khanlou
How do we start the show? Welcome to Fatal Error. Yeah.

Chris Dzombak
Yeah. Welcome to Fatal Error. I'm I'm Chris.

Soroush Khanlou
That's right. Welcome to Fatal Error.

Chris Dzombak
I'm Chris, and I'm Serous.

Soroush Khanlou
Perfect. Today we're gonna talk about Python. Chris has been writing a lot of code in a lot of weird languages, and we kind of, I think, wanted to compare Python to the other languages that we write on a day to day basis. And I want to know more about what chris's experience has been kind of picking up this new language.

Chris Dzombak
Yeah. So over the past several weeks at work, I've now written several thousand lines of Python for a little bit of context. This is in a web application, and it's written in Python 2.7 because Google app engine doesn't support Python Three, and we're using the pyramid web framework, and we can throw a link to all of this in the show notes.

Soroush Khanlou
Cool. I'll take care of that.

Chris Dzombak
And so now that I have a bit of Python experience under my belt, we thought that it may be interesting to go through my thoughts about writing Python so far, compare it maybe to Swift, which I'm obviously quite familiar with, and to objective C, which I'm also pretty familiar with. And see, I don't know, see what my thoughts and feelings are about Python so far.

Soroush Khanlou
Cool. So you mentioned Python 2.7 specifically. Why do you call that out?

Chris Dzombak
So several years ago now, python Three came out and, I mean, this isn't news by any any standard now, and Python Three broke backward compatibility with Python Two in a few important ways, most notably that Python Three has sort of built in Unicode support, whereas in Python Two you still like strings, and then you have Unicode type. And so doing proper Unicode support in Python Two is much harder than in Python Three. And porting code from Python Two to Three is not trivial because of in large part because of this string and Unicode change. And I really haven't written any Python Three, so I've I'm working entirely here with Python Two and can't talk too much about that. Those changes from two to three, since I haven't really worked with it at all.

Soroush Khanlou
Got you. So everything we're going to be talking about here is Python Two, which means it may not apply to some schools of Python, but it does still apply to a lot of people's code.

Chris Dzombak
Yeah. And I think that a lot of the stuff we're going to touch on is still relevant in Python Three, right? Yeah. Actually, before we touch on anything that I've noted specifically here, I just want to call out that for writing a big application, I really wish that I had a static type checker that ran on this code.

Soroush Khanlou
Chris, you don't need static types. You don't need anything but tests. Tests is the only programming tool that you'll ever need. And if you just use Test, it completely obviates every other tool that you can use for writing code. Sorry, but that's just how it is.

Chris Dzombak
I feel like we did we do an episode on that Uncle Bob post.

Soroush Khanlou
He did another Uncle Bob post. Okay, well, and it turns out not it turns out I mean, everybody's known this for a long time, but he has really bad opinions about women in tech as well. I saw some tweet that was like, if you can get past Uncle Bob's really bad opinions about women, you can get to his really bad opinions about programming.

Chris Dzombak
That's brutal but fair.

Soroush Khanlou
Yeah.

Chris Dzombak
Well, we'll link to our previous episode about Uncle Bob's take on and so it's important. Yes, tests are important, but not everything. Depending on whatever framework you're using, maybe not everything is going to be testable. And having a type checker just catches, like, stupid, trivial errors, like forgetting some parameter name or, like, I don't know, so many bugs that I've written in the last couple of weeks would have been prevented just at the outset by having a static type checker rather than waiting for something, be it a test or something else, to exercise this code path and then crashing at Runtime. I really wish that I had some more confidence in this code as I was writing it.

Soroush Khanlou
Yeah, that's the number one thing that I find about working in JavaScript or anything like that.

Chris Dzombak
I've also been writing JavaScript.

Soroush Khanlou
Oh, boy. Yeah, but that's the first thing I notice and I think that's the right thing to call out at the very top of the show. Now, I'm told that there are some what do they call, like progressive type systems or like incremental type systems for Python. Python, yeah. Do you know anything about those? Any experience or is that no, I'm.

Chris Dzombak
Aware of some of these for JavaScript, but no one has told me about anything in Python. I'd be very curious. Do you have any references?

Soroush Khanlou
I will put some stuff in the show notes. I don't know much about it other than I'm pretty sure it does exist.

Chris Dzombak
Interesting. So my next questions are is it compatible with Pyramid and is it compatible with Google app engine?

Soroush Khanlou
That I'm not sure. I have honestly no idea. Yeah, there's something called my pi optional static typing for Python.

Chris Dzombak
Speaking of optionals, I want optionals. I've had bugs because things are just because things are none, which is Python's equivalent of null, where at least it.

Soroush Khanlou
Only has one to be. Can we at least say that it's nice that there's not like undefined null and like six other forms for something.

Chris Dzombak
To be not set subtweeting JavaScript here.

Soroush Khanlou
Really? I mean, I openly tweeted JavaScript at JavaScript. The language is bad.

Chris Dzombak
No, that's definitely true. And one thing to call out that is kind of nice is that where you just have none in Python as your, like, null value or your null value. There are other things which are sensibly like which get, you know, which get coerced to a sensible boolean. So if you just write like if not some value, some value could be none, and then if not some value, that'll be true, some value could be an empty list, some value could be false. And I guess really what I'm getting at here is that an empty list is in boolean comparisons just interchangeable with none, which if you're in writing, sort of idiomatic Python style code works out fairly well.

Soroush Khanlou
Yeah, I think any empty value in Python is falsey. So empty sets, empty dictionaries empty strings, which I've gone on record. I think that's actually really nice. Yeah.

Chris Dzombak
You have a blog post about this, don't you?

Soroush Khanlou
What's it called? I do.

Chris Dzombak
We'll link it in the show.

Soroush Khanlou
Yeah, we'll find it for the show notes. But yeah, I think it's just called Falsiness or falsiness in Swift. We don't need to spend too much time on it. But basically most of the time when you want to check something about an array, you will just want to check if it's empty or not. That's the thing you want to know. And Python gives you that just out of the box, every empty value is just falsey and more or less works.

Chris Dzombak
Yeah. And you can still compare explicitly to none if you really want to do that, but that's often not what you want to do. That's what I kind of started out doing and then some of my coworkers in code review sort of like set me straight on this, just ask do a boolean comparison with the thing and it'll be fine. Something that you can't do with these values. This is something that I knew about and still wrote today and got corrected in a code review. You can't use something that's mutable as a default value for a parameter for a method. So just like in Swift, you can write in Python some method declaration and set default values for parameters so callers don't have to call your method with all of the arguments. And if you're just like using something like none or like an integer, then that's fine. These are immutable values, but that actually I forget exactly what the implementation detail that leads to this property is, but let's say you want that default parameter to be like an empty list. You can't do that or you shouldn't do that because it doesn't create a new empty list every time that function is called. That reference just lives throughout the entire lifetime of the program.

Soroush Khanlou
So it's a static reference to right?

Chris Dzombak
Exactly. So if you want to write a method that has an empty list as a default parameter and you do the trivial straightforward thing, which is just put an empty list there and then the function does something with the list and adds something to it, then the next time that function is called, that list will not be empty.

Soroush Khanlou
That's incredible.

Chris Dzombak
Yeah. And apparently this is still true even in Python Three. That seems bad.

Soroush Khanlou
Yeah, I don't like that.

Chris Dzombak
That's a language implementation detail leaking through, and I really don't like it. So the thing to do is you have to set your default parameter to none, and then in the function, check whether it's none and set it to an empty list at that point.

Soroush Khanlou
Wow. And because none is immutable, you never have to worry about mutating it.

Chris Dzombak
Right. So that's a neat Python thing.

Soroush Khanlou
I don't like that very much. That sounds really bad. I don't want to deal with yeah.

Chris Dzombak
I'm not really happy with that. Other Pythony things that are just pythony things that maybe aren't, are neither good nor bad. Coming from Swift, I kept writing a lot of code that used Map and Filter because, like, I want to apply this function to this or to this list of things that's map, I want to filter this list of things that's filter. And my coworkers are slowly breaking this habit and making me use list comprehensions in most case. In many cases.

Soroush Khanlou
So a list comprehension is basically a bit of syntax that lets you write.

Chris Dzombak
It'S basically like a for loop over.

Soroush Khanlou
Well, what's better than a for loop? Right? So you for for a Map, if you want to square all the numbers in a list, you would write x times x for x in my array, right?

Chris Dzombak
Exactly. Yeah. It's better than A for loop, but it's a declarative way to write that's still sort of imperative code.

Soroush Khanlou
Right, right. So it's idiomatic in Python to use this comprehensions over mapping and filtering. Is there any benefit, like, is it faster? Does it give you any extra abilities to use that syntax? Or is it just like, this is just how you write Python kind of.

Chris Dzombak
It'S just how you write Python lambda syntax in Python is not as nice as it is in Swift. So if you're trying to use Map and Filter with lambdas, it is a little bit less elegant. There are still some things that you can only do with Map and Filter. Right. If you literally just have a function that you want to map over a list of things, then using Map is still nicer.

Soroush Khanlou
Got you.

Chris Dzombak
And I forget the exact situation, but I have had one or two other cases where Map and Filter were the right solution. I think it was where I wanted to Map something and then filter it, whereas list comprehensions would like filter and then Map. And you could still do this with two different list comprehensions. Right. But that just seems right. So that's been something to get used to. We'll add some useful links on list comprehensions to the show notes. This is something that when I first came to this, I was like, this is some weird Python thing, and it's very advanced and I don't understand it. I'm scared of it. It turns out that it's fine, and if you can write a for loop, you'll fit right in. You can do this.

Soroush Khanlou
Yeah, it reminds me of just reordering the words in a for loop, basically.

Chris Dzombak
That's what it is.

Soroush Khanlou
Yeah. Like in Ruby, you can write like, do this thing if this case, instead of writing if this case, do this thing. And it seems kind of like that. Yeah, I think so. For a filter list copyright she, you write x for x in my array if x equals zero or whatever.

Chris Dzombak
Right. If X is even or something. Yeah, exactly. So in that way, it's kind of as like a filter and then a map if you want it to be.

Soroush Khanlou
Yeah. You can do a filter than a map, but it's harder to do a map and then a filter because of the way it's set up.

Chris Dzombak
Right. You can't really do them in that order, which is what I wanted in this case. And so I did get away with sneaking a map and a filter into the code base.

Soroush Khanlou
Nice. If you had better lambda syntax, what's your preference? Would you prefer to do it the Python way, or would you prefer to do it the swift way?

Chris Dzombak
I mean, my gut is that I would prefer to do it the swift way, but the the map synth the syntax for the map function is also like the list and the function are parameters to map, which takes a little getting used to and throws people who are reading the code off, especially if they're used to python. I don't know, if I were working on a Python code base with other people, I would use list comprehensions, because that's a thing to do in Python.

Soroush Khanlou
Fair enough.

Chris Dzombak
Yeah. If lambda syntax were nicer, then I would probably personally still prefer the map and filter primitives, but that's not Python, and so whatever, that's fine.

Soroush Khanlou
Right. And then my other question here is, are map and Filter built in?

Chris Dzombak
Yeah, they're built into the language. They're nice. First class.

Soroush Khanlou
Right. They're just built in the standard library. You can just use them.

Chris Dzombak
Yes. And functions are first class, so you can pass them around and just pass the name of a function as an argument to map and it'll work.

Soroush Khanlou
Right. That's nice.

Chris Dzombak
Oh, yeah, definitely.

Soroush Khanlou
Yeah. So you just write like array or list map, basically.

Chris Dzombak
Well, you don't. You write like, map and then the parameters of the list and the function that you want to apply to them.

Soroush Khanlou
Oh, it's a free function.

Chris Dzombak
Yeah.

Soroush Khanlou
Interesting. So it's more interesting. Okay.

Chris Dzombak
More like functional programming language style. But apparently you're not allowed to use it for some reason.

Soroush Khanlou
Does it work for other types of for lack of sequences and collections? Like, you map over a dictionary? Can you map over a string?

Chris Dzombak
I believe that you can map over anything. That's iterable. And maybe you can map over other things, but I'm not totally sure.

Soroush Khanlou
Right. Because you have, like, a range in Python, too. You could do range ten and it'll give you the numbers one through ten. Can you map over that?

Chris Dzombak
I assume so, because I assume that's iterable I know that you can iterate over dictionary keys and values, so I assume you can map over that. I haven't tried it, but I don't see why that wouldn't work.

Soroush Khanlou
Nice.

Chris Dzombak
Yeah.

Soroush Khanlou
Cool.

Chris Dzombak
So that's nice.

Soroush Khanlou
That is pretty good.

Chris Dzombak
What else do we have? Everything is passed by reference, and that is just something to keep in mind. I don't think I have too much else to say about that. There's no pass by value, which is a little bit disappointing.

Soroush Khanlou
That's just how the world is, I guess numbers just aren't mutable, right?

Chris Dzombak
Yeah.

Soroush Khanlou
I don't think there's any language that makes numbers mutable. Even Ruby. Where everything's mutable? I don't think you can really mutate a number, is there? Every operation that you do to a number returns a new number.

Chris Dzombak
That's probably how it should be.

Soroush Khanlou
Yeah, I mean, I think so, too, but with Ruby, there's no telling.

Chris Dzombak
That's true.

Soroush Khanlou
So you're basically very spoiled by Swift's structant enum system.

Chris Dzombak
Yeah, I really like swift.

Soroush Khanlou
Yeah, it's a good language. It's really nice. Is there any way to mark something as immutable? Like, say, okay, I have this list I want to make it not ever changeable, like in the way you would call copy on an Nsutable array.

Chris Dzombak
No, objective, I don't think there's any way to do that.

Soroush Khanlou
Yeah, it's always mutable all the time.

Chris Dzombak
Yeah. I'm realizing that if I'm wrong about any of this stuff, we're going to get so much I would love to get some email, so much feedback.

Soroush Khanlou
Email me, Chris@designback.com.

Chris Dzombak
Yeah, exactly. Yeah. Yeah. Email Chris.

Soroush Khanlou
Yeah.

Chris Dzombak
Let's see. I'm so I want to scroll through some other pull requests here and just note things that are, like people have pointed out to me that are gotchas. There's a lot of references to Pep Eight, which is just a formatting document because I haven't been formatting my Python exactly right. At some point, I should actually read through Pep Eight and memorize it, but I haven't done that yet.

Soroush Khanlou
So I have a question about the PEPs. Yeah, I'm a big fan of Pep 20. Do you know Pep 20?

Chris Dzombak
I don't. Let me Google this right now.

Soroush Khanlou
Check it out. It's called The Zen of Python, and it lays out a bunch of rules. It might be 20 rules. Yeah, the rules are some stuff like beautiful is better than ugly, explicit is better than implicit. Simple is better than complex, complex is better than complicated. Flat is better than nested, sparse is better than dense, readability counts and so on. I mean, I could people are driving in their cars. They don't have time to pull over and read these rules. So these rules are really good, and I actually think they apply to more languages than just Python. I really like them, and I refer to them when I can. Basically, when I need to fall on a certain side of one of these rules, I lean on this document. It's called Pep 20. There's also Pep Eight, which looks like this is for how to style your.

Chris Dzombak
Code, how to format your code, basically.

Soroush Khanlou
Right. Where to put new lines, where to put spaces, all that kind of stuff.

Chris Dzombak
Yeah.

Soroush Khanlou
Frustrated.

Chris Dzombak
It's just like, I don't know, starting anything new and having people be like, oh, no, this is the style for this. Okay, fine.

Soroush Khanlou
Yeah. As long as it's consistent.

Chris Dzombak
Right, right. And I mean, yeah, it's consistent, and it's fine. It's just, like, stuff to memorize. Right?

Soroush Khanlou
Yeah. So what are the other PEPs like? Are they just one through 20?

Chris Dzombak
No, there are hundreds, hundreds of PEPs. You can look at Pep Zero, which is the index of Python enhancement proposals.

Soroush Khanlou
Python enhancement proposal?

Chris Dzombak
PEPs. I think this is analogous, somewhat analogous to Swift Evolution proposals.

Soroush Khanlou
Interesting.

Chris Dzombak
I don't actually know that much about how the Python project is managed, but I'm pretty sure this is I don't know that these are, like, manifestos or evolution proposals or whatever you want to call them.

Soroush Khanlou
Interesting.

Chris Dzombak
Yeah.

Soroush Khanlou
And I guess these are, like, official documents that they're willing to kind of.

Chris Dzombak
Commit to, and some of them aren't really like, some of them are make the print statement into a function, like things that just happened once, and some are more like reference documents, more like RFCs.

Soroush Khanlou
Right.

Chris Dzombak
I guess I don't know that much about the process behind PEPs, but they exist, and I refer to them at times to learn about how to format.

Soroush Khanlou
It's good to have a knowledge base of how to do stuff, how stuff changed. It seems really nice.

Chris Dzombak
Yeah, definitely.

Soroush Khanlou
Pep Zero. We'll have to throw that in the show notes, too.

Chris Dzombak
Absolutely. Along with Pep 20.

Soroush Khanlou
Pep 20 is a great Pep as far as PEPs go.

Chris Dzombak
Great Pep. Yeah.

Soroush Khanlou
I wonder if they would accept a Swift evolution proposal that just had stuff in it. Like, beautiful is better than ugly.

Chris Dzombak
You could try it.

Soroush Khanlou
Yeah, you could try it.

Chris Dzombak
You'd have to find someone to implement that.

Soroush Khanlou
Oh, man. Yeah. Okay, cool. So Pepe has been driving you crazy.

Chris Dzombak
I mean, not driving me crazy. It's been a consistent presence in my life.

Soroush Khanlou
Is there any kind of background radiation of me writing Python? What's the tooling like? And I mean, specifically in this case, is there something like go format where every time you check something in, I could just format your code to map, to Pip Eight?

Chris Dzombak
I don't think so, but well, if.

Soroush Khanlou
You don't know of one that's I'm.

Chris Dzombak
Not aware of one.

Soroush Khanlou
Yeah, that kind of answers the question. Is there one that's popular in common, or is it just like Wild West?

Chris Dzombak
Yeah, none that I'm aware of, but I'm sure that several people have written tools that do that.

Soroush Khanlou
Got you interesting.

Chris Dzombak
Okay, let's see. What else did I want to talk about? Metaprogramming is a thing in Python.

Soroush Khanlou
Metaprogramming.

Chris Dzombak
Yeah. And there's not a lot of this in the project. There's some extend an object with functions from another file, which kind of like we do in Swift with extensions. So that's fine.

Soroush Khanlou
Kind of like a module in like a mix in.

Chris Dzombak
Exactly. Yeah. If you just have a string that is like I want to get this attribute of a function of a class, then you can do that. And those are maybe the only real metaprogramming things that I've done so far. There's another tool where the tool relies on just like iterating subclasses of one of its base classes, but that tool is kind of hacky. Nice open source though.

Soroush Khanlou
That absolves all sins as far as I'm concerned.

Chris Dzombak
But yeah, so I don't know that much about metaprogramming in Python. Just want to call out that that's a thing.

Soroush Khanlou
Yeah, the little Python I've written, there's some handles into the metaprogramming stuff with the underscore underscore functions which are also underscore underscore, init, underscore, underscore, and that's like the init function. But you can also use that to access which function you're currently in.

Chris Dzombak
Yeah, there's some magic things like that. And underscore underscore is kind of overloaded too, as I understand. If you just create a function or method or instance variable class variable that starts with underscore underscore, I think that that is not accessible outside the module at all and that the runtime does some name, mangling, to keep that thing private.

Soroush Khanlou
That's kind of cool. I do like that.

Chris Dzombak
I mean, it's cool but also okay, so you have some level of access control, but it is like based on the name of this thing, starting with a magic two underscores.

Soroush Khanlou
Right.

Chris Dzombak
That doesn't seem nice to me.

Soroush Khanlou
I guess it is better when it's built into the language and you could say like, this is internal or this is private.

Chris Dzombak
Yeah, well, I mean, it's built into the language, but it's like I don't know, it may be simple, but it certainly isn't beautiful.

Soroush Khanlou
Right. There you go.

Chris Dzombak
Little pep 20 joke.

Soroush Khanlou
One of the things that I said in the talk that I'm currently giving called you deserve nice things is like a lot of times with code we just end up making an alias for something in our head. And that's insane because we could just make the alias in the code because we control a code. And so if underscore underscore is like a talisman, that means private. Why can't we just put the word private there?

Chris Dzombak
Yeah.

Soroush Khanlou
So put the aliases in the code people don't put them in your head.

Chris Dzombak
So that's a good thing to know about if you're writing Python, but also kind of unfortunate. Let's see what else? So flipping over to some recent code reviews, I wanted to just literally scroll through and see what else python will let you do some weird things. There's one case where I had named a function argument Filter, and as previously discussed, filter is a built in free function. I forgot that somehow when I was writing this method, and so just within this method, it worked and it was fine. I think what happened was, within the scope of this method, I had replaced the filter function or overloaded that name with my argument, and it just wouldn't have been possible to use the filter free function, which seems like a weird thing for a runtime to let you do without any warning or error.

Soroush Khanlou
Yeah, I feel like I should definitely at least tell you that that happened.

Chris Dzombak
Yeah. But it didn't, and so that was weird.

Soroush Khanlou
Yeah. The problem with that is there are some cases I mean, Swift has this problem, too, where there are some cases where you intentionally do want to shadow something, but with Swift, you not have access to it.

Chris Dzombak
Well, with Swift, if you want to do that with a name that's built in, you have the you you can put backticks around it. And if you want to do it with a variable, you can you can shadow names. But I don't think you can just shadow the names of free functions in Swift without at least telling the compiler that you're intending to do it.

Soroush Khanlou
You can shadow free functions because you can still access them with, like, Swift free function name and it doesn't warn you.

Chris Dzombak
Whoa, okay, I didn't know that. Wait, okay.

Soroush Khanlou
Yeah, because you can shadow what's a really common example? You can shadow Error right, the type name, and then you could do Swift Error to access the protocol.

Chris Dzombak
Oh, yeah, I guess that's true. How does that interact with module boundaries in Swift? Man, I'm behind on my Swift these days.

Soroush Khanlou
How does it interact with module boundaries?

Chris Dzombak
Okay, so if you were within the Swift standard library module, I assume that you couldn't shadow the Error type. I assume that in Swift, you can only shadow types from other modules.

Soroush Khanlou
If what you believe yeah. That that'll give you an error. If you try to have two types in the same module with the same name, that will give you an error. Okay, so if you had a protocol named Error and then you had a struct named Error, that will give you a compile time error.

Chris Dzombak
Okay.

Soroush Khanlou
But across module boundaries, it's fine. And then sort of similarly, free functions work the same way. They're just sort of references in the global namespace. What's an example of a free function in Swift Min? If you override Min and you want to access the Swift version, you could type like Swift Min and that will give you the Swift version of it, but you can't override the same free function. Well, you can overload the same free function in the same module, but you can't override it.

Chris Dzombak
That's interesting. Is Min actually a free function?

Soroush Khanlou
Min is a free function, yeah.

Chris Dzombak
Okay, interesting. I did not actually know that about Swift. That's good to know. Thank you.

Soroush Khanlou
Yeah, you're very welcome. I have one sort of unrelated question, which is let's hear it. Do you have any intention or plan of pitching that some of these web tools are written in server side Swift?

Chris Dzombak
That's a good question. Probably not, because this tool is pretty tied into Google app engine. It uses Google BigTable, I think. Yeah, BigTable for data storage of a whole lot of data. And it's generally fairly tied to the Google ecosystem. And I don't think Google supports Swift.

Soroush Khanlou
Right. That sounds right to me. Yeah, seems fair. But any, what about other tools?

Chris Dzombak
I mean, other tools? I haven't run into a case where we're starting a new tool. If we were starting something new and depending on exactly what it was, I definitely would try to pitch it being written in Swift. My experience thus far has been that I don't really like writing really big projects in Python. I like writing them in Swift. I like writing them in, I don't know, other statically type checked languages. Small go. Yeah. Smaller projects, like a couple of scripts that work together that do something useful. Python is fine. Swift may be overkill, depending on the tool. I think the biggest thing, though, is that I wouldn't recommend right now that we try to rewrite any of these things in Swift. And I'm not starting any new tools right now.

Soroush Khanlou
Right, that makes sense.

Chris Dzombak
This whole site would be a big thing to rewrite in Swift and everyone else on the team. Everyone else who works on the site would have to learn Swift, and we'd have to figure out what our tool chain there'd be a lot to put in place.

Soroush Khanlou
Yeah, for sure. And you'd have to teach them optionals. There'd be a lot to teach. Well, I think optionals are not easy.

Chris Dzombak
I think that everyone who's working on this code base is familiar with an option type or maybe type that's good and in fact, complains about its absence in Go and in Python. But, yeah, Go really should have every language should have a result type and an option type.

Soroush Khanlou
I still can't believe the bad choices they made with Go.

Chris Dzombak
Well, yeah, it's C, but with C, but slightly better.

Soroush Khanlou
Very slightly. One of the things I was saying.

Chris Dzombak
Give it some credit. I mean, it's not I wish it has any number of problems, but it does take away a lot of the problems that C had.

Soroush Khanlou
Yeah, it does. So one of the things I was saying to Jason, who's been on the show before, friend of the show hi, Jason, is that there have been several attempts to fix C and make it good, starting all the way back to C plus plus with I think Java has the same problem, where it fixed. Some of the stuff about C but didn't fix other things like the primitive object distinction and then Go, and then I think now finally, Swift. And I think with each crack at the problem, we do a little bit better at fixing it, but it's very lipstick on a pig at the end of the day.

Chris Dzombak
So I'm a little bit hesitant to put Swift and Java and even C plus plus in a way in the quote unquote fixing C, because even C plus plus and C are trying to solve different problems. I do think that things get better with every iterate. I think Swift and C sharp are better than Java and C plus plus. I think that Go is better than C. I think that Rust is better than C and C plus plus and Java, but I don't know if I quite buy a like you don't see.

Soroush Khanlou
A through line there.

Chris Dzombak
I think it's more branchy.

Soroush Khanlou
Yeah, maybe it is a little branchy.

Chris Dzombak
Think of it as a directed acyclic graph.

Soroush Khanlou
Well, I don't want to correct your joke too much, but which of the nodes point? I guess there's no cycles. Yeah. Okay, I'm I'm down. Down for this show. Joke approved.

Chris Dzombak
Yay.

Soroush Khanlou
With that. You want to wrap the show up?

Chris Dzombak
Sure. I hope this has been interesting to make excuses, Chris.

Soroush Khanlou
This is a good show.

Chris Dzombak
I hope so. I hope so. I just thought it may be interesting to go over some of the stuff that I've been noticing as I work with different languages than what I've been doing for the last several years. It's been a learning experience for me, and there are things that I like and things that I don't like about Python and about various other languages and yeah. Please tell me what I got wrong, because I have not been writing Python professionally for very long.

Soroush Khanlou
Yeah, no, I mean, I think to understand our language well, we need to understand the other languages that it exists in the universe with.

Chris Dzombak
Yeah.

Soroush Khanlou
And without that, like, we don't know how things would be better. We don't know how things would be worse. We just kind of have blinders on. In the same way that I think it's good to learn other spoken or written languages, it's also good to learn other programming languages.

Chris Dzombak
Absolutely.

Soroush Khanlou
So getting this context, I think is really cool.

Chris Dzombak
Yeah. And just well, since I feel like I just delivered a bunch of caveats and gotchas about Python, I mean, Swift isn't totally without this sort of thing you have to know about optionals. And while I think that's a good thing, that is something that may be surprising for someone coming to Swift. I recently had to explain to someone at object C directive in Swift, which is like, Swift is great until you get to the objective C interrupt parts, and then you're like, well.

Soroush Khanlou
Let me.

Chris Dzombak
Tell you about next step.

Soroush Khanlou
Yeah. There are even non objective C, interrupt parts that are just like, well, this is a really unfortunate accident of history that we could just never fix.

Chris Dzombak
Right? Yeah. Swift isn't perfect. Python isn't perfect. Computers, shake your fist.

Soroush Khanlou
Thanks.

Chris Dzombak
Yeah. Old man yells at computers with that.

Soroush Khanlou
Chris, it was a pleasure.

Chris Dzombak
This has been fun, as always. Thank you for chatting, Sirush. We want to give a shout out to our Patreon supporters who get an extra episode or who get every episode that we publish. They get the even numbered episodes and they make the show possible. And thank you very much them for their support. We'll link to Patreon in the show notes. This is the last episode, or the last episode that will be not on Patreon of this season. Are we on season three, sirous?

Soroush Khanlou
We are on season three. This is the last public episode of.

Chris Dzombak
Season three, so we're going to take a break for five or six weeks and be back probably with a new format. We'll see.

Soroush Khanlou
Yeah, at the start of the year, we might get a new format and Patreon people, you get one more episode, so get excited for that. It's going to be a fun one. It will be, yeah, it's going to be worth it. But then, yeah, five, six weeks off and then we're back in the new year with season four.

Chris Dzombak
Season four.

Soroush Khanlou
Season four. Are we committing publicly to season four here, Chris?

Chris Dzombak
I'm committing publicly to at least trying, like we said at the very beginning, we or I reserve the right to stop doing this if it becomes too stressful or too much if there's too much on my plate. On our plates. Seems reasonable, but it's a best effort. Podcast.

Soroush Khanlou
Cool. Talk to you next week, Chris.

Chris Dzombak
Bye, sir.

