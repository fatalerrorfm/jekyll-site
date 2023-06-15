Chris Dzombak
It.

Soroush Khanlou
Hello friends. Welcome to Fatal Error season two. The first season of Fatal Error was a bit of an experiment. Chris and I didn't know if we had enough thoughts to make a really viable podcast. We didn't know if we would be interesting enough and if people would like the stuff that we had to talk about. But we got a ton of good feedback over the course of the last season and we're excited and happy to be back.

Chris Dzombak
Yeah, absolutely. Like I said at the end of, I think, episode ten, we're really thankful that all of you have been listening, have started listening and really have given us such positive feedback. And welcome to season two, episode eleven. I'm Krista Zomback by the way.

Soroush Khanlou
And I'm Sirush Kamlo. In the spirit of this podcast being kind of experimental and since we're paying for the editing costs and the hosting costs out of pocket right now, we wanted to try a somewhat different method for generating money to pay for these editing costs and these hosting costs for the show. So we have a patreon. You could find the Patreon in the show notes. It'll be $5 a month and for those $5 you get two extra episodes every month. So if you've been listening to it on an every other week basis, you will still be able to listen to it on an every other week basis. But we're adding an episode in between every one of our old episodes and that'll be only for Patreon patrons.

Chris Dzombak
Right? So another way to think about is just that we're now producing an episode every week for this season and every other one of those episodes will only appear on Patreon.

Soroush Khanlou
Yeah. So if you like our show, if you want to help support us, we would love it if you would go to Patreon and chip in and make sure that we can keep doing this stuff. We have a bunch of cool ideas for what we want to do with the show and where we want to take the show. And the more money we have, the more time we have to dedicate to it and the more cool stuff we can do. So I think it's going to be really exciting to see some of the stuff that we can do. So if you like our show, we would love it if you become a patron and we hope that you enjoy the in between our episodes as well.

Chris Dzombak
Yeah, thanks in advance for those of you who are, who are considering doing that. So for today's topic, I think Sirush and I figured we'd talk about Code Generation in Swift, particularly a few projects which are out there, one of which is really new, one of which has been around for a little while. But Sirish, do you want to maybe talk about why you want to cover this topic today?

Soroush Khanlou
Yeah, for sure. So we've actually had Code gen in our list of topics to talk about for a while. There is a project called Source Kitten which talks to the Apple provided source kit and it will basically parse all of your Swift code that you pass it and it will figure out what's a class, what's a method, all that stuff, and provide that data to you. Xcode internally uses that to parse how it should syntax highlight stuff, how it should figure out what documentation to show when you option click something, where to jump you to when you command click on something, all that kind of stuff. And so we had a little thing in our episode list that was just like it just said Sourcekittencode Gen. And the original place that I wanted to take this was for dealing with our model layer. We've been working with something called Mode Generator for many years, which if you've never used, is basically from your Xcode core data model plist file. It will generate a bunch of classes that have all of the managed object subclasses that you need to work with core data. And that was always really cool and always really useful because when you added something to your model file, you'd need to go back and add it to each of of things and you have to it manually. And you wouldn't be sure exactly if you've done it right and if you forgot it, you wouldn't be able to access it, but it would be there. It would be a whole mess. So I was thinking about that and I was thinking, well, it'd be really great, let's say, to do this kind of thing for JSON. So JSON, we have this current problem in Swift where it was much easier in objective C because you could just kind of read out the properties that a class had. You could say, well, it has a string named that has the name name and it has an int that's like the age and you could kind of iterate over those and process those and do whatever you needed to pull things out of a dictionary, assign them with key value coding, you could do all this stuff. But now with Swift, since we don't have those powers, I thought that code gen might be a way to kind of fill in some of those gaps I found myself. I think we talked in the Single Responsibility Principle episode about I have a struct that represents each model type, and then it has an NS coding conformant NS object for encodable. And then you could maybe have one for JSON that's bound by all that's bound by a protocol. And that is really tough if you want to keep that up to date manually. But if you have code gen that just says, hey, let me look at a list of properties on a structure or protocol and just generate the bevy of classes that you'll need, that would be pretty awesome. And so this has kind of been in the back of my mind for a while now, but haven't had any chance to work on it. And friend of the show, Christoph Ziplocky, made something called Sorcery a few weeks ago. So, Chris, you work with Christophe, right?

Chris Dzombak
Yeah, he's been working with us.

Soroush Khanlou
Can you share a little bit about what Sorcery is and what it does?

Chris Dzombak
Sure. So, sorcery reading right from the GitHub repository here brings metaprogramming to Swift. So really what it does is looks at your source code like using Source Kitten. I believe it's using Source Kitten under the hood.

Soroush Khanlou
Yeah, it is for sure.

Chris Dzombak
Don't know how else it would work. And then you can write templates to what was that?

Soroush Khanlou
I was just going to say you could use a lot of nasty regexes to get in there.

Chris Dzombak
Yeah, would not be pretty. So then it takes the sort of syntax tree that you have access to through Source Kitten and lets you use that plus templates that you provide to generate Swift code and that obviously lets you save time and also reduces the potential for mistakes. Like with core data models you mentioned, there was always the possibility that if you're manually writing those classes, you could forget something or have a tight mismatch versus the actual core data model. So this sort of automation reduces room for potential mistakes. Some of the immediate applications that I think Christophe had in mind with this tool, Christoph, by the way, is not quite the right way to pronounce his name, but I'll embarrass myself if I try to pronounce it any other way.

Soroush Khanlou
We should have Christoph email into the show with a voice snippet of him saying his name so that we can play it on the air, because I've always wondered exactly how to say his name.

Chris Dzombak
We can ask him about that. Yeah. So things that I think he envisioned as an immediate application for this tool are things like writing equality methods or functions for Swift types. Right. Particularly if you have an enumeration type, writing the double equal function is really just repetitive and tedious and frankly error prone. Right.

Soroush Khanlou
So if you have an enum and all of the cases have no associated properties, but one of them has an associated only one of them has an associated piece of data, then you have to implement equality yourself. You have to check every single case, and then for the one that has the associated thing, you have to unwrap it and then check that the internal contents are equal as well.

Chris Dzombak
Right.

Soroush Khanlou
And it's real pain in the butt. And every time you change the cases, you also have to go back and change the equality. And if you don't remember to do that, then your quality won't work. Right.

Chris Dzombak
Yeah. It's just hugely painful and clearly ripe for this kind of automated solution. Other things that you could use this for are automatically putting together a nice description method that goes over all the different properties and other things defined in the type and printing them out, you could implement that in an automated fashion.

Soroush Khanlou
Here one of the ones that he has in the README is if you want to know how many elements are in each enum. So there's another way to do this that's called case countable, and we can put that in the show notes. It's a little snippet. And what it does is, like, assuming that your enum is an int, it'll iterate from zero until and it'll try to create the enum from the raw value until it hits nil and then that many is the count. But that's like O of N. It's kind of a hacky way to get around the fact that there's no built in way to get to the count. And so there is a template for generating a static VAR called Count on each enum that will return the number of cases in that count or in that enum. It's like a super nice and if you ever change that enum, or if it's not, let's say, representable by an int, which the other way does require, it'll just do it for you and it just magically appears.

Chris Dzombak
Yeah, and that's something that we kind of worked around that in objective C and C by, you could have the last element enum be the special count enum. But that was such a huge hack and it's even less elegant and swift than it ever was in C for sure. So this is a really nice way to get around that. So you would run sorcery just as part of your build process at a build phase, fairly early in the Xcode build process, and then yeah, you have all this stuff just available for you to use.

Soroush Khanlou
Yeah. And you can make your own I don't know if it ships with any of the items ships with a couple of the templates, but you can make your own. So if you have like, NS coding, you could just generate that. And so for that encodable model thing that I had in that other project, it's just ripe for this kind of thing because right now we have to edit each of those manually every time there's any kind of change. So that part of it's really nice.

Chris Dzombak
Yeah, absolutely. If you ever find yourself writing this sort of repetitive code, particularly in a larger code base, this is something I would really recommend that you check out. It's super useful working with, say, swift value types, if your model layer is made of value types. Yeah, just all sorts of use cases that aren't even coming to mind right now.

Soroush Khanlou
Chris, did you ever write any code that relied on the objective, like runtime in terms of metaprogramming and stuff like that?

Chris Dzombak
Yeah, I absolutely have. I don't think I've shipped very much code that depends on that. But yeah, I've used runtime H. Yeah.

Soroush Khanlou
I've been known to use runtime H in my time, I've actually shipped it. It's stable, it's reliable, it works, but you really have to know what you're doing and if you make a mistake somewhere, you have to rely on catching that at runtime. So tests are really good to test all the weird little edge cases and all that stuff. But what's really nice about this is all this does is just generates more Swift. And that Swift is ultimately just compiled by the compiler. So if you write one of these templates and you forget a brace or you forget something somewhere, or you like, your logic is slightly wrong, you'll just be able to look at the code that's output from the tool and just say, oh, this is clearly wrong, I need one more space here and it'll look right. Whereas with the old metaprogramming style of things, you kind of had to think in your head, what code is this equivalent to? Whereas this literature shows you the code that it's equivalent to, and then that actually gets compiled by the compiler and what's wrong? We just won't compile, which is really cool.

Chris Dzombak
Right. And this also means that errors that you could have in Objective C metaprogramming, like type mismatch errors, the Swift compiler will catch that here, since we're just working in plain old Swift here.

Soroush Khanlou
Absolutely. Yeah. So, for example, one of the things I think I have a project that would be really ripe for this. I haven't had a chance to play with it yet, but we have maybe ten or so models. They all come from JSON. They all get NS coding compliance, the JSON stuff. If you read a property and like you said, with the type mismatch, you can make sure to guard everything that's not optional. You can make sure to cast everything. Like if it's expecting an int, you cast it to an int at the right time, and then if that cast fails, you can also fail at that point. And so you have such tightly grained control over, or fine grained control rather over the stuff that gets output. I think it's going to be a total boon.

Chris Dzombak
Yeah. I'd be really curious to hear if you use this tool. I'm really curious to hear how it works out.

Soroush Khanlou
So you work with Christophe. Are you all using this in your project yet?

Chris Dzombak
We are, yeah. It's clearly a very new open source project from him. I mean, he released this maybe two weeks ago, 15 days ago, and so we don't have it deployed too out our code base yet. However, we are using it for a few things, and we surely will be using it for more and more because it's something that we've run across time and time again, is writing this sort of repetitive, error prone code.

Soroush Khanlou
Right. So what do you use it for?

Chris Dzombak
So right now it looks like we have three templates in our project. Let me pull that up. Here one is we talked about any quality test for an enumeration with the associated values. And then the others are just printing out a nice, like a user friendly description of certain. Yeah, these are enumerations. So adding a user friendly I think this is mainly used for debugging description to a couple of other enumerations that we have got you based on the type name and case name.

Soroush Khanlou
Yeah, that stuff is super useful.

Chris Dzombak
Yeah, that seems so nice.

Soroush Khanlou
Definitely going to introduce it into some of our projects. I think another thing to think about with some of this stuff is I'm actually looking at the reading now. Another one that we didn't talk about is Diffibility. So right now, if you have like two structs that are not and you don't know how they're not equal exactly, like right now, you kind of just have to print them out and kind of look through it manually. But with something like this, you can just write a generated function called diff these two things and it'll say, hey, this first one has a name that matches the other one, but it has an age that doesn't match the other one. And it'll just print that out for you and say, like, for example, for testing. That kind of thing is super, super useful.

Chris Dzombak
In the future. Maybe if we do an Objective C versus Swift episode, which is another topic that's been on our list for ages, it may be cool to talk in a little bit more meta way about whether techniques like this come close to replacing the metaprogramming that we had in Objective C for common use cases in Swift.

Soroush Khanlou
Yeah, it's super interesting. I always thought of metaprogramming as code that writes code. I don't know how much have you written? Much Ruby and played around with like Rails is a lot of crazy metaprogramming stuff.

Chris Dzombak
Yeah, I have used ruby. I haven't used Rails very much before.

Soroush Khanlou
Rails has a lot of the same abilities as Objective C, often with a little bit nicer of an API for sort of like iterate for me, all the instance variables that are available in this object. Iterate every object that's available in the Runtimes like object space. Iterate all the methods on this class, add this method, add this class method. And I've always thought exactly that it's code that generates like byte code or code that generates things in the runtime table that are the same things as code would generate, but you're just like kind of skipping the middle person. And this is truly code that generates code. And I think adding that explicit step in the middle makes it so obvious what you're doing. And it's part of the reason I'm so bullish on, is bullish the one, the Sorcery project. So I'm really looking forward to getting a chance to integrate it into a project I'm working on.

Chris Dzombak
Cool. Maybe moving on from Sorcery onto other code gen or metaprogramming sort of topics. I added a link to the show notes to the Swift proto buff project, which works together with Google's protocol buffers, which are sort of a binary on the wire, a little bit better defined and a little bit more safe alternative to JSON. Is that something you've heard of before?

Soroush Khanlou
Yeah, definitely. It's something I've never had a chance to use, but I've always been curious to use. No one is adventurous enough to try it with me.

Chris Dzombak
Yeah, I've never used this before either, and I don't know that much about it, so I can't really talk very much about it. Beyond that, I know you end up with these proto files which describe, if not models, then at least how your data looks on the wire going between server and client. And this project will generate code to work with your proto definitions. And so this is sort of another thing that if you control the server and the client, or you can get someone to buy into using protocol buffers, this would definitely be another code gen tool to look into that really promises, I think promises to make things just a lot more safe and more convenient than using JSON. That's really all I can say about this project.

Soroush Khanlou
Protobuffs. The benefit is basically, you know, the type of everything coming down the wire. It's not like JSON where you just get a key and it could be anything, but it's very strict. It's just like this is an Int 32, or this is like another object that has this type, and that type is defined somewhere else in the proto file. And if you can share this proto file between your server and your client, they can both generate the code that will represent those models on the wire, and then you can be sure that they'll agree. So no more JSON mismatches, no more, oh, I thought I was getting a string here, but I'm actually getting an array of strings with only one element in it. And then you got to go talk to the person who's writing the server and everybody's upset. This just lets you agree on that stuff up front. And I didn't actually notice, I was looking in the proto buff, the Swift protobuff repo, and the code that generates the Swift is actually written in Swift, which I think is just great.

Chris Dzombak
Yeah. Is Sorcery written in Swift or is.

Soroush Khanlou
This a sorcery as well? Is written in swift. Yeah, but I thought it was nice because I know that the Swift compiler itself is written in C, but I thought it was nice that some of the side projects that the Swift team is making are actually written in Swift.

Chris Dzombak
Yeah, absolutely. Much of the Swift standard library is written in Swift too. Right, right. Just the compiler itself, that's C plus plus.

Soroush Khanlou
And it's actually very interesting that you bring up the Swift standard library because the Swift standard library also uses code generation.

Chris Dzombak
Oh, that's right. Yeah. I didn't even think about that, but that is true. So the Swift Standard Library uses a sort of custom tool, which was developed, as far as I know, just for Swift. GYB generate your boilerplate, I think is what it's called. And so if you look at the Swift, I forget which repository it is, we'll put a link in the show notes, but you can see these files that are used to generate a lot of this repetitive boilerplate code that appears in the Standard Library. And that is really cool to be able to sort of peek under peek under the hood and see how that works.

Soroush Khanlou
Yeah, it can be a little bit intimidating sometimes when you go into the Swift Standard Library repo and you're like, okay, well, this is where all the collections are. I see Random Access Collection. I see Mutable collection. I see Bi Directional Collection. But why is this file like a GYB file? Why isn't a swift file? And why is the syntax highlighting broken? And you're like, what's going on here? And then if you know that it's GYB and you know that it's like a specific form of code generation, I didn't actually know that they invented GYB specifically for Swift. I didn't know that.

Chris Dzombak
Don't quote me on that. But I'm pretty sure that it was just a purely internal tool.

Soroush Khanlou
I think it is internal, and then you look at it and you're like, oh, it's because they're like iterating through these four class names and generating one method for each of these class names. And I've heard from some people that know the Standard Library better than I do and that have even worked on some of this stuff, that some of these things are because of limitations in the Swift compiler. For example, if you have a protocol with an associated type, you can't have any constraints on that associated type. You can't say like, I want to have sequence has an associated type called subsequence, but you really want to constrain that to where subsequence also has to be a sequence and where subsequent Iterators elements are the same as your Iterators elements, which is really confusing to hear on a podcast. But basically these constraints aren't quite possible with the Swift compiler yet. I think they may be coming in Swift four, and that will reduce some of the need for some of the boilerplate generation that they do in the Swift Standard Library. But it won't get rid of all of it. I think some of it is just totally necessary, which is if it's necessary for the people who work on the Standard Library of Swift itself, it should also be necessary for the people who write the apps in the language as well, is kind of how I think about it.

Chris Dzombak
Yeah, I mean, maybe should is maybe a little bit strong, but I would say there's no harm in using it. So while you were talking, I added a few links to the show notes in the Swift repository. I linked to the Collection Algorithms template, which you mentioned, and also linked to this GYB PY tool. And that's just a Python script in the Swift repository that processes these templates.

Soroush Khanlou
Into the one Python Python file. That's crazy.

Chris Dzombak
Yeah, it's a 1146 line Python file, but it's one Python file.

Soroush Khanlou
There you go.

Chris Dzombak
And then I linked to a where did that link go? Post about reading the Swift Standard library source. For those of you who would like.

Soroush Khanlou
To go further into this, it's definitely worth it. And it's nice to also be able to settle some of the arguments about, like, oh, how does this thing work? How does flat might work on this specific collection? And you just dive in and find it. So I recommend being really comfortable with diving into the Standard Library source code.

Chris Dzombak
The beauty of this being open source is that you can do that, right? And the beauty of it being open source and such a young language, relatively speaking, is that it's still fairly easy to jump into the source, especially in the Standard Library and understand what's going on. Right? Sure. Things, of course, tend to accumulate cruft or complexity as they get older, and who knows if that'll happen with the Swift Standard Library, but I think they've.

Soroush Khanlou
Been really good so far about cleaning, keeping it tight, keeping it clean.

Chris Dzombak
Yeah, I think so, too. I guess I'm thinking more like jumping into the C plus plus. Standard library is more complex. But maybe that's also because C plus plus and not Swift.

Soroush Khanlou
Right? Well, and they've been able to do breaking changes so far, maybe at some point they will stop making breaking changes freely, and then the Standard Library at that point will start accumulating that craft.

Chris Dzombak
Yeah, that's a possibility.

Soroush Khanlou
So are there any other kinds of code generation that people use with Swift?

Chris Dzombak
What an excellent leading question.

Soroush Khanlou
Thank you. That's a segue.

Chris Dzombak
There's another tool which we're also using it. We're called Swift Gen from Olive olivier Alegon. Thank you.

Soroush Khanlou
Ali software on the Internet. Alligator with the hat.

Chris Dzombak
Yeah, I remember him as Ali Software. I can never remember his name. Besides, his initials are oh. I know that because Ohhtttp Stubs another great tool. So Swift Gen is a tool that is also written in Swift that will generate Swift code for accessing various assets in your project in a type, safe way. So everything from strings, from your localized strings tables to storyboards and colors and fonts and images. And this is really convenient because a lot of these things in UI kit, they're stringly typed APIs, right? You give something, a magic string that refers to some resource, and the system goes and gets this resource, maybe, and brings it back to you.

Soroush Khanlou
So what are some examples of some of these stringly typed APIs?

Chris Dzombak
Just something really simple like UI image named. Right. Get reading an image from disk or from an Asset catalog, getting a font that's embedded in your application bundle. Or Storyboards. Working with Storyboards segues, there's magic strings that various parts of your application have to know about.

Soroush Khanlou
You kind of name the segue and then you can refer to that segue by the string of its name.

Chris Dzombak
Right. And so you have to have that string defined in multiple places, and that obviously creates room for error when something changes down the road or when you just mistype something. Right?

Soroush Khanlou
Yeah. It's a real problem.

Chris Dzombak
Yeah. And so this tool, again, you'd run it as a build phase, and it will look through all these resources and generates enumerations in Swift that represent these string constants. So that rather than referring to an image or a Storyboard segue with a string, you have these nice constants that you can use with these APIs.

Soroush Khanlou
Yeah, this is a great tool. I've never used this. So you said do you use this in your project?

Chris Dzombak
Yeah, we do. We actually are not using it really heavily, obviously. We do have images and Assets catalogs and localized strings. We're not really using Storyboards and Segues because it's just such a clumsy thing to work with in Swift.

Soroush Khanlou
Right.

Chris Dzombak
As we discussed a while back, we're using the coordinator pattern to manage flow throughout the application.

Soroush Khanlou
Yeah. In a project that I'm working on, we do have Storyboards, and there's basically a way, I think Swift Gen adds a class method to each class that has a storyboard that backs it. So the UI view controller you would make with storyboard or whatever. So I have a project where we actually did bring that stuff over, just because grabbing the storyboard by name and then created initializing the View Controller with its name is kind of clunky, and I don't want to have to rely on that every time. So we basically have it pull from the name of the class and that's where it finds the files and it does all that stuff for you. Use Code gen to create those extensions. We kind of create those extensions manually, but in some sense, it is a little bit of metaprogramming because you use the name of the class that you're in. If you're like Location View Controller, it'll use the string of that class from like, if you do string describing the type, you'll get a string of the class name, and then from that it goes and finds fatal errors if it fails and then returns that. So it's a little bit of metaprogramming. But we don't actually use this tool for the Code gen. But I think we should.

Chris Dzombak
Yeah, why not?

Soroush Khanlou
Exactly. Why not? And I think it actually used to be written in Ruby, so now that.

Chris Dzombak
It'S written, I actually didn't know that.

Soroush Khanlou
I may be mistaken, but I'm pretty sure it used to be written in Ruby. But yeah, still pretty cool.

Chris Dzombak
I'm glad that you mentioned, too, that it adds some nicer API around storyboards in particular, because I had forgotten that because we're not using that part of this. One other thing that I really liked that we're not using now, but that I really would like to try to use is that you can generate an enumeration based on a list of colors just in text or even with an OS Ten color palette file. And that seems like something that could be kind of fun to play with. Right now we just have a extension on UI color that we use to get our applications colors. But yeah, this seems like it would be really nice too.

Soroush Khanlou
There's a benefit to the extension on the class way, which is that let's say you're saying view dot background color equals you couldn't write. Now, in Swift, you can just write dot black, whereas if you kept the extension on UI color with the class methods, you can just write like, dot my teal color or whatever, and it would still work. Whereas if you have an enum, then you have to pass it into an initializer, so you do like dot init with color name, and then you pass in the enum. So I feel like it's a little bit nicer of an API to just have the cross method.

Chris Dzombak
Yeah. So I don't think I have anything else to talk about, sirsh. Do you have anything else to mention?

Soroush Khanlou
No, those are all the code generation things in Swift that I know about.

Chris Dzombak
Okay, cool. If any of our listeners have other interesting tools in this vein that we should check out, obviously, please do let us know. Otherwise, I hope this has been a useful tour of some tools in Swift that we have for providing more typesafe metaprogramming than we had in objective C and really cutting down on some of the sort of duplicative boilerplate that we end up writing in Swift. And yeah, that's all. We'll talk to you soon.

