Speaker A
Welcome, everybody, to Fatal Error. I am Krista Zomback.

Speaker B
And I'm Siresh Kamlo.

Speaker A
And this week we're bringing you a special episode with Sirous live from Australia. Or I guess not live pre recorded from Australia. Sirush, why are you in Australia?

Speaker B
So there is a conference and it's called Playgrounds. And they wanted me to speak and they flew me down to Melbourne. And the conference is just wrapping up now, and so I thought I would call you and talk to you a little bit about it.

Speaker A
Awesome. I'm really excited to hear about it. We'll start with initial impressions. I've never been to Melbourne or really anywhere in Australia. How are you liking it so far?

Speaker B
So I also have never been to Australia. This is my first time in the southern hemisphere in Australia, and definitely Melbourne. And it is awesome. Australia is a beautiful country. I went like a road trip of the great ocean road. The food is great. Melbourne. This is one of the running jokes of the conferences that it's the most livable city in the world. And you could just tell because the air is really nice to breathe. It's so easy to get around the city. Bikes, or whatever they call them, don't have branding here. There's no company that sponsors it. So it's just the Melbourne bike, which is really nice. There's beaches cool. And it's just so nice.

Speaker A
That sounds really nice. Yeah, man. And it's not winter there right now. It has that going forward, too.

Speaker B
That's right. It's effectively August for listeners in the northern hemisphere.

Speaker A
Nice.

Speaker B
Yeah. And Playgrounds. The conference has been awesome as well. Andy Hope put it together and everything's been going really smoothly. The speakers have all been super great. The conference center is awesome. It's like really central in Melbourne and there's lots of cool stuff to do around it. There is. One of the things that Melbourne has, and I don't know if this is just Melbourne or other Australian cities as well, but in the parks there are barbecues and American barbecues. It's usually like cast iron and you have to kind of bring your own charcoal and light it. These are powered, so you just sort of push a button and you get 30 minutes of heat. And so I bought some yeah. Isn't that awesome? And so I bought some ground kangaroo and some buns from the Victoria, the Queen Victoria market and a little cheese. And I made kangaroo burgers outside, just like in a park. It was so cool.

Speaker A
I didn't know that people ate kangaroo.

Speaker B
Yeah, you can eat kangaroo. You can get it in loin form and in minced form, which is how they say ground down here. And the kangaroo burger was super good. And thank you to all the fine Australians who've hosted me these past few days. It's been awesome.

Speaker A
So you mentioned that the conference has been going really well, and I was really curious about your talk how did your talk go? What did you talk about?

Speaker B
Yeah. So my talk was basically it was titled everything that You've Ever Wanted To Know About Sequence and Collection. So for the past few months, I have been kind of studying Sequence and Collection and learning everything I can about the weird APIs and about the complexity guarantees that different levels of whether you have Random Access Collection or regular collection and what all those guarantees are and what the functions are and how they work. And so I basically distilled that down to 25 minutes. I didn't get a chance to cover every single protocol that was involved in it because it's a pretty complicated piece of the standard library. But I did manage to cover basically everything in the ladder from sequence collection, bi directional collection and random access collection.

Speaker A
Cool.

Speaker B
The ones that I missed were Range Replaceable collection and Mutable collection.

Speaker A
That seems like it would have been a really interesting talk. I mean, that's something that, like you said, is an area with some complexity in the standard library when you're approaching it that's not necessarily immediately clear. Right?

Speaker B
Yeah. And it's not clear how they all relate and what the associated types mean and all that stuff. So it's nice to have like a high level overview of it. The talk 25 minutes was barely enough time, so I was really blitzing through the material and I think some of the attendees were like, oh my God, this is so much stuff. And one person tweeted at me that they needed to rewatch the talk later because it was so much stuff.

Speaker A
Is there going to be a video of the talk up? Are you publishing slides somewhere?

Speaker B
I can publish slides, but yeah, Andy said that there were going to be videos. A company called Skill IO who does the swift summit. So they have some experience with making videos. They are putting the videos up, so that should happen in the next several weeks to several months.

Speaker A
Okay, cool. Well, we will definitely include at least a link to the slides in the show notes for this episode then. What are some interesting or maybe surprising parts of the Sequence or collection APIs that you want to share that I might not know?

Speaker B
Yeah, so the two big gotchas with sequence that kind of few people know about. One is that sequences can be infinite. So you can construct a sequence such that it never terminates. A simple one would just be like a sequence that adds one to the previous element. So you could just have all the natural numbers or whatever, and that can be a sequence and you can consume as many of those as you want. If you try to map over that sequence, you're going to have a bad day but get stuck in an infinite loop. So that's a weird thing, is that while collection is always going to be finite, sequence can be infinite but a.

Speaker A
Collection is also a sequence, right?

Speaker B
Right. A collection, you provide a different set of things and it automatically gives you sequence conformance.

Speaker A
Okay?

Speaker B
It's sort of a ladder where each thing inherits from the previous. So sequence collection inherits from sequence, bi directional collection, inherits from regular collection, and then Random Access Collection inherits from bi directional collection. So I kind of illustrate as a ladder on my slides so that you kind of we worked our way up the ladder.

Speaker A
That makes sense. And then just for clarity here, bi Directional Collection means that given an index in a collection, you can increment or decrement it to walk around the collection. Kind of like a link list.

Speaker B
Exactly. Like a doubly Linked list.

Speaker A
Right. And then Random Access Collection means that you can index just anywhere into the collection arbitrarily in constant time.

Speaker B
Exactly, yeah. So basically, from the names, you kind of picked out exactly what's going on here? The names are, I think, pretty good.

Speaker A
Yeah, I would say so. At least it seems clear to me, hearing those names. And I mean, having read some about this API before, it seems clear what's going on. We'll definitely put some useful reading in the show notes about what it means for something to be constant complexity, which you referred to as O of one time right. And linear complexity, which would be O.

Speaker B
Of N. The other interesting gotcha with the sequence protocol is that you're only guaranteed to be able to iterate a sequence one time. It happens pretty rarely, but there are some sequences where if you, let's say they have five elements in them and you iterate through all five, if you try to iterate that sequence again, you'll just get zero elements.

Speaker A
And this ties in with the concept of generators, right?

Speaker B
Yeah, exactly. So every sequence has a function that creates they're called generators in Swift Two, but in Swift Three, they're now called iterators. So every sequence has a function that will create a new iterator, and then that iterator that iterator is destructive and acts as sort of a cursor to each element in your sort of sequence. And so it knows where it is, it's stateful, but the sequence itself is usually not stateful and can usually create a new iterator on demand, but not always. And there are some really contrived things you can do with the standard library. And you can make a sequence that once you iterate through it, it's consumed and you can't iterate it again.

Speaker A
Is that constraint reflected in the type system around sequences at all?

Speaker B
It is not, and it really frustrates me.

Speaker A
So if you have just a sequence, there's no way to tell whether you can iterate it more than once.

Speaker B
Exactly. Usually you can just upgrade it to a collection and you know that a collection will be finite and infinitely iterable. So usually that's the way to kind of get around it.

Speaker A
Okay. Unless it truly is an infinite sequence. Like the Fibonacci numbers or something.

Speaker B
Right, exactly. The other thing I wish was reflected in the type system is I want finite sequences and infinite sequences to be different types so that if infinite sequences are their own thing and then finite sequence would be where you would add something like map or filter because those require the sequence to be finite.

Speaker A
Okay, and then collections would be finite sequences and so they'd get map and filter like they do today.

Speaker B
Exactly. So you would have infinite sequences which would kind of be another level of the ladder lower and they just wouldn't get some functions like you might be able to do. You would be able to do like lazy, you'd be able to do prefix where you get the first N elements of the thing but without it being a finite sequence you can't do for example, suffix where it would get the last N elements or you won't be able to map and stuff like that.

Speaker A
Yeah, that could make sense.

Speaker B
And I think that would be really nice. Yeah, I think that'd be a nice little guarantee to add to the Standard library.

Speaker A
I wonder if there would that fit in well with the current with the current design that's in the Standard library. I know that a lot of consideration has gone into the design of these protocols and how they all interact and you are in a better place than I am to know whether what you're proposing here actually fits in nicely into what the Standard library has today.

Speaker B
Yeah, I mean, I think it's possible. It's just that it makes some things a little bit more every time you add a stricter type to the system. You have to kind of deal with that in certain places and it can be frustrating to deal with. So you develop a sequence that looks like it could be infinite, but you know that it terminates. So for example, one sequence can be you start with your current view and then call self dot SuperView each time and then until you get to the end of the sequence which is the root view which has no SuperView. You know, that's going to terminate at some point but you would have to do some dancing and do like prefix 1000 just to ensure that hey type system. I really know that this is not going to have more than 1000 elements. I know that it's going to be finite, et cetera. So I think it's some of that stuff that they don't want to impose on consumers of the Standard Library. But infinite sequences are so rare.

Speaker A
Yeah, at least in the sort of programming that we typically do day to day.

Speaker B
And it would just give you a little bit more control and a little bit more flexibility over the stuff and it would just be fun. I like representing complex things in the type system and making things that will crash be impossible, such as trying to map over an infinite sequence.

Speaker A
Yeah, absolutely. So that sounds pretty cool and useful. I'll definitely look over your slides and I will look forward to video being posted. But you weren't the only person who talked to this conference. What were some of the other talks that you went to and that you found interesting?

Speaker B
Yeah, the other speakers, I mean, it's a really great lineup. So the way that the conference works is basically you give your talk and then you go to a special side room and in that room you have it's sort of like the speaker access room. And so for 30 minutes after you get to hang out there, and any of the guests, any of the attendees that want to come and ask you questions, they can bring their laptops. We can talk about code and you can really work with stuff rather than just sort of like having a microphone where you just sort of ask questions and the whole audience has to be there. But the downside to that is that the speaker misses the talk that's immediately after them. And so the talk that I missed was Matt Comey's talk from he's the bitbucket software guy who makes all those pixel games. So Stagehand, I think, is the one they just made. And so his talk seemed really cool. I only caught little pieces of it from there's, like a video feed in the speaker access room. And it looked really cool. It was about like pathfinding in games. It was about ray tracing and basically how to model these algorithms for your different games. And it looked really cool. So I'm looking forward to catching up on that one when the videos come out.

Speaker A
Yeah, that sounds awesome.

Speaker B
So I did miss that one, but I did catch quite a few others. So one of the first ones was Matt Gallagher, who writes a blog called Cocoa with Love. And it was really cool. I've never met him and I finally got a chance to thank him. He wrote an audio streamer class from, I don't know, five years ago. And I wrote a podcast player completely built on top of that. And I would not have been able to do it without his sample code. And I talked to him about it and I really thanked him and he was like, oh man, that code, I hate that code so much today. But he's really happy that so many people have gotten so much use out of it.

Speaker A
So setting aside thanking him for the example code, what was his talk actually about?

Speaker B
So his talk was basically about performance tuning Swift. And he basically wrote he had this algorithm, I think it was like a mercen prime generator. And he wrote it in C and then compared it to an implementation in other languages like Python and Go, and then wrote a swift implementation and a naive swift implementation, like basically, copying line for line was about 50%. To 60% slower than C. But when he kind of removed some of the safety guarantees of swift, he was actually able to get the swift to execute faster than the C, which is pretty impressive to me.

Speaker A
That's really impressive. Yeah. Wow.

Speaker B
So instead of an array, he used an unsafe buffer mutable pointer or whatever. And that is just like unchecked memory, and so you're able to scream through that. And then he also did additions without checking overflow. And that also helped a lot in tuning the Swift and making it more performant at the cost of some safety.

Speaker A
Yeah, that makes sense.

Speaker B
So it ended up like 10% faster than the C, which was pretty dope.

Speaker A
Yeah. Wow.

Speaker B
Yeah, that was a really cool one. Tamar, a friend of the show, Tamar, who works at Tumblr, gave a talk about how to use engineering concepts to talk to your designers, which was a really fun one.

Speaker A
Oh, cool.

Speaker B
Yeah, it was basically like, she has a designer that she works with, and the designer had overheard someone talking about unit testing, and it was like, oh, what's unit testing? And they ended up basically finding some common ground over this concept that seems very engineering focused, but the designer was actually able to relate it back to their own work and basically grow in their own way. And the design and the developer kind of grew it together and were able to do better work because they had communicated about their own sort of domains.

Speaker A
Cool.

Speaker B
So another cool talk friend of the show, Jason Brennan, closed out yesterday's sessions. He basically spoke about one of his passions is educating kids and giving them tools to understand systems. And so the best thing we have for that today is programming. But he thinks that programming within basically text is a very tough thing to grasp for kids. And so he wants to build tools for and he was kind of laying out this problem of how we should build tools that are more dynamic media that kids and adults can work with to understand complex systems. And so he talked a lot about human behavior and the human brain and education and what code is, and he talked about basically Swift Playgrounds, which we have today, which are being used on the iPad, like teach kids. And then also Playgrounds, which was an app that Apple made in the Think, probably before they called them apps, which would let kids write kind of pseudo code to add behaviors to fish and animals and stuff. I don't know the depth of it, but that was the example that he showed, and it was at a conference called Playground. So it was very meta.

Speaker A
Wait, so Apple had made this thing in the it was called Playgrounds?

Speaker B
Yeah. Well, so it's called Playground with no S, but yes. Okay, I may have misspoken earlier.

Speaker A
So the Swift playgrounds really came around. Like the name is coming full circle, isn't it?

Speaker B
Absolutely. Yeah. It's a total redux.

Speaker A
Cool.

Speaker B
Well, as Sam Gins talked about strings, which you would have really cared about, he talked about how strings shouldn't be the universal type.

Speaker A
They shouldn't. I've given a talk about that.

Speaker B
Yeah, you sure have. You got to give that is that online?

Speaker A
It is online, yeah. I think there's video and audio and slides of it online.

Speaker B
Nice. We should try to put in the show notes. So there were two more really good talks that I want to touch on. One was. Chris idolf did a talk. It's called How I Learned To Stop Worrying and Love mutation. A nice little Doctor Strange love reference. And he basically talked about how Structs are. They're pretty good and they can be immutable, but sometimes that mutating keyword is pretty good and it doesn't really mutate the thing. It only kind of acts as syntactic sugar around the mutating thing. And so he talked about how it's actually okay to have mutating functions and have mutating code. It's just choosing the right sort of paradigms for your app. So if you need a reference type that mutates, then great. If you want a Struct that has mutating functions on it, if that's the right thing for the code that you're working on, then that's the right thing for the code that you're working on.

Speaker A
Yeah, that makes sense. I mean, as much as we really push sort of immutable, functional sort of style of programming, especially with value types and with swift structures, there's absolutely a place in some applications and some algorithms and things like that for mutation. Right. It exists for a reason. It may be widely overused in some places, but it does exist for a reason.

Speaker B
Right. And you can kind of look at the Standard library. There's tons of mutating functions on Structs in the standard library. Like, it's just useful and it's built and designed to be used like that. And he live coded the whole talk. And it was so impressive because he barely mistyped any keystrokes. Like, when I live code, I'm just like messing words up all the time. And every keystroke he hit was, like, the exact right one. And he didn't have to backs me. So I was so impressed.

Speaker A
That's really impressive. Yeah. I never live code because yeah, it's just embarrassing. Yeah.

Speaker B
It's so tough. And it's tough to talk while you're doing it and not be boring because when you're typing, you're not saying anything and the audience is just watching you type. And he managed to basically have jokes and work his way through all of this stuff and not lose the interest of the audience. It was really cool.

Speaker A
Nice.

Speaker B
Yeah. And then the last talk that I wanted to talk about was a fellow named Harlan Haskins, who goes to Rochester Institute of Technology, and he is a student, and he worked on the Swift compiler team as an intern last year and he is crazy about LLVM. So he basically showed us how to build a parser, a lexer and a compiler for a language called Kaleidoscope, which is a very simple language where the only data you can have is floating point numbers and functions and you can kind of build up quite a complex bit of stuff with that. And so he basically passed his program through a Lexer and showed us how the lexer worked, passed the lexed data tokens into a parser to create a syntax tree and he showed a ton of code and it all made sense. And once that AST came out, then it would go to this thing that would emit LLVM intermediate representation, which at that point you can just build into any architecture so it can run on any computer, which is the whole promise of LLVM. And it was his first talk and he was just such a great he just had that natural teaching ability where he talked slowly and you understood and he was very clear and I asked him so Harlan, why are you so good at this? This is your first talk? And he was like, I'm actually an actor. He acts in various classical and more modern things and that's how he knows how to project his voice, how he knows to stand up straight and how he knows to be clear and don't say and stuff like that. And it was just honestly so impressive.

Speaker A
That's really cool. Wow. And there I am saying because I am not an actor, but this podcast.

Speaker B
Is very ad hoc.

Speaker A
It is pretty ad hoc, yeah. The whole field of sort of compiler, computer science, lexers and Parsers and things like that are things that I would love to understand better and to know more about but that I've never really gotten around to teaching myself or to learning. And so it's just kind of a black box to me and this sounds like it would be a really interesting talk for me.

Speaker B
Yeah, I would definitely recommend this one for you because it's all Swift, so you can understand it. I've seen Lisp interpreters written in JavaScript, which I don't care about Lisp and I don't really like JavaScript, so that's tough. But this is a very simple language, has almost Rubiesque syntax and all the code is written in Swift so it's super easy for us to understand. And he showed me after the fact, he showed me he has another language that he designed that he wrote himself called Trill and it's got its own compiler and everything and it's basically Swift lite. Like I looked at the syntax and it's like very simple Swift. It's like Swift without some of the features taken out. Yeah, so I thought that was really cool. And we were talking a little bit about parsing the individual Tokens and he said he was adding generic support, but that it was really complicated because when you add, like, the angle bracket for generics, you don't know if that's going to be a less than token or if that's going to be the start of a generics Token. So you have to kind of see what other tokens you have and then backtrack and update that one to be the right thing. It might be a generic token. It might be less than. So that one I thought was really cool too. And I think a lot of his code is open source on GitHub, so if any of our listeners want to go check it out, they can see how that stuff works.

Speaker A
Yeah, that sounds great. I would imagine that working as an intern on the Swift team or working on the Swift team in general, but that would be a really unique internship experience. That's pretty cool, for sure.

Speaker B
It sounded like it was really awesome. It sound like he learned a ton too, man. Yeah, it's been a great conference, man. There's been this through line of I love how when the talks, like, kind of interleave with each other. Like, I talked about Linked lists in my talk, and Chris Idahoff brought them up in his talk for, like, an example of he wrote a pop function on a Linked list, and he made it mutating, and he was like, this is okay, and here's why. And then there were other talks that related to other things. So, like, Ashborough talked about asynchronous programming and all the various styles. And then Greg Hio went into detail specifically on signals and RX, and so there was, like, a lot of nice dovetailing, and I really do appreciate when that happens at a conference.

Speaker A
Yeah, that's really great.

Speaker B
Yeah, it's been great. And Melbourne is just the best. Chris, you got to come to Melbourne.

Speaker A
Maybe if this conference is happening again next year, I will remember to plan a trip out there.

Speaker B
There you go. Andy, do you hear that? You got to plan this for next year so Chris can come. All right, cool. Well, I think that's about it for the conference.

Speaker A
Yeah. I don't think I have any other questions or anything to add. I'm glad to hear that your talk, I guess, went well and that it was an interesting conference and that Melbourne is a nice place to spend some time. How much longer are you going to be in Melbourne?

Speaker B
So I leave Melbourne tomorrow. I'm going to a little wildlife tour where we're going to get to feed some koalas and I think pet some kangaroos, which is the most Australian thing I will have ever done. And then I fly up to a town called Cairns, where it's like the gateway to the Great Barrier Reef. So I'm going to go do a little scuba diving, and I'm there until mid next week, and then I'm going to Japan after that. And I'm going to try Swift, japan so I would love to call you again after triswift Japan and have a little conversation about that conference, too.

Speaker A
That sounds great. You know how to get in touch with me.

Speaker B
There you go.

Speaker A
Yeah.

Speaker B
Same battime site, same Bat channel.

Speaker A
Yeah. All right, well, thank you, everybody, for listening. I know this is a little bit different from our usual format, but Seruch is out traveling, and I want to hear about how it's going. And I think that we have collected a number of interesting and useful links in the show notes for this episode. And we'll talk to you next week.

Speaker B
Yeah. As always, Chris, it was a pleasure.

Speaker A
Yeah. Have a good evening.

Speaker B
You too.

Speaker A
Or wait.

Speaker B
Yeah, it's, like five here, so it's 01:00 A.m. In New York or in Arbor, and it's five here, so I feel great. I'm a little jack. Blacks are great by Sergey.

