Speaker A
What was the thing we said we.

Speaker B
Were gonna record about Objective C retrospective?

Speaker A
Now, there was something else that we said right before that this that we thought was gonna be or that I was like, oh, yeah, we clearly we should do that.

Speaker B
Yeah.

Speaker A
And now I've forgotten it. Don't know why. I had a meeting at 830 this morning that I had to get up and be downtown for.

Speaker B
That's brutal. Yeah, that was right.

Speaker A
830. My life's really tough.

Speaker B
I'm it's early, man.

Speaker A
Not invented here. Do we still disagree about not invented here?

Speaker B
I don't know. Did we ever disagree about non invented here?

Speaker A
I feel like in the episode, this.

Speaker B
Should be the show.

Speaker A
I guess this can be the show.

Speaker B
Hello, and welcome to Fatal Error. I'm Sirous.

Speaker A
And I'm Chris.

Speaker B
And if you haven't already been able to tell from the pre intro little what do you call a stinger? What do you call that? We're going to try to talk about not invented here today. Yeah, we did a little bit of stuff on Not Invented Here with our Friends on the Runtime podcast, Caleb and Sam. But especially lately, I feel like I have been running into this more and more, and I just can't tell if I'm crazy or if I'm the only sane one. So this is going to be my weekly therapy session of programming. How are you doing, Chris?

Speaker A
I'm doing pretty well. We're recording this a little bit in advance, so this may not be totally accurate when everyone hears this, but I had a relatively boring week at work with sort of a lot of project management sort of work and getting acquainted with the code base I'm going to be working in for the next few months. So I haven't done any really interesting programming things for the better part of the last week. So I'm really going to lean on you here for interesting programming things. So if I had to guess, I would say this not invented here. Topic idea is coming from you because you are currently rewriting or you're writing an app in Objective C. You've been rewriting your promises implementation in Objective C. You've been hesitant to use third party libraries in this app for reasons that we discussed in a previous episode, which we'll link in the show notes. Am I right in guessing that that's why this is on your mind?

Speaker B
Yes, that is a big part of it, but also there's more to it. I sometimes feel like I impose these constraints on myself because I am so not invented here rather than the other way around. Like, I don't think this is necessarily the wrong call for this app, but we can make this app work if we did have Dependencies, but it shows itself in other places, too. For the Beacon app, for the server side, we needed the ability to talk to Twitter, and there was code that existed to talk to twitter and do the OAuth stuff, but instead of using it, I basically rewrote it. And I don't know if that was a good use of time at the time.

Speaker A
I think you had a good reason for rewriting it. Right. Which was that the code that you found didn't work.

Speaker B
Yeah, I think it didn't compile on Linux.

Speaker A
I'm remembering that correctly, right?

Speaker B
I think so.

Speaker A
It didn't compile on Linux. Or maybe it wasn't compatible with the current Twitter API, something like that?

Speaker B
Yeah, I think it was compatible with the Twitter. I think it was the Linux thing. And then also it made assumptions about what form you wanted the callbacks in.

Speaker A
Right.

Speaker B
And I wanted synchronous code and it all assumed asynchronous stuff and I was like, well, really, the only thing I care about in this is I care about the OAuth signature generator. But also the way that it was written didn't allow you to easily pull that out. So I pulled out the parts of it that I thought were important, built an OAuth signature generator, which I should actually really open source because I think it's a nice concise piece of code.

Speaker A
Yeah. And I'm sure if you had to write that, I'm sure other people will find it useful too.

Speaker B
Yeah, definitely. And even for understanding, like, how does OAuth really work? You could look at this code and I think it would give you a pretty good picture of it. Or another example from very long ago was when I was working on the back channel API that also didn't have any dependencies. The excuse then was that I couldn't bring in, let's say, Alamo Fire or whatever to do network requests because I couldn't impose those third party dependencies on somebody else when I'm already imposing my own self as an SDK.

Speaker A
Yeah, I think that's reasonable. I remember discussing that with you at the time.

Speaker B
Yeah, I think it was the right decision too, and I'm glad that I did that way. And so one of the things that I ended up doing was I wrote a multi part, like Request Builder is what I called it, and we can look into the show notes because the back channel API is all open source, so people can actually go look at that code. But yeah, so I wrote like a multi part thing and both with the multipart thing and the OAuth thing, I feel like I now actually understand how they work and why they are the way that they are, because I wrote a version of them. And so that seems important. But also your time is very valuable and why waste time figuring out some technology when you could just use somebody else's code?

Speaker A
Well, yeah, I mean, that's a really good question. I think maybe a better way to phrase that is how do you figure out how to balance what is a waste of time and what is a valuable learning experience? Or a valuable use of your time to produce some library that you need.

Speaker B
Yeah, I think that's a good way. And there are metrics.

Speaker A
It's not necessarily waste of time.

Speaker B
Right. You're not going to pull in, like, I needed map in Objective C. You're not going to pull in a dependency for that. It's not going to happen. But on the other hand, you're not going to rewrite UI kit. So there has to be some heuristic somewhere in the middle there. Although some people have been known to rewrite UI kit, crazy as they may be.

Speaker A
Shout out to going from a bricktor. Yeah. Shout out to letter press.

Speaker B
Yeah, that's right. So I think there's definitely a balance right, somewhere between map the function and UI kit, there's heuristics you can use to try to figure out what that balance is. Right. Like, do I want to learn the underlying technology behind this? How complicated is this thing? Is it proprietary? Could I even write it if I wanted to? Is it a lot of work for very little benefit? What exactly is the benefit of writing it yourself? I personally enjoy the control over writing exactly the interface that I want, knowing exactly the code, the implementation that's in there, knowing that there's no weird swizzling or anything like that, which a lot of these third party SDKs will do. Especially for analytics stuff.

Speaker A
Yeah, especially with some of the analytics SDKs and SDKs from bigger companies or SDKs that try to do a lot of things for you. You do have to look very carefully at the code and see really what's.

Speaker B
Happening under the hood, and you can't just trust them.

Speaker A
Right. And maybe sometimes you can't look at the code, in which case that really is something to weigh in your decision.

Speaker B
Yeah. And there's this quote that truly haunts me about this stuff, and I'm not sure if you're familiar with Will Shipley. He's like a person in our industry. Yeah. He writes on his blog about John Carmack, the guy that made Doom. He writes Carmack codes with a complete picture in his head of what parts he needs to make a hole. Back then, with every generation game engine, he'd start over from scratch. I mean, really from scratch, not nambi pamby. I rewrote some of the code and called it scratch. Since his engines ran on a variety of machines and OSS, he wrote every damn function himself. Carmack needs to log something. Carmack writes a logging function, new generation of engine, new logging function, everything from scratch. Because I was young, super anal, and wasn't on SSRIs back then, I once asked Carmack why he didn't use libraries for common why he didn't use libraries for common functions that he could share between engine revisions. CarMax is a super nice guy, but on this one instance, he used the well, I think my methods work pretty well defense, and I never suggested coding style changes again. And then he says, in case the first concern you have as well. That just means John Carmack's code is completely impenetrable. Right. Like, nobody could read this but him. But Will goes on, and he writes, don't take this to mean his code was spaghetti. It was actually some of the easiest to understand code I've ever worked with. It almost had an indescribable quality of obviousness. Like, you know, when a really good teacher explains something, it seems obvious that's what his code was like. And I just always fall back to this quote, and I don't know, I'm stammering.

Speaker A
So are you more in the Carmack camp here of you're going to write the stuff yourself because it's clear and you understand it and it works exactly how you want it to?

Speaker B
Yeah. And maybe the first time you write it is going to be kind of hard, but the second time, the third time you write it, you're just going to be going to pour out of your fingers. And I mean, I don't want to be self aggrandizing. I'm not John Carmack, but there is clearly some precedent in the industry for someone who is a very good programmer who doesn't use libraries like that. One other potential argument here is that if you're writing something that you know how to write, you're not really thinking about it actively, which means you can be thinking about other stuff while you write the code. And by the time you get to the next hard thing you have to write, you've already thought about it, and you can continue writing code, and you can maintain some sense of momentum while you program. That's a feeling I've had sometimes, which has been kind of nice, but I don't know if that's quantifiable as opposed.

Speaker A
To just, like, taking a break from coding entirely to think about and plan the next, like, hard thing that you're writing.

Speaker B
Yeah. And then you lose the momentum, and you're done. So you do Pod install to install your Twitter thing for your OAuth, and then you're like, okay, well, how do I use this thing? Go read documentation. Go figure this stuff out. Go figure that stuff out. Eventually you figure out how to use the thing, but you still don't know what exactly you want to do. And then you're like, I'm stuck. And so maybe you go for a walk, go take a shower, come back. If you work from home, you can take a shower. Otherwise, an office I mean, some offices have showers. This is a tangent, but then you basically lose that momentum, and I've felt that sense of, like it's almost like flow, but you're, like, filling in the spaces between the flows, so you don't slow down. And that can be kind of nice, but I don't know if that has anything to do with not invented here or, like, just writing code that you're comfortable writing.

Speaker A
I mean, I think that it may be more the latter, but that seems like a valid point. Yeah. This is what I was getting at at the beginning of the episode when I was trying to remember whether we agreed or disagreed. And I think that we maybe not disagreed strongly, but definitely tended to fall on different sides of this coin, especially. So when I was working the Times and doing iOS development professionally, we used a number of third party libraries. Some things were bigger and a number of things were really pretty tiny for a variety of different reasons. There may be business requirements that we integrate with such and such analytics, SDK, in which case we can look at the code and review it and maybe go back and say and request that the vendor fix things that we find that seem sketchy. But it's hard to argue with the business requirement there. Right, right. That maybe is something that you run into more at a bigger company rather than more than you would like working for yourself or working at a startup. And there's just an argument that in a lot of cases, I do feel like my time is better spent thinking about and working on the problems that are unique to our business, to our domain, like to the problem that I'm actually working on rather than reinventing, say, a logger which have been written. And there are loggers that work and maybe even send things off to Cert like an external server as a bonus. I don't know, it's not interesting to me. It's not something that I think is really worth the time of my time or the time of some other engineer on my team who could be doing something that is unique to our requirements.

Speaker B
Right.

Speaker A
Obviously, it's still a balancing act. Right. There are still times when you do take the time to review code that goes into the app we took time to review third party libraries that went into the app and decide based on things like how complicated is this code? Do we understand what's doing? Could we maintain this if we wanted to or if we had to adopt this? Can we use this code at least long enough to rewrite something for ourselves if this project gets abandoned? Is it good code? Is there documentation? How big is the community around this library? Are there people using it? Does it seem like it'll be supported? There are any number of questions like that to look at. But if the answers to most of those questions are positive, unless it's something that really is small, if you're going to save time by pulling it in. I feel like developer time, my time is really valuable, right?

Speaker B
Yeah. And it's interesting because everything you said, I don't disagree with any of it, but I think there are cases where someone with the perspective that you have would pull in a library and someone with the perspective that iPad that I have wouldn't even if they don't disagree on the sort of qualitative.

Speaker A
No, surely right.

Speaker B
On the qualitative idea that well, developer time generally is important. And the Reviewing SDK thing is actually super interesting too, because that's something that Times does, that almost nobody else does.

Speaker A
Well, that's something where the Times is unique that either. If there's some analytics company, for example, then if it's a closed source SDK, we may be able or they may be able to get the source to it, where most other companies can't and may be able to have some sort of communication loop with that vendor, even whether it's open source or not.

Speaker B
Right. They want Times as a client.

Speaker A
Right. Yeah. There are, I think, varying levels of usefulness that that communication loop has, depending on the exact circumstances. Right. But no, you're you're definitely right to call that out. But again, if it's a closed source SDK and your managers or your C level says that we're integrating with this analytics company, say you're even at a smaller company, in that specific case, there's not a lot that you're going to be able to do besides try to isolate it in your code as much as possible. Use a facade pattern. Right.

Speaker B
Yeah. Even at small companies, there are sometimes relationships that exist that make you use an analytics thing that you don't have a decision about. If you use it on the web, you're going to be using it on the client, like the app as well. In a lot of cases, you just don't have a choice. Yeah, I don't think the size of the company has that much of an effect on it.

Speaker A
Yeah, maybe. Let's think about something other than hypothetical analytics SDKs.

Speaker B
Right, think about analytics is actually one case where I probably would bring in an SDK just because I don't want to re implement every endpoint that they have. What's the point?

Speaker A
Yeah, that's a boring thing to reimburse. But I mean, even thinking about maybe some UI component right. That's something that is significantly higher risk because there tends to be more complication, there more complexity there because you're dealing with UI kit, there tends to be more mutable state there and it's something that the user sees and interacts with very directly. So that's something where I still will pull in third party UI components, but after looking through the code, making sure it seems reasonable, and I mean testing to make sure that it feels okay as a user, that it makes sense on the platform.

Speaker B
Right. Do you ever worry about like, okay, if I want to change this thing, I either have to fork it, make changes, and deal with a really annoying cycle of how to change things, or I have to submit a pull request and it has to be accepted. Do you ever worry about that stuff?

Speaker A
Yeah, definitely.

Speaker B
Business requirements? Not even business requirements, but just like things change and that's like the one, the one constant yeah, seem cheesy, but that's what I was I'll dive right.

Speaker A
In for the cheesiness. No, I mean, you're absolutely right and I think a few of the questions that I mentioned that I think you should evaluate if you're looking at some piece of third party code are really important here. Those questions are like, what sort of community is around this piece of software and what sort of support is there? Is there activity on the project? Do poor requests get merged or just sit around? Does the code review process seem really overly burdensome? Or maybe on the flip side, is it way too easy for someone to get code merged in?

Speaker B
Yeah.

Speaker A
And is this code that you feel like you or your team could fork and support if you had to? Maybe just temporarily to add something while you're waiting for it to be merged upstream, or maybe long term if the project is abandoned or if you have to diverge for business requirement reasons. Like if it's something where you won't be able to adopt it, and if the project is abandoned or you have to make some small change, you're going to end up rewriting it anyway, then it's probably not a good choice to bring it in. But if it seems like it's something you could probably build on if requirements change, then in my book it's probably a good move to at least think about bringing that into your project.

Speaker B
Yeah. Listening to you, I'm just like thinking about all the horrible ways that could go wrong. When you take a library like that, you're assuming that any way that you would want it to change essentially has to be an option in the library. Like it has to be coded in as something that's parameterized, or you'll code.

Speaker A
It in and send a pull request. And how's that different from code that you wrote that didn't anticipate this use case? You're going to end up going in and changing it anyway then.

Speaker B
Right, but changing the code that you wrote is easier. One, because you wrote it, two, because you have access, like the code is in its original state. It's not like an artifact of something else. When you run Cocoa Pods, you're really making a copy of a reference that's somewhere else. And if you mutate that copy, it's going to get blown away later. So you have to go change the source or change what the source is. Aka either open a pull request or fork it to your own thing. And so changing is much, much harder than changing your own code.

Speaker A
Yeah, but you're not going to have to do that for in my experience, probably even maybe not the vast majority, but the majority of dependencies that you pull in, you probably will never have to touch and will never have to change in that way.

Speaker B
There's cases for things that are definite wins. I wrote a promise implication because I'm crazy. I probably will write a reactive implementation because I'm crazy. But I think that's a really good example of something that you really shouldn't. That's where I feel my own ideology falling apart is like, I know now from writing a Promise implementation that there's so many weird edge cases ordering bugs just like things that you would not.

Speaker A
Think synchronization bugs in your eventual reactive programming implementation.

Speaker B
Yes, all of it. And there is a lot of things that go wrong and it's designed to be flexible. So I think that's something where okay, pull in the library. Another thing there is there's a decent amount of documentation for existing reactive libraries where there might not necessarily be a good amount of documentation for this global spinner or whatever pod that you're going to pull in or like custom alert view library just won't have as much documentation. Yeah, one thing that I do find interesting is I have no compunction with going to GitHub, finding something that I like and copying the code out of it and making it my own. That's something I do actually pretty frequently. Okay, well, I'm basically adopting that piece of code and that actually resolves a lot of the concerns I have. One, it's still easy to change because it's not artifact based. Two, I now know how it works because I've messed with it enough and rearranged it enough to where I understand what each component is doing, which I think is important to know how to change and fix stuff. It also gets some of the benefits of I didn't have to write every single part of it, I just had to write some part parts of it. So that's basically how the OAuth thing happened is I looked at how something else did it and modified that code to make it look the way I wanted it to look and it can match your coding guideline style, spacing, variable names, everything.

Speaker A
Well, that makes sense. This sounds like kind of a medium point between.

Speaker B
It is a nice thing too, because the author implementation thing was particularly interesting because there was a reusable component hidden inside of there that I wanted that I couldn't extract. And doing this thing of basically adopting the code and making your own makes it so you can extract that third or that reusable part in the middle and then reuse it elsewhere without having to write the whole stack yourself. One other part of this is maybe it's just a taste thing. Some people like two spaces for tabs and some people like four spaces for tabs and they just have sensibilities and they have or spaces and tabs is a bad example. A better example would be like maybe small classes versus big classes. Although it seems like there's a right answer there and a wrong answer. But basically people have seen bad things in their time and they're trying to avoid those bad things.

Speaker A
I mean, it may be like spaces and tabs where just you can make arguments on either way, but it kind of falls down to a personal taste or a personal balancing of right, but.

Speaker B
It'S more intense than space versus tabs because it's not just graphical or just an appearance. It does actually have functional Ramifications for how you work with your code.

Speaker A
I guess so, yeah, I think it.

Speaker B
Would be more like functional versus Oo or something like that, where they're both good, they both can do everything, but.

Speaker A
It'S not that big a fundamental difference, though.

Speaker B
I think it can be. Yeah, I think it can be. If you go into a code base where it's like a ton of pods and a ton of blue code, working in a codebase is very different than a codebase, where it's a bunch of really small components that even if those.

Speaker A
Components were copied from various GitHub repositories.

Speaker B
Yeah, but all matching a style. Granting that maybe I don't feel super strong about the arguments I made here. I don't know, I just see myself acting this way and I'm trying to rationalize it or explain it or express it to someone else and I have a very tough time with that with this particular thing, and I don't know why, I don't know what it is.

Speaker A
Yeah. I know where I stand on this, where I fall personally on the sort of balance that we've discussed, but I've given you my arguments and I don't think there's a right answer here. I think these are our maybe it's just taste. Yeah.

Speaker B
I wish this episode had a better conclusion, Chris.

Speaker A
Yeah, me too, but well, next time I see you in person, we'll fight it out. We'll arm wrestle and resolve the question that sounds good.

Speaker B
Of not bring your boxing gloves, man.

Speaker A
It's going to happen off the buy boxing gloves.

Speaker B
And I think if we worked on a project together, I don't think we would fall that far apart in terms of when to pull in a third party dependency and when to not.

Speaker A
No, I think that we'd probably get along pretty well, which we've never worked.

Speaker B
On a project together, Chris, isn't that correct?

Speaker A
That's true, we haven't. Yeah, there have been a couple of times, I feel like, when we almost did, at least in some capacity, but hasn't actually happened.

Speaker B
Yeah. So maybe that's something cool for the future.

Speaker A
Yeah. Someday we'll make a fatal Error app that includes a bunch of analytics around what our listeners are.

Speaker B
Every analytics library is going to be in there. It's going to be great.

Speaker A
Yeah.

Speaker B
They're all going to swizzle UI application send event, but only analytics.

Speaker A
Everything else we'll write ourselves.

Speaker B
That's exactly right. That's exactly right. Yeah. On that note, it was good to talk to you as always, Chris.

Speaker A
Yeah, it's great to talk to you. I'll look for boxing gloves on Amazon here. Perfect.

Speaker B
Yeah, talk soon. Bye.

