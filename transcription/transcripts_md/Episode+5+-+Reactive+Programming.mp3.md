Chris Dzombak
Mutable state, man. Knowing nothing about this bug, I'm gonna go ahead and diagnose it in order to make a point.

Soroush Khanlou
That's exactly right.

Chris Dzombak
Welcome, listeners, to episode five of Fatal Error. I am Krista Zomback.

Soroush Khanlou
And I'm Sirish Kamlo.

Chris Dzombak
And today we're going to talk about reactive programming. Or I will talk about reactive programming, and Sirish will ask me questions. But first, there's a really fun story that that everyone should know, which is a story of how Sirous and I actually met and became friends. And he's better at telling this story than I am. So I'm going to throw it over to you, Sirous.

Soroush Khanlou
I I appreciate that it I think it would be remiss if we talked about reactive without talking about the story of how we met. I usually write blog posts that have they're measured? I would say, with one exception, it was a blog post just titled Reactive Coco. And I just sort of took a very simple example of somebody using reactive cocoa. And this was back this was February 2014. So was that even before Swift came out?

Chris Dzombak
Was that 2014? I could have sworn it was even earlier, but it may not have.

Soroush Khanlou
Yeah, I'm looking at the dates, february 2014. I think it's right before Swift came out. And they had a simple example of how to use reactive cocoa. And this was back in the objective C days, and I think reactive was especially ugly back then. And so I just kind of wrote this really short post, just with two examples. We'll put this in the show notes, one of the reactive example, and then one of just sort of a delegate based, really simple example. And I close the post with just the sentence, it seems that people are looking for something new rather than something good.

Chris Dzombak
I couldn't let that stand.

Soroush Khanlou
I guess one of my friends, Jason Brennan, who is also Chris's friend, we didn't know we had friends in common because we didn't know each other at the time.

Chris Dzombak
Shout out. By the way, Jason is a wonderful human being.

Soroush Khanlou
Great guy. Jason linked to my thing on his blog, which is where Chris saw it. And then Chris gave kind of a snarky version of what I was saying, basically suggesting that a hello world in objective C was more complex than a hello world in Bash, and therefore sarcastically saying, well, objective C must be useless, then, given that it's so complicated for this seemingly simple example. And then we both kind of felt weird about it. And so I wrote a or I think actually Chris wrote a more in depth post about why he thinks that this stuff is good, and it actually has words and paragraphs, like a real blog post. And so then I felt guilty.

Chris Dzombak
I actually wrote wrote something with a thesis and supporting points.

Soroush Khanlou
It was crazy.

Chris Dzombak
I felt very bad about that blog post after I wrote it.

Soroush Khanlou
Yeah. And then I felt guilty because I was like, well, now I've trashed this thing that so many people have worked on. And then I also made this other person feel very upset. And so I wrote a blog post. We'll put all four of these blog posts. It's very much a back and forth into the show notes, and then we kind of, like, left it at that. And I can't remember if you reached out to me or if I reached out to you, but we decided to get a beer because we both lived in New York. You worked at The New York Times at the time, and I worked at Genius maybe it was still rap genius at the time. And we got a beer, and we talked it over, and I don't know what steps were in between, but now we have a podcast together.

Chris Dzombak
And as I recall, when we got beer, we actually barely talked about reactive programming at all.

Soroush Khanlou
I think we just kind of, like, hung out and just got to know each other. It was a good first date. That's actually what it was.

Chris Dzombak
Yeah, it was great. It was really great.

Soroush Khanlou
So that is the story of how me and Chris became friends. And I think it's only right that we talk about it when we talk about reactive and reactive cocoa in these things.

Chris Dzombak
Yeah, I think that is absolutely fair.

Soroush Khanlou
So now that we've kind of, like, introduced the topic, chris, I think you know way more about this. You've actually written code in this style before, and I haven't. So could you basically give me a high level? Like, why would I want to write code like this?

Chris Dzombak
Absolutely. So this all actually should go with the caveat that I've written relatively little, very serious reactive code over the last several months. So you'll have to bear with me on maybe on some of your questions, but all right, let me start by going back to promises, which we discussed in our previous episode. That gives you a type that represents a promise of some future value. Right. It says, like, we're going to get some result from this asynchronous operation at some point. We'll have some value or some error state here.

Soroush Khanlou
Right.

Chris Dzombak
So it's a little bit of a nicer approach to some common Asynchronous programming patterns.

Soroush Khanlou
Right, that makes sense.

Chris Dzombak
So one of the things that we mentioned in that episode or that I mentioned maybe, is that what if you started thinking about generalizing that to something that what you wanted to deliver more than one event or more than one value? So, as an example, you might think of something like a button being tapped on screen. That's not something that you probably want to model with a promise, because then you could only model that button being tapped once, and that promise would transition to its completed state. Right?

Soroush Khanlou
Right. We have the app that I'm currently working on. Basically, you subscribe to changes in a socket thing. In this case, app is to be firebase you like in the same way that you would model an API, just a basic rest JSON endpoint with a promise that doesn't make any sense when this changes stream to you. So you have to use something like reactive or some bad version of it, basically.

Chris Dzombak
Right? And a traditional cocoa way to go about this would be with a delegate relationship, right? Another example, which is in a different domain but is very similar, might be that you're taking data from an accelerometer or some other sensor, right? That's a continuous stream of values. That's not something that you can represent with one completed promise, right?

Soroush Khanlou
Right.

Chris Dzombak
So the idea with reactive programming, as I'm going to pitch it, given our last episode, is that we take this idea of promises of a type that represents some future value and extend it to represent more than one future value or maybe more than one future value. And the way that reactive Coco, one of the very popular reactive programming frameworks for iOS, defines this as, quote, streams of values over time. So rather than a promise where you get one value or an error and the promise completes with a reactive stream or reactive signal, as they'd be called in this world, you might get multiple values and that stream might continue to deliver values indefinitely. Or you may get several values and the signal might complete or might error out and deliver you with some notification that this stream has completed or that the stream is finished with this error.

Soroush Khanlou
Got you. I have sort of an implementation detail question. Do you get one error or can you get a stream of errors as well or does it vary based on implementation?

Chris Dzombak
Typically you would get one error. The error, like with a promise, is like a single completed state of a signal, right? If you had something that where you needed to model a stream of errors, like you're trying to model some outputs from some other process that seems more like you might have a signal of errors or of some result type from the other process.

Soroush Khanlou
I got you. I have to say that when reading about all those stuff initially, I've kind of come around on a lot of it. I was very anti in the beginning, especially when the listener reads those old blog posts, I was pretty anti and I see some of the value. But I have to say that the stream of values over time analogy, like the stream part is right, but the over time or the I heard data flow a lot when describing what this reactive stuff is all about, I feel like it didn't help me as much as I would have liked it to.

Chris Dzombak
Sure.

Soroush Khanlou
I feel like it wasn't quite the right analogy for me to really or quite the right model in my brain for me to get it sure.

Chris Dzombak
And you're right that some of this terminology is more or less helpful for different people. Absolutely right, exactly. So I'm hoping that introducing it more as this sort of almost natural extension of a promise type might be kind of helpful for some listeners. And like you mentioned, the overtime part of it is kind of abstract. But think about writing, I mean, code with promises or with callbacks or with any sort of asynchronous programming pattern, whatever your language provides, really, you are sort of programming over time already. Right. Like you're probably doing that implicitly, but you're taking yourself out of this sort of instantaneous flow of execution and writing code that's going to happen at another point in time.

Soroush Khanlou
Yeah, I guess I always thought of that as like later, even though obviously that is like some model of time, but I always thought of it as later rather than as we move forward through time. But it makes sense. It didn't help me in particular, I think, try to understand what I was.

Chris Dzombak
Yeah, that's not totally fair. So to sort of continue with my pitch here, something that you mentioned is dataflow. And I'll extend that to say that a lot of what we're thinking about in this sort of reactive programming mindset is thinking about not just data flow but event flow or what events trigger or beget other events are transformed into other are transformed to values somehow. Right, right. Or thinking about how one event might trigger something else to happen in your program which might get some data, which may be transformed into some other data which might be delivered somewhere. This is something that is common to express in Coco or iOS applications. Right. We have the user taps a button and something happens and we get data and it gets transformed somehow and displayed. But typically that sort of flow, that application flow, that event flow, that data flow is I'm not sure obscured is exactly the right word, but I'm going to go with it right now.

Soroush Khanlou
Right.

Chris Dzombak
That kind of flow is often obscured behind interfaces for the different types in your application and separating things into different types isn't a bad thing. I'm not saying that at all. I'm saying that it can be very, very helpful whether or not you're using reactive programming, actually. But especially if you want to use a reactive programming pattern to get into this mindset of thinking of how events and data flow through your app or might be transformed throughout the flow of your app in sort of a functional programming mindset as time continues forward or as your program receives inputs or receives responses.

Soroush Khanlou
Right. I would say perhaps instead of obscuring that flow, what you're doing with a signal or an observable or whatever you want to call it, a stream, you're making it rigid. You're defining strictly what that signal looks like and you're saying this might have originally been a delegate and it had some shape. But now I'm telling you that this is a signal and it behaves like all signals and you can combine those signals in useful ways.

Chris Dzombak
Yeah, that is exactly what we're doing. So we have these signals which represent values or events over time and we can combine them in different ways, we can transform them with common functional programming sort of functions of transformers. And you're right, that's exactly what we're doing. We're taking this thing, this flow that would normally be somewhat obscured and actually modeling it really directly in terms of how these events and values interact with each other. Because you're right, that is something I neglected to mention initially is that these signals can be combined and chained somewhat like you might chain promises, right, and transformed. Something that you might do very commonly would be to map one signal. So take values of one type as they are received over time and transform them into values of another type and send them on down the line, or apply some transformation to them and send them on down the line. So as one example of how this might work and then we can get into some more Q and A, maybe consider that we maybe have a button that the user taps that triggers a network request, that maybe we take that network response and use that to kick off another network request. And finally we take that and get some text out of that response and display it to the user. That's something that you can sort of intuitively tell how we might map into common iOS patterns like delegate pattern and maybe promises if we're using that. But you could also imagine that the button exposes a signal which emits some unit value every time the user taps it. And then we map that using just the standard map operator into an Nsurl request that gets sent off. And then when that response gets back to us, we map it into another Nsurl request and then that gets sent off via some reactive wrapper for Nsurl session. And then when that response comes back, we can again put it through another just map block to transform it into whatever we need for the UI. And the user interface can be subscribed to that result signal and those parts may still be split across different types. Right? But rather than having this asynchronous API sort of defined ad hoc via callbacks or delegates or whatever, these types would all expose these signals which can be wired up to each other in a really consistent way, right?

Soroush Khanlou
They kind of fit together kind of nicely, right?

Chris Dzombak
So this way, rather than exposing a method with a callback block or some sort of delegate interface, a type might expose just a signal that's generic over, say, the type string. So you know that every time you get a new value from this signal, that value will be a string.

Soroush Khanlou
Yeah.

Chris Dzombak
So that's sort of one somewhat contrived example in that I contrived it about ten minutes ago here. But let's see where you have questions like am I doing a decent job of explaining these ideas?

Soroush Khanlou
I think you are. I think with that last example, you hit on one particular thing, which is that we went from this sort of like very abstract world of we have signals and the signals become transformed. And then I feel like it kind of got a little bit technical and a little bit hostile almost with the way that some of the terminology just it is sure. I don't know, a little cagey, I think. I think there is that's one of as I've kind of developed my feelings about reactive and kind of played with it a little bit and read a lot more about it. I think one of the big things with it is that the terminology is so like at the very end and it just subscribes to the signal and it's, well, how does that happen and do I need to care about it and what does that interface look like and what does that mean? And there is a lot of terminology and a lot of lingo and jargon that comes with it that I think is one of the things that's kind of tougher to grasp.

Chris Dzombak
Sure, that's absolutely a valid point. So in that specific example, to subscribe to a signal just means that you have a block which will be executed with the new value that comes across this signal, which you could think of almost as a pipe. Right. So every time a new value comes across this pipe, your block gets called.

Soroush Khanlou
I think, from person to person, the exact analogy that is most I don't know that fits the best with your brain, I think varies. I think for me, the best one is subscribing to a thing like you're saying, I want to be a subscriber, I want to subscribe to your newsletter every time you change, I want to hear about it. Whereas for other people, I think pipe is a good analogy that they really like, especially that's very friendly in the JavaScript world because they deal with streams and pipes specifically versus signals versus observables. And for one person being able to say, well, I want to observe this observable that might have the same depth of meaning that somebody saying I want to subscribe to this signal, or whatever words you choose, you end up choosing. Yeah. So I think there's a bit of a terminology thing there that when I thought of it as a subscription, it really clicked for me. I was like, oh yeah, inasmuch as I have other reservations about this, subscribing to a thing that seems super useful, I can definitely see how I would want to subscribe to your newsletter or whatever.

Chris Dzombak
Yeah, I'll give one more example for subscribing, then move on to a little bit more general language or terminology point for sure. Another way to think about subscribing may be just like writing a then block for a promise, right?

Soroush Khanlou
Exactly.

Chris Dzombak
Except that it might be called more than once. Right?

Soroush Khanlou
Right.

Chris Dzombak
More generally, I will give you the point that reactive programming typically borrows quite a lot of terminology from the functional programming world. You will have terms like map, flat, map, zip, flatten filter. And some of those are more intuitive than others. Filter, for example, you can probably more or less think about what a function called filter does. Others like flatmap are not exactly intuitive.

Soroush Khanlou
Yeah, well, some of them we get from if you've worked a lot with arrays and dealing with lists, you are eventually going to find that mapping and filtering is just way more convenient than anything else. And so some of those come across neatly.

Chris Dzombak
Well, someone has to tell you what Map and Filter mean initially, right?

Soroush Khanlou
But once you get that and once you're like, oh, this is just way easier for me to write than anything else, once you have that Map and Filter I think come across pretty cleanly. So while Map and Filter kind of do come across pretty cleanly when you think about like, oh, here's what I do on a raise, I guess I can kind of see how I'm internally changing the value of what I'm looking at and that's what Map does. Or I'm removing some of these elements and that's what Filter does. Like something like flat Map, it just does something totally different in a way that's kind of hard to think about. And it's kind of the same. And I know why they're all named the same thing. I know why it's all called Flat Map, but it doesn't come across as cleanly as Map and Filter.

Chris Dzombak
Yeah, for sure. Before we move on from terminology, I do want to give a shout out to the site RX. Marbles, which will be in the show notes. We're going to have a lot of show notes for this episode.

Soroush Khanlou
Yeah, it's going to be a big one.

Chris Dzombak
And this site will give you a really nice overview of all these sort of map, flat map and other operations that you might do with signals that you may be curious, what does this operation mean? Or is there an operation that does X? This site has, if I'm remembering right, has interactive diagrams that you can play with that will give you an overview of what any of these operators do. And that is really useful.

Soroush Khanlou
It is very cool. And there's some that don't even make sense on an array like throttle, where we'll only send one every half a second, right? Like it will only let through one every half a second. There's no concept of time with an array. So you can't even it doesn't even make any sense.

Chris Dzombak
I was thinking about this earlier, thinking about applying these things to a signal which again are values over time rather than values over basically space. Right, right. So it's like we're sort of taking all the array functions and shifting them or rotating them into this other dimension. I'm wondering if there so there are things like throttle that don't make sense in space that make sense in time. I'm wondering if there are things that are the other way around.

Soroush Khanlou
Right. Things that you could do on an array that you couldn't do on an observable. Well, before we get to that, we're grazing up against this thing that I love so, so much. I only discovered it about a little less than a month ago and it really made a lot of this stuff click for me. And it is called a general theory of Reactivity and it is a GitHub repo with a bunch of docs in it and it's basically mostly about JavaScript, but the concepts are very, very like language independent. And the person that made this has a two by two grid and this thing to me is just so awesome. And across the top the options are singular versus plural and across the side the options are spatial versus temporal. So something that is singular and spatial is just a regular value. Something that is plural but still spatial. As you were saying, it's mapping through space is an iterable. Or you could think of that as just an array, something that is singular as in you, you can only have one of them, but it does represent a value through time is a promise. And then something that is both temporal and plural is what he calls an observable. I think it's a he, but could also be called a signal, could also be called a subscribeable, all that fun stuff. And this to me really clicks together a couple of things. One, it clicks together that observable is really where iterable and promise meet. And so it's both of them kind of at the same time that is to me like a very for me that's like the burrito that's like the thing that makes this thing click for me.

Chris Dzombak
That's awesome.

Soroush Khanlou
Yeah, he has a bunch of other stuff like he'll say like, well, the setter for an array I'm going to call an iterator or I'm going to call a generator. And the setter on the getter I'm going to call an iterator. I think I said that kind of funny. And he has setters and getters and the names for the values for each of these four like combinations of this square. It's a great read. It's pretty long. I think it was a talk at a couple of different conferences. So perhaps there's a video online but we're going to put this link in the show notes. It was very useful for me for crystallizing exactly what this thing is. And I think it helped me kind of understand. One of the things that makes this so tough is because when you I don't know, Chris, I really want to ask you this.

Chris Dzombak
Sure.

Soroush Khanlou
Which is, do you think that there has been a tougher uptick for reactive programming in the community than other technologies?

Chris Dzombak
Boy, that's really not uptick.

Soroush Khanlou
Uptake, I think is what I meant to say.

Chris Dzombak
Yeah. Let's see. First, I will note that I really enjoyed reading this general theory of reactivity and found it really useful and I'm really glad that it helped crystallize some of this stuff for you.

Soroush Khanlou
Yeah, for sure.

Chris Dzombak
If any of our listeners are maybe struggling with some of these concepts, maybe get promises, but are maybe not so clear on signals, that would be a really helpful read. Now, has reactive programming seen a I'm going to rephrase as more difficult or more resistant uptake in the community than other things?

Soroush Khanlou
Yeah, exactly.

Chris Dzombak
I'm not sure, honestly, because we have to have things to compare it to. Right. And you could compare it to something like objective C properties, or you could compare it to functional programming ideas and non core data persistence layers. Right, right.

Soroush Khanlou
I would also maybe add like something like AF networking, like bringing in some kind of rich abstraction for your networking. I would also maybe compare it to something like Swift in general.

Chris Dzombak
Let's see. So Swift is a little bit unique in that Apple is pushing it, right?

Soroush Khanlou
That's true. But it's also such a big paradigm shift of like your language is your biggest dependency when you're writing code.

Chris Dzombak
That's absolutely true. I think that if someone had found some way to come out with a Swift like language that you could ship on iOS and OS Ten, it would have seen a much less rapid uptake. Although that might just be because if you're writing on iOS or OS Ten, you should just use whatever language is blessed.

Soroush Khanlou
Right, exactly.

Chris Dzombak
It might not be because of the things like the optional types.

Soroush Khanlou
Right, yeah. It's tough to say swift.

Chris Dzombak
It's hard to say with Swift because it has Apple behind it. With something like AF networking, I think sort of the key distinction is that something like AF networking solves a problem that is very real and very concrete and that you can tell is hurting you. Right. If you're writing back in the day, like Nsurl connection code, that clearly sucked. And so AF networking was clearly an improvement, where reactive programming is a little bit of a harder sell. Because it's not necessarily so clear that things that omit, that some system constructed of ad hoc notifications and delegates and blocks and interfaces that don't quite describe or types that don't quite describe exactly how that object behaves, it's not quite so clear that those things are painful. It's more like death by 1000 cuts than like death by four URL connection delegates. Thank you. Thank you for laughing at that. It certainly has seen a slower uptake than something like AF networking, I think, because it's a little bit harder to sell and it doesn't. Well, I do think it solves a very real problem and helps model some relative, some fairly complex asynchronous code and dependencies, and helps unify these common patterns for asynchrony and event handling. It's not as viscerally clear to most iOS developers that that's actually a problem that needs to be solved.

Soroush Khanlou
Right, right. Another potential thing that we could compare it to is like redux or whatever. The one is where you have like a central data store of all the stuff in your app and all the data and state in your app and then you can have actions that modify it and then those get subscribed to by views that update themselves or whatever. I think that's called Redux, like maybe something like that, which hasn't seen that much uptake either. But it is a pretty big paradigmatic shift and it's maybe tough to have that stuff be pushed through without some kind of vendor providing it.

Chris Dzombak
And it's important to note that you mean Redux hasn't seen much adoption in the iOS world. Right?

Soroush Khanlou
Exactly.

Chris Dzombak
Quite popular in the JavaScript world.

Soroush Khanlou
Well, but everything's popular in the JavaScript world for about two and a half months. I'm sorry to any JavaScript developers who are listening.

Chris Dzombak
Yeah, you're absolutely right. There are some interesting ideas in Redux. I think reactive programming gives us some tools that might make building a Redux like architecture much, much easier. But I haven't actually tried that on iOS, so we'll see.

Soroush Khanlou
Yeah, I haven't tried the Redux thing either, and it's hard to say if it's a good analogy, but I guess the broad point of my question was like I don't think it's seen uptake commensurate with how much fervor there is from the people that like it. The people that like it. Really like it.

Chris Dzombak
Yeah.

Soroush Khanlou
And I and so I think one of the roots of this thing is these two axes of complexity, which is what I would call like basically your thing changes in time and it changes in space. And while that's fine for arrays are pretty straightforward and you can look at them, you can get them promises I think are pretty straightforward and you can look at them, you can get them. And when I say you, I really think I mean me here. I'm not trying to offload this off any onto anybody, but when I look at signal and I see a flat map over a signal, that means that each event coming out of the signal gets turned into its own signal. And then somehow is being combined and all of these signals together are being combined into one big signal. And I think isn't there like there's like merge latest, combined latest? And there's two other strategies for merging these things because of this complexity. And so some of it is, I think how do you say, the two types of complexity, incidental versus incidental.

Chris Dzombak
Innocent.

Soroush Khanlou
Yeah, so some of it is incidental. I think. Some of the ways that these things are named and some of the ways that the APIs look, especially in the Objective C days, used the word ad hoc a little bit earlier, and it definitely wasn't ad hoc system back in those days. I think it makes a lot more sense now in the Swift world, but some of it is really essential complexity because when you merge these signals, like, do you only want the last one from each one? Do you only want what if one of them sends an ending signal? Like, how are you going to handle that?

Chris Dzombak
So I totally, totally get what you're saying. This is not your core point. But I'll push back that things make a little more sense in Swift because we're still writing Swift with the same patterns for Asynchronous programming as we were in Objective C. Like, that hasn't changed. But I really wanted to bring up the incidental versus essential. Essential.

Soroush Khanlou
That's right. It's both kinds of complexity at once.

Chris Dzombak
Yes, incidental versus essential complexity. Because this complexity of the sort you're thinking about here, you're talking about, is a really common argument against using reactive programming techniques. Right. But let's think about what we're trying to do with these techniques, right? If we're trying to replace some system that's already in our app with a system that's written with reactive programming, it's not like we're aiming to change behavior or add more complex behavior. We're trying to model the system that's already there. And if we're trying to replace a system with something written with, say, reactive Cocoa or RX Swift, and our reactive code is somewhat complex, and we find that we're having to think very hard about how these two signals get merged. Let's say this is not incidental complexity that's due to bringing reactive programming into the mix. This is complexity which was already in whatever code you were trying to replace. It's just that you may not have been thinking about it. Right. So if you have a case where you have to decide on how you're filtering a signal, that's probably something that you would be writing and like, deciding whether or not to return early from some delegate method that is given new values. Right? If you're thinking really hard about how to merge two signals, what you're actually trying to do there is not something that is incidental because of the reactive approach. It's essential to whatever problem you are trying to solve. It's just that if you weren't using reactive programming, that complexity would almost be buried. Like, you wouldn't think about it. Things would just sort of would happen, however they happened to occur in the system that you construct. And hopefully you used NS operation queues with dependencies or dispatch groups to manage to manage merging these two asynchronous results correctly. Hopefully those are fairly complicated APIs too. Hopefully it's thread safe.

Soroush Khanlou
Right. I don't actually agree with you on these specific examples that you're bringing up. But I do think that there are.

Chris Dzombak
Examples that these are the examples you brought up. My usual pushback here is that if you're trying to model something with reactive programming and it seems complex, that more often than not is because you're trying to model something that is complex and you are just actually thinking about it instead of almost accidentally constructing a system that has that complexity in it.

Soroush Khanlou
So for some things I'm actually down, especially the examples you brought up. And if you're really talking about explicitly merging these two things, you have to have that option of like, should I combine latest, what should I do with completed signals or whatever. But the fact that you even, let's say, have completed signals is a result of you're making this signal type so generic that it has generic enough to fit every single possible case. And so you need this completed signal, let's say this completed event. Another example of this is like RX Swift's dispose bags. So if you're subscribing to something, make sure you do it with a weak self capture group to make sure that block that subscriber doesn't stay around for much longer than it's supposed to. And keep yourself around. And then when you're supposed to deallocate, make sure you deallocate any signals that you are trying to hold onto to prevent those retain cycles. So that's another bit of complexity. So dispose bags, I'm not actually sure I know how Rxwift does the dispose bags. I'm sure, like, reactive Coco has to have some kind of facility for that as well, because it's just necessary. Whereas if you had a simpler API, in certain cases, that stuff would just go away. Like, I've never had to implement a dispose bag for code that's not signal based. You just like, what is a dispose bag? You know what I mean? And that's not to say that that invalidates the value of this stuff because promises can't be canceled. For example, if you wanted to add the ability to cancel a promise, you would have to add that to every single promise. And you'd have to every new promise you make, you have to now check whether it's been canceled and have a bunch more machinery around that stuff. So if you need that in every single place, or if you need that in one place, you end up having to add it in every single place. And so in JavaScript and in most of the promise libraries that we have on objective C, with the exception of Swift Task, you just can't cancel. You just can't do anymore. And like we mostly say, it's fine, we don't need it that badly. But if you want to add those capabilities, you have to add that complexity.

Chris Dzombak
Yeah, so this is true. I do think that okay. I haven't looked at recent Reactive Cocoa quite enough to compare and contrast Reactive Cocoa and Arc Swift in terms of disposables offhand.

Soroush Khanlou
Yeah, I don't know how they do it.

Chris Dzombak
I do think that historically, I've liked how reactive Cocoa does it. I think there's a little bit more magic there, so there's a little bit less that you have to worry about. But I'll give you that that is a little bit more complicated. Although I will still say that my intuition is that these are things that you would be managing almost accidentally in writing conventional Cocoa code. It's just that you are thinking about them more when writing.

Soroush Khanlou
I don't disagree with that.

Chris Dzombak
I think that's basically right, which is maybe unfortunate, right? If you can accidentally write something that is correct, that's maybe better than having to think about writing something every time.

Soroush Khanlou
Or that it's so trivial to write it as correct that you can just look at it and say like, yeah, obviously this is doing the right thing. So one example, one of the things that really bums me out is like, you know, when you're writing, you're trying to write an array processing thing, I guess you call it list comprehension in terms of like a map and a filter, except you need something in the map from the filter or like vice versa. And then you try to flat map over it and then you end up passing around a tuple, like an array of tuples as your intermediate thing and then you're just like, oh my God, this just got way worse. And if I just use a for loop, like it would have been fine and every time that happens it makes me frustrated because I want to use those tools of the maps and the filters and the stuff. But you're just like, you know what? I'm just going to do it this other way because it's just like I need too much stuff from too many places and perhaps I can't change the types that they came from or whatever, and I just have to suck it up and do it with a flat map that returns nil instead of a map and a filter, let's say. And I feel like there are some of the cases that we're talking about with signals can be like that, where it's like, oh, well, I could shoehorn this to fit into the signal model, but I'm just making my life more difficult.

Chris Dzombak
I mean, so this is more just sort of processing things in a functional way, right. I don't know exactly what to say here. That's definitely something that requires more thought and certainly isn't as straightforward as doing things sometimes in a very imperative way.

Soroush Khanlou
Yeah, for sure.

Chris Dzombak
Yeah. I don't know if I really have anything to add there except to say that's not necessarily a knock on reactive programming so much as functional operations on data.

Soroush Khanlou
Right, yeah, I think that's more or less right. It's just that it works at some points and it doesn't in others, maybe. So let me turn that around and say there's a framework called Swift Bond. And swift bond has now become reactive Kit, which I really can't distinguish between that and RX swift and reactive cocoa. But Bond was, I thought, unique in that it was just so like its API was so simple and so dead useful that you look at the code and you're like, obviously I want this. What hoops am I going to have to jump through to get this? For example, we'll put this in the show notes, but on their README, they have this little line of code. And I read it and I was just like, this is like, I just have to have this. And their prefix is BND. So for their categories, everything's BND. So it says, like, text field, bndtext bind. And then the argument is to label BND text. And again, talking about code on a podcast is tough, but basically just like one line of code, zero blocks. I don't know what a dispose bag is. All I did was write this line of code, and now every time I change my text field, my label gets updated and I don't care how it happened. That is so cool. And then, yeah, you had the map. That makes sense. You had the filter. That makes sense. You do need the blocks. Eventually you want to do a custom thing, but when it gets I don't know, it from there can get really complicated. And that, I think, is the frustrating part. But if you can hide that complexity and basically, I guess what I'm trying to say is it's kind of a shame that this library, which to me seemed so elegant turned into another Reactive Cocoa clone. We don't need another one of those. But I do think we could use another thing that lets you write like, one line of code that just you don't have to think about it and this will just work. I don't know. That's the power of the stuff.

Chris Dzombak
The thing there is that any of those and I mean, you see this time and time again, any of those very simple. I just want to bind this to this is useful in is typically useful in a relatively limited set of use cases, and then it starts necessarily expanding to have more capabilities and eventually grows into, say, reactive Kits. Reactive Kit. Right. And I'll note that Bond does have some notion of disposables or dispose bet like, it's just it does.

Soroush Khanlou
Yeah. I don't know. So I haven't used this, which is why I can't speak to it with the level of depth that I would really like to. But if I could have the good stuff and not have to have the bad stuff, that seems tight.

Chris Dzombak
I'll just say that I don't think there's that much bad stuff. Like you have to hold on to. If you have an ownership interest in something, you have to hold on to something to retain it.

Soroush Khanlou
That's pretty trivial. Yeah, pretty straightforward. So, yeah, I don't know. The swift bond. I saw that stuff in the README and I was like, this is great. This is what I want. And so I guess I did kind of attach that. But I know there's other ones, and I know you have more experience with them than I do. I know there's RX Swish, which I feel like gained a little bit of popularity recently. And there's Reactive Cocoa, which still has like, a pretty loyal following. What is your preference?

Chris Dzombak
Yeah, I was just going to say can I give a little bit of context here?

Soroush Khanlou
Yeah, for sure.

Chris Dzombak
Reactive Coco was, as far as I know, the first library to bring this reactive programming paradigm to iOS and Mac platforms. It dates back to, oh, I forget exactly when, but way back in the objective C days preswift, and it notably deviates from the RX sort of quote unquote specification that I believe Microsoft and company put forward for reactive programming. And it deviates in a couple of key areas.

Soroush Khanlou
Is this like a hot and cold signal?

Chris Dzombak
This is a hot and cold signal thing. Or more recently, the signal versus signal producer thing.

Soroush Khanlou
Right.

Chris Dzombak
In a way that I think makes sense, but it's because of a basically differing design philosophy. RX Swift came onto the scene after the Swift programming language came out. Given that name, that seems obvious, right? Yeah, that checks out and follows the RX specification closely. And so those are sort of the two big players and that's the key difference between them. Really.

Soroush Khanlou
Got you. And the RX marbles are the same. They use the same terminology and the same everything as RX Swift.

Chris Dzombak
That is correct. Although in terms of those operations, you'll find that Reactive Coco doesn't really deviate from naming those operations generally.

Soroush Khanlou
Got you.

Chris Dzombak
Okay.

Soroush Khanlou
I remember a specific case where, like, Throttle was named one thing or one library called it Throttle and one library called it Debounce.

Chris Dzombak
Okay.

Soroush Khanlou
And we were in Slack trying to figure out which one is which, and turns out they're exactly the same, but they just have different names.

Chris Dzombak
Because programming differing. Yeah, because programming I started working with Reactive Cocoa back in the Reactive Coco two days and don't really have any experience firsthand with RX Swift. So my heart is with reactive cocoa.

Soroush Khanlou
Nice.

Chris Dzombak
Likewise. I don't really have any experience with reactive kit or interstellar.

Soroush Khanlou
Interstellar seems cool to me. I don't know if you've ever played with it.

Chris Dzombak
I haven't played with it. We did look at it at work, actually, a little while ago because it seemed simple and straightforward, which we liked in an implementation, as I recall. I was not impressed with the test coverage at the time. I'm not sure if that's changed.

Soroush Khanlou
That makes sense. That seems like a thing that would be sort of not easy enough to change, but seems like a thing that they could change and that could be like that's not a fundamental screw up. When I was writing my Promise implementation once. I had written it once and then found a bunch of bugs in and kind of scrap some code, rewrote it, I was like, well, let me take a look at some of this other stuff and see if I can make heads or tails of this other stuff now that I have. Like, I feel like when you write a piece of code, you know it more intimately than even if you've read it 100 times.

Chris Dzombak
Oh, yeah.

Soroush Khanlou
And so I went into just the source of their signal class and it looked so familiar because it looked so familiar and I was just shocked and I was running through and I was like, this is just exactly what I just wrote, except with the ability to change it more than once and inform all the subscribers. But one of the key differences, though is like so you look at the top of the class and it has the same three instance variables. Basically you have your value, which is a results generic over t an array of callbacks which are just callbacks and then they have a mutex. I used a queue, like a serial queue, but that's basically the same thing. So the shape of it is exactly the same, like the structure. But the difference that you notice is they can't clear their callbacks array once they've fired the callbacks, whereas a Promise implementation can. And so you don't actually have to worry about, well, did I subscribe weak? Did I need to dispose this with promises? You know, that all those callbacks will just be thrown away as soon as they're fired and they're done. But with this, now you've got this other layer of like, oh, well, you're going to have to maintain and make sure that you unsubscribe from this when the time comes or that you're weak or whatever. But I don't know, reading the implementation of this thing, it was really cool. It was really cool because it was like clear how these two things are.

Chris Dzombak
Just like enough siblings, if you, the listener, are very curious about this, maybe after reading General Theory of Reactivity or not, I mean, that's a lot of reading. You certainly take a tour through this, through Interstellar Signal implementation.

Soroush Khanlou
Interstellar the code is really nice. It's very like the spacing is nice, everything is nice, so you can just kind of look at it. It's important to have good spacing. That's all I'm going to say. And I attempted to write my own promise library with the intention of like, if you look at it, you can kind of see what's happening and what it's doing. I don't know if that is true because I wrote it, so I know it very intimately. But if a reader or if a listener takes a look and says like, oh yeah, I can actually kind of see what's happening here and why this thing looks like that. If you can get it from the promise thing, I think you can get it from Interstellar Signal class as well. It's really cool when you look at it. You're like, oh, wow, that makes sense. And that's really cool.

Chris Dzombak
Oh, yeah. Absolutely. Boy. So a few things that I wanted to note before we wrap up. Didn't find a good place to put these anywhere else in the episode. Nice. Swift and particularly support for generics makes this stuff so much nicer than it was in Objective C. If your only experience here was playing with reactive cocoa and Objective C, and you thought, like, this is kind of nice, but this is kind of verbose, and that is a whole lot of closing square brackets and everything is just ID, I have to know what's what. Try to get in Swift generic.

Soroush Khanlou
No more underscore underscore block. No more underscore underscore week. No more weird carrots everywhere.

Chris Dzombak
No more I forgot about the weird carrots.

Soroush Khanlou
Don't forget about weird carrots. They were bad. They were bad. But yeah, a lot of that stuff. One of the original criticisms I wrote in my big post about how much I hated Chris was that Objective C is designed for objects. And putting this stuff in there, you really are stretching in the name, doing weird. It is in the name. It's true. And it's good at objects, defining them. It is a little wordy to define them, but it's good at objects. It was less good at block based stuff at the time, and Swift is way better at it. And that part of the pain has definitely been ameliorated.

Chris Dzombak
You remember NS Block? Blocks are just objects.

Soroush Khanlou
What is NS block?

Chris Dzombak
There's a secret class underneath every block.

Soroush Khanlou
In Objective C. Nice block underscore copy.

Chris Dzombak
Yeah.

Soroush Khanlou
So you said you had a couple of things you wanted to throw in. One was that objective it's gotten better.

Chris Dzombak
Yes. The other is that if you're looking around, for example, code, there are a lot of examples of reactive code that is maybe not very well written or not clearly commented or just not very clear. And so if you find an example that seems like it should be good but just isn't making sense, feel free to move on and try to find another example that's totally fair. And that's true of just a lot of code that is on the Internet.

Soroush Khanlou
Right.

Chris Dzombak
But it's especially true in this world for some reason. And the last thing that I wanted to say is just be open to this. Right. I hope that one of the metaphors that we've touched on in this podcast was helpful for you, or some of the resources that we're putting in the show notes might be helpful and that next time you're trying to model some sort of intertwined asynchronous operation. Even if you don't use reactive coker or RX swift, I hope that you kind of take a step back and think not just about the delegates or blocks that you might have. To put in place to make something happen. But think about how data and events are flowing through your application or flowing through the problem that you're trying to solve.

Soroush Khanlou
I have a friend who they added an observable type into their project. It's not part of our exposure. It's not part of anything. It's just an observable type. You can subscribe to it. That's it. You can map over it. That's all you can do. And the whole thing is 100 lines of code. And it's super useful for him, and he loves it. So if that's the extent of this stuff, then great, right?

Chris Dzombak
If that works for you, then cool. You have a new tool in your toolbox that solves the problem. That's great. There you go. That's pretty much all I wanted to throw in.

Soroush Khanlou
So we're now entering our three of our podcast on reactive programming. We knew this would be a long one. This one. Not only is it a spicy topic, it's also the history. And everything with us is just so funny.

Chris Dzombak
We've got to be only entering minute 40, right? Maybe 40.

Soroush Khanlou
I think so. I think we're up there. We'll figure out if this is going to be two episodes or one episode, but it was pleasure, Chris. I think we touched on basically everything we wanted to talk about. Maybe we'll do a follow up episode. Who knows?

Chris Dzombak
Maybe. Who knows?

Soroush Khanlou
Yeah. This is good, though.

Chris Dzombak
This has been a lot of fun.

Soroush Khanlou
Yeah, for sure.

Chris Dzombak
I'll be in New York later this week, so I'll see you in person.

Soroush Khanlou
That sounds great. I'm looking forward to it. All right, well, thank you for listening. We hope that this has been fun, and we will talk to you in two weeks.

