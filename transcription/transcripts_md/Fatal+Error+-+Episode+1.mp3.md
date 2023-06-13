Speaker A
Let's do Fatal Error. I'm happy with fatal error.

Speaker B
You're happy? You're sure?

Speaker A
Yeah.

Speaker B
Okay.

Speaker A
I'm sure.

Speaker B
All right. That's what it is. I hope this is the beginning of the episode.

Speaker A
Okay. Hello, everyone. Welcome to Fatal Error. I'm Krista Zomback.

Speaker B
And I'm Sirush Khanlou.

Speaker A
So today we wanted to go over the subject of Coordinators for controlling flow through the View controllers in your application. This is something that I know sir has written about, so I'll throw it over to you here.

Speaker B
Cool. Yeah. The Coordinator is such a mysterious topic. No, it's not that mysterious. I feel like backstory is relevant here. I was diving into writing this app, and I found that every time I was pushing onto a navigation controller from inside of a View controller, that I was doing something wrong. Something just wasn't sitting right. And I actually tried quite a few things and tried quite a few names to try to kind of figure out what am I trying to do here and how can I make it better? I've had workflow objects, and I had there was some other type of object, too, a process object. And the idea was that, okay, let's say you're in an app that has, like, a sign up flow. I don't know why I didn't think of the name Flow. Flow is in workflow, but you have a sign up flow, and let's say you need to collect an email address, and then you need to check if that email address exists. If it does, they continue with the sign up flow, or if it doesn't, you continue with the sign up flow. And if it does, then you can go to a password entry screen, and then that will sort of complete the flow. And it took me a little bit of time to kind of get some of the pieces in place. And I wrote a blog post in January of 2015, and it was just called The Coordinator. And it was sort of about how if you take your View controllers and you make them no longer dependent on each other, sort of the graph of your app is a lot simpler. And the funny thing is, when I wrote this blog post, I hadn't actually implemented this anywhere. So that is like a deep, dark secret of this blog. I hadn't actually implemented this anywhere, but eventually I did, and I took the lessons that I learned from that and I turned it into a talk that I gave at NS Spain in 2015. So that was like, around, I think, September or October. And then I turned that talk into a blog post, which is one of the longest blog posts on my site. It's about 3000 words. Yeah, it's really, really in depth of, like, what exact problems does it solve and how does it solve them and how do you use this thing?

Speaker A
So I was just going to ask you about that. You mentioned that while you're pushing view controllers from other View controllers. It wasn't sitting right with you. Why was that? What what kind of problems do these Coordinators solve?

Speaker B
There's a few problems that they solve. Number one is and I don't know, it's kind of a cutesy joke, but if you have your let's say you have like a line of code in table view did select row at index path? So somebody taps on a table view cell and you need to execute some code. So usually what you do is you grab the object at that index path and then you create a new view controller, and then you grab the navigation controller, who's technically your parents, and you tell it, okay, push this view controller on and it should be animated. And that specificity of saying almost the arrogance of the view controller saying, I know exactly what you need to do next, and I'm going to tell you what to do, flies in the face of a lot of the other type of work that I was trying to do. And I feel like I'm personifying these view controllers a little bit, but that's almost what it felt like. It's like you're grabbing your parent and you're telling your parent what to do. And the joke I made during the talk was that in real life, children should never tell their parents what to do. And then in programming, children maybe shouldn't even know who their parents are. And so basically what that means is that you have a delegate and you don't know who your delegate is, and it's a weak property, so you could just disappear at any point. And you tell that delegate, hey, somebody tapped on this cell. And then your delegate's responsibility is to figure out, okay, what do I do with this data? Am I in an iPad context? Am I in an iPhone context? Is the user being a b tested? Do I need to send off a network request before I actually show this next thing? Should it be a modal presentation or a push presentation? And all these things are like important decisions that you have now sort of taken out of the view controller and you've put in this other place.

Speaker A
And you've done that because the sort of way that you described that you previously did things. You have View controllers which know how they're presented, or which check how they're presented, which check which presentation Idiom they're presented in, and know who their parents are and know how to push other View controllers. And if that's not bad enough, we can stack up here the violations of single responsibility, principle law of demeter. If that's not enough, then they also know about other View controllers, how to construct them, how to build them, what data they need, what dependencies they need, and how to create them and push them. So that's kind of a lot of stuff on top of whatever your view controller is already doing the dependency thing.

Speaker B
Is actually something I didn't really appreciate when I first started working with these. Because if you think about it, if you have a chain of view controllers that's four view controllers long, like one pushes the next four deep. If you have to pass anything to that fourth view controller, you have to pass it through every view controller before that as well. Whereas I feel like we haven't actually explained what the Coordinator is, whereas with the Coordinator, it basically goes back up to its parent each time, and the parent can decide which dependencies does this particular view controller need?

Speaker A
Let's go ahead and describe what a Coordinator is and then we'll get into how they help with dependency injection.

Speaker B
Yeah, so a Coordinator is basically, I find it's easiest to start at the root, which is the App Coordinator, which is basically you need a place to put the code for setting up your view controllers. And perhaps you do that in Interface Builder, perhaps you do that in a subclass of UI tab bar controller, or perhaps you do that in your app delegate. But if you're doing an Interface Builder, that's its own solution. But if you're doing it in either of those other ways, you are trapping yourself and you're putting that code in sort of the wrong place. And so this App Coordinator, its job is to just set up the root view controller and kick off whatever processes are next, whether that's like, hey, I really need the user to log in, and it knows about whether or not the user is logged in and starts presenting, let's say, the Authentication Coordinator. And each of these Coordinators, their job is basically create a view controller, present that view controller in whatever context it needs to be presented, and become that view controller's delegate, so that when a user action is fired on that view controller, that message bubbles back up to the Coordinator. And the Coordinator says, okay, now that this has happened, I know the next thing I need to do is push on this next view controller. And so instead of your flow for, let's say, signing the user up, being in four different objects, where, like, the first one only knows how to present the second one, which only knows how to present the third one, which only knows how to present the fourth one. You have one object, sort of at the top, that knows how to present all four of them. And those four individual view controllers can just focus on presenting their data and handling the user input and validating and whatever other stuff.

Speaker A
So just to sort of recap. So this is an object that sits maybe underneath the application delegate level, but above any of you view controllers and is responsible for creating and displaying all the view controllers in the app?

Speaker B
Yeah, pretty much. I would even make it like a property on the app delegate. I feel like that's where it belongs.

Speaker A
Your application delegate object owns this sort of Root Application Coordinator, and then this.

Speaker B
Root Application Coordinator owns its navigation controller or tabbar controller, which then own their child view controllers. And so you have a very, very clear tree rather than sort of a linked list of view controllers that extends out to that makes sense.

Speaker A
Yeah.

Speaker B
I was working on the app I was working on at the time, it had this whole login flow and I needed to bring it to an extension. And I wanted to pull in the login view controllers that we had because they looked right, like they were the right thing. But then when I did that, it also pulled in the API because that was the dependency of the view controller. And it also pulled in like half of the other view controllers in the app, which didn't need to be in the they didn't need to be in the app extension. This was like a Safari action extension. They didn't need to be in the app extension, but they had to be dragged along because of these explicit import statements and the usage of those classes in these other classes. And I was like, well, this is clearly not going to work. Why does using this login view controller imply that I also need all this other stuff and how can I isolate this login view controller and make it sort of stand on its own?

Speaker A
Right.

Speaker B
Yeah, cool.

Speaker A
So hopefully our listeners now, if they weren't familiar with this concept before, know what a Coordinator does, at least at a really high level, just a way to sort of remove all this view controller creating and pushing and dependency injecting logic out of your other view controllers. And I want to come back and revisit something that you've been getting to a little bit, which is the implications for dependency injection that using a Coordinator has.

Speaker B
Yeah, so the Coordinators, like, I feel comfortable letting them touch a lot of stuff because they're so simple and they're so focused on what is the business logic of the flow, like, what information do we need from the user before we can continue past this step? They get to know that, and because of that, I feel comfortable giving them these high level things of like, okay, this is the object that you use to write to disk, this is the object that you use to hit the network. And those components I ideally want to be able to inject into the view controller because that way the view controller doesn't create them on their own. When if we want to do screenshot testing, which may be a topic of a future podcast, if you want to do screenshot testing, you can inject those view controllers, inject those objects into those view controllers, and you prevent your root view controller from having to know so much about every view controller. That presents like what other dependencies they will need down the road. I don't know if this is just the projects that I've worked on, I assume that it's not, but the root view controller in almost every app I've worked on has been far and away the biggest view controller in terms of number of lines. Yeah, it's not great. So being able to take that root view controller and say, you know what, you're not a special view controller, you are just another view controller. And all you get to do is you get this data and you present it and you let me worry about the rest. Me being the Coordinator in this case.

Speaker A
Sure, that makes a lot of sense.

Speaker B
So have you had a chance to work with Coordinators yet?

Speaker A
So in the app that we started a few months ago at work, we actually have decided to use Coordinators from the ground up. And so, yes, I have haven't actually shipped anything with them yet, but I.

Speaker B
Fully plan to have you all written code with it.

Speaker A
We have, yeah, we have written actually not one, but two Coordinators in this application now. So we have our sort of root application Coordinator, which handles the sort of first level of navigation in the app and the sort of primary functions of the app. And then for something like the settings sort of view or the settings flow that we've started to implement, that is its own sort of child flow controller or a Flow Coordinator. We're calling them flow controllers in our app, but it's the same thing. So when the user taps a setting screen or taps a button that asks for the settings screen, we call up to the root flow coordinator and say, hey, the user tapped the settings button and the root flow coordinator. Goes ahead and presents this child Settings Flow coordinator in a way that makes sense depending on the user interface idiom.

Speaker B
Whether that's like iPad or iPhone.

Speaker A
Exactly right. And then that provides a nice way to sort of segment that one sort of self contained user flow out into its own object. Right, because in a complex app, you wouldn't want to have one flow Coordinator responsible for absolutely everything. That would be a pretty big object. So if you can find ways like I think you mentioned a purchase or a login flow, we have the same idea. We will have a login and account creation flow Coordinator as well. So that's a really powerful idea too. In much the same way that you can now break up storyboards and have storyboard references, you can do the same thing with these flow coordination objects. You can create as many as you want and define how they interact in different cases. And we've also found this subject I keep coming back to, to be a very, very nice way to manage dependencies because this means that each each view controller gets only the dependencies that it needs. It's not aware that there's anything else in the world?

Speaker B
What kind of dependencies are we talking about here? Like, is API client, for example, a type of object that would be a dependency here?

Speaker A
Yes, but through one or two layers of abstraction that are more application specific concerns. Well, right, because you may have an API client, but really what the application cares about is, give me this article, give me this list of articles for this screen. And you can imagine there's probably some Caching, maybe some offline support that sits in between the network API client and the user interface there. So what the dependency that gets injected? Might be something like an article provider protocol that provides an article, things like that.

Speaker B
Got you. And that abstracts away all of the Caching and the networking and all that stuff.

Speaker A
The Caching, the networking, the model parsing. Right, exactly.

Speaker B
That makes sense. You touched on storyboards. Are you all using Storyboards in this app?

Speaker A
We actually are not, no.

Speaker B
Yeah. My feel on it was always that Storyboards or that coordinators replace Storyboards, that the idea is because a storyboard is basically a giant global thing. Like, if you want to access the storyboard, you can access it by name from anywhere in the app that you want. You have to put almost all of your flow inside of this inside of this one storyboard. And you kind of get to do, like, a little bit of breaking up now that you have Storyboard references, but it's a lot more global and a lot more, I feel like a lot of the conditional stuff that you can do with coordinators, you can't do with Storyboards. So you want to say, like, this context, do this in that context, do this other thing. But someone emailed me, and I have a blog post here, and I'll put it in the show notes, and it's from this April, and he wrote about how to combine Storyboards and Coordinators.

Speaker A
Interesting.

Speaker B
Yeah, it's very weird. I just want to point people to it because it's super interesting. There is some swizzling involved. There's some intense stuff going on.

Speaker A
Oh, boy.

Speaker B
Yes. I wouldn't necessarily recommend this for sort of production use, I believe is the correct phrase. But I would maybe say if you want to think about an alternate way of structuring this stuff together, that this article might be a place to take a look at what someone else tried to do and how that works and what its benefits and drawbacks are. I think it's he also wrote a blog post, like, a couple of days later that was about, okay, I did make this thing. But also, here are the downsides. And he also lists them out, which I think is also really nice. So we'll link to both of those in the show notes, and you can take a look and see what you think about combining those two things.

Speaker A
So one other thing that I don't think you mentioned. But that is one of my problems with Storyboards, particularly with Swift, is again, injecting dependencies into these View controllers. If you have a non optional dependency that you want to give to a View Controller and you're using a Storyboards, you can't pass it the dependency into the View Controller's initializer. So the options you're left with are to have an optional property or to have an implicitly unwrapped optional property.

Speaker B
Well, it's even worse than that, right? Because you can't actually get a handle like, let's say you're in your app delegate and you create your dependency that you're going to want to inject. Can you actually get a hold of the View Controller that gets created by the Storyboard?

Speaker A
You mean of a root View Controller in the application delegate?

Speaker B
Yeah. So there's a root View Controller that gets set up.

Speaker A
You can I forget exactly what the syntax is. There is a way to manually instantiate the first View Controller from that Storyboard.

Speaker B
So you can't take it machinery. Right.

Speaker A
So that's one other problem that I personally have with Storyboards, which I know is a contentious issue in our community, for sure, but that the Coordinator approach solves quite nicely in my opinion.

Speaker B
And I think the Storyboard thing kind of pushes you in the direction of like, oh, just use a singleton, it'll be fine, just use a Singleton, it'll be fine.

Speaker A
So the counterargument to what I'm saying would be use an implicitly unwrapped optional. If you really need a dependency and it's not there, what are you going to do anyway? That's a valid argument as well. It comes down to sort of whether you think it is a failure you can handle gracefully, at least in production, and throw an assertion in Debug Mode.

Speaker B
But I just like having my Swift Lint rules in place and not having to remember which times the implicitly unwrapped optional is okay, and which time it's not. Okay.

Speaker A
Sure. Yeah. This is our approach in this code base is generally no exclamation points.

Speaker B
Yeah. Trying to get there with the project I'm currently working on, but we will get there slowly, one by one, removing the exclamation points.

Speaker A
Yeah.

Speaker B
So there's actually one or two more things that I want to bring up. One is like a non obvious usage note with Coordinators, which is that I actually and this might make you a little bit uncomfortable, Chris, but I actually have my Coordinators do two things, not just one. So they do control the flow, but they also decide when to mutate the model. And the mutation of the model is dependent on whatever app you're in. That might mean writing to the database, that might mean writing to the API, it might mean a lot of different things. But the reason that I have it do that is so that the View controllers don't know. Like you can abstract it behind a dependency and that's good. But sometimes, let's say the user hits like it's some kind of Twitter app or something, a very contrived Twitter app where you hit post but you haven't logged in yet. And so when you hit post, the app is actually going to need you to log in. And so where normally it would just write to that API or write to the thing on disk or whatever, do the mutation. In some special cases, it needs to do some additional information gathering. Maybe if you're about to delete something, it needs to ask you with an alert controller like, hey, are you sure you want to do this? And in those cases, because the lines between mutation and flow control are so blurry, I actually take all that mutation and pull it up one level into the Coordinator. Yeah, and I detail some of those reasons in the blog post, but you can kind of see, like, okay, if I want to change this flow and if I want to add one of these features, such as another controller that asks you if you want to really delete the post or if you need to log in before you can post something, you need to be able to answer those questions with all the data in place. And so you can't necessarily do that from the view controller. You could kind of contrive some situation where you would pass it, some object that it would tell in the case you're not logged in, and some object that it wouldn't. But I feel like just take all that out of the view controller, treat it almost as a dumb view, where all it does is bind the view to the model and pass those user input events up to the Coordinator and let the Coordinator handle deciding what to do with that user input.

Speaker A
So this sounds a little bit like we're getting onto the subject of what I would call view models rather than mashing them.

Speaker B
This is that a future podcast topic?

Speaker A
I think this is a future podcast.

Speaker B
Topic that sounds good to me because.

Speaker A
I certainly can see and appreciate the argument for not having the view controller do all these things both again, from a single responsibility point of view. And just because you're right, you end up with sort of messy delegation between the view controller and the Coordinator in some fairly somewhat complex conditional logic.

Speaker B
Right, right, exactly. And that's what you're trying to get rid of, right?

Speaker A
Yeah, absolutely. Well, you're trying to get rid of that, or if not get rid of it, you at least don't want it in a view controller.

Speaker B
Yes. Well, yeah, there's a cool thing that you can do with Storyboards, which is like, if you would normally in a view controller, you would have this basically this conditional that says, like, if Idiom is iPad, then do this thing, and then else in the case that it's the iPhone, do this other thing. Pushing that decision up to the Coordinator is really cool. Not only because you get it out of the View controller, but if you push it up to the Coordinator, instead of having a conditional in the Coordinator, you can actually just completely swap out the Coordinator and say, I don't even have an iPhone Authentication Coordinator, I have an iPad Authentication Coordinator, which does different stuff. And so you've actually taken that conditional entirely out of your code, except at the source, where you decide, like, is this an iPhone or is this an iPad? And that to me, is the total dream of not having that conditional in your code at all.

Speaker A
Cool. Yeah, that makes a lot of sense. Absolutely.

Speaker B
Yeah. So that's kind of what I'm after. And to get that, I feel like you have to pull model mutation up into your Coordinator. Now, I'm curious how you guys do it, because you all have Coordinators, but you also have View models.

Speaker A
So let's save discussion of View models for a future episode.

Speaker B
That's probably a good idea.

Speaker A
And we can open that episode with an explanation of what we're doing in our app, which I think is the best of several worlds. We avoid having any sort of model interaction or API interaction in our Flow Coordinators and we also keep it out of our View controllers.

Speaker B
Right, I look forward to hearing about that.

Speaker A
I look forward to talking about it.

Speaker B
I have one last thing, which is a small story, and it is one of those behind the blog. It's like a story that I've been meaning to share on the blog, but I haven't had a chance yet. Some delegates, sometimes an object that Apple provides for you has delegate. And that delegate really naturally suggests its own implementation. So one really good example of this is, if you remember back in the day before we had Nsurl session, we had Nsurl connection and Nsurl connection delegate. And so what you would do is you would create an object and that object would hold on to an Nsurl connection, and then it would conform to its delegate, which would have methods like did begin, did get data, did finish getting data, and then failed with error. And so it's your responsibility to take all that data and append it together into one continuous piece of NS mutable data and then convert that into whatever you expect it to be. And it was a really unwieldy API, but it was at least clear that you had to make a fresh object for it. And everybody did, and everybody made their own. And there was on top of that came Ashtp request or ASI Http request and AF networking and its Http request and all that stuff. But that was a cool delegate because it suggested how to use it. And part of when I was trying to figure out how does UI navigation controller delegate work? Like, let's say I need to know about some action or something that happens to the UI navigation controller. No one view controller in the flow really has a right to be that delegate. And so sometimes you just say, okay, well, it's the third one, because the third one is the one that needs that data. But then if the fourth one takes that away, then the third one can't do its job. And so part of where this idea came from is also like, okay, what if UI navigation controller delegate was an object? What if that was just the thing? And where does that take us? And it was that that kind of led me into the direction of like, okay, well, if we had this object at the top, and now that you have a coordinator, you can say, okay, I'm in charge of this UI navigation controller, I obviously would be its delegate. Who else would it be? And then when you get pieces of data like UI navigation controller back button pressed or whatever the delegate method is, you can take that data and do something with it, pass it to all your children, do whatever you like, pass all your child view controllers, do whatever you like. You have a complete control, and you don't have to worry about who the delegate will be because it's very clear who the parent of that UI navigation controller is. Cool.

Speaker A
Yeah, that makes a lot of sense. So this pattern almost falls naturally out of some of Apple's APIs?

Speaker B
A little bit, yeah, you kind of have to squint at it, but I feel like it does kind of naturally make sense when you think about it from that perspective.

Speaker A
Or at least it solves one problem.

Speaker B
Right. The rest of the problems will have to wait for a future episode.

Speaker A
Well, that's why we have a podcast.

Speaker B
That's right.

Speaker A
On that note, I don't think I have anything to add here.

Speaker B
Cool. Yeah, I think we just about covered it.

Speaker A
Ready to button this up?

Speaker B
I sure am.

Speaker A
All right, well, thank you, everyone, for listening to the podcast now known as Fatal Error. We will talk to you in two weeks.

Speaker B
Sounds good. Talk to you later, Chris.

Speaker A
Bye, sirish.

