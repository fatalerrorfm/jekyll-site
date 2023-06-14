Chris Dzombak
Welcome, everybody, to Fatal Error. I'm Chris De Zomback.

Soroush Khanlou
And I'm Serge Kalu.

Chris Dzombak
And this week we are going to talk about the kerfuffle around file private in the Swift Evolution ecosystem right now.

Soroush Khanlou
And we haven't done a good Swift Evolution episode yet, and I think there's a lot of interesting things to talk about. And I think we're going to start with file private.

Chris Dzombak
Yeah, we're going to gamble that we can talk for half an hour about this before we jump into that. Wanted to thank all of you for supporting us here on Patreon. It really does mean a lot to us. And you are making it possible for us to continue producing this episode, paying the hosting and editing costs.

Soroush Khanlou
Yeah, super. Appreciate it. And with that, let's dive in.

Chris Dzombak
So Swift Evolution proposal 0159 is under review as we record this, and by the time this episode goes out, the review period will have ended. But the proposal is pretty straightforward. It proposes simply to basically get rid of the file private keyword, which was introduced as part of Swift Three, and to give the private keyword the same behavior that it had in Swift Two and the same behavior that file private provides now.

Soroush Khanlou
Right. So this completely reverts the other one, which was 25 scoped access level.

Chris Dzombak
I don't think it completely reverts it. This really sort of laid out the rules for public and internal. Although I guess those were around already, weren't they?

Soroush Khanlou
Yeah, those were around already.

Chris Dzombak
All right.

Soroush Khanlou
Before basically in Swift Two, we had public, private, and internal and no protected.

Chris Dzombak
Yeah. Okay, so right, then this completely reverts proposal 25.

Soroush Khanlou
Right. And I haven't read the proposal super in depth, but does it do anything other than revert it?

Chris Dzombak
That's the only thing it does.

Soroush Khanlou
That seems good to me then.

Chris Dzombak
So let me ask a question that I think is really what we're sort of getting at here. Is file based privacy, file based access control actually a useful or meaningful thing? Or should the language provide some other way to share code, to share sort of private implementation details between I think the most common use case is probably between extensions that are declared in the same file.

Soroush Khanlou
Right, right. I think Swift could stand to have good modules or namespacing. Ruby system for that is basically pretty good. Maybe the file is the wrong sort of metaphor for how we want to break up our code. But on the other hand, like, the file is what we have. Nobody is suggesting a radically new system where everything is in one file and you kind of look at different views of the same file or like I don't really see swift is a compiled language of text. Like, it's never going to be a block space graphical programming language. I don't think it's possible. This is how it is. There's no way to make a semantic editor for Swift. And we have files today so I appreciate this line of thinking, but I'm not sure that it's right.

Chris Dzombak
This is something that I don't know if I have a strong opinion on yet, but someone I think zach, how do you zach Dreyer.

Soroush Khanlou
Yeah.

Chris Dzombak
Tweeted or posted somewhere that thinking of a file when you're thinking about code is not really a useful abstraction in the way that other lexical scopes are useful abstractions.

Soroush Khanlou
Right, right.

Chris Dzombak
So I guess I think that the whole, like, the file private is clumsy, but I think that there should be room somewhere for declaring this really, truly is an implementation detail that no one outside this extension should be able to access. And I think that tying that to just sort of this accidental fact that our code lives in separate files, it feels wrong to me.

Soroush Khanlou
Yeah, I feel that line of argument, I really do. Maybe there's a different way to do the whole thing from the top down, where you say the big thing that people like when they make a different extension for every protocol is they basically want to be able to separate out the core of the thing from the performance to sequence or whatever.

Chris Dzombak
Right.

Soroush Khanlou
And maybe there's a way to write a different kind of code in the thing and just say this is a marker, a separate I know we have mark, which is fine, but something that actually compiles. And you say this is where this protocol conformance begins. You write just like in ruby, you can write private, and everything below that in your type is going to be private. In the same way you'd write like conform sequence and then everything before after that is like, for conformance to sequence. Yeah, maybe that would be like a.

Chris Dzombak
Better I mean, maybe this is kind of what I'm getting at is that I haven't thought about this for too long, but it still feels like this proposal doesn't quite get it right either to me, because we still have basically file private. There's just no way to really segment off some implementation detail that it really is truly private API that only this one extension, this one little bit of behavior for your class has access to.

Soroush Khanlou
Right? Yeah. I don't know. I think one thing that I think kind of goes unsaid is I think a surprisingly large portion of the pushback is just because file private is such an ugly bit of code. It's like these two words don't really make sense together. There's no underscore separating them. It's just ugly because it doesn't have that elegance. And I think a lot of people, definitely me, I react and I see that. I'm just like, I don't want to write this in my code.

Chris Dzombak
Yeah, I totally get that. Do you think that's the reason for the bulk of the pushback against it?

Soroush Khanlou
Bulk is hard to say. I wouldn't be surprised if it was like 30%, it might be 60% to me. I would be careful saying this is like 30% of the pushback is like this is a really ugly identifier.

Chris Dzombak
Yeah.

Soroush Khanlou
I mean even super private I would like more like if you had private super private instead of file private and regular private. Yeah. And I also like what are the benefits to declaring something private? Right. Number one is people outside your module can't use them but you get that from internal for free anyway, so that's not a big deal. People inside your module can't access it, but they can change the code and say now I want to use this thing, which I have seen. The other benefit is that when you create generated header it doesn't show up in the generated header. It only doesn't show up in autocomplete. Not that autocomplete is super narrowed down already, but yeah, it doesn't show up in the generated header. And that's the argument I see a lot of in a lot of cases for why you should mark things as private. Which to me in that case it doesn't really matter if it's going to be private or file private. Like the file part of it doesn't matter. It's not that like, well, this extension shouldn't be able to see it because when you generate the header you're generating it for the whole file. On that level, I think it's basically fine.

Chris Dzombak
Yeah. This really is my problem with this proposal. Like okay, file private is clumsy, it is a long name. It uses files as if they have some sort of semantic meaning, encodes them.

Soroush Khanlou
Into language in a way that is so weird. Yeah.

Chris Dzombak
So this proposal says in Swift four mode, the compiler will revert the semantics of the private access level to be file based. This still comes with a lot of the same problems.

Soroush Khanlou
It's still there just hiding this solves.

Chris Dzombak
The ugliness of the modifier, but it doesn't solve the thing that really feels wrong to me.

Soroush Khanlou
Yeah.

Chris Dzombak
So if we threw out both private and file private, can we come up with something that lets you declare that something is available everywhere in this type versus just within this lexical scope? Well, that's not exactly what we already have because either of the options for what we have now will rely on files. Is there something that we can do that limits that takes files out of the equation that is playing just with the lexical scope where something that you want to be truly private is declared.

Soroush Khanlou
So we just have true private and just say, sorry, you just can't do extensions that touch private things, it's just not allowed anymore. That'd be a solution. Wouldn't bother me.

Chris Dzombak
That actually seems.

Soroush Khanlou
Instead of reverting to the old behavior, you just remove the file private accessor entirely and leave private the way it is.

Chris Dzombak
I thinking just off the top of my head, I think that would rush up against the way that we're using extensions in some cases. In my current app.

Soroush Khanlou
Right.

Chris Dzombak
And maybe this is part of the problem is that extensions are used for so many different use cases in the same way.

Soroush Khanlou
I think we're going to have to touch on modules in a little bit, but in the same way that people use enums as namespaces, I think people use extensions as code separators and that's not really what they're for.

Chris Dzombak
Yeah.

Soroush Khanlou
That makes me feel uncomfortable. More so than maybe that's just wrong.

Chris Dzombak
I mean, if you're extending something within the same module, like maybe you should just be using internal API.

Soroush Khanlou
Maybe file private should just go in private, should be truly private.

Chris Dzombak
Yeah, this feels really good to me right now. I haven't really thought about it, but that makes sense.

Soroush Khanlou
There's this thing you can do. So have you ever wrote an iterator?

Chris Dzombak
No, not in swift.

Soroush Khanlou
Okay. So if you write an Iterator, usually you make a type and it has properties it holds onto and then it has usually one function, maybe helper functions, whatever. But you can also do this thing where you can use any Iterator, which is a special type that takes a block and inside that block you can declare local properties because you're just in a function and then whatever you return is the returning result of the thing. And because of the way the blocks work, those references are held on too tightly and then the block can continue to work with them and there's a really nice parallel between them. So anything you declare as a local property in an Eddy Iterator block is the same as like a type property if you create your own class. Right.

Chris Dzombak
Okay.

Soroush Khanlou
It kind of has this really nice elegant balance if you think about that. There's no way to make those properties public. They're just in that scope and they're never leaving.

Chris Dzombak
Right.

Soroush Khanlou
And that's kind of nice. It's kind of nice to just say that's it it's never leaving. It it's never coming out of here.

Chris Dzombak
Yeah. Is it too late in the Swift language to have a change? So like as big as getting rid of file private and leaving private as like private to this lexical scope.

Soroush Khanlou
Right. I don't think it's too late. I just don't think they want to deal with the pain of it.

Chris Dzombak
That's going to be a pretty breaking.

Soroush Khanlou
Change because tons of people use extensions to mark breaks in code.

Chris Dzombak
I think that the more that I think about it, that really feels wrong to me.

Soroush Khanlou
Yeah. I don't really like it. I do it sometimes just to have one part of the code I can focus on, like just kind of a scope for myself, but I really don't like it.

Chris Dzombak
Yeah, that seems really like an anti pattern.

Soroush Khanlou
Yeah.

Chris Dzombak
Just think about it.

Soroush Khanlou
Think about it. Using the extensions to conform to protocols is an anti pattern.

Chris Dzombak
Well, maybe not necessarily even to conform to protocols. I mean, maybe you're adding the protocol conformance somewhere, like somewhere else in the code or in another module, in which case you're just using internal API anyway. And I find it hard to believe that in that case you should be calling into private API, even if you're doing it within the same module. In a lot of cases, yeah.

Soroush Khanlou
A very common one for this is basically I have a type that has an array, and I want that thing to act as, like, some kind of collection, random Access Collection, whatever. So what I'll do is I'll have that property, and then in an extension, I'll declare the conformance to Random Access Property or a Random Access Collection, start index, end index, all the stuff I need to give it. Great. For that. Your main type declaration is pretty short. You're really just saying, like, here's the array that I have. That's it. We usually mark that as private now file private, and then you'll put the rest of it in an extension. So what would you do in that case? You just put everything in one big declaration because you don't want that array that subarray to be public or even internal.

Chris Dzombak
Yeah, that's true. I guess you do need some way, at least in some cases, to share some sort of implementation detail between extensions. But I don't think that I don't.

Soroush Khanlou
Actually think you do. I think it's fine to not just to say if you need the internal, like, the internal details to this file, which would be private, not internal for some reason, you have to be in there. You got to be in there. That's how it works.

Chris Dzombak
Yeah, I guess I could see that.

Soroush Khanlou
Yeah.

Chris Dzombak
That would not be a popular change.

Soroush Khanlou
No, it wouldn't.

Chris Dzombak
People love their extensions.

Soroush Khanlou
Yeah.

Chris Dzombak
And I think that would be one of the big effects of this change would be to make extensions far less common, at least within the same within the same module, if we did the.

Soroush Khanlou
Way that you and I proposed. Yeah.

Chris Dzombak
So while we're talking about this, we should probably mention some other access control features that other languages have that are not in Swift for one reason or another.

Soroush Khanlou
Right.

Chris Dzombak
And so a common one that Swift is intentionally not bringing over would be the concept of something protected.

Soroush Khanlou
Right. So what is protected?

Chris Dzombak
So protected means that it can be accessed only by your class and by subclasses of your class. And that's distinct from private, because something that's private couldn't be called by subclasses.

Soroush Khanlou
Right.

Chris Dzombak
And this is something that I know you've said before we started recording that Swift has a bright line rule that we're not doing that. Do you know what the rationale for that is?

Soroush Khanlou
Yeah. So when Swift came out, they didn't even have access control until, I think, 1.1 or 1.2, and they added it. And I was kind of surprised because I was like, okay, public, private, internal. That seems really limited. Like, what about other ones. What about protection? What about different stuff? Now, today we have open public private file private and internal, which is five, which now, having played with public private, internal feels way too many and it's kind of weird out. But the rationale that they gave and maybe we can do this up for show notes, if I remember right, is basically like if your subclass is using a thing, it's an anti pattern to give it access to things from the superclass that aren't public. And we don't want to support that and we don't think it's right. And we basically want to help you avoid having the subcrossings at all where possible. So we're just going to not have that feature. You can't remove subcrossing entirely the way that Go did, because UI kit depends on it. You can't do there's actually a lot you can do with UIP controller before you subclass. You can add sub views and child.

Chris Dzombak
View controllers, but you can use Composition.

Soroush Khanlou
Yeah, you can do a lot of pretty crazy things, but you couldn't add any behavior to it. So there's a lot of stuff you just can't do without subcrossing with UI kit, and so it's just necessary. It's how you're supposed to operate with the thing. So since they can't remove it, I think they did the next thing and said, we're going to support it, but we're not going to let you just go crazy with it. So they removed the protective thing and I thought that was kind of a strong decision at the time, but now in retrospect, it was definitely the right decision.

Chris Dzombak
I think that makes sense. Helps avoid several just very fragile patterns that otherwise would commonly come up, especially.

Soroush Khanlou
With protocols being the way they are and having the ability to add functions to protocols, default implementations. You just don't need to subclass that much in Swift.

Chris Dzombak
Yeah, that's absolutely true.

Soroush Khanlou
Yeah.

Chris Dzombak
So one other thing that another language has that sort of plays into this would be C plus plus, where you can designate things as private and then use a friend declaration to declare that certain other classes or functions or types in general can access your private members.

Soroush Khanlou
So I don't know anything about C or C plus plus. So how does the friend thing work?

Chris Dzombak
So if you're writing a class in C plus plus, and it's been a while since I've written C plus plus too, but I think I'll get this mostly correct. If you're writing a class in C plus plus US, you can have private members, private functions, private instance variables, right? And then if you have another class that you're writing, probably as part of the same module, and you want that class to be able to collaborate very closely with the class that you're writing, you can declare in that first class that has the private thing you want to share, that this other class is a friend. And then that class will be able to access. The first class is private members.

Soroush Khanlou
Got you. So is it all private members or is it just the ones that you declare, hey, it's friends can access this, or like, this friend can access this one and this friend can access this one and that's it? Or do you just say, this is my friend, feel free to just mess with me internally, do whatever you want.

Chris Dzombak
I don't think that you can get too specific and say like, this friend has access to this member, this other friend has access to this other member. I think it's just like if you declare someone's your friend, then it can access any of your private gotcha.

Soroush Khanlou
What do you think of this as a feature? Do you think Swift should add it?

Chris Dzombak
I don't think Swift should add it. This seems like another pattern that it probably solves some problem in C plus plus and I don't know offhand what that problem is, but it feels like something that will also lead to some fairly fragile relationships.

Soroush Khanlou
Yeah, it seems like an anti pattern to me too.

Chris Dzombak
Yeah. If your friend is located in the same file, this is kind of like file private, isn't it?

Soroush Khanlou
Yes, but you have to be explicit about which friend it is. You have to say, I'm a node and this is the node visitor, and the node says, you can access my guts as a node visitor.

Chris Dzombak
Yeah, in that way, I guess this does feel slightly like file private, right?

Soroush Khanlou
Yeah, but it's so much more like you can just do really weird stuff. I don't know, I feel like you could write some really bad code with it.

Chris Dzombak
Oh, absolutely.

Soroush Khanlou
I mean, it's a CBOX plus you can write a lot of really bad.

Chris Dzombak
Code, but generally speaking, you can. You have a lot of rope to hang yourself with. Yeah.

Soroush Khanlou
Although if you're hanging yourself, a lot of rope is good. So truly, what does that phrase even mean? I would prefer to have more rather.

Chris Dzombak
Than less, I guess. But that's usually not your goal.

Soroush Khanlou
Yeah, that's true.

Chris Dzombak
So that's one other thing to consider, but that's another thing that I would not expect Swift to add at any time in the near future.

Soroush Khanlou
I don't think I'd want it either.

Chris Dzombak
No, I haven't written any C plus plus in years. This probably solves some problem in C plus plus.

Soroush Khanlou
Something they wanted the center library to be able to do or whatever.

Chris Dzombak
Yeah, I guess you assume that if you're writing a class and declaring that something else is your friend, you're also writing that friend. So you know what invariance should be held and you can still know what contract should be provided. But still weird.

Soroush Khanlou
Yeah, very weird. So I want to jump back to one thing that is common, or I don't know if it's common, but something you definitely can do in Swift. I do it. I know a couple of other people who do it. I think it's really useful. They call it a degenerate type or degenerate enum, which is an enum with no cases. And what that means is that if you have that, your enum cannot be instantiated in any way. And if you create an enum like that, you can add static members to it and the enum acts as a namespace for those static members.

Chris Dzombak
Right.

Soroush Khanlou
So if you have some global free function you want to add somewhere but you don't want to pollute the global namespace, you can kind of nest it inside one of these namespaces. I like this, for example. If I have something, I do want to make a singleton for whatever reason, I will basically make the class and I'll make it be its own thing. It's freestanding. You can essentially as many as you want. You can set up the internal details, how you need to it's testable. And then when it's time to share it, what I'll do is I'll make a shared X. Like if the thing is X, I'll make a shared X enum no cases, and I'll put like static. And then I'll name it like main or primary or whatever the specific names are that I need. And then I'll set up the singleton there. So when you want to access the singleton, you go through some other type entirely.

Chris Dzombak
Okay, so the traditional singleton pattern would be that the class just has a shared instance static property.

Soroush Khanlou
Exactly. And then you also might make the initializer private.

Chris Dzombak
Right. So this approach means that that static property doesn't exist on the class that you're using as a singleton.

Soroush Khanlou
Right.

Chris Dzombak
And that encourages you to use best practices in designing that class.

Soroush Khanlou
Yeah, exactly. So you make a class that's just a class, and then you say, well, I'm going to want global access to this thing. So here's how you globally access.

Chris Dzombak
Interesting.

Soroush Khanlou
Yeah, I think that's a nice pattern. There's a couple of other people and a couple of other cases that you can use it in. It's pretty useful, but you're kind of hacking into the enum thing just to make this namespace for you.

Chris Dzombak
Oh yeah, it's a total hack. You're using an enum with no cases just because you can't accidentally instantiate it. And you want to have a dumping ground for a collection of related static stuff.

Soroush Khanlou
Right, exactly. And so it's a bit of a hack, but I still do like it. But one of the things I think Jared Sinclair wrote about this maybe a couple of weeks ago, and he does the same thing, but he wants just the dedicated word, a dedicated keyword in the language for this. So scope or namespace or module. Module would be overloaded if we use module, but something like that. And the idea there would be that you basically can set up this sort of namespace. You can put types in there, you can put functions in there whatever you want. And it really has its own namespace, which would be really nice. A lot of times I find myself writing code where there are like everything has the same prefix, like authentication coordinator, authentication data, authentication gateway, like all these things that I need that I want to be separate. But I also don't want to have to type to our authentication every time. And when I'm inside there, I want to just be able to say like, this is just a view controller or.

Chris Dzombak
Whatever and so what's the motivation to add a language feature like this rather than putting all of that stuff in, say, an authentication module?

Soroush Khanlou
I don't like Swift modules is my feeling on this. Basically I've heard it set up, it's really confusing what optimizations you're going to get and I've heard if you have too many, your app starts to take too long to launch. Weird stuff like that. It just seems like not that good and I also might want to nest them and it's nice to be able to just say here's a keyword, here's a brace and now I'm in the module instead of okay, now go to the file menu and create a new module and set up the compilation parameters for it. I don't know about any of that stuff, I just want to be able.

Chris Dzombak
To make my module or make your namespace.

Soroush Khanlou
Make my namespace, truly?

Chris Dzombak
Yeah, I'll give you that. Modules definitely are not trivial to set up. It's a very heavyweight solution, particularly if you just want to set a few constants out somewhere.

Soroush Khanlou
And Ruby does this all the time if you have the module thing, which is actually overloaded, but if you use a module in Ruby you can say my module is active record and my class inside there's base. So when you want to refer to it active record base, instantiate that and you're off to the races.

Chris Dzombak
C plus plus has namespaces that achieve more or less the same thing.

Soroush Khanlou
Yeah, it's a useful feature and I feel like that would also play into the access control stuff as well if we did have a feature like that. So you could say like in my dream world, and I know this may be too highfalutin or whatever, but in my dream world you'd be able to say here's a module, here's a module inside that module and then here's what that module exports kind of in the same way that we do in JavaScript. You're saying this is what I export and you call public or whatever. So you would say this is public, this is public and all that does is it goes up one level to the next.

Chris Dzombak
Oh, that's interesting.

Soroush Khanlou
And then from that, if you do want that to be exposed externally, you say that's also public from this level and it goes up one more level and then it would play really nicely. With modules. You would basically just need one keyword, which is just like, make this public and maybe you maybe want private. I don't know, that's up to you. But you basically just need one keyword. You say, publish this, publish this, and then as you go out the levels, you just keep publishing the stuff that you want to export.

Chris Dzombak
I could see that sort of recursion being a little bit complicated and a little bit hard for people to get used to. And that feels like something the Swift team might object to.

Soroush Khanlou
Yeah, and it's also just like a lot of I don't want to export things over and over again.

Chris Dzombak
Well, right. So let me propose a less foreign idea that builds on what we've been discussing this entire episode. We introduced a sort of namespace operator that provides namespaces, or what you've been calling modules, right. Without the overhead of creating a whole separate Swift module, without the dynamic linking performance penalty that we get on iOS. When you have a lot of frameworks linked into your app. And we still have five access level modifiers. We have open, we have public, we have internal, and internal is still a module level declaration at this point, right? We have namespace, private. And we have private.

Soroush Khanlou
Interesting.

Chris Dzombak
So namespace private, basically replaces file private. It gets rid of files as a somehow meaningful abstraction.

Soroush Khanlou
So you'd have to basically say, I'm this API, API error collection. I have an array of errors and I want to conform to collection that goes inside its own namespace. You can have as many extensions in there as you want. Everything in there is Namespace Private you would basically get access to in the whole namespace.

Chris Dzombak
Right. And then the last declaration would be Private, which would keep the same meaning. It hasn't Swift three, which is private to this lexical scope.

Soroush Khanlou
Right. Okay. That doesn't solve the problem of it being kind of unwieldy.

Chris Dzombak
Right.

Soroush Khanlou
But it does solve the problem of having to care about files as like any kind of meaningful abstraction for anything.

Chris Dzombak
You could come up with a better name, I think, or a better modifier to write something like, I don't know, space NS Private. It definitely feels because it still feels to me like the private versus file private distinction is useful and that any sort of file private access level, whether it's called file private or something else, is wrong.

Soroush Khanlou
Right.

Chris Dzombak
Maybe what we've landed on is introducing namespaces, which are a seemingly unrelated feature, but one that we want and then using them instead of files for access.

Soroush Khanlou
Control, meaning I like that. How do you refer to the types inside the namespace? Different namespace? Type?

Chris Dzombak
Yeah. I assume that if you're within that namespace, maybe you can just use the type name that might come with some complexity around resolving collisions.

Soroush Khanlou
Right. No, I mean, it works today. Like if you do enums, you have nested enums, and then you're going to have types inside there and. It kind of figures it out. And if it doesn't figure it out, then you can be explicit about which one you mean.

Chris Dzombak
And I mean, you expect it to work sanelly and safely with module. Right.

Soroush Khanlou
Right.

Chris Dzombak
So whatever problems we've solved for modules and whatever else, let's just use the same solution.

Soroush Khanlou
Yeah, that's an interesting solution, too. There's options.

Chris Dzombak
There are, yeah.

Soroush Khanlou
I feel like maybe first step, revert, go back to the thing that we.

Chris Dzombak
Actually like, but it's still wrong and.

Soroush Khanlou
I don't quite but it's still wrong.

Chris Dzombak
And I don't quite like it.

Soroush Khanlou
Yeah. No, I feel you. It is wrong.

Chris Dzombak
It's maybe less ugly, but it's still wrong.

Soroush Khanlou
Yeah, that seems right. So in your code, do you use private versus file private? How do you oh, yeah, definitely.

Chris Dzombak
So, first of all, we have a few different modules in our application. So especially in the frameworks that get linked into the application, we use the proper access level specifiers, and if I'm writing code, I default to writing something as private. And then once it becomes clear that, oh, I actually want to share this, that's a sign that I should really take a look at what the API I've written does. Consider in a little bit more detail how it should be shared and if it should be shared, figure out what invariance and guarantees need to be made to actually share that. Right. I mean, changing that access level to be a little bit more liberal does mean that you should be a little bit more careful about what things like invariance and guarantees that that API provides. And I worry that maybe this proposal reverting file private and just using private for everything will cause us to be a little bit less careful.

Soroush Khanlou
Yeah, that makes sense. Yeah. And once things are back to the old way, I don't think anybody's going to feel any pain. And if you don't feel pain, you're not going to fix it.

Chris Dzombak
Right. I think that we're going to be stuck with files as an accidentally meaningful scope in Swift for basically forever at this point.

Soroush Khanlou
It could be worse in Java, I think the folder that you're in defines the module name. Well, you do like folder name, folder name, folder name file?

Chris Dzombak
I mean, that's at least I don't mind that, actually.

Soroush Khanlou
Yeah.

Chris Dzombak
So your file system on disk reflects the architecture of how things are split up in your application. I'm cool with that.

Soroush Khanlou
Yeah. Again, I feel like that's the same deal as relying on files as an abstraction for breaking up code.

Chris Dzombak
You're not relying on files as an abstraction for breaking up code, though. You're relying on the directory structure as an abstraction for structuring relationships between parts of the application.

Soroush Khanlou
Right. But it's clearly not necessary because in modern projects, you put everything in a folder and organize in an Xcode. The organization is just for the user, like it might be in two different folders or two different groups in the Xcode project, but it just represents one file on the disk.

Chris Dzombak
Yeah, well, I mean, we still end up with the same thing in Xcode. You have multiple projects split up for different modules. You're just taking the same organizational work and putting it into one tool as opposed to another.

Soroush Khanlou
Right. So interesting. So where do we land on the file private thing?

Chris Dzombak
Yeah, I mean, I described earlier where I've landed. You know where I've landed. File private is ugly and wrong. Reverting it and using private to mean file private is not ugly, but still wrong. And we need namespaces and some sort of not ugly namespace.

Soroush Khanlou
Private access, some way to group types and scopes that isn't a file.

Chris Dzombak
Yeah. Files as an abstraction for organizing access to code is just wrong.

Soroush Khanlou
Yeah.

Chris Dzombak
Thank you all very much for listening to Fatal Error. I don't really know where to go from here.

Soroush Khanlou
Yeah, we did it. We did 30 minutes on file private.

Chris Dzombak
Yeah. We did more than 30 minutes.

Soroush Khanlou
Did we?

Chris Dzombak
Yes.

Soroush Khanlou
Nice. Yeah. Thanks to the listeners. Thanks to the patriot. Is this patreon? Patreon, yeah. Thanks to the Patreon people. We love you. You mean a lot to us.

Chris Dzombak
Absolutely.

Soroush Khanlou
Yeah.

Chris Dzombak
And we will talk to you next week.

