Soroush Khanlou
Okay, let's kick this. Kick the show off.

Chris Dzombak
Let's do that. Welcome to Fatal Error. I'm Chris.

Soroush Khanlou
And I am, sirous.

Chris Dzombak
Today we thought that we'd take a little bit of break from the really intense concurrency episodes that we've been doing. There will be another one next week. There will be?

Soroush Khanlou
Oh, yeah, there will be. Yep.

Chris Dzombak
We recorded them out of order. You know, kind of a concurrency theme.

Soroush Khanlou
I'm going to hit the bell very lightly here.

Chris Dzombak
Very nice. So tonight we thought we would do a grab bag episode. So each of us has some moderately interesting stuff going on and we haven't had a chance recently, Sirusha and I, to just, like, catch up about some of the more minor stuff going on in each other's programming lives.

Soroush Khanlou
Yeah. Things that maybe don't deserve a whole episode, but things that are interesting nonetheless and that we want to talk about right before we get kicked off. You may notice that my dulcet tones are coming in a little bit smoother than normal. That is thanks to you, the Patreon listeners. I got an ATR 2500, which seems like a pretty good mic, and it wasn't too expensive, which was nice. And I've kind of put the Road podcaster to bed. I don't actually have a purpose for it. So if somebody wants to start a podcast, this Road podcaster was gifted to me, and I would be happy to gift it to someone else. If they wanted to sort of start a show, but they didn't want to spend any money on a microphone, I would be happy to send it someone's way. So if you are a Patreon listener and you want the microphone, definitely hit me up and I would be happy to send it to you. I'm pretty happy with this new mic. I still need a shock mount and a pop filter for it. So my peas may be coming a little hot, but I really want to thank everybody because it wouldn't have been possible for us to get gear like this, gear that really works for us without the Patreon. So we really, really do appreciate it.

Chris Dzombak
Yeah, absolutely. My new microphone, I got the same model as Sirous, is still in the mail. So my voice is coming in just the same as it ever has. But I want to reiterate thanks to all of your Patreon supporters for making this podcast possible.

Soroush Khanlou
Yeah. So episode 45 is already recorded, but then episode 46, I think, will be the first one where we both have our cool new mics.

Chris Dzombak
Yeah, great. It'll be exciting.

Soroush Khanlou
So, yes. Thank you. Thank you to all of you. All.

Chris Dzombak
Yeah. On to more technical topics.

Soroush Khanlou
Let's do it.

Chris Dzombak
So I think the first thing that we were going to discuss, unless you object, Sarosh, is that I have been working on a skill for the Amazon lady in a Tube device.

Soroush Khanlou
The lady who shall not be mentioned for fear of triggering right before mentioned.

Chris Dzombak
We'll leave things out as necessary throughout the show. I actually just started working on this yesterday, so, quote unquote, have been working on it is maybe a little bit of a strong statement. I fell asleep on the couch at about one this morning because I started working on it after work and then fell asleep.

Soroush Khanlou
It's always nice to have a project where you like it so much that you work on it late into the evening.

Chris Dzombak
Yeah, it is. And I've honestly been kind of struggling to find something that's like that. And so I'm really happy that I found something that I'm really excited about and I'm just rolling with it.

Soroush Khanlou
Yeah, I'm really happy to hear. So where are you? What is it? Can you share what it does?

Chris Dzombak
Yeah, so the idea so, earlier this week, I finally fixed up my home airplane tracking radio setup. This is a little Raspberry Pi that has a little software defined radio dongle that's hooked up to an antenna and it receives transmissions from airplanes that are flying around near me and plots those all on a map and also reports them up to sites like Flight Aware and a site called ADSB Exchange. And this is a really neat thing. We'll put maybe a screenshot in the show notes of what the front end of the software looks like. It's really cool. I have a little thing on my network that has a map of all the airplanes flying around and it's all data that I'm capturing, which is awesome. So I thought what would be even cooler would be, what if I hear an airplane and something flies over and I want to know what it is? Right now, I have to pull out my phone or run to a computer and look at what is flying overhead. And that's just such a pain. There are several of these echo dots spread around my apartment. And so I thought I really should be able to just ask what is flying overhead? So I'm working on a skill that does just that, and I have big plans for this. The idea is you'll be able to say what airplanes are nearby, what's the nearest airplane, what just flew overhead, which has a subtly different query than what is the closest airplane to me, since the airplane that just made noise overhead might not be the nearest airplane to you, like, 30 seconds later.

Soroush Khanlou
Right, right.

Chris Dzombak
I also envision you being able to ask what helicopters are nearby, if you, like, hear a helicopter and are specifically curious about that. Right. So this is really going to be a finely tuned application for me wanting to know what is flying over my house. Right.

Soroush Khanlou
Those are the best applications.

Chris Dzombak
So I have it working now to the point where you can ask exactly one thing and it just tells you what the nearest airplane to you is, and it gives you a little bit the output isn't formatted quite in the way that I want, but we can just try it here. We'll bleep all this out. Ask Aircraft radar what just flew overhead. The nearest aircraft is 2007 Airbus A 319 132 at 8500ft, heading 298.1. Boom. Just like that.

Soroush Khanlou
Nice. Sorry, quick interruption. How's your operational security on these matters? Like, did it give any tail code where somebody could track down when and where we recorded this episode?

Chris Dzombak
That's a very good point. No, I think my OpSec is intact here.

Soroush Khanlou
You got to keep that shit locked down.

Chris Dzombak
That's right. I think that was just the airplane's model, its altitude and its heading. And that's not really enough to track me down, for sure. Also, I'm fairly easy to track down.

Soroush Khanlou
He lives in Ann Arbor.

Chris Dzombak
Just hang out in downtown Ann Arbor for like, two days. You're guaranteed to run into me.

Soroush Khanlou
There you go. I heard it's a small town.

Chris Dzombak
Tomorrow's Friday, I'll probably eat lunch at Old Town, as usual. Yeah. Eventually I would like it to say that was a, you know, Delta 737 from that is up at this altitude and is flying in this direction, and it's going from here to here. And with whatever data I have, I want to just piece together a coherent message that puts the most important things toward the beginning. But I mean, I just got this working like, a couple of hours ago today.

Soroush Khanlou
Yeah. Still, that's pretty cool.

Chris Dzombak
Yeah. So there have been a couple do you want to dive into the sort of technical underpinnings of this for a few minutes?

Soroush Khanlou
Yes. I'm specifically curious about where does it run? How does the code work? What do you provide? Where they provide?

Chris Dzombak
Yeah. So I was actually pleasantly surprised by how easy this was. There are a couple of tutorials online. We'll throw some links to those in the show notes.

Soroush Khanlou
Cool.

Chris Dzombak
And it's really pretty surprisingly straightforward. The first thing is you go to Thumb Amazon developer page and put together a voice interaction model, which basically consists of defining an intent. So that intent could be like, show me nearby, or tell me nearby airplanes. And then you put in a bunch of example things that the users might say to get to that intent. So, like, what airplanes are nearby? What airplanes are flying nearby, what aircraft are nearby? Just a bunch of different things that the user might ask for. And I don't think that the Echo just listens for or only interprets those exact questions. I think there's some machine learning magic that happens, but at the end of the day, you have this voice model that is running somewhere in the Amazon world. And then when it gets triggered, so someone will say, like, hey dingus, ask my ask this application. This question. It identifies that application and sends you and tells you what intent the user has activated. And this runs on something called AWS Lambda. And I'm not totally. I forget exactly what AWS Lambda is even, but it seems like a way to run like a node application. I think it supports Python and maybe something else too. But you can run a node application basically in response to some external trigger, such as someone asking your echo for a thing. So it's not like an always on server. It's like you define some function and it gets triggered. And that function may do things like go out to a web service and grab information about nearby aircraft, for example. And so that's where the interesting part of this code, or the code that you're writing is running is within AWS. It's a function. And I mean, I say function. It really is like a full fledged node JS project. You can have dependencies. It can be many megabytes of stuff, but it gets spun up and run in response to some external trigger.

Soroush Khanlou
How do you deploy to the AWS lambda?

Chris Dzombak
So there are a few different when you're first starting out, you can literally copy and paste a JavaScript file into the web interface.

Soroush Khanlou
That's wild.

Chris Dzombak
It's really easy to get started. You can also edit in that interface.

Soroush Khanlou
Right.

Chris Dzombak
Once you're at a point where you want to use other dependencies, you basically upload a zip file to AWS lambda and it deploys from that zip file. That zip file consists just of like your JavaScript file or files and your Node modules folder. Right? Because AWS lambda isn't going to download node modules for you, they have to be all packed up in the zip file.

Soroush Khanlou
Got you. So that zip file might be tens of thousands of gigabytes potentially with all your node modules in there.

Chris Dzombak
That's right.

Soroush Khanlou
Got to get those settled.

Chris Dzombak
I have a very small project so far, and I think my no Modules file folder is up at like seven megabytes right now, so you're joking. I'm not.

Soroush Khanlou
Wow. It's not like there's any images in there. It's not like there's any video. There's no data. That's crazy.

Chris Dzombak
Yeah, it's possible to on the other hand, I don't really write much JavaScript and certainly much Node, but I've gotten this working so far pretty quickly, so that's cool.

Soroush Khanlou
Nice.

Chris Dzombak
There's a way to automate that deployment too. Like right now I'm working on making it so that I can trigger my lambda thing locally so I don't have to upload it to lambda to actually test. And there's also some way to deploy it from the command line, which I'll get set up at some point.

Soroush Khanlou
It sounds like it's a Heroku kind of system. And I bet there's actually probably a way to do like a git push to it and then it'll just deploy whatever's in the folder.

Chris Dzombak
Maybe, I'm not totally sure. Heroku is things that are running constantly, like receiving requests though, right?

Soroush Khanlou
Right. Yes. It is different in that way that it spins the well, actually Heroku spins the servers down when they're not taking their requests for certain tiers.

Chris Dzombak
Yeah, but this is something that I don't think is ever running persistently.

Soroush Khanlou
Right. Okay.

Chris Dzombak
So I don't know. That's my experience so far. I'm lucky in that the API that I'm grabbing this data from is really straightforward. It's from the ADSB Exchange site, which I mentioned earlier and which we'll put in the show notes. I don't feel bad using their API for this because I both donate to them to keep the project running, and I'm feeding them, like, live flight data from my little receiver set up here.

Soroush Khanlou
Oh, nice.

Chris Dzombak
Cool. Yeah, it's a nice little community run service or community supported service? I guess not community run. So that's that. Maybe by the time this episode airs, I'll have more features built in, and hopefully I'd like to go public with this at some point. There are one or two other skills that do a similar thing, but they're not very good, and unless I'm missing something big, mine will be much better.

Soroush Khanlou
Nice. Cool. So I'm still interested in how you kind of handle the node code and how you deploy and stuff. Can you write it and host it anywhere besides AWS lambda?

Chris Dzombak
I'm not totally sure. I don't know.

Soroush Khanlou
Interesting.

Chris Dzombak
Okay, that's a good question. I started reading tutorials about this yesterday.

Soroush Khanlou
Right. Yeah. This is like that Swift on the server episode we did where I'd been doing it for, like, two days, and you're like, how does this work? And I was like, well, you know, here's my best guess.

Chris Dzombak
Yeah, I mean, I can tell you for what I've done so far. It's really straightforward. Like, I have a folder on my computer that has my script in it and has, like, I can use NPM to install node modules. And then I zip it all up and upload it to lambda, and then I talk to my echo and it runs it, and it's pretty cool.

Soroush Khanlou
So for inputs and outputs so you said you kind of list out a couple of different ways the user could phrase the thing. Now, is it an exact match on any of those things, or is it kind of a fuzzy, like, oh, what's the edit distance between these two? It's close enough. Like, give it to them.

Chris Dzombak
Yeah, I'm pretty sure that it's not an exact match on those things because I feel like I've given it some phrases that are things that I didn't explicitly include in that list, and it's worked. So I think that there's some fuzzy magic, probably machine learning magic that happens in between. You sending a list of phrases and then like, a user saying something to the echo.

Soroush Khanlou
Right. And can you have parameters as well? Can you say, like, what flew overhead 2 hours ago?

Chris Dzombak
That's interesting. I'm not sure.

Soroush Khanlou
Right, okay. And then can you ask for more information? Is another question I have. So if they say, hey, what floor overhead? You could say, well, and the thing could respond. There's helicopters and planes. Which would you like? And you would say helicopters or planes.

Chris Dzombak
Yeah. So it's definitely possible to do that. Like, when your lambda function calls back to the device in a tube API, it can tell the echo whether this interaction is done or whether it should keep listening for an answer and then call you back.

Soroush Khanlou
Got you. Cool. And then the thing that you respond with is just a string. And they just read it.

Chris Dzombak
Yeah. So you just give it a string, and there's some markup that you conclude in that string to hint, for example, whether a number should be read as, like, 1234 or 1234 or 1234th as.

Soroush Khanlou
An ordinal or whatever.

Chris Dzombak
Exactly. Yeah. So you can provide various hints on how it should say things that way. Same with, like, letters. It'll try to pronounce things. But if you want it to just spell out letters, you can hint that it should just read raw letters to the user as well.

Soroush Khanlou
Got you. And then I'm also curious, like, between different homophones sorry, whatever the one is where they're spelled the same but pronounced different, like read and read or lead.

Chris Dzombak
And that's a good question.

Soroush Khanlou
I assume their speech algorithm kind of knows how to deal with that.

Chris Dzombak
I would assume, but I have not run into that yet, so I don't know for sure.

Soroush Khanlou
Got you. Okay. Yeah. I assume it knows because Siri knows how to read a sentence in a text.

Chris Dzombak
Yeah. This does seem like something that is.

Soroush Khanlou
More they can kind of figure out. Yeah.

Chris Dzombak
Cool.

Soroush Khanlou
All right. Nice.

Chris Dzombak
Yeah, pretty good.

Soroush Khanlou
And I feel like you could also fudge it a little bit. One idea is if you put in if the output you get from the API is, like, the number seven three seven for the plane 737, you could kind of replace that with the words seven and then 37. And then it would kind of read that. And so you'd be kind of tricking it.

Chris Dzombak
Yeah, definitely. And I may end up doing some things like that. We'll see.

Soroush Khanlou
That'll be cool.

Chris Dzombak
Absolutely.

Soroush Khanlou
Nice.

Chris Dzombak
We'll keep our listeners updated as to when they can install this on their Echoes. If I ever finish it enough to ship it.

Soroush Khanlou
I feel like it's shippable right now. It's not great, but my impetus is just to tell everybody to ship their thing as soon as it's even barely usable, and then iterate on it in public.

Chris Dzombak
I think there's some sort of approval process for the Amazon skills.

Soroush Khanlou
Even better. You should find out how what's the smallest, minimum viable application that they'll take.

Chris Dzombak
That's definitely true. I do have to figure out one big piece that I haven't done yet is getting the address from the Echo, the address that's assigned to the Echo and geocoding it for my search right now.

Soroush Khanlou
Is it hard coded for your address right now?

Chris Dzombak
Yeah, I started this yesterday evening. It's hard coded for my home.

Soroush Khanlou
Yeah. So the scope could be called what's, flying over Chris's house right now?

Chris Dzombak
Exactly. Yeah. So that's a big thing that I need to do. I assume that it's easy to get an address from the Echo and geocode it because I assume that everyone does. That nice.

Soroush Khanlou
Yeah, for sure.

Chris Dzombak
So that's that in the interest of sort of moving on to our other grab bag topics. You had something about Sorcery that you wanted to talk about, right?

Soroush Khanlou
Yeah, for sure. This one's a pretty short one, I think. But I basically finally got some time to write a blog post I've been meaning to write. And when I look back at the Get blame, I meant to write it back in February, so I am pretty far behind on this, man. Yeah, but it's finally out. It's called sorcery and practice. And Sorcery we talked about before on the show is a code gen tool for Swift. It'll basically let you kind of examine your Swift type system and using Source kit and generate code based on that. A lot of what I've seen with Sorcery in the examples and in a lot of bloggers and stuff is just really simple stuff. So auto equatable loop through all the properties and return false. If one of them is not equal, another one would be like, list all the cases in this enum and those are really useful, and I use those in lots of places, but I want to do a lot more. And so this blog post is basically all about how to generate an implementation for an NS coding wrapper for a Struct. And so, as you can imagine, that's not trivial because let's say you have a Struct, that Struct will then have a child struct that also you want to be encodable. So when you go through and make this thing, like when you prepare this thing for encoding, you not only have to wrap the original parent object, but you also have to wrap the child object before you encode it because otherwise it won't be an object that conforms NS coding.

Chris Dzombak
Yeah, it's not a trivial thing to accomplish.

Soroush Khanlou
It's not. And I think that's part of the reason that it makes it such a good example for Sorcery is because it's like, well, we've done such simple things with Sorcery to date, and we kind of leave out anything more complicated than that. But sorcery is pretty powerful. And so you can, and I did build this template that will create all of these implementations for a wrapper for each Struct that performs NS coding. You can read the implementation details on the blog post. I don't want to go too much into that here, but the big really interesting thing that happened was when I was looking at it, I was like, when we wrote this, I had this slight fear that this was not a very robust pattern. I was worried we'd have to constantly be making little edits to it, and there's like, it wouldn't kind of stand up, and I was worried it kind of wouldn't stand the test of time. And that turned out to be completely not the case. We wrote it in one day back in February, and according to Git blame, we have not touched the files since that day in February. We made them tons of model changes, and then this code reacts to those model changes, but it never sort of needed to be updated to handle. So the template kind of worked flawlessly. And so the code was a little bit ugly. I managed to actually clean it up a little bit. I was missing else if, so you can imagine I had a lot of nested if else sort of, sort of tags and commands, which was really frustrating. And I got a chance to sit with Kyle Fuller when I was back in Japan, and I was like, hey, I don't know why, but Stencil, which is the tool that Sorcery uses to make the templates stencil doesn't support LSIs if tags, and it kind of seems like a gimme, why doesn't it do that? And he goes, oh, it's just total oversight, my bad. And he coded up, and they had a pull request the next day.

Chris Dzombak
Oh, that's awesome.

Soroush Khanlou
Yeah. And that trickled its way down into Sorcery because Sorcery uses it as dependency, so they both have to be updated. But now, six months later, that has all finally landed. Like, it didn't take six months to land, but it was six months before I remembered to check. And now that it's all landed, I went in and rewrote the Cotiss LSIF, and it's a lot cleaner now. It's still a little bit messy, but the nice thing is that you never have to touch it once you get.

Chris Dzombak
It working mean, right? Yeah.

Soroush Khanlou
Which is crazy.

Chris Dzombak
Yeah. I'm looking at the post now. This is fairly impressive, right? You're handling a bunch of.

Soroush Khanlou
I call them encodables the objects that sort of need to be wrapped and turned into NS coding objects.

Chris Dzombak
Yeah.

Soroush Khanlou
So optionals, you got to handle special, because if the optional doesn't come out correctly, the whole thing should be nil. So you got to bail out of the initializer sort of you got to handle optionals correctly. You got to handle arrays differently. And then objects that are NS coding by default, like numbers kind of bridge to NS number in some kind of compiler magic Goop, so you don't have to worry about those. So you got to do all this special, all this special stuff to make all these things kind of line up. But we got to work. And we sort of opted in our models to this one by one. Like, we had a really rich model layer, and we took one object and we said, okay, let's make this work with the template. Then let's take a slightly more complicated and let's do another one and another one. And we added all these cases, slowly built up this code, and then we haven't touched the code in six months, which is a great feeling.

Chris Dzombak
That's really awesome. Yeah. Do you have these full templates on GitHub somewhere for others to examine, or is the code presented just in this blog post?

Soroush Khanlou
I have a gist that I could post.

Chris Dzombak
I think that would be cool too.

Soroush Khanlou
Let's drop that in the show notes. So, the thing is, we wrote this for ourselves and it might not work for every use case, and it's also designed to work with some other machinery. So, for example, we have a cache that's generic over some type, and then it's like we have a cache of locations, and then that cache will handle the bridging to these encodable objects and then back for you. So to you as the user, all you do is you create a cache of locations which is just a struct, and then everything else transparently is hidden from you and just works automatically. Without that stuff, it's not as useful. You have to manually wrap this stuff in encodables to make this stuff work in a useful way with like NS keyed archiver and stuff. But it provides just the general pattern of you can do really complex things with Sorcery.

Chris Dzombak
Yeah, absolutely.

Soroush Khanlou
So the two other interesting things I've learned recently since publishing this post well, one's an interesting thing I learned, and one is something I have like a longtime goal. The interesting thing is that there's another type of template that you can make with Sorcery, so that you could do stencil templates, which are like Liquid or like Ginger, all the different Templating libraries, mustache, all that stuff. But there's another one called Swift template, which is extremely crazy because the way that Swift template works is you can actually run any Swift code in the template. So anything in foundation, any of that stuff, you can just write it right into the template. Okay, so I need to look more into that and figure out how that stuff works. I think it's kind of in an early stage. I would love to talk to Shishtoff about it too.

Chris Dzombak
Is this his invention?

Soroush Khanlou
I'm not sure. I haven't been able to find out much about it and so I need to get more into it. But somebody basically tweeted me and said this thing Swift template, you can basically use any Swift code and any foundation code.

Chris Dzombak
Yeah, that could be really cool.

Soroush Khanlou
It could also be really problematic. Right?

Chris Dzombak
Yeah. I'm just googling right now, swift template and I'm not really finding anything.

Soroush Khanlou
So there's some stuff in the tests for Sorcery.

Chris Dzombak
For sorcery.

Soroush Khanlou
Yeah, right. And then there's some other stuff in the code that works that way. And the only way I can think that it would work is you basically have to do a bunch of find and replaces to turn your template into a Swift file where all the things in between the executable metacode is like a string literal and it all gets appended together and then execute that. I think that's the only way to make it work. But I don't know. I really want to dig into this because if this is true, this is crazy.

Chris Dzombak
Yeah, this is wild. Yeah. I'm looking at this one Equality Swift template that's included in the Sorcery tests. The test for the Sorcery repo. Yeah, that's cool. I don't know how it works.

Soroush Khanlou
Yeah. So maybe I'll get a chance to dig more into that should be more powerful than what we're using currently. But also if you do like a lot of logic in there, it could get really complicated. That being said, this isn't a server where you have a controller or a model to do your logic for you and you don't want to do the logic in the view. So maybe it's actually okay, I don't know. But yeah, so that's pretty cool. That's the one thing I learned about I want to dig more into. And then the other thing, which is the longtime dream of mine, is basically I think that it should be possible to generate the entire model layer from using this technique. Basically I want to have so we have a model repo for Beacon. I think we should be able to have a protocol that represents the event which has a sub protocol for location and has a sub protocol, not a sub protocol but like a references another protocol for users, all that stuff and then just push a button. And all the implementations for NS coding for Fluent, which is the vapor, orm for JSON encoding to it encoding from it on the client side, on the server side, all of that. You should just be able to instantly generate all that stuff and then it should go into the right projects and then you be able to add extensions in those projects for the extra data that you want to add to it should be possible. And I don't know if I'll get a chance I don't know when I'll get a chance to do it, but that's like my next thing. It's just like you should not think about your model at all. Besides also the code that sets up your migrations in vapor so that you could just add a property and then it will automatically get added to your database next time you run that server, which would be also be really nice.

Chris Dzombak
Yeah. So you're thinking about just sort of a more declarative way to put together models for Swift come with all these features. That's something that I know you've mentioned to me, but in the past.

Soroush Khanlou
It's truly my white whale. I've been chasing that for a while and I think I'm really close. Yeah, and then the other thing is you might want. To be able to make you might want, like, let's say you have a concept of an event in your app, like Beacon. You also have, like, an event draft, which is exactly like an event, except all the properties are optional. And then you could kind of assign them individually, and then you could generate bridges from the event draft to the full event. Or like, the event draft goes to server, whatever. But the point is, you could have all this stuff and you could just generate it and never use it, but it would be there for when you did need it. And that's a pattern I've done before. We have like, a mutable version for messing with it on the client. And then once it goes, if JPM goes back, you get an Immutable version. And I shouldn't have to write and maintain two different objects for that. This should just be done for me. It should generate classes, structs, whatever you want, just like, done. So that's my dream. I'm one step closer.

Chris Dzombak
Yeah, that's awesome. I don't see that there's any reason why you couldn't do that. Yeah, going back to Swift templates for a second, I found a commit in the Sorcery repo where somebody named Kunislav Tsar maybe drop it in the show notes. We'll drop this in the show notes? Yeah. The commit says Swift. Templates proof of concept. And this commit appears to introduce the implementation of Swift templates to Sorcery. So I think this is sorcery specific right now.

Soroush Khanlou
Nice.

Chris Dzombak
And I was listening to you, So, and I wasn't really, like, trying to figure out exactly how this works, but it seems like you could dig into this to figure out how Swift templates actually work.

Soroush Khanlou
Yeah, this is crazy. So this could also be really good if you're writing really complex templates and you need like I was basically doing a lot of weird, like, okay, let's say you have an array declaration. So it's like open bracket and then a type name and then close bracket. You want that type on the inside. So I was doing a lot of, like, okay, replace the first bracket and then replace the last bracket and then make it lowercase. It's like a bunch of crazy stuff like that. And if I could just use actual foundation code, like, oof, I could do awesome stuff. Pretty dope. So, yeah, that's my sorcery sort of most recent adventure. I just wanted to kind of touch on that.

Chris Dzombak
So one of the things that I forgot to mention in the discussion of that skill that I'm working on is that just before we recorded this, I was busy trying to figure out how to use the sort of await Async stuff from Es seven. And that looks really cool. It should really clean up the Asynchronous code that I'm writing in Node. I don't quite have it working. I have to figure out how Babel works and how to run things locally with Babel and then how to build it and get it all deployed and happy on AWS Lambda. But I think I found something useful just before we recorded today. So I'm hopeful that I get that working and that'll be really cool because this will be the first time I've actually used Async Await sort of semantics in a production, like in any real application.

Soroush Khanlou
Yeah. For all the consternation about Async Await in the last couple of weeks, you're totally right that neither of us have ever actually used it.

Chris Dzombak
Admittedly, it's in JavaScript, but I am looking forward to actually using that.

Soroush Khanlou
Yeah, that'll be really cool. You have to report back when you get a little more usage with it and you could say how much you like it or don't like it.

Chris Dzombak
Yeah, I expect that, I don't know, maybe in another month or a few months, if I finish this little skill project, I imagine we'll do some follow up on the podcast about the whole project.

Soroush Khanlou
Nice. Pretty sweet.

Chris Dzombak
Yeah. So one other thing that we wanted to go over today is that I recently had an opportunity to help a friend with a Swift problem, and he really stumbled into a pretty significant can of worms here. He is not an iOS developer, although he's a sharp developer in general, and he's used Objective C before and wanted to do a command line program that was written using Swift. And he had a Swift library from Realm that he needed to depend on. He's doing some work with comma separated values, among other things. So he wants to build a command line tool. And he had started a command line application project in Xcode, and he had started to use Cocoa Pods to integrate this library into it. And he emailed me because, as you might expect, when he tried to run the application, he got a dynamic linker error. It couldn't find, I think, the Swift runtime. And when I downloaded his project and tried to compile it, sure enough, it couldn't find one of the dependencies that he was trying to pull in via Coco Pods. So the issue here, and I'll throw a bunch of the same links that I sent him into show notes. The issue, of course, is that Coco Pods wants to compile all your libraries into Frameworks and put them on the application bundle. Xcode also wants to do that. Right. With the Swift library. The Swift runtime command line program is just a binary, it doesn't have a bundle.

Soroush Khanlou
Right.

Chris Dzombak
And this will be kind of familiar to a lot of people who tried to write Swift applications. It's difficult to distribute a binary Swift application, especially with third party libraries. So I sent him a little bit of reading about this problem, about the problem, and made two suggestions. The second one was basically just a bunch of useful looking links on stack overflow. Since I've never actually fixed this problem for myself. I haven't written any command line application in Swift, I've just read about it. But I sent him some useful links or hopefully useful links about how to change the path that the dynamic linker looks for libraries at Runtime. So maybe if he this seems like it's a tool internally for his lab. So assuming he can control how this is distributed and installed, maybe you could just link the or just tell the binary to look for these libraries in its directory and ship the binary plus all the dynamic libraries that it requires. Right, that could work. My other suggestion was that Swift Package Manager will now let you make a command line application in Swift and ship it and have libraries and stuff in it. And I don't totally understand how that all works from a linking point of view. I guess maybe it actually statically links all these libraries in, because otherwise how could you distribute just a binary? But I sent him some links about Swift package manager. Since command line apps are the only thing that Swift Package Manager works for, and suggested that maybe you just started this project, why don't you try starting over with Swift Package Manager instead of cocoa pods and Xcode and try to integrate these libraries and build it and see if it actually runs this way. And that was a couple of days ago and I haven't heard a report back from him yet, but he's going to experiment with SPM and report back to me how it goes. And I'm super excited to hear back from him because this is something that I've read about. I once started trying to write a Swift command line program and quickly gave up because I didn't want to deal with all this. But he is trying to use a Swift framework firm, Royal, so he doesn't really have a choice here. And I think that the Swift Package Manager stuff for command line programs especially has come a long way since I tried, which was two years ago at this point, probably.

Soroush Khanlou
Yeah.

Chris Dzombak
So I don't know, do you think that was the right advice?

Soroush Khanlou
I do think that was the right advice. Is this software going to run on Linux computers or Mac computers?

Chris Dzombak
That's a good question. I think no, I'm not totally sure.

Soroush Khanlou
Okay, so if he's trying to use a package from Realm, swift lacks the Runtime features that objective C does, which is why the Realm stuff I think, is still written in objective C, but there's just Swift bindings to it.

Chris Dzombak
I'll try to dig up what it was. This was like some Realm library for dealing with here. What will you talk? I'll try to find the library.

Soroush Khanlou
Yeah, for sure. See, I'm interested to see if it's designed for Linux. That library may not even work because if he's using it for persistence or something, it won't be able to know what properties he has because Swift has no reflection capabilities. That being said, I hope it does work. I think SPM is the right answer. It's what we use for server sideswift. It works pretty well for us.

Chris Dzombak
Okay, cool. That's good to know.

Soroush Khanlou
Yeah, it's pretty good. Now I don't use it for too many packages because, you know, I'm so crazy about not invented here, but it's generally working well for us. The other thing I would add is that if you want to write do you think he would write tests? Is he a software engineer that would want to do that kind of thing or is he more of like, Swift is going to solve my problem?

Chris Dzombak
I'm not totally sure. I'm not totally sure. I think that the idea here is that this is internal tool for them to use on their development machines. And so I think it's probably OS Ten or macOS. Although I will email him after the show to convince or to confirm that right. And we'll throw a link to the repository that he's trying to use in the show. Notes this is Realm Converter, an open source framework to make it easier to get data in and out of Realm. It has been built in Swift, but can also be easily utilized in Objective C programs.

Soroush Khanlou
Interesting, it may rely using Swift objectives. Yeah, it may rely on the Objective C runtime, which doesn't exist on Linux, but if it doesn't, then I think it will work. Or he could just run on the Mac. The other thing I want to add is so when you compile a binary using Swift package manager and using just like Swift Build or whatever, the problem is that you create a binary. You can't run tests against it because anything that you would run tests against, you have to hit that public API of the application binary. And so to actually run tests, what you have to do is you have to make a second module that has all of the code that you want to test in it and then run XC test against or like Xcode sorry, Swift test against that module. And then you can import that as testable because it can basically rewrite all your internal bindings to public bindings and then run code against it. But then yes, you can't test the actual thing that compiles it to your executable. You have to import the code that you're testing into the module that is actually going to be compiled into the executable and then build that. And so your public declarations have to be right. Testing in Linux is weird right now.

Chris Dzombak
Yeah, I think the good news is that most of the Swift Package manager tutorials that I sent him do follow that pattern of putting your code in a library so that you can test it. So assuming he follows one of those or he'll figure that out and he should end up with something that's a decent architecture. If not, I get the feeling he's writing an internal tool to do some stuff with CSVs and I don't know, I think he'll be okay. And you can always, like I don't think it's going to be a big program that it would be hard to refactor out later.

Soroush Khanlou
Right? Yeah, I ended up doing that for the Beacon app. Maybe like, a week or two in because I was like, I really want to write tests for this one component because it had a bunch of education I wanted to test. And it ended up being that. I spent a while trying to figure out, how does it actually work? And you have to pull the code out into a separate module, and that's how it works.

Chris Dzombak
I'll email him again after this, and I'll mention that to him too, so he's aware I'm always in favor of writing tests, even for stupid, small internal things. Although who knows if it's worth his time? We'll see.

Soroush Khanlou
Yeah. Cool. Well, this is fun.

Chris Dzombak
Yeah. This has been hopefully an interesting episode. We didn't get to the fourth topic on our list, which is Chris is writing Python and had some observations about coming to Python from Swift, but we'll talk about those another time.

Soroush Khanlou
Yeah, sounds good to me. As always, Chris, it was great to talk to you. And thanks to all the Patreon people Ash said.

Chris Dzombak
Thank you so much to all of you for your support. You keep the podcast sponsor free and pay for our production costs and now microphones, so we'll sound even better. Sarosh, it's always nice to talk to you and talk to you next week.

Soroush Khanlou
Sounds good. Talk later, Chris.

