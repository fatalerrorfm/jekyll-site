Soroush Khanlou
Did you hear about E fail?

Chris Dzombak
Yeah, I did hear about that. That is pretty bad. Yeah, that's not good.

Soroush Khanlou
Yeah, I don't really understand the ramifications of it yet, but it sounds bad.

Chris Dzombak
I mean, it seems like I haven't done that much reading on it, but it seems like the implication is someone who, like, has the ability to intercept or modify an encrypted email message can do things to it that cause your email client, when it views that message, to exfiltrate the encrypted content message out to a remote server. Yeah. And it's interesting because it takes advantage of certain email clients not doing exactly the right thing with some headers that PGP adds into messages. Apparently some clients kind of ignore those, which it turns out is bad. It has to do with email clients, like, automatically displaying images, which most clients do. Most people don't turn that off. And it also kind of exploits just the complexity that is mime, like multipart email and the way things get encoded and ordered.

Soroush Khanlou
GPG is like, I don't know which ones. One of them is GPG and one of them is PGP.

Chris Dzombak
Right, yeah. PGP was a, like I think it was a commercial or shareware product a while ago. I don't know if it even still exists, but GPG is the, like, free software implementation.

Soroush Khanlou
But yeah, that shit's like 20 years old, right?

Chris Dzombak
Oh, yeah, definitely.

Soroush Khanlou
We've learned a lot about encryption since then.

Chris Dzombak
We have. Although, for backward compatibility, like if you're designing PGP today or GPG today, there are different modes of encryption that would automatically that would defend against this sort of thing. Right.

Soroush Khanlou
Well, don't spit out the plain text email once you decrypt it. That seems like a good start.

Chris Dzombak
Or don't just load images in encrypted email by default. Right.

Soroush Khanlou
Things like that, which actually that's something I started doing. So that's a setting in mail app, which I do use. If you go to the Preferences and go to Viewing, and then you go to load remote content in messages and uncheck that.

Chris Dzombak
I found out so much.

Soroush Khanlou
When you do that, it's fine, because to me, it prevents recruiters from being able to track if I've opened their email. And there's people who aren't recruiters that are using those tracking chips or tracking pixels, and I, oh yeah, I am not into it. And then I don't need my email client, like, streaming out data about how I use my email and when I check it and stuff. I'm not into it. So you can turn off on both Mac OS and iOS, which I did. I really, really am enjoying it.

Chris Dzombak
Maybe I'll try this again here.

Soroush Khanlou
Every time there's an email with no images in it, and it says, like, oh, not loading images. You're like, I just caught you, I totally got you. You want to do an episode? Yeah, let's do it. E Fail aside, security exploits will continue to come out forever, but this show is coming to an end.

Chris Dzombak
It is, yeah. And we announced this now two episodes ago, right?

Soroush Khanlou
I think so, yeah.

Chris Dzombak
We've gotten a lot of very nice feedback from a lot of people, a lot of listeners. And I just personally want to say, like, thank you for that. It really is just on a personal level, it's like really gratifying to hear so many people are a fan of the show and are sad to see it go. That really means a lot to us.

Soroush Khanlou
It's really easy to forget how many people listen to the show because they don't, like, write us. So we just don't know. We just see RSS subscribers work. Lot number seems high, but it's nice to actually hear from people who are sad about the show ending in kind of a perverse way.

Chris Dzombak
Yeah, it's definitely kind of a weird feeling.

Soroush Khanlou
So this is going to be the last public episode of Fatal Error. There'll be one more patreon only episode.

Chris Dzombak
Is that what we're doing? Okay.

Soroush Khanlou
Yeah. I mean, if it ends up being a very special episode, we can we'll announce on Twitter or whatever.

Chris Dzombak
Yeah, that's true. We'll figure it out.

Soroush Khanlou
But today for our last episode, we wanted to talk about something that is kind of foundational and something that seems simple at first but ends up hiding a ton of interesting complexity and a ton of interesting parts of programming and how programming has evolved over the years. Absolutely. And that is what is sort of casually known as the billion dollar mistake, which is null.

Chris Dzombak
Null. And I want to give another shout out to Swift unwrapped too. I was just listening to a great episode this week about the changes to implicitly unwrapped optional in Swift, and that's a great episode that you should definitely go listen to. And I think it's also worth taking a step back. I know, like, a lot of you are writing Swift with Day In and Day Out, but I think that it may be nice to kind of take a step back and re examine why do we have optionals? What problem do we think they're solving? Right?

Soroush Khanlou
Yeah, I think it's kind of an interesting thing because the show has very much been about Swift in a lot of ways, but I think almost more so than any other feature optionals kind of personify. Swift like more so than generics, more so than protocols, more so than anything else, more so than enums. Even though optionals and enums are very tightly related. Optionals really are Swift to me.

Chris Dzombak
They do. Well, they are. And they are, right. They're swift. They're also, I mean, kind of a significant part of a lot of newer languages. Right. Think about Kotlin likes the sort of Swift counterpart on Android that brings optionals or some sort of option type to the table as well.

Soroush Khanlou
I think it's a hallmark of scala.

Chris Dzombak
Yeah, I think it's a hallmark of just a lot of relatively newer languages that people are starting to use more widely in industry.

Soroush Khanlou
People are talking about these languages more and more these days.

Chris Dzombak
Why is more and more these days? I've been writing Python for like a year now instead of Swift. And I really I still wish I were writing Swift. Yeah.

Soroush Khanlou
Hopefully soon. Hopefully one day.

Chris Dzombak
One day. Swift on the server. Do we dive right in here? Like, what is the problem with null pointers or null references or null in general?

Soroush Khanlou
Basically, if you don't have something that lets you model things as optional and more importantly, as non optional, then every single variable, every single reference in your system ends up being able to be null at any point in time. And there's no way to know before you run the code whether there's a null there or not. You can be pretty sure. You can kind of try to keep track of it in your head, which is how you do it in Python, how you do an Objective C, but you don't really know that there's never going to be a null there.

Chris Dzombak
Right. There's no way for the compiler or the type checker to look at the code and say, yes, this is not going to be null. This is safe to kind of like a little more formally say what Sirush is doing. Well, not even formally. Just restate. Right. Yeah. In a language that has null pointers or null references, then anywhere you have any variable, any instance that you think is some type, let's say, is an integer, it's actually like that type or null. It's an integer or null, really. To be completely safe, anywhere you use any reference to an object, you have to check whether it's null or make sure that whatever API you're using with can accept the null values. And I mean, if you think about it, most of what your program does is deal with references to things. And that's kind of a whole lot of if you're going to really do things very safely, that's a whole lot of busy work to do as a programmer. And humans are bad at busy work and it's a lot to keep track of. And so there will be mistakes or you'll take shortcuts because this thing should never be null, even though maybe it can be null in this Edge case and the compiler, your type checker can't help you, your tools can't help you find that case.

Soroush Khanlou
Yeah. And I think one other important part of this is like, there's no way to opt out of the nulls. They are what they are. They're always going to be there and there's no way to get around it. Yeah. And I think that's part of the perniciousness of nulls is just you have to deal with it. There's no other way to do it except just to keep track of everything in your head. Remember which APIs are allowed to accept null and which are not. And it just ends up being pretty painful, I think.

Chris Dzombak
Yeah, absolutely.

Soroush Khanlou
I remember the objective C days. Objective C is a little bit more forgiving than a language like Ruby or Java because if you try to do something with nil, namely if you try to call a message on nil, it will work silently. Or I think Chris would say that it would fail silently.

Chris Dzombak
It'll do something silently. I guess it'll return nil or zero or a false value silently, which in a lot of cases may be correct and maybe sometimes isn't, it ends up being correct.

Soroush Khanlou
Like, I want to say like an 85% or 90% of cases, which is what's so pleasant about it. Right, but then in those cases where.

Chris Dzombak
It'S not, you get just some really obscure bugs where and it ends up.

Soroush Khanlou
Happening way down the line.

Chris Dzombak
Yeah, it's not obvious what's going on.

Soroush Khanlou
Right. Whereas in Ruby and Java, they blow up immediately with the so called null pointer exception. And I mean, they blow up immediately when you try to dereference a null pointer in like C and C plus plus and stuff.

Chris Dzombak
Right, right.

Soroush Khanlou
C has pointers.

Chris Dzombak
Right? Yeah.

Soroush Khanlou
I don't know anything about C. That's fine.

Chris Dzombak
It is pointers and any of them can be null.

Soroush Khanlou
Yes. So one thing that I think of is actually super interesting about this. I think if you've been writing Swift for a while, you're deep in the optional world, you're learning all the strategies to deal with them. But there's all these interesting little theories and all these interesting little things around it that I think are super worthwhile to talk about. So one example is we're talking about, let's say Ruby's null, where you send it a message and it blows up and you're talking about objective C null, where you send it a message and it returns to you another value. If you think about it, that's kind of like a type that accepts all messages and a type that accepts no messages. Are you with me so far?

Chris Dzombak
Yeah, definitely.

Soroush Khanlou
So a type that accepts no messages can never take the place of any.

Chris Dzombak
Other object, any other object that it does accept any messages. Yeah.

Soroush Khanlou
Let's say you have a number type and you have an add one message that you can send to it. If there's nil in that spot and you try to send the add one method or message, it will blow up immediately. Which means it does not act like.

Chris Dzombak
That object nil does not have like an is a relationship to that object. It is supposed to be acting as.

Soroush Khanlou
Yeah, but I'm assuming that yeah, but I'm even making kind of a broader claim which is like what messages does it accept? And then when you flip it and you look at objective C's, weird nil, where it just accepts everything and just returns nil it in some way since it accepts every message in some way. It acts as a super type for every object because whatever message you send it, it's going to respond to that message. It's always going to respond in a way that you want it to, but it's going to respond with something.

Chris Dzombak
Does that make it a super type for any other type or a subtype for any other type?

Soroush Khanlou
I can't remember. It's a covariance and contravariance and bivariance.

Chris Dzombak
Your point is that you can substitute Nil for any other type, right?

Soroush Khanlou
Yeah, essentially yes, that is what I'm saying. And again, it's not always going to respond correctly, but it is going to respond. And I think that that interplays with the listkov substitution principle where a type is a subtype. Yeah, you're right. It's subtype relationship. A type is a subtype of another type. If you can send the subtype in place of the supertype and things will work. It's not perfect because things don't always work because the responses that you get break a lot of contracts that List Gov expects you to keep in place. But in a very weird way, nil acts as the subtype for every single sort of object that you can have.

Chris Dzombak
In your system in objective C. In objective only. Yeah. I would push back a little bit and say if returning Nil for some things violates an API contract then you're still violating the list gov substitution principle. Right?

Soroush Khanlou
Yeah, you are. You definitely are. But I think it's weird in that way and I think that's part of the reason that it is a little bit more pleasant to work with until you run into one of those kind of hard to debug bugs because it's.

Chris Dzombak
At least closer to following the list gov substitution principle.

Soroush Khanlou
Yeah. Following some kind of type system. Whereas if it's like if it's Java style, if you sort of convert that into the objective C world sorry, if you convert that to the swift world, you basically have your object plus one more enum case. And that enum case looks like it will accept messages, but in fact it just blows up every time you try to touch it.

Chris Dzombak
Yeah.

Soroush Khanlou
So I think that's really weird and interesting and I don't know, I think no is such a unique beast in our programming world because it causes so many problems. Like the inventor of it called it literally he called a billion dollar mistake. And I kind of wouldn't be surprised if it had caused more than a billion dollars of damage.

Chris Dzombak
Oh, I'm sure think about, I think this talk. So in our show notes, we've linked to a talk by Tony Whore and it's entitled no References the Billion Dollar Mistake. And this is kind of a classic, classic talk which I encourage you to watch when you have time. But going back to I think 1964 when this concept was first introduced, we're talking about 50 years of null pointers being around and that certainly has caused many billions of dollars of damage. When you think about all the different ways that null pointer dereferences in C in particular have caused so many security problems.

Soroush Khanlou
Yeah. I mean, think about all the times null has kind of bitten you as one programmer and then right, setting aside just a million other programmers well, and.

Chris Dzombak
Setting aside just even like productivity and debugging losses to things being null when you didn't expect them to. And there are just so many real world implications of security problems that have real world consequences. Right?

Soroush Khanlou
Yeah, for sure. Well, and that's one of those things that I always bring up on the show that I always find so fascinating about Swift is if you do Swift by the book, even for a reasonably complex app, you could just have zero crashes.

Chris Dzombak
You can yeah. You may have other functional bugs. Right?

Soroush Khanlou
Yeah, you have bugs, no doubt. But your crash lyrics will just be 99.9% crash for users.

Chris Dzombak
Right. And that's because mostly because of this that in large part because of this. Right. There are other sort of corner cases you have to be aware of with objective C right. That Swift also takes care of. But this is a huge part of it.

Soroush Khanlou
No, there's some ways for Swift to crash, but they just start to go away once you start dealing with null in sensible ways.

Chris Dzombak
Right. And that's because going back to what I was saying earlier, having the option type in Swift takes away this implicit fact about all the types, all the references in your program, that it is like your type or null, and the option type makes that explicit. And for things that can't be null, you don't use an option type. And for things that can, this lets your compiler, this lets your type checker provide help you and tell you, hey, this type is actually Foo controller or nil. It's not just a Foo controller.

Soroush Khanlou
And we talked, I think it was two, three weeks ago, we talked about you have been writing so much Python and there are things that you think are type int, but they're actually type int or null.

Chris Dzombak
Yes. In fact, everything I think is an int is an int or null.

Soroush Khanlou
Right.

Chris Dzombak
Which is annoying. And I don't check that for every time I have something that I think is an int, because that would just be the 80% of the code that I wrote. And so every once in a while there's like something 500 in in production because there's a none somewhere that that I wasn't expecting.

Soroush Khanlou
Yeah. Have you ever have you played with any of the python typing, progressive typing stuff?

Chris Dzombak
I would like to. However, mostly that is for Python three, and we're using Python 2.7 because we're on legacy or the older version of Google app engine, which doesn't support Python Three. Eventually we'll move to Python Three and we'll use the like pep 44 type annotations and at least have we can opt into these type hints and have our tooling check. It IntelliJ. The ID that I've been using for Python that I've talked about, can totally use those. Like Python Three pep 44 Annotations And as we move into the future here, I would love to start using that, but no, I haven't really played with it yet.

Soroush Khanlou
Yeah, hopefully soon.

Chris Dzombak
Hopefully.

Soroush Khanlou
It's really nice when you're able to do some of that stuff. Oh, yeah, it should be sweet. One thing I want to ask you about is when was the first time that you became aware of something that like a maybe type or an option type or an optional type?

Chris Dzombak
That's a great question, boy, because mine.

Soroush Khanlou
Was a very specific moment, a specific blog post that I read. Because before that, you're kind of trapped in the ideology of just being a programmer. You're like, yeah, of course everything should be null.

Chris Dzombak
Everything might be null. There's no way to tell how I.

Soroush Khanlou
Live my life, right? And I read this one blog post and I'll put it in the show notes, and it's called Why Maybe is Better Than Null. And I think I just found out, like, hacker news or something. And I remember specifically being in an airport, and I was just, like, browsing. I was really bored. I found this article and I was like, Holy crap, this is crazy. And I think back at that time, this was 2013, swift hadn't come out yet. I think the only language that I would have really known about, like, Maybe Scala, but I think it was mostly Haskell that was doing this kind of thing. There are other languages that support it too, but those are the ones that were kind of in my sort of.

Chris Dzombak
Periphery sort of circles. Yeah.

Soroush Khanlou
And I was just reading this thing and I was like, wait, you're saying that my references, I can know if they're null or not? How does that even work? Yeah, it's crazy. And so I kind of read through this postings, and the guy explains sort of, now, no references can be null. And then you also need an extra way to handle something that Maybe has a value and Maybe doesn't. He calls that the maybe type. And I knew about generics, and I knew, like, I wanted generics and objective C. And you do use generics for this feature, so you know what's inside the maybe. But sort of seeing this was the thing that maybe realized, like, oh, my God, I absolutely want this as soon as possible.

Chris Dzombak
Yeah. And once you I feel like it's one of those things that once you someone, like, tells you about it or you read about it, in a lot of ways, it is kind of like a light bulb turning on. I think that, you know, thinking back, I think that maybe it was like, early Swift that actually introduced me to this idea. I don't know. May have seen something about it before, but yeah, it was probably when was Swift announced? Was that 2014?

Soroush Khanlou
Summer of 2014?

Chris Dzombak
It was probably summer of 2014.

Soroush Khanlou
Yeah. So I guess this was about a year before that. So not crazy long before that. And in the article he mentions Rust and he mentions Kotlin. Those did exist back then, we just didn't really work with them or know much about them. And Swift was secretly being worked on at that time.

Chris Dzombak
Oh, yeah, definitely.

Soroush Khanlou
Which is cool. And the other nice thing about the post, he has this big frequently asked question section and he basically goes into all these little details of like, oh, here are some cases where no is better than maybe. And he kind of goes through them one by one and says no. You know what, maybe is really important, like this argument. The real problem is people not properly reasoning about their functions. That isn't the fault of null. And it's like, yeah, in some way that's true, but I want tooling to support me, not make me have to think about stuff.

Chris Dzombak
Right. The job of your tooling is to help you focus on the problem that's in your business domain. For lack of a better term, like the problem you're trying to solve, not bookkeeping. You probably write in a language that doesn't force you to deal with pointers and very low level structures all the time. You're probably not writing your applications in assembly code. And yeah, it's because your tooling is here to help you. And so any of this sort of busy work that is not like your problem that you're trying to work on, that's not your business domain, that your tooling can take off your plate, that's a good thing because we like to think that I'm very smart. I can keep everything about this whole system in my head.

Soroush Khanlou
100,000 lines of code, no big deal. I can keep it all.

Chris Dzombak
Humans are bad at that, right? And if you have a tool that can check that entire 100,000 line code base in a few seconds and for all these kind of mistakes, that's just clearly a win.

Soroush Khanlou
Yeah, I think so too. So I kind of want to take it in a slightly different direction and talk about sort of the galaxy brain feeling that working with optionals can start to give you where you're like, oh, I can use an optional here to solve this problem. But then over time you start to realize like an optional isn't actually the right solution here and I can actually go a level up and make something that is even more safe and even better. And so I wrote this post. It was a little while ago, I guess it was last year and it's called that really?

Chris Dzombak
A year ago?

Soroush Khanlou
Yeah, it was called that. One optional property. And this is actually one of my favorite posts I've ever written what I argue there is that sometimes you're working with some code and you're like, you know what, if I just add one more property to this thing, I just make it optional. I just turn it on in some cases and leave it off in other cases. Then this will be perfect and I can solve my bug or I can build my feature or whatever. And the argument that I make in this post is that that is a big flaw in terms of the design of your types, essentially. So what do I mean by that? So the example that I read through in the blog post is imagine you have a view controller where the view controller either is presented normally, or maybe it's presented via a push notification. And so if it's presented via push notification, you want to be able to display that notification message text at the top of the view controller in like its own label. And if it's presented normally, that label should not be there. And this was an actual thing that came up in an actual project that I work on. And we went through it and we slowly worked through. We realized, well, this notification message, it's being represented by an optional string. If the string is there, that means that it was presented by a push notification, and we need to show that label. But if the string is not there, it means it was presented normally, and we don't need to show the label. So now the presence of this string is determining the layout of the view, right? And that's a little bit weird because the string's presence, what does it mean if the string is present or not present? And because optional is so flexible in its use, it doesn't ascribe any semantic meaning to the stuff that you're looking at because it has to work in every situation. So you don't know what nil means. You don't know what none means in this case. And so the solution we ended up coming to is we ended up saying, okay, well, actually, you know what? This view controller, it's not that it has a message that might not be there or not. It's that it has a mode. And that mode might be normal, and that mode might be from push notification. And once you have that extra type in, there a type which has the same shape as an optional, right? It has one case where it has an associated value, and it has another case where it doesn't have an associated value. Once you have that extra type, you can start to do other stuff, like you can add functions to that type where there are certain data that might belong on that type that doesn't belong elsewhere. And so once you start working with optionals, you start to realize that, yeah, they help you model your system better, but there's even better ways than that to model your system. And that's when you hit that true galaxy brain level.

Chris Dzombak
Yeah. So adding like optional properties to kind of sum up, adding optional properties to.

Soroush Khanlou
Your class like a sum type. All right, let's do it.

Chris Dzombak
All right.

Soroush Khanlou
69Th Episode nice.

Chris Dzombak
This is a professional podcast.

Soroush Khanlou
We're professionals.

Chris Dzombak
We are professionals. Adding these optional properties might indicate that your class is taking on additional responsibilities or is like gating behavior or certain behaviors on this piece of data being present or not, which isn't that explicit. Like it's very implicit and like as you add more of those that it's going to be harder and harder to untangle that behavior, right?

Soroush Khanlou
Yeah, absolutely.

Chris Dzombak
So extracting trying to extract things to types that, again, have one clear purpose or using an enum or some type to make those different states, different modes, different behaviors, explicit can be a really powerful approach as well. And that's something that something to keep in mind. Going back to my whole sort of type or null point, is that as you add properties to a class, every time you add a property to the class, you're adding another set of possible states for that class to be in. Right. If you have a structure that has a few, for sake of simplicity, say a few booleans, and you add another boolean, you've multiplied by two the number of states that that structure can be in. And that's something that is is even worse if you're adding optional properties because then, you know, let's say you add an optional boolean, which doesn't make any sense, but now there are like four different states that that property can be in. So you're multiplying the possibly the state space for that structure by four. And this is how complexity grows, right? This is how things get more and more complex. And at least in Swift, we have tooling to help us deal with that. But that's really something to keep in mind.

Soroush Khanlou
So real fast, I want to touch on one thing that you mentioned, which is as you add another boolean, you double the potential state space of your object, right?

Chris Dzombak
Did I get that right?

Soroush Khanlou
You did. No, you nailed it. Okay. There is some really cool stuff out there. There's one particular post I'll put in the show notes called the Algebra of Algebraic data types. And basically this person goes through and he uses Haskell, but all the concepts come across to Swift as well and basically says, okay, well, if you have what they call in Haskell, they call it void. But we call it never in Swift because it's impossible to construct that type. It has zero possible values. And then you have what we call void, what they call unit, which is the empty tuple, which has one possible value. And then you have Boolean, which has two possible values. You have optional, which is however many possible values your original type had, plus one and so on. And you can start to. Think about your types algebraically. There's also the point free boys, they did an episode on this stuff and it's actually super cool. And there's a ton of really interesting analysis that you can do on your types and figure out sort of what your types are representing. And the crucial thing here is that your optional type represents, let's say you have an optional boolean. Like Chris mentioned, it's the two from the boolean plus one more case from the optional, right?

Chris Dzombak
So I guess adding an optional boolean multiplies your state space by three, not by four, but like yeah, exactly. It is strictly worse.

Soroush Khanlou
Yeah, it is strictly worse. And again, maybe there are really three states there, right? Maybe it's like my promises, for example. They're either pending or failed or succeeded. That's three states. You really need to represent three states instead of representing your type as, let's say, this thing, plus one more using the optional type, it might be valuable again to make your own enum and say, you know what? I'm just going to actually make my own enum that has exactly three cases not use optionals at all and take basically those potential values that you had before true, false and nil, and give them real names and give them real values and semantic meaning and all of that.

Chris Dzombak
And then it's explicitly clear what each of those three possible states means rather than having null or two other states.

Soroush Khanlou
And if you realize you need another state, it's much easier to add that extra state because you now have an enum that you control that you can add stuff to, right? Yeah.

Chris Dzombak
I can't keep track of this, but the universe brain here is like, not only are option types great, but when possible, you should think about whether you need an option type or whether you should make a different type that actually represents more closely what you're trying to model.

Soroush Khanlou
Yeah, I think that's right. I think one of the most enlightening things about Swift is if you go back and look at the definition of the optional type, right? It's an enum. That enum has a generic type which is called wrapped, which is the type that it's wrapping. And then there's two cases in enum. One case is called sum and it contains a single wrapped value, and the other case is called none. And once you see that, for lack of a better word, shape. But once you start to see that structure of the optional, you realize, well, if my wrapped is actually an enum with three other cases, then really this whole thing can be represented not as my enum with three cases plus the nun, but as a totally different enum with four cases. At the end of the day, the optional is just another enum and you can kind of take advantage of that to fit your app a little bit better. Whether that's making state machines, whether that's making modes for types to be in, whether that is figuring out a potential set of options that you might likely the user might be choosing, Maybe enums are the true universe brain. Small brain. Small brain is use C and dereference an all pointer. Medium brain is use Ruby and get a null pointer exception, which is functionally the same even though you're not actually dereferencing a pointer.

Chris Dzombak
Is medium brain the objective. C? At least have messaging nil.

Soroush Khanlou
That's the large brain. And then you've got the Galaxy brain is using optional, and then the universe brain is just using them. Man, it's all good.

Chris Dzombak
Just use wait, how many brains are there? I thought there were only four.

Soroush Khanlou
They get really big. There's some with 6715.

Chris Dzombak
Wow, that's a lot of brains.

Soroush Khanlou
Universe brain is a very flexible meme.

Chris Dzombak
It's a malleable.

Soroush Khanlou
You could shape it to exactly what you want, just like an enum. Okay. All right, I figured it out. We're going to put in the show notes. We're going to put a new enum called brains and case. Small case, medium case, large case, galaxy and case universe.

Chris Dzombak
Now, does that have to be I forget where we landed on enums. Does that have to be declared a, like, extensible enum or something?

Soroush Khanlou
Is it a frozen enum or not frozen?

Chris Dzombak
I don't think it's a frozen enum.

Soroush Khanlou
Yeah, you might want to add more later.

Chris Dzombak
Yeah, absolutely. You forgot medium. There we go.

Soroush Khanlou
Yeah, I'm literally typing this in the show notes right now.

Chris Dzombak
Oh, yeah. I'm watching Serish type now. The miracle of real time text editing over the Internet. Which is cool. Think about how this works. Like, we're 500 miles apart. We're, like, talking and writing on the same document. That would be hard to do with paper in person.

Soroush Khanlou
Do you remember Sub Etheredit from back in the day?

Chris Dzombak
I do. Yeah.

Soroush Khanlou
Sub Ether edit was so bomb.

Chris Dzombak
It really was.

Soroush Khanlou
Yeah, I still think about that. Back in those days before Google Docs, it was just like a Mac app and you could just edit the stuff together. It was edit, like code edit, whatever. We didn't use git. We didn't use a stuff. We just use subbedit. It was great.

Chris Dzombak
I don't think I have anything else to say about this.

Soroush Khanlou
Yeah, optionals are really good. Really lean into them. Try not to use exclamation points and force unwrapping and implicitly unwrapped optionals. Try to use the natural facilities. Like iflet guardlet the question mark, question mark operator, all these little tools that Swift gives you. If you really want to get to the advanced level, use map and flat map on your optionals and learn about that. But really lean into the optional stuff because, again, you can make an app that just doesn't crash. And it's incredible.

Chris Dzombak
This stuff seems weird if you're coming to it, but it's here to help you. These tools are here to take a whole lot of busy work off your plate. So you can focus on what's interesting about your problem.

Soroush Khanlou
Absolutely. Thank you so much to everyone who's listened over the past two years.

Chris Dzombak
Yeah.

Soroush Khanlou
Thanks for listening to us drone on about our pet programming topics that we love so much. We really appreciate it. WWDC is coming up. If you see either of us there, definitely say hi. We love you so much.

Chris Dzombak
Yeah, thank you. Everything Sarosh said, I mean, this has been a lot of fun, and yeah, man, I really appreciate all of you who've listened and supported us over the past two years. It really does mean a lot.

Soroush Khanlou
Yeah, I remember we started the stupid podcast. We were just like, maybe we should do a podcast. Ten episodes and see where it goes.

Chris Dzombak
Yeah. Every time we see each other, we end up talking about programming.

Soroush Khanlou
Let's just record it.

Chris Dzombak
Let's record a podcast.

Soroush Khanlou
And it ended up being more work than we expected, but also way more rewarding than we expected.

Chris Dzombak
Yeah, both of those. It's more work, it's more of a time commitment than certainly I expected, and it also has been very rewarding.

Soroush Khanlou
Yeah. So, again, thank you so much to everyone who's listened and yeah, I guess that's it.

Chris Dzombak
That's all cool.

Soroush Khanlou
All right, talk to you next week.

Chris Dzombak
We'll see you on the Internet.

Soroush Khanlou
Yeah, see you on the Internet. Bye.

