Soroush Khanlou
Sorry.

Chris Dzombak
Let's do it again. Maybe that say who you are.

Soroush Khanlou
My name Smart. This guy. That's what he paid the big bucks. All right, welcome to episode two of Fatal Error. I am Sirish Conlon.

Chris Dzombak
And I'm Chris De Zomback.

Soroush Khanlou
Alright, today we are going to talk a little bit about View models. So View models are a topic that Chris has a little bit more experience with, so I'll let him kick it off and sort of explain what we're getting ourselves into here.

Chris Dzombak
All right? Sure. So I'm going to start by explaining a little bit about the problem that I think viewmodels solve, and then we can get into what a View model is and how they solve it. But first, let me argue that UI View controllers are in a typical iOS app, are pretty complex, and they have a whole lot of responsibilities you're not.

Soroush Khanlou
Going to hear any disagreement with for me on that.

Chris Dzombak
Let's start with the responsibilities that are assigned to them by UI Kit. Right. That's already quite a lot. And they are literally controlling the view, controlling the View lifecycle, handling putting these views on screen in your application. Right. That's already kind of a lot of responsibility.

Soroush Khanlou
Managing children.

Chris Dzombak
Managing children. Yeah, that's full management itself. A lot of responsibilities. And then in a typical iOS app, you end up with even more responsibilities because where do you learn to put things that your application needs to do? A lot of that goes in the View controller. And so in a fairly typical iOS app, you may find a View controller coordinating interaction between a network API client or some sort of persistence layer. It may be parsing dates, formatting things for display. It might be creating and configuring and presenting other View controllers, which is a problem we talked about in episode one where we discussed Coordinators. And this all leads to what you might call the massive View controller problem, where your View controllers have a whole lot of responsibilities. And because they're sort of tied to the whole UI Kit application lifecycle, they're not really very testable either. It's very hard to test in isolation any of these sort of added behaviors that your application puts in any of its View controllers. Right?

Soroush Khanlou
Right.

Chris Dzombak
So what if, hear me out. What if we took all of these sort of application level responsibilities? Let's take everything that you're assigning to your view controllers and just as a first step toward making those things more testable, toward isolating those out of this sort of like, view controller class that's just part of UI kit. Let's take these responsibilities, this job, and move it up into some object which works to provide data and handle interactions with this view controller.

Soroush Khanlou
So you're saying basically, we take our View controller, which already has the responsibilities of controlling the controlling the view, as it were, managing rotation. The other stuff we talked about, let's leave those responsibilities there. But all the application concerns. You want to move over to this thing called a view model.

Chris Dzombak
Exactly. Or I want to move up to this thing called a view model. Right. Because in this world, I'm thinking of the view controller almost as being just part of the view layer. Okay, so all of your application concerns for a given screen, a given part of your app, can get moved up to a view model. And this view model is just a class. This is some reference type that you might initialize with some dependencies. This is where you might talk with an API client or with a persistence layer that sort of abstracts away your API client and your model parsing and everything you may pass in. What other dependencies might have you controller needs like a motion manager or something, right.

Soroush Khanlou
Step counter.

Chris Dzombak
A step counter, yeah. And so this means that you have an object that handles these sort of coordination between other objects with the goal of powering this view in your app. And that is something that provides a place for you to inject dependencies for testing. And it's something you can test in isolation since you've broken it out of the UI kit world.

Soroush Khanlou
Got you. So, I have two questions so far. So the one question I have is, you keep saying that you will move these responsibilities up into the view controller or up into the view model. Does that mean that the view model holds onto the view controller or does the view controller still hold on to the view? What's the ownership relationship here?

Chris Dzombak
Yeah, that's a really good question. So in my mental model and in what we're doing at work, let me think about this here. You inject a view model into a view controller, but the view controller isn't responsible for creating that view model.

Soroush Khanlou
Got you.

Chris Dzombak
If that makes sense. So, as I mentioned the last episode, we're using the Coordinator pattern to have sort of flow Coordinators in this application. And so that's where a view controller gets created and presented. And then that Coordinator is also responsible for creating a view model appropriate for that view controller because as we talked about, this provides a place for your view controllers to get their dependencies. So actually what we do is we create a view model with all the appropriate dependencies, create a view controller and present it however it needs to be presented. And we inject that view model into that new view controller. So that's where I think in the last episode, I alluded to view models fitting pretty nicely into this sort of Coordinator fueled world. And you can see how that works right now that view controllers aren't creating and presenting each other, we can almost like naturally fit in this other, this other object that sort of models the the behavior of a given view rather than being the UI part of that view.

Soroush Khanlou
That makes sense. So the Coordinator is responsible for creating it. And so in some sense that there's like a parent child relationship there, but then the thing that actually holds onto it and uses it is the view controller. And so there's a parent child relationship there too as well. The second question that I have for you is that you mentioned that this view model is initialized with some kind of persistence layer, some kind of some kind of network ability, talking to network, maybe a motion manager, all these types of things. Does that mean that the view model, in an ideal world, acts as sort of a facade to all of these other interfaces?

Chris Dzombak
It's not so much a facade because I think of a facade as almost wrapping another interface, whereas I think of a view model more as an object with inputs and outputs. And so these inputs might be dependencies, which it internally might subscribe to to get updates, or they could be static inputs that the view model does something with too. And then the view model has outputs which are exactly what the view controller needs to put whatever the view's concern is on screen. So you may have a view model that you initialize with, let's say, some sort of reference to your persistence layer and some sort of step counter or something, right? This may not be a great example since ideally I think the step counter would probably update the persistence layer somewhere else. And then the view model will just subscribe to the persistence layer, format the data for display and spit out, say, NS attributed string, right? And then the view controller just takes that string and puts it on screen in the right place, as well as handling all the view layer concerns that UI kit gives it.

Soroush Khanlou
That makes sense so far?

Chris Dzombak
Yeah. Okay, good. I'm glad. I haven't really practiced this explanation. So I hope that everyone's following so far.

Soroush Khanlou
I'm with you so far. I really like the distinction between application logic going in your view model and view specific logic staying in your view controller. And I think that is like a very clean way to separate the two things.

Chris Dzombak
And that's something I really want to emphasize here, is that there's so much talk about view models, but all I'm arguing here is that this is a good way to incrementally improve iOS application architecture by starting to separate out some responsibilities.

Soroush Khanlou
Now, let me ask one more question. Your interfaces to your view models, are they protocols or is it just the concrete view model type itself?

Chris Dzombak
That's a very good question. What do you mean by interfaces to view models, though?

Soroush Khanlou
So the view controller holds onto a property, it'll be like, let view model and you'll have a colon and there'll be a type there, and then it'll be set to whatever. So that type that's set there, is that a protocol that represents this view controllers? The things that this view controller needs or is it the actual concrete type.

Chris Dzombak
Of the yeah, okay, I see what you're saying. It is a protocol. Let me explain why. Because you could make an argument for doing either, right? In this case, this means that a view controller can define a protocol. That is, this is the data that I need in order to put things on screen. These are the events that I need to be able to tell this sort of coordination layer. The user tapped this button and the view model may do something in the persistence layer or at an API client to respond to that action. But really, the view controller doesn't need to know much about the concrete type that's doing this, right?

Soroush Khanlou
Right.

Chris Dzombak
So it makes sense to have a protocol there if you were doing something dead simple. I mean, you could just have the view controller know about the concrete view model type. The other argument for having a protocol here is that that opens the door for you to do snapshot testing of your view controllers. So let's consider view controllers as just being part of the view layer. Well, in order to just test the view layer, you don't want to have to put together like you're not going to mock up a fully featured view model and try to adjust all those inputs. You want to be able to just inject a view model that just effectively exposes static data to your view controller, put the thing on screen, take a screenshot and see if it works.

Soroush Khanlou
Right? That makes a lot of sense. There is another benefit to view models as well, which I heard a little bit about on another podcast called Runtime FM, hosted by friends of the show, Sam Sofus and Caleb Davenport.

Chris Dzombak
Great show.

Soroush Khanlou
And they talked about or Caleb mentioned specifically that his collection view controllers, they have a view model property. And so, like, let's say he needs to display some data and there's an empty set of results. That is one specific concrete view model type that conforms to this protocol that the collection view controller needs. And so he'll just update the view model on the view controller and say like, okay, now that this is updated, just refresh yourself and everything will just lay out as it should. And then if new data comes in, he can say, well, here's some fresh data, do this. Or if an error comes in, there's like an error view model, for example. And as he swaps out that view model property, the view controller can just refresh itself and just show the exact right thing without having to worry too much about conditionals and all that stuff.

Chris Dzombak
Absolutely. And that kind of touches on something else that I think is powerful, which is that depending on exactly how a view model is designed, you can compose view models too, right? Like, let's say some view models, depending on the screen that they're powering, may be fairly complex and fairly specific. Right. You could imagine another view model, for example, one that knows how to take a blog post and knows how to apply different formatting to the title and body depending on some properties of the.

Soroush Khanlou
Context that it's displayed in or whatever. Sure.

Chris Dzombak
And then spits out an attributed string. Well, that's something that maybe isn't really specific and maybe is all you need to power a screen that shows a blog post. But then let's say you want to show a blog post in another screen in your app. That simple view model. You could compose that into a view model that is powering another screen where displaying a blog post is only a small part of that screen. Right, right.

Soroush Khanlou
But there's no formal connection between these. It's just a you should write the code that will connect these two together in a composed way. It's not as though, like, you have a composed view model type that takes.

Chris Dzombak
Multiple view models and no, I'm imagining something here that's more ad hoc, where your blog post collection view model has a few of these sort of blog post view models just as dependencies and it just knows about the blog post view model protocol.

Soroush Khanlou
Right. That makes sense.

Chris Dzombak
And uses them under the hood.

Soroush Khanlou
Got you.

Chris Dzombak
Cool.

Soroush Khanlou
So is there anything else on the base level explanation of view models that you'd like to touch on?

Chris Dzombak
No, not really. Again, I'll say is it's, I think, a pretty simple and simple incremental improvement. And I'll sort of emphasize that this isn't anything that's really formally there's no really formal definition here. Right. It's just take the sort of coordination and responding to actions that your view controller does now about responding to responding to actions that are application concerns that's in your view controller and put it in something that you can test.

Soroush Khanlou
Right. It seems kind of like Coordinators in that sense of just like there's not really a really formal pattern or like any strict interface. It's just like build the thing that you need at the time that you need it.

Chris Dzombak
It's a lot like Coordinators in this idea that I will keep coming back to, which is identify things that have a lot of responsibilities and try and break them down.

Soroush Khanlou
Right.

Chris Dzombak
There's going to be a recurring theme on this podcast.

Soroush Khanlou
So that actually leads into what I would say is one of my first big criticisms.

Chris Dzombak
All right, let's hear it.

Soroush Khanlou
So I wrote a blog post about half a year ago now, and it is called MVVM is Not Very Good. I remember this and I originally had actually titled it MVVM is Terrible. But MVVM is not terrible, it's just not that good in my eyes. And so I changed the title of the blog post to something that I thought was a little more accurate. But one of my big concerns with the view model is that because the name is not precise, because the name is very abstract. Well, it's just a View model. You can put things in there sort of out of Laziness. In the same way that you would with a View controller. And while you could just be strict with yourself and make sure that you always do the right thing and be really strict in code review, if you name the class. Let's say you were talking about something that formats the attributed string for a blog post. For example, if you take that code and put it in something called a presenter, you can never put any code in there that has anything to do with network logic, because you know that as soon as you put in there, it's like, this makes no sense.

Chris Dzombak
Sure.

Soroush Khanlou
Never go here.

Chris Dzombak
So can I respond to this in three prongs I want to hear, let's see if I can hold this all in my mind while I speak. The first one is that you're right, it's not formally defined. That doesn't necessarily mean that it is bad. It's certainly still better than throwing all these things in a View controller.

Soroush Khanlou
I agree with that, definitely.

Chris Dzombak
So my second prong here is let me try to give a slightly more formal definition, kind of off the cuff, all right? But the goal of a View model is to model the interactions and the coordination and the actions that are needed in order to drive a View in the app, right? So it's to model all of the sort of application and domain logic, the coordination with other objects, and the sort of data outputs that are needed to drive a screen in the app. Third, this idea isn't incompatible with presenters, for example, if that's something that concerns you, there's nothing about this pattern that stops you from breaking out other responsibilities into other objects. And you should and you could keep going and really hone the idea and really hone these ideas out into separate objects down to the point where you have a View interactor presenter. I forget what the e is. And entity and entity responder is that.

Soroush Khanlou
No, it's router and router router.

Chris Dzombak
So the question really becomes, for your application, where do you start seeing diminishing returns on that? I think in a lot of View models, it might make sense to sort of let the View model just handle the, again, coordination between objects and have reusable presenters. Kind of like the blog post view model that I described earlier. That almost feels like a presenter, doesn't it?

Soroush Khanlou
For sure. And it's interesting, you keep bringing up coordination between objects that drives a View, and that sounds a lot like the facade pattern. And we'll put a link to the show notes for the facade pattern, okay? And I think that if it were defined in that way as like, look, this is a object that gives the view control everything that needs to function, but it should function as a facade. It shouldn't really do any logic. It should just glue together these components. I think I'd be a lot more comfortable with it that way.

Chris Dzombak
You can think about it like that. I'm happy with that.

Soroush Khanlou
Yeah. And I think I might I really like your distinction. I haven't heard it before of like, view specific logic goes into the view controller and application logic goes into the view model. I think that's really smart.

Chris Dzombak
What is your company paying you to write versus what do you have to write for Apple?

Soroush Khanlou
Right, exactly. So maybe in another world, if you could and I think some people do write Swift Android apps, you could wholly take your view model from Apple's system and put it into a thing. And it theoretically, obviously there'd be a ton of weird concerns.

Chris Dzombak
This is the dream.

Soroush Khanlou
Theoretically, you could use it in a totally different context and a totally different platform.

Chris Dzombak
Theoretically.

Soroush Khanlou
Yeah.

Chris Dzombak
That division that's really theoretical would be nice if that worked, but that may be a useful way to think about right, yeah.

Soroush Khanlou
Okay. I really do like that. There is another pattern that some people like that they also call ViewModel that I want to touch on, which is I would call more accurately view data where in the same way that a UI label is set up, with a string that is its text property or a UI image is set up with an image. Your profile view would be initialized with some in Swift. It would be a struct that would have all the fields that it needs, but it would be very dumb. It wouldn't have any of the transformation logic. It wouldn't have anything other than just the pure data that this thing needs to be configured with. And that way you can make the fields make the sub views on, let's say, the profile view be totally private and then no other view can or no other object can access them and tweak them and change the parameter so you know that they're, like, sealed inside this class and the view data is the only thing that crosses over that boundary.

Chris Dzombak
Sure. Again, a three prong response. If I can remember all of the prongs, there's nothing about what I'm describing so far that prevents the view controller from keeping its views totally private. Right. Once you bind a view model to once you bind a view model to a view controller, it's the view controller who's responsible for consuming updates from this view model protocol, which, again, the view controller set out and updating its views appropriately. So those can be totally secret if you want to have the outputs be rather than like a set of string or attributed string properties. If you wanted to set up a struct that the view model spits out and hands over to a view controller or a view subclass, that works fine. That I'm going to view as a little bit more of a stylistic choice. Right.

Soroush Khanlou
I would even give it a different name. It's a really different way of approaching I would call it View data rather than View model.

Chris Dzombak
Well, so then you still have something that's handling the sort of coordination to put together that bag of data, right?

Soroush Khanlou
Yes.

Chris Dzombak
That, I think, is your view model. The structure is more your view data or something.

Soroush Khanlou
Right, I got you. Yes.

Chris Dzombak
And so what you also might do, again, you may try to separate the sort of formatting of data for a specific screen date formatting, applying font sizes and colors, all that kind of stuff, out into another object, which again, maybe is part of the pipeline downstream of your View model and above your View controller. And that maybe fits into what you're describing to.

Soroush Khanlou
Right. I think MVVM, likers, want to treat the view and the view controller as the same, but I think this distinction between a struct that holds just the pure data versus a live view model object that you can bind to, and I'm assuming bind in this context, you're referring to, like, a reactive type of thing, which hopefully we'll talk about.

Chris Dzombak
We'll get to that.

Soroush Khanlou
Yeah, maybe a future episode. But I would never pass that kind of live object to a View where I would feel totally comfortable passing it to a View controller. What are your feels on this?

Chris Dzombak
Yeah, I'll totally agree. So I'm considering View controllers here as, quote, part of the View layer, right? Because that is sort of where they live in this sort of overall UI kit land. But you're right in that Views and View controllers do have separate they exist for different purposes.

Soroush Khanlou
Right.

Chris Dzombak
And I would go so far as to argue that whether you are binding data from a sort of live view model with observables as outputs, or whether you're assigning a view controller or you're assigning your view layer a struct, that's a bag of data. Either way, I think that sort of distribution of this data to the underlying views is still probably a view controller's job.

Soroush Khanlou
Yeah, I would agree with that.

Chris Dzombak
Rather than a UI viewer class the.

Soroush Khanlou
Way I would do it. And I always thought this was what people meant when they talked about View models, because in a lot of tutorials it was. But I would basically have a View controller that has a presenter, and then it initializes that presenter with whatever actual data and model objects that the presenter needs to have the output. And I usually make a method called like configure view, and that's where the binding would happen and it would just say like, username text label text equals presenter, the name with the at appendix and whatever formatting needs to happen. And so that's how I would typically, typically do that kind of thing.

Chris Dzombak
Yeah, I think of some of the there's a little bit of a problem of terminology here, right, because these are sort of less well, understood terms, there may be different subcommunities who have slightly different understandings. It was really important for me starting this podcast to give a clear overview of what I thought I was talking.

Soroush Khanlou
Did a really good job, for sure.

Chris Dzombak
Thanks.

Soroush Khanlou
So the idea of View models and MVVM originated from a Microsoft white paper. I'm not exactly sure what framework it was supposed to work with, maybe one of the net ones. There's a really good post that somebody posted in response to my MVVM is not very good post and I will try to dig that up for the Show notes. But basically in this Microsoft firm, they didn't really have something that served the role of View controllers. And so they made up this thing called View models and it was supposed to sit in between the view and the model and serve as sort of an adapter mediator role in between the two, much in the same way that our View controllers do today.

Chris Dzombak
I like the term mediator here. That's a nice word.

Soroush Khanlou
Mediator is a great word.

Chris Dzombak
I'm going to remember that. So I'm going to just really briefly, I'm going to speculate, not knowing anything about this, that if they didn't have something like View controllers, probably their View layer had some of the responsibilities that we associate with View controllers in UI kit.

Soroush Khanlou
I wanted to get up this post so that I can be sure about this and it will be in the Show notes, but I think their view layer was all XML, so you actually couldn't put any code in there. It was purely just this layout. And these views are here. It's an interface builder file, for example. And I think then that forced them to put the code in really weird places, sometimes in the model, sometimes in these really ad hoc controller objects. And so View models were proposed as an idea to make sure that everybody was kind of doing it the same way. Yeah, cool. Yeah. I have one sort of implementation level question as well. So I understand how especially like in a reactive world, you have a property on the view model that is observable and maybe it's not observable, maybe it's just a text property and you can read from that property and append it to your views. When a user taps a button that probably funnels through the view controller and then at some point that signal or that piece of information needs to get to the view model. So the view model can do its internal cooking and then output some changes.

Chris Dzombak
Right?

Soroush Khanlou
How does that part of the binding happen?

Chris Dzombak
So communicating user actions from the view up to the view model and presumably to whatever in the app needs to happen, this is pretty much as simple as you might expect. Remember how the view controller defines a protocol that says, this is what I need the view model to do. Like this is the application domain logic that I need to power my in the app we're working on so far, those protocols might just contain a such and such button tap or like such and such user action.

Soroush Khanlou
Just a method.

Chris Dzombak
Yeah. And then the view controller just calls that. That means that you can still test that the view model does the correct things in response to that. Right. Because there's nothing again, that's just a method on the view model. It's not tied to the view layer. So that's still testable. And, I mean, it's dead simple. There are very few things that are difficult to debug about that particular interaction.

Soroush Khanlou
Right. I'm really curious about the reactive stuff now in that world, is there a way to say this is a source versus this is a sync? Like, your name property would be a source of data coming out, but how do you define, like, a sync?

Chris Dzombak
Yeah, go to so how would I define that propagation of a UI event in a more reactive right way?

Soroush Khanlou
Exactly.

Chris Dzombak
Okay. Not having done this recently, I don't have a really good answer for that offhand. There certainly are any reactive framework, especially reactive coco has some UI kit extensions. RX Swift may or may not. I haven't really used RX Swift. They do provide nice UI kit bindings. So you can have a signal as an output or an observable as an output from a UI element. But I'm struggling to think offhand of exactly what the most elegant way to set that binding up would be while still maintaining the same sort of ownership chain that I've described so far.

Soroush Khanlou
That makes sense. Well, let's do some research and we'll come back.

Chris Dzombak
Yeah, we'll come back on this. A future episode that we do, I think will definitely be about this sort of reactive programming world. And we'll do a little research here, and I'll have a much better answer for this later.

Soroush Khanlou
That makes a lot of sense. Yeah, I'm really looking forward to that one. I think that one will be really good.

Chris Dzombak
I think so too. So since you mentioned the sort of reactive programming world, I think something which I've been assuming this whole time, but never said explicitly, is that the outputs I'm talking about on these view models are exposed as observable or signal properties. So each of those represents just almost like a promise, but something that the output will change over time, and you can subscribe to that and get updates. So when you assign a view model to a view controller, the view controller says, okay, I'm going to subscribe to these properties of the view model, and when one of them changes, I will update myself appropriately. I will update my sub views appropriately.

Soroush Khanlou
Right. I think if I were doing that in a non reactive context, I might just have a delegate that says I'm a view model and I updated. And then that would call that like, configure view method. Which would just reset all the properties to the outputs of the View model. I think it functionally works the same.

Chris Dzombak
I mean, functionally, but you're right, that would work the same. That's going to be more concept. That's going to be a little more boilerplate. Your testing of that View model because you have a delegate relationship involved now is going to be a little bit more challenging. That's a good point, but you're right, that could work.

Soroush Khanlou
All right, cool. That makes sense. Is there anything else you want to add about View models?

Chris Dzombak
No, I think I'll call out that we would welcome input from listeners on what do you think a ViewModel is? Is it different from what I described? Do you have better ideas about handling bindings? Do you have nifty ideas about binding a View model to user interface actions while still maintaining a sort of, for lack of a better term, a one directional ownership graph here. Right. I really do love having a clear picture of object ownership in my applications. But beyond asking listeners to point out what I'm missing and what I don't know, I don't think there's anything else I wanted to note.

Soroush Khanlou
Cool. Yeah, I think I touched on all the questions I have. I have a much better picture of how you would actually set this up.

Chris Dzombak
Okay, cool.

Soroush Khanlou
So I feel like I've expanded my horizon on this topic a little bit.

Chris Dzombak
I'm really glad to hear that. Well, on that note, I don't have anything else to add. Do you have any more questions?

Soroush Khanlou
Cool. No, that's it from me.

Chris Dzombak
All right. As always, thank you for listening. This has been episode two of Fatal Error, and we'll talk to you in two weeks.

