Speaker A
Hey, everyone. Welcome to Fatal Error. I'm Chris.

Speaker B
And I'm, sirous.

Speaker A
And today we're going to talk about proposing something to Swift Evolution. I didn't realize this, but apparently Sirous has a Swift Evolution proposal. Sirous, tell me about it.

Speaker B
Yeah, I made a Swift Evolution proposal. It is built on top of the ideas of a couple of other people as well, so I don't want to take all the credit. One of them I only know is Richie A, because we're in a slack together and that's the only name that he has. And I also worked with a friend of the show, Caleb Davenport, a little bit on it as well, and there were a bunch of people that gave a ton of feedback as well. I felt like I should shout out, erica Sadun helped. Oh, and Tim Vermulin also helped. So the basic idea is it's a guard catch statement. So, like, today, you have guard let so that you can kind of deal with something being nil and get it out of the way and then exit the scope and then continue sort of on the happy path of a function. This would let you do the same thing, but with a function that throws. So you would say, basically, guard let, my variable equals try, and then some throwing function. And then you would write catch and then open a brace, and then inside of there, you would basically have an error and you'd be able to handle it. That's the basic idea. I'm going to put the pull request for Swift Evolution into the show notes so that people can see it.

Speaker A
Okay. Yeah. I was just going to say, is there a link where we can actually read this somewhere? Yeah.

Speaker B
And then that link also has a link to the thread on Swift Evolution the mailing list, where you can also read the discussion around it there.

Speaker A
Okay, cool. So just to make sure I understand that this is different from saying guard let, some variable equal try question mark, which would just discard the error. This is in a case where you want to try something, but then actually get access to that error if it failed.

Speaker B
Exactly, yeah.

Speaker A
Okay.

Speaker B
So whether you want to wrap that error and rethrow it, whether you want to print it before just returning nil or whatever, whether you want to the way we laid it out, you can also catch a pattern match. So if it's like this kind of error, you can handle it in this way, whereas this kind of error, you might just want a fatal error because you know that case should never happen, and you really want to know when it does. So you could pattern match on it and gives you a lot more flexibility in dealing with it. And all that is flexibility that you lose if you do try question mark or try bang.

Speaker A
Right. That makes a lot of sense. Okay. And then the only other way that you could achieve this with current Swift is to say, like, declare your variable up above, which you can still do with a let and then write your try.

Speaker B
Right. So the way you would do it in current Swift, you would have to write do and then you'd have to have the let above and then not assign it to anything. And then you would have your do and then you would call the function and assign that variable that you declared but didn't give a value to above. This is very confusing. And then call that and then in the catch block, as long as you return from that, it will let you use that in the main body of the function. But it's like really unwieldy.

Speaker A
That's really verbose.

Speaker B
It's not great. So I looked through all the places that I'm actually using error handling in my iOS and in my server side projects, and pretty much all of them I could just completely replace with Guard Catch. Like I would rather write Guard catch than do catch in all of those cases just because it's one line. By using Do, I have to create this extra level of nesting that I would rather not deal with if I could. And this gives you pretty much all the same expressivity, but just with way simpler syntax, basically.

Speaker A
Yeah, that makes a lot of sense. I was pausing early because I forgot that it's not called a try block in Swift. It's do. I've been writing Python recently where it's try nice.

Speaker B
Which also fun fact, you can have a do with no catch in Swift. That is the way that you just create a new scope.

Speaker A
Yeah, that's a nice trick to know about.

Speaker B
Yeah, it's a cute little thing you can use.

Speaker A
Yeah. And objective C did that with just the like open and closing braces too, right?

Speaker B
It was called like a GCC. Was it called like a trick of some sort?

Speaker A
Yeah, I use that occasionally. Fun times. Remember objectivity?

Speaker B
Yeah. Do I ever?

Speaker A
Okay, so it looks like you opened this poor request when? A few days ago? A week and a half ago.

Speaker B
A week ago, I think. Yeah, something nine days ago.

Speaker A
I don't follow Swift Evolution email list. So maybe do you want to walk me through how did this start and what discussion happened on the email list and what's the process been like up to this point?

Speaker B
Yeah, so I also don't follow Swift Evolution. It's way too much stuff and there's just no reasonable way for me to try to get through it all. So I only pop in there when somebody leaks to something or says, hey, this person is saying that that and if you want to chime in, now would be the time. So what I do with Swiss Evolution is I basically am subscribed to it and then I archive all the emails automatically so that I can search for them and reply to them if I need to, but I don't read it regularly because it's way too much stuff. So the process of this basically is and it's nice to go through the process just to have a sense of have the feeling of what is it like to do. The process is essentially you kind of have this format, right? And I think everybody's sort of seen this format where it's like at the top, it's got this block of like, here's the proposal ID. Here are the authors, here's the status, here's a review manager. It's like an introduction, a motivation, detailed design, and then alternatives considered. All these sections are kind of like or impact on existing code is another fun one. So all these blocks, this is like basically a template. So you copy this template and then write your proposal. What I did first was I kind of bounced it around a couple of friends and said, like, hey, what do you think of this? And those friends people that I mentioned earlier helped me nail down like, okay, what happens in this case? What happens in that case? Did you consider this, did you consider that? And that was actually where a lot of the alternatives considered sections came from, is like, well, sometimes they change my mind and I changed the body of the proposal itself. But if one of the fundamental ideas doesn't change, like, one of these alternatives, then I would add a section and say, like, we also considered this and we don't think it works because of X, Y and Z. We also considered that and we don't think it works because of A, B and C. And so that section is pretty rich in here just from basically asking people about it. So sort of after a week of that, then I posted it to the mailing list itself. So to do that, I mean, it's pretty free form, but I think the standard sort of Idiom that you would use is you kind of have like an opening bracket and then you write pitch and then a closing bracket and then the name of your pitch, in this case like guard, catch. And then you kind of do a short one paragraph summary of what you're trying to pitch and then maybe a link to a gist of the thing that you want to propose, like write this thing that you wrote from this template and then you just kind of let people duke it out. You jump in when you want to. People had some interesting feedback. One of the interesting things is that maybe I could dig this up for the show notes, but Chris Lattner proposed that if you has posed this syntax but minus the word guard, so you would just type let thing equals try throwing function catch. And then you would just have to know that that catch has to return interesting. So I added an extra section. Once I learned about that, I added an extra section of this alternative considered. And I was like, I don't think that's really good because I think guard the meaning of guard is like, hey, this situation better be the case. If it's not, you have to exit the scope. And I think guard is like, that's the meaning of guard. And so I really wanted to preserve that. But yeah, so that was like one of the piece of feedback that came out of it. There were a few others. There was a lot of discussion around basically how to handle a function that both returns an optional and throws an error. Right. And if you think about it, it's kind of weird because you don't really have guard else anymore.

Speaker A
Interesting. Yeah.

Speaker B
Or you could you could like try to make them all into one statement where you could do guard let thing equal, whatever. Yeah, but that's going to and catch just weird.

Speaker A
Yeah, I'm kind of reading through the proposal right now, but how did you end up resolving that?

Speaker B
So the feeling that I had was that guard catch should just be a totally separate thing than guard else, because Elf doesn't necessarily say that it's like the Nil case of the Nil case of an optional. So if it were like, guard let value because whatever, catch this and then on Nil do that, then I think I would like, obviously that doesn't sound very swifty, but something like that I think would be much more clear than else else to me, doesn't necessarily mean that we're dealing with an optional. So the thing that I proposed is that if you come up against this edge case often, you can add a function to optional and that function is called unwrap. And then it either throws or returns the thing on the inside. So that way you can kind of hoist an optional into the world of throwing functions. And so your catch will just catch everything. And then you could do catch let error as nil error. And then you would be able to handle the Nil case separate from the rest of the errors.

Speaker A
Okay. Think that makes sense? Yeah, I'm trying to think of like I guess there's no really elegant way to handle that because you're kind of overloading this guard let syntax.

Speaker B
Right, right. It's mixing monads and mixing monads is always dangerous. Like, if you have an array of optionals, that's weird. If you have an optional of arrays, that's weird. If you have a function that returns an optional and throws, it's weird. And so on.

Speaker A
Yeah, you have a burrito of burritos, that's weird.

Speaker B
Yeah, you don't want burrito of burritos. It's not good.

Speaker A
So you're not proposing, though, that that optional function be added to the standard library or to all optionals or that seems like probably overkill for this case.

Speaker B
Exactly. So I wrote that adding this is out of scope. So while the inclusion of this extension in the standard Library is beyond the scope of this proposal. Adding it to a project is easy. So I do think it's a good thing to add to the Standard Library. I just don't think it's a good thing for this proposal to propose. Like, it's totally orthogonal, basically.

Speaker A
Yeah, I can see that. Okay, after you got some feedback from the pitch email chain, what's the process for actually putting this into the Swift Evolution GitHub repo or opening a pull request for it?

Speaker B
Right, so the feeling that I've gotten is basically if the feedback from your pitch thread is mostly positive, then at that point you say, okay, it's time to make a proposal with it. It's time to make a pull request with this actual proposal. So then you sort of fork add your thing. You don't know what number it's going to be, so you just put, like, XXX or NN, and then you basically open up a pull request with this thing. They're a little bit backlogged on pull requests right now, which is probably pretty stressful for them. They have 16 open pull requests for draft proposals and stuff.

Speaker A
That's a lot these aren't like yeah, it's not like a software project where some of the pull requests are just one line fixes. Like, this is something that requires a lot of attention and a lot of resources.

Speaker B
Well, and each one of these has an official review period of one week. Yeah, and some of them look pretty official. So, like, Airspeed Swift, the Airspeed Velocity guy, Ben Cohen, works at Apple, and so he's an Apple employee who has an open poll request since April 8 for removal. I don't actually know what this does, but the point is there's a lot of open poll requests. That's just kind of how it is for now. I'm not worried about it. I don't think that this is something that obviously wouldn't make Swift Four. I would honestly be surprised if it made Swift Five because it's pretty much just syntactic sugar and they have bigger fish to fry.

Speaker A
Yeah, I guess I don't remember what they've set are the priorities for Swift Five, but it doesn't seem like something that would be too complicated to add if they decide they want to add it.

Speaker B
Yeah, I tried to reuse as much of the system as I already could in the thing, which I actually didn't know this. So if you write, like, do whatever in braces, and then you write catch and then open a brace, the variable error is actually implicitly bound for you. So you can use the variable error and it's bound to the error without writing Catchlet error, which I didn't realize. That was one of the things that I had to change in my proposal when I realized that's how the default behavior works in Swift. That was one interesting thing. So I tried to keep it as much like the current catch syntax as I could, so they could reuse that or whatever and just so it's also cognitively easier for people to use. But yeah, honestly, the experience of creating a proposal has been interesting enough that that was already worth it for me. If it actually gets approved, even if it gets deferred, that would be really awesome. I'd be super happy with that outcome.

Speaker A
Yeah, that's awesome.

Speaker B
I don't even know if it would make Swift Five is kind of what I'm getting at, but maybe at some point they'll go through these proposals, open the review period on each of them, and people will be able to discuss if they think it's a good idea or not.

Speaker A
Yeah. So you're just sort of waiting now for a review period?

Speaker B
Yeah, I think I've actually done everything that I will do for this. I don't know that much more about the rest of the process, but they'll make a thread, soliciting feedback for it. I guess I can put another argument in there of why I think it's good, but I've kind of made my argument and then it's kind of like I can't implement it. This seems crazy. Somebody else is going to have to do that part. I've let my thing out into the world and hopefully it turns into something beautiful.

Speaker A
That's awesome. Hopefully, yeah. I don't know if we have that much to say about or I don't think I anyway have much more to say about the Swift Evolution proposal or process, aside from maybe to call out that it's kind of cool that Apple is involving the community this much and this successfully on still a relatively new language.

Speaker B
Yeah, there's definitely a lot of passion on the Swift Evolution mailing list. Like, there are people who have very strong opinions and no, I mean this in a really positive way. It can be overwhelming to look at that stuff, but at the same time, I don't know. It's nice that there's people that care enough to put their time into it. Yeah, it's really good.

Speaker A
Yeah, that's awesome.

Speaker B
And I have strong hopes for Swift for being a language of, as they say, the next 20 years, maybe longer, and making sure that we get those foundations right and discussing them and figuring it out is really important if it's going to be a good language for the long term.

Speaker A
Yeah, it's absolutely worth it.

Speaker B
Yeah.

Speaker A
So it looks like scrolling through the proposal here, it looks like there are a number of design details here and I assume that each of these is addressing some kind of edge case that either you came up with or someone on the mailing list came up with.

Speaker B
Yeah, pretty much. I think only one or two of them are from the mailing list. Most of them are from talking to friends and really fleshing out how this stuff has to work. It's interesting because it was I thought it'd be a pretty simple thing. But once you start thinking about the edge cases, there's actually quite a few of them in Swift today. If you want to use try, you can put it anywhere in the expression before the throwing function. Right. If you want to say, like, you have two functions that each return a number, and you want to add their result. Right. So you say, like, function one, call the function plus function two call the function. If one of those throws, you could put that try before the whole expression, or you could put it before just the expression, just the function that throws. Yeah, that's like an edge case thing that you have to think about. It's like, okay, are we going to allow you to put the try anywhere, or are we going to require that it always be at the beginning? Is one easier to read? Is one harder to read?

Speaker A
I think that you should probably just follow the Swift convention that it could be anywhere in that statement that is supposed to produce whatever result. Right?

Speaker B
Yeah. And I feel like if you wanted to change it, that's a separate proposal, right?

Speaker A
Yeah, I think so.

Speaker B
Yeah. Say, that was, like, one interesting one that came up. Obviously, you can do guard VAR as well as guard let in current Swift. When you're unwrapping an optional, like, if you want that value that you unwrap to be mutable, you can make it VAR. And so should that be allowed? Probably that should be allowed also because it's like this mishmash of two constructs in language already, right. Guard and the do catch, and you want to try to pull the features from each. That makes sense. I thought it would be a simpler proposal than it actually was, and it turns out there's quite a few edge cases to think about.

Speaker A
Were there any other interesting edge cases that you want to call out?

Speaker B
One interesting one is that some functions throw but don't return a value. And so you can put a boolean inside of a guard, it doesn't necessarily have to bind to a variable, right. Like, it doesn't necessarily have to be unwrapping optional. It can be just be checking that some condition is the case. And so should you be able to do, like, guard, try, model, save, and then not bind it to any variable at all?

Speaker A
That seems weird to me. That really feels like it's duplicating the Do Try catch sort of structure.

Speaker B
Yeah. Why do you think so?

Speaker A
I mean, in that case, you just have well, I guess the Do Try catch doesn't say you have to exit the scope.

Speaker B
Right. Although you can exit the scope, and because it doesn't return anything, it has to be a mutant. It has to be a side effect inducing function. Right?

Speaker A
Yeah. It just seems very, like yeah, it's weird, right? Yeah, I guess I'm not sure why. It just really seems like if you're not like the whole point of guard. Yeah, I guess it's.

Speaker B
So if you want to write your own proposal, you Chris or you the audience, I recommend it. I think it's a fun experience, but there are lots of weird things that you're going to run across and you're going to have people that tell you either on the mailing list or your friends or whatever, no, it can't be that way. It has to be this way. This way makes so much more sense. And you're like, well, that doesn't make sense to me. And you just kind of have to pick one, either be convinced or fast, in your opinion. I don't know. The guard with no binding of variables. The guard try with no binding of a variable. It also looks weird, like a really weird series of swift tokens, I guess. Guard, try, model, save, catch maybe.

Speaker A
The only reason that it seems weird to me is that with guard let try, you're saving several lines of verbosity there. Right. And with just guard try throwing functions. Right. You're not saving that much.

Speaker B
It's actually saving characters. Oh, no, that's not true with the spaces. But if you put like, brace, if.

Speaker A
You take the white space out, then it's more non white space characters than just having that do try. Right?

Speaker B
Yes. And you can inline the whole do, brace, try, model, save, close, brace, catch and it would look exactly the same.

Speaker A
Yeah. Is this the first example that we've seen this proposal I mean, the first example that we've seen of try occurring without a dedicated do scope associated with it.

Speaker B
So you can just call like try some function that throws, but the function that you're in also has to be throwing. So you can do that.

Speaker A
Yeah, but I mean, so someone down the road has to either have that scope that's defined with the do catch or use try bang or try question mark.

Speaker B
Yes. Eventually down the road, you have to do one of those three things. There's no other way.

Speaker A
So this guard let or just guard try syntax is almost introducing that getting rid of the need for that scope in a different way. Yeah. There's an interesting proposal.

Speaker B
Yeah. I like it because it's a nice one to do first. I hope I do more. I don't know if I will, but it's like a very softball one. Everybody kind of agrees it's a cool thing to add to the language. The only question is, is it worth the priority of doing it? And so it's not like something where I have a really strong opinion about the language will work this totally different way and nobody's going to agree with me. It's like a pretty straightforward thing that more or less everybody thinks is good, notwithstanding the details on whether you have to bind a variable or not. Which I'm glad we did find something to disagree with about this proposal.

Speaker A
Yeah. I don't know how strongly I disagree with you.

Speaker B
Yeah. And I see where you're coming from. Right. It's just really not that much better than just do. If you've in mind to do it's just pretty much the same.

Speaker A
Yeah.

Speaker B
Interesting. Do you have anything that you would ever propose to the mailing list?

Speaker A
No, nothing comes to mind immediately, honestly.

Speaker B
Yeah, we got to get you writing more Swift. That's what we got to do.

Speaker A
Yeah, we'll see. Maybe after I learn more about Swift on the server, maybe. We'll see.

Speaker B
Yeah. There you go. Write some Swift scripts.

Speaker A
Yeah.

Speaker B
User bin Swift.

Speaker A
You joke about that. I could see that being really useful for some of the sort of one off things that I'm doing. Like, Swift is a nice language to work in for some of this stuff. That shell scripting is just terrible. And I mean, Python works, but it would be cool to use Swift for it too, just because why not?

Speaker B
Yeah. And you're familiar with standard library? You're familiar with building abstractions quickly. Could be good.

Speaker A
Yeah, absolutely. Although it could also be good just to exercise my Python and work on getting quick at using write good abstractions in Python too.

Speaker B
Yeah, that's fair too. Cool. Yeah. So swift evolution. If you're thinking about something to propose, I think you should propose it.

Speaker A
Yeah, I would agree. And I really don't have anything else to add here, so I guess we'll say thank you very much for listening. We should note that we do have a Patreon, so if you're wondering where all of our even numbered episodes have gone, they're on Patreon and there will be a link in the show notes. Our Patreon supporters help us pay for editing and hosting costs for the show, and we really appreciate the support.

Speaker B
Yeah, totally. Last week on the Patreon feed, we talked about going to conferences and writing blog posts and writing talks and how all those things kind of come together, and that was a pretty fun episode to do. So if you're interested in listening to that, definitely hop over to Patreon and become a patron and help us with our hosting fees and our editing fees.

Speaker A
Yeah, that was definitely a really interesting episode to record. We, I guess, should note you're going to be speaking at 360 IDV in, what, a week from when this episode comes out?

Speaker B
Yes, a week from when this episode comes out. Almost exactly. Cool. So hopefully I'll see some of you all at 360 IDEV. Come wave. Say hi.

Speaker A
Yeah, I won't be there, but say hi to Syria.

Speaker B
Cool. I will talk to you next week.

Speaker A
Chris, I'll talk to you later.

Speaker B
Fantastic. Bye.

