Speaker A
What happened.

Speaker B
I thought it was really good. I thought it was great.

Speaker A
I think that will be a good episode. I'm just, like, so much more confused now. I really am like.

Speaker B
Hello, listeners. Welcome to episode seven of Fatal Error. I'm, Sirush. Khan lou.

Speaker A
And I'm Chris De Zomback.

Speaker B
Today, Chris, I want to talk about the single responsibility principle. This is something that I feel a little hazy on, even though it seems like it's the most concrete of all the sort of solid principles. And I want to really dive in and figure out how. I guess there's, like, a pun with solid and concrete, but I want to understand where you tackle this from and how I should be thinking about this. So what is the single responsibility principle?

Speaker A
Well, first, let me back up for a second. Say, in the little bit of research that I did for this episode, I realized that I'm a little bit more fuzzy than I thought on the single responsibility principle, but I also learned some things. So hopefully we go on this journey of exploration together.

Speaker B
I would like that very much.

Speaker A
So the single responsibility principle is I can say it colloquially as each class or each type should have one responsibility. More formally, the way that I think Uncle Bob Robert Martin, who as far as I know, came up with this as part of the solid object oriented design practices, he states it as, there should never be more than one reason for a class to change.

Speaker B
So I feel like both of those are really abstract. Like, can you give me a little bit more than one sentence?

Speaker A
Well, sure. So let's break it down. So you're designing your application, you're creating objects, interfaces for classes, structs protocols. This is a guideline that says every one of those types that you create should do one thing, should have one responsibility, should represent one concept. Right. And the more formal or, like, original definition, there should never be more than one reason for a class to change. That means that exactly what it says. If you can imagine different reasons that you would have to change the implementation or the interface of a type, then that type probably can be split into two different types that interact in some way or are used by some other type to achieve something.

Speaker B
Got you.

Speaker A
So, as an example, if you're drawing, like, a rectangle to the screen, it probably doesn't make sense for a rectangle that has a width and a height and an area to also know how to draw itself to the screen.

Speaker B
Right, right.

Speaker A
Then changes to, I guess, basic geometry or changes to the graphics interface layer for this whatever system you're programming would cause that rectangle type to change. Right.

Speaker B
Got you.

Speaker A
Yeah. More concretely, you don't want a change in one area of business rules and maybe a change in an external API to both be able to affect the same class. Does that make a little more sense?

Speaker B
It does. It's getting towards the path. But I guess I think one thing that would help me is if we talked about, like talk about actual things that we work with on a day to day basis. Right. It's like UI view, right? UI View has a method called Draw Rect where it literally gets the current context and just like, puts stuff on that buffer. It also has a method called layout sub Views where it decides where the different sub views that it controls belong. Right. Are those two responsibilities?

Speaker A
I mean, I'm not going to say that UI View is particularly well designed.

Speaker B
Right.

Speaker A
Those seem like different responsibilities. Although I will point out that some things, like the actual auto layout implementation is separated out into another constraint solver class. Right. A lot of the actual drawing code is separated out into core graphics land, right?

Speaker B
Yes. Some of it is going back to.

Speaker A
Just sort of single responsibility principle at a high level, maybe before we get into more intense Q and A. So hopefully now we have some sort of kind of intuitive understanding of what this means. Right. It means that if you have some class doing networking and drawing something to the screen, that's probably bad, right?

Speaker B
Right. Yes.

Speaker A
And once you start thinking about this a little more, I find this to be a very, very useful tool when designing some part of an application. Like, if you have a problem and you're approaching a blank slate and you're trying to figure out, how do I break this down? This is a really, really powerful tool, just even if you're not thinking about single responsibility directly, but to think about responsibilities, like, what roles am I trying to model in the system that I'm building? What interfaces should be present to model each of those roles? Do these roles line up one to one with responsibilities? Can I split responsibilities out further?

Speaker B
Right.

Speaker A
And just thinking about the, again, like, business roles and other requirements that you're trying to model and the responsibilities that might collaborate to achieve those goals is like it's a very powerful way, I think, to help you break down a problem. And using the single responsibility principle to figure out when you're done, or at least done enough with that design is really useful for me.

Speaker B
Yeah. When you say, like, done enough, I want something that's like a very specific heuristic. If I'm going to have to apply this heuristic and I'm going to be able to say, let's say, in code review to someone, hey, this violates the single responsibility principle. I need for that to be something very specific and something very actionable for them to say, okay, I understand how this breaks these specific rules that have these specific terms. With these specific definitions, responsibility is just so vague. I don't know, I have a tough time with this and I feel like, I had a tough time with TDD at first, and I was like, it's completely bonkers that anybody could write a test before they wrote an implementation. Like, what would take so much time and how could it ever work? And whether you do test first or test last or whatever is still not I'm not that interested in it. But the idea of writing tests to me was so foreign, and I was like, this just seems impossible. And eventually I got to a point where I think I can do it in an okay way. So it took some time. And I think that there's another thing that's a lot like this as well. Dependency injection. For a while, I was like, why would you ever want to this seems silly. Why would you just inject these dependencies and eventually, as you get more of the testing thing, you kind of have to do more of this. And the thing that seemed, again, foreign and almost impossible and pointless had a lot more purpose, I think. I'm hoping that the single responsibility is something that is more like that, where it's like, I just don't understand it yet. And I'm trying to get to that point that I understand it. How do I decide what responsibility is? Because I feel like you could say layout is a responsibility. You could say drawing onto a context as responsibility. Okay, let's say you break those out into separate objects. Now, UI view encapsulates some interface that calls both of those and brings both those together. Is that one responsibility? Even though the responsibility is really just bringing two responsibilities together?

Speaker A
Okay, so thinking about responsibilities is really the question here. What is a responsibility? How do we tell where one ends and another begins? Right. I'm going to go to this thing that I wrote down while I was preparing for this episode. I don't remember which link this is from, but it will be from one of the links which I will put in the show notes going back to one of the definitions I gave. Let's think of a responsibility as an axis of change. Meaning, like something externally that could change that would cause you to change the implementation of this class. Right?

Speaker B
Right.

Speaker A
Or the interface of a class, I guess. So think about what could change externally that would cause you to change this class. Is it that your business rules about what content should be stored offline in your application have changed? That would be a reason to change a class. But if you have a class that handles storing stuff online and something like iOS networking APIs change, and your business rules about storing things offline change, and both of those changes mean that you have to change that class, then that class probably has two responsibilities.

Speaker B
Interesting.

Speaker A
Does that seem like it might be a useful tool for thinking about this?

Speaker B
I feel like it's getting closer. It's a little bit more specific, but we've kind of swapped out responsibility for what is it reason to change to now access of change. And I feel like we're still a little vaguer than I'd like to be. I don't know. I think part of what this is, is like when you get it, you get it. But there's no one example that kind of like makes it super clear. Like in this paper that the people that came up with this, it's Uncle Bob, this guy Tom DeMarco and Miller Paige Jones, they have this chapter of a book which we'll put in the show notes where they kind of describe it and talk about it. And they use this example of having a rectangle that has logic and properties of how to get the area and separating it out from the drawing of that rectangle. Right, right, that makes sense. But wouldn't that mean that UI label for us, it stores all the properties of the label, like should it have a certain number of lines, what font should it have, what color should it have? But then it also takes that data and it also draws it. So that is a single responsibility principle violation, I think.

Speaker A
So I could see in designing like a UI kit replacement or successor, I could see there being some way to separate out that sort of specification for something like a label and separate out layout of many of these things and drawing these specifications out to the screen. Right. On the other hand, I don't know, maybe the view really does just encapsulate the appearance of a label on the screen. Right. It would be hard to separate out that rendering basically to an image for the screen. Right, yeah.

Speaker B
I feel like you could separate like, this is all the data and then we're going to wrap the data in a thing and that's going to be sort of what we use to actually do the drawing. So, for example, I have in this new app I'm trying using Structs as my model classes.

Speaker A
Right, okay.

Speaker B
And I do need to be able to write these things to disk. So at some point I'm going to need NS coding or if you like, core data. But that can't go in the Struct because Structs are not classes and they're not NS objects and they can't have any of these behaviors.

Speaker A
Right.

Speaker B
So what we end up doing is basically we have like a type that's coordinate and it's just a latitude and longitude double and that's just a Struct. And then we have another thing called encodable coordinate, which is an NS object that conforms to NS coding, takes a coordinate and then does all the work around actually turning this into conforming to Nscoding, basically turning this into data that you can write to disk or do whatever you want with. And I like this. I like the fact that when I look at the coordinate implementation, I don't have to bother myself with the NS coding implementation. It's sort of separate and we have tests to make sure that these things don't break. Like the interaction between these two parts doesn't break. And those tests have saved us, which has been good. But this is definitely more complicated. Like I went from having just throw these two methods in an extension or whatever, to when I have this new type. This new type sometimes has this valid state of it's been initialized with a coordinate that needs to be saved. Other times it's been initialized with a decoder that has to create that coordinate itself. It's definitely more complicated. So on the one hand, I do like keeping this separate and I do like keeping that stuff out of there. But on the other hand, what is it actually buying me?

Speaker A
I mean, so it's more complicated in some use cases, right. In probably the majority of your application, you're dealing with a coordinate, just the structure, which is two fields, right?

Speaker B
Yeah, pretty much.

Speaker A
This does sort of point to something like there's a little bit of what I want to call flexibility here, right? Or maybe not flexibility, but there is a little bit of ambiguity in terms of how extremely you apply this to every one of your types. Adding NS coding to an object maybe is a separate responsibility. Well, no, because that's just tied to that class's implementation. Right.

Speaker B
I think I'm pretty comfortable saying that NS coding is a separate response. Coding coordinate is a separate responsibility than so the primary thing that this struct does, if you really think about responsibilities, like it can convert to and from CL location coordinate 2D objects. But the primary thing it does is it parses JSON because you have to do the JSON parsing in the object if you want to have non optional, non implicitly, unwrapped optional types.

Speaker A
So what I'm thinking about here is NS coding. What would change, what would our axes of change be for a coordinate like class that has NS coding implemented?

Speaker B
Yeah. So let's say we took this coordinate and we added a name property to it, right? So that would change the JSON and so this coordinate struct would change, but then we would also have to change the encodable coordinate. So maybe that's one change, like adding a property is one axis of change.

Speaker A
And that really is the only changes to what a coordinate is, are basically the only motivation for change that I can think of here.

Speaker B
Well, so coordinates don't change too much, and I think that's actually part of the reason they're well modeled as structs. We could add some code here that validates to make sure that okay, well, your latitude has to be between what, 180 and negative 180 and same with your longitude, something like that. So we could add that. But there's a world in which this were a type where those constraints could change. And so even this type, we would be changing for purposes of properties and for purposes of validation or whatever. So maybe the answer then is JSON parsing also needs to happen somewhere else and pass things into an initializer that has all the properties that seems to.

Speaker A
Line up with my understanding right. Is like changes to, say, the format of JSON that you get from a server and changes to how you model a coordinate in your application seem like two different motivations for change. Right, right. So maybe those shouldn't be part of the same type.

Speaker B
So, okay, if we're going to do that and we're going to say, okay, well, JSON parsing happens over here, and it passes everything into an initializer to the thing that all it does is store data, and encoding happens over here and validation happens over here. Isn't that absurd? Isn't that just completely ridiculous?

Speaker A
Well, let's see here. We've identified coding, which I think we agree could maybe be part of the Struct, if Struct supported coding. Right, that's one thing. But JSON parsing validation, I think I.

Speaker B
Would agree with that.

Speaker A
I mean, going back to the fact that the only reason for coding to change is the same reason for this Struct to change, which is I can.

Speaker B
Actually think of another reason for it to change. What if you want to change from my persistence is NS coding based to my persistence is now realm based, let's.

Speaker A
Say that's a very good point. Yeah. That is a different responsibility.

Speaker B
Yeah. And I mean, I think it intuitively makes sense as a different responsibility, too.

Speaker A
Yeah. Then you have to subclass, like, realms, God class.

Speaker B
Right, right. But that's okay because it happens elsewhere. Like our struct stays the struct, and then the encodable struct becomes the realm object.

Speaker A
Yeah, okay, that makes sense. You got me there. So in that case, no, I don't think that's that absurd. Now, the thing is that there's clearly an argument to be made for implementing JSON parsing for a type in an extension. Right?

Speaker B
I don't know.

Speaker A
I don't extension of that type.

Speaker B
I draw a lot.

Speaker A
Isn't this what you were just arguing, that it's absurd to have that all separated out?

Speaker B
So I was going to say putting it in an extension, I don't agree with. So what I was going to say is that I draw a lot of I guess a lot of my thoughts come from the Ruby community I feel like has existed and been large, and they're just a few years ahead of us, basically. Like, Rails got big in 2003, whereas Is development got big in 2006, something like that. Or sorry, 2008 or nine.

Speaker A
This is true. Although I will quickly point out that Rails is not Ruby.

Speaker B
Yeah, that's fine, but it does represent probably 90% of the Ruby community.

Speaker A
Yeah.

Speaker B
And it's like the only reason that anybody cares about Ruby today. It's a very important part of Ruby. But the point is, they've been through so much of this stuff before and this is a real tangent, but basically there was this whole thing where people were like they had their Fat controllers and the Fat controllers became Fat models. And then what people decided to do was take their Fat models and extract what they would call mix ins or modules. And basically you would just say like, I have my user object and I'm going to mix in the validation and the validation is a separate place, but it's not reusable, it's just kind of in a separate place. And there's this quote which is the whole reason I brought this up, which is any application with an app concerns directory is concerning. So I don't think that what goes.

Speaker A
In the app concerns directory.

Speaker B
The different mix ins. Yeah, the mix ins are all basically in there. Okay, I left that part out. I think that's on me. So I basically think like, okay, if you have this type and you're extracting an extension to do like JSON parsing, you're not really conforming to the single responsibility principle you are.

Speaker A
That's probably true, although it's probably I think it maybe is possible to be conforming in spirit in that at least you've extracted. I mean, let's go down the route that you have a struct that you can initialize with properties and you also have a static method that tries to decode a JSON dictionary and call that struct initializer.

Speaker B
Right, right.

Speaker A
And let's say you put that static method in an extension, maybe even in a different file. It could be in a different module if you have your models extracted out into some shared framework. But then JSON parsing is application specific for some reason. The point is that it's possible to put a lot of distance between that struct and its initializer and the JSON decoding. And I mean, at that point you do have these kind of separated out.

Speaker B
I don't disagree with you that it is possible.

Speaker A
It's almost like name spacing, but maybe that's still a little messy. I don't know. I guess I don't have a strong argument one way or another here.

Speaker B
Yeah, I can see the reason for wanting to for name spacing. You're saying if you want to conform to UI table view, delegate everything's in this extension and if you just delete this extension, you'll delete the entire conformance. I can respect that, but I don't think that is the same as building another object with another responsibility. You're not conforming to the single responsibility principle. When you create an extension that does the other responsibility, it's still the same type, it still has access to all the private members of the type or whatever.

Speaker A
Well, not if it's in, right? Yeah, not necessarily.

Speaker B
Not necessarily. But I'm wondering I don't think that's a satisfactory answer to the single responsibility principle stuff.

Speaker A
So we're kind of in the weeds right now, which I know we like, but if we take a step back from the question of splitting up these sort of closely related responsibilities or not splitting them up, are we on the same page in terms of what the single responsibility principle means in general? And maybe we go back to the example of View models which we talked about quite a long time ago, but with the argument that basically we clearly in sort of conventional iOS application architecture. Most of the example code that you see, stuff you get from Apple view controllers have a lot of responsibilities, they have a lot of axes for change, right? A lot of motivations for change. And that extracting some things out into view models and coordinators helps and is in line with single responsibility, even if we can sort of debate whether to continue splitting up view models into presenters or formatter objects and sort of morgue coordination responsibilities. Right? So I think we're in agreement about the usefulness of this tool in general. We're quibbling about exactly how far you go with it.

Speaker B
Right, right. But let's say with presenters, like, I have a very clear argument when I go to someone that I'm code reviewing and I say, look, the View controller is doing this manipulation and transformation for display and it shouldn't be doing that. That is a very clear, bright line that I can draw and say this code belongs in this other type. And that's not as general as the single responsibility principle, but it's something I can go and say this is like a value that we have, which is that view controller shouldn't do data display transformation and we should put that elsewhere. That is something that I can very clearly go to someone and say and if they agree with me on that value, then it's super easy to get them to agree and do this thing on code view. My problem is that even if someone agrees with me on the single responsibility principle in general, we still won't agree on the individual specific cases of like should we break this out? So like you brought up formatters and presenters as part of view models. You could have a view model do something as simple as like take the person's first name, add a space and then add their last name and make that into one string for their full name. That's technically doing some formatting, but that's so simple that would you break that into its own object. And I would argue if you need to test it and there's a lot of weird edge cases, definitely you got to extract that, test it and make it data in, make it data out, make it fast. That makes total sense.

Speaker A
I mean, that specific example so this kind of gets into the don't repeat yourself principle, right, which is another thing that single responsibility relates to, which is that that name formatting is probably something that you're going to do in more than one place in your application. And so it really does make sense to pull it out both because then you have maybe your name formatting rules change somehow. That's a possible motivation for change that is split out into another object. And then if you go to change, it like you have tests in one place and that implementation in one place. Right. We should also give a shout out to falsehoods programmers names article that pop.

Speaker B
That in the show.

Speaker A
Not first name space, last name is wrong in the general case.

Speaker B
No, that's true.

Speaker A
I'm really interested now in sort of interpreting. So I went into this episode thinking, okay, great, so you have like a class and there's one motivation for change and that's great. But how does this apply to the world of Swift and Extensions and Protocols? So what I'm wondering, and I'm going to think about this more and maybe publish a blog post before this episode goes live, maybe single responsibility in Swift means slightly different things. Maybe you have one motivation for change per extension on a type that is still motivated toward achieving one thing. Right.

Speaker B
Okay, I'm listening. I'm intrigued.

Speaker A
This lets me get away with my because extensions can be far apart from the original definition, right? This lets me get away with putting a static JSON decoding method in an extension for a struct. The tests could live in a totally different place. The interface for the pure struct is still intact. It exists. You have to use that initializer.

Speaker B
Here's my beef with that. It's to say that synchronous responsibility principle is not valuable in itself, to me at least, and I hope like to most programmers, it's valuable because it gives you the ability to test stuff. It's valuable because it gives you the ability to reuse stuff. Like small objects aren't intrinsically valuable. They're valuable because they're easy to read, they're easy to test and they're easy to reuse.

Speaker A
What do you mean by not intrinsically valuable then are easy to reuse, test, read, easier for someone to get started and figure out where to make changes, which reduces risk. Right. What would make a class intrinsically valuable?

Speaker B
I'm just saying that basically ease of change is one reason.

Speaker A
Okay, well, I mean, having types that have like one motivation for change per type, that seems to me to imply that something is at least easier to change, right?

Speaker B
Yeah, I think basically each of those points, each of those three things, easy to read, easy to test, and easy to reuse, those are I would call intrinsically valuable. Those properties like you're really putting me to the wire on this one.

Speaker A
This is ask the hard questions here on Fatal Error.

Speaker B
It's directly valuable as opposed to indirectly valuable to me. Making small objects following serial responsibility gets you those three things which are things that you want. I don't want small objects just for the sake of small objects. I want small objects for the reason that I can test them now or I can reuse them now. And extensions don't lend themselves to testing. Extensions don't lend themselves to reuse. And maybe you could argue they lend themselves to being read more easily, but I'll happily grant you that.

Speaker A
What do you mean they don't lend themselves to testing?

Speaker B
Or so, okay, imagine you have a View controller, and one of the responsibilities that you break out into extension is formatting of text, right? So you have some model object on the View controller itself. You pass that in the initializer, and then you check these properties for whatever, right. You're still just testing the View controller. You're not able to, let's say, inject a protocol based user, you're not able to let's say it doesn't even accept user. It accepts like it requires you to it takes an ID and it requires you to go to the network, get the user and come back or go to the cache, get the user. And now you're testing the cache in the network and you're not testing the ability to that's why extensions aren't testable.

Speaker A
Well, this is where I'm thinking like, okay, have we just flip flopped on this?

Speaker B
What happened here? I feel like you were defending now I'm defending it.

Speaker A
I'm trying to allow myself to do a thing that I think makes sense, which is put a static decode from JSON method in an extension on a struct.

Speaker B
Right, okay.

Speaker A
I'm trying to come up with a general principle that lets me do that. Right.

Speaker B
Yeah.

Speaker A
I'm not going to defend adding formatting code as an extension on a View controller. Right. I will try to defend adding some what principle can I go with here? Is it like identity? It's like functional?

Speaker B
Oh, referential transparency is what you're thinking of?

Speaker A
I think I'm thinking of like a whole bunch of I'm thinking about anything I can use that feels like the right general principle. Right. But it's working toward the same goal as the user class. Right. Or as the user struct. Right. As the coordinate struct that we're thinking about, maybe. Whereas adding presentation to a View controller is not working toward the goal of a View controller in as much as a View controller has a goal. Right?

Speaker B
Right. So I think I would disagree with you there by saying, okay, so let's say you've added your static JSON decode method to your extension. Now, let's say you've added your NS coding stuff in an extension, and now you've added, let's say, your formatting stuff in an extension. You add your network stuff in an extension. Where are you going?

Speaker A
I don't think you add all that in an extension. So that's a question that has to be answered is like, where do you stop? Or really, what's the general principle that dictates where you stop in any given.

Speaker B
Case where I'd be happy to land on where you stop is like, do as much as you need. If you need to break out presentation code or data transformation code for testing, break that out. If you need to break it out for reuse reasons, break it out. If you need to break out your, let's say, encoding stuff for testing, do that. If there's a reason to do it, do it. Don't be shy.

Speaker A
So where I'm landing is like, I'm okay, have to find justification for this, right. To help me with this.

Speaker B
Sure.

Speaker A
I'm okay with adding static decode function in an extension. Maybe it's not okay with adding formatting. I'm not okay with adding networking.

Speaker B
Right.

Speaker A
What's the line here? What's the principle that separates these?

Speaker B
The only thing I think of is that JSON decoding is very small, which.

Speaker A
Is simplicity is like too big.

Speaker B
I can't think of it's functional.

Speaker A
There are no side effects.

Speaker B
There's no side effects with formatting. Formatting, yeah.

Speaker A
One is like view specific. One might introduce a UI kit dependency. All right, we're so in the weeds right now.

Speaker B
So there's definitely one other thing I want to talk about, which is protocols.

Speaker A
Okay. Yeah.

Speaker B
So in this PDF that we link in the show notes, this is chapter nine of some book or something that Robert Martin and these other two people wrote. He shows an example, or they show an example of basically like modem Java, which is an SRP violation because it has methods for dial, hang up, send and receive. And he's saying there's two responsibilities here. First is connection management, second is data communication. And he wants to separate the responsibilities. And he says it may not be perfect, but one thing you can definitely do is make two interfaces which are in Java, the same thing as protocols are in Swift. One for the data channel, which has the send and receive methods, and one for the connection, which has the dial and the hang up methods. And then the modem implementation conforms to both of those. And he's saying that this is also good in a single responsibility way.

Speaker A
Yeah, let's talk about it.

Speaker B
So if you made your model just a protocol, right, and then you hydrate your object from NS coding or from Realm or from JSON, it doesn't matter what the implementation is. It just matters that it has a property called latitude and a property called longitude. And is that maybe a better way of thinking about single responsibility principle is single responsibility protocols. Single responsibility protocols, which we kind of talked about last week.

Speaker A
Which we did.

Speaker B
We did.

Speaker A
I don't know that it's necessarily better or worse, but it's certainly probably very useful in Swift, right, or in Java or anything.

Speaker B
Yeah, I would agree with that.

Speaker A
And that's where I know I've been saying interchangeably, like class and types. When we're talking about single responsibility principle, a lot of the original stuff here is talking about Java, talks about classes directly.

Speaker B
Right.

Speaker A
I'm thinking more about interfaces that should have one or types generally, which includes protocols right. That have one motivation for change.

Speaker B
I'm certainly not going to deem you for using class to mean class structure enum. I'm not worried about that. I do kind of think protocols are a little bit different.

Speaker A
I'm going to say, like, types more generally, your interface should have one motivation for change. Right. But also implementation.

Speaker B
Yeah. Well, programming is really hard. I don't know if you've ever thought about it, but it's hard.

Speaker A
It is.

Speaker B
Yeah. I feel like we've gotten we've teased out some of this stuff. I feel good about what we did here today. I think we helped a lot of people.

Speaker A
I don't know if I feel good. I feel like I'm more confused now than when we started.

Speaker B
Oh, no.

Speaker A
I'm going to have to go back and really think hard about what single responsibility principle means in the context of Swift. Do we mean that each interface for a type meaning protocol, class struct enum has to have one motivation for change? How do extensions play into this? Do we mean that this applies to the implementation more so than the interface? I'm so confused now.

Speaker B
I have done this to you, and I apologize.

Speaker A
That's okay. I'm going to try to figure this out and maybe blog about it if I figure anything out before this episode airs. But coming back out of the weeds in general, when you're trying to solve a problem, when you're trying to model the solution for something you're doing in your application, it's very useful to think about what business rules you're trying to implement, what sort of roles different objects might take in working toward achieving this goal. And a useful way to do that is think about what responsibilities are at play and how they interact with each other. That's really going to drive how you design your interfaces. And if you think about things in this way, you're going to end up probably with more types or with more interfaces, which is a good thing. Those are going to be more reusable, easier to change in a low risk manner and more testable, and you're going to end up in a happier place. Even if, like me, this is actually like, this episode ended up being more confusing than you had hoped for.

Speaker B
Yeah. The basic principle of, like, if you need more types, make a lot more types. I think I would say most programmers err on the side of too few types rather than too many. But I could see how this could slippery slip you into too many types, which is my new show on Netflix.

Speaker A
Setting aside that the Too Many Cook song just started playing in my head, I would say that I'm generally not very worried about too many types. That's not a problem that I've seen too often, and I see the too few types problem all the time.

Speaker B
Right? Yeah, exactly.

Speaker A
It's apparently not a very slippery slope that's true.

Speaker B
What trick I want to ask you about, Chris, is basically like constructing your project in such a way that things can't obtain more responsibilities than they deserve. And so a lot of this comes into play with naming. We talked about session controller last week. If we had renamed Session Controller to just Session, you just wouldn't be able to add the controller parts of it. That is an example I bring up in one of my blog posts is Music Library Controller versus Music Library. And then like, library queue and player queue items or whatever, however you want to break that up. So naming, I think, helps a lot in preventing you from, like, encodable coordinate. I will never add formatting code to encodable coordinate. It would be ridiculous. I would look at it like, this.

Speaker A
Is just wrong, but maybe you can add JSON parsing in an extension since that just gives you a coordinate.

Speaker B
Well, so think about this. Why would you just not make it a free function? We just went back into the weeds.

Speaker A
Out of the weeds. We're like out of the weeds. Right on like 40 minutes on this episode, I think we're getting up there. I thought this was going to be a fast episode.

Speaker B
You thought wrong.

Speaker A
Oh, my God.

Speaker B
It's a tricky one. It's not as straightforward.

Speaker A
Going back to your point, I can't believe I didn't even think about bringing up naming. Naming is so important and it's hard to come up with a good name unless you actually have thought about what the responsibility of the type you're naming is. Right.

Speaker B
I sometimes put all the stuff in the type and then name it, and then the more specific the name, the better.

Speaker A
Yeah, that absolutely works. Or if you know what you're modeling, giving something a good name from the get go, like you said, it really does limit you to putting things that adhere to what this class is or what this type's responsibility is. Yeah, that's such a good point. Names to watch out for things, as you mentioned, like Manager Controller, tend to be a little bit more dangerous because what's a manager do?

Speaker B
Well, those all kinds of whatever it wants.

Speaker A
Yeah, that's such a good point. Thank you for bringing that up.

Speaker B
We should wrap up to respect our listeners time and their attention as well.

Speaker A
Yeah, I'm just going to keep going in circles for the next several weeks on this.

Speaker B
I'm sorry I've done this. I apologize.

Speaker A
No, it's good. I will come out of this with a better understanding once I figured out.

Speaker B
So thanks to all of our listeners, thank you being here.

Speaker A
Thank you for listening. For the three of you who stayed through this entire.

Speaker B
Thank you, Chris, for talking through this stuff with me.

Speaker A
This turned out to be so much more invest than I had anticipated. Thank you for listening and we will talk to you in two weeks.

Speaker B
Sweet. Later chris.

