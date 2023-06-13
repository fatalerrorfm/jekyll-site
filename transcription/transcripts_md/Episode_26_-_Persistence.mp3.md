Speaker A
Hello and welcome to Fatal Error. I'm Sirous.

Speaker B
And I'm Chris.

Speaker A
And today we want to talk about persistence.

Speaker B
Yeah. We realized that this is something that we hadn't actually talked about on the podcast yet, and we thought it may be interesting to go over what are some of the, like, concepts that we think about when we think about persisting data for our iOS apps? Like, what are we trying to do? What are some of the common approaches, all the from user defaults to core data to third party persistence solutions. I feel like there's a lot to talk about here and we don't really have an outline or anything. So let's dig in. Where do you want to start?

Speaker A
I would love to know you're working on an app. It's the New York Times app. What do you all use for persistence?

Speaker B
So in this app, we decided to go with Yap database and we'll have links in the show notes to all the persistence solutions that we discuss in this podcast. Of course.

Speaker A
Right.

Speaker B
We chose Yap for a couple reasons, which I can delve into if you want to hear.

Speaker A
I do, because we are actually looking at graduating from flat files of NS coding to something better than that. And since we already have our NS coders, I was thinking, yeah, it might be a good fit, but I would love to hear some on the ground experience.

Speaker B
So especially if you're replacing flat files, the updatebase may actually be an interesting thing for you to look at because it's modeled as a key value store. It's not a it uses SQLite under the hood to write things to disk, but you don't worry about that. You're looking things up by like, by key. And so if you're trying to migrate from some sort of, like, I don't know exactly how, you have files structured on disk that could translate nicely into Yap database depending on your data model.

Speaker A
Yeah. So right now the way it works is we just tell NS keyed archiver to write, let's say, an array of location objects to a file, and that file just basically acts as a cache for some stuff from the web.

Speaker B
But your intention is to look up or to use those location objects maybe independently of each other.

Speaker A
Yeah, ideally we want to be able to filter them. We have about 2000 right now, which is just enough to where it's like, okay, you can't really store us in memory anymore. We're having trouble putting it bring it all over the wire. Reading it, especially in certain circumstances, is taking several seconds reading off the disk. So 5 seconds sometimes.

Speaker B
Okay.

Speaker A
And so we want to do something where we say, you're looking at this part of the map, just give us these locations.

Speaker B
Okay. So another thing that you'll keep in mind with the app is that it's not necessarily just a key value store. You can also put keys in buckets, which are called collections. So each object in the database needs to have a key that identifies it. And that key only needs to be unique within a given collection. So you might have a collection of locations or a collection of, say, that is some bucket of locations that you're interested in.

Speaker A
Got you. Does that kind of correspond to like, a table?

Speaker B
It kind of does, yeah. Although this isn't something that you're thinking about under the hood. I think that Yap actually writes, at least by default, it serializes things with NS coding as like blobs of data that get written into SQLite. But you can think of a collection and collections and keys, I guess they're not really like tables because everything in a collection doesn't have to have the same schema. So you can have objects of varying different types in a collection.

Speaker A
Right. And can I index based on, let's say index based on, let's say, the latitude and longitude. So I can filter and say I only want things that are in this range of latitudes and longitudes.

Speaker B
You can do that, yeah. So since Yap is built on SQLite, it does provide an API free to create indexes and index those objects even though they're being stored as blobs of data. You can also tell Yap database how to create SQLite indexes for fast lookups of things.

Speaker A
That's pretty cool.

Speaker B
It is really cool. And I think there may also be an extension for dealing with geo like geographical data more nicely in Yap database. I'm not sure if I'm making that up, but if there is, we'll put a link in the show notes.

Speaker A
I saw that there was like an extensions section of their README, but I wasn't sure what all cool stuff you could do to it. So I'll have to definitely check that out.

Speaker B
Yeah, absolutely. So one of the other things that I liked about Yap databases is very extensible. It's a simple model. It's a relatively simple framework. The mental model that you need to keep in mind while using it is quite straightforward, even around things like dataflow and updates. Again, depending on how you model your app, you can choose to go with Immutable or Mutable models, but you can use the app database in a very simple, very straightforward way. But it's also extensible. So these extensions that you mentioned that you noticed let you bolt on all sorts of extra behavior and functionality. The indexes that I mentioned, for example, are actually implemented as an extension of Yap database. You can also create things called views, which you can use to map your Yap database into something that is very nicely compatible with UI table view or UI collection view. And that's also a Yap database extension.

Speaker A
Nice. That's pretty cool.

Speaker B
Yeah. So that's something to check out. A couple of other reasons that we liked Yap database. I'll go over two more points here, and then you can talk about something.

Speaker A
No, go for it.

Speaker B
We liked that you didn't have to inherit from a God class some magical superclass to work with it.

Speaker A
Right. Like core data? Is NS managed object or active records like base class?

Speaker B
Right. Or Realm I know, has a similar base class that your models have to inherit from.

Speaker A
Right.

Speaker B
The only requirement that Yap database makes is that you have to be able to encode your model objects to data somehow and decode your model objects from data somehow by default. That's going to be via NS coding. Although you can also plug in your own encoding and decoding solution if you want. For some reason, you want to use custom serialization, go for it.

Speaker A
That's pretty crazy.

Speaker B
So this meant that we could use swift value types in our application with the addition of some adapter classes that take care of the coding and decoding part, like for NS coding compliance. But outside of our sort of persistence layer, everything in the app is just dealing with immutable swift structures, which is really nice and which is something that Core Data or Realm couldn't support for us.

Speaker A
Right. Realm, since it relies on subclassing, relies on using classes. So you can't use Structs at all, right?

Speaker B
Well, yeah, I don't think Core Data you have to have a managed object subclass too, right? Unless something yes, you have to. Unless something very big has changed since I last used Core Data.

Speaker A
No, you do. The only weird thing that you can do is you can use transformable properties where those can be conformant to NS coding, but they have to be like a child property of an NS managed object.

Speaker B
Okay. Interest. That's right. Yeah. And the last thing that we liked about Yap database that really drove that really drove me to pick Yap database for this application is that you can also create relationships between, not just entities in Yap database. So you can have a relationship between two things in your database that say, when this object gets deleted, this other object should be deleted. And it's almost like a reference counting sort of relationship. But you can do that between or from things in Yap database to files on disk.

Speaker A
Weird.

Speaker B
So you can say, this entity in Yap database owns or is the parent of or has a relationship to this file on disk. And so when you delete that entity from Yap database, that file on disk goes away.

Speaker A
So, like, a concrete example of that would be if you have a Tweet object in your database and you tie it to some piece of media, like a photo that it's attached to, when you delete the Tweet, it'll also delete the photo.

Speaker B
Exactly. Right. Because let's remember, this is still a SQL Light database. You probably shouldn't be writing, like, three megabyte blobs into it.

Speaker A
Right.

Speaker B
It's still a good recommendation, or it's still a good practice to keep your large binary data blobs. Like photos, movies, et cetera, on disk. But so this provides a really clean way for you to create these relationships and make sure that things aren't orphaned on disk after something falls out of your database.

Speaker A
That's pretty cool. Now does it work in reverse as well? So could it use something like FS watch to see if the file is deleted and then delete the element out of the database as well?

Speaker B
No, it doesn't. Watch the file system to delete things from the database. Although you can have these relationships go either way between entities in the database, but you can only have an entity in the database that quote unquote owns something on disk, not the other way around.

Speaker A
Interesting. Yeah. Our app is really similar to yours. We have structs, those structs have code generated encoders that will basically conform to NS coding and do that translation for you. And then we just like, let's say we have an array of locations, we just write that to a file. But this seems like a natural evolution to that. I think this is probably like the direction we want to go in. The other really nice thing about this, I feel like this is kind of the way I would write it and so I feel like it will make sense to me in a way that something else might not since I'll be like, oh, I might have done some basically this is a hack ultimately, right. Like you're abusing the fields in the database table to store the whole object and then also adding indexes and whatever else you want to add to it on top of a database that wasn't kind of intended to be used this way. But this feels like something that I would do. So I feel like I would really naturally, I feel like I would understand it.

Speaker B
It seems straightforward, it seems easy for me to understand. It seems to match up with right. It seems like a sane implementation from my point of view. And while you may be kind of sort of abusing SQL lite in this way, you also, let's remember, can create indexes in SQLite to enable fast lookups without iterating over everything. Right. You're still taking advantage of SQLite's write ahead logging capability that it does and all the fun things that databases do under the hood, right?

Speaker A
Right.

Speaker B
So you're still getting some bang for your buck here.

Speaker A
Yeah. But ultimately SQL requires a schema and this is basically schemaless.

Speaker B
That is true. Yeah. This is your NoSQL database for your iOS app.

Speaker A
Yeah. It reminds me of there's this really cool post about how Friend Feed does basically this exact same trick with MySQL. And they had, like I'll put the link in the show notes, but they basically had 250,000,000 entries in their database. And every time they went in to add an index, they had to lock the table and index all this data. And it became really expensive to change their application. So they did all these crazy shards and read slaves and all kinds of other stuff, and they realized eventually they're like, you know what? Why don't we just store the data as, like, JSON in the database and then add our indexes as I think they add their indexes as separate tables. And so the adding of the index is actually totally separate from the data itself. So you can create indexes super, super.

Speaker B
Quickly and then I assume that they get populated asynchronously once that index is created then yeah, exactly.

Speaker A
It just sort of like figures itself out. The blog post goes into some detail. My understanding is there are some trade offs here, but basically it seems pretty good to me.

Speaker B
Interesting. Yeah, I'll have to check that out. As long as we're talking about schema lists like server side databases too, I'll throw out a call out to PostgreSQL. Postgres.

Speaker A
Postgres.

Speaker B
Yeah, which a while ago added some native features to support storing Schema list JSON and dealing with it in some neat ways.

Speaker A
Interesting.

Speaker B
I haven't actually used this, but if this is something that you're considering, I would highly recommend that you check it out.

Speaker A
Does anybody use Postgres on the client? That would be a cool idea.

Speaker B
I don't know. My gut feeling is that it's probably like overkill because if you have just one reader writer then I don't know, then sequel lights more well suited to what you're trying to do, but yeah, I've never heard of anyone doing that.

Speaker A
Yeah, me neither. Seems like a pretty crazy idea, but I don't know. But yeah, I would pick if I were doing server architecture, I would definitely pick Postgres. It seems like the most stable and reliable thing whether you choose to have a schema or not. I mean, I feel sold on the app database.

Speaker B
I'm not going to say that you absolutely should use it over all other solutions, but I think we're pretty happy with it so far and I think it deserves a look.

Speaker A
What downsides does it have?

Speaker B
So one of the things that I was going to mention is if you are looking to store Swift structs in it, there is some boilerplate that you have to write or maybe code gen now with sorcery but there's some boilerplate that you will have to write for those encoder and decoder classes.

Speaker A
Right. So we already have those, so that's done.

Speaker B
Okay, so that's definitely a downside. I honestly can't think offhand of any big downsides that we've hit so far. Maybe if you do have data that you're storing in the client that really lends itself to having a well defined schema and maybe is highly relational, then this is not the choice for you. Right. Something like core data does handle through faulting, et cetera, does handle going back to the database to look up other related entities really well and that's just not something that Yap database is going to do for you.

Speaker A
Got you. Okay.

Speaker B
So if you use something that's highly relational like that, then core data might handle things more nicely. Although using core data correctly is kind of a pain. And we've discussed the possibility of doing a core data good or bad episode at some point.

Speaker A
Yeah, I think we absolutely should do that episode.

Speaker B
So that is one downside. But all in all, I have to say I'm a fan.

Speaker A
Nice. Cool. So yeah, it sounds like if you want some of the ultimately, I guess let's talk a little bit about realm and core data and maybe some of the ways that Yap works while I come out and we can I was.

Speaker B
Going to say so we've talked a lot about Yap database and also somehow server side databases so far. Let's talk about some other approaches to data persistence that you can take. And first of all, I'll call out quickly. You've mentioned just writing things to disk just as archived files. This starts to fall down. Well, do you want to give a really quick overview of when and how this starts to fall down?

Speaker A
Yeah, sure. I feel like one of the things I've been doing with new apps is or trying to do, trying to get good at is only use the bare minimum for what you need. So when this app started, it was like 20 locations that were coming out of one single JSON file. And if it were even less than that, I might have even started in user defaults. Right. I've built extensions that will basically take some NS coding thing, translate it to data, and then store that data in user defaults. And if you have under 20 items, that's super not a big deal. So I might start there and then at a certain point you realize, okay, well, this isn't going to suit our needs. So you want to scale it up one level. So the next level above that I would say is this would go up to several thousand items, which is about where this app is right now. Several thousand items. Let's just take all the items, store them in memory, and then save them to a file on disk. So NS Key to Archiver has a really simple API for just saying like, hey, take this object and all of its children and everything like that, or this array of objects and all their children and write it to this file and you give it a path and it just takes care of it for you. This scales pretty far, honestly, like up to thousands of items. This pretty much just works. In fact, the bigger bottleneck that we're hitting is we're actually serving all of our data in one big JSON file from the server. And that's like a two and a half megabyte download each time. But you can imagine that means we don't have to worry about Pagination. There's a lot of problems it solves, but we're hitting the limits of like two and a half megabytes per request. It's like a bit high.

Speaker B
Yeah, so that's quite a lot. And then the other downside, as you mentioned, is that you're keeping all this in memory. You're reading the entire data set from disk at once and trying to work with it and write two megabytes. That's not that bad to deal with, but you're starting to maybe find some bottlenecks.

Speaker A
Well, and the trick to remember is like, okay, let's say you download the JSON. It's like JSON plus little metadata. So it's like whatever the strings are plus the metadata, call it three megs, whatever. Not only do you have that in memory, but you're also translating it to these encodable objects in memory, which have these like structs, right? So that translation, you're actually holding two copies of everything in memory at once. So that could be a lot. That being said, I mean, it's not an image, it's a bunch of string data. If it's ten or 15 megs in memory, like our phones have a gig of memory, it's probably going to be fine. But yeah, we're hitting these limits of like now with this single file, we're hitting the limits of well, in certain weird cases, it's taking up to five and 6 seconds to read off the disk the very first time, I guess before the caches are warmed up, I assume the disk has a kind of cache. And so it's time to start thinking about options beyond that. I would say if you can get away with it, just store everything in user defaults. Once you get beyond 20 items, then start to think about flat files, which takes you pretty far. You just do all your filtering and memory and it's really not that big of a deal. And then once you get beyond that, then it's time to start thinking about some of these more advanced persistence options.

Speaker B
So the first persistence option that you're likely to run into that you're likely to find as an iOS developer would be core data.

Speaker A
Yeah, that's the first party provided persistence framework.

Speaker B
And that's a huge thing to jump into right off the bat, like coming from flat files to core data. So I know that this got a little bit better with was it iOS ten when they added the like, what's a new API? That's like a core data stack that you can set up easily.

Speaker A
Right? So there's NS core data stack, which is pretty recent. And there's also like you can now batch update and do stuff like that. Batch update, batch delete. And so those are all pretty recent.

Speaker B
I was thinking just of the core data stack just because setting that up honestly was such a pain point, especially for someone who's new to core data and was trying to figure out how to store stuff in their app. Just getting a stack set up and working was nontrivial. And once you have this working, the Xcode Data modeler works fairly well. You have to deal with getting your model classes written and synced up with a data model. Or does that happen automatically now?

Speaker A
I think that part is automatic, but you have to set up the Persistent store coordinator. The persistent store, it's a pain in the butt.

Speaker B
I haven't actually used Core Data in a couple of years now. So the last project that I used Core Data on, we were using Mode Generator, which is a great tool if you're working with Core Data. And so I don't really know if you have to use something like that now to keep your data types in sync with the Core Data model or not.

Speaker A
Yeah, so there's two components there's. One is like when your app is launched and Core Data reads, it reads the model file, which is like a big XML file, and it makes the schema of the database line up with the thing it reads from this XML file. That's one thing. But then also your classes have to map to that schema. And there's no autumn, it doesn't do that automatically. You have to type in each property manually, unless you use something like Mode Generator, which will code gen those classes for you.

Speaker B
Right, and that's what I was thinking of. And I mean, again, especially if you're new to the framework, that's just super weird and seems messy. Right?

Speaker A
It's super intense.

Speaker B
As with many things that code gen can solve for you, that's something that's tedious and boring and where there's room for error to creep in.

Speaker A
Yeah. So I found the core data stack class. It's new in iOS Ten. It's called NS. Persistent container.

Speaker B
That's it. I didn't think it was actually called NS core data stack.

Speaker A
Yeah, somebody told me it was just called NS Core Data Stack, and that was wrong. But yeah, it's called NS specific ethereum. You give it a name and then you can start working with it. Done.

Speaker B
And so once you start using Core Data, then you get exposed to all the sharp edges that come along with it. And we'll cover this more in our Core Data episode, since we're already at maybe 24 minutes right now. But suffice it to say that there are a number of sharp edges that come with using Core Data, kind of because of some of the design constraints and goals that come along with Core Data. Core Data tries to give you a consistent and always updated view into the database in all your model objects. It tries to update things for you in near real time as things are changed. And as it turns out, that's a hard thing to do, especially when all your models are also mutable. Right. This turns out to be a just giant ball of complexity that you now get to deal with. Congratulations.

Speaker A
Well, and don't forget, it's not threatsafe.

Speaker B
Well, right. Yeah. Right. So in addition to trying to provide a consistent view of the world to everybody and everything and provide all this nice faulting behavior, it's not, generally speaking, thread safe. And so you have to do things very carefully, anytime, anywhere that you're say, adding 2000 locations to core data from a 2.5 megabyte JSON response in the background.

Speaker A
Yes. And there's a lot of weird tricks you can do around there's people that are better at core data than us that you should go learn from. But there's all kinds of weird tricks you could do. Like you can make one thing a background context and one thing a foreground context and only use the background one for writing and only use the foreground one for reading. And this makes sure that things stay fast. There's a lot of weird tricks you can do. It does work. A lot of people do use it. There's a lot of help on the Internet for it, but it's got a lot of sharp edges and it can be frustrating in a lot of ways. Yeah, I tend to shy away from it these days.

Speaker B
As I said, I haven't used it, I don't think since maybe 2014 at this point. Is that even possible?

Speaker A
Yeah, seems reasonable. I think I've used it since 2013. No, that's not true. One of my clients used it and there was a lot to deal with there.

Speaker B
Yeah.

Speaker A
The other thing that I would be remiss if I didn't add is a lot of people use core data as a cache. So they'll get objects from their JSON, from their API and then they will kind of take each schema and map it to a table and then save those objects in the table. Right, but if you're just using this as a cache, there's I think, a couple of problems with that. One is that you don't have these relationships set up of like, hey, what does it mean that if I download this and a fresh piece of data comes in, like if this child doesn't update, are these things now out of sync? There are deletion relationships here that we talked about with the app, but there's also deletion relationships in your core data stuff. I find with the cache, it's much easier to say, here is the new version I just got, blow away the entirely, blow away the old version, take this new version and replace it entirely. And that way we know we always have a consistent view on the world as judged by the server.

Speaker B
Right.

Speaker A
If you have an app where all of the users data is on the device, core data maybe makes more sense because you do have the entire data set at any given time. But if you use it kind of as a cache, you could end up with objects that you have, let's say an ID to a reference to, but that don't exist in that other table. If that makes sense.

Speaker B
Well, I mean, that's true of any sort of persistent solution that you're using as a cache, right. You're going to have to deal with missing IDs occasionally.

Speaker A
Right. But I think if you're using as a cache intentionally, it's much more obvious and those boundaries are more sharply drawn and so, you know, whereas if you're just using it as like, oh, it's just a table, and let me just bridge over to this table and oh my God, the data is not there. I think that's a big part of core data and a big part of the mistake of core data is if you're just using it as a cache for JSON API, there are a lot better solutions than that.

Speaker B
Absolutely. Yeah. That is one thing to note is that core data is clearly designed to be like your application's data store, not to be a transient cache for parts of your application data.

Speaker A
Exactly.

Speaker B
So one other thing that we probably should discuss before we wrap up would be Realm. And this is something that I actually haven't worked with and haven't even looked at too hard. Back when we were choosing a persistence layer for this app, the fact that it required inheriting from a god superclass was a problem for me and so I didn't go too much further into it. Have you actually worked with Realm?

Speaker A
I have not worked with Realm. I know a little bit about the details of it, but I haven't actually written anything that works with Realm.

Speaker B
Do you want to talk at least a little bit about the details that you do know? Because I am completely out of my depth here.

Speaker A
Yeah, for sure. One thing I should say is the people who use Realm really like it. We have friends that work on projects that use Realm. They're really into it. So there are people that really do like it, even if it's not the best solution for you and me.

Speaker B
Sure.

Speaker A
So basically it kind of came out to patch over some of these things that core data has a tough time with. So number one, setting up a stack is super easy, I think. You just make a new realm and then you're good to go. You can start adding and saving objects. It's also thread safe. So anything you do is just like you just pass these objects across thread boundaries and it's basically totally fine. It doesn't rely on SQLite. It's actually really interesting how it works. Your class kind of dynamically bridges to the disk. It's kind of memory mapped if you know about the memory map function. So basically when you read a property, it is actually going to the disk and reading that straight off the disk. It's never copied into memory first the way it would be with core data. So it's not SQL lite, it's something totally different. They had open sourced their bindings for a while, but now they've also open sourced the. Actual C plus plus core of the thing that actually manages these bindings and all that stuff. So it is entirely open source now, which is really nice. Core data is the only option that we talked about today that's not open source. The app is also open source and so because it never has to bridge and copy these things into memory, it's supposed to be much more performant than something like core data. Yeah, it's got some really interesting, weird stuff going on with it.

Speaker B
I would assume that means it's, in theory, even more performant than Yap too.

Speaker A
It depends, I think. Right, so if you're reading a lot, every read that you do is going all the way to the disk. So that's a trade off you may not be willing to make. You may want to just want to copy that once into memory and be able to use that value. But if you're reading a little bit less and writing a little bit more, it may be a better balance and it may make more sense to read it directly off the disk and work with the data as bytes on the disk instead of in memory.

Speaker B
Okay, that makes sense.

Speaker A
Yeah, it's a pretty cool solution, and I know they have a lot of funding and so they have a really good team that works on a lot of really interesting things. They make Swiftlin, which is a great tool that we use, so it's kind of best in class in terms of the people that work on it and the features that it has. So it does work and it may be a really good option for you. I don't know how it works. Is it a relational database per se?

Speaker B
I really don't know this offhand, I'm sorry.

Speaker A
Yeah, I'm not sure I do either. I'm sure we'll get an email about it, probably. Yeah, it's a pretty cool thing. It can be a good solution. I might recommend it over core data in every situation. Do you think that's fair to say?

Speaker B
Well, I don't know that much about it, so I don't really feel comfortable saying that, although I feel like you may be right.

Speaker A
Yeah, I'm just struggling to think of a time when I would be working on an app where I would think core data is appropriate and Realm is not appropriate.

Speaker B
Yeah, I'm really not sure.

Speaker A
Yeah, I don't know. So maybe email us, leave a comment.

Speaker B
On that page, please let us know. We definitely would welcome more input about this. And we'll include a couple of links about Realm in the show notes at least.

Speaker A
Yeah, for sure. Those are all the persistence frameworks that I know about. Yeah, I guess you could do raw SQLite. I did that for a couple of apps.

Speaker B
Really?

Speaker A
Yeah, it was a lot of boilerplate, but I think with some code gen, you could totally make that.

Speaker B
Got to worry about input sanitization, et cetera, though.

Speaker A
I mean, it's not as bad as on the server, right? Because all the data on the device is usually just the users.

Speaker B
Yeah, I guess so.

Speaker A
But it's not as big of a deal and they have I mean, I think SQLite is actually better than MySQL about like if you pass a string to it, it will sanitize.

Speaker B
Really? That's got to depend on the bindings that you're using, doesn't it?

Speaker A
I don't know. It's been a long time. We've talked about doing an episode about our first apps. This app, I would definitely need to talk in the episode about our first apps. Yeah, but yeah, I wrote all the code manually. I wrote all the JSON parsing code manually. I wrote all the SQL light code manually. And it was you just need code to bridge from like a table row to a fully fleshed object and then one to also save that back. But if you had code Gen, you could kind of just write yourself. Yeah, like if you're code Genting, that like Struct to NS coding bridge. You could just code gen the SQLite to Struct bridge, for example. Think about it.

Speaker B
I'll think about it. Before we wrap up, I wanted to mention two things that I thought of when you mentioned that you were working directly with SQLite, which would be Fmdb, which are objective C wrappers around SQLite. Is that what you were using for SQLite or were you?

Speaker A
It is what I was using. There was also something called Ego Database back in the day, which I think was also a SQLite wrapper, and it had Operation QSOR maybe when Fmdb didn't. So I used one of those, I can't remember which one or both possible.

Speaker B
So Fmdb would be something to look at if you're interested in using SQLite more directly. And then from Marco Arment, there's FC model, which I've never worked with, but which it says on GitHub is an alternative to core data for people who like having direct SQL access. So there you go. If you want, quote some of Cordata's convenience, but with more control over implementation performance database schemas, yada yada, yada. This may be something to check out. I've never worked with it, so I can't necessarily recommend it, but put it on your list.

Speaker A
Yeah, that's definitely something to check out. Okay, so we could toss links to those in the show notes, but other than that, anything else, Chris?

Speaker B
No, I don't think I have anything else to add. Those are everything that I've worked with or most of the things that I can remember ever reading about.

Speaker A
Cool. Well, thanks Patreon supporters, and we will to you next week.

