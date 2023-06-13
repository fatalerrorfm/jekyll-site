Speaker A
Welcome to Fatal Error. I'm Chris De Zomback.

Speaker B
I'm, sirish. Khanlo.

Speaker A
So this season, we've decided arbitrarily to go in a season of ten episodes. So this season we've talked a lot about software architecture, we've talked about testing, we've talked about the single responsibility principle, we've talked about design patterns. Is there anything we've talked about that I'm forgetting?

Speaker B
Oh, yeah, lots of stuff.

Speaker A
Lots of stuff.

Speaker B
We talked about singletons, we talked about coordinators, we talked about View controllers. We talked a lot about view controllers.

Speaker A
Talked a lot about View models.

Speaker B
We talked about view models.

Speaker A
Okay, so in this episode, we're going to try to make a case as to why you should care about any of this, why you as an app developer, should care about the stuff that we've talked about. This is going to be a little bit less of a technical episode than a lot of the stuff that we've done so far, if that's not already.

Speaker B
Clear, chris, I think our listeners are currently screaming at their car stereos or into their headphones, why didn't you do this episode first? And the answer is because we didn't feel like it.

Speaker A
Well, and the answer, I think, is also because I didn't know that I wanted to do this until about halfway through the season when I added this topic to the episode ideas list.

Speaker B
Would you say it's path dependent?

Speaker A
So in addition to music, we need.

Speaker B
Like, rim shot sound effect, maybe like a groan, maybe? Could we do a groan right there? So that was not bad.

Speaker A
Thank you. Thank you very much. So, okay, it's it's a valid question for you to ask as the listener, as someone who Sarish and I have been yelling at about this stuff for the past six months, okay, this is all great. We can talk about View models and where responsibilities lie and how this stuff works together, but why does it matter? Why do I care about this? And the answer, I think, is that this stuff does matter, abstract as it seems, in that it's reflected in the quality of the product that we make. It's reflected in the quality of your application. It's reflected in the number of annoying bugs, even small bugs that your users see over the lifetime of the application. It's reflected in the number of support requests that you get. It's reflected in the number of crashes that get reported that you see in hockey or in the itunes crash reporting thing. And it's true that depending on the size of your company, depending on how many people work on your app, depending on the age of your app, you can make a case that this matters more or less. But I think that I really do honestly believe all this stuff that we've talked about, thinking about this stuff, really does help drive you toward building a better product, right? Am I wrong about this, sirish?

Speaker B
Yeah, I don't disagree. I might phrase this slightly differently, I might say, like, this stuff is important because your app is important to your users. Chris. You work at the Times. There are people for whom the Times is just a pinnacle of the newsworthiness, journalism, all kinds of stuff like that. And when they see the app and they see a bug in the app, like, that means something to them. It means that the app that they use is as polished as the newspaper that they might hold when their data that's in that app is really important to them. And when you lose that data, people freak out when you have a crash, I mean, that's another form of data loss in a lot of senses. And it should be important to you because it's important to your customers and to your users.

Speaker A
Exactly right. And my particular company is maybe a little bit of an extreme example because of the number of users and the whole sort of institutional I don't want to say institutional baggage, but it's such an institution. Right, but no matter. I mean, you have people using your app. They care about your app. Right. Why do design patterns matter? Why does testing matter? I think these things matter because the reason that we have design patterns, the reason that we try to avoid singleton's, the reason that we're sort of thinking about view models and coordinators and about different ways to model application logic through promises or reactive code, is because these techniques are designed to reduce the number of ways that bugs can creep in. Right. And to increase the testability of our applications.

Speaker B
Yeah, I would say. And testability's ultimate goal is also to reduce the number of bugs in the long term.

Speaker A
Well, right. And testability test coverage also reduces the number of ways that bugs can creep in. Right. But those things do translate into a better user experience. And I'm going to say, even if you're a one developer shop, right. You maintain your own apps, and you're the only person who touches the code. It's been your code for years. I'm going to argue it's still important. Like I touched on in the testing episode, you might come back to an area of the code you haven't looked at in two years. You haven't thought about this. You don't know what assumptions went into this code back when you were writing it. You don't know what edge cases were considered in the development of whatever class, whatever procedures being changed and having automated tests that capture that is so, so valuable. You may end up selling an app to someone else who then has to maintain it. And all of a sudden, all this knowledge about how the parts of the app work that has been in your head, that needs to be transferred to whoever bought your app. Right. And it's going to be really hard to do that transfer if that knowledge lives entirely in your head, if that's not documented, I mean, at least hopefully in comments in your interfaces. But if that's not documented through tests, if it's not clear what interfaces do and how they interact, then whoever maintains this app next is going to have a really hard time and is going to introduce a lot of bugs. And your users who love your app and who made it worth selling your app are going to be really disappointed. Right?

Speaker B
Yeah. They're ultimately the ones that suffer. Yeah. I think in addition to testing, testing is one of the most recent things we talked about, but there's also these other ways in which we prevent ourselves from being able to write certain code. I have been doing a lot of code review recently, so I was in the process of converting one app from just success and failure callbacks, which were just sort of called manually. Like you would just type success, maybe with a question mark if it was an optional closure, and then the parentheses, and it would call that. And there was one particularly tangled flow, and I realized that if a certain request was failing, it would be calling both the success block and the failure block. And it wasn't really obvious that it was doing this for certain reasons and converting things to promises made it just completely impossible to express something where the success block and the failure block were being called at the same time. So the static types that Swift pushes us on while they're annoying, sometimes the abstractions that we use to make our lives a little bit easier, the tests that we write, it's all in service of preventing us from doing a bad thing that ultimately causes a bug, ultimately causes data loss or somebody to be sad down the road somewhere, right?

Speaker A
It's all about eliminating or reducing room for error. Right. And we both are fairly smart programmers and we still, like, write bugs all the time. I would prefer to leave myself as little room to write bugs as possible. So if I have some complex asynchronous logic modeled as a reactive sort of data flow rather than through an ad hoc arrangement of delegate methods and block callbacks, I'm going to say that's a good thing, just because there are fewer ways that events can interact over time and it's something that have thought about and modeled directly instead of almost accidentally modeling. Right, for sure. And that plays into that same example that you just provided, Sirush, with the promises. In place of a callback, I want.

Speaker B
To talk about the counterargument a little bit as well.

Speaker A
Okay.

Speaker B
There's this blog post that Jared Sinclair wrote, and it's entitled the Judicious Use of shitty Code. And I put a link to it in the show notes. He writes, repost still loved and used by some app. Net Diehards has one or two view controllers I wrote that are thousands of lines long. The app was littered with procedures that should have been generalized but copied and pasted everywhere. And it didn't matter if we had had the time reposted as a side project to write all the code quote unquote correctly, it wouldn't have made the app any better for the end user. And I really do feel this argument and I think that there is a sense in which not caring about it can be judicious. You're writing a minimum viable product, you don't know where this thing is going to go and you got to get the thing off the ground. But there's a lot of cases in which if you do that, you end up screwing yourself down the road. So you're kind of making a bet with yourself. And I think the longer term a project is I've worked at a few startups that have had enough runway to say we're going to build an app and we're going to work on it. You don't want to bet that that is going to fail. You know what I mean?

Speaker A
Yeah, no, absolutely. Yeah. This is a really good point and it is somewhat situation dependent. I'm like clearly at my work, at the times, I'm sort of in a place where we have a pretty good idea that the app is going to be around for a while and we want it to be as maintainable as possible. Right, right.

Speaker B
I mean, the fact that you're rewriting it speaks to that.

Speaker A
Yeah, absolutely. And we're rewriting it in Swift with a lot of the practices that we've discussed this season. Right, but you're right, so there's a time and a place for maybe not using some of the best practices that are well known and that have been outlined here. Right. So it varies based on the age of the app, the expectations for your app, how many people are working on it, what expectations are from your stakeholders and how many customers you have already. Right. If it's a very new app where something like app. Net, it's maybe not clear if remember app. Net, it's not clear where it's going to go and you have a limited runway because you're at a startup. I'm still going to argue for like if you're writing something from scratch anyway, maybe use a view model because it's really not that much harder than putting everything in the View controller. But okay, sure, there definitely is a quote unquote good enough, but you have to adapt, you have to accept that really at this point, we're sort of talking about technical debt. Right?

Speaker B
Right.

Speaker A
Like actual debt. I mean, technical debt is a very it's an apt analogy because like, actual debt, it's really useful and it makes impossible things possible. But there's a trade off and if you take on too much technical debt without starting to pay it down as it looks like, hey, maybe this startup is going to be around for a while, or like, hey, we're adding people to this dev team and this is becoming kind of a mess, right. If you don't start paying that technical debt down just like actual debt, it comes back to bite you and it comes back to bite your customers. Because now where you had a six month old app with one developer working on it and that was good enough, okay, well, that's good enough. Now it's maybe a year and a half in and you have three developers touching this app, and the practices that were good enough a year ago with one developer are really going to start coming back to bite you here. So you do have to recognize, as circumstances change, when to start paying down that technical. That when to say, okay, we need to start getting serious about moving some of this stuff up to view models. We need to come up with a sort of overarching principle for like, this is how asynchronous APIs work in this app. This is how the data layer in this app works, right? Because if you don't, you end up with an app that is just impossible to maintain, and your users will start to notice more crashes that happen as developers accidentally violate assumptions that were in place from ages ago that maybe they didn't even realize were in place. Because you didn't bother to put a unit test around that assumption, right? Your users will start to notice bugs that creep in again as, like, interactions between different objects that maybe weren't obvious start coming into play. So there definitely is a place early on in an app where if you don't know where this thing is going, then maybe you can take shortcuts then. But at some point you also have to start paying down those shortcuts or your users will start noticing. Does that make sense?

Speaker B
Yeah, I think it does. There's a really good post that I like about technical debt a lot. I'm really glad that you brought that up. It's called Technical Debt 101. And the point that this author makes I'll put it in the show notes. The point that this author makes is like, yeah, technical debt is important and it's useful, but you have to do it very intentionally. If you don't do it with that intentionality, you have to assess and make a decision like, okay, at this point I'm going to take a shortcut and I'll do this thing more quickly just so I can get it out the door and I'll fix it later. That is what technical debt is. It's not an excuse to write bad code, if that makes sense. It has to be done in an intentional way. You have to be able to write the good code to know that the bad code that you're writing is bad and bad on purpose so that you can be done more quickly, right?

Speaker A
It has to be a willful thing that you're aware of while you're doing it, right? You shouldn't accidentally take out a lot of technical debt. Another sort of corollary that I'll point out is that let's say you want to take shortcuts because you have to get something out and you don't have much runway. You should at least keep track of the shortcuts that you took so that in the future you can start walking those back. You can start making this into a much better app so that as you add developers, as you add users, you can pay down that debt. You can make the app more maintainable so that your users will continue to see what you intend the app to be.

Speaker B
Right. Do you have any tips and tricks for keeping track of the debt that you quote, unquote take out?

Speaker A
I mean, the thing that I think Jared mentions in this blog post is adding a fix me comment. That's definitely one step. Maybe you add GitHub issues with technical debt label right. Or you keep a jira backlog of tech things that we would like to fix in the future. Right. I would suggest keeping this in whatever issue tracking system that you are using for the project because trying to track issues of any kind in two places is a terrible anti pattern and is not going to work.

Speaker B
Yeah. One cool trick I heard about recently is you make a global function. In this case it was for to do's, but you would make it, you could call it debt and you would pass in a date and the body of the function basically logs something out, something really obnoxious with a bunch of rotating light siren emojis that says like, hey, this technical debt date has passed. And so once that date has been passed, it starts logging. And so that way every time you run the app you really feel the pain of oh, I took out this piece of technical debt. I really should go back and refactor this like terrible class.

Speaker A
That is clever. I think in large organizations it's probably useful to have something that's more visible in an issue tracker so that people other than developers can work with it. Right. You can flag to your project manager, hey, as long as if we want to add this feature, we really, really should we should take care of this ticket first so that we are building on a concrete foundation instead of a duct tape and two x four foundation. Right?

Speaker B
Yeah. I've just seen like the project manager will always pick the new feature over the tech debt and the developer really has to push for it to make sure that that tech debt gets paid down.

Speaker A
Yeah, well, that's this part of tech debt like you should that's part of your job. Yeah. You should be aware of that when you're taking out tech debt and make sure that everyone, all the stakeholders and this obviously applies more to bigger situation than in a bigger organization situation than in a startup. Right. But if you're taking shortcuts to get something done more quickly, then the stakeholders should know about that. And on the flip side, if you need to undo one of those shortcuts in order to keep things good for your users, all the stakeholders should be aware of that as well.

Speaker B
Yeah, it's a tough thing to try to express to them. I've had a tough time with it. And the only way I've really been able to succeed at it is to really have concrete examples of. Like, here's a time where we could have fixed this bug six months ago, but we pushed it out for a feature and this bug popped up and we should have fixed it a long time ago.

Speaker A
Yeah. Part of that is like having project managers and other stakeholders who actually trust you and who you actually trust, and that is hard and to some degree who are technical who have at least some technical knowledge. Yeah.

Speaker B
The project managers who are technical are some of the most helpful to me that I've ever worked with.

Speaker A
Yeah.

Speaker B
So Jared kind of ends his post. He says, don't assume that a web service will always give you the values that expect. He's making the argument that it's judicious. There's some shortcuts that you shouldn't take. Don't assume that some index is always within the length of some array. Don't pass an NS managed object between threads. Some corners shouldn't be cut right. And I feel like a lot of this is just the places that you've been hurt and that you've had scar tissue form in previous places. I've had an issue where there's I wrote a blog post about it, but I don't know what this most succinct way to talk about it is. Basically, there's an instance variable that you're keeping in two places, and every time one of them changes, you're trying to update the other one and trying to keep these two things in sync manually. And I had enough trouble with it that I wrote a blog post. We'll put that blog post in the show notes. And so I wrote this blog post and in Code Review a couple of weeks ago, I had a situation where so imagine you have like, a table view controller that has a data source object, and then this data source had three different arrays. It was like all of the data all the data filtered and then all of the data filtered and mixed in with the location. And since you don't necessarily know if you're going to have the user's location, you have to keep both of those arrays around. And I saw this thing in Code Review and I put a comment down. I said, hey, I think this is going to be problematic. I don't know if we should fix it now. I feel like we should get this merged and get this to users. But I'm just putting a flag down here to say I don't think that this is right. And I think this can cause problems for us. And I swear to God, Chris, it was not three days before there was a bug in that exact code because two of the things weren't being kept in in sync and the index paths weren't lining up the way they should be. And it was, it was using an index path from one array and then mapping it to one of the other arrays and the indexes don't line up. And it was crashing and it was just such a crystallization of let it go if you have to. Let it go now to get something out to your beta testers to, as Jared puts it, like, is this app fun or what? To find out if the feature that you just built is fun, do it. But you got to know, hey, this thing could screw up. And it did screw up. We fixed it and it hasn't messed up since, fortunately.

Speaker A
And so the silver lining there is that everybody to whom you communicated, I think this is going to be a problem at some point, will now trust you the next time you say that, right?

Speaker B
Yeah, I'm hoping so, at least.

Speaker A
Hopefully.

Speaker B
I'm definitely going to remember this. I hope they remember this as well.

Speaker A
Well, you can always bring that up as a concrete example. Assuming they actually remember.

Speaker B
Yeah, exactly.

Speaker A
So, yeah. Boy, that's a direction I did not expect this conversation to go in, but right. It can be wise to take on technical debt, but keep track of it and pay it down before your users start seeing the app get really annoying to use.

Speaker B
Yeah. I would say if you want to write code that takes out technical debt, you should at least have a picture in your head, a rough picture of what that code would look like if you didn't take out the technical debt. If you don't, then that means that you don't actually understand the problem and that you're going to cause more problems than you're going to fix. And again, maybe your app is going to go out of business in three months and it doesn't matter, in which case nothing matters. But the only thing that matters is if you can get the money from your customers or from your venture capitalist, keep going. But if that's not the case, you got to know what you're doing.

Speaker A
Right. So one thing that I want to note while we're talking about technical debt is as a possible red flag for when you really should start thinking about applying more better practices, about maybe refactoring, about splitting things out into separate objects that have better test coverage is if you have an area of your app that has some accumulating complexity and that is becoming sort of a pain to work with. This would be a real red flag. Right. If you're in a part of the app that no one really wants to touch and everybody knows that it's a little bit shaky. And your app probably has something like that in it. Now just if I had to guess, the average iOS app probably has one or two areas like this. Those are maybe areas where it's time to really go back and think, okay, how do I apply Solid principles here? We'll do a series at some point on Solid, the acronym. We've already covered the single responsibility principle. How can I start decomposing this object into better defined responsibilities? How can I test it? That's definitely an indication that you should start thinking about that.

Speaker B
I would say yeah, I think it's not just iOS apps. I've talked to people in other sort of verticals of programming and they're just like, yeah, we have one controller. It's 5000 lights of code. It's fine.

Speaker A
I'm confident that this applies to every field of software development except hopefully aerospace.

Speaker B
For sure.

Speaker A
Hopefully.

Speaker B
Yeah. And I think the accumulating complexity is interesting. There are a couple of different metrics that you can use. One of them is called cyclomatic complexity, which counts the number of different code paths that you can have. Basically, if you have an if statement in your code, that's like two. And if you have two if statements next to each other, that becomes four. So cyclomatic complexity can be cool. And there's like different tools you can run to kind of gauge that. But honestly, the best one that I found is just line length is if your class has I would put a cap around 200, more than 200 lines of code. It's time to start thinking about it and time to start time start thinking whether it's a view controller, whether it's some kind of data access object, whatever it is. 200 lines of code is right around when I would start thinking about it. 1000 lines of code is right around where if you need to touch anything, you kind of have to scroll through the whole class and really understand what the whole class is doing. And 1000 lines of code, I would say, is like red flag marker. I got to be honest, I've written View controllers with 3000 lines of code. I've worked on View controllers that are even bigger than that. We've all made horrifying mistakes. Just because you have a view controller that's this big doesn't mean that you're damned to hell. It just means that you got to start thinking about this stuff.

Speaker A
Yeah, I was going to suggest another method of finding areas of accumulating complexity, which would be ask every developer on your team. Hey, what part of this app are you most worried about working in right now? And if two people say the same area of the app, or if three people give the same area of the app, just put that at the top of the list of things that we have to fix. Right. Also on scrolling through a thousand line file and hoping that you understand what's going on. Maybe if you're lucky, someone added unit tests for that file. So it's a big file, but you can at least see what expectations there are. Maybe if you're lucky.

Speaker B
Yeah. I found very few well designed classes that are 1000 lines of code. Does that sound accurate to you?

Speaker A
That's probably fair. Yeah.

Speaker B
I feel like the best classes are the ones that I can glance at. Glance at. I can see the whole class in one screen full and I can just instantly, obviously see what it does.

Speaker A
Yeah.

Speaker B
And if my whole project were that, I'd be thrilled.

Speaker A
Yeah. So I'm not sure that I really have anything else to add here. I just want to reiterate that this stuff matters. Because if you don't pay attention to this, if you don't think about this, your customers will start to notice. In the form of crashes, in the form of weird UI glitches that only happen sometimes. In the form of just obscure bugs that are often difficult to reproduce, or in the form of not obscure bugs that just slip out because they're in some really complex area of the code that you're not testing and that your QA team didn't happen to catch. Right?

Speaker B
Yeah, totally. And I just feel awful when I ship a bug, especially a bad one. One time I shipped the staging version of an app to the app store and it was hitting the wrong database and I was just for like a day, I was just miserable. I was just like, I can't believe I did this. I felt horrible. And I put the infrastructure in place to where I could never make that mistake again. And I feel a little bit better because of that.

Speaker A
Yeah. I mean, part of this process is learning from errors, finding mistakes that you've made, and putting infrastructure in place so you can't make that same mistake again. That's part of something we mentioned in the last episode. Part of test driven development is when you fix a bug, you write a failing test for that bug, and then hopefully that bug can never happen again. Right?

Speaker B
Yeah. That's the dream.

Speaker A
It's the dream. And so it's true that thinking about this does take some care and some attention. And maybe you don't always have a chance to really consider application architecture and design, but eventually you should pay some attention to it or your user will notice. And it takes work. But I think we've all mostly fallen on the side that swift's option type is a good thing in general because.

Speaker B
I think there's holdouts, but it's really.

Speaker A
I think there are still some holdouts, but I guarantee that they have all written many bugs, just as we all have, that proper use of an option type would have prevented. I think we've all shipped crashes that use of Swift's option type would prevent.

Speaker B
Yes, that's definitely true.

Speaker A
That's all I've got.

Speaker B
Cool. Great season. Chris.

Speaker A
I think this has been a really good season. I think we got some good stuff out there. I think we had some episodes that were a little rougher than others, but I think overall, it was pretty good.

Speaker B
Yeah. Yeah, I was really I was really happy to do this. I'm looking forward to maybe seeing what next season holds.

Speaker A
As am I. As always, we welcome feedback on not just this episode, but the entire season. What would you like to see from us next season? And thank you so much for listening. We really do appreciate it.

Speaker B
Yeah. Thanks, listeners.

