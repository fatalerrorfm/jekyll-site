Chris Dzombak
Man. We need more shocking and driving.

Soroush Khanlou
We need a lot more.

Chris Dzombak
Where are we gonna get an intro for this one?

Soroush Khanlou
Why don't we? I don't know. I don't know. Maybe this is the intro.

Chris Dzombak
Whoa. Mind blown.

Soroush Khanlou
Very meta. Honestly, that wouldn't be the worst thing in the world.

Chris Dzombak
No, that would work. Alright. Welcome to episode eight of Fatal Error. I'm Krista Zomback. Cool.

Soroush Khanlou
And I'm Sirush Khan. Lou. Hi. Chris.

Chris Dzombak
Hi. So today, Sirous has promised to tell me about domain driven design, which is a term that I am not at all familiar with, but I am always excited to learn new things. So sarosh, I guess take it away. Cool.

Soroush Khanlou
Yeah. I guess maybe three years ago, I kind of went on a tear of asking people to recommend me programming books and kind of reading through them, skimming through the parts that I thought were obvious and then kind of studying more in depth the parts that I thought were really novel and interesting. And I have a post on my site that's about some of the books that I found during that time that I thought were really good. So I thought Martin Fowler's refactoring was really good. I thought Sandy Metz's practical, object oriented design in Ruby was really good. And there was also this other book called Domain Driven Design, and I don't remember who recommended it to me. I think it was a coworker. And I kind of just got it on a lark. I was working at a company that had an unlimited budget for programming books, which was nice. Yeah, really great. Perk. So I just sort of bought it on their dime and started reading it and found that I actually liked it a lot. And so it kind of became part of the tools in the tool chest for how I write stuff and how I think about how objects interact and what a model layer really is. And I feel like it's a good natural follow on to what we talked about last week, the single responsibility principle stuff.

Chris Dzombak
Cool.

Soroush Khanlou
Yeah. So this book is by Eric Evans and it basically runs through a very I would say it seems like a forced example of like cargo shipping and whatever. And it's kind of a dry topic, but he sort of lays out how a developer and a domain expert come together to develop what he calls a ubiquitous language to talk about this domain, which is shipping things back and forth between different like they have Itineraries and Cargo and ports and all that all those kinds of things to the model. And he has sort of dialogues between a domain expert and the programmer and he shows what a bad dialogue looks like when they're not really communicating at a high level. So in those bad dialogues, the programmer is talking about like, oh, so what should I have a database row for? Or like, really specific technical details which the domain expert just doesn't know about. And then he contrasts that with sort of good dialogue where they have developed this ubiquitous language and they can communicate really efficiently together. And part of this involves the programmer learning more about the domain and a little bit about the domain expert learning about the technical limitations of the system that they're working in.

Chris Dzombak
So I'm already really interested and pretty invested and have already ordered this from Amazon, this book, just during the show well, just before we started recording. But that sounds really familiar to me. At my current job, working at The Times, the first thing that you do as a developer really is start to get an understanding of how the newsroom thinks about things and how the newsroom sort of models their world, their domain. Right, right. And you end up working with people from the newsroom or the product team who need to have some understanding of sort of not necessarily technical, like, in depth concerns, but what the iOS platform is and what conventions here are and how we sort of model things in that platform. So, yeah, I totally get where we're going with this, I think.

Soroush Khanlou
Yeah. And if you really think about it, sometimes there are developers that work in contexts of more code. So if you're writing a tool for developers, you might need models for a representation of a class that's backed by a file that has the contents of that class, which is very meta and weird, but you could have concept of a program and all these things built into your model. But for the most part, we don't work on tools for other programmers, we work on tools for other people. And so we have to understand the domains that those people think and work in. We have to learn something about those domains, otherwise we can't make good technical decisions.

Chris Dzombak
Right. You have to understand the problem you're trying to solve.

Soroush Khanlou
Right, exactly. I kind of want to go over like, I can't go over the whole book, but I want to go over a couple of things that I drew from it that were very revelatory for me and hopefully that inspires you and hopefully our listeners to go and check this book out and learn more of the in depth stuff. So in this book, after the author introduces us to this concept of a ubiquitous language and sort of this coupling layer between the domain expert and the programmer he mentions go ahead.

Chris Dzombak
Can I back up just a second? So this ubiquitous language is a shared understanding, like shared terminology between these okay.

Soroush Khanlou
Yeah. I think he uses that exact language of a shared understanding between the developer and the domain expert. Cool.

Chris Dzombak
Maybe don't even need the book.

Soroush Khanlou
Maybe you've got it all ready. Yeah. And it's also it's funny because it's written in kind of a Java esque world and kind of like a 90s vibe. I think it's from 2003 maybe, but it's like more than a decade ago. And so there's like XML or UML, markup with the boxes and the asterisks and describing the how do you call that? I guess the object graph.

Chris Dzombak
Right. I learned, UML, once it seems like.

Soroush Khanlou
A somewhat useful thing.

Chris Dzombak
I'm sorry it took us down into the weeds.

Soroush Khanlou
Maybe the Weeds is the new name of this podcast.

Chris Dzombak
There's already a good podcast called The Weeds.

Soroush Khanlou
What is it about?

Chris Dzombak
It's about policy, so not at all programming, though. Yeah, it's interesting. It's a Vox podcast.

Soroush Khanlou
Oh, nice.

Chris Dzombak
Right. So things that you took away from this book.

Soroush Khanlou
Right, let's back on track out of The Weeds. So one big thing I took away from this book is, for example, he talks about the distinction between entities and values. And the really simple way to think about that is that an entity is sort of more like a table in a database. Like one instance of an entity represents a row in a table in a database, and then the value represents one field in that row. Right. And I think because we think of our model layer as mostly just the tables in a database, like each table gets a class. And from that, that's the bulk of our model layer and that realization. And this was I read this, I think, in 2014, so it was actually right before Swift came out. And so values weren't really on the, on anybody's radar talking about, well, this object doesn't have any identity in itself, it just matters what the contents of it are. Right. Like, if you have a car with a specific type of leather, you might not actually care which instance of the leather you have, you just need to know that you have this kind of leather. It's more about the information about the type of it rather than the, rather than the thing itself. And then Swift comes on the scene and draws this very first class distinction between classes and structs, and it's more sort of solidified. Now, what is the difference between what we treat as entities and what we treat as structs or values?

Chris Dzombak
And so what are some key differences that are outlined? The first thing that comes to mind is whether identity is important.

Soroush Khanlou
Yeah. So that's basically the primary distinction that he draws.

Chris Dzombak
Okay, I'm trying to think of a.

Soroush Khanlou
Better example than the leather in a car. Car analogies are just the worst.

Chris Dzombak
They're always kinds of animals.

Soroush Khanlou
That's the class kinds of animals. A lot of these are enumerations also, which are also valuable, and they're also sort of the values in the same.

Chris Dzombak
Way that sort of aligned with exactly right.

Soroush Khanlou
So you could have a database column that's an enumeration of that holds one of many disjoint states. And he talks about some of that stuff too, but I'm trying to think of when there would be just like.

Chris Dzombak
Let'S say if you have a product that has like a price attached, right? You would have just a value that represents that price. It's not important that that price has an identity on its own. It's not important that it can be shared between other instances as this one spot in memory. Right. It's more of an inert value. It's more of a property of something than something that exists on its own.

Soroush Khanlou
That's a really great example. Or another one would be if you had you're welcome. If you had something for a class and you wanted to model grades, you could model them as a letter, which is fine, but then you have a bunch of invalid values that you can store and you can't sort of initialize one with a number that turns into a letter grade, like ABCDF. But if you represent this as a fully fledged model or as a fully fledged value, then you can attach behavior to it, you can attach validation to it, all kinds of stuff like that. Those are some basic examples of when you would use a value in your model rather than using an entity. Because again, if two people have an A in the class, it doesn't matter if it's the same instance, it doesn't matter if it's different. You can't really mutate it. It just is an A. Right.

Chris Dzombak
There's no relationship between those two A's, right?

Soroush Khanlou
Yeah, exactly.

Chris Dzombak
So this distinction between entity and value objects in domain driven design, why is this important? Are there any interesting properties or ways to think about design that fall out of this? Or is it sort of the same ideas that we think about when writing Swift code now?

Soroush Khanlou
They're really similar ideas. I kind of feel like they serve run parallel in a sense, because they deal with not only the representation of things in memory, but they also represent the thing sort of on disk. And some models and some apps don't need to deal with that and they just fetch all the information on the fly. They don't even bother caching. And so you don't really have to worry about that. But I think it's a very similar thing to classes risk structs, but it's sort of on a parallel track because it represents something that might be on the disk rather than something that is in memory at all times.

Chris Dzombak
Okay.

Soroush Khanlou
Yeah. So I read this and we were all still writing objective C. And objective C kind of inherently has this concept of identity. Everything is a fully fledged object. Everything is a reference type, as we call it now. And reading this kind of made me realize, like, wow, there's this whole other world of things that I can model that aren't necessarily going to have an ID, that aren't going to have its own identity. And I ended up writing a blog post about it called The Value of Value Objects. And that blog post came almost basically entirely from the stuff that I learned in this book, and I did a little bit of extra research into other communities and how they handle it. So I linked to a post called Tiny Types, and they talk about that stuff in there as well. And then I followed it up with a post on Enumerations. And it's funny because now the blog post has, like, a caveat at the top. This is like, hey, this was written before Swift came out, and you can now add functions to enumerations. But before, we had just had basically they were just typesugar around numbers. And it was a very different time back then. And so this technique was actually useful the Dark Ages. And this concept of, like, an enumeration as a value as well sort of came from what he talks about in terms of values versus entities. And that was definitely, like a big, you know, when you have that epiphany and you're just like, wow, just see the world in a new through glasses. And this values versus entities was definitely a big part of that.

Chris Dzombak
Okay, cool.

Soroush Khanlou
Yeah.

Chris Dzombak
So that's one thing that you took away from this book. Is there another thing that springs to mind you want to talk about?

Soroush Khanlou
Yeah. So there's also another thing that he brings up, which is this concept of aggregates. And this is a little bit harder to talk about since Swift doesn't have sort of a first class construct for what this is. There's no nice parallel to something that we deal with on a day to day basis, but you can kind of approximate it with sort of access levels, like public, private, and internal. Basically, the concept is when you're dealing with this model, there are objects that you might be touching, but you're never holding on to them directly. And he actually does use a car analogy for this. And so he has the concept that there's sort of a boundary around a car, and while the car has maybe an array of wheels or however you decide to model it exactly, the users of the class car, instances of the class car don't grab those wheels directly and hold on to them and do stuff to them. They kind of always access it through this car. And so if you were thinking about it in a Swifty sense, you might say, well, if I put my model into a module, I might make the wheel internal and then gate all of the access through the car to access those properties and mutate them and change them in the way.

Chris Dzombak
So is this sort of basically like composition or facade related concept, or is it something vastly different?

Soroush Khanlou
It's not vastly different than a facade. It's like a facade. So a facade is what? A facade is. One object that has one interface that touches many objects underneath it, is that.

Chris Dzombak
I think that's sort of right, yeah.

Soroush Khanlou
It's sort of saying, these are the objects you should touch and deal with and while there may be other objects that you have access to, you shouldn't necessarily be instantiating those objects. You shouldn't be pulling those objects out of like you shouldn't be pulling a wheel out of a car. For the car to stay a valid car, it has to keep wheels.

Chris Dzombak
So I'm looking at this post from Martin Fowler about aggregates in domain driven development. Seems like and this lines up with something that you said a moment ago about sort of access control levels in Swift. But it seems like the idea of aggregates is useful for drawing boundaries around, maybe implementation details of the model you're implementing.

Soroush Khanlou
Yeah, that's definitely and sort of the.

Chris Dzombak
Outer, maybe interface that is what that is. Like, what the rest of the application might deal with these higher level constructs that are not implementation details. Maybe the aggregate is what you test rather than testing the individual parts. Is that true?

Soroush Khanlou
Yeah. Well, so you might within the domain module, like, inside the model, you might be testing the wheels to make sure they're consistent, but when you create the car, you might not be mocking out those wheels.

Chris Dzombak
Okay, we're really stretching this metaphor.

Soroush Khanlou
Yeah, we're really pushing it. Really pushing it.

Chris Dzombak
Okay. I'll put this Martin Fowler article in the show Notes, though.

Soroush Khanlou
Yeah, I think that'll be useful.

Chris Dzombak
I think it's just a useful for sort of something like access control, but defining and enforcing boundaries.

Soroush Khanlou
Right, exactly.

Chris Dzombak
Okay.

Soroush Khanlou
And as you define new types in the thing, maybe one way to think about it is, let's say in Swift, you might have your car class have a nested type inside of it that's a wheel. And when you see that, it's kind of a red flag, like, hey, this wheel really needs to stay part of this car. And you could instantiate your own, but don't.

Chris Dzombak
Interesting. Okay.

Soroush Khanlou
Yeah. It's kind of like a nested type is a way to think about it. You don't want to prevent access to it, but you also don't necessarily want the user to just be able to rip it out and create their own and put them in. Unless that's what the model sort of needs to do.

Chris Dzombak
Yeah. Okay, cool. So that's probably a useful thing to keep in mind. So what I've gotten so far and again, coming into this knowing nothing about this, really, so what we've talked about so far seem generally to be basically ways to think about modeling something that's really complex and ways to break it down into something that's maintainable and manageable for you to implement. Right?

Soroush Khanlou
Yeah.

Chris Dzombak
Is that a fair characterization of what we've talked about so far?

Soroush Khanlou
Yeah, that is a key point of how domain driven design works. And I think another part of it is like, if you have a concept in your app, make the concept real by making a type around it. And of course, this was Javas. They were just calling it class. All the time, but we would call it a type. Make a type around it, add the functions to it, test it so that your domain is rich enough for people to come in and understand it, for you to be able to move through it and say, well, this thing has a name now, and I can look at it. I can see what it does, I can see what its purpose is in the app. I can see where it's used in the app, rather than, let's say, just passing around a dictionary or passing around a string that really is only supposed to be in three states. But in fact, you're not enforcing that anywhere, and you're not making that real. And I think part of it is make the concepts that need to be real, real and use those to sort of flesh out the rest of your model.

Chris Dzombak
Okay, is this one of the key points in domain Driven Design? Just step back and ask a really big question. What is domain driven design then? Is it a set of tools for thinking about modeling complex domains, or is there something else here?

Soroush Khanlou
I think it is a set of tools, but I think it's more of ideology. Feels like a heavy word, but it's a framework for understanding and creating models that are really rich and really good to work with. Okay, yeah, I feel like a lot of the time when we talk about our model, we think about it in terms of, oh, it's these tables in our database, and they become these classes, and they have these relationships. Or we think about it in terms of, okay, well, I have this JSON, and that JSON has every object in that JSON becomes sort of a class in my domain. But I think that a real domain is so much richer than that. You not only have your entities, which I think are these, like, top level JSON objects or top level tables in your database, you also have your value objects, which might come from JSON values of true and false might come from JSON values of integers or strings. They also might come from fields in a database. But they're an important part of your model too, and they help you really flesh it out. Then you have other components, like Services, which is a little abstract of a name for my taste, but basically represents, hey, I want to access this database or this network service or whatever. Okay, and so you have all these components, and all these components come together in a bigger way than just, well, my model is these 20 core data classes, right?

Chris Dzombak
So, so far, we've talked a lot about modeling entities values and about drawing boundaries right, with aggregates. What, if anything, does domain Driven design have to say about modeling business rules, like actual logic? And I mean, that's a very broad question, sort of intentionally, because I, again, don't really know what we're talking about here. Does it have anything to say about how to model logic, how to model complex business rules, where this logic lives, anything like that?

Soroush Khanlou
So he mentions two things regarding how to wrap business logic into your domain. One of the things he talks about is constraints and policies and how to model those. And so in his cargo shipping analogy, or rather example, he has like an overbooking policy. And so it's a way for a voyage to determine if it has too much cargo. And voyage and cargo are capital V, capital C. There they're fully reified concepts in his model and his overbooking policy kind of just gets fired up and just tests whether the voyage has the right amount of cargo. And he also mentions sort of the strategy pattern in terms of you can inject different policies, let's say for testing, you don't ever want one to be overbooked. So you might inject a special one for testing or special one for certain clients, stuff like that. And then he also talks about processes. So if you had some kind of not long lived but also not short lived thing, where, let's say in one specific example, it might be a transaction in a database, you have to get this object out, grab its ID. Do something special to it. Transform it somehow. Save it as a record, update some cache count in another place, and then maybe release some lock on the database that might be represented as a process. And that process is also like part of your domain.

Chris Dzombak
Okay, but so that's a part of the domain that would be, I guess, modeled in an object that does things right, that maybe takes dependencies like a database and like other model objects, maybe entities and then performs actions. Right, okay, but that's considered part of the models because it represents some business rules or something.

Soroush Khanlou
Yeah, it does.

Chris Dzombak
Okay, so this terminology is somewhat different than the terminology we're used to thinking about in our little iOS corner of the world and the terminology we used in episodes one through seven.

Soroush Khanlou
In terms of what specifically just in.

Chris Dzombak
Terms of, I mean, considering as part of the quote unquote model to have these sort of process objects or maybe something we might more traditionally name like a coordinator or something.

Soroush Khanlou
Right, right.

Chris Dzombak
We're already talking about the term model involving a little bit more than just the sort of traditional data model classes.

Soroush Khanlou
Right. He's really specific. He calls those entities in a really rigid way so that he doesn't get it confused with the rest of the model. Okay, yeah, but yeah, I mean, inasmuch as especially if you have a core data heavy app, all of your models, maybe you create some special version of your own object, but probably for the most part you're transacting with NS managed object subclasses and those, like they're going to do the database stuff. They have knowledge of how the database works. They are passed into other things and in that way, I think they're part of the model as well.

Chris Dzombak
Okay, this makes some sense. I can see that. And this does sort of line up with I'll let you get back to your thought in a moment. This sort of lines up with a question I remember you asking, I think in the view models episode or something shortly thereafter where you were thinking about reconsidering what exactly the term model means in this context.

Soroush Khanlou
Yeah, that was episode three view models again. But yeah, we had to do a follow up because I had too many questions. But yeah, I definitely think that that's part of it. Right. Inasmuch as a view controller binds a model to a view and a view is managing what's on display and how we interact with that thing that's on display, the model then is left with basically all of our business logic.

Chris Dzombak
Okay, interesting.

Soroush Khanlou
Yeah, I think it's basically right. I don't really like the sharp distinction between model, view and controller, but would you put the business logic in something that we would traditionally call a controller?

Chris Dzombak
I mean, I think something that we've been tending toward with view models, with thinking about the single responsibility pattern with coordinators is starting to tease apart the parts of the application that are more business logic oriented, that are more model oriented and the parts of the application that are more maybe iOS housekeeping oriented and the parts that are actually, like strictly view layer. Right, right. And we can maybe quibble about what things fit in model, view, controller, view model. Maybe view models are a little bit somewhere between controller and model. After all, that's sort of where they go in a diagram if you replace the controller with a view model right. That sort of mediates the view.

Soroush Khanlou
Right. I don't know if it would be considered a view specific thing, but it knows, like, hey, should this button be visible? And that's kind of like knowing about the view, but in some sense the button could be on a platform.

Chris Dzombak
Yeah.

Soroush Khanlou
Weeds, weeds, weeds of the weeds. Very happy in the weeds.

Chris Dzombak
I mean, I think it is useful for us to take a step back from thinking about just talking about this in the abstract and think, okay, how does this apply to what we've talked about so far in this season and in what we do in our day to day job?

Soroush Khanlou
Yeah, and I think it's like the lessons that he gives are very couched and like, here's how you create a model. But I think that they can be applied more broadly in the same way that the single responsibility principle can. If you need an enumeration that represents these things that can only have these consistent states and are not allowed to be in any other state than those, then create that enumeration even if it's not in your model. Specifically the lessons of identity. Is identity important versus identity not important? Are broader than just using this for your model. But a model is a good place to start with that stuff.

Chris Dzombak
Or, I mean, if you introduce an enumeration for something like this, whether you call it part of your model or not is almost inconsequential. Right. You are modeling something there.

Soroush Khanlou
Yeah, exactly. Even if you're trying to represent here's the three kinds of ways you can auth to our API, you're modeling something even if it's not the domain of your app itself.

Chris Dzombak
Yeah. Okay, cool. Is there any other big lesson that you took away from this or interesting way to think about something?

Soroush Khanlou
Yeah, and this is sort of one of the broader things that I picked up from the book. Not necessarily something that he talks about specifically, but one of the things that I took away from this was that and we sort of touched on this in a singleton episode, but basically, if you have a concept in your app that needs to be modeled but doesn't feel like a traditional model, go ahead and make it anyway and see what behavior and stuff you could attach to it. Right. So if you had I think we talked about the concept of a cart or like a current cart. You have a cart model for sure, which has an array of items that are in the cart, like a subtotal, whatever else. But the current cart is really a different concept than any cart.

Chris Dzombak
Right.

Soroush Khanlou
The current cart is something that you could name it something different and just call it a view model, I think, in some worlds, but it might have a method like, hey, add this to the cart. Add this item to the cart.

Chris Dzombak
I don't think the current cart would be something that you call a view model, but right. There's a difference between a cart in general and the current cart and those rules or the fact that there is a current cart that you're adding things to. That's part of your business rules. Right. That's part of the business logic.

Soroush Khanlou
Right. And while you might be tempted to model the current cart with any cart object, the one that's database backed or core data backed or whatever, there are really different policies and different restrictions and different functions that need to be available on each one. Might need to be able to check certain preconditions before adding two. So the current cart would have a cart model. Right. I need to check certain conditions before it adds, like, are you logged in? Can you do this thing? Do you have the permission to do this thing? Whereas the cart itself might have preconditions on it that are like, oh, can this cart be this big? Or how many items can be in a cart at a given time? Especially if you're starting out like that might be a nice piece of business logic that. You need. And so that goes on any cart, but there are other preconditions that might go on, specifically the current cart.

Chris Dzombak
Sure. Yeah.

Soroush Khanlou
So those are the things that I kind of drew from this more generally, is, like, if you have a concept that needs to be reified, if you have a concept that needs to be formalized into a type, you got to do it. And then it becomes more clear what functions need to go on it, what behavior, what data needs to go on it. And the names of those objects yield so much more clarity, especially to someone coming in that's new, especially to yourself in six months or a year. It's super important.

Chris Dzombak
Cool. I will look forward to getting this book from Amazon and really digging in, but I think already we've looked at some really useful things to think about that line up with a lot of the things that we've talked about already in this season, especially around the single responsibility principle. We've touched on singleton's, we've touched on the Facade pattern. We've touched on some kind of similar or sort of related concepts. And so I feel like some of the stuff that we talked about tonight is just more useful tools for thinking about how to think about modeling the domain in which you're programming. Right. Which is a hard thing and which isn't necessarily a given. Like, if you graduate with a computer science degree, you know about computer science. But to be really, really useful as a programmer, you have to understand both computer science and the domain that you're working in.

Soroush Khanlou
Right, yeah, exactly.

Chris Dzombak
And any tools that we can find to help with that are definitely really valuable.

Soroush Khanlou
Yeah. This book is really good at taking all the things that we think about and really formalizing them, giving them names, and giving you a way to talk about it and think about it. I think it's an awesome book.

Chris Dzombak
Awesome.

Soroush Khanlou
Sweet.

Chris Dzombak
I don't think I have anything else to add today. Cool.

Soroush Khanlou
Yeah. There's a lot more in this book. I recommend our listeners go out and check it out. It's a great book.

Chris Dzombak
Cool. And we've added a lot of useful links on subjects that we touched on to the show notes as well. Cool.

Soroush Khanlou
All right, well, it was great talking to you again, Chris.

Chris Dzombak
Yeah. As always, great to talk to you. And thank you very much, everyone, for listening. We'll talk to you in two weeks.

