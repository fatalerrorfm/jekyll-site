Soroush Khanlou
Hello, and welcome to Fatal Error episode 27. I'm, sirish. Khanlo.

Chris Dzombak
And I'm Chris De Zomback.

Soroush Khanlou
And last week we kind of talked about a few different approaches to persistence on our Patreon Only episode, and we sort of touched on why we don't use core data. We kind of brushed past core data, but we want to spend a little bit more time this week talking about why it is that Chris and I will basically, basically never consider using core data for an app from scratch. Is that a fair assessment, Chris?

Chris Dzombak
That sounds pretty accurate. Yeah.

Soroush Khanlou
So there's a couple of nice posts we want to go into a nice talk we're going to talk about and kind of explain our reasoning for why with a new app from scratch, we wouldn't consider using core data.

Chris Dzombak
Yeah. So one of my favorite posts on this topic is actually a comment which Mike Ash wrote on Hacker News three and a half years ago at this point. And it's a comment on a thread titled, should you Use Core Data? And he says the short and easy answer is, no, never.

Soroush Khanlou
That's, like, pretty harsh.

Chris Dzombak
That's pretty strong words and it's pretty harsh. But, I mean, I think he does make some good points in this comment. I don't know, do we want to go through just each point and talk about it?

Soroush Khanlou
Yeah, I feel like a brief, like, reading series, we put the link in the show notes so you could follow along. We won't read all of it, but I think there's definitely some snippets in here that are really, really worthwhile.

Chris Dzombak
So the first thing he writes first, the API is awful. If you want decent model objects in memory, you either have to do a bunch of manual work or use a third party tool like Mode Generator. Even then, the result is a massive soup of mutable objects with no intelligence. So, I mean, this is this is true. I think, like last week, we did mention Mode Generator, which is kind of a necessary tool, I think. If you're using core data, like anyone sane model objects, core data's API pushes you to just have I really like Mike's phrasing here. A massive soup of mutable objects, like just mutability everywhere. And that also leads you to various thread safety and concurrency issues that you have to be aware of with core data.

Soroush Khanlou
Right, right.

Chris Dzombak
And those kind of lead you to the next point or to the next thing that Mike says on this same point, which is that the API encourages passing your entire context around everywhere, which basically turns a whole lot of this stuff into global variables. And that is definitely a huge problem. Right. Like, one of Cordata's goals is to have mutability like, everywhere on all your model objects and also to provide everything with at least sort of a consistent view of what's in that context. And this ends up being hideously complicated. It puts a lot of requirements on you as the programmer who's using core data to make sure that you do everything perfectly correctly with regard to concurrency, which, I mean, you should be doing things right anyway. But it's so hard with core data because there's so much to be aware of. You have to be aware of what reads could trigger a hit that has to go back to the persistent store. It's just so complicated to use that API correctly.

Soroush Khanlou
Yeah. I feel like especially when it comes to threading, most APIs are forgiving where if you accidentally do something on the wrong thread, you probably get away with it and it'll probably be fine. Maybe you'll have a weird bug somewhere. But core data just immediately just like, something goofy happens and everything just shuts down for some weird reason that you can't quite put your finger on. And it turns out it's, oh, we touched this on the wrong thread, tried.

Chris Dzombak
To read this property, and it turns out that you can't do that from a different thread.

Soroush Khanlou
Right. And the fact that sometimes you literally will be reading a property and it will have to go and do a disk fetch for it, which is like, I understand why it does that. Like, it's delaying that. But especially in a world where Apple doesn't want any we don't want to stop the world's garbage collection because it might take a line, might take way longer than we think, and it will be very deterministic. That is, like, how core data works. Like, it'll stop the world, hit the disk, pause everything, and wait for that data to come back, get parsed, and then the code can continue as sort of explained.

Chris Dzombak
Right, so that sort of faulting behavior is what it's called. Right? Yeah. That can lead to weird and unpredictable performance problems. I think that there are ways to rein that behavior in or to kind of control what happens.

Soroush Khanlou
Yeah, there are. You just have to know so much about core data to get it to basically do the right thing that you would want.

Chris Dzombak
That's actually a good point. We've talked about how Swift sort of has progressive disclosure as a design goal. Right. And we can argue about how well it achieves that. Core data does not do well with progressive disclosure. You have to know and understand everything about it to actually use it correctly.

Soroush Khanlou
Yeah, there's a lot to know.

Chris Dzombak
It's a complex it's a very complex framework. It's like a complicated API. Even when you do it correctly, you end up with glorified global mutable stuff all over the place and it's just not great.

Soroush Khanlou
Yeah.

Chris Dzombak
So the next thing that Mike writes is that it ties your on disk representation to your in memory representation way too strongly. And that makes it more difficult to choose appropriate structures or make changes to either one. This actually is something that I feel a little bit less strongly about.

Soroush Khanlou
So to me, this is exactly what Orms do. And this is the problem with Orms is they make a very, very strong coupling between how the table looks and how the object looks and how the relations between the tables look and how the relations between objects look. And so, to me, Realm has this exact same problem. This is just when you make your bed with an Orm, this is just what you got to work with. This is just part of it.

Chris Dzombak
How is this different from, like, with the App database? Let's say I'm using NS coding to write things into the database, I guess. Then you have your coder, which decouples your on disk representation from your actual in memory model. Okay.

Soroush Khanlou
Yeah, exactly. So if you want your coder, let's say originally you were but a young programmer and you didn't know any better, and you stored your date as a string. Right? And that's how your coder works, and that's how your in memory objects work as well. Later you get smart and you realize, oh, I could store this as a date in memory. All you have to do is basically change that translation layer between the on disk stuff and the in memory stuff and just say, okay, well, while you're pulling this out, also go ahead and transform this for a date to a date for me, and you get to decide what that bridge looks like because you get to just write that code.

Chris Dzombak
Okay.

Soroush Khanlou
Yeah. So I think the App database and coding, which we talked about in the last episode, really do solve this problem in a real way.

Chris Dzombak
I guess I don't have too much more to say about this, right? Like, if you're going with an Orm that handles a bunch of this stuff magically for you, this one does kind of come with the territory.

Soroush Khanlou
Yeah. If you get the ability to not have to write that boilerplate, then you just lose that flexibility as well. And tough cookies.

Chris Dzombak
Mike's, third point in this post. It locks you into the technology fiercely. Core data is very different from everything else, and once you build your model layer on it, you're pretty much stuck there forever. Moving away from it is pretty much impossible if you do it. It's a ton of work that reaches into every corner of your app. And I'm paraphrasing him here a little bit, right. But that's also totally true. We talked about how the sort of design of core data and the API encourages you to pass around not just model objects, but sort of this context in which you have to work with the model objects. And it encourages you to have the specific core data concurrency requirements encoded into just the structure of your application everywhere that you're touching any model object. And that is something that is much harder to move away from than a solution that just provides you with boring old classes to work with, right?

Soroush Khanlou
Yeah, totally. One of my clients last year had a stack on built on core data, and it just touches everything we talked about. They were having problems with a couple of different parts of core data, and they wanted to move away from it, being able to pass stuff around and having sort of this thread safety. They were having trouble with the mutability elements of it. They were having a couple of different things. And we talked about how can we get rid of core data? And the conclusion we came to is just not possible. The best thing we can do is build kind of a protective bubble around core data that has the exact interface that we want, and then maybe some point later, years from now, we could totally swap out the innards of what core data does and replace it with something else.

Chris Dzombak
Right. And even that task, building a protective bubble around core data is so hard and so impossible because core data, it just leaks its ideas and abstractions all throughout the app and touches everything. How did you go about even building that productive bubble?

Soroush Khanlou
We didn't. Basically, we just decided to be too tough. The approach that we wanted to take was basically sort of having data source data store objects that you can basically request some predicate or something from it and then just get objects back. But that doesn't solve the problem of, like, right, there's a network as well. And so the network has to write directly into core data, send out an NS notification, and then other objects can update themselves, other view controllers can update themselves. That's a tough thing to fix. It was a lot of stuff, and it was like, is this really going to be possible or feasible in the several months that we have to work together? And the answer was just like, there's just nothing we do about this.

Chris Dzombak
Have you ever moved anything, like, actually moved anything off of core data?

Soroush Khanlou
No.

Chris Dzombak
Okay.

Soroush Khanlou
No.

Chris Dzombak
Neither have I. The closest I've come, I think, is that one of the first iOS apps that I worked on at a startup that I used to work at had been using core data for almost as a cache, which we briefly touched on in the last episode. Is not a good use case for Core Data, but it was using that to provide some offline behavior and as a cache for online behavior. And rather than moving away from it, we ended up just having the parts of the app that were powered by that. We're still powered by that. And as we built new functionality, we used various, like, one or the other different model. So it was just core data plus new stuff for the newer parts of the app.

Soroush Khanlou
Yeah, that's definitely one way to do it. If you don't follow through all the way, you're going to end up with two styles of code in the same code base, and then you're just like right. And you end up with three, and then it's just horrible.

Chris Dzombak
Yeah, no. Nobody wins here.

Soroush Khanlou
Yeah, it's not it's not good. Kids, stay in school. Don't use core data.

Chris Dzombak
Stay in school.

Soroush Khanlou
I wrote a post called Cache Me If You Can.

Chris Dzombak
Okay.

Soroush Khanlou
Which is maybe funnier now with this, like, Cash Me Outside meme. But it's basically about how you shouldn't use core data as a cache, especially if all you're doing is saying, like, I have these objects from the server. I'm never going to have the whole network graph or not network graph, but, like, graph. You shouldn't use core data to store that just so you can use it offline. You should definitely just use something way simpler and just, like, treat it as a cache. And so this post is kind of about that. So I'll link that in the show notes. We don't need to go too much into it, but I just want to.

Chris Dzombak
Mention yeah, but it's definitely a good thing to keep in mind. And as you said, we'll definitely put that in the show notes. Maybe also a link to the Cash me Outside thing in the show notes.

Soroush Khanlou
Yeah, that might be good.

Chris Dzombak
Okay. And Mike's final point here, he says, fourth, it's unbelievably slow. And this is one that I don't know if I've ever really worked with, putting enough stuff in core data to make it to hit it being slow. I think that I've stored maybe 1000 records in core data, like, ever.

Soroush Khanlou
Really?

Chris Dzombak
Yeah. Well, I don't think I've ever written an app that used core data heavily enough to store more than maybe a couple of thousand items in it.

Soroush Khanlou
Interesting. Yeah. I actually didn't know. He says it's unbelievably slow. Literally unbelievable. As in, I tell people about it and they don't believe me. I didn't know it was this slow. So this is actually news to me.

Chris Dzombak
Yeah. And like I said, this is something I can't really talk to, talk about with any authority. So I'm happy to I don't know, I'm happy to give Cordata the benefit of the doubt. I will note that people spend a lot of time trying to figure out what the optimal core data stack is for certain use cases and set up the different contexts to have various relationships to each other. So you're importing data in the right way and it makes its way in some performant manner into your application and doesn't impact the UI. Using it in a way that it is fast is really hard. It's easy to use it and make it slow, even for small numbers of records.

Soroush Khanlou
Interesting.

Chris Dzombak
Which just points to our initial point of discussion, which is that it's hard to do even fairly simple things with it in a correct and fast way.

Soroush Khanlou
Yeah. And you can't even do the thing where since we talked last week, we talked about how we're doing property lists and we were reading things off of the disk and it was being a little bit slow. We just changed it to where we read it in the background and then just pass the objects which are just structs to the foreground and it just kind of works. You can't do that with core data. You have to do it's a whole other thing to make it happen.

Chris Dzombak
Yeah, it's a whole thing. Yeah.

Soroush Khanlou
Not great.

Chris Dzombak
One other thing that I don't like about core data, which Mike doesn't mention here. It requires everything to inherit from the NS managed object superclass.

Soroush Khanlou
Yes.

Chris Dzombak
I don't really want to have to have this God class that contributes to lock in. Right. That contributes to your persistence layer sort of leaking out all across the app. It's a very leaky abstraction. And that means that you can't store swift value types, like swift structure in core data.

Soroush Khanlou
Right. There's just nothing you can do if you want to do that. Yeah, I think if you are going to use core data, you have to basically say core data is going to be the way that I store my objects, but not the way that I work with my objects in memory.

Chris Dzombak
But if you're going to do that, what benefit do you get used from using core data?

Soroush Khanlou
Pretty much none. I'm down to grant that I kind of want to bring up this point of like because it's going to lock you into this thing, you have to isolate it. And I kind of think this is true of Realm or Yap database or NS coding or SQLite or whatever as well. You just have to isolate that part of your app so that it could.

Chris Dzombak
Be oh, yeah, absolutely.

Soroush Khanlou
And so, I mean, I've all long wanted to use code gen for this, and now that we finally have the tools, we can but basically say, I want to pull these objects out of disk off the disk, and they come out as NS managed objects. Fine. That class is going to be code gen for me, either with mode generator or sorcery or whatever. And then I'm also going to have like a struct version or a simple class version. Like if you need reference types, then you would use reference types, but they don't have to subclass from anything because that wouldn't be required and it would just kind of copy the data from one to the other. Now, with core data, when you copy that stuff, you lose all the aspects of faulting and whatever, but fine, it's already slow. And then you get these objects that are yours that they're just bags of data. You can move them around as you want, you can pass them across threads, like you can decide how to use them. And that's the only way I think core data can be basically tenable.

Chris Dzombak
Yeah, I mean, I tend to agree. The thing there is just that, again, owing to the design of core data versus something like Yap Database. It's much harder to isolate core data than it is to isolate Yap database.

Soroush Khanlou
Yeah, definitely. So I'm going to throw in a talk into the Show Notes. It's called Architecture The Lost Years, and it's by Bob Martin, who we've actually talked about before on this very podcast. And it was back in our what episode was that? We talked about the types versus tests. Kerfuffle from a couple of months ago.

Chris Dzombak
I don't remember exactly when we talked about that.

Soroush Khanlou
We might be able to dig it up and put it in Show Notes. I actually think this talk is really good, but he basically talks about if you have a Rails app, your model shouldn't be the same thing as your Active Record Base subclasses, which Active Record Base is the equivalent of ans managed object. It's the thing that you subclass from to get all the benefits of working with the Active Record Database system. And he says that is an implementation detail. Push that out to the side. Your code should be central, and your objects and your logic should be central. And once you have that as central, then you can just replace Rails with Sinatra. You can replace Active Record with Object Mapper, which is another Ruby library that does a similar thing. You can replace each of these components with something else, and your code basically gets to stay the same. And so that is like the only way I think you can use Core data, and Realm for that matter. If you're using Realm, I would definitely still isolate what Realm does. And you lose the performance benefits that we talked about last week that Realm gives you if you use their base classes.

Chris Dzombak
But it's a trade off to consider.

Soroush Khanlou
Yeah, it's more important to me to be able to own the code that I work with on a databases and to understand it from top to bottom than it is to be able to eke out that last bit of performance.

Chris Dzombak
Right. You may build your app and find some situation where you do want to eke out that last bit of performance, and then you can look at optimizing, how you work with your persistence layer. But in the common case, it's probably not worth going there right off the bat.

Soroush Khanlou
Right. Treat it as opt in rather than opt out.

Chris Dzombak
Yeah. So another post that we want to call out here is a post from friend of the show Caleb Davenport, and this is a post that he wrote. Where's the date stamp on this?

Soroush Khanlou
2015. February 2015. So a little over two years.

Chris Dzombak
Man, that really this long ago. This is one thing to call out. I have not actually worked with core data in three years at this point.

Soroush Khanlou
I worked in the last year. It's just as bad as you remember.

Chris Dzombak
Well, I mean, there have been some they did add some way to mass delete a large number of objects right. Or make a change to a large number of objects more efficiently. So there have been some improvements in Cordata, but I think the problems that we're talking about are sort of inherent to Cordata's design. We're not talking about the lack of a way to mark everything red, which was a problem until a year or two ago.

Soroush Khanlou
Right. The problems are a little more foundational.

Chris Dzombak
Anyway, so Caleb wrote a post entitled Ditching Core Data and he landed on a list of features that he wanted in a persistence framework. He wants his objects to be plain objects. We just talked about that. Right? Core Data objects are not plain objects. Realm objects are not plain objects. He doesn't want to have to worry very much about concurrency. I think what he means here is that he wants to be able to read a model object without worrying about concurrency. You will worry about concurrency when you're writing an app, but the Core Data level of worrying about concurrency is just absurd. He doesn't want to write migration code. This is something where, I don't know, like you definitely do end up having to write migrations for Core Data with something like Yap database. I think you kind of end up baking migrations into your decoders. Right?

Soroush Khanlou
Right into that translation layer.

Chris Dzombak
Right? Yeah. Do we want to talk about Core Data migrations here?

Soroush Khanlou
So I actually would like to bring that up. Core Data is not fully smart, but it's a little bit smart when it comes to migrations. So if you add a property to an object so that would be like a column in a database table, it will actually figure that out and do that migration for you and you don't have to worry about it. The problem arises when weird stuff needs to happen. Like if a column needs to change types or if a column needs to maybe be deleted. I don't know if we can do deletions automatically. And anything you want to do custom, like, hey, copy this data over to here using this bit of code. You have to define that yourself. But it is a little bit smart about migration code.

Chris Dzombak
That is true. You do get a little bit of behavior for free there, but that is definitely another thing to be aware of with Cordata. It always seemed really weird that you have to keep around every previous version of your Cordata model in your app.

Soroush Khanlou
Yeah, I forgot about that.

Chris Dzombak
Although that history is going to live on. Let's say if you end up with 30 different versions of a model that you're storing in the app database, your decoder is going to reflect some of that history anyway, just because, well, unless.

Soroush Khanlou
You iterate through them all, decode them and then write them back. But then I guess you still don't know when that will run.

Chris Dzombak
Yeah, you don't know how many. Not everyone installs every app update.

Soroush Khanlou
Right, right. And the benefit here is that Caleb writes, with few exceptions, it is served entirely as a network cache. If it's a cache, it doesn't need to be durable because you can always get that data again. So if you do end up changing the schema, just blow it all away and just start over. Just download the data again. It's just not a big deal.

Chris Dzombak
That's a good rule of thumb in general, not just with core data.

Soroush Khanlou
And yeah, that's how we do our when we have NS coding. If we want to change the schema, what we do is we have like the file on disk is like, there are a bunch of location objects, so we have locations and then we have V Four. And so if we change the end of that has like, cache at the end of it, it's like its file name. If we end up changing the schema, we just change it to V Five. And that other V Four just gets cleaned up. When it gets cleaned up, like, we don't worry about it.

Chris Dzombak
Yeah.

Soroush Khanlou
So the benefit of a cache is databases. They have that acid guarantees or whatever. It's like atomicity consistency, isolation, and durability. Caches do not need durability, they don't need to stay around. User data needs to stay around. But if it's just a cache of something that happens on the server, like, throw it away and just start over.

Chris Dzombak
Yeah. So I don't know that I have too much more to say on this subject. Do we want to talk about are there any situations where Cordata actually is the right choice? Mike Ash says no, there aren't.

Soroush Khanlou
Yeah, I mean, we we touched on this last week. My, my answer is like, there's no situation I can imagine where core data is the right answer and Realm isn't.

Chris Dzombak
Okay.

Soroush Khanlou
Maybe the fact that it's first party, if that matters to you.

Chris Dzombak
Yeah, I don't know. Yeah, I'm really struggling to come up with an idea here of when I would choose to use core data.

Soroush Khanlou
Yeah, I mean, I generally wouldn't opt to use Realm either because while it does fix some of the issues of core data, it doesn't fix all of them and I would rather just write my persistence layer myself. But if I did want those things, I can't imagine why I would use core data over Realm in any circumstance. Maybe if a listener has an idea on a time that core data is just better than something like Realm, tweeted us, email us, and we would love to hear about it.

Chris Dzombak
Maybe if you're worried about the longevity of Realm versus Apple clearly will continue supporting core data for a long time.

Soroush Khanlou
Right?

Chris Dzombak
Yeah. Okay. I don't know that I really have that much else to say. This is like, I guess a slightly shorter episode this week, but yeah, the.

Soroush Khanlou
Big one for me is just don't use this as cash, man.

Chris Dzombak
The big one for me is like, oh, my God, why is it so complicated? You have to know everything to work on it.

Soroush Khanlou
There are there are books that have extensions of, like, how to get an object from core data's cache without letting it hit the disk. And so, like, in certain cases, when, you know the thing has been fetched, you use this thing, and it's crazy how much there is to know about core data.

Chris Dzombak
Yeah.

Soroush Khanlou
All right, cool. Well, that was a fun episode.

Chris Dzombak
Yeah. Always nice to talk to you. Thank you very much to all of our listeners, and we'll talk to you next week. Bye.

