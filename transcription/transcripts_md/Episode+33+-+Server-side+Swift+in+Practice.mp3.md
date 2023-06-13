Speaker A
What's a droplet.

Speaker B
Welcome to episode 33 of Fatal Error. I'm Sirous.

Speaker A
And I'm Chris. And this week we wanted to dive into Sirush's experience in serverside, Swift. So we in a previous episode last season, we talked about your your experiences with Servicide Swift thus far, and you launched a thing. You launched beacon, right?

Speaker B
I sure did. I think when we talked, I was, like, five days into server sites with I think that's right now that it's more like five weeks, maybe a little more than that. We have a little more to talk about. So I have a lot more experience, and I know a lot more things awesome. And would be happy to share sort of my knowledge about it.

Speaker A
Before we dive into that, do you want to pitch us on Beacon a little bit or at least explain what it is that you built?

Speaker B
Right. So Beacon is an app that Ashley Nelson Hornstein and I built. We built in five weeks for WWDC. We built it real fast. And essentially what it does is you can kind of post events and post when you're available to do stuff, and your friends can kind of see that. We try to do smart push notifications to get people to see when you or when your friends does something, and then they could hop on that event and say, like, oh, I want to see Wonder Woman tonight as well. So it works out really well at WWEC just because everyone's always running around and nobody knows where the cool parties are and nobody knows where their friends are.

Speaker A
That's something that, when I've attended WBC, I found just really stressful, honestly.

Speaker B
Yeah. And it was even worse this year because of San Jose. Nobody knew where anything was in San Jose. So we were all just kind of aimlessly wandering around, trying to figure out, where should we go?

Speaker A
What should we do?

Speaker B
So we had a good amount of success. Like, there were people organized morning runs. Friend of the show Curtis Herbert organized some morning runs. There were, like, dinners, lunches, drinks, coffees. There were a microblogging meetup, which was pretty cool, that Manson Reese and Gene McDonald's put together. And one of the weirdest things, several Apple engineers also put their labs on Beacons to try to get people to come to them, which I'm not actually sure if they're allowed to do, but we obviously end up doing really cool. Yeah, it was really great.

Speaker A
So that sounds like a very successful launch for WWDC, and the server did.

Speaker B
Not fall over, so that's really good.

Speaker A
And that's something that we wanted to talk about. When we last talked, you had four or five days of server side Swift experience. You were using Vapor, and you were just diving into it. I'm trying to remember what all we talked about. You thought the documentation was a little bit lacking. Yeah. I mean, what's changed in your experience? Like, what do you feel better about? What do you feel differently about? How have your thoughts about Swift on the server changed in the last six weeks or so? Right, the last ten weeks, now, eight.

Speaker B
Weeks something, I don't know. We started the last day of April, I think, something.

Speaker A
Okay.

Speaker B
One thing is you just have so much more familiarity once you've been working with a platform for a while. So now it's not hard for me to figure out, okay, well, where do I need to put the tries? Because these statements throw and these don't. Where do I need to put the why is this thing not compiling? I've seen this particular compiler error before, so in particular I'm thinking of like, when you build JSON on the server, the way that vapor does it is with this thing called a node. And a node represents structured data. So it's an enum that can be in many different states. So it's either a string or an int or a float or a double or a date or whatever. And so when you create a JSON object, you create it with one of these nodes. And so the node can be like, how do I put this? We're getting really in the weeds, which I think people like the weeds. I hope people like the weeds. Write to us, send us an email if you like the weeds. But yeah, let's say you're setting up this note. You set it up with a dictionary literal, because your JSON is going to be a dictionary. And then if you put something in there that's not convertible to one of these JSON objects, you'll get like a really inscrutable error. And so now that I've done it a little bit, I see, oh, it's that error again. I must have put some kind of weird object in here that isn't convertible freely to JSON and therefore I need to go and find that and fix that. This is part of the reason that I want this specific problem is part of the reason that I want conditional conformances, because I think they'll make it a lot more easy to work with JSON because you can say, well, a dictionary, if it only has JSON objects in it, is also a JSON object. And then a lot of those problems just kind of go away. So I'm really looking forward to that, although I don't know if it's going to come into a for it now. I'm so deep in the stack, Chris. You got to save me from the stack. We got to pop this a couple of levels.

Speaker A
So at a high level, it sounds like you're saying you're just much more familiar with the errors that you might encounter, like common problems that you encounter, just more familiar navigating this whole, like, the stack of how vapor works, right?

Speaker B
Yeah, for sure. Learning the platform, learning how the RM stuff works, learning the ins and outs of postgres and this query won't work because of this reasons. And this will need an index over here and just better at it.

Speaker A
And that's got to be similar to the process of learning like iOS development at first. Right. You're getting to know UI kits, rough edges. Right. You're getting to know maybe core data. Core data won't work for this because of whatever reason. Right? Yeah.

Speaker B
And I kind of think it's going to be true of any platform you kind of develop on. You need to learn its quirks. Like, I don't think I could make an app kit app for the Mac, just like tomorrow. There's a lot of little things I'd have to learn.

Speaker A
Absolutely.

Speaker B
Even though I am fluent in Objective C and Swift and whatever else.

Speaker A
Now that you've actually deployed something, how many quirks have you encountered? Would you say it's less quirky than iOS development? More quirky.

Speaker B
It's got to be more quirky.

Speaker A
Really?

Speaker B
I'm pretty sure it's way more quirky. Let me give you a couple of examples of quirkiness. So part of it is like people say tooling or whatever, but part of it is tooling is just not there. So you edit the code in text mate, you tab over to the terminal to build the thing. When you build, you end up with build errors. And then those build errors, they aren't on the line the way they are in Xcode. So you kind of have to parse through them and figure out, what is this build error actually saying? Where is this problem? This would be solved if I move to Xcode, which I do need to do. And I think next week I will finally have some time to do that. That's a weird quirky thing. I think last time I shared, had I deployed to Heroku last time we talked?

Speaker A
I don't remember, but I don't think that you had. And that's one of the questions that I wanted to ask is what's the deployment process? Like, what are you deploying to? What is your sort of ops? How are you serving this?

Speaker B
Right, so short answer is Heroku. Long answer is everything is hilarious and totally ruined. No, it's fine.

Speaker A
I have to hear about this.

Speaker B
Yeah, the funniest thing about the Heroku thing was you can fix your Swift version by putting a dot file in your repo. That's just called, like, swift hyphen version. You put just 3.1 or 3.0 in there. If you leave that out, it'll just like pick one and it's horrible. So it turns out that Swift Foundation on 3.0 and 3.1 had a broken base 64 encoder. It would just crash when you tried to base 64 encode data. Okay. And vapor relies on the built in foundation base 64 encoder. So when I was trying to do OAuth stuff, I maybe told the story already, I'm not sure. But it was a patron episode.

Speaker A
Oh, yeah, I remember this. But yeah, let's hear it again.

Speaker B
Yeah. So basic foreign coding was broken. So then I pinned it to the right version, that was part of the problem. And then pinning it to the right version turned on stack traces for some reason. And before, this issue wasn't happening in my local, it was only happening on Heroku. So every time I made a change, I'd have to wait like six minutes for the thing to deploy so that I could actually see if I fixed it. So this was literally like 12 hours of debugging. It was horrible. So when you say it's a quirky, like, it's pretty quirky. It turned out eventually that I found out that it was the foundation base 64 encoder I found a totally swift base 64 encoder on the internet and started using that instead. And that solved the problem.

Speaker A
Okay. Well, I'm glad. Wow, I'm glad.

Speaker B
Yeah, it was brutal. I think it was like a Friday. I was working on it and every time I thought I had it, I was, okay, one more deploy, one more deploy. And I sort of got before I knew it, it was five in the morning and I went to sleep and I woke up at noon the next day and worked until five that afternoon until I finally got it. And it was people in the Vapor Slack that helped me to the point we talked about in the last episode about ask questions, because people can help you, and sometimes they know things that you need to know and they can tell you that information faster than you figuring it out. Once they ask, they were like, oh, do this and this and this, and maybe this will have a problem and this will show you a problem. That was a very quirky thing. As for the rest of deployment, it's not too bad. We're doing a mono repo, which is interesting because that sounds like you've got questions.

Speaker A
I'm very excited about this.

Speaker B
Yeah. So right now we're not taking advantage of the mono repo very much. There's just two folders, API and iOS, and people can just sort of like work in there and it's fine. But the thing is that when you deploy to Heroku, your app has to be the root thing in the directory. It can't not be the root thing in the directory.

Speaker A
Can you deploy just a directory to Heroku or you deploy the whole repo?

Speaker B
Yes, you can deploy just a directory. So that's called like git subtree. And so it's like some tool that's built into git and it will basically repack all of your commits and only create a new commit for every change that's only in that repo and basically chop off some prefix. Okay, so it will create a brand new tree of commits and then it will push that to a special branch on the same repo. And then Heroku is listening to that branch. And when I push to that branch with the subtree command, it just does the thing, and it deploys.

Speaker A
Cool. Okay.

Speaker B
Pretty good. Yeah. The only problem with it is that it has to repack every commit individually, and so the more commits you have, the longer it takes. So we're up at, like, 700 commits now, getting to the point where it's like, all right, we got to figure something out. I did a little research today, and I think there's a way around it where you can kind of reuse the work from previous Git subtree commands, which would make our deploys a lot faster.

Speaker A
Yeah. It occurs to me that we're using the term mono repo without defining it. So do you want to define it?

Speaker B
I don't know if I could give a good definition, but I could take a stab at it.

Speaker A
Okay, let's do it.

Speaker B
Yeah. So my understanding is basically, like, a mono repo is a Git repository that has more than one program in it, usually separated by folders. And the benefit to it is that everything always stays in sync so that if you make a server side change, you can make the client side change at the exact same time. There are also drawbacks, one of which we just talked about, where you have to repack everything. Is that a good definition, do you think?

Speaker A
Yeah, I think that's a good definition. If I were to take a step, I would say more or less the same thing. I would also note that you would normally use this to put, like, projects that have some dependency or some relation to each other in the same repo. So, for example, an iOS app and the server side that powers that iOS app. Right. Or the iOS and Android apps and the server side. Or maybe library internal libraries and applications that use those libraries. And the idea here is that this in some ways kind of shortcuts, at least for internal tools like your server and your iOS app for some library and the Go program that uses this library, this helps get around dependency management issues. Like, you make a change in that library. You fix whatever uses the library to work with that change, and you commit all this just to the same branch and send a poor request that includes a change and all the changes that make the rest of the stuff in your company work with that change. Same with if you change your server side API, commit that, fix the iOS app to work with that API, commit that, fix the Android app. Commit that all the tests run. Submit a pull request so that you have the API change and like, the iOS and Android changes all in the same poor request. And that simplifies dependency management and can help simplify project management, too.

Speaker B
Yeah, for sure. The one thing I would say to that is that is the dream. Although, in practice, merging something doesn't mean that it's deployed true.

Speaker A
Yeah.

Speaker B
And so you can make a change to the JSON. If you're adding a key, that's great, that's the perfect use case. But if you're trying to change a key, you could change it in everywhere at once. But that doesn't actually mean that it's on everybody's phones. So it has its drawbacks.

Speaker A
Yeah.

Speaker B
That being said, it's easier for us, and it's just so easy to just jump back and forth between things. And you do know that everything's kind of in the same state. And since both of us are Swift engineers, both me and Ashley are Swift engineers years, we can touch both sides of it. So if there is a change, we want to do like, I remember when I had push notifications, you just like, do the stuff you need over here and then do the stuff you need over there, and then make a pull request and it's all done. And it's kind of nice.

Speaker A
Cool.

Speaker B
Kind of nice, kind of convenient. I think I would recommend it.

Speaker A
This has been a good detour. Yeah. I've always been very curious, very excited about the idea of mono repos.

Speaker B
I think it's going to really shine once Shustoff makes Sorcery work on Linux. I hope you're listening to this, Shustoff. You need to fix this for me. Once that starts working, then what I really want to do is code gen all my JSON nonsense so that I just have one Canonical whatever, maybe a protocol, and it just spits out everything for both the server and the client. That way I can just change the JSON key once or add a JSON key once and then everything updates. That's what I really want. But we're not there yet, tooling wise.

Speaker A
Yeah. So how did we get here? We were talking about deployment ops. What's your experience running Swift on Heroku and keeping your Swift server up on Heroku?

Speaker B
Pretty good. We've had two crashes so far.

Speaker A
Tell me about them.

Speaker B
Yeah, so the problem is that the way that all this stuff works. Let's say you're deploying a Rails application. Rails just has exceptions. So Rails exception might mean that a validation failed, but it also might mean that you accessed an Ray out of bounds. In Swift, those two things are modeled as different components and they're different in Objective C. Two errors are the things that you should be able to recover from. So that might be like a validation error. Exceptions are the things that are really programmer errors and should never have happened in the first place and bring the whole process crashing down. So because there's no way. So in Objective C, you could try and at catch, and that would catch an exception, even though you really weren't supposed to use that. You could so you could build a server with Objective C and it would like, worst case, throw an exception. Something really bad happened and you could rebuild everything from scratch and rebuild some kind of request responder thing and you'd be fine.

Speaker A
Sure. Yeah.

Speaker B
In swift you can't catch a fatal error. You can only catch this podcast in your favorite podcasting app. So you can't catch traps in Swift, so you can't catch Fatal Error, you can't catch Tribe, you can't catch Force Unwraps. So if you do that stuff, everything crashes. So I've been pretty good about not having any crashing and trapping things in the app, but still, something happened somewhere and something crashed. It could be vapor, could be my code, could be Swift Foundation, could be anything.

Speaker A
So notably, this undercoverable crash will occur if you access an array out of bounds. But more importantly, if you unwrap something, that if you unwrap an optional that's null. Right?

Speaker B
Exactly. If you force unwrap something that's nil, if you try bang something that fails, there's a few things that can go wrong. And then the problem is that right now, the way we have things set up, there's no way to get that crash report. And that's the real challenge. So I need to invest some time and build some tooling that will like, when it crashes, it needs a supervisor that will watch that PID restart the thing, trawl through the logs, find the crash report, and then email it to me or something.

Speaker A
This seems like something that must exist and other people must have deployed Swift on Heroku and have something like this, right?

Speaker B
Yeah. I've been asking around and I don't have too much on this. I've been also talking with the IBM folks, the people that work on Coutura, and they have something that's set up that will watch the PID and restart the app. But I don't think have anything to catch those traps in those stack traces yet. So that's something I definitely need to figure out. Fortunately, we've only crashed twice so far and then just kind of restarting all the dinos fixes it. It sucks when things crash because it goes down for everybody, not just the one user on the one device, like it is with iOS development.

Speaker A
So you really want to avoid that?

Speaker B
Do you really want to avoid that?

Speaker A
Are you running multiple instances of the server? So if one crashes, like, one can still serve requests or no, it's one Dyno. Okay.

Speaker B
Partially for cost reasons and partially for, like, it's extremely performant on the one Dyno.

Speaker A
Yeah.

Speaker B
So why worry? We use a tiny, tiny amount of Ram. I mean, the Ram graph is just flat at the bottom of this. It's amazing. So that's what happens when kind of things go wrong on Heroku.

Speaker A
Okay, so just to make sure I understand the gist is that when you're writing server side Swift, you want to make sure that you don't use exclamation points, you handle errors and just return like, an error for that request rather than letting the server bomb.

Speaker B
Exactly. Yeah. So almost everything in Vapor is a throwing function.

Speaker A
Okay.

Speaker B
And so you can pretty much try, regular try from anywhere. It's very friendly with swift errors. And I've set up my own middleware to where so I have errors that I catch and I might print out whatever happened into the logs. But then also I have a protocol called externally visible error, which has an external message. So some errors you don't want to expose, right?

Speaker A
Yeah.

Speaker B
If your database query messes up, you don't want to be spitting SQL out to the user. That's not right. So what I do is the ones that I do want to vent to the user. So that'll be like a validation error, hey, you can't join this event because it's already full, your comment can only be 500 characters long, that kind of thing. That is all conforms to this externally visible error protocol. Invalid credentials also conforms to that. And then the other ones just say there was an error, sorry. And so that gives you the ability to sort of separate and make it like so you separate your errors into like, oh, these are just going to completely crash my app. These are programmer errors and I want to catch them and I want to be able to handle them. Maybe I get emailed about them or something in development, I want to actually show the user what happens because I'm the user and then in Prod, like hide those implementation details because I don't want people to know. So one really common thing was this is such an interesting thing. So I have a helper function that I've added, I think, to every project since I started using it, which I call unwrap. It's a function I put on every optional and it either returns the value or it throws a nil error, right, if the thing is nil. So that basically if you're in a throwing context means you never have to deal with optional error handling.

Speaker A
Okay? And this is useful because exclamation point would just cause the whole force unwrap, whole program will die. So this takes the case where it's nil, where it shouldn't be nil, but it might be and like changes it into swift's error handling. And that's something that you can catch with Vapor and handle gracefully still, right?

Speaker B
You can handle it gracefully except the error that you get because a nil error is not really like a domain specific error. So the details that I include with it are what line did it occur on and what file did it occur in? So that when I see that, I can go and say, oh, this time that I called unwrapped, that caused the problem.

Speaker A
Yeah.

Speaker B
So when that happens, obviously I want to know about that because I need to go and fix that because that's a bug. But there are other times when that does represent a real thing. It's just not something that I would want to express to the user. So a concrete example of this is in vapors orm vapors orm is called fluent. And you have like, let's say an event entity and your event entity has a find function on it. Like every model object, every database backed entity has a find function. The find takes an ID and it's a static function and then it returns an optional instance of the actual entity that you're trying to find. So you would do like event find by ID ten and it would return either nil if that ID doesn't exist in the database, or it will return the event itself. Okay, so far so good, right?

Speaker A
Yeah.

Speaker B
The problem is that I had tons of places in my code where I was like, okay, let event equal event find and then I'd pass in the ID, let's say from the path. You might have like, event ID attend that ID from the path, I would extract that and put that in the thing and then it would be optional. And I don't really want to work with an optional because I know I have to have an event here otherwise something's gone wrong. So then I unwrap it using this unwrap function. And then before I had this whole error system set up, the user, like if they basically tried to access, let's say, the comments for an event that was deleted by someone else, it would say, oh, there was a nil error on create or Fetch events command on line 55. And it's like, well, I don't actually care about that as a user. What I really want to know was like, hey, this thing doesn't exist. This is a 404. And so it's funny, in beta testing somebody was like, oh, you're using Swift on the server for this? I was like, oh, that's interesting. We are, how did you know that? And it's because the file name that had been spit out by this nil error had like the Swift, which is pretty funny. So what I ended up doing is essentially making another function on every model called find or 404, which is a throwing function. And so what that does is if it's nil, it will unwrap and it will throw a model not found error which includes the type, and it just figures everything out and just does the right thing. So now I can just freely call try event find a 404 with this ID, and then if it doesn't work, it'll return a correct error that has the correct status code and just does the right thing everywhere. So basically getting out of optional world and getting into Swift error world is like really good on the server.

Speaker A
Cool, that's really good to hear. I know that's something that maybe we've talked about. I know that we've talked about in person. I don't know if we've talked about it on the podcast, but Swift's error handling comes up sometimes in iOS development, but often the right or at least the same thing to do is just to error out and let the program crash.

Speaker B
Right, right.

Speaker A
Yeah. I'm glad to hear that. At least in other contexts, it's really useful and it sounds like pretty powerful.

Speaker B
Yeah. If you're in a context where you can throw, then there's tons of interesting things you can do. So, like we talked about, I think we talked about the promise library many years ago now.

Speaker A
Yeah.

Speaker B
Back in episode four. Really? Yeah, I think it was. I think it was that long ago. Okay. But yeah, in the promise library, because it's not error parameterized, you can throw because it can catch any error. And so when you throw from inside, like my promise then and inside that block when you throw, it just gets turned into an error. So when you're dealing with Nils and other weird things, you can just kind of dot unwrap and everything just works. So if you're in a context where you can already throw, the Swift error handling system is really nice, so you can take quite good advantage of it on the server. And I think I do an okay job, especially when you start defining your own errors and doing rich, interesting things with them, such as 404, such as, oh, this JSON key that I was expecting wasn't there, do something nice for me and tell the user what key was expected to be there but is actually not there. Yeah, stuff like that.

Speaker A
Do you think you're going to take lessons from error handling and Swift on the server and apply them to iOS apps that you write? Or is your error handling style on iOS going to remain more or less the same?

Speaker B
That's an interesting question. I think what it actually comes down to is the fact that everything on in Vapor is synchronous. And so because it's like everything on iOS on the client has to be pretty asynchronous. Just because network requests are asynchronous, sometimes even disk fetches are asynchronous image decoding, all that kind of stuff, you really want that stuff to be off the main thread. And so any kind of thing that I want to do in that realm, I would probably do in a promise, maybe in a signal. And there you already have error handling and that's like how you would handle all that stuff. Whereas here, because everything is synchronous, the error handling really shines. So for example, in Katura, which is the IBM switch on server framework, everything there is evented more like node JS, if you're familiar with that. And so throwing doesn't exactly do the same thing as you would expect. So you actually have like a function on some response that you have to call and tell it, hey, this failed. So it just doesn't work as well. Nothing doesn't work as well. It doesn't work as cleanly with Swift's error handling system. Yeah.

Speaker A
Okay, cool. That's interesting stuff to think about. I think so. I know you're still working on you and Ashley both are. Still working on Beacon, right? Yes. What have you been working on lately?

Speaker B
So the thing we built this week, we built emoji reactions for comments. So when you have a comment, you can click a little button and add an emoji reaction and it will kind of pop up. Kind of like slack.

Speaker A
Nice.

Speaker B
So that's really fun. And the other thing we built was mentions. So you can actually type a user's right? Now they're Twitter usernames and you'll type that in and then when you do that, it will turn into a link and it will send them a push notification so they know that you got tagged. So if you make a new event, you would say, I really want Chris to come to this. You can say. Hey, Chris, I checked. Went out.

Speaker A
Yeah. Okay. That's interesting. So mentioning just in general can be kind of a surprisingly hard problem, right. Using Twitter names simplifies it a little bit, but as someone who started to implement this once for a project a long time ago, if you have names that kind of spaces in them, right. If you're doing Facebook style, if things are editable, that can make things a bit more complicated, right?

Speaker B
Yes.

Speaker A
First of all, are your comments editable?

Speaker B
No. Which makes life a lot easier.

Speaker A
Yeah, just in a lot of ways. Okay. Immutability. Yay.

Speaker B
Immutability. It's kind of nice for programmers.

Speaker A
Yeah.

Speaker B
Okay.

Speaker A
So I guess I have two questions here. First, what is the user experience? Like, are you watching for an app sign and like suggesting usernames? Or do you just have to know a username or copy and paste the username?

Speaker B
Right. So this is a minimum viable product, so there's no autocomplete yet.

Speaker A
Okay.

Speaker B
I obviously would love to have autocomplete in the future, but for now there's no autocomplete. So that makes that side of it a little bit easier. But essentially that would, I think, involves some kind of as they type an ad symbol, listen for the letters after that, and then do some kind of query to the server to see what users there are and then put those in a list, make it happen.

Speaker A
And this is a classic example of where you may want to use reactive programming because you can nicely take this stream of changes and debounce it and apply restrictions to it and then transform that into a request. It goes to a server and yeah, that's kind of like textbook reactive programming.

Speaker B
We should do an episode of reactive programming. That'd be great.

Speaker A
Yeah, that would be great. Have we done that before? We'll add that to the show notes.

Speaker B
Yeah, we'll have to add that one to the show notes for sure. So the nice thing about the mention system, the way we have it set up is it's kind of in memory only so we can actually retroactively apply it to every comment that's already been sent. And there have been some comments that have been sent with mentions already in them. So essentially I have a class I call mention extractor. And so that gets initialized with some string which is like the body of the comments and then has some regular expression that can match against an ad sign.

Speaker A
Is this on the server that this.

Speaker B
Is all on the server, yeah. And it has to be on the server so that you can set push notifications, right?

Speaker A
No, that makes sense. But you may also I could see how you may want to put this on the client too to do things like style it differently or to allow you to click on that person's name, right?

Speaker B
Yeah. So we do actually allow styling and click on the person's name but it's a little bit more clever which is kind of fun.

Speaker A
Oh yeah, let's hear it.

Speaker B
So let's say you go to save a comment. Basically you're going to take your comment body and you're going to run the mention extractor on it and grab all the mentions out of there. A mention is basically just a range and the name and then also means property for name with at. So you add an at symbol to it as well, which is great. So once you have that then you can kind of go look up those users and see if they're first of all you would want to see if they're real because you don't want to send push notifications and you don't want to even create mentions for users that don't exist in the database. And then once you have that, then you have those users based on their kind of Twitter usernames and then you can send all their push notifications out. So that's on create pretty straightforward. There's a little bit of dancing around the fact that if they get mentioned and they were going to get a push notification anyway because they're an attendee of the events, you got to make a decision. Are you going to do both? Probably not. Which one do you want to do? And so you have to kind of like balance that. So we manage all that stuff. Not so bad. But then on the other side where you go to display the thing, we could have taken this exact class and copied it over into the client and said, okay, well when the comment body comes down, parse out the mentions, turn them into links and see where life takes you. But the problem is that the client doesn't necessarily know which at usernames are valid and which are just like bogus that somebody typed that doesn't actually mention anybody service.

Speaker A
Yeah.

Speaker B
So that stuff is all on the server. So what we do is in addition to passing the comment body, we also pass the mentions down as JSON. And so the mentions there are the JSON property includes a username, it includes a range object which has a location and a length and it has like that name with that. And as you can imagine, because it has a location and a length that looks an awful lot like a foundation type called NS range, which you may be familiar with.

Speaker A
Indeed it does. Or just range in Swift now, right?

Speaker B
Well, there are complicated, tricky details between range and NS range. Range doesn't operate on integers because Swift indexes aren't integers.

Speaker A
Right. It operates on string indexes.

Speaker B
Right.

Speaker A
In the context of a string.

Speaker B
Yeah, in the context of the view that you're looking at also.

Speaker A
Yeah.

Speaker B
So don't forget that.

Speaker A
Isn't there a proposal to unify string indexes?

Speaker B
Yeah, we talked about it on the episode 31.

Speaker A
Yeah. We'll add another link to these show notes just to be sure.

Speaker B
Yes. The super nice thing about using NS range, there's two nice parts. One, it's just integers, so you can put it in JSON really nicely as opposed to whatever OPIC index type string Swift string uses. But the other nice part of it is I have NS range on the server and it uses the same implementation for figuring out ranges and finding all the matches of NS regular expression inside an NS string. And so because it's the same implementation, I know that when I get an NS range on the server, it's actually going to be the exact same NS range that the client would have found if it had access to the same data.

Speaker A
Assuming so my only thought here is that assumes that your server and client are both working on the same looking at indexes in the same string view, like the same Utf 16 or Utf eight view.

Speaker B
Right. But the thing is that regular expression doesn't work on Swift string, it works on so you're purely in foundation world.

Speaker A
Okay.

Speaker B
Yeah. And so you get these ranges out and then you know that they're going to be the same because it's the same library backing both it's NS strings on both sides.

Speaker A
Nice.

Speaker B
And so once you do that, then on the client, you can kind of iterate over your mentions and create a new attribute for each range on your comment body and then add the link attribute, add the bolding, the coloring, whatever else you want to do, and you're off to the races. You only have to parse mentions once.

Speaker A
Awesome. Yeah, that sounds like absolutely the right way to do it, I think. Unless you have anything else you wanted to talk about, we should probably end here. It seems like we're going a little bit long.

Speaker B
Yeah, no, that's about it. I'm sure as I do more of this stuff and as me and Ashley discover more interesting quirks of switch on the server, we'll talk more about it. But for the most part it's been really fun and I've been really enjoying it, so yeah, awesome.

Speaker A
I'm glad to hear it. Listeners, if you have questions or things you want to hear about in Swift on server, then let us know. I'm happy to make Sirish answer them.

Speaker B
Yeah, absolutely. That'd be great. So, yeah, cool. It was good to talk to you, as always, Chris. And I will talk to you next week, as always.

Speaker A
And I'll talk to you later.

