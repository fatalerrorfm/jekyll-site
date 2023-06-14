Chris Dzombak
Hello, listeners. Welcome to Fatal Error. I am Krista Zomback.

Soroush Khanlou
And I am Sirish Khanlo.

Chris Dzombak
And today we decided to talk about code review. This is something that probably all of us encounter in our in our professional lives, and we figured it might be useful to go over. What do you want as somebody who's having your code reviewed? What do you look for as someone who's reviewing code and what are sort of the goals of the code review? Why do we do code review? What are the goals of this process? Sirous, do you want to kick us off?

Soroush Khanlou
Yeah, for sure. Code review is an interesting thing to me. Specifically, I've been on a number of teams. I've been in situations where I'm the only programmer, so there's no code review to do. I've been in situations with very rigorous code review. In terms of there are basically you sit down and synchronously review the code and talk it through rather than just leaving comments on GitHub or whatever. I've been in situations where I don't actually write any code on the project. I'm just code reviewing and just saying, hey, I don't know exactly what's going on the rest of your code base, but that looks wrong to me. Let's talk about that part of it. And it is, I think, such an important part of making a complex software project that you've got to do a good job with it. It's really important, is what I'm trying to say.

Chris Dzombak
So it's important. What are the goals? Like, what are we trying to accomplish with a code review process?

Soroush Khanlou
So there's, I think, at least two components. One is to get other people in the project to have some knowledge of the code that you're adding to the project, so they're not surprised when they see this code. Like, how did this get here? And two, it's to catch bugs, and it's to make sure that styles are maintained and all that stuff. The styles is an interesting question, but primarily to catch bugs. If you can use the Linter to catch style stuff, that's better.

Chris Dzombak
I would add maybe ensuring that not just catching bugs and making sure that everyone is kind of on the same page, but making sure that the application ends up with sort of a consistent architecture.

Soroush Khanlou
Right, right.

Chris Dzombak
Sort of the key concepts in the application are consistent and compatible.

Soroush Khanlou
Right. I'm open to the idea that that should happen before you start writing code. Not that I've ever worked on a team that does legitimate architecture review or anything like that, but I am open to the idea that that's important. So there's the Joel Spolski's Twelve Steps to Better Code. And it's like, step one, do you use source control? Step two, can you make a build in one step? And one of the things that he doesn't talk about in this is, do you do code review? And to me, code review is really up there in terms of these like his his thing is like, should you accept a job somewhere where they don't pass these tests? And I think code review is one of those things where you should really think about it before you should be a component of your thought process. It's tough when you're one person I've been in that position to try to figure it out. We end up having a contractor do code review for a little bit. It's also tough to make sure to give really good code review feedback. It's kind of easy to just rubber stamp stuff or just catch you have an extra space here and then just say, it looks good to me and ship it. But the level of things you can catch is actually quite deep. So I'm curious to know what your experience is with code review.

Chris Dzombak
Sure. So boy, my experiences with code review I guess I've had a couple of different experiences with code review at a smaller startup that I worked for back a little while ago. At this point we had really a pretty loose code review process looking mostly for obvious bugs, kind of does the software seem to like does the code you've written work? And that was pretty much it.

Soroush Khanlou
Can this thing ever be nil?

Chris Dzombak
Right? At my current company, at the Times, we tend to have a much more it's still informal, but a much more in depth code review process. When people review code, they're looking for all sorts of potential issues and problems and there's a lot more discussion that happens above and beyond. Are there any obvious bugs and does this code more or less work?

Soroush Khanlou
Right, there is a really good blog post called On Code Review. This person doesn't have too many blog posts in general and this actually may be his only one, but it's really great. His thesis is pending. Code reviews represent block threads of execution because context switching is so hard and because you can't move forward on a certain project without getting the code review done. You should prioritize code review over other people's, code review over all of your own work just because it's so important to get done to get kind of out of the way. Because otherwise everybody kind of has to have two projects so they can page into another project, work on that while they wait for their code review.

Chris Dzombak
Yeah.

Soroush Khanlou
So I think this post is really good and I will put this into the blog post sorry, into the show notes. So now that if we can kind of agree that code review is important and possibly very important.

Chris Dzombak
Yeah, absolutely.

Soroush Khanlou
Let's maybe talk about a little bit about tools and processes for doing good code review.

Chris Dzombak
Sure. At work right now, we use just GitHub as our tooling and either one or two people look at all poor requests before they get merged and the process is still pretty informal. We do have continuous integration that will check out the branch and run the unit tests and the screenshot tests. And we run Danger CI, which we've mentioned in a previous episode. I'm sure to check for a few other things that we don't want to get merged into the code base, but that's kind of what our fairly informal process looks like here. I'd be curious to hear what sort of processes you've worked with since in consulting, you've worked with many more places than I have over the past year or two.

Soroush Khanlou
Yeah, so I think GitHub is a really great baseline. I've done bitbuckets code reviews. They're not as good, especially with the new tools that GitHub made where you can submit all of your comments at once rather than doing one email per comment, which can be really stressful for the person being reviewed, especially if it's a big pull request. And I've also tried Atlassian has a product called Crucible where you can kind of pick several commits and say, please review these commits. But I think that the pull request model is much better than the standalone code review model because you can reject a pull request outright, whereas you can't really do that with a code review because that code is already kind of in the develop branch. You could revert the commits individually, but it's not as good. And there's also fabricator, which I've never used. I've heard mixed things mostly bad about fabricator, but I don't know if you've ever used fabricator.

Chris Dzombak
No, I've never used it.

Soroush Khanlou
Yeah, I mean, I think GitHub is a really good baseline. The way to level GitHub up is to do the GitHub pull request in person. And basically you have one reviewer and the person who's being reviewed, and you sit down together and you say, okay, let's take a look at your code. And I've worked at a company that calls the Synchronous Code Review. So there'll be like a day of Asynchronous code review where everybody just kind of gets to leave comments and then you can kind of respond. But that's the more informal part of it. And then the more formal part is like, you sit down and really because sometimes when I'm doing code review, I'll look at something and I'll be like, I'll have a thought. And the best thing to do is really to write that thought into a comment because other people have that thought, because it'll help you. It means that there's something in the code that you don't understand. And once you write that down, you can kind of get an answer from the person who made it say, well, I didn't really love this part either, and it's because of this limitation over here. And then the code reviewer can either respond like, oh, that's an unfortunate limitation, or hey, I know a workaround for that limitation that's a cleaner than this one. And so if there's something that you don't understand or a question that you have, it's important to raise it. And doing a synchronous code review means that those thoughts that you have, there's a much smaller barrier to sharing them with the reviewee and to say, oh, all I have to do is say it out loud and then we can start talking about it. So synchronous code review, while it does take, since it's not asynchronous, you have to really block two people to do it and it's going to with two people, it can be a little bit more expensive, but the quality of the feedback that comes back is oftentimes better.

Chris Dzombak
Interesting. I haven't really done very much of that and that sounds like something that it might be good to try.

Soroush Khanlou
It's almost like pair programming.

Chris Dzombak
Right? And I was just going to say, obviously I'm remote, but like, tools that we use for pair programming, like screen heroes, seem like they would work equally well for code review.

Soroush Khanlou
Yeah, absolutely. And it gives you like I think the remote thing is interesting too, because it gives you this chance to defend your code without being able to point or type or do anything. You just have to use your words to express why you wrote your code the way that you wrote it. And so you're kind of on the hook for a better explanation for why you wrote what you wrote. Yeah, and you mentioned a couple of interesting things. You mentioned CI, you mentioned Danger CI, and we talked about Swiftly and a little bit earlier. There are tools basically you can use to make sure that the code review doesn't have extraneous comments in it, that the comments are really focused. So if you find yourself commenting a lot like, hey, we don't really put colons over there, we kind of put the space over here that wastes sort of the bandwidth of the code review. And you can use something like Swiftly to say like, hey, if you check this in, you better have no warnings because if not, we're not going to review it because it's not ready yet. And then having basically having a robot do that also adds to the since the robot is more impersonal, it doesn't feel as much like the person is being attacked during their code review. If they have a pull request open, that gets 20 comments. If they're all style comments, they're small, but they have some cost, they have some load on the person and putting that into a robot makes it a lot easier and a lot more impersonal to get those things fixed without having to take a toll on the actual. So you can get to the meteor issues without taking a toll on the person who is being reviewed.

Chris Dzombak
Yeah, I feel like these style issues, that's not the main goal of a code review. Right. And so offloading that tool to automatically enforce these style rules, it frees you up to focus on things that are actually important.

Soroush Khanlou
Exactly. Yeah. And a similar thing with CI. Where do you want something to download the new code? Run the new code, run the test, make sure all the tests are passing, make sure the build completes, and so that you can know if the build is broken before you merge. Before you merge stuff in that is also similarly important thing. Now. I've never used danger. CI. What kind of stuff can you get from Dangerous CI?

Chris Dzombak
So, Dangerous CI a big thing is it runs swiftly for us and posts a comment that on the GitHub pull request that details style violations.

Soroush Khanlou
Nice.

Chris Dzombak
Let's see. So other things that are in our file that Dangerous CI checks, we're using Quick for behavior driven style testing. And so we have a check to make sure that no focused or exclusive tests have been accidentally committed. And that just makes sure that you don't accidentally focus to run just one test and then commit a commit that's accidentally disabling the whole rest of the test suite.

Soroush Khanlou
Right. So do you count the number of tests and make sure the number of tests doesn't go down?

Chris Dzombak
No. So just the way that you focus a test with Quick is just add, like, where normally you would write like it and then a description of what it does, and then a block that runs a test, you just change that to F. It like F-I-T. And so we just check for any calls to fit in the tests and error out if you've added one of those focus tests anywhere. We have a grep statement in here that checks for misplaced views in Nibs and will give you a warning or will fail the build if there are any misplaced views.

Soroush Khanlou
Nice.

Chris Dzombak
And let's see. We've extracted our build settings so that they're in XC config files instead of in the Xcode project. And so we have a warning here that will check whether any build settings have been added back to the Xcode project. And we'll give you a warning if that's happened.

Soroush Khanlou
Oh, that's cool.

Chris Dzombak
And then finally, there's a script here that verifies that the Xcode group structure matches the project folders, the structure on disk of the project files and folders.

Soroush Khanlou
That's a fun one. I really like that.

Chris Dzombak
Yeah. I've always been kind of split on whether it actually matters whether the Xcode project matches the file system. But the consensus of this team is that the file system should match the Xcode groups, so we have a script to make sure that it's enforced.

Soroush Khanlou
Right. It kind of doesn't matter because the only thing that matters is what's in Xcode. But it's nice to have that consistency in the same way that it doesn't matter if you have one extra space or like trailing white space or something like that. But it is nice to not have it.

Chris Dzombak
Right. It's a style thing.

Soroush Khanlou
Yeah, exactly.

Chris Dzombak
So these are the sorts of things that you can have Danger CI enforce for you but that you don't want to. These aren't the things that are the responsibility of your human code reviewers.

Soroush Khanlou
Right. In as much as you can offload this to automation, you should offload this to automation.

Chris Dzombak
That's true of many, many things.

Soroush Khanlou
Yeah. I've always wanted something where it will basically alert if you have reduced the number of tests. Not that it's wrong to delete a test, but just that if a test accidentally gets deleted or doesn't get run, it means maybe like, let's say that the file in Xcode got removed from Xcode but it's still in the project and so the file looks like it's there but those tests aren't being run anymore. I would want to know about that and it would be nice to have Danger do something, post something and says like, hey, you actually lost this test file. Did you intend to do that?

Chris Dzombak
I think you could probably do that. I mean, there's a plugin to work with xCoV or however it's pronounced, like Xcode's code coverage. And I think that works from a fairly standard J unit style test report. And you could probably look at the number of tests that were run.

Soroush Khanlou
Right.

Chris Dzombak
You could probably do something like that.

Soroush Khanlou
Yeah, that seems worthwhile to me. I would like to set something like that up.

Chris Dzombak
So one other thing that I think is important in code review that we haven't talked about so far is that it's an opportunity, especially for more junior members of your team to work with and get constructive criticism from and learn from the other developers on your team. It's a really good opportunity in a healthy team. It's a really good opportunity for learning and education too.

Soroush Khanlou
Yeah. So it's an inherently social thing because you're all talking to each other and it's kind of set around the code. So is that something that you all do?

Chris Dzombak
Absolutely. Yeah. I don't know that we do anything really formal to achieve that, but people will request code reviews from people who they think may have more experience with this area of the code or with this framework or who they just want constructive criticism from. And that's a really important function, I think, that code review achieves. It's not necessarily important for the project so much as it's important for the people whose code is being reviewed. Right. It's an opportunity to level up and to continue to learn.

Soroush Khanlou
Right. That makes a lot of sense. Have you seen people grow from the stuff they learn in code review?

Chris Dzombak
Oh, yeah, absolutely. Again, I can't think of a specific example offhand, but every day, every week, some small thing comes up in code review and maybe there's a discussion in that code review thread or we may even pop out of that and talk about it with the whole team in slack. And then at the end of it, people have learned things and that's a good thing.

Soroush Khanlou
Yeah, exactly. One thing that I forgot to bring up in the different styles of code review is group code review. I don't know if you ever done this.

Chris Dzombak
No, I don't think so.

Soroush Khanlou
Where you basically pull up your code on a projector or on a TV in a conference room and the whole team kind of gathers around and says, like, let's talk about this. Let's figure it out. Oh, man, on the one hand, it's pretty stressful, but on the other hand, you will really end up with a better thing, and everybody will actually agree that it's a better thing. Whereas if you're just online, it's easy to just kind of tune it out and say, oh, yeah, this is fine, I'm fine with this. Whereas if you're all in the room together, you can really have a super productive conversation about the code and the code review.

Chris Dzombak
So one other thing, sort of just in terms of the social aspects of the team to consider is that it's important that everybody on the team understands that this is supposed to be constructive criticism, right. You're not here to tear each other down. You're here to support each other. And you're all working toward the same goal and trying to help each other. And it's important for whoever's reviewing a poor request to keep that in mind. Right. And be polite, basically. Right?

Soroush Khanlou
Right. For sure.

Chris Dzombak
And it's important for the person whose code is being reviewed to also keep that in mind. Like, this isn't personal. Right. And if it feels personal for people on your team, that probably indicates a much deeper problem on your team that you should really deal with.

Soroush Khanlou
Yeah. The foremost thing is that the code review is about the code and not the person who wrote the code. That is tough to internalize for a lot of people being included because it feels like the person who's criticizing the code, well, I wrote the code, so am I a bad person now? And of course, the answer is no. But to mitigate that, the reviewer has to be, I think, very careful about the words they use. I use a lot of question marks and a lot of gentle suggestions, and I try to be really explicit about like, hey, I think this is a good idea and I would have done it this way, but of course it has no functional difference or like, this is purely style. I'll be really explicit about the level of severity of the comment that I'm making, like, hey, this is just a suggestion. Hey, this is how I would have done it, but your way is fine too. Hey, this is going to cause a bug in X, Y and Z ways. Let's fix that. And being really clear about when I think something is important, I think helps the other person to know, like, oh, this is just a difference of opinion, rather than like, I'm bad, right? Yeah. So I think that can help a lot because I'm a millennial, I phrase a lot of things in terms of questions, and I add question marks at the end, like, hey, I think we should do this thing and then add a question mark at the end to kind of soften it a little bit. Or what do you think about X, Y, and Z? And it is cheesy, but it does really help the reception of that code review comment. Ultimately, it's being read, so you have to use your punctuation and your emojis and your wording and the tools at hand to make it be read the way that you intended it.

Chris Dzombak
Sorry, was that a question?

Soroush Khanlou
I'm a millennial, so I ended up with a high rising terminal. So you thought it was a question, but it was not a question?

Chris Dzombak
Yeah, I'll absolutely do the same thing, too. I will often instead of phrasing something, this is wrong, because, I mean, I could be wrong, too. I, too am human. We'll ask, have you considered this case? I don't know if maybe that makes me come off as more of a jerk, but I don't think so.

Soroush Khanlou
No. I think being aware of it is usually enough to say, like, okay, this person's not trying to be an asshole or whatever.

Chris Dzombak
Yeah.

Soroush Khanlou
So the last thing that we should, I think, talk about is what do we look for in code reviews? Like, what kind of things are we trying to find and what kind of things stand out to us as, like, code smells and red flags?

Chris Dzombak
Boy, yeah, it's such a big topic, right. And I don't know, like, I don't have a comprehensive list. I mean, go through I basically look at the code, look at the diff, look at the context where that code right. You're not looking just at the code that's changed. You're looking at where it is and how it's being used and think, like, does this make sense at a high level? Right. In Swift, we don't necessarily have to check, does this thing accept a null parameter or whatever, right?

Soroush Khanlou
Yeah, which is fortunate.

Chris Dzombak
But you do look and think, okay, do things that do APIs that accept optionals or return optionals. Does that make sense semantically? Right? Like, should this be optional? Here, look at interface design. Right? Look at whether the single responsibility principle is slowly being violated. A lot of the stuff that we've talked about so far on this podcast are things that you you will look for during code review. Right?

Soroush Khanlou
Right.

Chris Dzombak
I also I try not to be really picky about naming because it seems like a fairly well, that's not entirely true if it's something like a parameter name or like a variable name. Internally, I try not to be very picky about naming because that seems like very NIT picky. And reasonable people can disagree on names, and neither of us is wrong. I will be more picky at looking at names of types, particularly public types, just because they're likely to be more widely used and more widely read.

Soroush Khanlou
Right.

Chris Dzombak
What kinds of stuff do you think about?

Soroush Khanlou
I think about a lot of the stuff that Swift is good at is list programming. And I try to make sure that things are using the highest level list abstractions that they can. So if something is a for each, that adds a bunch of things to an array, that's probably a map. If something is a map and has side effects, that probably should be like a map followed by a for each, stuff like that. Definitely I look for I look for long methods that could be broken out into their own types, especially if I can come up with a good name for it. If I can, I'll say this is a bad pitch for a name, but here's where I would start and maybe you can try renaming it. So sometimes like extra types that can be pulled out, I look for things that are written differently than I would have written them. Not to say that the way that I write them is the only way to write them, but that they must have had a reason for or maybe they didn't. And that's worth knowing too, for writing things the way that they did.

Chris Dzombak
And that can help even if you just want to understand why this code is the way it is. Right. That's going to be helpful for you in the future. I'll look for anytime that you're dealing with arrays or anything with ranges, really consider and hopefully maybe there's test coverage, hopefully there's test coverage. But consider is like logic around ranges with strings and arrays, especially with Swift strings. It's so complicated. Like is this code correct? Right. Just because that's something where I mean, I write errors all the time and other people do too. And having someone look at it and really consider whether it seems correct is very useful, for sure.

Soroush Khanlou
One Nitpicky, one I look for is optional strings and optional arrays. Like if the thing can be better represented as just an empty array or an empty string for the Nil case, sometimes it is right for it to be optional or wrapped in some other enum. But if it can be represented as an empty array cleanly, then I'll push for that. Another one that I'll sometimes look for is if there's too much state. I had one case where there was kind of a data source for a table view and there were three arrays that were being held. It was like kind of all of the data, the data being filtered and then sorted by the user's ducted distance to some location based on the user's location and then the data without the user's location because they might not opt to give you their location. So it was sorted by name and these three arrays fell out of sync in a certain case and caused bug. And so I'll say like, well, these three things in this case maybe could be two things, maybe it could be.

Chris Dzombak
One thing anywhere that you have that you're trying to keep different state in sync, that's often a big code smell, basically.

Soroush Khanlou
Yeah. As much as you can make it computed, you know, that's always going to be correct and not have to be kept in sync manually.

Chris Dzombak
Right.

Soroush Khanlou
Another one that I look for is if there's a primitive on a View controller. So if there's like a bool or an int directly on a View controller, it may make sense to move that to a type with more semantic meaning or move the code related to it into its own type and give it more powers. And sometimes that can make a lot of sense. Look for stuff like that, there's a lot of little things. I think we could do a whole episode on little things that we look for in code review.

Chris Dzombak
Yeah. In fact, if we wanted to do an episode about that, we should plan it ahead of time. And then for the week leading up to the recording, note things that we all the comments that we make in code reviews.

Soroush Khanlou
Now, that's a good idea, but that's about everything I have for the code review topic. What do you think?

Chris Dzombak
Yeah, I don't think I have anything much to add. We sort of touched on different styles of code review, the things that you look for in code review, the things that you can automate in code review. And we mentioned a little bit about the sort of human and social aspects of code review, which I think really are important to keep in mind, especially if, like with my team, especially when some people are remote. It's very important to keep in mind that everyone involved in the process is human and is trying to do their best, and that you're here to help each other.

Soroush Khanlou
Absolutely. Cool. Well, as always, Chris, it was a pleasure and thanks to all the listeners for hanging out and listening to us blather for another 30 minutes.

Chris Dzombak
Yeah, it's always great to talk to you. Thank you so much to our listeners and supporters. We really do appreciate it and we will talk to you later.

