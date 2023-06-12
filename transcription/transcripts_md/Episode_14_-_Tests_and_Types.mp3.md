Speaker A
Welcome everyone, to Fatal Error. I am Chris De Zomback.

Speaker B
And I'm Siresh Khanlow.

Speaker A
So recently, Uncle Bob Robert C. Martin, who writes the Clean Code blog and who writes a lot about test driven development and who I really do respect as a as a software engineer, wrote a blog post called The Dark Path. And sirous, do you want to take a stab at summarizing the blog post here or should I?

Speaker B
I do. My summary is that Uncle Bob wrote Swift for about 3 hours and decided, no, I'm just playing. Uncle Bob is famous for writing a lot of Ruby. I think he's spoken to a few Ruby comps, and he's also famous for writing a book called Clean Code. And I think The Clean Coder about Java and how to write like, better, cleaner code. And so he's used to Swift's or he's used to Java's type system, which has lightweight, generics it has a bunch of stuff, but some stuff it doesn't have. Numbers, like doubles and integers can be intermingled and stuff like that. They're primitives and they're not like really fully fledged objects. And he came to Swift and reading between the lines of the blog post, he talks about Swift and Kotlin. Kotlin is effectively it's almost exactly the same as Swift, but it runs with a JVM. The syntaxes are shockingly close. It's a very cool, interesting language. I'd love to write some code in it.

Speaker A
Me too.

Speaker B
Yeah. So he wrote some Swift and some Kotlin, and two things in particular, I think stuck out to him. One was having to deal with optionality, and another was having to deal with how when you throw something in Swift, you have to really explicitly say, hey, I'm going to throw from here. And if you're not going to handle it, you have to mark yourself as throwing or you have to handle it explicitly. And when coming from a throwing exception system like Java's, his expectations didn't line up with what he thought was going to happen, and he got frustrated with the way that Swift's type system was getting in his way, basically. So he wrote a big post about it. That's what this post is pretty much all about, the dark path. The idea is the dark path is Swift and Kotlin have such restrictive type systems that we're going down a dark path and we won't be able to return.

Speaker A
Well. So I think the central thesis is that Swift and Kotlin's tendency toward not papering over, but toward closing every sort of hole in the type system is a dark path that makes a programmer's job harder. Right. And that it's not necessary because these are the sorts of things that your tests should be covering. Right. Not necessarily something that the type system should be enforcing.

Speaker B
Yeah, that's his general thesis, I would say.

Speaker A
And although, as we will learn, I disagree with a lot of the things in this post, I'm trying to characterize his position accurately here.

Speaker B
Yeah, I feel where he's coming from and if you want me to, I can be the devil's advocate here pretty easily. I do still think he's wrong and I more or less agree with you. But I understand where he's coming from enough to where I can take the opposite position. If you want, like, a little more.

Speaker A
Fairness towards Uncle Bob, I think that would probably be a good thing. So I have a number of problems with this post and I really don't even know exactly where to begin.

Speaker B
So I think I have a place that we might be able to start from. Uncle Bob has a tough time writing Swift and I think one of the main things he has a tough time with is the optional type. And I think that the optional type is kind of like if you like it, then you're going to like Swift, and if you think it's too restrictive, then you're going to have a tough time with Swift.

Speaker A
Okay, so let's talk about optional types. Or as Uncle Bob writes in post nullable types and use this as sort of a canary as a starting point for this discussion. Uncle Bob writes, perhaps you've seen enough null pointer exceptions in your lifetime. Perhaps you know that unchecked nulls are the cause of billions of billions of dollars of software failures. And he says it is risky to have nulls rampaging around the system out of control. And he asks whose job is it to manage the nulls, the language or the programmer? So just at the outset, I have a problem with this question because I think we've proven at this point that programmers are pretty bad at keeping track of nulls everywhere. The fact that applications still crash because people try to insert nil into a dictionary in objective C or people try to dereference something that's null in Java or in C or in pretty much any language points to the fact that there's so much complexity here that it's simply not reasonable to expect programmers to deal with it. Good programmers write bugs around this stuff all the time because there's so much complexity here. You can't possibly remember what invariants there are around when something may or may not be null or just checking for null overly cautiously everywhere.

Speaker B
Or if you want to naturally change something that used to accept null to now not accept null or change something to that used to accept that used to not accept null and change it the other way around as well.

Speaker A
Well, we'll get to making changes in a system like this. But right now let's just talk about the value of the option type in characterizing the behavior of a system. Right?

Speaker B
Right.

Speaker A
So the goal of an option type then is to specify whether or not something is allowed to meet null and make sure that the programmer actually handles something where it can be null.

Speaker B
Right.

Speaker A
I don't really understand why this is so painful, but let's accept that it is sort of a pain to deal with and we'll try to make a case that it's worth dealing with that extra amount of effort.

Speaker B
Yeah, I'll happily grant that it is a little bit annoying to deal with. I've seen programmers who I really, really respect move from objective C to Swift, and Objective C has its own weird handling around Nil, but they'll move from Objective to Swift and they will have a very tough time with like, why is this thing necessary? Why do I have to do this? Why do I have to annotate every time I expect something will be nil or not nil? And so I'm happy to grant that it is actually there are growing pains and we moved over to Swift a long time ago and maybe we've forgotten them, but they're definitely there, so that's definitely true.

Speaker A
Now, later in the post, Uncle Bob talks about tests and specifically says what is it the programmers are supposed to do to prevent defects? And he says that it starts with a T. You got it. Test. You test that your system does not emit unexpected nulls. You test that your system handles nulls as its inputs. So I have a few problems with this statement. First of all, to provide the same level of confidence that a type system with an optional type provides about what things can and cannot be null, you're going to need to write a whole lot of tests, and specifically testing that a system does not emit nulls unexpectedly. You kind of are going to have to cover every possible input to a function to be sure that it actually doesn't unexpectedly emit a null pointer. Right.

Speaker B
Or some kind of randomness testing or something like that.

Speaker A
Right. You can use some sort of property checking. Like Quick check would be the sort of original implementation. I believe Fox is an implementation of property testing for objective C. And there's one for Swift that I don't remember offhand quick, maybe. I don't think it's quick. I think it's maybe Swift test.

Speaker B
Swift check.

Speaker A
Swift check. That makes sense. But I think it seems like a fair statement that no one is really using those to test properties of their systems and objectives, C and Swift. So really what I think I disagree with Uncle Bob about here is the intention of tests versus the intention of your type system. Given a function or a system that you're trying to characterize, you care whether inputs and outputs can be null or not. And you can verify this with one of two verification methods. You can use a type system which provides you with a guarantee about what can and cannot be null, or you can write tests about what can and cannot be null and hope that you cover the inputs that might somehow trigger a null output from this system. And unless I'm missing something in Uncle Bob's argument here. I don't buy that. I just don't buy that for every class you're testing, you're going to cover a sufficient range of inputs to actually have the same level of confidence about whether it'll output a null pointer that you can get from the Swift type system just by default.

Speaker B
Yeah, I mean, I would really like to see some of his tests to see how thoroughly does he really check that, oh, this thing will never emit null, you know what I mean? And in a lot of cases, it seems like you'd just be relying on even documentation or comments just to say, hey, you shouldn't pass null here, at which point just use the thing that enforces the comment within the code itself.

Speaker A
Right. That signature, that type signature becomes the documentation of whether null is allowed.

Speaker B
Right, right. And it's not just the documentation. It is the thing.

Speaker A
Right. It's self documenting in that regard.

Speaker B
Right, exactly.

Speaker A
So more generally, I think what we're talking about here are I'm going to say there are sort of two methods for verifying that a piece of software works as expected. You have like static type checking, or let's say for purposes of this discussion, just type checking in general. Right. And in the case of Swift, we have a pretty in depth type system with things like an option type. And then we have tests, and we have tests in a number of languages, too, including Swift. I'm going to make an analogy here. Let's consider each type in our program, or let's consider each object in our program as a puzzle piece. Now, puzzle pieces have a color or pattern printed on them, and they also have a shape to the outside, right?

Speaker B
Right. I'm with you so far.

Speaker A
Okay, so I'm going to argue that the behavior of this object and whatever data is contained in this object are sort of the pattern or the color printed on the puzzle piece and the type of this object or this function is the shape. And I mean, you see this actually when we discuss the shape of an object or the shape of a type or the shape of a function, right?

Speaker B
Right.

Speaker A
Our end goal is to put together a puzzle that is correct, that the patterns and colors match up and that the shapes also match up, right?

Speaker B
Right.

Speaker A
And so to provide that level of verification, we have a few tools. We have tests which I think should be used to verify that the color and pattern printed on an object. Let's consider this the interesting parts of an object, the behavior that you've written, the properties that you've added to an object, the implementation of a function. Right. These are things that we cover with tests. And I think it's the type system's job to verify that the shapes of these objects go together. Now, different programming languages will have different type systems that allow you to create more or less complex shapes for your puzzle pieces, right?

Speaker B
Right. So something like Haskell could make a really complex puzzle piece and something like Java could make a less or C or C plus plus could make a less complex puzzle, right.

Speaker A
Or something like JavaScript will make a.

Speaker B
Less distinct in JavaScript, everything is just a square that sits next to each other. There's no shape at all.

Speaker A
Okay, it's a bad example. Okay. What Uncle Bob is kind of arguing is that having less distinct shapes and relying on the programmer to look at the color and pattern of these puzzle pieces to make sure they're put together correctly is a good approach. And that making those shapes more distinct so that the programmer is concentrating more on the shapes of things. Has to think about the shapes of these things a little bit more is a darker path. And I really don't necessarily buy that. In fact, with sufficiently distinct shapes, you could even imagine putting together a puzzle without even looking at the pattern printed on puzzle pieces. And we do this kind of thing like if you look at the function signature for the Map function, you can almost know what the implementation of this must do, know what the color and pattern on that puzzle piece must be. Simply by looking at the shape, right. You have something that takes an A and a function from A to B and gives you a B. You don't really need to look at the implementation to know how that fits into the larger application, right? Does that make sense?

Speaker B
Right. So friend of the show, Brandon Williams wrote a really great blog post last year called Proof in Functions and it really walks you through step by step, why, if a function accepts, let's say, an A and a function from A to B, it can only return a B. There's nothing else it can return because it doesn't know what B is. And so we'll toss that in the show notes. It has these cute exercises at the end which are really, really fun to do. So I recommend those as well. But yeah, for sure there are some things like Map where there is only one way you can implement it because you have to get the values from the things that you're passed in.

Speaker A
Right? And that is a really great post that we'll put in the show notes and I highly recommend that our listeners go and read that episode.

Speaker B
Okay, one of my big questions for Uncle Bob is you could write this exact same article about any type system at all. So you could write this article about Java's type system. But he seems to like Java's type system. He likes the fact that he has generics and he likes the fact that he says Java and C sharp have done a quote unquote reasonable job of hovering at the balance point. And then he likes Ruby and stuff. So I could just see him easily writing this exact article for like how dare you make me tell you what's going to be inside my array. I'll put whatever I damn well please inside my array. And it's like the argument that proves too much proves nothing at all really. If you could use this for anything, why would you use it for anything?

Speaker A
Right? At the core there's the argument that we don't need type system feature X because we can cover it with tests, can be used against any feature and any type system feature. And I feel like that may be a logical fallacy of some kind, but I haven't gotten around to figuring out which fallacy it is. I should note that as we record this, I'm drafting a blog post that is turning into a much bigger project than I had anticipated to respond to Uncle Bob's blog post here. And so I'm sort of workshopping some of these ideas here. So at the end of the day, our goal is to verify that our system is put together correctly. Is to verify that our puzzle is put together correctly. And I say that having more distinct puzzle piece shapes is a good thing and helps us because programmers are notoriously bad at exactly matching up colors and patterns and noticing when one pattern is next to another pattern that's almost, but not quite the same. Am I taking this metaphor too far?

Speaker B
I like the metaphor to be totally honest. It's a good way of saying the colors are behaviors and the puzzle pieces fitting together are shapes and verifying that having both tools to do the verification is good. So yeah, I do like the analogy.

Speaker A
I also do like the metaphor because it's sort of clear that at some level we are arguing a subjective point. Right?

Speaker B
Right. So ultimately the unfortunate truth of all this is nobody has been able to prove that having a static type system will deliver defectless or like a system with less defects than another system. If you put two good programmers on a big project, one is Ruby and one is Haskell, nobody has done that study yet to prove that the more rigorous type system is like, producing fewer defects.

Speaker A
This is true. I will however, argue that we know that certain classes of defects, particularly defects that cause fairly common security bugs like buffer overflows, null pointer exceptions that's Java terminology, but dereferencing null pointers. In this article, Uncle Bob also talks about exception handling. We know that unexpected changes in control flow are to something that the original programmer didn't anticipate. These are all things that have caused very real, not just bugs, but really serious security vulnerabilities that have impacted real users of these systems. And things like Swift's type system do go a really long way to prevent these specific classes of bugs. So though there will be defects, I think that eliminating some of these classes of defects which have led to just some huge number of very common and very harmful bugs is a concretely good thing.

Speaker B
The person who invented the idea of null is Tony HoR. I don't know how to pronounce his name exactly, but he calls his own invention the null. He calls it the billion dollar mistake. He says that we just should have never done this in the first place. And between null dereferencing and between, like an objective C, that behavior was implicit and you would kind of have this big long chain, and something in there was nil, and now your value is zero when it should have been something else. And that's caused bugs that I've had to fix more than one. And I'm certainly happier and more confident with my code knowing that I have the types there as a check to sort of sort of catch me.

Speaker A
I think that's absolutely true, and we'll try to find a reference for that quote from Tony HoR. I also don't know how to pronounce his last name. Skipping ahead a little bit in Uncle Bob's blog post here, he says all these constraints that the languages are imposing presume that the programmer has perfect knowledge of the system before the system is written. And I mean, that's simply not true. You can absolutely write a system that you think is right and go back and figure out what needs to be done to make your optional types match up with each other. And the places where those mismatches occur are places where bugs might have arisen before. If you wrote this system and then tried to characterize where things can and cannot be null after the fact by writing tests, or if you're writing those tests ahead of the time, I don't see how that's any different from knowing whether something could, can, or can't be null before you go ahead and write an optional type there. I just don't see how this argument is valid. You're either writing tests about nullability before the system is written, which assumes that you have knowledge of the system, or you're writing a type signature before the system is written, and that's before the system is written. I just don't believe that's a valid argument. Now there's sort of a discussion here that we can have about whether a more restrictive type system makes code harder to change. It means that you have to know more about the system in order to change it. I also think that that's not true because you can still go in and make changes, and a compiler will flag where mismatches have occurred. And first of all, this is how you learn about a system. You can learn about a system by trying to change it and seeing where these mismatches occur and learning more about the code that surrounds the part of the system that you're changing. Right. The same thing would happen with tests if the tests that are there actually characterize the system to this degree of detail. If you make a change and now something returns null that didn't return null before, then either the type system will catch it in a language like Swift and say, oh, by the way, these callers for this function need to handle this output now or the test for this function will fail. And you know that you have to track down the callers for this function and make them handle null properly. If your tests are actually characterizing your system and providing the same degree of verification, then I don't see how that's any better in terms of writing the system initially or in terms of changing the system than having the type system enforce these constraints for you. Except that writing tests around all this stuff is going to be so much more verbose and takes so much more time. And maybe there's an argument that you're not actually writing tests that characterize everything to the same degree of confidence that a type system gives you. But I mean, in that case I'll opt for the type system because I want a high degree of confidence that my system is put together as it should be.

Speaker B
Right? I feel like the counterargument here is that even if the test takes a long time to write and a long time to set up setting up let's say the and I'll go all the way back into type system. World system like Ruby or JavaScript, where you would have to set up a protocol so that you could do, like, let's say, the null object pattern. Whereas with Ruby or JavaScript you just make it kind of respond to the same messages and you don't need to make that protocol. So there's a little bit of work up front you need to do to create the type system like constructs that you're going to be using and there's going to be some work you need to do in the testing world to set up like your arrange your system under tests and then actually test it. I don't know. The deeper we get into is the more I'm convinced that tests and types are the line between them is super, super blurry. They're both ways of verifying your system and verifying that it's true. If Uncle Bob wants to throw one out, that's fine, but I think if anybody tried to throw out TDD, he would really have a huff about it.

Speaker A
Well, and to be fair, I don't think he's throwing out type systems entirely here.

Speaker B
Well, I mean isn't he? He's really making the case that he says a bunch of his arguments are around like oh, you have to know these things up front or oh, you have to declare what you think this is going to look like. And that applies to all type systems. It doesn't just apply to nullable type systems as he calls them.

Speaker A
Well, I mean, it's true that the argument can apply. I don't think he's trying to apply them. I want to try to be a little bit charitable to him.

Speaker B
There's another thing that I think is interesting here where it kind of sounds like he's trying to write a server and he wants to be able to throw from really deep in the stack. Like let's say if some input is not valid, he wants to be able to throw all the way up the chain to the top. And there's reasons that Swift doesn't allow it. And I think it's kind of elegant the way that Swift works because they introduced defer at the same time as they introduced throws and all of that stuff so that you could defer code that would run when you return from the function or when you throw from the function so you can clean yourself up more easily. And I think that's kind of like a nice elegant way to handle things. But throwing errors in Swift is not the same as throwing exceptions in JavaScript or in Java. Also in JavaScript they look really similar, but they really are not the same thing. I think thinking about Swift system as typesugar, which is in my opinion not that sweet typesugar around a result type makes it really obvious that hey, you're not actually throwing something up the stack, you're like really returning an error and so you can't use it in the same way that you would use Java. Exceptions. They're a very different thing and if you want to it's not going to go well for you. You need to figure out how this language works and how to work well with it. And I think it's one of the big things that he misses about the fact that hey, these are different languages that are designed in different ways.

Speaker A
I mean, I think that's an excellent point. So he does seem to conflate exceptions in Java or C Sharp with Swift's error handling model, which looks a lot like exceptions, but as you note, is almost more of a functional style result return type.

Speaker B
Right?

Speaker A
But even given that let's accept this for a second, I will argue vehemently against exceptions automatically propagating up the call stack with no awareness, with no note about that in the type system, particularly if you're writing a server. I mean, again, those sort of unexpected control flows are the sorts of things that lead to security problems, right, which we're really concerned about if we're writing a server. I hope. And he writes that you test every exception you can throw is caught somewhere. The thing is, if types aren't notated somehow that they throw exceptions, I mean, how do you know what exceptions can be thrown or how do you know what can throw? You're sort of back in the Stone ages where anything might exit at any time and it's not good. I've got nothing else, it's dangerous.

Speaker B
Let me ask you something else here. Obviously Swiss type system lets you annotate that and you kind of touched on this, that things can throw, but it doesn't say what they can throw. Now, Swiss type system basically does not have, as I think they're calling Java checked errors. So it checks that you will throw an error, but it doesn't say like, I will throw these types of errors. And that is in some senses a more strict type system that Swift opted not to have. And people who write any kind of signals or observable or reactive based code know that, well, those errors are parameterized and I do have to declare them upfront. I think sometimes that's frustrating to work with. So maybe am I making the same argument here that Uncle Bob is making?

Speaker A
I think you kind of are. Although we have a huge body of code written in C sharp and Java that just uses the top level exception type everywhere anyway, which is an argument for the Swift approach.

Speaker B
So if Swift had very strictly typed exceptions where you couldn't use just error or error type, and you had to use a specific error type, would you be in support of that?

Speaker A
I used to say very emphatically yes to that. I'm now unconvinced. Like I'm open to being convinced one way or another right now.

Speaker B
Right? Yeah. For me, I mean, when I wrote my promise library, I chose to have unparameterized errors. It's just a little easier to work with, I think.

Speaker A
And let's remember that if you do want parameterized errors for some part of your application, rather than using the sort of Swift throwing mechanism, you can use a result type that has a type constrained error. Right.

Speaker B
You could just bring it all yourself, basically.

Speaker A
Yeah. Boy, I don't know, there's a whole lot to unpack here. There really is. I just think that tests and an in depth type system are two different ways to verify software and they're complementary ways. But for some things that are common mistakes that we know programmers are bad at dealing with, like error handling, like null pointers, these are things that elevating them into the type. System is really trivial and I really do not believe impose more work on the programmer either when you're writing the system initially or after the fact changing the system than covering everything with tests to provide that same level of confidence. That's more work than just letting the type system work for you.

Speaker B
Yeah, I'm really not a fan of this argument of, like well, either extreme is bad because on the one hand, that's kind of trivially true, and on the other hand, you can't use an argument to say that the far end of the thing is bad because then you'll just end up at the other extreme. Kind of like why do you write Java? Why do you like Javas types of stuff?

Speaker A
So, a few days after this blog post, there was a large outcry from a lot of people and. Uncle Bob posted a follow up entitled Types and Tests. And I also take issue with the number of points that he makes in this blog post, but I haven't read it as carefully. So I'm going to choose one thing here to pick at. And it seems to be a thing that his argument sort of hinges on and I think that it is incorrect. He says that types do not specify behavior. Types are constraints placed by the programmer on the textual elements of the program. So what the type system is checking is not the external behavior of the program. It is checking the internal consistency of the program text. And that is not true. It's checking the consistency of the program. It's checking these high level things within the program function signatures and objects and structures all actually line up. It's checking that consistency at a really high level, not making sure that the program text matches up. It's checking that you're not passing null to something that doesn't accept null. Right? These are high level checks. This isn't checking the consistency of the program text. A little bit later he writes so how internally consistent does the program text need to be? Does every line of text need to be 60 characters long? And I mean, I think this is a straw man argument that maybe demonstrates that he doesn't understand what a type checker is trying to accomplish. We're not trying to check that the text is internally consistent. We're trying to check that these high level concepts that these puzzle pieces that we're building a program out of actually match up correctly. And we're trying to take some of that cognitive work away from the programmer because again, programmers are not that great at matching up colors that look really, really close on the printed puzzle piece.

Speaker B
So I think that's a really interesting point too, because anytime that something is causing a problem and is consistently causing a problem, especially as programmers, we want to kind of factor that out and create some abstraction around it so we don't continue to make that, to continue to do the same thing over and over again. So if we have to check if something is null every time, why don't we build a structure around the fact that it can be null or can't be null and kind of formalize that in the same way that we might formalize any abstraction? Like if something comes up over and over again, such as throwing errors, such as something being there or not there, why don't we just make a program that can verify that for us, right?

Speaker A
And when we come up with one of these abstractions that we want to elevate, elevating it into a system that can verify it, as you say, automatically for us, that takes all of the cognitive load off of the programmer is, I mean, just in my mind, so clearly self evidently valuable.

Speaker B
Yeah, but it's not so clear to Uncle Bob, and that's so strange to me that he's written so much code and that he knows what it's like to write a good object, and he knows that it's like it should have a consistent identity and it should be around a thing. He literally invented the single responsibility principle, and to me, the concept of optional really crystallizes the single responsibility principle because you're saying, hey, if this object exists, if this person exists, it must have a name, and I can build something around that requirement. And I don't really understand how someone can understand programming and objects on that level and still be like, but I don't want to know if it's going to be there or not. I'll write a test or something.

Speaker A
Well, right, but I mean, again, from my reading of his first article, he does want to know. He just wants to guarantee it via tests. And I just fundamentally don't understand why we can verify this automatically for you. And I have tried, and I can't buy the argument that somehow enforcing these properties via tests is somehow easier or requires less upfront thought or requires you to know less about the system. I don't understand this argument.

Speaker B
Yeah. Honestly. Yeah, me neither. Okay, so if you remember, is TDD dead thing, basically, he, Kent Beck, Martin Fowler, and David Hannah Meyer Hansen all got on, like, a Google hangout that was, like, published to everybody, and they argued about whether TDD was good or not. And he writes, the conclusion of the hangout was amicable, respectful, and agreeable. Martin and Kent said TDD worked. David said that TDD did not work in fewer circumstances. If there was some disagreement, it was simply a matter of degree. All parties agreed that programmers should try TDD and then tune their use of it to what works for them. And if you really like no pointer exceptions, you can put exclamation points everywhere. That's fine. Choose that level of whatever. You can't have exception handling the way you want it. You could say the exact same thing about tests, and it's like, I don't know. I feel like if we were in person when you're in person with someone, you kind of can come to some kind of central area. And I think the conclusion we will come to is like, hey, I like types. You don't like types, that's fine. We'll just do what we feel like, and we'll make the software that we like to make like it's valuable for some people, and they find comfort in that safety net.

Speaker A
Yeah. Use exclamation points right, and you get.

Speaker B
The exact behavior of Java, which is no pointer exceptions if the thing is not right but you see it and you don't want to. And I think that's the kind of telling thing. It's like, I could leave this exclamation point out, and I'm choosing to have to put it in there because I kind of wouldn't be surprised if he kind of, like, pulled back on this claim a little bit. If he did a blog post in three or six months, it was like, yeah, I understand why these types are valuable. I understand why optional is valuable. I do miss it now in, say, Java, but I still don't like types or whatever.

Speaker A
Yeah, I'm thinking that he might. Thank you so much, everyone, for listening to this episode of Fatal Error. I hope that this has been informative or at the very least, thought provoking. And since this is an episode that we're posting just on Patreon, I would like to say again, thank you so much for your support. It really does mean a lot to us and it's really making it possible for us to produce, I think, a better podcast for you guys, for sure.

Speaker B
Yeah, I just want to reiterate and just strongly agree with Chris. It's really great that you supported us in this way, and we really do appreciate it.

Speaker A
So thanks again and we'll talk to you next week. Kids, these days, have I become a grumpier older man than Uncle Bob?

Speaker B
It's possible. He literally has a blog post called not on My Lawn. Or what is it? It's called my lawn.

Speaker A
Oh, shit. Maybe I should call my blog post. No, my blog post is going to be titled well, I posted it to you in defense of in depth static typing and software verification. No, static typing is wrong. Of in depth type checking.

