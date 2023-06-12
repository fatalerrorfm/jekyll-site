Speaker A
Welcome back, listeners, to episode six of Fatal Error. Today we want to talk about singletons. We want to talk about what they are, why there's so much, I guess, enemy in the air and why you should avoid them and then how you can avoid them, and a little discussion of how it might fit into other patterns we've talked about as well. So I want to kick it off to Chris. I feel like Chris has a better theoretical grasp of how these things all work together. And so, Chris, how and why are singleton's bad?

Speaker B
Sure. So first let's review exactly what a singleton is to make sure that we're all on the same page. A singleton is a class which is designed for there to be only one instance which is shared among all classes in your program.

Speaker A
So there's a few in the system there's like NS Notification Center, NS File Manager, where you kind of get the default one, or NS Standard User Defaults. Those are all singletons.

Speaker B
Yeah. I was going to use Notification Center as an example, and then I realized it is possible to create a Notification Center if you want one that is scoped just to a certain part of your code base. But you're right.

Speaker A
Third party library, which is kind of a cool trick.

Speaker B
Yeah. Thank you.

Speaker A
So I would add one thing, which is yeah, it's designed to be shared among all the things in your app and like having one instance. But there's also one thing that I think makes it really pernicious, which is when you have a global variable that lets you access it instantly from any object or any bit of code in.

Speaker B
Your app, you mean this sort of the shared instance class method that you might find on a singleton?

Speaker A
Yeah, I would call it like a singleton getter.

Speaker B
That's sort of the defining characteristic of a singleton. Right?

Speaker A
Yeah. I don't think it's necessarily bad to have one class that like a type of thing where there's only one and it's shared among many objects throughout your app or throughout your program. But the thing I think that is problematic is when every class knows how to get that thing and knows how to get that specific one, and they.

Speaker B
Can'T be changed, and that becomes a problem for a lot of reasons. Right. That is a convenient place to share a global state, which I think we generally agree is not a good thing. Like, you probably want to think a little bit more carefully about who owns certain bits of state in your application about who can change that state and how that state gets changed and passed around to the things that actually need it.

Speaker A
Right, right.

Speaker B
That also hurts testability. Right. If you have a class that depends on a singleton and it knows how to just go out and get an instance of this singleton that doesn't allow for dependency injection. Right. So if something just knows to go out and get the default Notification Center. Rather than letting you pass in a Notification Center to use, then if you want to test that object, that depends on Notification Center, you can't test that object in isolation. Right.

Speaker A
You end up testing the Notification Center as well, and you don't really need to do that. And the notifications that you send might have some effect on your actual app, which is like running while you're running your tests, right?

Speaker B
Like, let's hope that nothing else in your unit test suite depends on those notifications or vice versa, right?

Speaker A
Yeah. And in fact, there's one other big problem, which is that this is one of the things I've dealt with a lot, is that the singleton is just so convenient and sometimes kind of poorly named, and it's just so inconvenient to just dump something that, you know a bunch of things are going to need access to.

Speaker B
It's a very convenient, very tempting dumping ground, for sure.

Speaker A
And I wrote a little bit on my blog about why I don't like calling objects. Like, I don't like ending the object naming Controller, because I think it's just a vague name, and I've come across singletons that are just called like, Session Controller or Account Controller.

Speaker B
And it's like Manager is another good name.

Speaker A
Yeah. Manager is the same situation that could just do anything and everything. And so you end up with huge Bloated classes that end up doing way more than they should be just because it's convenient, just because management is breathing down your neck to ship some feature product is breathing down your neck because they have a backlog of features they want to build. And a bunch of angry customers got to help you if you have a sales team that's also doing the same thing. And you got to get the code out the door. So you put it here like, wow, I would love to fix this later, but it's just going here for now, and you end up with this class that's just huge.

Speaker B
And the problem there is that while you might ship something today, quickly, you are shooting yourself in the foot down the road. Like, if this isn't truly something that needs to be a singleton, if this doesn't truly need to be in this global dumping ground, this is something that is going to become very hard to maintain. It's something that's going to be very hard to test, and that makes it hard for you to deliver a good product, right?

Speaker A
For sure. And one other thing is we talked about testing the things that use the singletons, but how do you test the singletons themselves is another part of it.

Speaker B
That is one point. So I have a blog post about designing a non harmful singleton for the real world. Right?

Speaker A
You have a whole domain.

Speaker B
I do have a whole domain singletons info because I have a problem with buying domains but so in one of these blog posts, that is, one of the things that I note is that you should still allow for creation and usage of a standalone instance of whatever class you're creating.

Speaker A
You can block the objective. Yeah, I don't know if you can do this in Swift, but you can block the initializer I guess you can make it private, maybe Swift, but you can do like, NS unavailable or something. And if Alec is NS or Init or whatever, if one of the methods is NS unavailable, then people from the outside just won't be able to even initialize one. All they can do is access the one that you give them access to using the static variable. The static let the singleton getter, as it were, right.

Speaker B
That becomes a problem. Obviously, if you want to test an instance of that singleton in isolation. And allowing use first, like allowing standalone use, encourages design down the road, where you're injecting a properly scoped instance of this class into something that depends on it, rather than having one global scoped instance.

Speaker A
Yeah, that makes a lot of sense.

Speaker B
So Sorish I know you recently had a project where you untangled a web of singleton dependencies. And that's another problem with singletons, is that they're so convenient and they tend to grow dependencies on each other. And so you end up with this web of dependencies that under the hood, all depend on each other, and none of this is exposed in their interfaces. So you pull one of these singletons in and all of a sudden there's a whole pile of complexity and code underlying simple thing that you're trying to do, and none of it is testable well.

Speaker A
And it's sometimes even worse than that. So this app that I was working on was it was almost a year ago now, and there were, I think, nine singletons that were all like, pretty substantial. Yeah, it was a lot. And the interesting thing was a lot of them depended on each other. And normally when things depend on each other, I like to make it more look more like a tree where there's like one clear parent and then that parent has children, and then those children have children, and none of those children ever link back up to the root of this tree. But in this situation, what we had was we made a really small change to the app, which is like, we took sometimes I like to like, if you're using a singleton in a class, I like to extract it and put it as like a property on the class. Like, if you're using, let's say a very simple example would be NS Notification Center. In a class, you would say, like, let notification center equal NS. Notification center, default center. And that's default in swift three.

Speaker B
And that's a good first step toward making your classes that depend on singleton's more testable in isolation without reaching out to these magic global things, right?

Speaker A
You can eventually replace that with a regular property that you can then inject, and then all the rest of the code is already ready to use that code that way, right? So we were in code review, and I just suggested, hey, why don't we just extract this to the top of the class and we'll be sort of off to the races and I can merge this portquest. So the person who was doing the curtary did that, but it was a simple change. So we didn't even run the code. So we merged this branch, and then we go to work on Master and we see that we launch the app, and then it just gets stuck on the launch screen, on the little launch screen. Zib. And we're like, what could be causing that? Like some kind of hang? And so we're like, maybe it's like a compiler ghost in Swift where sometimes you change a piece of code, but it doesn't get reflected, right? And you have to do a total clean and a re build to make that go away.

Speaker B
So I assume you tried a total clean and a rebuild.

Speaker A
So we tried to clean and rebuild nothing. And then we're like, well, maybe it is something in the code. And so we switched to another branch, and the other branch was working fine, and we switch track to Master. Master still broken.

Speaker B
So how did you go about tracking this down?

Speaker A
Like, well, I was really confused, and I was like, the only thought I had was, like, maybe this could be like an infinite while loop. And so what I thought I was like, why don't we just pause in the debugger and we'll see where this while loop is and we can catch it? And I was expecting to see, like, what the mock message trap or whatever it is you normally see while it's, like, spinning idly. But instead I saw that we were caught on one of these singleton getters, and I was like, Isn't that interesting? And so we dug into it, and the stack choice was very, very clear. And it said, okay, well, you were trying to get this first singleton, which tried to get the second one, which tried to get this third one, and it kept going to the fifth one, and then the fifth one referred back to the first one. And because when you do static let, shared instance equals self new or whatever in Swift, that actually takes a lock so that if two people try to access that at the same time from two different threads, it will wait. Like, the first one will begin the process of allocating it. The second one will hit it hit the lock and wait until the first one is done. And then when it's done, it'll have access to the same instance that the first one didn't. I believe every static let in Swift acts that way.

Speaker B
So these static lets for this shared instance of the singletons, which have this circular dependency. You ended up deadlocking just trying to initialize these static properties.

Speaker A
Yeah. By explicitly saying, these are our dependencies, we reveal the circular dependency in our objects.

Speaker B
What did you do to fix this? What did you do to start untangling that?

Speaker A
So the first step was we had to fix Master. And so what we did was we just did lazy VAR, mysingleton Equals, my singleton class, shared instance. We got to get Master working. That's step one. Okay, so that worked. Lazy vard is great. And it would have been a lazy let if you could do lazy let.

Speaker B
But that's not yeah, that would be nice.

Speaker A
Yeah. So we did that, and Master was working again and refactor singletons had been on my to do list for a while, and it just rocketed to the top of the to do list, which was the next thing I worked on the very next day. So we had several problems, right? We had view controllers that were touching these singletons. We had all kinds of objects that were touching these singletons from small to big. We had singletons that had no clear responsibility, so they kind of absorbed a bunch of things, and so they reflected multiple responsibilities. So we had to find a way to break that up. But it was so ingrained into the fabric of the app that if I just tried to break it up immediately, then the app wouldn't compile and I would have to do a really large scale refactor that would touch tons of parts of the code to get this thing to be broken up into this into sensible responsibility. And so I looked at it and I thought about, how can we sell this wrong? One answer is like, well, maybe start building a new stack of dependencies and sort of copy the code from the old to the new, slowly bring that stuff over, and then eventually you'll hopefully be entirely on the new stack, and then you can delete the old code. The problem with that is that singletons, like, they have shared code, but they also have shared state. And if they didn't have shared state, it wouldn't matter if they were singleton, you could just create a new one at each call site, everywhere you needed one. But because they do have shared state, you have to use the same one. That's kind of the whole point. So that solution was sort of out. So we had that problem, and there was maybe a way I could have danced around that. But the thought I had and I actually spent most of the morning just writing in my notebook, trying to figure out, what can I do here? How can I fix this problem without totally upending the entire app? And this solution that I came to is this thing that I call slicing, basically taking small pieces of the giant singleton and slicing it up with a protocol and saying, I know that this singleton does a lot of actions and activities and has a lot of responsibilities, but I'm just going to say, you don't know that this is a singleton. All you know is that this is a protocol that conforms to this very narrow subset of responsibility.

Speaker B
Okay.

Speaker A
And dividing up one big singleton into many of these slices and then that was the first step.

Speaker B
So just to recap, so your first step was to take a singleton, figure out what responsibilities and state it had, and group that into a logical set of smaller protocols, all of which are adopted by that singleton class.

Speaker A
Yeah, pretty much. I started with like one. I was like, well, you know, you're going to need to be able to do this one behavior, let's say get information about the current user that was on a very large singleton. And so I made that protocol and I said, okay, well, when anytime you need the current user, you have to have this protocol, you can't anymore. You can no longer access it via through the singleton, like static getter.

Speaker B
So your intention here is to inject the singleton as a dependency into the things that need it, but to use as the interface for that dependency one of these smaller protocols. A slice of the functionality, right?

Speaker A
Exactly.

Speaker B
Yeah, that seems good.

Speaker A
If you needed to fetch a certain kind of item, you would have a method called fetch available items. And then you have a property that's like fetched items or whatever, so you can get those anytime you need. And that would form the basis of the item fetcher protocol, for example. So I did that and then I started from the root view controller and I slowly worked my way out. And the root view controller, I feel like in every app, the root view controller is always the biggest one. It just has tons and tons of logic. I kind of know why this is, but I still find it kind of weird. But yes, this one was huge and so it needed like seven of the nine dependencies or something crazy.

Speaker B
Were you using Coordinator in this application?

Speaker A
I will come to that. That ends up being an important piece of the puzzle.

Speaker B
Got you.

Speaker A
I had started moving on the road to Coordinators, but I hadn't done it all yet. So, yeah, that was definitely a piece of it. I ended up with like, we had one single thing called a session controller and I ended up breaking down into, I think, four or five protocols. That's how many responsibilities were in this thing. So once you're breaking these things down to protocols, one cool thing is you only need to put the essential things inside the protocol. Anything that's dependent on those essential things can go into a protocol extension. So, for example, if you had like, this item fetcher, right, you would have a method called fetch items, and then you would have a list of fetched items, and then maybe there's like some kind of state on that item that tells you whether it's available or not. And you could have a computed property called Available items that lives on the protocol itself. That code can be moved from the singleton to this protocol. And that thing would just run through every fetched item and only get it would filter out the ones that aren't available for and leave you with only the available ones. And so that code. Now, if you even need that code, you can't get it from the Singleton anymore, unless you reverse cast it back to the protocol that it needs to be, at which point you kind of know you're doing something wrong, and you know you can go back to square one. And inject this dependency the way you should be doing, okay, does that make sense?

Speaker B
Yeah, I think so.

Speaker A
The dependent stuff can go on the protocol extension itself or the protocol's extension, and then the essential and the core stuff is defined in the protocol and still has to live on the Session Controller.

Speaker B
Okay, yeah, that makes sense. That's a solid first step.

Speaker A
It's very solid.

Speaker B
So where do you go from here? Like, did you actually end up slicing your singletons into a bunch of responsibilities and then move on to splitting them up? Or did you try this on just one singleton? Where did you go from here?

Speaker A
So my sort of metric for how this refactor was going was I searched for Shared Controller within the project, and I had, I don't know, 250 references to Shared Controller, and not all the singletons were called a Controller, like some called Manager. So there was a Shared Manager, but my metric was just like, can I get Shared Controller down as far as possible? And I started with only view controllers. So I said, okay, well, I'll search for Shared Shared Controller, and I'll look, if a thing is a View Controller, then I will change its initializer to use to be injected by the specific protocols that it actually needs. So whether it's like the current user protocol or like the Mutable current user, I need to be able to also set the current user. Those are actually two different responsibilities. And so whichever ones it would need, I would put that in the initializer, I would extract that up to properties at the top, and then I would use those properties instead of the singleton getter. And then each time I got rid of a line that said Shared Control or whatever and an angel got its wings is basically how it worked. So that was my next step. And then once I had all these initializers, I basically was doing dependency injection. Right?

Speaker B
Right. So this is probably a good point to talk about ownership of some of these objects. So these singletons previously sort of owned themselves and other objects could reach out to the singletons to get that shared instance. Now you're doing dependency injection. So someone has to sort of own these classes that were formerly singleton. Someone has to be responsible for injecting these into the things that need these dependencies. So how did you work with that in your application?

Speaker A
Yeah, so that's how we get to the Coordinator part. And when I was kind of writing about Coordinators at the very beginning, we talked about this in our first episode when we talked about Coordinators. And I'm glad we did it in this order so that we could talk about this after we talk about Coordinators. But I didn't understand the value of dependency injection at that time. And now that like right, so we talked about how if you have four navigation controllers or four view controllers in a navigation controller, whatever dependency that fourth one needs is going to have to be passed through the third one and the second one and the first one, unless you use Coordinators or some kind of better flow pattern.

Speaker B
Right. And that's just because in standard iOS code, where you have one View Controller creating and pushing another, if you're doing dependency injection, that first View Controller has to have all the dependencies that the second one needs as well.

Speaker A
Exactly. And all the way down the chain when you flip that model into something more sane. And you have View Controllers that are pushed on by one object rather than by many objects you now have centralized where all the View controllers are allocated. And that's in your coordinators. And so your Coordinators eventually, when the Coordinators also need to be tested, they're going to also be injected with these dependencies, which I guess would be set up maybe at App delegate time or something. I don't really know where that should get set up. I haven't figured that part of it out yet. But yeah, they would each then be dependency injected with all the single tints, basically, or all of the dependencies that everything needs. And those are trickled down to the ones that are needed specifically. And so those Coordinators can serve as sort of the object that marshals everything and keeps everything, that kind of organizes all of those tiny dependencies that aren't really View Controllers. But they do have logic. They're not just dumb objects that you can initialize anytime you need. They have state, and they need to be singletons in the old sense of the word, which is that you have one object that many things touch, but without the new sense of the word, which is that we have the singleton getter that lets you just do whatever you want.

Speaker B
Right. So this lets you maintain that sort of singleton essence. Right. That there is this one piece of state, one piece of logic that multiple things touch, but with a much more clear idea about ownership.

Speaker A
Right, exactly. And what we do get is we get that testability. So we get to say, let's say inject this dependency into this view controller and take a screenshot of it, see what it looks like, that kind of thing.

Speaker B
Yeah.

Speaker A
So we got all that testability that we want, which is really, I think, a core thing of what I was after in this. And we also make the dependency hierarchy super, super clear.

Speaker B
Right.

Speaker A
Which was another thing I was after.

Speaker B
And in terms of testability, it really helps that the way that you were able to slice up these singletons initially was into protocols, which gives you a nice point to do dependency injection of a stub of some sort.

Speaker A
Yeah, exactly right. And yeah, you already have those protocols, which is nice.

Speaker B
Right.

Speaker A
And then the other thing that I wanted to do but never got around to was well, so eventually once you've done enough of that and you've eliminated every reference to the static, let the singleton getter shared instance, you can then just delete it because nobody's using it. And you've gone from having this reference all over your app to this reference being nowhere in your app without ever breaking your app with these small sustained steps that slowly get you to where you need to be. Which means that you don't have to do like a catastrophic, like we got to just refactor all this all at once and we don't know how many bugs this is going to surface. It's a very slow and methodical process and that part of it was really important for an app that was like in flight and people were using.

Speaker B
Right.

Speaker A
And then the next step that I wanted to do that I never got around to is those protocols. They represent like a slice of functionality. Eventually they could become their own fully blown types. Either structure class, I wish there was a way to refer to like, I'm trying to make something. I don't care if it's a structure or class, it's not really germane to the discussion. But I think it would have to be a class because this state is shared. But basically they would graduate from being protocols to being their own types. The computed properties that are already on there are good. And then you would add like whatever shared state needed to be there or inject it with something that can manage that shared state for you. And then all the logic that has to do with, okay, I'm going to be the item fetcher can now live on a class called Item Fetcher, backed by some protocol called Item Fetcher protocol or whatever, of which the naming has still not been figured out. And that would have been sort of the next step. And then we would have very concrete individual dependencies and then these abstract objects like session controller or whatever would just finally be able to die out.

Speaker B
Cool.

Speaker A
That was the best way that I could come up with to basically take the singleton that has too many responsibilities, touches too many parts of the app, and is completely untestable. And the code that it touches is then untestable to something where it's much more manageable. Objects are smaller, smaller responsibilities, and the dependencies between those objects are not hard coded into the app and they're more flexible. They can be injected and passed around and changed.

Speaker B
Yeah. I'm really happy that this process involved thinking very specifically and very concretely about what responsibilities these objects actually had and how to break them out into a set of protocols, each of which represents a single responsibility. We've talked about this offline, but that's something I keep coming back to is this idea that of all the sort of solid principles, single responsibility is a very powerful tool for figuring out what objects you have in your app and how they interact. And if you're really thinking in that mindset, so much of your design can fall out of that.

Speaker A
Yeah, I think I would love to do we should maybe do an episode on single responsibility principle sometime.

Speaker B
We probably should.

Speaker A
That would be good.

Speaker B
Yeah.

Speaker A
So as far as singleton stuff, that is more or less my current thinking on it is like, it's okay to have an object that many things touch. A lot of things in your app are going to need that. You're going to need some way to get to current user. And if it's not a singleton object, it's going to be like maybe you'll save it on disk and fetch it from disk fresh each time. And that's also its own kind of singleton that is shared state in a slightly different way, but that has some of the same problems. And again, also not testable if it always looks at the same spot on the disk. Might as well just be a singleton because it's looking at the same spot in memory would be the analogy. That's my current thinking on singletons and how to kind of break away from that scary world.

Speaker B
Yeah, I think that's a really good place to start if you're in that situation where you have a bunch of these classes and you need to start breaking it down. We will link in our show notes to a few posts I've written about singletons and a few other posts that I found interesting or useful when thinking about this or defining a type that is kind of a singleton. There's some useful things to keep in mind and you touched on a lot of these.

Speaker A
Good work. Thank you. There's one post that I refer back to a lot called Sin in Singleton by Ben Sandovsky. And I think that does a pretty good job of breaking down. Like, what really is the kernel of the problem with this thing, right.

Speaker B
Why is this thing that exists and a lot of people use and like UI kit encourages you to use. Why is this a problem?

Speaker A
Well, and it's super easy to fall into the pattern.

Speaker B
Well, and that's the thing. It's not always a problem, but that you can fall into very, very quickly.

Speaker A
Yeah, I've heard they say, like, global state is like, okay, you do it once, you're like, well, it's not really that bad. It kind of works, and it solves my problem, and it's solving the problem that I have at hand, and it's not causing new ones. Okay, great. So you do it once, it's fine. Do it a second time. It's okay, you do a third time. All right. But then eventually the global state starts talking to other global state, and then other stuff starts talking, and there's just no way to control it and have any rigidity or structure around it. And by the time you have your 20th piece of global state, things are out of control. And so I think that's part of the reason that, well, first singleton is really not that bad. You're just, like, creating an API client and network is kind of global. It'll be fine. And then eventually you end up with a thing with nine singletons, five of which are in a dependency cycle and are causing a deadlock in your app. Classic. It happens to all of us. It happens to all of us. I have written some bad singletons in my time.

Speaker B
So have I, but we learn.

Speaker A
Have you learned?

Speaker B
Well, on that note, I don't think I have anything else to add for this episode. Cool.

Speaker A
Yeah, that's about it for me.

Speaker B
This will be a little shorter than our last one.

Speaker A
Our last one was a real hefty.

Speaker B
That was yeah. Cool.

Speaker A
Well, Chris, as always, it was a pleasure talking to you.

Speaker B
Likewise. Listeners, thank you for listening. As always, we welcome feedback. Error FM or on Twitter. I believe our handle is fatal. Error. FM. Is that right, sir?

Speaker A
Yeah, that's right. And I guess we never do, like, a closing, like, what our personal Twitter handles are.

Speaker B
Should we do that? Do I have to spell my last name on this?

Speaker A
Yeah, you know what? We do, because I just want to make you spell and I'll spell my last name because I also will have.

Speaker B
To so my first and my Twitter handle is Cdzomback. That's C-D-Z-O-M-B-A-K. Yeah, and I'm at Kanlou.

Speaker A
On Twitter, so that's at K-H-A-N-L-O-U.

Speaker B
All right, on that note, thank you so much for listening, and we'll talk to you in two weeks.

Speaker A
Sounds great.

