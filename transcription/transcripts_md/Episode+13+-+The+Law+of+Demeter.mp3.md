Speaker A
Okay. Welcome, listeners, to Fatal Error. Thank you so much for tuning in. I guess we still say tuning in. Yeah, definitely dialing in this frequency on your podcast players. I'm Krista Zomback.

Speaker B
And I'm Sirous Khanlow.

Speaker A
And on today's episode, sirous wants to talk about the Law of Demeter, and I do, too. We both want to talk about the Law of Demeter or the principle of least knowledge. This is something that I'm not totally sure if we have 30 minutes, if we can talk for 30 minutes about it, but I wouldn't be surprised if we can.

Speaker B
I think the Law of Demeter touches on so much of these little concepts of, like, encapsulation and loose coupling and information hiding that I think we'll get there.

Speaker A
Okay, cool. I just spilled a little bit of water on my mouse, but that's fine.

Speaker B
Problem? Everything's fine.

Speaker A
Everything is fine. So do you want to give an overview of what the Law of Demeter is first?

Speaker B
Yeah, I would be happy to. So I'm going to go ahead and preface this with, like, I'm not exactly sure where the law of Demeter is useful and where it's not, but I will give the definition that I've always heard, which is basically, if you're an object and you have children, don't talk to your children's children. Basically sometimes this is paraphrased, as you should only use one dot. So if you have, like, self dot my child, that doesn't count because you're accessing a member on self and then you have your one dot, which is like my children's. Did I say this right?

Speaker A
I'm not sure.

Speaker B
I've not tried. Yeah, you could tell your child to do something, but you can't do anything with your child's child. Right? Yeah.

Speaker A
Okay. I'm looking at the Wikipedia article for Law of Demeter.

Speaker B
Now, it is so named for its origin in the Demeter projects, an adaptive programming and aspects oriented programming effort which was so successful that its link is still read on Wikipedia.

Speaker A
Maybe we'll call it the principle of least knowledge then. But so that says a unit should have and I guess in terms of unit here, we're mostly talking about a class or a type, I think so.

Speaker B
Or like a function that gets passed.

Speaker A
Some object or maybe okay, well, so let's go over what this says in terms of units. And then I have something to say about maybe what a unit actually is. So units should have limited knowledge about other units. It should only know about other classes closely related to the current class. Class should only talk to its friends, not just strangers. This is also I see already why we're confused about that.

Speaker B
Yeah, it's very confusing.

Speaker A
And then only talk to your immediate friends. That last one, I think, is what you're getting to with this sort of colloquial. Don't use more than one dot.

Speaker B
Right. And that's kind of how I've always heard it in just, like, common conversation right.

Speaker A
So to kind of rephrase that interpretation, it's that you, being a class in a program, may have things that are various properties or references to other objects and it's okay for you to use those other objects, but not okay for you to use those other objects references to yet other objects, more distant objects.

Speaker B
I think one nice way to think about it is like, don't rely on the layout of another object, rely on that object's interface.

Speaker A
Are these not part of that object's interface if you can get to them?

Speaker B
So in some cases, the object chooses to make its layout public. And I think that's generally a flaw of the object. If it's just like if every property on the object is public, it should be either a very dumb object or type whatever, or it is like a poorly designed object, especially when you get into the territory where it becomes everything's variable, everything's mutable. Then you get to the point for sure where it's like not that well designed object.

Speaker A
When you say the word, when you refer to the layout of an object, what do you mean by that?

Speaker B
So in C and more like, I guess primitive, closer to the metal languages, you would literally know like the memory layout of an object. You would say like, this is in these bytes and these words, and this is in these words. And in Swift, you don't have access to that stuff, but you do have access to the properties that the thing has. And that, I think, is a shorthand for its layout. Basically, that is what the layout kind of looks like.

Speaker A
Yeah. Okay, so you mean like literally the class's layout memory. So you're thinking that the principle of lease knowledge means maybe relying on the publicly declared interface of a class rather than what I'm still not exactly sure.

Speaker B
What you're the way I would put it is this. So let me give you a concrete example. On one of my projects, I have a concept of like a task queue and I have a variable that represents an array of task items. And then this queue works through that array. I could make that array public. I could make that array's property public. And that was what I would be calling publicizing or publishing rather the layout of the task queue. But instead, what I chose to do is basically add one ad method and the ad takes a task and internally it decides how to append it to the array. That's to me the difference between basically publishing your layout and publishing an interface that is the correct way to access that internal layout, whatever it is. So we may need to add thread safety to this class. And that's something that's really easy to do if your public interface is merely this ad method. But it's much more complicated if now your array is just open to the world to be touched by anybody right.

Speaker A
Okay. So let me put this question to you then. Let's assume that you're writing a class and you're using another class's public interface to get to yet another object to one of your children's children. What's the problem there if you're using the public interface to do that?

Speaker B
The problem can be sometimes that the public interface is not very well designed, is my thought on it.

Speaker A
Okay.

Speaker B
So if the implementation details of that class change, then all of a sudden code that was valid is no longer valid.

Speaker A
I'm kind of thinking in the same vein, like maybe if you're doing that, you're kind of assuming a lot about how the object that you have a reference to is using or is related to the other objects that it's related to. Right. You're making an assumption there about right. And I guess it's important to note that maybe you are like maybe that assumption is sometimes perfectly valid.

Speaker B
So some things are dumb and some things are never going to change. Like a rect, like CG rect is always going to have an X-A-Y-A height and a width you can rely or like it's going to have an origin and X and a Y and a size of the height and the width.

Speaker A
Those are sort of intrinsic to yeah.

Speaker B
The idea of a rectangle is just so baked into everything that we do is just never going to change. I think it's fine to rely on that. But in terms of as you're writing these abstractions for yourself that may take on new requirements and new responsibilities and need to do those things in a slightly different way, it's important to create that public interface correctly.

Speaker A
Right. So to use another example here, if I'm writing an object that wants to write something to a database or to some storage mechanism, maybe I'm using a class that gives me data that also for some reason exposes the database that it uses to store data in. Right, right.

Speaker B
And it might be an action like somebody just forgot to put the private modifier on it.

Speaker A
Right. That's a possibility. Even though it might work for me to grab that reference to that database and stick some data in there that probably isn't the right thing to do. Right?

Speaker B
Yeah.

Speaker A
Okay.

Speaker B
And I don't think that's that disagreeable of an idea. And I think it's a little bit different than what law of demeter is kind of presented as being. It's presented as being don't use two dots.

Speaker A
Yeah. Or principle of least knowledge, don't use two dots. I'm also wondering now that we're really kind of getting into this, I'm wondering the top of the Wikipedia article summarizes this in terms of units, not classes. And so maybe in our applications, we're thinking rather than saying a class should only talk to its friends, not just strangers, maybe say like each module right. Or each area of an application should only talk to classes with types within that area and maybe to the externally defined interface like entry point for other areas. Do you see where I'm going with this?

Speaker B
I do. I think the reason they picked unit is because they don't want to tie this too closely to object oriented design or functional design. So I think the idea is like a function might be a unit where a function might get passed some structure of data, but then also there's no I guess you could use another function to get the child of the child out of the thing, if that makes sense.

Speaker A
Yeah. So take maybe a different tack here. What are the motivations for the principle of lease knowledge?

Speaker B
I think the motivation here is basically I think it's very closely related to the single responsibility principle stuff we talked about. If you write code that assumes too much about the world that it's in, any change in that world causes the code that you just wrote to be brittle. And that is bad is, I think I think the shortest way to put it.

Speaker A
Okay. And so the principle of least knowledge says by reaching far into other objects and getting dependencies or telling things far away from me to do things, I'm assuming more and more about the structure of the application and about the architecture surrounding me.

Speaker B
Yeah.

Speaker A
Okay. And those assumptions can lead to bugs. Okay. This seems reasonable.

Speaker B
Before we move on too far from the concept of not publicizing your entire layout of what properties you have or whatever, there's a blog post I'm going to throw into the show notes. It's called Set the Setting set, which is a really nice pun. It's by Graham Lee, if I'm remembering his last name. Yeah, Graham Lee. He is a UK based programmer. I think his blog is really great. Definitely check it out. He's got tons of good stuff. But one of the things he talks about is like the idea of setting a set is actually in English, one of the words with the most number of meanings. And we use it in programming for tons of stuff. So we use it for unordered collections, we use it for setting a property on a value. We use it for tons of stuff or settings. We use it for setting up stuff, all this stuff. So he brings up all these things. And so he basically, in this article in particular, singles out the idea of publicizing your setters and your getters. And that's more of a Java E type thing. Or like when you write objective C, when you write app property, you get a set and a get method synthesized for you for free. And he's saying, well, sometimes you're not setting something, sometimes you're updating something, sometimes you're renaming something. Sometimes you can provide a little bit more semantic context than just set thing. And I think user name equals whatever has the same flaw sometimes. Why are you changing the name of this user? Why can you change the name of this user? Aren't names like an Identifier that generally don't need to change? Is it like, what kind of name change is this? And providing more information in your API is better for the readers of your code. And it also providing a strict API around the stuff that you're working with. Lets you change the internals without having to worry too much about how much people rely on things from the outside. And so this blog post really crystallized this idea for me.

Speaker A
Okay? I didn't read this before the show. I did not know this post existed until just now. So I'll take a look at it after the show.

Speaker B
It's a really good one. It's a very good one.

Speaker A
Cool. So I'm still sort of mulling over this stuff because I really, honestly hadn't thought that much about the Law of Demeter or Principle of Least Knowledge until now. But sort of thinking about the motivation, which is right. Just sort of reducing coupling as a means to reduce the number of assumptions that an object makes about the world around it. I like that motivation. So in Swift, what are some things that we can do to follow at least the spirit of this motivation? Right. We agree that it maybe doesn't necessarily mean that you're not allowed to use two dots. So what does it mean for us?

Speaker B
I use computed properties a lot and shout out to Brian Irace who thinks that there should be no difference between functions that take no parameters and properties. And I think he's really right about that. But basically, I think just a property is just another way to expose details that you want to expose to the outside world. And as much as long as you can control how you expose that stuff, I think you're good. And so that's part of the reason that I use computer properties a lot. So let's say if you have, like it's a couple of interesting cases because let's say you have a book that has many pages and a page has many lines. You might call book pages, flatmap lines to get all the lines. Or you could make a computer property on each page that returns each line and a computer property on the book that returns all lines. And so the book only knows that it has pages and it gets all the lines for the pages. That being said, sometimes I can get a little bit unwieldy because it feels like you're defining a bunch of code that you don't really need to be defining. People know how to get the lines out of a page so it can feel like you're adding a bunch of intermediate steps. The place that I think you have to make that call is when you are trying to decide, like, how do other people use this? Do I want other people to just be able to reach in and mutate these lines as they please or read these lines as they please. Do I want to hide that information in some way and say like, oh, book might be made up of pages, but it might be made up of images, it might be made up of some HTML like Dom tree that's like representative of an EPUB. How do I want to represent that stuff to the outside world? So I think that when you are at that stage, you have to think about what other objects use this and how likely is this to change.

Speaker A
Okay, so I like this sort of thinking about your interface and depending on your intended use cases and how likely your implementation or dependencies are to change, you may bubble some of this API up to your sort of what's a good word for this almost entry point for that object graph, if that makes sense. Okay, so I like that. Oh, go ahead.

Speaker B
You mentioned like an entry point into your object graph. The other place that I think you would really be interested in some of this stuff is when you're testing something. If you have to mock out some dependency like this book, you all of a sudden have to make a mock that is, the page as well. And you have to return an array of pages. And then from the page you have to mock out the returning of the lines. Whereas if you just had a function on book that returned all the lines, you can just mock out that one function or fake or whatever the right term is.

Speaker A
That's true. Yeah. So really consider testing. Right, that's a really good point.

Speaker B
Right. And as ever, testing provides the motivation that you need to execute the good design in your app.

Speaker A
Yeah. So I'm sort of thinking here as you're programming, it's probably useful not just thinking about your interfaces like that, but to think about maybe not necessarily even modules since your entire application in Swift is probably one module. But to sort of think about the different maybe domains or areas within your application and really think about the entry point isn't quite the right phrase, but I don't have a better phrase. Now try to think about the entry points or sort of the main external APIs for each of these areas of your application and either don't cross one of those boundaries with a lot of getters or method calls. And if you're finding that you have to do that to achieve something, that's probably an indication that as you note, some of that should be captured or consolidated into one API at the sort of external surface of that area of the application. Does that make sense?

Speaker B
Yeah, I think it does. I think you're definitely onto something, which is maybe if I can slightly rephrase that. If you have a situation where you are violating logged meter, you have thing, thing, thing first thing, then that's like a code smell that suggests a bad design and suggests that you go back and look at the design of how you laid these things out.

Speaker A
Yeah, absolutely. Or again, if you're like crossing from one area of the app into the other somewhere in that chain of things. Right, that's probably a good point to introduce a new API that hides at least some of that behind a nicer API.

Speaker B
One thing that can be nice in terms of breaking up your app into different components without having to worry too much about setting up modules and doing all that stuff is doing the fake name spacing with an enum. With no cases and using that and saying, this is the authentication part of my app and everything that is in here is for authentication and this is the push notification part of my app. And if the authentication part has to reach into the push notification part a lot, that's really weird and that's definitely a sign that something's gone wrong. And I need to reevaluate what's up here.

Speaker A
And it bears mentioning too. We should find and add a link to the show notes about that trick of using an enum with no cases just as a namespace in Swift for sure.

Speaker B
I have a blog post on it.

Speaker A
Oh, that works fine. Yeah, I don't know how I missed that. I'm sorry.

Speaker B
No problem.

Speaker A
I'm really glad that you mentioned testing too because right, like reaching far into an object and its dependencies is going to make testing whatever it is that you're writing in isolation incredibly difficult. And so that's another motivation to, if not adhere to the principle of least knowledge as being just one dot like to adhere to it in spirit. Right. Just know that every time you reach one level further out in the object graph, that's a whole lot more that you have to set up in your testing suite.

Speaker B
Right. I have a code sample from a friend where they were just trying to make something work and they were presenting this as good code, but it was like some kind of transit app and it was like a filter. And to get a bunch of trips, let's say it was a filter that gets a bunch of routes and then flat maps those routes, then a bunch of route IDs and then it gets the directions from those. So it's another filter flat map, another filter flat map. And sometimes these filter flat map chains can be really nice to write and really pleasing that like, oh, I turned to this really elegant functional chain. But that even though you're not accessing properties directly on the thing, in some sense you are relying on a ton of knowledge of like well, I know that this type is going to have this type of thing and this type of property on it. And then I know that'll come out as an array that I can flat map. And I know that this acts like that and you end up with a ton of knowledge in just let's say this looks like nine lines of code. And so that can also be a bit of a code smile, even though you're not directly accessing properties in a chain.

Speaker A
Maybe, although I suspect that at least each of those parts could be tested in isolation. Right, from what you described.

Speaker B
Well, but it's one set of code that says, like, hey, get all these and then filter by this, then get all these, then filter by this, then get all these, then filter by this.

Speaker A
Yeah, that's tough.

Speaker B
Yeah, stuff is not easy. There's something I'm looking for in the Apple docs. It was really funny and I can't find it anymore, but it was basically like it was somewhere in the al assets, in the al assets documentation. And it was really absurd. Just like a crazy chain of, oh, this might be it. I think this is it. So it's player item tracks objected index, zero asset track asset duration. And the idea is that's how you get the duration of a thing. And with public APIs like Apples, you're pretty sure that that stuff is not going to change. But if you are going to rely on this in a lot of places, it may make sense to just turn this into a computer property, expose it somewhere, and then just use that exposed thing rather than just having all this crazy code everywhere.

Speaker A
Yeah. I'm wondering, I don't know that much about the Demeter project that this law apparently came from, but I'm wondering if that was in a statically type check language or if that was in a more objective C or Ruby style language.

Speaker B
What difference do you think it would make?

Speaker A
Well, I'm thinking so you mentioned that with that example, we know these are in Apple's frameworks and they're probably not going to change, but if something in that chain did change in Swift, that's something that the compiler would at least flag and say, hey, this objected index no longer has this property. Right, right. Whereas if it were in Ruby or objective seat, that increases the surface of things that can break your application without you even knowing so substantially. Whereas here, at least you would know about it.

Speaker B
I'm looking at the website for Demeter, the aspect oriented software development thing. It looks like yeah, but I can't tell what languages it was Northeastern University looks like.

Speaker A
Yeah, I am too. This is going to be something that I will look at after we record, but it's going to be really boring to hear me read through this website.

Speaker B
Yeah, that checks out. But yeah, I guess my big fear about logged meter was that I've heard so much about this and it's got law in the name, even though there's no laws when you're programming. I had a coworker, a former coworker who calls it the Gentle suggestion of demeter.

Speaker A
I think from going forward, I'm probably going to call it the Principle of least Knowledge.

Speaker B
Yeah. And that is a better name, but also nobody's going to know what you're talking about.

Speaker A
No one knows what you're talking about with Law of Demeter anyway.

Speaker B
That's true. That's fair. The principle of don't use two dots. But it's just like I feel like that's such a reduction of what it actually is and what's actually important here that it's like, oh, well, if I just create this variable on another line, then I'm fine. Like, create the intermediate variable on another line. It's like well, you've kind of skirted around, as you said earlier, like the letter of the law rather than obeying.

Speaker A
The spirit of the law, but you're creating the same problem or not creating the same.

Speaker B
Exactly. So do you think you have a good handle on what Law of Demeter is?

Speaker A
Yeah, I think I do. Like I said, hadn't really thought about this seriously in quite a while. I think that going forward, I'm still going to call it the Principle of lease Knowledge, because that seems pretty self explanatory. Really precise. It seems more precise. Yeah. I think I have a little bit better idea of the motivation behind it. And the things that you want to look out for is warning signs that you're violating this principle in a way that's going to be problematic down the road.

Speaker B
Right. Let me ask you this. Would you ever add it as a Swift Lint rule that says you may not use two dots in one line or find a way to define you may not rely too much on the details of external?

Speaker A
I probably would not. Maybe with an extreme number of dots, but even then, probably not.

Speaker B
Yeah. I feel like if you're in four and five, something's gone wrong.

Speaker A
Well, maybe I'm thinking what about one of your, like, a promise chain, though? Like, you may easily have five dots in one of those chains.

Speaker B
Right.

Speaker A
And it's still one statement.

Speaker B
Right, right. Yeah. That's definitely different than like because you're causing an action to happen each time and I feel like that's different to me than touching a property each time.

Speaker A
Well, how are you going to tell Swiftlin that, though?

Speaker B
That's true. That's fair.

Speaker A
So it is something that I will look for in code review and be able to better defend in code review now. Right. If I say, look, you're sort of reaching pretty far from your object here and here's where I think it crosses into, like it crosses a boundary into a different part of the app. And maybe this is an indication that this needs to be implemented as an API in that part of the application for you to consume here. I think that's really my biggest takeaway here. And again, the same sort of just testing implications in terms of dependency management that we grapple with every day.

Speaker B
Right. That makes a lot of sense. I think that's a pretty sensible approach to this problem.

Speaker A
And before we conclude, I wanted to mention too obviously, if your app is split into modules, then you can use Swift's access control rules to really enforce good practices here.

Speaker B
Right. But the takeaway is that the design has to happen upfront when you're at the point of making the chain of all the dots, something has already gone wrong.

Speaker A
Oh, yeah, absolutely. But that doesn't mean that you can't go back and make it right when you find yourself writing a chain of dots.

Speaker B
Right, of course. Yeah. I think that's the biggest thing I have about logged meter is that it's not about the call site. It's about like the call site shows you that something has gone wrong, but the actual problem is elsewhere, not at the call site. The actual root of the problem. And I think that's the core of what I'm trying to get at.

Speaker A
That makes sense. And the problem might just be that this use case hasn't been considered before. Right. It may not be as insidious.

Speaker B
Right.

Speaker A
Yeah. Cool.

Speaker B
Yeah. That was fun. That was interesting.

Speaker A
Yeah. I don't think I have anything else to add, do you?

Speaker B
No, that's it for me. This is an interesting topic.

Speaker A
Yeah.

Speaker B
Let me ask you a semi side related question here.

Speaker A
Sure.

Speaker B
Let's say you're making a new type in Swift, let's say Struct class, whatever, and you need it to be initialized with a couple of things and maybe a couple of dependencies. When you initialize it with those things, you obviously have to store those things into properties on that object. Do you make those properties public or private or read only public or anything like that? What do you decide to do there? Let's see, because the issue that I'm foreseeing and I'm worried about is that if it's public, then you kind of can skip over all of the constraints that that object puts into place for you and jump right over them, touch the actual dependency inside and just do whatever you want.

Speaker A
I would say, obviously it varies on a case by case basis. I would usually default to making them private and until there's a use case for them to be something else.

Speaker B
Right, okay. That makes a lot of sense. I used to in objective C, I used to always make them read only on the outside, I guess, so that you could init it with the thing and then check that you initiated it correctly. But the more I think about it, I think that was just wrong. I think they should just be private.

Speaker A
Well, and that specific check is maybe less useful in Swift, because Swift will warn you if you didn't initialize something.

Speaker B
Right, right, exactly.

Speaker A
Yeah. I would say make your dependencies should be private and you should provide API to do things that involve those dependencies. And if your dependencies need to. Become maybe internal. That seems like in some cases, that's reasonable. If you're just exposing something that was given to you as a dependency, as public, then there's probably something else you probably want to do. Something else?

Speaker B
Yeah, that makes a lot of sense.

Speaker A
Yeah.

Speaker B
Cool.

Speaker A
I haven't thought about that as a guiding principle both for too long here, but I think it's right.

Speaker B
Yeah, it seems right to me, too. Awesome. This was a lot of fun.

Speaker A
Yeah, absolutely. Thank you, everybody, for listening. And we'll talk to you soon.

Speaker B
Sounds good. Later.

