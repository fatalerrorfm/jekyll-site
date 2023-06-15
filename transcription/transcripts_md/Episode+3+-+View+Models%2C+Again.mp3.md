Soroush Khanlou
We're figuring out. This is our first this is my first day. You know, I've never podcasted before.

Chris Dzombak
What is what is a podcast? What what is like what is male.

Soroush Khanlou
Kemp it's it's it's have you heard of Feedburner? It's like feedburner.

Chris Dzombak
Welcome, listeners, to Fatal Error, episode three. I'm Krista Zomback. I'm Sirush Khanlo, and I just had to think for a second to REM remember what the podcast was called. This is where I am. It's been a long day. We got a little bit of feedback on the last episode about View models. And when Seruish and I went out for drinks after recording that episode, he had some other questions that he'd forgotten to ask during the recording. So we figured, why not do another.

Soroush Khanlou
Episode about view models, like a Prudent podcaster? I did not ask the questions at the time, and I held them in me. I held them in for me for two weeks, and now I'm ready to release them.

Chris Dzombak
Excellent. Well, do you want to kick us off here?

Soroush Khanlou
So before we touch on some of those questions, I want to address one of the biggest pieces of feedback we got about that episode of the podcast was a lot of people were dismayed, I think is a good word. That view model has come to mean this thing that's live and active, that you bind to, that maybe acts as a facade, maybe acts as your application data, like the thing that is alive and holds your application code instead of being the inert dead thing. And I don't know, I feel like the reactive side of our community has taken this term and made it their own. Not that there is anything wrong with that, but that's sort of what's happened. And the battle for inert view models is sort of lost already. And I was kind of wondering if you had any thoughts on the value of inert view models versus the value of live view models.

Chris Dzombak
Okay, so this is kind of getting back to a question that you asked a little bit in episode two about having a sort of static bag of data that you hand to a view in order for a view to present. Right?

Soroush Khanlou
Right. So if it was swift, it would be a struct. It would not have computed properties. It would just be a set of properties on a thing, just holds data. No behavior, no functions, no computer properties, just data.

Chris Dzombak
Okay, so, man, let's see what comes to mind here. We're talking about a few different responsibilities here, and it doesn't matter to me that much what you want to call each part. We have a view layer, and we all know pretty intuitively what that view layer does. Although I'll make the argument, like I did in the previous episode, that the view controller is more or less part of that view layer. Its responsibility is controlling views. We have the responsibility of basically being the data that gets presented in a view. Right. And this is what you're alluding to as what you might want to call a view model. And we have the responsibility, which is a little bit less well defined, but the responsibility of taking input from that view and producing data that needs to be and producing that bag of data that's going to be assigned to that view.

Soroush Khanlou
Right, right. Whether that comes from the network or the database or from some user action.

Chris Dzombak
Right.

Soroush Khanlou
Like a form.

Chris Dzombak
And again, that probably involves collaborating with at least one other object within the application that is at some level shared between different parts of the application. Right?

Soroush Khanlou
Right. So I guess the argument is we definitely don't want to put in a view controller and you should put it somewhere and you might as well call that a view model.

Chris Dzombak
That's an argument. Yeah. So certainly we agree that these three responsibilities are separate and probably shouldn't all be jammed into the view controller, right?

Soroush Khanlou
Right. Yeah. I don't think there's anybody who's going to disagree with that.

Chris Dzombak
So then it becomes a question of what these other responsibilities get named and whether they are somehow combined together into one object. So then it becomes a question of how we split up the other two responsibilities, the sort of inert data and the sort of live coordination responsibilities and what we call those responsibilities. Now, remember in my version of what a view model is or what a view model might look like that I presented in the last episode how the in the view controller there there's the definition of a protocol of what the view controller needs from a view model in order to update the view and display data on screen. Right?

Soroush Khanlou
Right.

Chris Dzombak
You could look at that protocol as being effectively just the specification of that inert data. Right. I mean, all it specifies is that I need these certain strings or other values to put data on screen. And then the other thing that that protocol might define is I need to be able to propagate these events up to someone in the application who will deal with them.

Soroush Khanlou
I don't know. I don't actually like that very much if it's just a protocol that provides strings or observables of strings. First of all, those are, I think, two very different things. And second of all, okay, so imagine you have your full model, right? You have an entity. That entity knows how to write itself to the network, let's say, or write itself to the disk. It's an NS managed object subclass, and you put a protocol on it. Just because there's a protocol on it doesn't mean you're immediately comfortable passing it directly to a UI view subclass. Right.

Chris Dzombak
You will have something in between needs to produce that data. Right?

Soroush Khanlou
Right. And so I'm saying so there are live objects that even if you wrap them in a protocol, for some reason, it still feels pretty gross to pass that directly to a view. But the inert data, we feel more comfortable saying, yeah, the view can just have it because it's just inert, it's just data. It's not doing anything. So I feel like there is a real difference there between view data and view data being the inert thing and view models being the live coordination facade, complex, reactive thing.

Chris Dzombak
There definitely is a difference. But maybe let's take reactive out of the picture for a moment and consider maybe that there's just a protocol that specifies that we need these certain strings and certain values. Does it really matter so much at the view controller, at the view level, whether you provide an object backing that protocol that's a reference type with some other responsibilities, or whether it's a struct that conforms to that protocol?

Soroush Khanlou
Right, so it shouldn't. But for some reason, again, if you're talking about view controllers, like, yeah, I'm fine with a view controller having access to this kind of data, especially if it's wrapped in a protocol. But if you're talking about a view and I can't really explain why I feel that that's different than a plain bag of data struct, I can't explain why I think that's different, but I do think it's different. I wouldn't feel comfortable passing an entity or a view model directly into a view subclass even if it were wrapped in a protocol and the view subclass didn't know what was going into it.

Chris Dzombak
Okay, so there are one or two differences here that I want to probe you on a little bit further. Yeah, for sure. First, you're drawing a distinction between view controllers here and a UI view subclass, which maybe is a useful distinction to draw here. Right. When I talk about a view controller or a view layer defining a protocol that determines what data is needed to drive that view, I'm really thinking more at the view controller level. And I'm thinking that the view controller is what is the object that is unpacking whatever data is being handed to it, whether it's in a struct through a protocol interface, or just a struct whose type we're using directly, or whether it's taking values from some observables and assigning those values, those inert values, into its view hierarchy. Right, right. I also will agree that a UI view probably doesn't need to know or probably shouldn't know about observables or deal with other live objects.

Soroush Khanlou
Right. But I think the thing that the people who champion, like sort of the other form of view model, view data, I think is probably a better way to call it, especially for the scope of the show. They want to take a struct and they want to pass it directly to a view subclass. So the distinction here is between those two things, if that makes sense.

Chris Dzombak
All right. I mean, that makes sense. So we're talking then about two first, we're talking about two different patterns here.

Soroush Khanlou
At this very different pattern. Although it's unfortunate that they have the same name.

Chris Dzombak
Well, they have the same name, although they're not necessarily incompatible. Right. You could imagine a live view data producer of some sort that hands a new instance of a view data struct to a view controller, who then unpacks that and hands view data some embedded view data structures down into its view subclasses. Right, right.

Soroush Khanlou
Totally.

Chris Dzombak
And my other thought is that, which I just touched on, is that that view data structure still needs to come from somewhere, something has to produce that, and that still shouldn't be the view controller. And I mean, call it what you want, I'm going to keep calling that a view model.

Soroush Khanlou
Yeah. I think that the tension here is almost entirely sort of naming wise. There's no tension of like I don't think either party thinks the other party is bad, and some people maybe do both, but the tension is that we have overloaded this term.

Chris Dzombak
Sure, I think that's definitely true. And yeah, the more I think about it, the more that the way you've described it, at least, these ideas aren't really incompatible. If you want to define a very specific structure type that a UI view takes, it still has to be produced somewhere, which probably shouldn't be a view controller. Maybe the view controller collaborates with some other live object to get a view data structure and assign it to its views.

Soroush Khanlou
Yeah. So you're actually I think it sounds like you're even going a step further. You're saying view data is fine, but don't do just view data, make sure that it comes from some kind of view model, whether or not you choose to actually call that live thing that produces the view data a view model. But you're saying, like, don't do view data if you're just going to create the view data within the view controller. Am I understanding? You right.

Chris Dzombak
More or less, yeah. Moreover, I mean, do that if you want, but be aware that no matter what you do, if your view controller is responsible for collaborating with other objects to produce values to assign to views.

Soroush Khanlou
Right.

Chris Dzombak
I don't care what pattern you're using to assign those values to those views, your view controller still is doing too many things.

Soroush Khanlou
Right, right. I'm sympathetic to that, for sure.

Chris Dzombak
I totally agree and acknowledge that there's tension here, but I think it's mostly AA tension in naming because I don't think these ideas are very incompatible.

Soroush Khanlou
Yeah, I think that seems right to me. The people that I was talking to about the view data thing still want to call it a view model, and one of the things I said was I was sort of like, yeah, I think the battle has kind of already been lost and they sort of reluctantly agreed. So I think there's sort of not much else to be said about that, basically. So I have one big question which I think we touched on in the Coordinator episode. I think have one question here. And then I have two kind of heretical ideas which I would love to run past you.

Chris Dzombak
This sounds great. I love it.

Soroush Khanlou
This question may also result in a heretical idea. So that's three heretical ideas which may be too many for a podcast episode, but we're going to do it anyway. So we touched on this question of in the Coordinator episode, we talked about Coordinators not only handling flow, but also handling model mutation, which I defined as you might be hitting an API, you might be writing something to the disk, to the keychain, something where the user's action is like somehow persistently or semi persistently stored.

Chris Dzombak
So you talked about this. I'm not totally on board with this.

Soroush Khanlou
I talked about this and the reason being, I think I gave a couple of cases of when that's useful. For example, if you want to change the flow of, let's say, some kind of posting screen that lets you get into the posting screen before you've logged in, you tap Post, and at that point you have to log in, kind of pushing that login flow down the funnel a little bit. And when you do that, change in the flow in order to not have to change both the view controller, which originally was handling the quote unquote model mutation, which is like posting this message, but also so you would have to change two components. You have to change the coordinator to add this extra piece of flow. And you would also have to change the view controller to handle the fact that while sometimes you're going to be going through this alternate flow to log in, and sometimes you're just going to be directly posting to the API or wherever you're posting it to. That's like one example of attention of you don't have to change both of those objects for that case. So having the view controller be really dumb and I think this is sort of I don't really disagree when you say that the view controller is part of the view layer. And because of that, I don't want it to be able to mess with data. I'm fine with it reading data to some extent, like if it's just a get request, I'm more or less okay with that. But when it starts writing data, then I feel like you become more hamstrung with the ways that you can use that specific view controller. So having the delegate methods on the view controller be things like did tap button or did perform whatever user action, I think gives you the flexibility to when a change comes down the pipeline from your product team or your designers or whatever, you can make that in a clean way. If you bring both of these responsibilities up into your Coordinator rather than leaving one in the view controller for the context of this episode the view model and one of the responsibilities in the Coordinator. So how do you solve that problem in your view model world, given that you don't want to put the mutating code up in the Coordinator?

Chris Dzombak
So let me ask a clarifying question here. So I think I understand what you're describing and what you're asking in the case that you're describing is the Coordinator. Do you mean that the Coordinator is collaborating with some other object in order to determine the user's login state and mutate it? Or I mean, is the Coordinator doing that more directly?

Soroush Khanlou
So in the way that I would do it, when you tap the button in the view controller, sort of, you get like a target action which comes to your view controller layer. Your view controller fires a delegate method which then bubbles up to the Coordinator and then that is where the view controller's responsibility stops. The view controller does not know if another view controller will be pushed on navigation wise, if it will be presented modally, or if some API action is going to happen. It really can't know what's going to happen after that. Ideally, yes, it will be in some kind of collaborator of the Coordinator, but it won't I don't think the Coordinator should be like touching an S URL session directly. I think that because the concepts of model mutation and flow are so intertwined in these weird cases, you have to move this stuff up. And I'm wondering, if you were designing this exact same screen, how would you because it sounds like in your world, a view model would have a method on it that's like post with data or whatever, and that is hidden from the view controller by way of encapsulation. But then, if that flow needs to change, how does the view controller now know whether it should talk to the Coordinator or whether it should talk to its view model?

Chris Dzombak
Okay, let's see here. So with the caveat that I'm designing this totally after thinking about this for tens of seconds, it might as well.

Soroush Khanlou
Be a tech interview or tech job interview question. Whiteboard ready?

Chris Dzombak
This would be good. Well, let's set that aside. So what what I would do here is so clearly the view controller calls up to the view model, says, hey, the user tapped the post button and this is the content of this field or something, right? The view model at this point, I'm going to say probably delegates out to some other object, right? Because in order to fulfill this requirement, the login is deferred and can be injected into this later point in the sort of flow of the application. It feels like there's maybe some other object that almost handles in queuing this state, if that makes sense. Maybe it's your sort of user login Coordinator that authenticates one of these requests before it goes out and then that maybe has some way to flag to the applications flow coordinator that a login is needed. I'd have to think a little bit more about what goes on behind the scenes. But the high level answer is this switching logic doesn't go in the view model or the view controller. The view model knows to delegate out to another object that handles this switching logic, maybe.

Soroush Khanlou
Right.

Chris Dzombak
That kind of feels like kicking the problem down the road, though.

Soroush Khanlou
It is. So eventually you get to a point where something is going to be owned by the view model and knows about the coordinator, whether it's through a block or through a weak delegate or whatever.

Chris Dzombak
Yeah.

Soroush Khanlou
And so why don't you just do that right at the source? And just all my view controller does is ties well, this still isn't the view controller.

Chris Dzombak
Right?

Soroush Khanlou
Well, what I was all the view controller does is it binds the model data to the view, in this case view model data to the view. And then also whenever any action comes in or an S notification or any of that stuff, it just bubbles that up to the coordinator and the coordinator is in the position to make all of the decisions that it wants.

Chris Dzombak
Yeah, this kind of makes sense. Okay, my answer 2.0. What I would do, the view model takes this, takes this input delegates out to your API client, says, hey, post this data. If the API client comes back with an error that says login, hey, the user needs to log in. Yes. There's probably a way to make this more there's probably a way to mix this logic into your view models in a reusable way. Maybe extract this little bit, that little bit of logic out to some object that deals with API responses. Right. But then your ViewModel can take this and say, oh, hey Coordinator, go perform a login flow and call me back when this is done.

Soroush Khanlou
Yeah, I like that better. That's definitely better. But I feel like you still have two delegates now. You have one delegate of the view controller that the coordinator conforms to, but then you also have another delegate of the view model that the coordinator also has to conform to. Why make this difficult for yourself?

Chris Dzombak
Well, so I don't see the view controllers having any reference or knowledge of the coordinator whatsoever.

Soroush Khanlou
Well, it's a delegate, right? I guess. Do you all not use delegates to.

Chris Dzombak
Bubble the messages of communication between the view controller and coordinator is entirely through the view model in response to the user inputs or other inputs. Because again, the view model is where all the logic that drives this view belongs.

Soroush Khanlou
So if you had a table view, let's say an article list and somebody tapped on an article, you wouldn't pass that directly to the coordinator. You would pass that to the view model, which would then know to bubble that message up to the coordinator.

Chris Dzombak
Right.

Soroush Khanlou
Okay, then, yeah, that's basically the same thing as I'm saying. But yeah, having the one delegate, I'm perfectly satisfied with that solution.

Chris Dzombak
So in this case and you can probably think of a way like it probably would be messy to have this sort of check for an error and bubble up to a coordinator with a callback in every view model. So there's probably some object that a view model can instantiate to handle that little bit of logic or flow or something that you'd have to consider the pros and cons, but not a mix in what's it called a protocol extension in Swift that a view model can use to bring that logic in.

Soroush Khanlou
That makes sense. That makes sense. I didn't realize that even your flow methods go through the view model.

Chris Dzombak
Yeah, again, this keeps your view controllers very isolated.

Soroush Khanlou
Right.

Chris Dzombak
This means that even that flow, in most common cases, that sort of flow logic that the view model handles is trivial and your tests for it are going to be trivial. But maybe there are some other cases like this one where you do want to test that your flow coordinator or excuse me, your view model tries to kick off the correct actions in collaboration with the flow coordinator. So this lets you test that interaction as well.

Soroush Khanlou
Got you interesting.

Chris Dzombak
Okay, I can almost see you interesting.

Soroush Khanlou
Because I was actually sort of trying to push you in a slightly different direction, which was that I'm more comfortable with my view model or with my view controllers reading and not writing. And so if you were able to split your view model into one read only component and one more or less write only component, reading what it needs to do to do the writing, and then having passing the read only component down into the view controller and then keeping the read write component up in the coordinator, then you could get all the effects that you want. But the way that you push that message down and then back up through the coordinator like bypassing the view controller is super interesting. Where I was going with it is a read only view model sounds a lot like a presenter and a write only view model sounds a lot like an interactor and all of a sudden you're in a whole new place, you're.

Chris Dzombak
In a whole different ballgame.

Soroush Khanlou
Yeah, exactly.

Chris Dzombak
But no, you're right, it does sound that way. A read only view model also does sound offhand to me like a view data structure that you were discussing earlier.

Soroush Khanlou
Well, I would actually say it's different than that because I would have a read only view model presenter actually construct that data in real time with computer properties rather than computing all that stuff up front. That kind of doesn't matter really, where you do it. But that's probably how I would do it is just defer that execution until you need it, until you always are sure that you have fresh data. And I don't know if you would agree with this, but I feel like I'm turning your own guns against you. But having a View model whose only responsibility is to prepare data for presentation seems like a better single responsibility object than one that does both that and all the model mutation and other stuff that you might have to do.

Chris Dzombak
Oh, yeah, you're not going to get me to disagree with that at all. We talked in the previous episode about the possibility of decomposing View models into smaller View models that seem almost more like presenters than full fledged live View models. Which, again, we can do because this terminology is incredibly imprecise. And that seems a little bit like what you're describing. And then those could be reused very heavily throughout a code base and composed into larger, more complex View models.

Soroush Khanlou
Okay, cool. I did not expect your solution with the View model having the handle on the coordinator. I didn't realize that's how you all were doing it. And that actually makes so much sense. So that's super interesting. I have now here with me two heretical ideas. I'd like to let them out of the bag and I want to know what you hear about them. The caveat is that I know that they're kind of whack, but also are they whack? So the first one is that so traditional MVC. MVC was invented for small talk, right? And the idea was that you had a view which was responsible for putting data on the screen. You had a controller which was responsible for corralling user input, and then you had a model which was responsible for all the data basically involved in this. And the thing that's different about classic model View controller versus what we do now is that the model and the View talk to each other directly. The controller and the View talk to each other directly, and the controller and the model talk to each other directly. What we have now is more of a model view adapter, model View mediator, however you want to kind of break that down. But we don't let our models talk to our views. And that is really, really very different than the thing was originally intended. But our conversation last week got me kind of thinking that we call our entities models. Like we call them model objects. But really I think entity is a more precise term and expresses what we mean, right? Which frees up this idea of model. And the thing that I kind of like is instead of calling it View model, we could just call it a model. So you'd have a sign up model that has any validation functions on it, or any validation collaborators, however you want to look at it, it has any actions that are associated with signing up and all that stuff. And that is the model to a View controller. In the same way that a View control has one view, it would have one model and that model and the model and the view would be bound together via this controller. And I feel like if we release the term model from our model objects like Tweet or whatever, we can get to a place where I think model is really what we're talking about. It is a model for the controller to consume and apply to the view.

Chris Dzombak
Sure, this doesn't sound that crazy to me. I'm looking at actually the Wikipedia page for model view controller right now. They have a nice little flowchart here. We'll include a link to this in the show notes, but this says the model directly manages the data, logic and rules of the application. This sounds kind of like what I'm describing here. You're starting to shift some of these responsibilities for, again, your application domain logic from a view controller up into this other object, which I've been calling a view model, which is a model that manages the data, logic and rules of the application needed to power such and such a view. An important observation here, I think, is that the view model that I've described is really only a part of the whole model for the application. Right. Managing the data, logic and rules for an application, like in an iOS application, there's a lot there. You have caching, networking, those responsibilities, just to name a few. But your view model is sort of your window into that world for the view and controller.

Soroush Khanlou
Yeah, I agree with that. I also don't think that's necessarily incompatible because this talks about a view as well, and it doesn't require that the view is every single view in the app. It can be, I think, a slice of the model and the rules and the behaviors of our application in the same way that the view is a slice of what the user sees.

Chris Dzombak
Yeah, absolutely. So heretical idea the first is that what I'm calling a view model so far is more of just a window into what you would call a model in MVC.

Soroush Khanlou
Yeah, I think so. And we call it a model layer. But what if you really just had an object called model and then that way you would have to call your other stuff entities or really? We don't even usually append the word model to the names of our models. So maybe it's not even a problem.

Chris Dzombak
No, I don't think so.

Soroush Khanlou
So heretical idea number one. Not that heretical. Is that the verdict?

Chris Dzombak
I'm going to rate that. Not that heretical.

Soroush Khanlou
We're going to get a lot of Tweets, Chris. A lot of tweets. So that was heretical idea number one. Heretical idea number two is that a view model on some level represents data. It represents a consistent view on data. It represents, I would say, like more of a tree like structure of data rather than a graph like structure of data. Would you say that that's sort of fair?

Chris Dzombak
I. Don't quite understand exactly what you mean by that.

Soroush Khanlou
So by tree, I mean there are no cycles in this graph and there aren't like, no child can point to any parent.

Chris Dzombak
So how are you applying that to a view model specifically?

Soroush Khanlou
So, in a traditional application, if you have your model layer, let's say it's a relational database, a core data or an active record, you could easily have a cycle in that. Like, you could have one user that has many projects, and that project has collaborators, one of which is a user that owns another project that has a collaborator of the original user, for example.

Chris Dzombak
Okay?

Soroush Khanlou
So you could just walk this graph infinitely, right? Whereas a view model in a view is a tree, right? It's a single top root view, and that has many child views and child views and so on down the road. But none of the child views ever relate back to the top view.

Chris Dzombak
Right?

Soroush Khanlou
And in the same way, I think a view model is designed to be a really structured form of data, and there shouldn't really be any cycles in a view model, especially like, if you think about it, like the view data way where it's all a struct. The struct that represents a collaborator representing Chris De Zomback would be a separate struct than the struct that represents Chris De Zomback, the project leader. Right. Okay, so there's that. And there's another thing I would add, which is, like, a lot of times it's responsible for making calls out to the network and handling that stuff for like, when a thing happens or when a thing changes. The second heretical idea that I have is that if you if you squint and you got a squint that kind of looks a lot like JSON, JSON is a tree. And every like, if you, if you have if you got a JSON response, assuming that was like the total, totality of the response, that can never have any cycles in it because JSON has to be defined as a tree. And I've seen certain JSON restee implementations that define what methods you can call on that particular Restful model through, like, I don't know how you pronounce it. Hate OS hateos I've got nothing. I don't know how to pronounce it. I barely know how to spell it. It's hypermedia as the engine of application state, which is like rest plus plus it's rest plus this ability to tell you what actions you can take on any given model. And this one, I feel like, is a little bit more of a tenuous, a little bit more of a reach. But basically, when you get JSON back, you could model that as a struct and not have any problems. Whereas if you were in a Rails application or like a really rich core data application, you could never model those core data objects as structs because of these cycles. But JSON is guaranteed to never have any cycles in it. So it's really easy to model that as a struct. And the server can do any processing of, like, if it needs to append first name and last name together to make the full name for display. Like, the server can just do that for you. And so in iOS, our quote unquote model, our entity objects, as we dubbed them earlier, they're really just really thin wrappers around JSON. They could easily be structs. All they need to know is how to turn from a JSON blob, how to take in a JSON blob and become a fully fledged, fully qualified representation of that thing, maybe a little bit of validation. And the Craziest case, they'll need to know how to call out to the web server to do some stuff, which, if your web server returned really structured responses, could just be baked into the JSON itself and baked into sort of a generic way of saying, well, I know I have this type of action I can run on this. Just run this action and be done with it. So what do you think about the idea that our models are already basically View models?

Chris Dzombak
Okay, I'm processing this. Do you mean our models as in our entities? In the definition we came up with? Okay, you still need to get those models, those entities, from somewhere, right?

Soroush Khanlou
Yeah.

Chris Dzombak
So you need something in between. Like, regardless of whether you want to treat one of these models, I'm going to keep calling them models instead of entities.

Soroush Khanlou
Right.

Chris Dzombak
So you could certainly call one of these models as something closer to a View data structure. Maybe aligning the models that you're storing more closely with the format of certain screens in your app is not a bad thing.

Soroush Khanlou
Right.

Chris Dzombak
But there's still coordination to be done in fetching those models from a web service or from a cache in Mutating, and updating those models if necessary. There's other coordination to be done here, and that has to happen somewhere. I would put that in what I'm calling a View model, which is this active, not inert thing that sits between a View controller and the rest of the application with the goal of powering that View controller. And I don't see an inert entity doing anything similar to that. So I guess I'm a little bit confused here.

Soroush Khanlou
Yeah. So there's one thing that I feel like I should also add, which is that, like, generally, we don't we don't have that much logic in our apps. Like, if you look at a really crazy back end app, like a Rails app or a Node app, it's doing a lot more stuff not only in the department of validation, but also in the department of, like, it's billing the user and it's talking to different services, handling emails. It's got logic for like, if you have this many items in your cart, do this thing and this other thing where our clients rarely have that, especially on most of the apps I've worked on. They're really just like a pretty way to look at JSON. That is sure something that Orta of Artsy said to me once, and I was like, yeah, that's really true. It really is just a pretty way of looking at JSON.

Chris Dzombak
And somewhat depressing, but true it is. Don't tell the non app developer.

Soroush Khanlou
Yeah. And so that concept that we don't really have that much real logic in our app, maybe there's a little bit of validation around some of your forms just to be a little quicker for the user, but that validation sometimes comes from the API too. I guess what I'm kind of saying is maybe you could extract all of the weird common components of, let's say, the ability to perform actions on a specific model. You could extract that out into a thing, into a very generic thing. The ability to parse the model that's kind of already there, the ability to combine and compose components of the model. Like, that could just be part of the server thing. Validation could be part of the server, and you could end up with a really lean iOS app that really I mean, it's model layer. I mean, how much does the model layer really need to do? Does that help you understand where I'm coming from? I know this is like I think so, yeah, I'm doing a bad job expressing it. But ultimately, what is it that our model layer needs to do? It needs to parse JSON It needs to prepare some stuff for display, maybe apply some colors to some stuff and put it on the screen, and then be put on the screen, let's say.

Chris Dzombak
So as you get more complex, though, you have Caching requirements to take into account. You may have offline support requirements, you may be dealing with a number of different APIs across the lifecycle, across the user, doing one thing in your application. I agree, but I'm not really sure how. So I agree with you a little bit in principle, but I see an app still as having a number of other responsibilities, even if it is a pretty dumb interface to a rest web service. And that coordination has to happen somewhere. You could push a lot of it out of a ViewModel into a more generic content store, if that is something that truly does apply to the majority of the app, but you still need some sort of coordination to get data from that content store into your view layer.

Soroush Khanlou
Yeah, I think Caching is also something that if you really, really made your models really strictly defined, you could also abstract and genericize that away. Ultimately, I think it's kind of a half baked idea. I think it's ultimately pretty half baked. But I don't know, it's just been bothering me for a long time, I guess. Like people say, I've heard from many people that they don't like to put the JSON parsing logic into their model, like, their entity objects. And it's like, why not? What else do they do? If you really want a single responsibility object, this object's responsibility is to parse JSON, and that's it.

Chris Dzombak
Fair enough. Yeah, I don't think I have anything to add here.

Soroush Khanlou
Those are the biggest questions and things I wanted to talk about with regard to view models.

Chris Dzombak
Okay, cool. Yeah. I had just one thing I wanted to add as follow up to something that I didn't know the answer for offhand in the last episode.

Soroush Khanlou
Oh, nice.

Chris Dzombak
You had asked a question of what would be a more reactive style way of binding user interface actions up into the view model.

Soroush Khanlou
Right, right.

Chris Dzombak
So I did a little bit of digging before this episode, and I remembered that Reactive Cocoa had a pattern for this. I believe it was called commands in reactive. Cocoa One and two. Now, Reactive Cocoa has an action type which represents a way to trigger side effect de work and get some result back. And the Reactive Cocoa framework also provides ways to bind an action to various UI kit UI elements so that your view model may expose several may expose one or more actions as part of its interface, which, when you assign a view model to a view controller. The view controller can then bind those actions to its UI elements in the same way that the view controller is binding observable outputs from the view model to its UI elements.

Soroush Khanlou
Right, that makes sense.

Chris Dzombak
And I'll add some links to the Reactive Cocoa documentation here and to this type itself in the show notes for those interested.

Soroush Khanlou
That makes a lot of sense. So, basically, when the observable updates on the view model, you can directly bind that to, let's say, UI label text or whatever. And when a button is tapped in the UI, you can also directly bind that to some kind of, like, thing that accepts inputs on the view model, which would be the same as defining a target action and then calling a method on the view model. Right, yeah, that makes a lot of sense. Yeah, it seems like something like that should exist, and I'm glad to know.

Chris Dzombak
That, as it turns out. It does.

Soroush Khanlou
Yeah. That's really good. Okay, cool. Very interesting.

Chris Dzombak
Well, I think we're running a little long on this episode.

Soroush Khanlou
I think that's right.

Chris Dzombak
Unless you had anything else you want to add.

Soroush Khanlou
No, that's everything for me.

Chris Dzombak
Cool.

Soroush Khanlou
As always. Thanks for listening. This has been episode three of Fatal Error. I'm Siresh Khanlou.

Chris Dzombak
I'm Chris De Zomback. You can find us at Fatal Error dot FM or at Fatal Error FM on Twitter, and please send us feedback, and we will talk to you in two weeks.

