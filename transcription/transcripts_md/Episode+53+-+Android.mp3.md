Chris Dzombak
So what do we want to talk about today?

Soroush Khanlou
That is a great question, Chris.

Chris Dzombak
I would like to hear about your Android and Kotlin and Java experience.

Soroush Khanlou
Yeah, we gotta do that for sure.

Chris Dzombak
Want to talk about that?

Soroush Khanlou
Let's do it.

Chris Dzombak
Hey, everyone. Welcome to Fatal Error. I'm Chris.

Soroush Khanlou
And I'm, sirous.

Chris Dzombak
So today we were going to talk about Android. Sirous, I know that you've been doing some Android dev. You've mentioned that on some of our calls recently. And so I want to hear about what are you doing with Android and what's it like? I haven't written any Android code since probably 2011, so I assume it's changed a little bit since then.

Soroush Khanlou
I couldn't speak to how it's changed, but I will tell you what my experience is. Basically, I have a client, and we've talked about this client before. A lot of their users are based in the Middle East and North Africa. And the reason this came up before was we were talking about how their Internet connections aren't as good as ours. And including the swift runtime with the app was basically a non starter. And so what we did was we ended up writing the app in Objective C so that we wouldn't have to pay that cost. Now, of course, that works for all the people who have iPhones, which there are a lot of people who have iPhones in that region, but more people have Android phones. And so we knew we needed an Android phone at some point. And once we kind of had done the proof of concept of the iOS app, we were like, all right, we got to do this Android app. And I really didn't know how we were going to do it just because I didn't know how to do Android. Basically all I knew about Android was activities are like view controllers, something which turns out is not quite right.

Chris Dzombak
Yeah, it may be interesting for us to compare and contrast some of these things between Android and iOS, but activities have their own lifecycle and the application lifecycle is less concrete what's the right word? Yeah, it's less concrete than it is on iOS. And you have these activities that really have their life cycles that really make up the application.

Soroush Khanlou
Yeah, exactly. So I basically probably spent maybe two weeks just trying to get a tab bar on the screen. It was a lot of work. And so they don't really have in Android world. So one of the first places I started was the sort of Objective C-I-O article on it's called Android 101 for iOS Developers. We'll put that in the show notes, and I figured this would be perfect. Right. This is exactly what I need to know to get started. And it was completely inscrutable.

Chris Dzombak
Really?

Soroush Khanlou
I read it. I read it again. I read it a third time, and I did not get almost anything out of it.

Chris Dzombak
Let's see. So they did a whole issue on Android. This was back in April of 2014, according to this page. Do you think that this is outdated by now, or what did you find inscrutable about it?

Soroush Khanlou
I think part of it is that it's outdated, and part of it is just that it doesn't really do that good of a job explaining what you're working with. One of the big things is activities versus fragments. And I feel like I didn't understand at all when I would use either one.

Chris Dzombak
That's something that I have wondered as well. So it might be helpful for us to cover what activities are they're basically like a screen that appears a screen of the application that appears on screen. And unlike iOS, where you launch an application and then the application is responsible for navigating to whatever screen you need to go to, or like displaying a home screen where the user can navigate, it's possible on Android to launch a specific activity of an application. You can launch into different points in the application. And so in that way, the application lifecycle is sort of split among a bunch of activities which are maybe more independent than view controllers on iOS, if that makes any sense.

Soroush Khanlou
Yeah, I think that's basically a good way of thinking about it. The other important thing is you can only ever have one activity on screen at any given time. So I kind of like to think of the activities as each little mini apps. And so because of that, it actually made sense to put our entire app into one activity, which is crazy. Yeah. So once I started to figure this stuff out, I realized, a, there's no tab bar controller on an Android. There is a control that you can use at the bottom of the screen that functions like a tab bar, but you don't get that automatic switching. You have to write all that stuff yourself. And then there's also no concept of a UI navigation controller where you would say, okay, I want to look at this screen, and then when the user taps this, I want to look at.

Chris Dzombak
The next screen just to back up for a second. We talked about activities and you mentioned fragments, but we didn't talk about what those are.

Soroush Khanlou
Right? So I'm getting there.

Chris Dzombak
Okay.

Soroush Khanlou
Basically the way that if you think about it, like iOS world is you would say, okay, well, every screen in my app is going to be a certain activity. And then when I click or when the user does something, I will change the activity. And that works to a certain degree, but you can't change just part of the screen the way you would with like a UI tabbar controller. So with tabbar controller, you have one kind of parent view controller that's a tabbar controller. And then it has sub child view controllers that switch around. They don't have that. And you can't do that with an activity. So you end up having to do this really hacky thing where you say when you switch activities, keep these views on screen in the same place so you can kind of fake it.

Chris Dzombak
So fragments are like views that can be shared between activities somehow.

Soroush Khanlou
Yes. That brings us to fragment. So if you don't want to do that weird trick where you tell the activity to change, but you don't want to change the whole screen and you want to keep the tab bar there and you're basically saying, okay, keep this tab bar here, but then underneath it change the activity. If you don't want to do that, then you have to use something called fragments. And so a fragment is basically the best way to think about it is like it's a child view controller, only it starts to be hosted within an Activity, which is like a parent view controller, and it has access to data in the same way that a View controller does. And then it has views. Like a view is its own thing.

Chris Dzombak
And it has its own life cycle too.

Soroush Khanlou
Right. It again has its own life cycle, which is actually even worse than the Activity lifecycle. A lot of the reasons people don't like to use fragments is because their life cycle is really bad.

Chris Dzombak
What do you mean by really bad?

Soroush Khanlou
I haven't run into this yet, so I don't really understand what people's problem is. But basically my understanding is that as you get to a more and more complex app, you start to run into the limitations of the fragment lifecycle. Basically. Yeah. There's a library from Lyft called Scoop, and the idea is like it's scoops of ice cream that you stack on top of each other. It's very cutesy. And Scoop is designed to basically replace fragments because they hit this point where their fragments were getting too complicated and they were kind of hitting up against the limit of what fragments could do. And then so they basically made this whole almost UI framework around it.

Chris Dzombak
Wait, so this replaces fragments or it.

Soroush Khanlou
Yeah, it completely replaces fragments. The Scoop. I don't use this.

Chris Dzombak
Okay, so you're not using this, but this library provides some sort of router. It says View Controllers, layouts. Oh, I want to talk about layout. Like view layout on Android as well.

Soroush Khanlou
We definitely will get there for sure. That's super interesting part.

Chris Dzombak
Okay, but so fragments are sort of like reusable, at least in theory, reusable sort of child view controllers that have their own life cycle.

Soroush Khanlou
Right. And if you want to ever have an iPad style, like on a tablet where you have two activities next to each other, because you can only have one activity on screen at a time, you have to use fragments. So fragments are also kind of more future proof in that way.

Chris Dzombak
Okay, so there are these building blocks and I misunderstood earlier when I thought you were saying that they could be shared between past between activities, but you're saying that you might have one activity and fake a transition between different things by changing between fragments within one activity.

Soroush Khanlou
Yeah, so that's what I did end up doing. I basically have one activity. It's my whole app. And that activity behaves both as a coordinator and as a tab bar controller. And so what it does is it has a method where, depending on which tab you tap, it'll say, okay, based on this tab switch, and figure out what fragment to build and then animate to that fragment. And then if you tap on something within that fragment, you are the delegate of that fragment as well. And so it behaves like coordinator. So you'll say, okay, well, I tapped an image in this fragment. Okay. You figure out what the next thing to do is, and in this case, it's slide on a thing, kind of like a navigation controller push. That code is also all in the fragment.

Chris Dzombak
That makes sense, I think. How complex is this app?

Soroush Khanlou
I would say less than ten screens.

Chris Dzombak
Okay, so that's not true, but it's not complicated, right?

Soroush Khanlou
Yeah. It's not a joke app, but it's also not like, I'm sure left app is 50,000 lines of Kotlin or whatever.

Chris Dzombak
Yeah. Oh, right, we have to talk about Kotlin.

Soroush Khanlou
That's right. Yeah. That's definitely a fun part of it as well.

Chris Dzombak
So maybe what are your sort of overall impressions of, I don't know, the sort of activity and fragment application lifecycle? And then I want to hear about Kotlin. I want to hear about Tooling in general. Want to talk about view layout.

Soroush Khanlou
Yes, I have a ton of thoughts. Just real quick before we move on, the kind of, like, combination tabbar controller coordinator thing is 114 lines of code. So not super complicated.

Chris Dzombak
Yeah, that's not bad.

Soroush Khanlou
Not bad. Even though it does have this role of controlling everything that's on screen. And what happens when different buttons get tapped. All told, it's still 115 lines of code. Not too bad.

Chris Dzombak
I feel like that would probably be more code in iOS, even with Swift, just because of the frameworks.

Soroush Khanlou
I would guess that that's right. Yes. Yeah, I agree with that.

Chris Dzombak
Just, you know, not because Swift is more verbose, but just because achieving that with the building blocks that we have.

Soroush Khanlou
Yeah.

Chris Dzombak
Okay.

Soroush Khanlou
I'll just basically leave that there. Okay, so what do I think? I think basically the ecosystem that you work in is just worse than iOS. Things are more fragmented.

Chris Dzombak
Fragmented?

Soroush Khanlou
Well, there you go. There you go. Yeah. Things are more fragmented. It's not clear how to do stuff. If you look at the popular apps on the platform, all of them do things in a different way. So there's this back button, right? And then you have, like, a back.

Chris Dzombak
Yeah.

Soroush Khanlou
So you can tell things to be added to the backstack, but then if you look at an app like Instagram. It has a back button at the top left, just like iOS, but then also the back button does the same behavior.

Chris Dzombak
Yeah. This is my recollection from coding on Android and from using Android for about a summer back when I was learning to program for it, was that it was never clear what the back button was going to do. It varied depending on what application I was using as a programmer. I wasn't sure what was supposed to go on the backstack. And some applications have their own sort of back infrastructure, and it was just really confusing.

Soroush Khanlou
I agree with that. It's kind of like the escape button. When you're using a computer with a keyboard, when you hit it, you don't always know what it's going to do, but you have a safe feeling that it's going to cancel whatever you're looking at or stop whatever you're doing or get out of wherever you are. It's not super concrete what it does, but it is always there.

Chris Dzombak
All right, I guess that makes sense.

Soroush Khanlou
Yeah. I don't particularly use it when I am testing my app. I don't use Android on a day to day basis, but when I'm testing my app, I don't really use it. But it is there to kind of get you out of situations.

Chris Dzombak
Okay. Are you testing this app on an actual hardware or are you using the Android emulator?

Soroush Khanlou
I bought a really cheap Android phone. I bought the Alcatel A 30, and it is $100, no contract, which is unbelievably cheap.

Chris Dzombak
And what do you get for $100?

Soroush Khanlou
You get a phone. You get 16GB five megapixel selfie camera, five inch display. I'm just reading off of Amazon at this .2 Gigs of Ram. I mean, you get a real phone.

Chris Dzombak
That's really impressive.

Soroush Khanlou
Yeah, it is slow and it does drop frames and whatever, but it's a phone and it has access to the Google Play Store. It's not like a fake Android phone where they just don't give you access to the Google stuff. It has Google Assistant, it has Gmail, it has all that stuff.

Chris Dzombak
That's pretty cool.

Soroush Khanlou
Yeah. And then there's also a version that you can get that has ads or whatever. And it's like, even cheaper than that. But I got the no ads because I don't need to look at ads.

Chris Dzombak
That's probably the right call.

Soroush Khanlou
Yeah. So. Yes, I have that. And then I think if I keep working, I'll probably get like a pixel two or pixel one, even, as my full time Android phone. But there's also you also have to remember that the people that are going to be using your apps are not going to have the latest and greatest, like, 4GB of Ram and all the crazy camera and stuff.

Chris Dzombak
Oh, absolutely.

Soroush Khanlou
The camera on this thing is so bad, it's comical. Like, in my room with the light on, which is not dim by any means, but it's also not like bright sunlight. Things are just dark. It's just dark. It's really comical. And you compared to any generation in the last five years of iPhone, they have pretty good low light performance and.

Chris Dzombak
This thing just can't yeah, well, it's $100.

Soroush Khanlou
Yeah, how can you complain?

Chris Dzombak
Yeah, man.

Soroush Khanlou
Yeah. So I got the Alcatel, I started programming and it's a camera app, basically. So I needed to test on hardware. And they actually do some cute tricks when you're kind of doing the camera in the emulator. They'll kind of set up like a moving checkerboard grid so that's like the camera image and then when you click capture, it'll capture that image. So you can actually test it in the emulator. But it's just better to have a device. So I got a device, I started programming and I had no idea what goes in the activity, what goes in the fragment, like how do I break down data, how do I communicate between fragments?

Chris Dzombak
Oh yeah, how do you do that?

Soroush Khanlou
Well, I started in Java. I was like, I'm not going to learn kotlin yet. This is too much to learn all at once. Let me just start with the simple thing because I know a little bit of Java. Let's get this off the ground. Pretty much the only communication pattern in Java is like message sending. There's no blocks, there's no notification center, there's no as far as I know, there might be like a note, but I don't think there is. There's none of that stuff. And so the way you do stuff is you basically do this thing where it's like an inline subclass. Have you ever seen this pattern? Oh yeah, it's like a big time Java thing. So basically what you do is something expects like a listener, right? Like an on click listener. And so the listener, the type that it expects is an interface which is like a protocol in objective C or Swift World and has one method that's like on click and it'll pass you whatever. And so what you do is you basically write some code that in line, creates a class that conforms to this interface or protocol and overrides that one method and then you can do your behavior in there, which is, as you can imagine, totally horrible and that's funky. Yeah, that's like the main. So right now I'm looking at some code. So the bottom navigation view, which is what they call UI tab bar, it has an on navigation item, selected listener, and that gives you the item from which you can get the item ID and then kind of do your thing from there.

Chris Dzombak
Now if you're working within an ID, especially there are shortcuts for autocompleting, most of this sort of boilerplate code. And I think in newer versions of Java, actually they have much more concise ways to do this. But as I recall, Android doesn't support those newer Java language features. Just yet.

Soroush Khanlou
I think that's right. So there's Java Eight, and Java Eight has real blocks, which is huge step up. But I don't know. I didn't really look into running Java Eight just because nobody really talked about it. So I was like, maybe this is impossible. And also I knew I wanted to move to Kotlin at some point.

Chris Dzombak
Okay, that makes sense. Yeah.

Soroush Khanlou
So I'm basically dragging myself through broken glass, like trying to make this Java stuff work because okay, so remember in Java you can't extend any classes. You can't make extensions or categories, which means anytime you want to add a helper function to, let's say, a file object, you have to make a file utils class and then add a static method. It's horrible. So that stuff there's all this crazy inline subclassing protocol conformance thing, which is like its own mess. And I'm also learning Android at the same time and it's just like it's not really working. So I was like, let me just take a day and see what I can do with Kotlin and it's way better. First of all, just off the bat, I started screaming once I was writing Kotlin code. Like it was way faster. I was just like, it was awesome. But there's a bunch of other crazy stuff around it. So for example, you can right click on a Java file and say, convert this to Kotlin for me. And it just does.

Chris Dzombak
Whoa.

Soroush Khanlou
Yeah, and it's not perfect. It messes up some of the optional stuff, it messes up some of the little things, and then some of the patterns are not quite as elegant as you would maybe want them to be. But it works. It's Kotlin and it basically gets you 98% there. And then you kind of scan through the class, make sure everything makes sense, and then you can kind of test it, compile it, test it, and commit it. Which is pretty good.

Chris Dzombak
Yeah, that's awesome. So that feature comes from JetBrains and it's built into the Android studio, which is just a JetBrains IDE, right?

Soroush Khanlou
Yes, it's free. I don't really understand the relationship, but it is free. And I think Google is the one who maintains it. But it is built on top of the back of basically Eclipse.

Chris Dzombak
I think. It's no longer Eclipse, but it's built on because Android studio used to be just an Eclipse plugin. Basically back when I was working with Android, I think a while ago, it changed to be based on IntelliJ idea.

Soroush Khanlou
I thought IntelliJ and Eclipse were the same thing.

Chris Dzombak
Oh, no, they're definitely different.

Soroush Khanlou
Okay, that's my bad. Yeah, it's based on the JetBrains stack, which is like app code. If you're coming at this from an iOS perspective, I thought Eclipse this was based on Eclipse.

Chris Dzombak
No, it used to be JetBrain stuff is way better than Eclipse.

Soroush Khanlou
Got you. Yeah, I can agree to that. I thought it had just gotten better, but it's a different thing and it is definitely better. There's other stuff, too. So if you paste code that's Java, let's say you got some code from stack overflow because you're a really good developer like me, you can paste it in line and it will translate it to Kotlin for you.

Chris Dzombak
That is wild.

Soroush Khanlou
It is so cool if you have some code where it's like, create an array loop over some other array, test some condition based on that value, and then conditionally append it to that array. It'll prompt you to change that to a filter in Colin.

Chris Dzombak
Wow, it's really good.

Soroush Khanlou
It'll prompt you for maps. It'll prompt you for if you have like so then they have like you could map something and then do filter not null. So to remove basically flat map we're changing that.

Chris Dzombak
Yeah. What are we changing it to?

Soroush Khanlou
Compact map that one.

Chris Dzombak
Yeah.

Soroush Khanlou
But basically if you have a map and then a filter not nulls, it'll prompt you to change that to a map not null.

Chris Dzombak
Okay, cool.

Soroush Khanlou
It prompts you to do this stuff. And it's so cool if there's a variable that could be private because it's not being used anywhere. It'll prompt you to make it private if it's got so many little things that just like, it's just like constantly popped up. These little light bulbs are like, hey, you could try this. Hey, you could do this.

Chris Dzombak
I think the JetBrains guys have or the JetBrains folks have a reputation for being on the ball with stuff like that and sort of attention to detail and providing really in depth, like language, I don't know, analysis and refactoring tools.

Soroush Khanlou
Yeah, it's very impressive. It works pretty well. I'm pretty into it.

Chris Dzombak
So that's the experience of using some of the tooling around Kotlin. What's your experience been like with the language itself?

Soroush Khanlou
So the language itself is fine to me, it seems to make compromises in order to work on the JVM, which are compromises that I'm happy to make because it means that I can use this in Android, but if I didn't have to make those compromises, I wouldn't want to.

Chris Dzombak
Yeah.

Soroush Khanlou
So let me give you some examples of this.

Chris Dzombak
Yeah, please do.

Soroush Khanlou
So what are some good ones? One cool thing is so we mentioned inline subclassing protocol, conformance thing like this on click listener type of thing. One of the cool things is if you just use a block column, we'll just kind of promote that to one of these inline subclasses. Okay, that's pretty useful. But it has to do that because it has to work on the JVM, right? Yeah. There's no concept of a value type or a struct because you can't represent that in the JVM. This is my understanding. Email me if I'm wrong. But you can't really represent a struct on the JVM. And so it's represented as a class. And then so they give you something called data class, which if you use a data class. It basically gives you a bunch of methods for free. So it'll implement or derive a hash value for you. It'll derive equatable conformance, it'll derive a description, it'll derive all this stuff for you based on the properties of the thing. And all you have to do is basically type the word data before your class. And that's pretty cool, but it's ultimately not a value type like at the end of the day.

Chris Dzombak
Yeah, I mean that makes sense. I feel like at least the first one of those turning blocks into these boilerplate classes that implement one interface that may have more to do with just needing to interrupt with Android libraries than running on the JVM.

Soroush Khanlou
Yeah.

Chris Dzombak
Okay, so what were some of your other examples?

Soroush Khanlou
So another big one is you can't have structs, you also can't really have enums. Those aren't value types. And so the way that that works is they have something called a sealed class. And what it is, is basically imagine you define a class and then inside the body of the class you can subclass it, but nowhere else.

Chris Dzombak
Weird. Okay.

Soroush Khanlou
Yeah. So basically I rewrote my promise library in Kotlin, obviously, which could probably be its own episode, but what I end up doing is you basically say sealed class, state generic, over T, and so that defines your sort of type, your broader type, or in this case your superclass. And then inside I have several subclasses of that and that's the only place that you're allowed to subclass the thing. And then the really interesting part of that is you can add specific data to those subclasses. Right, and that's kind of like an enum with associated values, but then you can also add specific functions, just only specific cases.

Chris Dzombak
Interesting.

Soroush Khanlou
Exactly. And then because those cases are actually fully blown types, you can actually cast it. So you can say like, okay, I'm going to make a function that expects only state fulfilled. Right. And then state dot fulfilled might have a function on it. So then your function basically accepts one of these state fulfills, because state dot fulfilled is just another class that's another type. So then when you do your switch statement, once you're in the block where it knows that it's a state dot fulfilled, you can pass it to that function and then that function doesn't need to switch on the enum again because it knows that it's that case of that enum.

Chris Dzombak
Okay, that sounds really cool, actually.

Soroush Khanlou
Yeah, it's kind of nice.

Chris Dzombak
Yeah, that would be really nice.

Soroush Khanlou
So it's pretty cool. So you can add your own data and your own functions to your sort of edom cases, which is wild, or you can also add the same function to all of them and then you can call it on all of them in the same way you would with Swift.

Chris Dzombak
Yeah, that makes sense. Comparing this to Swift briefly, there have been a couple enum related proposals on Swift Evolution recently, which we should discuss in yeah, we got to talk about that.

Soroush Khanlou
Sure.

Chris Dzombak
That's been on the list for a few weeks now. We should get to that. I would also note there are some things in Swift which are a little bit maybe a little bit ugly or a little bit workaround, specifically because of interrupt with Objective C and with the existing cocoa objective C APIs.

Soroush Khanlou
Yeah, like the add Objective C protocols, like subclassing from NS objects, other weird stuff you can do.

Chris Dzombak
Yeah. I wonder if that I guess all I'm saying is we can't hold that against Kotlin too much.

Soroush Khanlou
Right? Yeah.

Chris Dzombak
Glass houses and all that.

Soroush Khanlou
That's right. Yeah. But, you know, for the most part, the language is actually a real pleasure to use, especially compared to Java. But basically the column people are not afraid of giving their users or their consumers of that language things that are nice in the worry that they might have to take them away at some point. Swift is very conservative about adding stuff. Right. If you want a function that just operates on sequences of optional values and removes all the Nils, they just didn't give us that until Swift Two gave us flatmap. But then still you had to write flatmap like dollar sign zero. They never just gave us what Colin calls filter not null. And I don't really have a great answer for why Swift doesn't give us some of that stuff, but they just don't. And when you contrast that with Kotlin, kotlin just gives you everything. Have you ever written any Ruby?

Chris Dzombak
A little bit. I mean, not a whole lot, though.

Soroush Khanlou
Have you used the Tap method, which I think is in active support part of Rails?

Chris Dzombak
No, I haven't.

Soroush Khanlou
Okay, so imagine that you need to construct a value and then you need to modify a little bit, and then you need to return it. Right?

Chris Dzombak
Okay.

Soroush Khanlou
The normal way you do that is you create a reference, set it equal to assign it to a new instance of the thing, modify the thing, and then write return the variable that you created. Right?

Chris Dzombak
Yes.

Soroush Khanlou
So what tablets you do is Tap basically takes a block and then returns the original value. So you could just write return, construct a thing, Tap, and then modify the thing inside the block.

Chris Dzombak
Oh, cool.

Soroush Khanlou
It's really handy. I use something called then in Swift, which is like a little micro framework that lets you do basically the same thing. It's even better in Swift because it lets you do it in line when you are defining an instance variable, if you can kind of imagine that. So that's super useful. But you have to add that to Swift yourself. Whereas in Colin it's just there ready to be used. And they have a couple of different forms of it.

Chris Dzombak
So it's more of like batteries included, kind of.

Soroush Khanlou
Exactly, yeah. Okay, so. For example, there's one function called Also. So any type in the system, you can type like whatever, Also, and you give it a block and then you can modify the thing in the block and the block returns void and then it just returns the original value. Or there's another one called Let which basically will let you map a single value, if you can imagine that.

Chris Dzombak
Okay. Yeah.

Soroush Khanlou
And then if you call let on an optional, it'll actually unwrap it on the inside and it behaves somewhat like map optional map.

Chris Dzombak
Okay.

Soroush Khanlou
In the same way we have iflet in Swift, they just have let. And some of that stuff is just really nice to use. And so, like I mentioned, they don't really have good patterns for communication between objects. I just started using the delegate pattern. I talked to some android people and they were like, it's fine, you can do that if you want. And so what I end up doing is when I'm switching for my tabs, I'll create a new fragment and then I'll write dot Also, and then I'll set the delegate to self, essentially.

Chris Dzombak
That is really nice. Yeah.

Soroush Khanlou
And because Also returns the value and it'll intuit the return, you don't even have to write the return.

Chris Dzombak
That's nice.

Soroush Khanlou
So you just write galleryfragment Also. It delegate equals this. It is their version of dollar sign zero.

Chris Dzombak
Okay, cool.

Soroush Khanlou
Yeah, it's super, super nice. And it's just like swift just won't give you that stuff.

Chris Dzombak
Speaking of the delegate pattern and memory management, do you have weak references built into Kotlin and or Java somehow?

Soroush Khanlou
No, you don't need them. It's just since it's because it's garbage. Garbage collection. Right. When that becomes its own retain cycle disconnected from the root of the app, it'll just sweep it away.

Chris Dzombak
So Kotlin is also garbage collected, right?

Soroush Khanlou
Yes.

Chris Dzombak
How has working with a garbage collected language been? Have you run into any problems or challenges or has it been pretty transparent for you?

Soroush Khanlou
Totally chill. Totally chill. I have not had any problems. I haven't really noticed any garbage collection happening like slowing down my app. Although to be fair, I haven't been looking that hard. It just kind of works. It's nice.

Chris Dzombak
Cool. That's great.

Soroush Khanlou
Yeah. I bet there's some gotchas like if you weren't used to it, automatic reference counting could bite you and you just wouldn't know because you would like cause a retain cycle and you would just never see it. But as far as I can tell, seems very chill. Cool.

Chris Dzombak
Another thing I was wondering while you were talking about all these sort of nice features in Kotlin, was how did you learn Kotlin? Like, what reference materials did you find helpful? I'd like to throw some of those in the show notes.

Soroush Khanlou
That is a good question. For the most part, I just Googled what I needed to know how to do stuff.

Chris Dzombak
Okay.

Soroush Khanlou
Basically I kind of try to keep abreast of things that are happening. So I've read, like, Kotlin intro tutorials, like, how is Kotlin different from Swift? That kind of thing before, so I knew what I was getting into.

Chris Dzombak
Okay.

Soroush Khanlou
There's a cool talk by Brandon Williams and Lisa Lozer, I think is how you pronounce her last name. And it's called anything you can do, I can do better. And it's about comparing Swift to Kotlin and saying, like, anything Swift can Do, Kotlin can do better. And it's a cool talk. I'll put in the show notes, and that gave me a good picture of, like, okay, how do these things compare?

Chris Dzombak
Cool.

Soroush Khanlou
Yeah. Oh, I'm sorry. It's lisa Lowe. L-U-O her, like, Twitter username is loser or loser as I think it's kind of like a self deprecating joke.

Chris Dzombak
Yeah, well, definitely. We'll put that in the show notes, and I'm interested to watch this myself. I'll do that later tonight after we record.

Soroush Khanlou
And then yeah, a lot of sample code on the Internet, and then when they use stuff like let it also I would like, command click on it, and that'll jump you to the definition of it in the column standard library, and then you can kind of examine it there.

Chris Dzombak
Nice.

Soroush Khanlou
Another cool, weird thing that I'm reminded of is if you have a function that's a single line, you don't need braces.

Chris Dzombak
Okay, cool.

Soroush Khanlou
Yeah. So haskell also has this. But basically, if you want to write a function that you can express in a single line, you just put an equal sign and then write the expression, and that turns it into a function and everything. And when, which is their switch statement, and if are expressions, not just statements. So if can evaluate to something and return something.

Chris Dzombak
Oh, nice.

Soroush Khanlou
Yeah. That is really cool. So you can write, like, return if this case, do this, if that case, return that. But you only need one return outside of the if. It's great. And then you could do the same thing with switch statements. It's great. I'm into it.

Chris Dzombak
That is really nice. Yeah. That's something that I wish other languages that I use could do.

Soroush Khanlou
Yeah. They've said why Swift doesn't do that, but I forget the exact reason.

Chris Dzombak
Yeah, I know there's been discussion about that, but I can't remember anything specific. Offhand if you, the listener, have any insights or can remember any links about that, please let us know, because I should know that.

Soroush Khanlou
Yeah. Ruby, I think, is a language where if statements and switches are expressions, which is nice, but I don't think Python is.

Chris Dzombak
I don't think so. Offhand although I'm not a Python expert yet, so you'll get there. Yeah. If you're ready to switch gears from Kotlin, I do have a couple other things that I wanted to ask about before we wrap up here.

Soroush Khanlou
Yeah, go for it.

Chris Dzombak
View layout on Android is something that I'm really curious to hear you talk about and compare to auto layout on iOS.

Soroush Khanlou
View layout is awesome.

Chris Dzombak
Yeah, isn't it? That's totally a leading question.

Soroush Khanlou
Yeah, there's a couple of things here. So every view can have an associated XML file, right? And they call those layouts a couple of cool things. So one is when you define that, first of all, you edit that XML file by hand, and so you don't really have to worry about merge conflicts and stuff because you know exactly what you're editing. There's also a visual editor. Yeah, right. Like let me touch the code. There's also a visual editor which you can use, but it's kind of like a maybe it's nice to use that, but really the core representation is this text XML file, which is great. Then when you define that XML file, the root value of the XML file, you get to decide what kind of layout it is. So you can choose a constraint layout which functions a lot like auto layout, or you can choose a relative layout which kind of lets you position things relative to other things, or you can do an absolute layout which works more like iOS like frame based layout, or you can do a linear layout which behaves a lot like a stack view. And so each time you create a view, you kind of get this chance to decide what is the best form of layout for this. And it's very much not a prescriptive like just use auto layout for everything. Which I feel like our community falls into the trap of sometimes.

Chris Dzombak
Yeah, absolutely.

Soroush Khanlou
And so you get to have this explicit decision that you have to make at the very beginning and it's so cool.

Chris Dzombak
Well, not that you have to make that you get to make. Right, right. Everyone was really excited when was it iOS nine that introduced stack views? Something like that, right?

Soroush Khanlou
It was earlier than that, but yeah.

Chris Dzombak
Ios eight something, and it's really great. And you can nest stack views to create these really? To create more complex layouts, even though it's kind of slow because auto layout but you can actually do that. People have been doing that on Android since 2010.

Soroush Khanlou
Yeah, exactly. Also, in my face, it was iOS nine. You were totally right.

Chris Dzombak
Yes. So you may be writing Python, but I still remember some iOS trivia, all the good stuff.

Soroush Khanlou
Yeah, so that part of it's really dope. I'm really into that. And then the other cool part of it is you get to decide when you're what they call they call it inflating a view. When you're inflating a view, you get to decide which layout you're going to use. So iOS, there's a tight one to one coupling between the class and the XML file that's associated with it, if you choose to use ZIBs. Right, yeah, not so with Android. With Android, you get to choose which layout you want. So if, let's say, you could AB test the user in code and then inflate a different layout for them in different cases. It's a little bit more boilerplate than the iOS way, but you get to choose which layout you want for a thing which is awesome.

Chris Dzombak
So you can attach like, totally different UI layouts to the same underlying view code yes.

Soroush Khanlou
To the same class.

Chris Dzombak
That's pretty cool. I don't think I knew that was possible.

Soroush Khanlou
Yeah, it really rules. And that also gives you the ability to since it's no longer one to one, you could take not only can you have one class that can be backed by multiple layouts, you can also have multiple classes that are backed by one layout. Also deduplicating code.

Chris Dzombak
Yeah, that I know. And that is really, really useful.

Soroush Khanlou
Yeah. And then the last thing with the layouts I want to touch on, which is awesome, is, again, in this world of like, Kahlin just gives its users cool stuff. In Swift, let's say you're writing Swift, you have an instance variable, and that instance variable is not going to be set up at init time. What are your options?

Chris Dzombak
Your options are make it an optional, make it lazy, which requires it. Well, you can't make it let.

Soroush Khanlou
Yeah. So you can't make it let. You can't make it lazy because it's not going to have a value. Lazy only works if you know what it's going to be, but you don't instantiate it yet. So you can make it an optional. Yes. And there's one other option.

Chris Dzombak
You'Re going.

Soroush Khanlou
To have to so basically also the same thing. Implicitly unwrapped optional.

Chris Dzombak
Oh, yeah.

Soroush Khanlou
Use that sweet, sweet exclamation point.

Chris Dzombak
And that really is like implicitly unwrapped optionals are kind of, at least as I recall, the Swift team's recommended approach for this. If it's something that you know is going to be initialized right after the class is initialized, but just isn't initialized in the classes initializer for some reason, then I think the standard answer is it's okay to use an implicitly unwrapped optional in that case.

Soroush Khanlou
That's right. That's what it's for. And so for a great example of this is IB outlets. They're not set up until awake from NIB or something. And so you just got to use implicitly unwrapped optionals. Yeah, and implicitly unwrapped optionals make me feel real gross. I don't know why. They just make me feel real gross. I try to never use them.

Chris Dzombak
I do, too. I had kind of been coming around to the idea that for things like IB outlets, where really at no point in the class's life cycle, I don't know, for things like that, I was starting to come around to it, if only because that's how they say that you should write Swift. But I've never really liked it.

Soroush Khanlou
Yeah, me neither. So the way that Kotlin does this, which I actually do not have a problem with at all, is they have a keyword called late init. And so you just say like late innit VAR and then the name of the property and then the type of the property, and it behaves exactly like an implicitly unwrapped optional, which they also do have that, but it just like semantically, it tells you, hey, this is what this thing means. And if you try to access it, it'll throw a specific semantic exception.

Chris Dzombak
So that's what I was going to ask is how this actually differs in behavior from an implicitly unwrapped optional.

Soroush Khanlou
Yeah. So basically two things. One is you don't have this implicitly unwrapped optional in your code, which I like specifically for the reason of like, if you have that capability, this late init capability, you can just say implicitly unwrapped optionals are not allowed ever. Don't do them. And I think that's a much easier rule to follow than like, well, it's okay in this case. In this case, but not this other case.

Chris Dzombak
So you could make a role on your team that says late in it is okay, but implicitly unwrapped optionals in general, not okay.

Soroush Khanlou
Exactly.

Chris Dzombak
I'll allow it.

Soroush Khanlou
Yeah. And then it gives you a specific exception as well. It says, like, hey, you tried to access this variable with this name on this class, and it gives you all the metadata you need instead of that is nice. Yeah, it's really cool. And if we had property behaviors, I guess we could build this ourselves. We don't.

Chris Dzombak
We're going to get that someday, right?

Soroush Khanlou
Yeah, maybe. Joe graph hit me up on Twitter.

Chris Dzombak
Joe Graph replied to one of my sue a joke on Twitter today. I was very happy.

Soroush Khanlou
Both your joke and his joke were very funny.

Chris Dzombak
His joke was very good. Yeah.

Soroush Khanlou
So Latent is really cool and then I get to use Latent without feeling guilty. That like, oh, I haven't set this up in a new time and I have to use an exclamation point. Yeah, also exclamation point overloading not into it because of the not operator and the implicitly unwrapped operation. Implicit unwrapping operation, right. Yeah. So in general, android's cool. There's things that I would change about it if I could, but there's also things that I would steal for iOS world. The tooling in particular. I didn't really get it to go into too much detail, but the tooling is so good. Renaming stuff is really good. You can rename a layout and it will rename where that is used in the code.

Chris Dzombak
This is something that I had meant to touch on and I kind of hinted at with the JetBrains shout out. But they really do have a reputation, a well earned reputation for putting together very good development tools.

Soroush Khanlou
Yeah, I don't love the app itself. It's very obvious that it's a Java app and there's a lot of really non standard keyboard controls.

Chris Dzombak
To show my hand here. This week I've started playing with, or I guess last week I've started playing with IntelliJ Idea with the Python and Go plugins for the development that I'm doing. And so it definitely is clearly not a Cocoa app. It doesn't feel extremely like a Java app either. It fits the platform kind of well. I've rebound a couple of keys to things that are more familiar, particularly in that text editor, and there are some tweaks that you need to make. But even with Python, they're doing things in Python that I didn't think were possible with the language that wasn't compiled, where you don't have even type annotations to do static analysis. It's really good.

Soroush Khanlou
Like letting you refactor stuff.

Chris Dzombak
I don't know if you can refactor Python. I think you can at least do.

Soroush Khanlou
Some extract a method or rename a class.

Chris Dzombak
Yeah, definitely. I know there are definitely renaming operations you can do, and I think there are some other refactorings that you can do. But even just jumping around to definitions, searching for finding where things are declared and where things are used, just stuff like that, that you just don't get in a text editor. And it's really impressive. I mean, after using it for several hours, it's impressive.

Soroush Khanlou
So you could get this stuff for iOS. I mean, they have app code.

Chris Dzombak
Yeah, I mean, that's definitely true. If I go back to iOS now, I'll be more tempted to try app code. But my feeling there was always that, like, Xcode is the sort of the first class citizen there and there. There are always going to be things that you can do in Xcode that I can't do elsewhere. And especially with the newer refactoring tools in Xcode Nine, I had kind of thought that it's not really worth trying. This other weird IDE, it seems like it's always going to be second class, especially in things like Swift support. But I mean, honestly, maybe I should have given it a fair shake, and I definitely will next time I'm doing some iOS work.

Soroush Khanlou
Yeah, I've tried to give it a fair shake and I can't get into it.

Chris Dzombak
Well, maybe you're getting used to the tooling now with Android Studio and I am with the Python plugin. So maybe we'll come back to that. We'll revisit this in six months.

Soroush Khanlou
Yeah, maybe we should. Maybe we should. Yeah. It's just that the non nativeness really gets to me. Like you mentioned, the text editing stuff.

Chris Dzombak
All the text editing horrible shortcuts are non standard command backspace. Kills the line instead of just deleting to the beginning of the line.

Soroush Khanlou
Yeah. And it puts the cursor on the same place in the line before.

Chris Dzombak
Yeah. So the thing is, all this stuff is like, you can customize all these key bindings. I haven't put a lot of effort into this yet because I want to try to learn to use it in its more or less natural state. But I've rebound a couple of the text navigation keyboard shortcuts already. And I mean, you can do that and then fix things as they annoy you and it works out.

Soroush Khanlou
I should do more of that. It's a good environment to work in.

Chris Dzombak
Yeah, it definitely is. Yeah. I've been very impressed with the stuff, the Python Go stuff that I've tried so far.

Soroush Khanlou
Yeah.

Chris Dzombak
I think we're running a little long. Do you want to wrap up here?

Soroush Khanlou
Sure. Yeah. So that's my feeling on Android, the state of Android in 2017. I haven't really written much Android in 2018 yet. I was going to say it's been two weeks.

Chris Dzombak
I'm still writing 2017 on my podcast.

Soroush Khanlou
I'm glad to have learned a lot about Android. I'm glad that I could make an Android app now if I need to, clients get at me. I can make your Android app. I could do the full service. I could do the top to bottom. It's an interesting world. iOS has a lot to learn from it. It is fragmented, but that's the price you pay for some of the crazy cool stuff you can do.

Chris Dzombak
On the topic of fragmentation, I was going to ask if you had any experience with the compatibility library.

Soroush Khanlou
Oh, yeah, we didn't even talk about that. Yeah, the compatibility stuff is its own thing, man.

Chris Dzombak
Can you give me a quick thumbs up? Thumbs down here?

Soroush Khanlou
Mostly thumbs up, but sometimes okay, imagine you have a fragment and then that fragment owns some object, and then that object owns some object. If you import the regular fragment, then you'll get the regular sub object and regular sub object. But if you import the compatibility one, you'll get the compatibility ones. And then the types of them, like, let's say the third level down in that tree, are not the same. The types are different.

Chris Dzombak
They're different types.

Soroush Khanlou
So you write a function saying, oh, I accept a fragment, and then your ID imports fragment automatically, but it imports the wrong one. And then you try to pass it to a function, it gives you some meaningless error. Yeah, so there can be weird stuff like that, but for the most part it works. And I get to use stuff that I wouldn't get to use otherwise on old phones. And that is very cool.

Chris Dzombak
That is really cool. And I mean, this is a way that Android has paid, has put some effort into backward compatibility, even backporting user interface features and things like that in a way that you just don't get on iOS, period.

Soroush Khanlou
I could talk about this for hours. There's also a bunch of really cool, interesting concurrency stuff. Concurrent is interesting as well.

Chris Dzombak
We've been talking for almost an hour here. Let's do another episode. Soon we'll cover Java util concurrent. We'll maybe dive into more detail on stuff like, I don't know, the compatibility library and what we could learn from.

Soroush Khanlou
Code gen. We could talk about all the other different types of XML files in the system. Them.

Chris Dzombak
Yeah, there's a lot to talk about.

Soroush Khanlou
It's cool. There's a lot of stuff that iOS the iOS ecosystem should just steal straight up. Should just steal it.

Chris Dzombak
Yeah, I totally believe that.

Soroush Khanlou
Yeah. Android.

Chris Dzombak
It's a thing.

Soroush Khanlou
It is a thing.

Chris Dzombak
All right, let's wrap up. It's great to talk to you, as always.

Soroush Khanlou
Yeah, talk to you later, Chris. Bye.

