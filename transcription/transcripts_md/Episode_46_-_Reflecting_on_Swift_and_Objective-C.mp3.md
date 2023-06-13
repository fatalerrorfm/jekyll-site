Speaker A
Alright. A I still don't know what a run loop is. B let's start the show.

Speaker B
I don't have a great idea what a run loop is either, but I feel like it's I mean, if you're starting, like, a program that's gonna have, you know, have multiple threads and actually be doing things, then you're you start off basically with some sort of loop that, like, handles inputs and sort of distributes them to threads. Right. I really understand how that plays along with GCD queues.

Speaker A
That's the thing, because it's obviously just a big while loop. Right. But then how does the while loop know to DQ blocks off the main thread and only let them execute until it's time to refresh the screen and then do that stuff? And how does it know?

Speaker B
Well, I think maybe there's the idea of the main queue and the main run loop is these days largely like DQing things from the main queue and running them and it doesn't know to stop when it's time to redraw the screen because your blocks on the main queue can block redrawing the screen. Right.

Speaker A
Do you think it's just constantly pulling blocks off the main queue and everything is going through that?

Speaker B
Partially. And it also does things like if you are doing things with reachability or the network, you register handlers in the main run loop. And I think that the run loop knows how to deal with other sorts of ways to manage concurrent sort of execution right. Or manage different threads, manage different events. In some ways it's almost like Node has like a loop that it's constantly going through and events come in. And I think that a run loop in an iOS app is kind of analogous to that in some ways. Right.

Speaker A
But the thing is like a node that's all obstructed away from you.

Speaker B
Yeah, definitely. And it mostly is in iOS too. Right, right.

Speaker A
But then there's times when you have to change the scroll update, like a scroll view update parameter. It's like, hey, where on the run loop should I update this? Do you know what I'm talking about?

Speaker B
Yeah. And I know that there are network things that play with the run loop and I'm a little bit fuzzy on how this all works under the hood because I feel like a lot of it actually does tie in with GCD. Like somehow GCD interoperates with some of the lower level stuff that yeah.

Speaker A
It's got to be really important.

Speaker B
Yeah. That GCD.

Speaker A
I would wager that GCD is pretty important.

Speaker B
Yeah. Not in Swift six or seven. Yeah. So welcome to Fatal Error. I'm Chris.

Speaker A
And I'm, sirous.

Speaker B
Today we thought we would talk a little bit about reflecting on Swift through the lens of maybe writing a new objective C app, which you may recall that Sirous did somewhat recently. Before we start that, I want to give a shout out, of course, to all of you, our supporters on Patreon, you are making it possible for us to do the show without advertising. You're paying for editing and production costs and we really do appreciate it, for sure.

Speaker A
And not only are you paying for editing and production costs, you are also paying for Chris and his new microphone.

Speaker B
That he's recording on that's right, I have a new microphone. It's an audio technica ATR 2500, I think. And so far I think it sounds pretty good.

Speaker A
Yeah, I'm very happy with the microphones that we got. We got matching mics now. Great.

Speaker B
Adorable.

Speaker A
Cool. Yeah. I just want to echo what Chris said. We say this all the time, but we really love you, Patreon. People, you make this podcast possible in the most serious of ways. I don't know if I have the energy to do ads and chase that down every week and I think I would just feel bad doing it. And so I really like that you all like what we do enough to just directly support us and make it so that we can make this podcast without having to worry about how we're going to pay for editing and how we're going to pay for sounding good and stuff like that.

Speaker B
Absolutely.

Speaker A
Thank you so much.

Speaker B
So on that note, Sarush, you recently worked on a new app that was written in Objective C for various reasons, and we had one or two episodes about this where I think we focused on the fact that you were rewriting your promises library in Objective C so that you could use it in this app. Right?

Speaker A
That's right. And that has been working out pretty well. I've been pretty happy with the way that the promise library is shaken out. I don't like the lack of type safety, I don't like how many brackets there are, but there's nothing to be done about those two things.

Speaker B
You mean you don't like lack of type safety and the prevalence of brackets in the promises library?

Speaker A
Specifically the way that you have to write it in Objective C and the.

Speaker B
Number of brackets that show up in chaining method.

Speaker A
So if you chain like four or five, thens together you're going to end up with a bunch of brackets on the front end.

Speaker B
Yeah, that's super. Not ideal. Lack of type safety. You mean sort of lack of generics, basically. Right? Everything's in ID.

Speaker A
Yeah, and it's even worse than that because sometimes there are generics, but you can't say, okay, so the promise actually can be marked as generic. It's a very light touch of a really hint.

Speaker B
Yeah, lightweight generics only applied to collection types.

Speaker A
No, you can use them if your own types. The problem is that you can't describe anything more interesting than that. So the then method in some cases will map a promise of type T to a promise of type U, but you can't describe that in the type signature of the thing.

Speaker B
Right. The lightweight generics pretty much attach a single type as an annotation.

Speaker A
Right, exactly. And you can't do anything more advanced than that. So if you, let's say, have a promise of type and a string, that you're kind of mapping the constants of into a promise of type UI image, and then you want to return a UI image, the type system. Doesn't know enough to make all that work, and so you just end up returning a regular promise with no generic specialization, and you just kind of throw that type information has just gone, gone with the wind.

Speaker B
That's unfortunate. So having actually used this promises library in an application, how much of a hindrance is that versus writing this in Swift? I mean, if we want to take sort of a maybe not critical, but really think about what Swift has given us versus objective C, how big of a pain is this for you?

Speaker A
I think this is one of the smaller things.

Speaker B
Oh, really?

Speaker A
Yeah, I think it's it's a little bit annoying, but for the most part, you don't have to think about it too much. It doesn't get in the way. Whereas other rough edges of objective C are like, I see them and I'm like, it does not have to be this difficult. I've seen a brighter future, and it could be better than this.

Speaker B
So let's dive into some of those rough edges. Maybe what has struck you?

Speaker A
It's like things that I see. Like, I see, okay, there's a singleton, which I think is actually maybe gone now. I think I finally factored it out. Searching for dispatch once. No, we still have an image cache, which is global.

Speaker B
Okay.

Speaker A
Stuff like the singleton, you got to make the dispatch token, and then you call it a dispatch once method with the dispatch token and blah, blah. And it's like, it doesn't have to be this complicated. Like, Swift lets you do this in one line, and it's kind of an anti pattern, but still, when you need it, you need it. And you want it to be simple when you want it. So it's like, obviously that's a small one, but it's like thing after thing after thing that's like that. So, like, when you're doing the dance between primitives and NS numbers, and you're.

Speaker B
Just like that's, right? Yeah.

Speaker A
And you're like, okay, well, some things can be int. Something's going to be NS integer, something can be NSU integer, and other things to be NS number. And which one do I really, really want to use here? And it's kind of annoying. It's kind of pain in the butt.

Speaker B
Yeah, I had pretty much blocked that out of my memory.

Speaker A
Yeah, it's bad. I have a couple of model classes here. It's really simple. I think it's like three nested models, but when I store those things as JSON or pull them out of JSON, I have to do the stance back and forth to the kind of wrapped NS number type and then back out to the regular value. And it's like well, if you want to mutate it or work with it, like, add two numbers together, you got to pull it out. And if you want to store it somewhere you got to put it back into the lower container. And that's kind of annoying.

Speaker B
I think it's worth calling out too. That that's annoying. It's maybe not hard, but it's annoying. It's tedious. And those sort of tedious things are error prone. Right. You're like repeatedly taking these values and doing things with them and then you have to repackage them in the correct NS number type. Well, I guess NS number, NS number.

Speaker A
Fuzzes, all that stuff for you.

Speaker B
Yeah. You have to pull them out of NS number is the correct type though, right?

Speaker A
Right.

Speaker B
Yeah.

Speaker A
And there's a little bit of checking it'll do for you, but not everything. And if you would sign the thing wrong, you'll get an integer that represents like a pointer value of the thing. That is not what you want.

Speaker B
No, very much not.

Speaker A
And then on top of that, so when you pull something out of the dictionary you get it as out as an ID type. Also you can't put Nil in into collections. Really annoying. So then you're putting an snull in there and then when you pull it out then you've got to kind of cast it. There's no as question mark cast in objective C, which I didn't really missed that much when I was only writing objective C. But now that I know I could do something like that, I ended up adding a method to NS object called as class or nil. And then I will pass it across and tell it what class I want it to be.

Speaker B
That's a neat thing to add. And I'll throw in we'll add a link to the show notes here to a couple of macros that I have for objective C which add similar things that aren't hanging on at a subject as well.

Speaker A
Yeah, wherever you decide to put that code, it's just actually pretty useful and it's kind of nice that Swift just has them built in. It's not like Swift doesn't have its rough edges. And then, okay, so I needed to map something and it's like, well, what am I going to do? Am I going to use key value coding which is stringly typed? Or you know how you can write like my array value for keypath and then you pass it a string of the property name and it will return to you an array of all of those child properties. You could do that. That would work. But it's stringly typed and it might not work. Might work, who knows? And then, so it's like, well, okay, I'll write a map function. The map function is also not going to be type safe. Really. It's a little better than being stringly types, but not by much because you don't know what type you're getting out. You should get IDs out. And it's like thing after thing after thing like that, and it just gets great. Yeah, it's really not, and it really makes you miss Swift.

Speaker B
So, so far, we know that generics are really useful. Having number types that are built into the language or standard library instead of being like, having a weird primitive versus reference type number dichotomy is a nice thing to have. We know that being able to do the as question mark thing is really nice. So a lot of good things about types having an actual type system to.

Speaker A
Work with in generics, having real optionals is great.

Speaker B
Yeah, that's true. Optionals makes.

Speaker A
It'S all of that stuff. Yes. But it's also like Objective C, and I've complained about this in other environments, too, I think, on this podcast. But Objective C, especially in its later years, didn't feel designed. It felt very much like a bunch of stuff was piled on and glommed on into this mutant aberration of a language. And the parts of it, the core of it was beautiful. I think the parts of it that work together and the parts of it that were designed in those very early days was really nice. So the way that nil works in Objective C just works beautifully with the rest of the language. If you get Nil out of, let's say, a dictionary and you call int value on it, you just get zero. And it's like, that is kind of implicit behavior, but it also just kind of does make some sense, and it all kind of just works together nicely. Yeah. Whereas once they started adding more and more of these features, things started to get weird, I think. And then I think it also started to get notably worse once Swift was really in full force. Like, starting from 2010 on, they didn't really do anything with the language. And so that was four or five years of just stagnancy for the language. And I think there are things they could have tightened up, and I think if Swift hadn't happened, like maybe Objective C 3.0 could have happened, and it could have sanded off some of these rough edges. But as it is, Objective C is like this mutant thing that this mutant workhorse that's carrying all this weight, and it's doing a good job, but it can be frustrating to work with on a lot of levels.

Speaker B
I totally get that. And I think you and I have had this conversation before. I'm not quite as down on the later years of Objective C as I think you are. I mean, it's true that there weren't that many big changes to the language over the last past 2010, but I mean, a certain amount of what you describe as like, stagnation for the programming language, you could also see as effectively stability. Right? And that's something that we don't have in Swift, and that is really kind of like, makes writing code in Swift a little bit more painful.

Speaker A
Yeah, that's definitely fair. And it's nice that I did open up a really old Objective C project, one from, like, five years ago today.

Speaker B
And it worked, actually just compiled. Right.

Speaker A
Everything was fine. It was really great.

Speaker B
Yeah, that works. My only other piece of feedback is that I understand what you're saying and where you're coming from, but also let's remember that Objective C is strictly a superset of C, and therefore some rough edges can't be sanded off. Right?

Speaker A
That's right.

Speaker B
I think it's important to keep that in mind, unfortunate though. It is.

Speaker A
Yeah. And I mean, I basically think that's some of the worst parts of Objective C I don't want to get too off topic, but when they said Objective C without the C, that sounded really appealing.

Speaker B
Yeah, as it turns out, a lot of the really sharp edges in Objective C are from the C part.

Speaker A
Right. And it's because of the C interop part. And if they could have made it such that you could say, okay, this is an Objective C class with no C interop right. Then you could get rid of a lot of things that would be really nice.

Speaker B
Yeah, absolutely.

Speaker A
Kind of to go back to the fact of Objective C kind of not making much sense in its later years, that starkly contrasts with the way that Swift does make sense and does work together. And for all the consternation on Swift's evolution or whatever, I think that the Swift team is really good about making a language that kind of is cohesive. And to your point about Swift is in flux, to my eyes, that's like a trade off. Basically, you can either have something that is immutable and it's basically an ad only design spec where you can only add stuff to it, or you can have something that's designed to work well with itself.

Speaker B
Yeah, absolutely. Swift is. I mean, Swift has been and is and should remain, like, through the evolution process, like internally consistent and very considered and very designed. And I think that's generally a good thing. Although it will be nice seven years from now when the language is stable and you can open a Swift project that's a couple of years old and just compile it.

Speaker A
Yeah, definitely.

Speaker B
But I think just the price that we pay for that is a few years of source instability here in the early days.

Speaker A
Yeah, that's basically right.

Speaker B
Kind of unfortunate, but it is what it is.

Speaker A
Yeah. It's like a trade off that you get to decide if you want the language that's fast to work with, stable, reliable, but doesn't necessarily have that consistency. Objective C exists, and that is a choice that you can make today. But if you want the cohesion, if you want the consistency, if you want the language that works well together and the language that feels designed, then the trade off of that is that it's going to be changing over time.

Speaker B
Yeah.

Speaker A
And it's not even a theoretical I wish they could just make Swift not change anymore. It's like, if you want that, that is Objective C, and that is the trade off that you would have to make. And everybody I work with, almost all of them have been like, all right, well, we'll pay the price of working with Swift rather than paying the price of working with Objective C. Yeah. One really interesting thing I want to point to that's, like the kind of like the Objective C way to do stuff versus the Swift way to do stuff. It's like a really technical, specific thing. But I do want to bring it up because I think it's interesting. Everything that we would use list comprehensions for in Swift. Not everything, but a lot of the things you can implement with key value coding. And it's really terse and actually kind of nice. Okay, so two examples I want to point out. I have a situation here where I have a set of form groups, and each form group has a bunch of form elements in it. Those form elements each have an expected height, kind of like an intrinsic content height. And then those form elements form a form group, which then also adds up all of its constituent expected heights to make its own expected height and so on. And you have a bunch of form groups, and that's the thing that you're after. And so with key value coding, so in Swift away, you would write this. You would say, I have my form groups. So self dot form groups map into my expected heights and then reduce into zero with the plus operator. And that would like, sum all the expected heights together. It would first map to the expected heights and then sum them all together. Does that make sense?

Speaker B
I think so, yeah.

Speaker A
Right. So you have this object, you have an array of objects that has an expected height, map to the expected height and then sum those together with the produce. That works great in Swift, but that is really tough to do in Objective C because deuce is weird. You would have to transfer this ID object around for your accumulator. So you're constantly wrapping and unwrapping your NS number. It's really weird. But the key value coding for this is it's a string, which kind of sucks, but also gives you this really trist expression you just do at sum expected height. And that does all of it. It does the summing automatically, and it does the mapping to the expected height automatically, and it just works. It's wild. And there's no way to test it without running it. When you get your types right in Swift, when it compiles, you're pretty sure you got it right. But here there's no compiling. So it could just be wrong and crash at Runtime, but when you do get it right, it's extremely terse, which is really nice. Yeah, so that was a cool one. And then the other cool one was I have a situation where I have a bunch of photo sections, and each of those photo sections have arrays.

Speaker B
Okay?

Speaker A
So I basically want to make one big array of all the photos. So in Swift I would do a flat map. So I would say like self dot photosections, flatmap dollar sign, zero photos, and that would make a big array of all my photos. Right. In Objective C you can do value for keypath and again, stringly typed, no type safety really bad, but it's just at unionovarrays photos and that's it nice. Yeah, it's pretty cool. So it does the map and the flattened for you in this pretty tourist thing. And I played around with like, I have a version of the block based map in this project because it's really useful. Should I write block based flat map? I was like, well, it's actually kind of complicated and the type safety makes this pretty tough and I'm really not going to be happy with the result no matter what. So why don't I just use the tools in Objective, like let Objective C be Objective C, right, and use this native Objective C feature and then end up with actually like a very terse expression that gets me exactly what I want.

Speaker B
That's pretty good. Yeah, I guess that's something to keep in mind, is that these problems are not totally new to Swift. We did have some tools for solving some of these things in Objective C.

Speaker A
As flawed as they were.

Speaker B
Right. Flawed though they might have been. Like, there are tools for a lot of these and in some cases they actually work out quite nicely.

Speaker A
Yeah. And actually, now that I think about it, I bet when you do at Union of arrays, it doesn't actually create a giant array. It probably creates an NS array subclass class cluster that knows where to go to find the original photo. So it actually still stores an array of rays under the hood, but depending on what index you ask for, it will go to the right subarray and the right element within that subarray as an added optimization. In the same way that if you call joined in Swift, you'll get a join sequence and that preserves laziness and it does these extra things so you never have to think about it. And I bet under the hood this is doing the same thing. And I bet if I called dot class on this, I would figure out that, hey, this is not actually just a bare NS array.

Speaker B
There's actually NS union array or something.

Speaker A
Something like that. Yeah, totally.

Speaker B
That totally makes sense. I do wonder how feasible that is, given that any of those NSRA subclasses that you hand in might also be mutable. But I guess if you were careful with the implementation of the Union array type, that wouldn't be an issue.

Speaker A
It would have to copy each subarray. But the thing is that if it's already immutable, then copy just returns self. It doesn't need to actually make a copy. So it would have that optimization built in.

Speaker B
It wouldn't necessarily even have to copy. Right. It would just at the time that you are asking for an out, like it wouldn't have to cache information like the length of either the summaries or of the subarrays, but if any of.

Speaker A
Them are mutable, then those would be able to change from underneath it. And there's no like I don't think there's any kind of is uniquely referenced type thing in objective C.

Speaker B
Yeah.

Speaker A
And calling copy like does exactly what you want if it's already immutable, does nothing, and if it is mutable.

Speaker B
That's true. Yeah, I guess that's exactly that makes sense.

Speaker A
Yeah.

Speaker B
I still think that the mutable subclass thing is such a horrible.

Speaker A
Yeah, it was a nice hack.

Speaker B
Not good.

Speaker A
It's a nice hack.

Speaker B
It wasn't even a nice hack.

Speaker A
It was a bad hack.

Speaker B
It's a bad hack because the immutable subclass of some immutable class, like immutability is a property that the class provides that providing that immutable subclass breaks it takes away that property. And there are cases where you can use an Immutable type that you cannot use a mutable type.

Speaker A
Right. And so that has to be baked into whoever's using the potentially immutable type to call copy. It's on them to call copy.

Speaker B
Right. And that violates the which principle is that list golf substitution principle. And that's not good. That's using object oriented programming poorly.

Speaker A
Yeah, I think I agree with that. One answer I have for this is you can either bake that in in the implementation of whatever is like in the writing of the code. Right. So you know that if you're going to be writing something like this NS Union array thing, then you're going to need to know to copy all the subarrays. Or you can bake it into the language itself and it's like in some sense, again, trade offs, whatever, but there is a cost of baking it into the language itself and it's like, well, we talked about it makes the language more complicated, more keywords, more things to know about. But at some point that knowledge does have to be baked in somewhere, right?

Speaker B
Yeah. And I mean, there are problems with doing it in the way that objective C has done it.

Speaker A
Yeah. You got to know to call copy.

Speaker B
And you have to defensively co copy almost anywhere. You use an array for many common tasks.

Speaker A
Yeah, that's fair. And it doesn't create a deep copy, which is in some cases even work like core data relies on you not being able to copy the thing.

Speaker B
Well, that's not a problem. Unique to what? Objective C, right? If you caught copy an array of reference types. In Swift, that's not a deep copy either.

Speaker A
Yeah, that's fair. But I feel like if you have reference type, you're really explicitly saying, hey, if you create a new references, I expect them to be the same pointer in the same instance.

Speaker B
So this brings us to a question like, what have you have you run into any cases in this Objective C application where you want value types but don't have them because everything is a reference type?

Speaker A
Yes, that photo section, I definitely want it to be a value type. I have a concept of metadata, and every photo has metadata. And then when I change any property on the metadata, I want that metadata to turn into JSON and save itself to wherever it needs to save itself, usually disk, sometimes network. And if that were a value type, I could abuse the Didset thing where if you change any property on a value type, it will call the did set on its owner. And when you call did set, then I could do one behavior there and say, hey, if the metadata changes at all, I want you to save this, or execute some code, basically. Okay, so that's a really good example of when I would want a struct. There was something else, too, that happened recently where I was like, this is 100% a struct. There's one situation where I want enums. I want really rich enums. I have this concept of a gallery, right, for the photo sections. And then I have these gallery modes, and then some of them allow multi select, some of them allow single select, some of them allow normal tapping behavior. And so depending on the state of how everything's displayed, changes in the view controller, the state of the tab bar, buttons that are enabled changes, the ones that are invisible changes. And if I could bake that all into the enum and I started with two cases. I started with zero cases, obviously. Then I went to two, and then I'm now at four. And each time, anywhere it's used, I have to remember. Okay, I got to go check there to see if I have to add an extra case to my if statement. If it's this case or this case or this case, and it's like, if that was all baked into the type, it would be so much better.

Speaker B
Yeah, I forgot to ask about this until now, but, like, Swift enums are so much better than they're so good than C enums. I've been writing quite a lot of Python over the last couple of weeks, and there have been several cases where I want even a basic enum would be good, but having Swift style enums would be incredible. But instead, I just have a class with some constants defined on it, and this is just how we do things.

Speaker A
That's right. So in Objective C, when I have to do stuff like. That I do like doing the template method pattern, where you have one abstract superclass and then for your enum type and then you have subclasses for each of the enum cases and then any associated data goes in those subclasses.

Speaker B
Yeah, but that's so it is heavyweight.

Speaker A
And it's really hard to maintain, but it works.

Speaker B
Yeah, that's true. That's true.

Speaker A
One other situation like enums that we haven't talked about yet is protocols with default implementations. And this is a feature that we use in Swift and I think we almost take for granted, but those do not exist in objective C. And so the issue here is that I have this concept of a report. And the report can either be a draft, it can be in its kind of upload state, or it can be in its finalized report state, which is immutable. But in any of these reports, they always will have an array of images. And so sometimes I want to be able to generate a string that represents like, hey, there's four images in this thing. And there's a couple of ways to do that, right? One way is to put it at the call site so the view controller would have that code in it and say, well, hey, I know there's an array here, I'm going to grab the array and make that code. I don't love that. One option is to duplicate everything and put it everywhere. Obviously that's not great because if it ever changes, which it has changed, or if it was localized, all that stuff, you'd have to change in multiple places. And then what we would do in Swift is we would do each one of these report states would be like they would conform to a protocol and the protocol would have this computed property on it that would figure out how to build this string for you. And then there's other ones too. So there's like date formatting, there's date interval formatting, there's a bunch of stuff. So what I ended up doing was basically, and I actually did not know what to call it, so I called it a view model. And it's actually the first thing I've ever made that I've called a view model, which is really funny, but it's basically a report view model. And we will call it a decorator, I think in objective C, where basically it takes one of these report objects, whether it's a draft or an upload or a finalized report, and it wraps it, and then it gives you all this extra behavior and it gives you access to all the properties that are built in to that report. So it will give you access to the array of photos, but it will also give you access to the photo count string. So that was basically like I would have loved to do protocols with associated or sorry, protocols with default implementations, but because you can't, I had to do this wrapping thing where I have to reimplement everything I want to have access to.

Speaker B
Did you consider any kind of crazy metaprogramming runtime trickery?

Speaker A
I did a little bit, but I don't feel confident enough in my metaprogramming. Maybe I would have two years ago, but right now it just seemed like more work and that much benefit. It's like ten properties I just wrote. I forwarded all those methods over to them.

Speaker B
I think you're probably right. I'm just curious if you really wanted to do something like something like this in Objective C, that would be the way to do it, right?

Speaker A
Right. Very dry, very don't repeat yourself.

Speaker B
Yeah, might not. I mean, yeah, runtime H is maybe not the best thing to import. Right.

Speaker A
But I wonder if I do import it anywhere. It was imported. The person that I adopted this project from was using associated types to associate a model object to a cell.

Speaker B
Which.

Speaker A
I did not like. Especially because the cell was just a subclass.

Speaker B
That right. We own properties to a subclass.

Speaker A
Yeah.

Speaker B
I was not one to shy away from using associated objects and rejective C, but that is not the right time to use one.

Speaker A
Yeah. So now I think there's no reference to runtime H, so I think that's aces.

Speaker B
There was one time where I forget the details, but there was a table view involved in propagating different events from cells. And I think yeah, I had involved the responder chain and associated objects on UI event somehow.

Speaker A
Yeah, you could do some crazy shit.

Speaker B
I always thought this. Yes, you can. I always thought that the responder chain was like an interesting concept that is just basically not used in objective in iOS, the same way that I feel like it is in OS Ten.

Speaker A
I think that's right.

Speaker B
And that maybe it's useful and iOS should have used it in some ways.

Speaker A
This is a patreon, so I can tell secrets on this.

Speaker B
I don't think that's how it works, but sure.

Speaker A
I have a blog post idea for basically what if all of your coordinators were view controller subclasses? And I'm definitely not the first person to suggest this. I want to give a shout out to Dave DeLong who's been pushing this idea. But if that were the case, then you could actually pass events up to your coordinators via the responder chain. And so I want to play with that. So look out for that post sometime in 2019.

Speaker B
I think that's really interesting. I mean, the responder chain seems like a way to pass events up in the application through like a relatively clear I'm not going to say perfectly clear because there is some weird complexity there, but through a fairly clear conceptual chain. And maybe it could be useful in iOS too, since iOS apps are not trivial.

Speaker A
Right. Part of what makes it tough is I don't think that you can't inject your own objects into responder chain as far as I can tell. Which is a little bit annoying.

Speaker B
I thought there was some really hacky way to do that, but you're right. There's no good way to do it, right. Yeah, there's something you can do if you really want to do that, but it's not ideal.

Speaker A
I feel like it's a Linked list, and you should just be able to say, like, the element that I'm interested in now points to me, and then I'm going to point into the element, that element's parent or whatever, and it should just work. But it doesn't work that way, I don't think.

Speaker B
Why do you think in I mean, we're coming up on eleven years of writing iOS apps, if not in the public. Apple's been doing it. Why do you think the responder chain is so minimized on iOS versus OS Ten?

Speaker A
I think it's a single window thing. Yeah. I think in the Mac, you had several technologies. We use one responder chain, two bindings. Again, this is one of the situations where they kind of built something that really worked nicely with itself, and then when it came to iOS, just, like, didn't make any sense.

Speaker B
Maybe even more than the responder chain bindings would be useful in iOS. Like, writing code that binds your UI to your data model is the most boring part of it's. Just mind blowing.

Speaker A
But it's extremely important in Mac programming because you're going to have two windows that point to the same entity or resource, and you just never have that in iOS. It just never happens.

Speaker B
Yeah, I guess that's true.

Speaker A
Maybe a weird case in an iPad app.

Speaker B
Or if you have an external display, doesn't that come up as an extra window? Or can't you do but yeah, you're right.

Speaker A
But I can count the number of apps I know of that use an external window in a good way. On one hand.

Speaker B
I can't even think of one offhand.

Speaker A
I think Spanx status Board keynote.

Speaker B
Yeah. Isn't status board no longer a thing?

Speaker A
That might be right. R-I-P status board. Pour out some whiskey.

Speaker B
I'm out of whiskey. I'll get some after we finish recording.

Speaker A
But yeah, those are some of my thoughts about what it's like to write objective C and what I miss about Swift. I think it's funny, too, because I was such a hardcore anti Swift. I wrote this big blog post how I would never write swift.

Speaker B
Oh, I kind of remember this.

Speaker A
Yeah. And now I'm just full circle, please. I would love to write some Swift some more.

Speaker B
Oh, how the tables have turned.

Speaker A
That's right. Yeah. I don't know. I'll put that post in the show. I think it's called, like, why I Don't write Swift. Yeah. And then Six Months later that's such.

Speaker B
A serous blog post title.

Speaker A
It really is. And it did not age well. And I have another post where I was like, it's called Reflections on Six Months of Swift and I was like.

Speaker B
Man, this wasn't even like it was a year that long ago.

Speaker A
Oh, it was two years ago.

Speaker B
Oh, is it? Oh, wow. Yeah, you're right. Wow. Okay, never mind.

Speaker A
So, like, basically a year later, I wrote another post that was like, all right, I was wrong about Swift. Well, I was like I was right about Swift in that it has these problems, but I was wrong about Swift in that it's fucking fun to write true really nice to write in true stories. Yeah. But yeah, I miss Swift. I'm lucky that I get to write Swift for most of the stuff that I do. Swift project is the only objective C thing I work on.

Speaker B
I'm not writing really Swift or objective C right now, but it's okay. I'm learning other languages. It's fun.

Speaker A
Yeah, we're going to have to talk more about that soon. Some rust python.

Speaker B
We should. I've done at this point. A good amount of python. A bit of go, really. Not any rust so far to speak of, so we'll have to wait longer on that. But we'll get there.

Speaker A
Get it together. Chris. Come on. We got a podcast to record. You can't just be not writing rust at your day job. This is ridiculous.

Speaker B
I'm doing my best.

Speaker A
All right, Chris, it was great talk to you.

Speaker B
Yeah, you too. I'll talk to you next week. As always, thank you so much for listening. And thanks for your support.

