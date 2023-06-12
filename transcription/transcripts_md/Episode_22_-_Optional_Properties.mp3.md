Speaker A
Hello, Patreon. Supporters. This is fatal error. I'm Krista Zomback.

Speaker B
And I'm Sirish Conlon.

Speaker A
Before we started this episode, we wanted to give all of you a shout out. Thank you very much for your support here on Patreon. It really does mean a lot to us and it's making it possible for us to continue producing this podcast and we really appreciate that.

Speaker B
Yeah, we are basically we're almost at the point where we are breakeven in terms of editing costs, in terms of hosting costs. And the fact that this podcast is actually now sort of break even for us is really nice. And hopefully we have only cool places.

Speaker A
To go from here, hopefully. So this week we are going to talk about something that Sarosh posted about on his blog a week or two ago, and that is a blog post with the title, that One Optional Property. And so in this post, Sarosh, you're talking about how in a lot of cases, like in many code bases, you'll see that there's a view controller that has one task, and then there's this one optional property that's been tacked on that is maybe some sort of optional data that the view controller displays in some certain special case. Or it's something that otherwise changes the behavior of that view controller.

Speaker B
Right, yeah, exactly. And often I find, like, when you make the view controller the first time, it's kind of tightly focused and when you go to change it and add some small piece of behavior, that's when you add that one optional property and you're like, this doesn't feel right, but I can't think of how else to do this.

Speaker A
Well, let's maybe think about some of the reasons that you might add this optional property and then we can try to explore why it's problematic to add that property.

Speaker B
Yeah, the two that I kind of laid out in the post are one is something that is needed in some cases, but not in others. And so if you have this view controller that's used in multiple different contexts or multiple different ways, sometimes you have a slightly different little bit of layout to do, a little bit of data that you need, something that's basically depending on if that optional property is there or not. That defines what mode the view controller is or what presentation context it's in. The example I gave for that is we had a view controller in an app I was working on where there was an optional notification message and it was a string and it was basically like if you came from a push notification, we needed some data from that to be displayed in some particular way. And we had this view controller, it had everything we needed and it was ready to go. It's just that it didn't have this ability to display this notification message. And what was kind of hidden in the fact that we were adding just an optional property was the fact that that optional property defines a totally different presentation context. It's a totally different way this thing is used. That's sort of the laying out of the problem. The optional property defines how layout is going to happen because it determines whether a certain view is going to be on screen or not. And it determines things that an optional string shouldn't be the thing that tells you whether you're going to display a view or not. They're only sort of tangentially related and there's some implicit coupling between those two pieces of data. The fact that a string is there or not shouldn't have any impact on your view layer.

Speaker A
Right. That makes total sense. Right. You're sort of adding a different mode or different use case or like kind of sort of a different responsibility. Well, I don't know if that's really the right way to phrase it, but you're adding some different use case to this view controller in a very, like a very ad hoc way. And this happens a lot, probably even if we're not talking about view controllers, but we can keep focusing on view controllers for right now.

Speaker B
Yeah, the reason I talked about it in terms of view controllers is I see it the worst there because I feel like if you're working with an object and you want to slightly tweak it in a certain way, there's a plain old object, it's a lot easier to say, oh, just make a new one. Maybe this object is 30 lines of code and I'm happy to just make a new one or inject some strategy or whatever. But I think there's something about view controllers that you're just like, oh, this is just the dumping ground for all the stuff. And if you kind of indiscriminately apply that, you end up with bad view controllers. And I do think it is really a unique problem to view controllers. So kind of giving people strategies to stop them from thinking about their view controllers as a dumping ground and start them from thinking about like, this is a tightly focused object that has a really strong sense of identity.

Speaker A
And so this is one of several techniques you can use to combat or to look for if you're trying to combat the massive view controller syndrome.

Speaker B
Right, yeah. And it might not be fewer lines necessarily, but it's just that it's kind of unfocused when it's just like this random optional that's hanging out here.

Speaker A
Sure. And over time, as you end up adding a couple of other random optionals to that same view controller, you end up adding kind of a huge number of different possible states to that view controller. Right. And maybe some combinations of values in those optionals are invalid and you expect them never to occur, but you kind of end up almost building out a matrix of possible states that this view controller can be in and that is going to explode really quickly into a pretty complex View controller, right?

Speaker B
Yeah, for sure. I like the term state space for this. It helps me think about what are all forms that this can be in and each of those forms represent kind of a point in this state space. Yeah, we had a situation there was basically a more complex form of this exact thing that I'm talking about, where we had a View controller whose responsibility it was like a form to collect an address. And if you were editing, it had an optional address property, and if you were adding, it had the preselected type of the address, a home or work or other, and they were both optional because if you were editing, you wouldn't need that preselected thing and if you were adding, you wouldn't have the address already created. So we ended up with these two optional properties on this thing that looked like they were independent. But what was really going on was those two things should have been more tightly bound together because if you had one, you wanted to make sure that you wouldn't be able to have the other. And the way it was set up was you could have both of them be nil, which would have been invalid, or both of them not be nil, which would also have been invalid.

Speaker A
And we talked about this a little bit when we covered, I think in the last episode, we talked about the result enum and how that takes kind of the same problem, this state space of an asynchronous callback with two optional parameters and reduces it down to a combination of like valid states.

Speaker B
Right, right, exactly. This is exactly what's going on. And you won't be surprised to find out that the solution is exactly the same as the solution for the result enum, which is you use an enum and you become very explicit about like this is this mode, this is this other mode, and this is maybe this third mode. And so you could say like, oh, if I don't need that in this case, the notification message string, I'll just have like a normal mode. And then if I do need it, I'll have a from notification mode and then that mode will have an associated value on that case, which will be like the string called the message or whatever. And now all of a sudden, you've really richly defined what you're talking about when you are working with this object.

Speaker A
So the first thing to do here, if you're thinking about adding an optional property or you're looking at a view controller that already has some optional properties, is to think about what sort of states or modes each of those optional properties represents and what combinations of them are valid and invalid to start to try to drill down. Okay, what does this view controller do? What different states can it be in? And then take those states and put them into an enum right?

Speaker B
Yeah, pretty much.

Speaker A
Okay, cool. And then later in the View controller, when you're configuring your Views layout or when you're putting some string on the screen, you can switch on this enum anywhere that that state needs to be taken into account and make sure that you handle all of the states that the View controller can be in. And you don't have to write code that handles possible invalid states because you can't represent invalid states.

Speaker B
Yeah, they won't even compile.

Speaker A
That's a really cool idea. I haven't noticed this too badly in the code base I'm working on right now, but I will certainly start to keep an eye out for this and see where I could apply this pattern.

Speaker B
Yeah, I think you start to see it when you start changing things. Like when you write things the first time, you have a pretty clear sense of where you're going and you do the thing and it's fine. But then you're like, okay, well, we need this exact View controller. But it's slightly different in this case. And then that's like that, but slightly is like your worst enemy because it's like I can mostly reuse this object. Do I subclass it? Do I, like, reimplement it? Like none of those options seem right. I'll just add this optional property and move on.

Speaker A
And that optional property doesn't really do too well to document what's going on. Right. And so that quote unquote slightly that you mentioned gets completely lost down the road. Whereas if you take it out into an enum and kind of make this concept of the different mode that the View controller is handling, a more realized concept, then that acts as documentation, makes the code more future proof for whoever's coming along to document it in the future.

Speaker B
That's it exactly. There is a Sandy Metz talk that I link in the blog post. We'll have to put a link to it in the show notes as well. And it's called nothing is something. And in it she says there is never just one specialization. Right. It's not like I have thing and I have weird specialization. You really, at that point, already have two things. And so if you try to think about it in terms of I have a thing and a weird mode for the thing, you're already kind of in a weird space because then what about when you add another mode? Is that another weird thing off of it? Like treating those two modes as kind of equal partners? Because not that it makes your code clear, it's that it separating the two states and making them equal.

Speaker A
I think it does make it more clear. Again, like I was trying to say the word might be reifies the concept. Right. Gives them underlying structure, some concrete definition.

Speaker B
To give you semantics.

Speaker A
Right? Exactly. Yeah.

Speaker B
Gives you words to use instead of just nil and not nil. You know why it's nil.

Speaker A
Right. And you know that this thing can't be nil. You don't have to know that this thing can't be nil if this other thing is nil. Right. It provides you with some structure and with some rules to help make your code more what's the opposite of fragile?

Speaker B
Robust. Robust is a good word to make.

Speaker A
Your code more robust. Yeah, I'm very good at English, so this is kind of reminding me of a somewhat related topic, which would be state machines, right?

Speaker B
Yeah, for sure.

Speaker A
So this is something that, if you've spent any time in computer science education especially, can seem like big and complicated and scary. But it's really not. I mean, right? Am I wrong there?

Speaker B
No, you're not. It's annoying because it has this really aggressive name, especially if you use the really formal name for it that you'll find on Wikipedia and stuff. It's like a finite discrete state automaton or whatever. And it's like finite state automaton? Yeah. What is that? Who even knows what that means? It's just, I think, technical academic jargon that people use to make themselves sound smarter. But it doesn't have to be that complicated.

Speaker A
No. The key concepts here are you have some system and that system might be a view controller. It could be like your authentication controller in your application, but basically you figure out, what states can this be in? Am I not displaying a notification or am I displaying a notification? Am I waiting for the user to enter username and password? Have I sent that to the server as a server told me that this is invalid password. Drill down what states your system can be in and keep track specifically of which state it's in. And obviously, like, an enum and a variable can work pretty nicely for that. Right? And that's sort of what we've suggested so far. And the last thing that you need to have are rules or conditions around when you can go from one state to another state. So, for example, you probably can't go right from waiting for the user to enter username and password to invalid password without going through the check in with the server state first. So you have some rules around which states can go to which other states, and what happens when one of those transitions from one state to another happens. And that's your state machine. So what you've proposed in this View controller looks a lot to me like a very simple half of a state machine here.

Speaker B
Yeah, I think that's exactly right. The other half that if you added it to this, you would get a state machine, is basically the concept of change or the concept of a transition. Like the way that this particular example is set up. The enum is a let property. Once you make it, it doesn't change. And that's like the mode that the thing is in, and that's not going to change once you introduce that concept of change. Such as, for example, in your authentication example, where you have to go from the user is typing in their username password to the user, or the system is checking with the server to see if the password is valid to sort of the next thing to the next thing. Once you add that concept of transitioning and moving through that system, then that's when you have like a fully blown state machine.

Speaker A
Yeah, absolutely. And as you said, this V controller doesn't go from one state to another. But I don't know, as long as we're talking about this, it seems like a useful thing to mention.

Speaker B
No, it absolutely is. State machines are I think so. They're so useful and they're criminally underused because you can say these transitions are valid and these transitions are not valid. And once you kind of have used it in one place, you look around your code and you're like, wait, actually this code is also a state machine. And this code is also a state machine.

Speaker A
This is an important sorry to interrupt you. This is an important observation. I think a lot of the code that you've written in whatever app you're working on now probably is a state machine. You just haven't thought of it that way.

Speaker B
Right, yeah. There's a Cocoa Pod that illustrates this really nicely. It's called Stateful View Controller and we'll make sure to put it into the show notes. And the way that it works is basically it gives you a state machine which is like, I am either loading or I have content or I have loaded successfully, but I have no content, I e, I'm empty or I loaded with an error. And they define all the valid and invalid transitions. Like you can't go from content directly to error. So they define those transitions for you and then you just provide views for those particular states and those views get the data that they need. Like if you have content, then you're going to have some array of content, but if you have an error, you're not going to have that, but you will have an error to display. And so by giving it these views, it automatically knows how to display things and when things happen, and you just tell it when change occurs and you say, hey, I just loaded. And it will change itself to the loading state display, the loading view. And that's a really concrete example of a state machine that's in really every single app.

Speaker A
You just don't know it yet.

Speaker B
You just don't know it yet. Exactly. And I think the concepts in this while I might not pull in this pod specifically, I think the concepts in this Cocoa Pod are like super applicable to tons and tons of apps.

Speaker A
Oh, yeah. I mean, just the flowchart of the decision tree that is in the README for this repository is really interesting to look at.

Speaker B
Yeah.

Speaker A
And that's something that I wanted to mention is that you don't necessarily have to pull in a library or a cocoa pod to implement some sort of state machine just to keep track of something in your app. Right. Like I said before, all you need is to think about what states there are, put them all in an enum maybe with associated values and define a method or methods that try to transition from one state to another. And in that method you can implement some logic that maybe calls out to other methods so that you don't end up with one massive method but that handles changing from one state to another. And in a lot of cases, just the act of thinking about the different states that you can have and making this sort of a more real concept in your app can really eliminate a lot of room for errors.

Speaker B
Yeah. Being thoughtful about the code that you write kevin S.

Speaker A
Way to take my point and turn it into something that sounds super obvious.

Speaker B
I wasn't trying to be a jerk. I was trying to summarize. I was trying to summarize with the listener.

Speaker A
I know. I appreciate it.

Speaker B
So what do you do if you have a state machine and basically you have a state that you're currently in and a state that you want to be in but that transition is invalid? How should the program react to that?

Speaker A
That is definitely a tough question. I mean, really, I think the only generally correct answer is to fatal error out at that point and be sure that you don't ever try to transition from one state to another. There are other tricks that you can play, like the one that I know you're leading up to where state machines with invalid transitions won't actually compile.

Speaker B
Right. I played around with this to see if I could make it make sense. And the unfortunate truth is that it doesn't really work out the way you would want it to. But basically, if you could imagine a state machine where its current state is baked into the generic type. So if you have your states pending loading, loaded and failed, you could have like a state machine that's in the pending state and that would be its generic type. So each of these states would be its own type and then your machine is generic over those types. The problem with that is that you can't store that in a property anymore because you don't know what state it's going to be in. So you can't fully qualify that type. Right. And so if you can't do that, then you can't really have any asynchronicity with it. You can't make a variable and then call some network thing and then change that variable from hey, I'm a pending machine to I am now a loading machine because that variable's type is fixed and so you have to create a new variable every time you want to do that. It isn't quite as easy to use as I really want it to be, but you can kind of use it synchronously, which is nice, but you will have to create like a new variable each time because the type will be different. Because the type is really defined by both the machine generic type and then the specific, the specialization defined by, let's say, the pending type as well. I just said type a lot. I don't know if that made sense.

Speaker A
That's probably going to be a little bit hard to follow if you're just listening along. But there's a gist and there's a link to that gist in the show notes.

Speaker B
Yeah.

Speaker A
And it's interesting to look at and read and sort of consider how this works and how you might be able to improve on it.

Speaker B
Yeah. The benefit is that if you take a machine, a state machine, and you transition it to the loading state and then you try to transition it to the loading state again, it just won't compile, which is really cool, it just says, hey, you can't do that. That's like not really awesome. Yeah. But I think in practice it's not that good and it's also kind of like a dependent type is another way of thinking about it. Like in a dependent type you would be able to say, hey, I'm an array and I have five elements and I'm going to encode the fact that I have five elements into my type. And that encoding will make sure that the compiler can check your work along the way. Of course, the problem with that is if you have that again in a property and you try to load some array from the network, you're not going to know how many items are in that array at compile time and so the compiler can't really check your work. There are languages where it will let you do stuff like that and it will let you check like, oh, this array must always be more than three elements or something like that.

Speaker A
Yeah, although very few of those are languages that we can write production software and certainly on iOS and Android.

Speaker B
Right. There's a really good post that we'll link to in the show notes of how you can kind of get dependent types in Swift. We'll link that in the show notes and it will basically give you the power to say, this is an array with five elements in it. And if I append one to the array, I'm going to return a new array that has six elements in it and you know, at compile time it's going to have six elements, which is pretty wild.

Speaker A
There's another library. There is a library that I would want to mention here that you can use that doesn't give you quite these guarantees at compile time, but that lets you attach a quote unquote validator to a type that the validation runs at runtime and you can fatal error out or something if validation fails. But this allows you to specify an API where you know that any value that you get has passed some sort of validation. It's sort of also a clever use of generics and Swift type system, which is worth checking out too. That library is called validated from Benjamin Banks.

Speaker B
Yeah, it's a cool library. And basically, if you try to instantiate one of these things that has a Validator attached to it, it'll either give you the thing or it'll give you nil. It'll give you the chance to handle the case where the thing is not valid. You could throw, you could just have a bang there and enforce it, wrap and crash. But it makes you handle the case where the thing is not as valid as you want it to be. And with a mention of optionals, we've come full circle back to the beginning.

Speaker A
Well, there was one other thing that I wanted to mention related to state machines.

Speaker B
Cool.

Speaker A
Let's do it. Which is a gist from Andy Matushek. And at this point, this is from I forget when he first posted this, but it's been floating around the Swift world for a little while now. And he, in this gist has given a lot of thought to putting together a state machine that follows a sort of functional core imperative shell paradigm. So it's really interesting to read through how he thinks very carefully and deliberately about modeling a state machine that has sort of a functional core. You can have side effects which you want, especially if you're using state machine in something like a view controller or something to have effects on the network. Right. And it's also designed to be composable. So if you can break some part of your application down into a few different systems, each of which is its own state machine, you can then compose it together into one larger state machine and use that whole state machine together, if that makes sense. I've done a terrible job of explaining this.

Speaker B
No, I think he did a good job. I think he really clearly explains two concepts. Which is one is the composed state machine, which is like, this state machine is a child of this one or this one, and this one versus an orthogonal state machine, which is like, this state machine happens at the same time as this state machine, but does not affect it directly. And he calls that orthogonal. Yeah, and I think he does a really good job of breaking down how those two things interplay and how to make them work in your code base. I think he has like an orthogonal state machine and then like a composed state machine, you can bring two of his state machines together and compose them or make them orthogonal in whichever way you want. Yeah, it's pretty dope.

Speaker A
Yeah. If you have some time, I'd highly recommend reading through that and hopefully you can take that and some of the other things we've talked about in this episode to think a little bit more carefully and think a little bit more critically the next time you are considering adding an optional property to a view controller.

Speaker B
For sure. This was a great discussion session, Chris.

Speaker A
I think so. I hope so. Thank you very much everyone for listening. And again, thank you for supporting us on Patreon. We really do appreciate it. I hope that this episode has been useful or at least as some food for thought.

Speaker B
Yeah, thanks again to the listeners. Really appreciate you all being out there.

Speaker A
And we'll talk to you next week.

Speaker B
Sweet. Later, Chris.

