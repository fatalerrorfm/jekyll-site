Chris Dzombak
My life's so hard.

Soroush Khanlou
Yeah, it sounds tough. Maybe you should get a whole different computer for broadcasting. Maybe that would be a solution.

Chris Dzombak
Yeah, maybe. My keyboard on this one. You know, it's I've had the computer for, like, three months, so you know, the keyboard's starting to go bad. The the GMP keys now don't don't work.

Soroush Khanlou
This is the aMacBook Pro, a top of the line new Apple computer.

Chris Dzombak
This is a $3500 laptop that I got in August or September of last year.

Soroush Khanlou
Yeah, not great.

Chris Dzombak
And I use external keyboards, like, 80% of the time, so it's not even like I've been pounding away on this on the laptop's keyboard. Like, I rarely touch it, but, like, there yeah, I just look at it and it and, like, it breaks.

Soroush Khanlou
I've heard so many horses. I've been mercifully spared from the keyboard horrorsters, but I have heard so many. Just awful.

Chris Dzombak
It's so bad. I do not know how Apple shipped this.

Soroush Khanlou
I mean, maybe they tested in pure white rooms with no dust. They're testing them in clean rooms.

Chris Dzombak
That's like, the only possible explanation.

Soroush Khanlou
Yeah, man, I don't know. Not great. I do have one question, though, which is semi related, which is every single one of this generation of laptop that I've seen in the wild is a space gray one. Has anybody bought a silver one?

Chris Dzombak
You know, that's a good point. I don't think I've seen a silver one either.

Soroush Khanlou
Is it because the silver one looks like the old model, so you wouldn't notice it? I feel like the back is different. Like, the little apple doesn't light up anymore and the touch bar seems obvious.

Chris Dzombak
Yeah, I mean, that's a good point. I think the space gray just looks better.

Soroush Khanlou
I think it looks so much better.

Chris Dzombak
Looks so good. If only it worked. Yeah.

Soroush Khanlou
The space gray isn't the same color as the imac Pro.

Chris Dzombak
It is not.

Soroush Khanlou
I'm asking. I don't know.

Chris Dzombak
Oh, I have no idea.

Soroush Khanlou
I think the imac I don't know.

Chris Dzombak
Is it the same as where's my iPhone? My iPhone x ten here. This is definitely a different it's very different. Which I guess makes sense since the phone is not aluminum.

Soroush Khanlou
Yeah.

Chris Dzombak
I don't know. Now I have alias GGIT to just get in my shell, because sometimes when I hit the G key, I get two G's and sometimes zero. And now the same thing is happening with a B key.

Soroush Khanlou
Well, you should also alias it just in case the G key doesn't work.

Chris Dzombak
That is true.

Soroush Khanlou
Just think about that.

Chris Dzombak
Usually it gives me two instead of one. Yeah, it's incredible. It really is.

Soroush Khanlou
Just that's really too bad.

Chris Dzombak
Yeah.

Soroush Khanlou
I don't know what I think about mine. I mean, mine mercifully, like I said, has been working. I kind of wish I stuck with 13 inches. I feel like 15 is just too many inches.

Chris Dzombak
I love my 15 inch. I think it's a good just doing stuff on a 13 inch laptop just seems so it's too cramped.

Soroush Khanlou
That's right. And this is your primary computer, right?

Chris Dzombak
Oh, yeah. This is like my computer. I connect it to monitors at home and at work to work on it. But I mean, if I'm taking it places and working like I'm working on the 15 inch screen.

Soroush Khanlou
Yeah, that makes sense. Mine is more of a secondary computer because I have an imac in the house.

Chris Dzombak
I see.

Soroush Khanlou
And actually the imac from 2012 is so fast that this MacBook Pro, this new space, gray, whatever, has finally caught up to it in speed.

Chris Dzombak
Nice.

Soroush Khanlou
From 2006.

Chris Dzombak
Now the IMAX are really good. My thing is I got so tired of trying to change a keyboard shortcut on one thing and then I go to use it on the other and it's not in sync and I have to keep files in sync and I'm just like, it's too much effort.

Soroush Khanlou
Yeah, that's not great.

Chris Dzombak
No. I want one system to maintain like four servers for personal projects. Those don't change as often.

Soroush Khanlou
Speaking of servers, my server is all set up.

Chris Dzombak
Awesome. That's good. You got it locked down?

Soroush Khanlou
Yeah, everything is locked down. As far as I know. I'm still not doing SSH login.

Chris Dzombak
You mean public key only login?

Soroush Khanlou
That is what I mean. Yes. Public key. Like a full 128 bit key or whatever. I'm still not doing that. I probably should, but I've been lazy. And then the other thing I realized is I don't have Https set up. So I got to figure out remind myself how to do that. So that's also on the list.

Chris Dzombak
Are you using let's encrypt for Https or something else?

Soroush Khanlou
I'm not using anything.

Chris Dzombak
Okay.

Soroush Khanlou
I forget how I did it on my old server. I'm pretty sure I did do it, but I forgot how I did it. I don't know if I did it, if I paid for one or what. But I did something.

Chris Dzombak
I've been meaning to write a guide to setting up let's Encrypt plus NGINX on a server.

Soroush Khanlou
Let's Encrypt is the free one, right? That's pretty cool.

Chris Dzombak
Yeah, and it works really well. I got an email today, actually, that two of my certificates had been renewed and were installed. And I went to look at the website and it was a new certificate that was there. Didn't have to do anything.

Soroush Khanlou
That's pretty incredible.

Chris Dzombak
It is pretty nice. It's still kind of finicky to get it working, but maybe I'll try and write this blog post even before this episode comes out, in which case I will put it in the show notes. That probably will not happen, but when you get it working, it really is. It's slick.

Soroush Khanlou
That is pretty tight. Yeah, I definitely have to do that because I don't want Comcast inserting any whatever's into my page. Not interested in that.

Chris Dzombak
Yeah. Okay. So let's pop the stack a little bit. You've got honestly. You have disabled root login for SSH, right?

Soroush Khanlou
Yes. Although I don't understand how that makes anything different. Well, except that they have to guess your username and your password. Right, but isn't that the same as just guessing a longer password?

Chris Dzombak
Kind of, yeah. Except that I think most of the sort of dragonet brute force attacks are just like looking for root plus random, just fairly easy passwords. I don't know that anyone is running a bot that is guessing usernames, although I'm sure that exists. But you are also running Fail to Ban. Right?

Soroush Khanlou
I am running Fail to ban, and I'm running it slightly differently than the recommended settings.

Chris Dzombak
Okay.

Soroush Khanlou
The way I set it up was if you try to log in 100 times and it fails, then you're banned for ten days.

Chris Dzombak
Oh, wow. Usually it's like if you try to log in like six times, you're banned for a much shorter period of time.

Soroush Khanlou
Right, right. The reason I have it set up that way is because I could imagine myself accidentally typoing six times. Probably won't happen, but I could imagine it. I cannot imagine myself typoing 100 times.

Chris Dzombak
By typoing you mean copying pasting a password from your password manager?

Soroush Khanlou
Yes. Or maybe you copied the wrong one. Like I copied the root password instead of the SSH user password or something like that. I could imagine it happening six times. I can't imagine screwing that up 100 times. So I'll never hit the lockout because 100 times of mistying a password would be pretty rare. But then when that does happen, that means it is a brute force attack and I could just lock them out for a very long time.

Chris Dzombak
Yeah, that makes sense.

Soroush Khanlou
And I kind of calculated, like, how many brute force attempts someone would get with both schemes. And you end up with a lot more opportunities to guess the password over the course of ten days. If you do it where it's like you typo for six if you type the password incorrectly six times and it blocks you for five minutes. Okay, so that's what I ended up doing.

Chris Dzombak
Nice. Well, that's pretty interesting. Probably. That sounds like a pretty good set up.

Soroush Khanlou
Probably will work.

Chris Dzombak
I have to imagine you'll be pretty good here.

Soroush Khanlou
Oh, and it's supposed to email me, although I need to test that because I installed send mail or whatever, and I couldn't really get it to work, so I need to double check that.

Chris Dzombak
Okay. Yeah. I usually have installed postfix on my servers and you tweak it so that it only accepts connections from the local host and it'll send mail and that works pretty well.

Soroush Khanlou
Yeah. And the other thing I'm really happy about is I made an image, so if I do get hacked again, I can just deploy that image instead of having to go through all this rigamarole again.

Chris Dzombak
That's nice.

Soroush Khanlou
So I'm very excited about that as well.

Chris Dzombak
Cool.

Soroush Khanlou
Yeah. So if you go to my blog, if you've tried to hit the tag pages or you've noticed something's weird about some stuff that was a problem from the last few months and now it should be resolved and blocks should be fully back to normal. Oh, the other cool thing I did is I made it so when I get pushed to it, it runs jekyll so I don't actually have to render it on my side. I can just push the raw changes to the markdown files and it will render it for me.

Chris Dzombak
That is nice. I've been doing just to render locally and our sync sort of workflow, but either way it works. That is nice to have set up on the server.

Soroush Khanlou
Yeah. The reason I was excited about that was because it would mean I can use working copy on my phone to make quick edits and then just push the edits up. That is my hope. Yeah.

Chris Dzombak
Cool. What do we want to talk about that's on topic today?

Soroush Khanlou
I'm open to a bunch of things. What do you feel like talking about?

Chris Dzombak
We could finally do a bunch of we could talk about Swift enums. We could talk about the Swift forums.

Soroush Khanlou
The enum thing sounds like a pretty cool idea. Maybe we can talk about Enums and the Swift Evolution forum at the same time and then if that works for you.

Chris Dzombak
Yeah, that sounds great. Swift forums, they announced this like ages ago, right? I don't even remember when I think I was still an iOS developer then.

Soroush Khanlou
I feel like it was more than a year ago.

Chris Dzombak
I think that's true. Yeah. And I mean, I know that everyone on the team has a lot on their plate, but I have created my account on the new discourse based forums and subscribed to notifications for a couple of the announcement areas and I haven't used it a lot beyond that, but I've got to say this looks really nice.

Soroush Khanlou
Yeah, I am very much enjoying it. I also made my account and I actually made a topic as well, which went interestingly. I don't know if you saw it.

Chris Dzombak
No, I didn't. You want to link me to that?

Soroush Khanlou
Yeah, sure. I'll throw it in the show notes and slack it over to you.

Chris Dzombak
I guess I should open these show notes and slack on my computer.

Soroush Khanlou
I mean, either one. So what essentially happened here was one of the things that I think is a limitation of the kind of sequence and collection system in Swift is that some sequences are single pass only, which means if you run through them again, like if you iterate through them, you get the values. If you iterate through them again, you may get no values, you may get different values, or you may get the same values.

Chris Dzombak
Yeah.

Soroush Khanlou
So that makes writing some algorithms a little bit tougher. So one example of an algorithm that you can imagine is each pair I talk about the each pair algorithm a lot, but basically if you had the numbers 1234 in an array, the pairs would be one and two together, two and three together, and then three and four together. And it's a super useful algorithm for like if you have a bunch of, let's say a bunch of UI views and you want to install a constraint between them, you can call, like, my Views each pair, and then it gives you two pairs together as a tuple. And then you can install a constraint between those two. And then you don't have to do that dance around. Okay, well, let me get the index and then do index minus one to get the previous element. You don't have to do that anymore, it just kind of handles it for you. So when you write that algorithm for a multi pass sequence, it's real easy. It's just a zip and it's like a one line thing. So it's really easy to write it for a multi pass sequence. But because not all sequences are multi pass, you have to basically, when you write this algorithm, handle the fact that sometimes there may be single pass sequences. So the way you do that is you hold on to the first item, then you uncue the second item, put them together, and then iterate that and then get the third item, pair it with the second item and so on. It's a little bit tougher to write, it's a lot more code for sure. You could check in the thread if you want to see my implementations. And the reason that we have this single pass requirement when we're dealing with sequences is for a vanishingly small number of edge cases. So one of them is randomly generated numbers or randomly generated anything so that's one another one is sometimes people use sequences to read from sources that are transient. So if you read from the network, for example, so that's another case. And then there are some cases where there's one particular case in the standard library where both the sequence and the iterator are the same object and it's a class. So when you get the iterator to iterate through it and that's like mutating as you iterate through because the iterator is kind of a destructive cursor, you're also destroying the sequence at the same time. Which I don't understand why that code is written that way, but it is. And so there's a couple of these edge cases and they seem to me like not worth muddying the water of the line that separates sequences. And iterators in my mind, which is that sequences represent a series of things and iterators represent a destructive mutating cursor through that series of things. Sure, if you have something that's naturally destructive, it should just be an iterator. So if you have a cryptographically secure random number generator, for example, you should be able to as you DQ items off of that if you can never get those items back, which means it couldn't be a sequence, then it should be an iterator. And that way we can maintain this really clear separation between these things are destroyed as you use them and these things are not destroyed as you use them.

Chris Dzombak
Okay. Yeah. That seems like a useful distinction to capture, just offhand.

Soroush Khanlou
Yeah. Instead, the current setup is that you basically have iterators are always destructive and sequences are almost always not destructive, but in some very rare cases they are. And so when you write code that deals with sequences, you have to deal with the single pass, the potential single pass ones that are out there, which is kind of frustrating. So I basically kind of pitched, I was like, hey, what if we just got rid of these? And it was not very well received at all.

Chris Dzombak
Yeah. Not reading. I've been kind of skimming through and it generally seems like people do not like this suggestion.

Soroush Khanlou
No, they really don't, which I was a little bit surprised by. But it's a community that is a thing that they kind of play. And it's four years into the development of Swift publicly or like, once it was announced. And it's probably pretty late in the game to change this kind of thing, even if it is a small change. So I respect that, but it seems like a good change to me. But a lot of people didn't agree, which is fine. So that was my first thread on the new Swift Evolution forums.

Chris Dzombak
Yeah. So I'm coming at this without actually having read this thread since you just linked it to me. One thing that stands out is someone in this thread pointed out that I'm not sure which side he's on, but the sequence protocol has a syntactic, meaning that instances can be iterated with a for in loop. Yeah, that okay. It looks like he's kind of agreeing with you. But there's a case that comes up in a few different APIs where some basically implementation detail ends up breaking an API contract. Right.

Soroush Khanlou
In this case, the contract is that you can only assume that a sequence is ever iterable once.

Chris Dzombak
Okay.

Soroush Khanlou
Yeah.

Chris Dzombak
And so if you are going to need to use the sequence more than once, you're responsible for implementing some sort of buffer.

Soroush Khanlou
Right, exactly. You would basically so the way, like, let's say, sort works is because you need to read items multiple times. The first thing it does is if it's not the right type to be mutated, which I think is a mutable collection, it will actually copy everything to an array first and then begin the sorting process.

Chris Dzombak
Okay. Yeah.

Soroush Khanlou
And that's your responsibility. So a really good example people brought up in this thread was Cartesian Products, where you would say, I have these two sequences, I have these two arrays, and I want a new array, or whatever. I knew something that represents each combination of these things. So if you imagine it being like a big grid with the values of one array on the top and the values of the other array coming down the side, each of those little boxes would be one combination of those two arrays. And so the problem is that one of those usually the way you write that is like nested for loops. Right. And the problem is that inner for loop is going to require you to be multi pass and finite, but it requires you to be multi pass and if it's not multi pass then you'll iterate through the yeah, so you'll iterate through and then you'll just get like garbage values at a certain point. And so that's a really good example of something where you would have to copy if you're dealing with sequences, you would have to copy it all to an array and then iterate over that array, which bears some cost. But I think the randomness stuff is really important and I do think some people are writing code. Like somebody mentioned packets which I didn't really fully understand, but I think they're writing code that is like reading from the network using a sequence.

Chris Dzombak
Interesting. Okay, that seems like I'm curious why a sequence is the best API to use for that, but I guess I could see that being useful.

Soroush Khanlou
Yeah, I would model it as a stream or as a signal or whatever.

Chris Dzombak
But I don't feel like sequence is really a good general purpose like stream abstraction.

Soroush Khanlou
Yeah, but either way, that is kind of where that topic landed. I'm going to try not to let this sort of dissuade me from posting more in the future, but this is my first thought. I've actually been waiting until the forums were rolled out to actually write this.

Chris Dzombak
So setting aside the reception of this pitch, the experience using the forums was positive, I assume.

Soroush Khanlou
Generally positive discourse is very nice. They brought back all the archives so you can search through the archives, which is really nice. A lot of super good stuff there. The one thing I will say is because it's easier to post now, sometimes people get lost in little tangents.

Chris Dzombak
I'm noticing that skimming through your conversation here too.

Soroush Khanlou
Yeah, there's a really funny thread where basically someone wanted to add filter to optional, right. So you would basically return true or false. And if it's false, the optional is transformed to nil and if not the optional stays the value that it is seems useful enough. Right, but then they got onto this weird digression about well, if we're like mammals with body hair rats in this thread. Yeah, if we're being pedantic, all mammals have body hair. And then there was multiple posts about mammals and body hair and naked ball rats and it was just like.

Chris Dzombak
It.

Soroush Khanlou
Was quite a tangent.

Chris Dzombak
And this kind of thing you think didn't happen so much on the mailing list because it? I don't know, seemed less like it was like a higher friction interaction.

Soroush Khanlou
Exactly. Yeah. I think still worth it. Still the right thing to do.

Chris Dzombak
Yeah, definitely.

Soroush Khanlou
But ultimately, with forums like this, I think you need some level of moderation. I think that's something they're maybe still figuring out. And I mean, some degree of tangents should be allowed, but this thread got really funny really fast. And it's one of those things that if you've been on the Internet for a while, if you've seen these forums, they do devolve into, like, well, I think Hitler would have done this. Yeah.

Chris Dzombak
I mean, that's not to say that can totally happen with email lists, too.

Soroush Khanlou
Yeah, that's true. But I think that's the only real downside I see. Other than that, I think pretty good move discourse is really nice to use. It's much easier to keep up with stuff. Easier to subscribe to things that you care about but ignore things that you don't. Easier to skim. There's like markdown formatting for code. There's a lot of good stuff in it.

Chris Dzombak
Yeah, that's really awesome. I'll read through your pitch and the conversation in more detail, and maybe we'll talk about that more on an upcoming show or maybe not at some point. We had thought about doing just a sequence and collection episode, I think. Right.

Soroush Khanlou
Did we never do that?

Chris Dzombak
I don't think we ever actually did it.

Soroush Khanlou
We didn't. Okay, well, that's a good idea. We should do that in the future.

Chris Dzombak
Put that on the topic ideas list here.

Soroush Khanlou
There you go.

Chris Dzombak
So, enums. There have been a couple of discussions on Swift Evolution about enum related things.

Soroush Khanlou
Yeah. So there were two big ones, right? There was one was, should we allow nonexhaustive enums? And then the other one was, should we allow like, an all values for certain enums?

Chris Dzombak
Right. And these were proposals, 192 and 194.

Soroush Khanlou
We'll pop those in the show notes.

Chris Dzombak
Yeah. So maybe going in order, there was a proposal for nonexhaustive enums, which is basically it's an enum that you're allowed to add cases to in future releases of your API. Right?

Soroush Khanlou
Right. So the whole problem here is essentially if, let's say I'm writing code that links against some library, and the library has some subset of some enum that has like three values in it, and I make an exhaustive switch statement that has those three values. And let's say with those three values in each case, I return something for my function.

Chris Dzombak
Right.

Soroush Khanlou
Now, if that library changes and adds a fourth value, and then my app gets linked to that new version of the library with the extra case, when my code hits that exhaustive enum where each of those three branches were returning something, I still have to return something from that. I have to do something at that point. So my options are either crash, basically, or I have to have known ahead of time that, oh, there may be cases that were added to this that will be added sorry, to this enum. And I need to write a little bit of code to handle that situation. So that would be it could look like it could be like default. It could be like a future where you would just write a future colon and then handle the case of any Enums that you haven't seen in the future that you haven't seen yet that.

Chris Dzombak
May come in the future.

Soroush Khanlou
And so you may just choose to fatal Error at that point.

Chris Dzombak
Or hey, that's the name of the show.

Soroush Khanlou
You could or you could write code, let's say return empty string. There are certain defaults that you could return or do something.

Chris Dzombak
Sure. You pick something that makes sense in context.

Soroush Khanlou
Exactly.

Chris Dzombak
So what happens now if you're using a library in your application and the author wants to add something to an enumeration, you won't be able to compile your app against that newer version of the library. Right.

Soroush Khanlou
So right now, because Swift only supports static libraries, you don't really have to worry about it.

Chris Dzombak
Right.

Soroush Khanlou
The only libraries that can change are app kit and UI kit. And I think foundation basically like those libraries may change as the phone gets updated. And if those happen to add a case, I think the Swift runtime has no choice but to crash at that point.

Chris Dzombak
This is really the case today with what happens in real Swift apps.

Soroush Khanlou
Oh, sorry. There is actually one other option. It can return garbage memory.

Chris Dzombak
Oh, that's like the least Swifty of these options.

Soroush Khanlou
Yeah, exactly. So, yes, today, if UI kit did add an extra case, something would happen.

Chris Dzombak
I guess that's true. I'm skimming through the proposal again here. I don't know if it discusses what happens.

Soroush Khanlou
I think at this point it's undefined behavior.

Chris Dzombak
Yeah.

Soroush Khanlou
But I think the correct thing to do would be to crash.

Chris Dzombak
Unless this yeah, that's the only correct thing to do.

Soroush Khanlou
What they wanted to do was they wanted to make enums nonexhaustive by default. Public enums nonexhaustive by default, meaning that.

Chris Dzombak
The enums your library exports, that clients who are using those would be required to have a future or a default statement in addition to all the case statements that handle each value of the enum that we know about. Now.

Soroush Khanlou
Exactly. Right. And then if you wanted to opt out of that, you could add like at Frozen or at Exhaustive or something to mark your Enum as saying this is never ever, ever going to change.

Chris Dzombak
Right.

Soroush Khanlou
So you can imagine, like optional is an Enum that is never ever going to change. They are never going to add another case to optional.

Chris Dzombak
There's like a Quantum or Schrodinger's cat joke here, but sure, yeah.

Soroush Khanlou
So they're never going to change that. They can freeze that. But then something like and like days of the week, assuming grow grandkid, blah, blah. Also never going to change. Sure.

Chris Dzombak
Something like if you had a color picker library, like, you can easily imagine adding more colors that a user can pick.

Soroush Khanlou
Right, absolutely. Yeah. That's a great example. And so for things like that, those things you would just leave as is or you could add like nonexhaustive as a special keyword. Now, the interesting thing was that the feedback to this was very, very strong.

Chris Dzombak
Strong in which way?

Soroush Khanlou
Mostly negative.

Chris Dzombak
Really?

Soroush Khanlou
Yeah.

Chris Dzombak
Why? How?

Soroush Khanlou
I think a lot of it stemmed from the fact of there was a couple of one component was the fact that it was nonexhaustive by default. And so I think people kind of were triggered and they were thinking about the open versus closed classes, final classes. I think they were kind of reminded of that situation and there was that component of it. There were also people who were saying like, this is not going to solve the problem of binary compatibility, so okay, let's just not do it at all. Essentially was the argument which I'm not giving it a fair shake because I don't agree with it, but essentially the idea was like, if you're writing a library, it's your responsibility to make sure that your library's behavior doesn't change except on, let's say, major version updates, assuming you're using.

Chris Dzombak
Okay. I mean, so sure, it's your responsibility, but what's the problem with putting in place tools to help you?

Soroush Khanlou
I am not sure. I don't know. But yeah, people it's also your responsibility.

Chris Dzombak
Not to dereference no pointers in C and get all software written in C is horrible.

Soroush Khanlou
Right, that's a perfect example. And I think you would want help from the compiler where you can get it. And also most of the people who were talking about it were people who write apps that they're not necessarily exporting modules for other people to use, so they wouldn't really have to worry too much about it.

Chris Dzombak
That's one thing that's striking me is this really only affects a small number of authors and a small, relatively small number of lines of code. Like, this affects people who are writing libraries that export public enums, which are fairly rare.

Soroush Khanlou
Yeah, I mean, they're there but yeah, there's not like millions and millions.

Chris Dzombak
No, this doesn't seem like a change that touches a huge number of lines of code.

Soroush Khanlou
Yeah. So one thing that people recommended was instead of doing this, why don't we change the UI kit export layer and instead of exporting UI kits, C enums as swift enums, let's export them as swift structs that are backed by, let's say, an integer. And then the only way that you can construct them are with static methods that have the same names as the enum cases.

Chris Dzombak
That seems kind of ugly, but in.

Soroush Khanlou
Practice it would look exactly the same, except that you would no longer be able to exhaustively switch over it and so it would be force you to add a default case.

Chris Dzombak
Okay.

Soroush Khanlou
This was a solution some people like.

Chris Dzombak
But that's not a general solution here.

Soroush Khanlou
Yes, but also the Enum exhaustive enums isn't a general solution.

Chris Dzombak
Isn't it solution for binary compatibility or for this specific problem?

Soroush Khanlou
Even this specific problem, because you could just put exhaustive and then change it in a future version.

Chris Dzombak
Sure, but I mean, you could unwrap optional. Yes. At some point you can do something like stupid and ignore a warning.

Soroush Khanlou
Yeah. I still think this is a good change, and I think the core team also thinks it's a good change. So I think it's one of those things that's going to happen no matter what.

Chris Dzombak
Okay. This is going to be one of the cases. I mean, this should surprise none of our listeners where I think this seems like a good change and think it should be accepted.

Soroush Khanlou
Yeah, I agree. I like this change. I think it makes total sense. And I think one of the other criticisms was, what are you going to put in that future case besides just crashing?

Chris Dzombak
Yeah, but I think you should get the choice and I think there are definitely cases where there actually is a sensible default or it is a recoverable condition.

Soroush Khanlou
Right. Or like maybe you can turn that into an error and then bubble that up through the UI.

Chris Dzombak
You could just I mean, I don't know if this is ever something that should really hit the UI, but I mean, I'm sure there are cases where there's reasonable program behavior.

Soroush Khanlou
Yeah, for sure. And so, I don't know, to me it seems like it could change, but a lot of people really did not like it.

Chris Dzombak
That's really surprising.

Soroush Khanlou
I don't know where I guess it says Return for revision review author. Here we go. So here's the link to the kind of summary of the feedback.

Chris Dzombak
Okay. In terms of naming most people seem to like frozen is a great soundtrack. I haven't seen that movie, but there.

Soroush Khanlou
Are some good Frozen puns in this threat, actually.

Chris Dzombak
That's good.

Soroush Khanlou
Shout out to Dave Zelong.

Chris Dzombak
I don't have time to follow this stuff. I wish that I did, but I just don't have time to follow Swift discussion or Swift Evolution discussion.

Soroush Khanlou
There's quite a bit about it. Well, that's why you have me and that's why people listen to this show.

Chris Dzombak
I know, I appreciate it. That's why I listen to the show.

Soroush Khanlou
That's right. Yeah. So I guess most of the feedback he took was more seriously. This discussion has convinced me that it's worth including what the proposal discusses as a quote unquote future case. The key point that swayed me is that this can produce a warning when the switch is missing a case rather than an error. So they want to maybe use a warning instead of an error. I know people won't be 100% satisfied with this, but this seemed like a reasonable compromise. And then he talks about the bike shedding about the name. I think frozen is a fine name for frozen enum.

Chris Dzombak
I think that's more clear generally than exhausted.

Soroush Khanlou
Right. And then I think future is a good name for the thing, but I think the names are pretty.

Chris Dzombak
So my one note, would you have a future in addition to a default case? Or if you have a future, does that mean that you don't have a default case as well?

Soroush Khanlou
So if I'm understanding the problem right, if you have let's say there's three enum cases right now, and it's nonexhaustive, it's non frozen, you would basically, if you had three items, you would have a future. But, like, if you had three items in your switch statement, so if your switch statement was exhaustive, you would still need a future. But if your switch statement only had two things in it, you would at least need a default. And then I guess the future part would be optional.

Chris Dzombak
That makes sense to me. Yeah. I think it would be odd to have a default and future case, but I guess there are situations where you might want to do that.

Soroush Khanlou
Yeah, I could imagine a situation, but definitely you don't need to have both.

Chris Dzombak
Yeah. Okay. That makes sense.

Soroush Khanlou
But I don't know. I haven't actually reviewed anything, but that's just kind of my intuition.

Chris Dzombak
That's my gut feeling. Yeah. Okay, so are those the only revisions, the future case and some naming changes?

Soroush Khanlou
I think so, yeah.

Chris Dzombak
Cool. In that case, this proposal is from, I guess we should mention Jordan Rose at Apple, who's on the Swift team. Cool.

Soroush Khanlou
Yeah, he might be on the core team. I can't remember who's on the core team and who's not.

Chris Dzombak
Yeah, I guess I'm not totally sure who's where, but I guess the correct thing to say is that's a name which comes up in Swift discussions fairly often.

Soroush Khanlou
Yeah, he definitely does work on it, but he's not on the core team. The core team is Ben Cohen. He's airspeed swift.

Chris Dzombak
Okay.

Soroush Khanlou
Chris Latner dave Abrams doug Greger joe Groff john McCall and Ted Kremenick.

Chris Dzombak
Nice.

Soroush Khanlou
Yeah. So that's this sort of exhaustive enum proposal.

Chris Dzombak
Okay. So kind of moving on, I guess, from proposal 192 onto proposal 194, which is it looks like this is a proposal from outside the Swift team. Is that right?

Soroush Khanlou
I don't know. Brent royal Gordon definitely is not on the Swift team. The other names I've seen a lot, but I don't know if they work on Swift. I don't think they do. I would guess they would have Apple emails.

Chris Dzombak
Yeah, that's a good indicator. Okay, so this is a proposal for derived collection of enum cases, or there's been so much discussion over the last several years over having some way to get all cases of an enum.

Soroush Khanlou
Yeah.

Chris Dzombak
That is something that is just useful, I think. I hope we can all agree it's useful. It's maybe not useful in all cases, but it is useful to just get a list of everything in an enum. I have personally needed this, albeit in Python, not in Swift, but I needed this for something I was doing earlier this week and it's Tuesday, so that's for something I was doing yesterday.

Soroush Khanlou
Yeah, I used to use Sorcery to generate this stuff, or like that case countable.

Chris Dzombak
Oh, yeah. Shout out, as always, to Sorcery, which is a really cool piece of software that has helped paper over a lot of things like this that are just really useful to have that Swift doesn't give you.

Soroush Khanlou
Yeah, for sure. There's also kind of another trick called case countable where you like, as long as the enum is int backed, you kind of start from zero and initialize. Just try to initialize it and see what happens.

Chris Dzombak
Yeah.

Soroush Khanlou
Until you get a nil.

Chris Dzombak
Such a hack works. Yeah, but I feel dirty and not all my enums are in fact yeah.

Soroush Khanlou
It is definitely a hack, but it works and I use it.

Chris Dzombak
Sure. And you shouldn't not use it. It's possible to do it safely, it just feels dirty. But it is.

Soroush Khanlou
You have to iterate through all of them just to get them, instead of just getting one static collection. Which is what this proposal aims to fix.

Chris Dzombak
Right, so how does this proposal aim to fix it? And I say this with a caveat, that I have not read this proposal yet because as mentioned, I don't have time. I wish I did.

Soroush Khanlou
So the way that this works is this proposal suggests a protocol that they're calling value enumerable, which I'm sure everybody will bike shed to death, of course, but basically, if you conform to this protocol, the compiler derives an all values implementation for you, assuming that you have no associated values. Right, because if you have associated values, it doesn't know what to put there.

Chris Dzombak
Yeah, okay, that makes sense.

Soroush Khanlou
Yeah. There's a world in which if that value is also value enumerable, it could also enumerate that one, but I don't think this proposal goes that far. Sure, so there's that. And then the other thing is, I think if your protocol does have associate values, you can provide your own all values implementation and so you could just provide those defaults yourself, which is pretty cool.

Chris Dzombak
That makes sense. Okay, so what value do we get from this being a protocol as opposed to just being a static collection that is automatically added by the compiler to enums where it's possible to generate this?

Soroush Khanlou
They do talk about that in the proposal. They basically want it to be opt in rather than just being on everything. I don't know if that's for binary size reasons or something, but they want it to be opt in explicitly.

Chris Dzombak
I guess there are surely there are enums where it doesn't make sense to be able to list all possible cases, but I really don't see what that would hurt. Binary size really that big of a problem.

Soroush Khanlou
I made that up. I don't know if it's actually binary size. I just kind of threw something out. And it's interesting because if you have an enum with no associated values, it's automatically equatable and you don't have to type, like, auto equatable or anything like that right. Is equatable and it conforms to the protocol automatically and everything there is precedent.

Chris Dzombak
Right. And it's not like you're going to I just can't imagine a situation where having a protocol where you're going to be using this enum via the value enumerable protocol rather than knowing what enum type you're dealing with.

Soroush Khanlou
Yeah. And you actually can't be just dealing with a value enumerable because the value numeral has an associated type and that associated type can be any collection.

Chris Dzombak
Right.

Soroush Khanlou
So it's not just an array. It's like you have to provide the collection type. And so you wouldn't be able to just hold onto a random value enumerable.

Chris Dzombak
Right.

Soroush Khanlou
Yeah. Okay. It's a good change. Everybody wants this. There's nobody that doesn't want this.

Chris Dzombak
Yeah. I mean, this seems like a really good change, and I'm clearly just nitpicking.

Soroush Khanlou
Here and I think that's what a lot of the thread was, was just nitpicking stuff.

Chris Dzombak
Sure. And I mean, I just worry about the case where it's some library that's not frequently updated and you want to be able to enumerate all values of an enum in it, but the library doesn't support it, hasn't opted in yet. And I think this seems like something that you can't retroactively impose on an enum from outside the same module. Right.

Soroush Khanlou
From a different module. That's a really good question, actually. I wonder what they is that they.

Chris Dzombak
Covered in here at all.

Soroush Khanlou
I don't think so. I read it a few times, but I didn't see anything about that.

Chris Dzombak
That's really my only concern. Unlike the previous case, where it makes sense, it is something that library authors should have to think about. I don't see that. I'm not convinced this is something that requires a lot of attention on the part of library authors.

Soroush Khanlou
Yeah, I agree. And you should just kind of be able to use it.

Chris Dzombak
Exactly. Yeah.

Soroush Khanlou
I think this is really straightforward. I think everybody wants this and we can bike shed it to death, but this is happening and everybody wants it.

Chris Dzombak
Ship it.

Soroush Khanlou
Yes. Cool. That's enums and Swift evolution.

Chris Dzombak
Yeah. And on that note, this is a little bit of a long episode somehow. We talked about, like, forums and enums. We can talk for half an hour.

Soroush Khanlou
That's right. We can talk about half an hour about anything. Broadly. It's about Swift evolution.

Chris Dzombak
Yeah.

Soroush Khanlou
Stoked about Swift Evolution. What do you think about that for a title?

Chris Dzombak
I don't know how I feel about these punny titles.

Soroush Khanlou
You don't like the new format?

Chris Dzombak
I think the format is good. I don't know about that.

Soroush Khanlou
Ecstatic about enums.

Chris Dzombak
All right, we'll do I hear you.

Soroush Khanlou
Just sighing over there. Just how do I deal with this? Love you, Chris.

Chris Dzombak
Love you, sir. Shall talk to you later. Bye.

