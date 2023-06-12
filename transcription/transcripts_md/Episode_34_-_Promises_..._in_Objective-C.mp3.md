Speaker A
Hello, Patreon. Supporters. Thank you so much for your support and welcome to Fatal Error. This week we thought we would try something in a little bit different style. We don't necessarily have a set topic ahead of time this week we thought we would just try to have a free form discussion and see where it goes. This is something that we thought for season three we wanted to try some slightly different formats and see how they work for us. And so this is going to be a little bit an experiment.

Speaker B
Yeah, for sure. Especially since this podcast was kind of born out of just Chris and I talking. Anytime we would hang out, we would just have like a nice conversation about programming and none of those discussions really ever had topics per se. They just kind of went where they went. And so we're trying to see if we can capture some of that for this as well. Maybe a sneak peek at a new episode stuff for you awesome Patreon listeners.

Speaker A
Yeah, and eventually for non Patreon listeners too. Who knows?

Speaker B
Yeah, could be.

Speaker A
So how are things going?

Speaker B
Things are good. Things are good. The most interesting programming thing that happened to me this week is I have a client who the app needs to be deployed on kind of less than reliable networks. So spotty WiFi, maybe not that great of so this is like the app is designed for places in the Middle East, bahrain, Syria, Egypt, as well as like other countries, nepal, where you might not necessarily be able to have the strongest network connection.

Speaker A
Interesting.

Speaker B
And so we can't necessarily afford to have the Swift runtime packaged in with the app. So the app has to be all.

Speaker A
Objective C. Okay, interesting. I was going to say, like, I already have a number of questions. Like, this is definitely an interesting use case and there certainly are a lot of constraints that come along with that deployment scenario that we don't necessarily normally think about, like front of mind. But let's go with the constraint that you've mentioned. Which Swift runtime is too big to package into the app.

Speaker B
Yeah, exactly, because it's too big. It's got to be all Objective C. But some of the swift things that I've gotten so comfortable with don't exist in Objective C. So, for example, this app does a lot of stuff with firebase, and there's a part where we have to upload multiple images and we have to set various keys in firebase and we want, like, kind of one completion block for all of it, which is a perfect use case for promises. But promises and objectives don't get along so great because they don't have really good generics and the brackets make life kind of tough. But the way I was doing it before was dispatch groups and the dispatch groups were real hairy and I was like, I can't keep doing this dispatch group thing anymore. So pretty much what I did is I ported my Swift promise library over to Objective C. Okay.

Speaker A
Wow. That is not where I was expecting to go with this.

Speaker B
Yeah, it does make the code marginally better. It would be even better if it were Swift because like I said, mentioned that the generics and the brackets and text are not great.

Speaker A
You mean let me interject. It makes the code that is using promises better than it was before.

Speaker B
Right? Exactly. And there's a couple of interesting changes. One is you no longer have the nice state machine enum that backs the promise. And so the way that that works now is it's one ID property, and it's either nil, which means it's pending an error, which means it's failed, or anything else means it succeeded. So that's not great, but works. And then the other weird thing is you can't really type overload an Objective C. So you can't say this message when you pass this type behaves differently than the same message when you pass it a different type.

Speaker A
What do you mean exactly? If anything, you have more flexibility to vary things between types and Objective C.

Speaker B
Well, but you can't do two method implementations. So the case here is then, right. The way I have it set up in Swift is there's a method called then when you call then with a block, and depending on what that block returns, determines which implementation of then you'll get. And there's three possible implementations in Objective C, you can't reimplement that same message with different types. Right.

Speaker A
I got to say, I don't think I'm totally following what you're saying.

Speaker B
Okay, so in Swift, you could write, like, handle a person object, and, like, a function called handle that takes one parameter that is like, an underbar parameter. So it has no label, just handle. And then it takes a person and then a handle, and it takes, like, a location. And you can implement both of those methods side by side. And then the static picker, like, the method picker, the dispatch tables or whatever they are, picks which one it is at compile time, which one that message will go to because it knows what the type is, and that, if I'm not wrong, is called overloading. Right.

Speaker A
Yeah. No. Okay, I'm sorry. I understand what you're saying now.

Speaker B
Yeah. So in Swift, I have three then methods that are each overloaded depending on what you pass them. But in Objective C, you can't do that. So I have one then method, and depending on what you pass it, it switches dynamically. So if you return nil, it does nothing. If you return an object, it basically performs a map on the internal contents of the promise. And then if you return another promise, it will actually flat map that promise.

Speaker A
I mean, that seems like the most straightforward Objective C way to do that.

Speaker B
Yeah, pretty much.

Speaker A
Okay. And right. You kind of touched on how Objective C's, lack of generics and more bracket heavy syntax probably makes this a little bit oh, and block syntax, I guess.

Speaker B
Probably makes this so bad, Chris, especially with the new nullable, non nullable annotation.

Speaker A
That'S going to be so bad. That's going to be pretty heavyweight.

Speaker B
Yeah, it's not great. The compiler will walk you through what you need to do for those, but like not great.

Speaker A
Yeah.

Speaker B
And the brackets, I mean, you did a lot of reactive cocoa and Objective C, so you know how bad the brackets are.

Speaker A
Yeah, it's not pretty. Gotta say, reactive programming promises much prettier in Swift way.

Speaker B
Prettier. And then the generics are really like a suggestion. They're honestly just a suggestion. They're not really type checked in any way. Oh yeah, you definitely can't do anything meaningful like take an array of promises and turn it into a promise of an array. Like the promise. All method.

Speaker A
Yeah.

Speaker B
So the generics are just barely a hint. I mean, honestly, they're not really back.

Speaker A
In my day, we didn't even have Objective C. Lightweight generics uphill both ways.

Speaker B
That's right. Yeah. I bet it was even worse. I guess maybe it wasn't because you kind of just had to know.

Speaker A
I mean, that is by definition worse.

Speaker B
Yeah, well, but it's like a false sense of security with Objective C ziyawa generics, you think you know what's in there, but you don't actually, that's better.

Speaker A
Than how are you going to communicate that? Comments?

Speaker B
Yeah, it's not great.

Speaker A
Yeah, there's no good solutions. Are there any positive parts to rewriting this in Swift? Is there any positive takeaways?

Speaker B
So rewriting an objective c. Excuse me. Yeah.

Speaker A
I'm sorry. Rewriting an objective.

Speaker B
C yeah, well, the positives are I get to use promises like I don't have to deal with. Yeah. So before, what I would have to do is let's say one of these, it has a concept of like uploading a report. So when you upload a report, you have to set one key in Firebase for a title. You have to upload each individual image, you have to upload the metadata for each individual image. And then later if we wanted to have you be able to set a date or any other property, you'd have to do is actually a separate request over the like over Firebase, basically. So before I basically had to have a dispatch group enter and a dispatch group leave for each one of those completion block asynchronous calls. And if you leave out the leave or you leave out the enter, it's all just really very brittle. Right. So now I could just do a promise all, I can return promise all, and then put all the tasks that need to happen right there. And then I'm just guaranteed that as long as I put the thing in that promise, all all those things will be completed and I'll get one completion block and I'm guaranteed to get it. And it's guaranteed to be thread safe. Yeah, so much simpler in terms of implementation.

Speaker A
Why did you choose to rewrite your own promise library rather than using an existing promise library for Objective C?

Speaker B
Yeah, I think it's mostly because I have a very non invented here mentality, if I'm totally honest. But it's the same reason I wrote my own Swift promise library, just because I had a certain way that I wanted it to look and work, and nothing that was out there worked in that way, and I just wanted to be able to tailor it to my own thing. The whole thing took about two or 3 hours to port. Not too bad. Okay. Yeah. So I didn't feel like I'd really wasted a lot of time. And then I actually initially started with a promise library called BA Promise and tried to kind of rejigger that to make it work really nicely with what I was trying to do. And it wasn't cooperating. And I basically spent 30 minutes on that, got nowhere, and I was like, I'm just going to write this myself, and wrote it and it really wasn't terrible, wasn't the worst thing in the world. I also looked at Promise Kit, but Promise Kit, when you call it from Objective C, you're actually calling through a translation layer that just calls the Swift version. So you have to include the Swift version. And I go back versions in Promise Kit, but then I feel like I'm just using outdated code with a bunch of crust that I still don't care about. So whatever, I'm just going to just write this thing. And I think there's that paper or whatever that I love, which is like, if you need to rewrite more than 25% of something, or if you need to touch more than 25% of something, you're probably better off just rewriting it. Which those results were drawn from Fortrand, from like 40 years ago. So maybe they don't apply to modern day, but it feels like they apply. And so if I have to edit something way too much, I'll just be like, whatever, I'll just rewrite it myself. And you get exactly what you want out of that bargain.

Speaker A
Sure, yeah. Okay. As long as you've rewrote this. Let's see, I had a couple of questions. What's the test coverage like on the Objective C version?

Speaker B
Yeah, so I'm not happy about that part.

Speaker A
There's zero test coverage, and this kind of ties into my next question. Do you have plans to improve that or is this kind of going to sit as it is for a while?

Speaker B
I'm open to it. The thing is, right now I know the state of the code works, and I have a set of Swift tests that I could basically port over. And I think that would be an effective test library test suite. It's just a matter of finding the time. And basically if I have the need to refactor the thing or add an extra feature where I'm like, is this just going to break everything? At that point, I would port over the tests, make sure they all pass. Probably I'll find some that actually fail and then fix those and then add my new feature or do my refactoring with the confidence.

Speaker A
I was going to say, how do you know that the current state of the code works?

Speaker B
I mean, just from like queuing the app. But no, I know what you mean.

Speaker A
And I'm clearly being a little bit pedantic here. So the other thing I was going to ask was what are your plans for maintenance? Like your swift promise library is open source. I've seen you merging pull requests that people open. Are you planning to maintain the objective C version and accept or is it open source at all?

Speaker B
So there is a gist. I'm not sure if I've open sourced it. I will open source a gist. It is open source.

Speaker A
Okay.

Speaker B
There's a gist. I'll put it in the show notes and I'll try to keep it updated. But I think the gist is nice because it's like there's no real guarantee here. There's no issue tracking, there's no anything. But if you want this code, it is here.

Speaker A
Yeah, if there's a gist, I'm guessing you're not super committed to taking pull requests.

Speaker B
No. And the thing is, I do want to be forward looking as opposed to past looking. But at the same time, there's no benefit to keeping this closed source and not letting other people look at it. And if they have the same sensibilities and tastes as me, which is that my Swift Promise Library is like the whole thing is under like 300 lines or something like that. This one is also under 300 lines, although not as full featured. And if you have the same sensibility as me and you want something that you really understand, this may be something for you to take a look at. Okay, cool it's out there. But I don't plan on maintaining it, adding a ton of features to it. I will add what I need to it, and if somebody else wants to take it and run with it, great. But this is about where I'm happy to leave it.

Speaker A
This occurs to me. This is something that you don't have to answer if you don't want to. Is it adding even a 300 line promise library to an app that you're just contracting on and then handing it off to someone else? It's not like a standard iOS API, and presumably this is becoming a fairly major part of the app. Is this something that you think is okay for you to do as a contractor to add something like this and then hand it off to whoever's going to maintain it for whoever's responsibility it is next?

Speaker B
Yeah, that's a really fair point.

Speaker A
I don't know if I have a good you're not wrong.

Speaker B
So part of it is that I do want a really long term relationship with this with this client. So much so that, like, I would consider taking a, like, more not as, like, a full time thing, but I would consider taking a more serious role with them, whether it's but, yeah, I definitely really like, this is an important client in terms of the stuff that they work on. And I do want to be a part of the project long term. That being said, you can never predict how long you'll be with something. So I think maybe a little documentation, a little test might go a long way. But that being said, yeah, maybe you're right. Maybe that is something I should put some effort into just to make sure that someone understands how this thing works.

Speaker A
That kind of feels like it may be good, because I know that was always an objection to, or a common objection to introducing reactive programming into a code base. And promises are certainly easier than reactive programming to wrap your head around.

Speaker B
Well, but there's also less written about them. Is the other part of it less.

Speaker A
Written about reactive programming?

Speaker B
No, reactive programming has much more. Many more, like explainers tutorials.

Speaker A
Oh, that can be a curse or a benefit.

Speaker B
Yeah, that's true. But I feel like there's just not as much really good, rich promise stuff. At least in our community. JavaScript has a little bit better stuff, but in our community, if you're like, what's a promise, you might be searching in the woods for a little while.

Speaker A
Well, it's like a reactive signal, but it only fires once.

Speaker B
Right. So go learn all this reactive stuff and then come back and then you understand this. That's a fair point. I think I will add some documentation around. What is this thing? Why do we like it? Why do we use it?

Speaker A
I think that would probably be wise.

Speaker B
Yeah, I think that's a fair point.

Speaker A
If you don't mind, I just had some other questions that have come to mind about Lay mommy. Maybe not your promises library, but about the constraints that you have in this app. So Swift Runtime is out because it's too big. What else is out because it's too big? And specifically, what are you doing for resources? Are you using something like paint code? What are you doing for third party libraries? Is there anything that you would like to pull in but you're not using because it's too big?

Speaker B
Yeah, so I need to do, like, a really rigorous analysis of what is actually causing the space. Right now, the app is about eight megabytes, so it's not small, but it's also not big. It's smaller than it would be if it had any Swift in it at all. But that being said, I think there's a ton of room for improvement. So assets right now are just PNGs of multiple sizes, but I think they will be paint code very soon, especially once we're ready to do a product release, we'll do an analysis of all this stuff.

Speaker A
Okay.

Speaker B
It's just that you can pretty easily go from PNG to either PDF or paint code or whatever, but you can't really easily go from I'm using Swift and I'm not using Swift.

Speaker A
Absolutely. A note about PDFs. Don't PDFs end up being rendered out to PNG during the build process anyway?

Speaker B
I'm glad you asked. Yes, they do. As of iOS ten and earlier, but as of iOS eleven and later, they now are actually shipped in the App Bundle, and the rendering is done at Runtime.

Speaker A
Oh, neat. Is this an iOS change that I just missed because I wasn't paying close attention to Dubdub?

Speaker B
Yes.

Speaker A
Cool. That's really good to hear. I assume that this app, especially given the areas where you're trying to deploy it, probably isn't targeting iOS eleven exclusively.

Speaker B
That's right. That's exactly right.

Speaker A
So you're going to be looking at Paint Code or generally at programmatic drawing instead of PNGs.

Speaker B
Yes, exactly. Programmatic Drawing. Probably Paint Code, the designer I work with already, I showed him Paint Code and he went crazy. He was like, this is awesome. And so he went and bought it already. So we use that for all of our assets. Maybe we'll use one of those font awesome type things if we need it. So then there's a bunch of other considerations. Like basically, it's an app pretty much where people on the ground in either disaster stricken or war torn areas can use it to assess either sites or buildings or artifacts that have historical value that can't necessarily be moved. Because, let's say ISIS is in Syria. I think this is the first time we talked about ISIS on this podcast.

Speaker A
I think so.

Speaker B
And so basically, people will be taking pictures of this and building reports and assessments around how dangerous they think the area is, how much something needs to be extracted, how worrisome the current situation is in terms of will be destroyed soon. And it also provides sort of a paper trail for people like that Hobby Lobby CEO who are trying to take treasures and artifacts and stuff out of that area and actually are probably funneling money into ISIS while they do it. So it provides basically a paper trail to kind of be able to track down what exactly is going on. So that's the goal of the app. So one interesting thing is we need to be able to upload really big pictures.

Speaker A
This is another thing I was going to ask. I just have so few questions.

Speaker B
It's a super interesting problem.

Speaker A
So right. Let's go right to image handling and more generally, like network traffic. What are you doing to let's say you can download the app. Fine. What are you doing to minimize network traffic?

Speaker B
Yeah, so that, I think the way we're going to handle that and this is TBD, there's a little bit of user research that needs to be done. We just shipped the first version of it to the actual testers that are in the region and they'll be like shooting stuff in their backyard. But what I eventually want to do is I want to make the report publishing, which is the primary offline thing or online thing that you need to be able to do. I want to make it really transparent, exactly how it works so that you can see like, oh, this image is uploading, how fast is this image uploading? How long is this going to take? And then I also want to be able to basically have triggers for like, oh, this is on WiFi, or like, we're waiting for WiFi so that you can go to WiFi and say, okay, and now at this point, upload this report.

Speaker A
Okay.

Speaker B
Basically give the power to the users without necessarily removing any of the quality because the quality is really important, especially if you're doing like actual analysis and stuff on this. So you could upload thumbnails first and then upload full resolution. There's some things we're playing with, but there's also this whole MVP thing we got to fight with, which is one developer and we got a pretty full feature thing we want to build.

Speaker A
Interesting.

Speaker B
Yeah.

Speaker A
Okay. One thing that I mentioned earlier that we didn't get to are there third party libraries that are that I know you mentioned Firebase. Are there others that you would like to pull in but you haven't been able to?

Speaker B
Yeah, I'm pretty anti third party library in the first place. So when we were working on Urban Archive, I think the first 3rd party library that we pulled in was Mixpanel. Just because there's no other way to do Mixpanel, but we built our own networking stack, we built our own image loading, we built our own persistence, we built everything ourselves. At this point, I think we have some kind of bug reporting thing. We have some kind of like I think we use map box now, so we pull that in. But in the early days, a lot of that stuff I don't really think is necessary. We built our own JSON parsing. And so for this app, the only dependency we're really reliant on is Firebase. And we just dragged in Firebase manually. There's no Cocoa Pods, there's nothing like that.

Speaker A
Okay.

Speaker B
Yeah. So no Carthage and no especially one of the other concerns of bringing a promise library was like my pulling code that I'm not going to all compile but I won't need. And so just not having a library at all and I don't know if there's any overhead to Cocoa Pods is like bundling and building frameworks and stuff for you, but I won't have to worry about any of that.

Speaker A
With cocoa pods specifically. I think there's very little overhead in the actual thing that you deploy and at Runtime, but right. It's good to think about this.

Speaker B
Yeah. And bitcode is another thing that's worth thinking about. It's like if Apple can do the slicing for us and cut out the irrelevant segments of the app, then even better.

Speaker A
Absolutely.

Speaker B
One thing I am worried about is especially if the latency is really bad, even setting one key in Firebase, that's like one full round trip net request. So if you set ten keys, I don't know if Firebase does intelligent stuff around, like, okay, well, when should I send these, should I batch these, et cetera. But you got to dance with the one that bring you or whatever.

Speaker A
Yeah, I mean, at least hopefully that sort of thing should be a fairly small amount of data, even if it's high latency.

Speaker B
Yeah.

Speaker A
And hopefully the Firebase library under the hood will deal with transient network, some.

Speaker B
Kind of badging and something. It's an interesting set of problems and maybe we'll talk to the people and they'll be like, yeah, RLT is fine and you're worrying about nothing. Just go ahead and go nuts. Yeah, and maybe we will at that point.

Speaker A
But have you gotten any feedback about actual network conditions from users in these areas yet?

Speaker B
I haven't talked to users, but I have talked to the stakeholders and so that's where I get my picture from. But yeah, it could be if we actually talk to them, they'll say, like, hey, not a concern.

Speaker A
So it occurs to me this is all stuff that, I mean, maybe not most iOS apps maybe aren't written to target such an extreme environment specifically, but it's definitely something good to keep in mind regardless of what you're working on. Right. We know that people in war torn areas of Syria are using, for example, Twitter for communication. And I'm guessing that the folks who work on the Twitter app probably aren't thinking about this stuff day in and day out, right?

Speaker B
Yeah. And you would think that Twitter is a really unique case of it would be really cool if they built two versions of the app. One is like, Twitter Lite that doesn't have any of the stupid crap in it, and there's like a super small version of the app that just allows you to reading your timeline and posting and maybe DMs, right? But doesn't need to worry about like, open graph or doesn't need to worry about any of that extra stuff and could be really valuable in place like that. To me, it's like the technology is downstream from the product and the product is downstream from the use cases. So your use cases and ultimately what that audience is determines what product you build, and that determines what technology you need to use to build it. That being said, there's one other big thing here that we're kind of talking about, which is that this is an iPhone app and it probably should be an Android app.

Speaker A
Well, so I didn't know if I wanted to ask this, but why is this not a web page? Like a web service?

Speaker B
Definitely it can't be a web page. So the way that the experience works right now is it's kind of like Snapchat, and that when you open it, it drops you right into the camera. So the idea is you don't know how long you can be in this dangerous area, especially if there's rubble that could be falling if it's like disaster stricken. Like the Nepal earthquake is one of the use cases. We've been talking about real shit. So making sure that the app is quick to get in and out of is super important. And so for that, we want to make sure that assessing is quick. Taking pictures is quick. Getting in and out is super, super fast. That's kind of why it's an app and not a web page.

Speaker A
Okay, that makes sense.

Speaker B
And then I think it will end up needing to be an Android app at some point. So we'll see how that part of it shakes out.

Speaker A
Yeah, it does seem like having both major platforms covered with well and the.

Speaker B
Android thing also is dependent on a little bit of user research because I know you can't just make an Android app and it just runs on everything. You have to know what phones you want it to run on and that determines what technologies you can use and how old they can be and all that stuff.

Speaker A
As long as you're planning basically to take pictures and tag them with locations and upload them, I don't think you're going to run into anything too messy there, even on Android.

Speaker B
Yeah, I don't think so. But I do want to make sure that I actually target the phones of the people who are going to be using this because it also may end up being 100 people. Could do a lot of good with this app in that area, especially if it's the right hundred people. So we don't really need a huge user base. And especially because of that, if 60 of them have Android phones and 20 or 30 of those phones can't run a Honeycomb or KitKat or whatever we're on, then what was the point of building Android app? We got to make sure that we build the right Android app.

Speaker A
That's definitely something to keep in mind. But I haven't done professional Android stuff in years. But I really feel like for this application, that fragmentation is probably going to be less of an issue than you're thinking.

Speaker B
I'm hoping so. I'm hoping so.

Speaker A
Android also has, like their, or at least when I was working on it, had the support library that you could drop into your app that would bring some newer platform features to your app, even if it were running on old operating systems.

Speaker B
Interesting.

Speaker A
Yeah, it was a pretty neat thing to be able to do. I wouldn't necessarily write this off too quickly, is all I'm going. To say, right?

Speaker B
No, you're not wrong. But this product in particular, there's a lot of interesting choices and things to think about.

Speaker A
Yeah, this sounds like a really fascinating project.

Speaker B
Yeah, it's pretty cool. I'm really enjoying it.

Speaker A
Yeah, that's awesome. Well, I'm excited to hear how it progresses.

Speaker B
Yeah, it should be good.

Speaker A
Yeah.

Speaker B
So that's kind of what this project has been all about. That's why I rewrote my promise library in Objective C for this for this interesting, weird use case. Do you have any other questions or thoughts?

Speaker A
There was one other thing I wanted to mention. Back when Swift was first coming out, I put together a few Objective C macros that brought a couple Swifty things to Objective C. That's right.

Speaker B
Didn't you do like an iflet as kind of thing?

Speaker A
Yeah, and I'm not going to send you that.

Speaker B
I want that.

Speaker A
I'm not going to suggest that you actually use any of these. But as long as we're talking about going from Swift back to Objective C, that may be fun to read through.

Speaker B
So it's actually really interesting. I was doing basically JSON parsing because the way we store this data on disk metadata is just JSON instead of NS coding or whatever. And I just wanted something really simple, which is I wanted to say pull this item out of the dictionary if and only if it's a string. And there's actually not an easy way to do that in Objective C. Well.

Speaker A
I may have a macro for you.

Speaker B
Yeah. So what I ended up doing, and email me if you think this is terrible, but I added a method to NS object called as class or nil. And basically you pass it NS string class or NS string space class brackets. And it'll return to you either something that matches that class or nil. And so what I'll do is I'll say dictionary subscript this key as class or nil NS string class. And then I'll do the question mark colon operator, which is like Nfnil use this side. And I'll do like empty array so that way I know it's never empty.

Speaker A
So I have a few in one of these gists. I have a few macros and a few NS object category methods that may be nice for you.

Speaker B
I definitely want to see them. Yeah.

Speaker A
Here. So you have as checked, which basically takes an expression and crashes if the expression isn't the type that you expect it to be. So that's your as bang. Right. As exclamation point. Cool. As option is like your as question mark. It returns nil or the object if the object is the right type. And then I also have those implemented as NS object category methods too.

Speaker B
Perfect. Yeah, this is basically exactly what I needed.

Speaker A
Yeah, there you go. Great on that's everything that was on my list of to discuss.

Speaker B
Yeah, I think that's a pretty solid episode.

Speaker A
Cool.

Speaker B
Great to talk to you as always. And thanks to the patreon patreon people.

Speaker A
Yeah, absolutely. Thank you so much to all of you for your support. We really appreciate it. And, Serish, it's great talking to you. I'll talk to you next week.

Speaker B
Sweet. Talk to you soon. Chris.

