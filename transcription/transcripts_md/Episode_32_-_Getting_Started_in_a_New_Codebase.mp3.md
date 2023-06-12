Speaker A
Hello and welcome to Fatal Error episode 32. I'm one of your hosts.

Speaker B
I'm one of your hosts.

Speaker A
I didn't know what to say.

Speaker B
Like, your name.

Speaker A
Yeah, I was going to do, like a positive. Like, I'm one of your hosts. Rich Kanloe. How are you doing?

Speaker B
I'll be one of your hosts today. Hi. And I'm Chris.

Speaker A
Cool.

Speaker B
So this is the show. Well, before we start, I guess this is our first Patreon episode of the season. We want to give a shout out to everyone who's supporting us on Patreon. As we've said before, we really do appreciate your support and you are making it possible for us to produce the show.

Speaker A
Literally, our Patreon supporters are the best.

Speaker B
Literally, the best.

Speaker A
The actual best.

Speaker B
It's true. No, we really thank you very much for your help and support. So today, the thing that we thought we would talk about is something which is very relevant to me right now, and that's getting started in a new code base. Like, let's say you started a new job, as I have, and you're not familiar with the code base, or in my case, with the 20 different code bases that make up various parts of a fairly complex data processing and storing and web front end pipeline. Where do you start?

Speaker A
Right, absolutely. So you just started a job, and this job, you said, has 20 different.

Speaker B
Code bases and some approximation, but I mean offhand roughly, maybe generous, like maybe 15 or so different.

Speaker A
I think especially, like, a lot of people listening to this, when they start a new thing, they might have one, maybe two code bases. Right? Like an iOS code base they got to get really familiar with and then maybe like an API that they got to also touch.

Speaker B
Well, so these aren't necessarily giant code bases, right?

Speaker A
Right.

Speaker B
A lot of them are designed with kind of the Unix philosophy, where each of them does one thing and then, I mean, four or five of them are tools that you literally run together and pipe standard output from one into standard input of the next.

Speaker A
Got you.

Speaker B
Some of them are still pretty big, but it's not like they're all iOS app sized code bases.

Speaker A
Right. I was imagining that they were all web services. Actually, no, but they're not.

Speaker B
So only one of them? Well, only one of them is really a website. The others are all like, Internet scanning or data gathering, data processing and database sort of tools.

Speaker A
Got you. And you just run them locally?

Speaker B
Yeah.

Speaker A
Cool. So how big is, like, an example? Big one. And how small is a small one?

Speaker B
So looking at this here, the website that I mentioned that we run is right around 40,000 lines in total. And that's Python and that count that I just ran, this count here. So that may include some of the libraries and stuff. I don't remember the structure of this repository offhand the main scanning tool is right around 17,000 lines. That's mainly in C. One of the other tools is like, a 60,000 line go tool.

Speaker A
Wow.

Speaker B
And then other tools are, like, 16,000 lines of Python and like, 1000 lines of Python. So there's a range both in languages and in code base size here, right?

Speaker A
Yeah. So these are substantial code bases. They're not gigantic, but they're also not small by any means.

Speaker B
Yeah. And I mean, some of them, like 1000 line Python tools. Right. That's pretty small. But 15,000, 16,000 lines of C is not trivial.

Speaker A
No, that's not a small program. Interesting. Okay. So something around 15 to 20 repos where the big ones are, like, in the 50, 60,000 lines of code range, and then the small ones are maybe 1000.

Speaker B
Yeah.

Speaker A
Okay. So what have you been doing to get into these code bases?

Speaker B
Yeah, I mean, so the thing that I started with was with the help of a couple of the students who work in this lab who wrote these tools, I started figuring out how to use these tools. Right. Since it's kind of like research software. It's not super well documented, perhaps even less well documented than many iOS apps are, if you can believe that.

Speaker A
I can indeed.

Speaker B
And so just figuring out what sorts of inputs and command line parameters and what sorts of outputs and output formats to expect was actually a nontrivial amount of work. So just understanding what each tool does by reading, READMEs and talking to people and maybe looking at the main entry point for each code base and trying to work back and try to use each tool for what it's supposed to do to get some idea of what I'm looking at. Right. That's a good start.

Speaker A
Got you. So, first step, actually figure out what the app does. The app do the program and then start to use it and start to figure out what its sort of capabilities and edges are.

Speaker B
Yeah, exactly. And while I was doing that, I put together notes about where documentation could be better. And I haven't gone back and actually fixed and documented all that stuff, but at least I have a list of improvements. So that's a first step. Right.

Speaker A
Nice. Yeah.

Speaker B
And after that so as I've started to actually make changes to these tools, there are a few different techniques that I'm using, just depending on the problem at hand. So the first thing, and depending on the language that the tool is written in, the first thing I've been doing, which works in pretty much any language, open whatever main routine runs when you start the program, and just try to trace just try to trace what happens, given whatever parameters that you've passed to it. And doing that, I've been doing with a lot of sometimes it's clear exactly. Sometimes it's clear which module the code is calling into. And you can sort of navigate to this in the file system, depending on how things are organized. Sometimes, just like project wide search is really valuable. Find everything that implements a method with this name and work backward from there.

Speaker A
A lot of gripping.

Speaker B
Lot of gripping. That's honestly a large part of what I've been doing. And that works even if you're not like starting from main. Right. You just have some idea that something needs to change that has to do with some key phrase to search for that phrase and figure out what calls that, which, again, grepping can help with and work from there. So there's kind of a lot of poking around kind of in the dark with Project Wide Search and grepping.

Speaker A
Right, right.

Speaker B
There are some other useful techniques, though. So I've been using Atom, the GitHub text editor, to work on all these code bases. At some point, I want to get at least the C code bases building within Xcode, if only so that I can use those cool refactoring tools that we saw at WWDC, right?

Speaker A
Yeah. Feel me? That's amazing.

Speaker B
But there's some Go language plugins for Atom that make working with Go and Adam really nice. Like you can command click on things and see where they're defined. And that's really useful when drilling down into a Go program too.

Speaker A
For sure. Yeah. When I'm working on Swift server stuff and I'm doing it in TextMate, I just want to command click and option click everything.

Speaker B
Yeah.

Speaker A
And it's just yeah, maybe I should just switch to Adam or something.

Speaker B
And I think there are probably Atom plugins for other languages that do things like this, but that's probably harder with something like Python. But there must be similar things for like, C, for example. Right?

Speaker A
Yeah, it seems like. And like something like Swift, where you have a pretty good sense of the static type of everything and you can kind of jump to the right thing.

Speaker B
Yeah, well, I mean, Xcode does this in Swift now, right? So that's one of the techniques that's two of the techniques that I've been using and most of the work that I've been doing are in the Go and Python code bases. So both of those have actually worked pretty well so far. There are debuggers, obviously, for Go and C. I'm familiar with GDB in Sealand, although I have to re familiarize myself with the command line interface for GDB. Right. Like running something in a debugger just from the terminal is different from running it in a debugger. In Xcode. There are less buttons to click.

Speaker A
Right. Xcode gives you so much stuff for free.

Speaker B
Right.

Speaker A
I maybe also have never actually debugged something in the command line.

Speaker B
It's been a while for me.

Speaker A
I've done it with like Pry or whatever in Ruby, where you just put Pry in the code and then run it and then it'll give you a breakpoint there. But I've never spun up GDB, attach it to a process and then added a breakpoint to a specific line and file.

Speaker B
Yeah, it's been quite a while since I've done that. There's a Go debugger, too, which should come as no surprise. Right.

Speaker A
Which does it hook into, Adam, so that you can put a breakpoint on a line?

Speaker B
It does. There's a plugin that lets you do things like that.

Speaker A
Amazing.

Speaker B
I haven't used it too much yet because it's just something else to learn. And I mean, starting a new job, I just have such a long list of things to learn and things to investigate. It's kind of overwhelming. Right.

Speaker A
Especially with so many languages.

Speaker B
Yeah. Languages that I haven't been using really seriously in a couple of years. Right. But that's one thing that I have on my list, is to dig into this Go debugger and the Atom plugin for it and figure out how to use that. Because obviously, using breakpoints and printing values out with a debugger and sort of poking around in a paused program can give you so much more information than just, like, looking at the source code and log based or printf based debugging.

Speaker A
Right, right. Especially with you got to build with some of these C things, like, how long does that take Python? Maybe you don't have to worry about that as much.

Speaker B
Yeah, so that's something. And the other thing is that I have to figure out how, if I want to use this Atom plugin for the Go debugger, how do I pass the correct parameters and pass input data to these tools when I'm running it from Atom? I'm sure there's some interface for this, but I don't know what it is.

Speaker A
Right. It's just yet another tool you got to figure out and learn.

Speaker B
Yeah. And then I actually should check whether there's any sort of interactive debugging for Python. I'm sure there is, but I have never looked into that.

Speaker A
Yeah, I know. It's tough, too, because both Python and Ruby, you can define methods at runtime, and then how are you going to attach to those?

Speaker B
Yeah, I've never tried this with Ruby either. Totally new to me. So one of the things that I wanted to ask you, what else would you be doing? What recommendations do you have? Am I missing anything that may be useful?

Speaker A
No, I think you basically have it. Right, okay. One other thing. My only experience with this is, like, you're contracting. You get a new client. Client lasts a couple of weeks, maybe two months, and you're like, I have to spin up on this as fast as possible and get productive as fast as possible, and then essentially throw that all away at the end of the contract once I've done the useful thing that the client wanted me to do. And one thing that can be useful for that is just, like, completely ignoring everything. That is not the thing you're trying to figure out at that exact time. So if you're just trying to explore the code base and figure out what's what, then that's fine. Like, yeah, go nuts. And just like, it's kind of a playground, right. And try to just see what you see. But if you have a task just like trying to stay single mindedly focused on, for me, it's really hard. Like, I get distracted by different weird code spells and stuff. I see them like, oh, that's weird. Why does that happen? And then when I go in and dig into it but I have to not do that. I have to just stay super laser focused on the thing I'm trying to fix. And what that means is that especially on some of these shorter contracts, you never really get a full state of the sense of the code in your head. You just sort of constantly have the sense of like, well, I don't know what's happening in 85% of this app, but I do know how to fix the thing I need to fix.

Speaker B
I'm glad you mentioned that because that's something that is a very familiar feeling for me right now. It's been a few several weeks now of knowing at least enough to figure out how to do what I'm trying to do, how to fix what I need to fix, but not really knowing the whole system. And that's a new feeling for me. I've spent the last since college working at places long term where you get to know the entire code base really well.

Speaker A
Right, right.

Speaker B
Maybe I'll get there eventually here, but that's definitely something that's new here, but right. I'm glad you mentioned this. Trying to stay focused on what you're trying to do is really important. There have been a few days where just like, I spent the entire afternoon going down some rabbit hole, just exploring something that I saw, which which can be helpful. Right. I mean, I think that's probably good. I'm just trying to balance at least because this is a full time job, this isn't a two week contract.

Speaker A
Right, right, exactly.

Speaker B
So trying to balance that instinct with just trying to focus and get done whatever it is I need to get done is a little bit of a challenge.

Speaker A
Yeah, for sure. One other thing that I think could be kind of helpful in the same vein as this, is when you have a specific task to do, like just trying to do it regardless of whether or not you have enough. Knowledge and regardless of whether or not you're even going about it the right way, based on the architecture of the app as a whole, just like trying to execute the thing you want to do and observing how the thing breaks as you change it, can I find it give you a ton of insight into the thing as a broader construct, if that makes sense.

Speaker B
Yeah, that totally makes sense. And something else that occurred to me while you were speaking was just trying to fix something. Regardless of how well it fits into the current architecture, can be useful because you can observe how things break, what other things get affected by this change that can also I mean, I'm again trying to balance that with knowing when to ask questions. Right, right. I know about myself that I will not ask a question that I should ask for an entire workday or two workdays. Right. Because I'm like, I can figure this out. I will figure out how this works. I'll make this happen, and then eventually, after way too long, go and ask a question about, okay, so what's going on here?

Speaker A
Yeah, that's actually a really important one that you brought up. We don't do a lot of live Tweet readings here on Fatal Error, but I do have a very good one, which I'll drop in the show notes. And the Tweet is when you start a new programming job, you have to walk right up to the biggest function in the yard and refactorate in front of everyone. And this is one of those things that you start this new job, and especially, I think, for certain types of people, they're afraid you don't want to show any like, I'm definitely one of these people. You don't want to show any weakness. You want to show like, I'm like a really confident, smart person. And so asking questions at some points, like whether or not this is valid or not, can feel like showing weakness. And so you end up in a situation where you're like, oh man, if I ask a question, they're going to think I'm dumb. But also, should I be expected to know this? I just got here. And so trying to balance also, you're wasting someone else's time, or you feel.

Speaker B
Like you're wasting someone else's time and you're not wasting their time. Right. And you just started a new job, a new project. Like, it's it's okay to ask questions, but right. I just realized that I've backed myself or like, talked myself into a corner by not asking a question for so long and then so that's an important thing to do when you're starting getting started with an unfamiliar code base.

Speaker A
Yeah.

Speaker B
So on the flip side, I just want to add before we move on from the topic of questions, if you have someone who new, who's starting on your team, who's starting with your code base, with your twelve or 15 different code bases right. I think it's really important, especially if the person is more junior or not, even if they're a senior level program like whatever, to encourage and be open to a lot of questions. Because really, that's going to be really useful. And they're going to get a lot of background information about the software and about how it works and about why it's structured this way. And you can be off putting and it can be intimidating for people to ask questions like making clear that that's welcomed and encouraged and that actually is something that you welcome and encourage is really super helpful.

Speaker A
Yeah, for sure. And it's one of those things where a little bit of effort from the person who's been at the company a little bit longer ends up paying back in spade. So if you want to think of it as like an economics thing of like, no, I really have this project that's important, you're going to spin up this person who's new so much faster, and they're going to add way more capacity to the team than you've already added your capacity. You can enable another person to add their capacity. So even from like, I'm really busy and I got a lot of stuff to do, it makes sense to answer a ton of questions. So if you can answer questions, you should answer questions.

Speaker B
Absolutely. Yeah. If you can come up with questions that the person should ask but doesn't even know to ask yet, just make a list or talk with them about things that they will probably find surprising as they dive into the code.

Speaker A
Right. Apologize a lot. Done that before.

Speaker B
I mean, seriously, that's really useful. And I hope that both of us and many of our listeners have talked someone through some part of a new code base and pointed out things that seem weird because they are weird and explained, this is why this is weird. And either we plan to change it at some point in the future or we know not to touch this because X, Y, and Z. Right?

Speaker A
Exactly. We tried to touch this once in 2008 and it didn't go well.

Speaker B
Exactly.

Speaker A
Ben and I'll hope Yehu attempt to refactor here.

Speaker B
Monsters.

Speaker A
That's right.

Speaker B
So one other thing that I thought of a little while ago, code review. Let's say that you have through some combination of grep and debuggers and asking questions and just fix it. Just trying to make this change. Regardless of how it works, hopefully you send a pull request and get feedback about how well this fits into the architecture of the SAP. Right. Does this code work? Right. Does it work as we expect it to? Are there other approaches that other people on the team would have taken? This is something where both if you're a code reviewer, this is obviously a good teachable moment, like, help introduce this person to your code base again. And if you're the person sending the pull request, what I've been doing is call out specific things that I'm less sure about right. And say, hey, I don't know if this is really the right approach, or I don't really know if this goes here. I could find examples in the code base that do this in both of these different ways. How do we choose between them, ask questions and call things out in the code review that are in your pull request that you want covered in the Code Review, right.

Speaker A
Yeah. Definitely important. And not just for new people, also.

Speaker B
Yeah, absolutely. I mean, I think it's maybe more important for new people, and there's a whole lot of just sort of institutional knowledge right. That they need to get. We actually did an episode on Code Review, which we'll add to the show notes for those of you who may not have heard.

Speaker A
When did we do that episode?

Speaker B
I don't remember, but I we definitely did one. We definitely did one.

Speaker A
Review. How many weeks have you been at this job?

Speaker B
I started, I think about six weeks now.

Speaker A
Can you give a ballpark of how many pull requests you've opened or, like, how many code reviews you initiated?

Speaker B
It's not that many. It's maybe five or six.

Speaker A
Five or six, okay.

Speaker B
Yeah, cool. All right. I spent the first, basically two weeks just figuring out what a lot of these tools did and how to use them. It's been slow moving, honestly. And, I mean, some of those pull requests are mostly documentation. Some of them are actual functional changes and fixes.

Speaker A
Right.

Speaker B
Yeah.

Speaker A
So there's one thing that's kind of unique about your job compared with other programming jobs, where, correct me if I'm wrong, but you were basically hired because of your expertise in maintaining software projects and kind of your seniority. In terms of how much you know about different code bases and how much you can help people who's writing code for them is just a means to an end rather than any kind of end in itself.

Speaker B
Yeah, I think that is true. I do have some ideas of research questions that I would like us to look at. Right. But that is a large part of why I was hired, is because it's a group that consists of grad students and a postdoc and two undergrads. And even people in the group who are older than I am don't have the same professional software development experience. And so some of their code, it suffers in one way or another just because we've had a very different set of experiences. Right, right.

Speaker A
Exactly. And so, essentially the thing I'm curious about is, like, since you have this slightly different role, since you're almost there to guide people into how to make their code more reusable or more maintainable or whatever, how does that affect how you look at the code base and the eyes that you look at it with?

Speaker B
I mean, I'm definitely looking at it with a somewhat critical eye all the time since I know that this is part of what I'm supposed to be doing is not just adding features and fixing things in software, but also over the long term, helping improve the quality so that it's more maintainable and so that it's more stable.

Speaker A
Right, right.

Speaker B
So I've definitely come at things with a slightly more critical eye. I'm trying to keep track of things that I notice that could be fixed as I notice them. Right.

Speaker A
Is that in a personal document or is that in some shared space?

Speaker B
It's in a personal document right now. It will not surprise you that a research group doesn't have a very formal ticket tracking system.

Speaker A
That's a really good point. Actually, I did not consider so there.

Speaker B
Is a Trello board, but it start. Yeah, I mean, it's a fine start, but it's not really a backlog of future refactoring sort of Trello board. It's more of a like what is everyone working on right now? Sort of thing.

Speaker A
Got it. Yeah, got it. In a past life, I also used to be in academia. I was getting a master's degree in bioengineering and pretty much every form of engineering has some element of code in it these days. And I was someone who I wasn't great at this stuff by any means, but I had a head for it. And you would see people would write this code in MATLAB, mostly array and matrix manipulation of big numbers and processing, fitting, curves, stuff like that. A lot of statistical analysis. But yeah, there was no concept of source control for one. There was definitely no concept of issue tracking because nobody else could really see your code except they would look at your thesis once it was done and bound into a book and they would flip to the back and all your code would be there as kind of an appendix. I kind of was expecting, because this is a computer security research team, that they would have some stuff in place for it and they have Git, which is far cry better than most things. Right? Yeah, that's good. And then I guess what I'm trying to say is I'm not surprised that there's no issue tracking, but might be worth, especially if some of these projects are going to live in really long term ways. Might be worth trying to get more rigorous about that stuff.

Speaker B
Right. I might have spoken too soon here. Some of the code is open source and those GitHub repos do have fairly active issues where I have filed some sort of longer term issues and where I should probably be filing more things. But so there's that. There's Trello, but especially for closed source things, there's no long term backlog of stuff that needs to be refactored and maybe I should just throw that up in trello just so that it's public and not in a personal document. This is probably more of a failing on my part than on the group's part.

Speaker A
Generally, I think it has to be okay for you to keep private notes just because not everything can be prepared for public eyes immediately. And it's really hard when I've worked on teams where they try to force you like you have public private notes, just make them public immediately because we want to see that stuff. That being said, the more open the better. In as much as you can pull it off. So that might be interesting things to do and see what kind of feedback people have about it. Because people might say, oh, I've been thinking about the exact same thing. Or they might say, oh, I never considered doing it that way. I'm glad you brought this up.

Speaker B
That's true. Yeah. That would be a good way to start some of these discussions and kick off some teach bowl moments, either for everyone else or for me as to why whatever I'm talking about is the way it is.

Speaker A
Right, right, exactly. You mentioned there's public GitHub repos. Is that something we could link to in the show notes?

Speaker B
Yeah, definitely. It's very much not iOS related, but we'll throw links to those GitHub organizations in the show notes.

Speaker A
That sounds good. And is it stuff that I could download and run myself?

Speaker B
Some of it is, yeah. The best documented thing is internet wide scanning tool, which you need a decent internet connection to run and isn't really going to be that useful, but you could at least download and build it. And most of their tools that are open source are designed to take the data that comes out of that and process it in one way or another. And those aren't super well documented. I've kind of concluded that those tools it's almost only possible to use if you know somebody personally in this lab. Yeah.

Speaker A
Is that something that you would want to change over time or is that just like kind of how it's going to be?

Speaker B
Yeah, it's absolutely something that not just I, but that everybody would like to change. Right. Things like reproducibility are really important in the research community, but there's just a long list of things to do.

Speaker A
Yeah, I can imagine. One final thing that I wanted to make sure I asked is this is kind of a small question, but you mentioned documentation and a lot of command line tools. They have kind of conventions around. So let's say how do you get the version of this tool? How do you get the help for this tool? What is the pattern of how you should add different flags and stuff? Is that stuff set up in a good way or is it kind of.

Speaker B
It depends on the tool. So, like, C, Python, Go, all have libraries that do command line parsing in a sane way and implement those sort of standards or ideas about how things work. Right, right. We'll do things like print out a help page of all the documentation for you. And so you can always get at least, like, a list of what options the program accepts. In some cases, the documentation that accompanies those options is less good than it is in other cases. So while you may be able to tell what arguments this program accepts, certain combinations of arguments are invalid or like, only certain combinations are valid. And that's really not very. Well documented either. Plus, you still have to have a good, high level idea of how the program works, and that is more possible with some of these repositories than it is with others.

Speaker A
Got you.

Speaker B
Yeah.

Speaker A
Okay, that makes sense. Interesting. So do you feel confident in the amount of learning you've done in the last six weeks?

Speaker B
I think so. I always feel like I should be learning more and moving faster, and it's impossible for me to tell whether that's reasonable or just me holding myself to an unreasonable standard.

Speaker A
Yeah. I can kind of tell you that everything I've ever worked on has always felt like that. And I think you're just the speed that you are, and you want to go faster and suck the information you brain faster, but it just takes time for everyone.

Speaker B
Maybe that's a good note to end on. It. Takes time.

Speaker A
Yeah, takes time. Chris, a pleasure as always, and to our Patreon listeners, thank you so much for supporting us.

Speaker B
Yeah, thank you very much for your support, sir. It was great to talk to you. I think this was a really useful chat for me and talk to you soon.

Speaker A
Cool. Talk to you next week. Bye.

