Speaker A
Hey, how's it going?

Speaker B
Pretty well. I'm tired. It's been a long day.

Speaker A
Classic Chris. Tired after a long day of hard work.

Speaker B
Yeah, well, tired after a long day anyway. Yeah, no, I don't know what it is. Just ready to go to sleep and it's eight at night.

Speaker A
Yeah, man, you got to get that sleep.

Speaker B
Yeah. Glorious life of a late 20 something, I guess. Dive right into this, tying into me being tired here, kind of. We have some news.

Speaker A
Yeah. This is unfortunately going to be the last season of this show, right.

Speaker B
So for those of you who are following along here, we've been doing this in seasons of 20 episodes, kind of thinking that this gives us an opportunity about every half a year to evaluate, is this something that we still feel like we want to do and have time to do and it's useful for us to do? And so we're coming up on that here with episode 70. And yeah, we've been talking about this and kind of landed on like, we're going to shut down the show.

Speaker A
Yeah, we've talked about a lot of things over the past two years and we've had a lot of fun doing the show.

Speaker B
Has it really been two years?

Speaker A
Man, it really has. We started Summer of 2016.

Speaker B
Really? Man, that is kind of unbelievable.

Speaker A
Yeah, we talked about a lot of stuff, and frankly, we think we've said what we want to say about a lot of programming topics and there will be more stuff that happens in the future that maybe is worth talking about. But as it is, we're kind of running out of steam and running out of things to talk about.

Speaker B
Yeah, that's exactly. We're running out of stuff to talk about. A lot of the early episodes that I know a lot of you appreciated were discussions that Cerci and I had just had ongoing for years. And then we've talked about them for a lot on the podcast and kind of moved on from those discussions to other things and yeah, our episode ideas list is running pretty thin these days.

Speaker A
It's getting dry down at the bottom of the barrel. Our 70th episode may be very special. We haven't nailed down exactly what's going to happen there. So no announcement yet, but stay tuned.

Speaker B
Stay tuned. It could be special.

Speaker A
Could be special. So yeah. So that leaves us with episode 67.

Speaker B
Which welcome yes, welcome to episode 67 of Fatal Error.

Speaker A
That's right. I'm Sirous.

Speaker B
I'm Chris. We haven't done that intro in a while.

Speaker A
Fun fact, someone actually started listening to the show kind of in the middle, and they were interested in some of the Swift Evolution topics, and they were not sure which one of us was which.

Speaker B
I mean, that's totally reasonable. How would you know?

Speaker A
Yeah, I mean, we used to be really diligent about the welcome to Fiddler. I'm Sirush. I'm Chris. But we just sort of dropped off.

Speaker B
Yeah. Especially earlier this season, around, like, episode 50, I think we decided to do a little bit less formal intro less formal format.

Speaker A
Yeah. So I am Sirushi as Chris, and we want to talk about a couple of things today.

Speaker B
Yeah. So we've gotten news out of the way. The next thing was just that I wanted to check in on your Swift Evolution proposal. What's going on there?

Speaker A
Yeah, if you've been a listener to the show, you'll remember kind of my ongoing saga with Swift Evolution and trying to get something in. I pitched something that was well received, which is the function count where which tells you how many elements in a sequence pass a test. And it's a super useful function. And I pitched it, and there was good reception. And so I kind of asked around and I said, what's the next step? And they said, the next step is write up a proposal and write a sample implementation so we can see that exists and we can actually merge it in. Okay, that makes sense. And I started with the implementation just because I knew I could. Obviously, I could definitely write a proposal, but the implementation I wasn't sure about, and it took me about a month from start to finish, but I did end up finally getting everything working and everything building. And I added my function and I added my tests, and I ran my tests, and I verified that my tests are actually doing the thing I thought they were doing for a while. They were not being executed, which is always fun. Biggest thing with unit tests is make sure they're actually executing. Don't get bitten by that.

Speaker B
I was briefly bit by that earlier today on a project at work.

Speaker A
Yeah. Honestly, it's like, I think for me, the number one rule of unit test is, like, is this unit test actually running?

Speaker B
I mean, it's up there. In my case, it was pretty obvious because I had written a test that I thought was supposed to fail, and then it didn't fail. And then I was like, Wait, what's wrong here?

Speaker A
Yeah, exactly. That's why they always say red, green, refactor. You need that red step so that you know that the thing fails in the way you expect it to fail.

Speaker B
That's one of the reasons. Yeah.

Speaker A
Don't skip that red step.

Speaker B
No.

Speaker A
Yeah. It turned out what was going on with my thing was I was running the tests, but I wasn't recompiling the actual code that the test was running against. And so I was just continually running or I hadn't recompiled the test, I was just running the tests. So while I thought that I was running the test, I was actually running, like, an old binary of the tests, and my changes to the test were not being executed. So I figured that out for a couple of other things. One thing I want to give a shout out to is Harlan Haskins and Robert Whitman codify on Twitter. They gave a talk at the conference in Switzerland's, app Builders, and they go into really good detail about exactly what you should do and what the steps are and how to run tests and how to build everything. That was actually very helpful. I kind of set aside a Saturday to do it and there was a lot of waiting around for compiling and stuff.

Speaker B
Yeah, definitely. Is there a link to that online that we can put in the show notes?

Speaker A
Yeah, they made the videos really quickly, so yeah, those videos are okay.

Speaker B
Awesome.

Speaker A
I'll definitely put that in the show notes.

Speaker B
Thanks.

Speaker A
And oh, one other thing I learned is remember when we were talking about this a couple of weeks ago and I read in Ole Begamin's blog that you're supposed to always compile a release build instead of a debug build.

Speaker B
I vaguely remember that, yeah.

Speaker A
And they say, like, the release build is way faster because the optimizations are different. So I tried a release build just to see how bad could it really be? Let me just do it. Or sorry, I tried a debug build, the slow one. How bad could this honestly be? Let me just run it and see what happens. It was 3 hours and 20 minutes.

Speaker B
That's pretty bad. Well, for comparison, how long is a debug build or release build?

Speaker A
About 40.

Speaker B
Okay.

Speaker A
Clean. I think 20 or 40, I can't remember which. But yeah, it's long, but it's not like leave, go to the movies, come back. And it's still not finished compiling long.

Speaker B
Right. Yeah.

Speaker A
So once I got all that stuff working, I kind of repurposed the filter tests because count where is a lot like filter, except instead of testing against some output array, you're just testing against some output count.

Speaker B
Right.

Speaker A
And so I just repurposed all those tests and opened up the pull request for both the implementation and the proposal itself. So the implementation goes into the Apple Swift repo and then the proposal goes into the Apple Swift Evolution repo.

Speaker B
Got you. Okay.

Speaker A
Yeah. And so when I pushed the button, I was very excited. I was like, okay, I can't wait to let's do it. I'm ready. And of course, nothing's happened since this was like two weeks ago. Yeah.

Speaker B
Everyone's busy getting Swift 4.2 out the door now, right?

Speaker A
Yeah. Although I'm not really clear what Swift 4.2 is. I didn't know there was going to be another point release of Swift Four. I thought we were going straight to Swift Five.

Speaker B
I think it sounds like they're at least aiming to get some hashable changes in for Swift 4.2. I was listening to Swift Unwrapped earlier today, had a new episode about that.

Speaker A
Okay, cool. So it's not like Swift 3.2 where it's like a compatibility layer for the next version of Swift.

Speaker B
I mean, I'm not sure about that. I know this one thing about the release. I don't know what else is supposed to be in the release.

Speaker A
Yeah, we'll have to look into that. Yeah. Swift 4.2, but yeah, they're all busy with dub dub stuff and 4.2 stuff.

Speaker B
All right, that's coming up.

Speaker A
Yeah. Also dub dub is coming up soon.

Speaker B
That's almost next, practically in about a month. Yeah.

Speaker A
As this releases, it will be like, a month from when this comes out. Right. So I opened these two PRS, and I kind of started thinking, like, actually, probably nothing's going to happen today. Is it because there's a process to these things and they have their own work that they need to do, and they can't automatically they can't immediately deal with the stuff that I send them. So I kind of looked around at some other PRS that were very similar to mine. So I looked at Chris Idolf did a PR for reduce in two, which is like a version of reduce that's in out. And that took like six or eight weeks to go from proposal to merged. So I've kind of just taken a chill pill and I've accepted that this will take some time and people will get to it when they get to it. Chris Lattner commented in my pitch thread and said that he thought it was a good proposal that fills, like, an obviously empty spot in the standard library. So I think it's going to go through. It's just a matter of it being a waiting game.

Speaker B
Yeah. I mean, I think that's the right approach. What can you do here? Just wait and see.

Speaker A
Yeah, pretty much.

Speaker B
Cool. All right. I remember when we talked about this before. You had run into a problem where your implementations seemed to have some side effect or expose some dependency on some implementation detail elsewhere in the standard library or in the tests. Do you remember what I'm talking about?

Speaker A
Yeah. So that was a different change that I was trying to make. I was trying to optimize drop last.

Speaker B
Oh, that's right. You were trying to always have a lazy drop last.

Speaker A
Right, exactly. Yeah. So I may actually take another crack at that now that I have a little bit more experience with this stuff.

Speaker B
Okay.

Speaker A
But no, that was a different set of things. And what ended up happening with that was when I ran those tests. Like, the tests for drop last succeeded, but the other tests elsewhere in the code failed.

Speaker B
Right.

Speaker A
And it wasn't really clear why they were failing, which actually that happened here too, which was really cool.

Speaker B
This was a purely additive change, though, right?

Speaker A
Yeah. So it's a really interesting thing that broke. Yeah. There's a set of tests for the diagnostics that come out, and diagnostic is a fancy word for, like, warning or error. So anytime you see a warning or an error in Xcode, the Swift team calls that a diagnostic. And in this particular case, there was one diagnostic that was written such that if you tried to take the count of an array and call it as though it were a function, it's a property, so you're not supposed to put parentheses after it.

Speaker B
Right, okay.

Speaker A
But if you tried to call it like a function, the old error message was really inscrutable. So they added an extra diagnostic and they wrote some code to have a better diagnostic that said, like, hey, you can't call a method of type int. You can't call an object of type int because calling is like, what you do with the parentheses. And int is what count evaluates to and you can't call an int, basically.

Speaker B
Right, okay.

Speaker A
In the way that you can call a function. And so what happened here is that now because you can call count, because count is now actually a function that has a parameter label called where the new error is it's a wrong number of parameters for your function, which that's a correct error, but it's not what the test was expecting. And so that had to be fixed.

Speaker B
Yeah. Okay. That makes sense.

Speaker A
Yeah. So that wasn't too scary. Definitely. The drop last thing was a lot weirder.

Speaker B
Yeah.

Speaker A
Don't know how to fix those things. I'll take another stab at it, but it'll probably be a while before I do.

Speaker B
Okay, interesting.

Speaker A
Yeah.

Speaker B
This sounds like at least something that it's fairly clear what's going on.

Speaker A
Yeah, definitely. I was really nervous about it at first because I was like, is this even my fault? I didn't touch anything in diagnostics, and once I read it, I was like, oh, I do see what's happening here, and this is correct, or whatever.

Speaker B
Yeah. Cool.

Speaker A
So yeah, so that's what's up with that. Anything else is interesting that happened with that? Not really. I hope it gets merged in. It would be nice to have a little bit of a tiny little finger in the pie of Swift.

Speaker B
Yeah, that would be awesome. Nice point of pride.

Speaker A
Yeah, for sure.

Speaker B
So another thing that I think we wanted to talk about today I don't know. You have anything else on that?

Speaker A
I don't think so.

Speaker B
Another thing that we thought we would cover today is this blog post from Dave DeLong entitled, you should Give That Presentation. And I thus far have only have skimmed this blog post or just shared it with me right before we recorded, but it's something that really resonates with me. Like, we've talked to think a couple of times before about giving presentations, giving talks, and writing blog posts. Right. And something I've expressed that I'm sure you remember, sirous, is like, I don't really know, what should I give a talk about? What do I know enough to give a talk about? Right. And here, like, paragraph three, dave is like, you may question whether or not you know, in quotes enough to give a presentation. So this seems like something that really would really resonates with me. Do you want to try to give me to pitch me this article?

Speaker A
Yeah, I would. I just thought it was a very nicely written, nicely expressed blog post about this thing that a lot of people are nervous about. And I think he really lays out why you should what kind of talk you can give, why you would be the best person to give that talk. I just really appreciated the way that he broke it down and kind of pushed people and said, hey, you should do this thing. And then at the end, he also makes an offer of if you are preparing to give your first presentation, he's down to help.

Speaker B
Cool.

Speaker A
Yeah, the three different sort of types of talks that he talks about are one is sort of technical presentations where you're just talking about either a new API or trying to explain something or break it down or you released a new library or something like that. And he kind of breaks that down as like that's, like the kind of bread and butter of a thing. And you can always give that talk because it's just technical, it's useful for everybody, and you just want to teach people some technical thing, which I think I think that's a really good baseline for, like yeah, when we're starting out technical might be the best thing that we can do. Just because we've dug so deep into this particular API or how this thing works or how it behaves around the edges and stuff like that, that we have some particular knowledge that other people might want to know, which is yeah, I think it's a really great place to start with a type of presentation that you might want to give. And then the second one he talks about is like the kind of he calls it the inspirational presentation, which is not really about the code, per se, but it's about taking you and saying, hey, you can do this. Thing, giving you the motivation and the inspiration to kind of make a big change in your life, perhaps or do something that you maybe weren't so sure about before. I remember when back in 2012, I went to Second Conf, which is in Chicago. Do you remember this conference, Chris?

Speaker B
No, I don't.

Speaker A
Second Conf was this pretty good conference. It's like Chicago is like a second city. So it's the Second Conf after, I guess, dubbed Dub, and it ran for four years, like so many conferences do. And I think 2012, 2013 was the last year. And I remember kind of coming back from that and just feeling so energized and feeling so like I could kind of take on the world. You hear from all these people who have done these things that you want to do. They've started businesses or they've made products that you are very impressed by or that you look up to. Man, maybe I could do this maybe I have the chops to go and follow in the footsteps of these people. And I don't think I've actually ever said this publicly, but second Comp 2013 convinced me to quit my job.

Speaker B
Oh, really?

Speaker A
Yeah, I had a job. I wasn't very happy there and I was kind of suffering through a bunch of stuff and a bunch of changes and it kind of made me realize like, you don't have to put up with this, you can do something different, something better. And that kind of motivational presentation, that kind of nice feeling that you get after a conference of just like I got a cumulative 9 hours of sleep this whole weekend but I just feel like a million bucks and I feel like I could take on the world. I think there's like so much value there.

Speaker B
This is one thing, we'll just go back to you for a second. So is 2013 then when you started doing consulting?

Speaker A
No, I actually switched from one startup to another startup at that point. Yeah, it was just more about not feeling valued at the startup that I was at. Yeah, totally finding a place that fit a little better.

Speaker B
Yeah, that's great. I think that there are definitely some talks like this at Strange Loop too. This is a conference that I've gone to the last couple of years and that I've really enjoyed. There are some really great technical presentations and some good inspirational presentations and it's a really nice mix of hard technical information. Interesting stuff that I'm probably not going to, isn't immediately relevant to a programming language that I'm working in, but is interesting to think about or has interesting ideas to take away and talks that are more inspirational, more motivational, more sort of how do we say this exactly? Right? There's this whole world and you're in one part of it and you can like I don't know, I don't know.

Speaker A
Where I'm going with this, but it's stimulating and encouraging.

Speaker B
Yeah, exactly.

Speaker A
I literally opened dictionary and went to thesaurus mode and typed in inspiration. But that's also how I read my code and how I wrote my blog post. Please in this time of need do not add me.

Speaker B
Fair point. Okay.

Speaker A
Yeah, no, but it is really just like it changes how you see things, it provides a new perspective and changes your feeling towards stuff.

Speaker B
Right. Makes the world feel like a little bit bigger.

Speaker A
Yeah, there's this really nice distinction.

Speaker B
Amazon is telling me that Earth is whatever planet from the sun. Anyway.

Speaker A
Don'T know why, but classic Amazon robot. There's this really cool distinction that I've always wanted to write about on my blog, but I've never quite nailed down what the post is about. So I haven't had a chance to flesh out what that post is. But it's this distinction between exploration versus exploitation and I don't know if you've ever heard this before, it's basically this idea of there are some things that, you know, have some value, right? Let's say ten points of value, and you can continue to do them as much as you want and you always get ten points of value. But you also need to and that's the exploitation. You're taking the thing that you know, and you're exploiting it to generate that value. But you also need to kind of explore as well because there may be other skills, other places, other situations where you could do the same thing and generate more value or less value or do a different thing and generate more value or less value. And that value function can be anything. It can be how much fun do I have scuba diving versus how much money do I make? Versus it could be like, how much do I enjoy the books that I read? It could be any value that you're trying to maximize. And you have to find a balance between exploration and exploitation. Because if you do too much exploitation, then you'll never find the global maxima.

Speaker B
Right?

Speaker A
And if you do too much exploration, you'll never actually achieve that maximum. Maximum.

Speaker B
Yeah. So just googling exploration versus exploitation here. I hadn't heard this before. This is really interesting. I have found a blog about productivity strategies. Yeah, right. Exploitation requires our complete concentration to do better what we are doing. And then exploration allows us to get away from our current reality, visit other realities and find new horizons. This is the origin of innovation.

Speaker A
That's how I see a lot of these conference talks is, yeah, I can sit here and jam my fingers into the keyboard and make things pop up in Xcode, but at some point I need to get out there and see am I jamming the right things into Xcode? Like, am I typing the right words or should I be typing different words? And I think that that's one of those things that those motivational, those inspirational talks at conferences can really help you. And sometimes it's not the talks, also sometimes it's the hallway conversations or whatever it is, but it's that deeper exploration. Yeah, if you've ever heard of the multi armed bandit, which is like a better way to a B test, this is also exploration versus exploitation. Yeah. So you just have to find that balance for yourself. And I find that going to conferences periodically can give you some of that exploration that you need.

Speaker B
Yeah, absolutely.

Speaker A
So sort of like to kind of keep going with this blog post. The last thing that Dave talks about is he says there's a more fundamental type of presentation that underpins both of the other kinds, both the technical and the inspirational, which is the experiential one. And the experiential talks are the ones that, as he puts it, everyone's qualified to give. So it doesn't matter who you are, you have experiences. I talked to people and I talked to friends, some friends who listen to the show and probably can hear this now. Who. They tell me stories and they're completely bonkers. And I'm like, this is something that other people would love to hear about. Whether it's their relationship with their boss or whether it's a thing that they went through with their code base, or whether it's, like, some new approaches they're trying out all this stuff that you might think that you're the only person out there, or you might think you're just somebody who's doing this thing that everybody's doing. But some of these stories that I hear are just completely, totally nuts and deserve to be shared on the stage and deserve to kind of have that voice be put out there.

Speaker B
Cool. Yeah. I guess I hadn't thinking about possible talks to give, obviously, or maybe not obviously, but I've tended to gravitate toward the technical talks and hadn't even really thought that much about the sort of experiential genre of talks. But that's totally a thing now that I think about it, and totally like a kind of talk that I have enjoyed before.

Speaker A
Yeah, for sure.

Speaker B
And so this is definitely something for me to think about, I feel like, yeah, if I wanted to give a talk, it may well be something more like this.

Speaker A
Yeah, for sure.

Speaker B
This is good food for thought.

Speaker A
Yeah. Thank you. Just give you one example. You led a redesign, or rewrite, actually, of the New York Times app, and you oversaw that for almost a year.

Speaker B
Pooh boy. Yeah, I did. Yeah.

Speaker A
I mean, there's a lot of things that you learn there, and they say, never do a rewrite, and that's probably true. But having done that at scale and at a company on an app that has millions of users, there are things that you learn that nobody else knows.

Speaker B
That's probably true. Yeah. And there are things, both technical and cultural and team related. There are things related to doing this at a big company versus doing a rewrite at a small company, if you're going to do that. There are things, like things I learned about myself, like looking back on that experience, there are definitely things that I could have handled better from a team, from a technical leadership point of view, too. Yeah, I should think about that, especially with the distance of that being, what, about a year ago in my life now.

Speaker A
Yeah. And also I want to add that I think that a lot of this stuff is cyclical as well. Back when second conf was still around, almost every conference, I feel like, was more focused on the softer side of things. The more emotional talks, the more experiential talks, the more basically less technical. There was almost never any code on stage at these places, and I feel like that pendulum has definitely swung around the other way. And now there are conferences where almost every talk is like code on the slides, teaching you how to write code teaching you how to think about things like, let's say, architecture or Structuring code or whatever. It didn't used to be like that. Like the first cocoa love, there was one talk that had code on the slides, and it was a designer and it was CSS. That's insane. But now you'll see, like, Trisift, let's say Japan has tons of code talks. They're very, very code heavy. So these things will also kind of ebb and flow. So if you feel more comfortable with technical, now might be a good time to dive in. If you feel more comfortable with sort of the more motivational type or the more emotional type of talk, then maybe something where you can kind of help swing the pendulum back the other way. Somebody was talking to me. They were like, they want to start a new conference and they want to focus it around feelings and around emotions and stuff that could be really good rather than focusing it on code. And I think that's just part of this sort of pendulum.

Speaker B
Yeah. I was going to say, if we're in a part of the pendulum now where everything is all technical talks, that seems like a good space to maybe not to try to compete with more technical talks, but to throw in a talk from the other side of the pendulum. Right?

Speaker A
Yeah, absolutely. Talk about what nobody else is talking about.

Speaker B
Exactly.

Speaker A
Yeah. And then Dave kind of closed out his blog post by saying that he has an open offer for anybody who wants help with their first presentation. I just want to say I'm actually open to the exact same thing. If you are listening to this and you want to give your first talk and you're a little nervous, hit me up. Or hit both of us up. I think Chris would also be happy to help.

Speaker B
Yeah, absolutely.

Speaker A
Hit us up and we'd be down to help and to talk you through the conversation, look through slides and get you to a more confident point. So definitely know stuff about that.

Speaker B
Yeah, I think both of us definitely are open to doing that.

Speaker A
Yeah, for sure. You got any conferences coming up? This the rest this year, Chris?

Speaker B
No, I don't have anything planned right now.

Speaker A
I guess strange Loop is probably happening in the fall, right?

Speaker B
Yeah, I assume so. I actually haven't looked at that too much, but I should add that to my to do list.

Speaker A
September 26 through 28th. Yeah, it's coming.

Speaker B
Gonna look at that this week. I would love stuff on my calendar.

Speaker A
That's strange loop. It's such a it's a good conference.

Speaker B
Yeah, man. I'm thinking, like, yeah, this has actually been a really useful podcast for me, thinking maybe this would be an interesting talk to give.

Speaker A
Yeah, I think it'd be cool. I think it'd be really interesting.

Speaker B
Maybe the last couple of episodes of the podcast. Let's shift from anything technical to just like. Check in about what our experiences this week and how we're doing that's.

Speaker A
Right. How are your feelings this week, Chris?

Speaker B
I'm tired, sir. You know that already.

Speaker A
Yeah. Well, I could pretty much guarantee with 100% odds that if we're recording a podcast, Chris is going to be tired.

Speaker B
Yeah, I don't know why that is. It's not podcast related. I'd be tired if I weren't recording now, too.

Speaker A
Yeah, it's what? 08:00 P.m.? It's getting pretty late, Chris.

Speaker B
It's almost nine.

Speaker A
Yeah, cool.

Speaker B
Yeah. I guess on that note, thank you so much for listening.

Speaker A
Thank you for listening and I'm going to sleep.

Speaker B
And thank you for your support. And I'm going to sleep. We have three more episodes, right? 68, 69, 70. Yeah. And so we'll try and come up with some good topics for the rest of those, for sure.

Speaker A
Yeah. On the patreon note, thank you to everyone, seriously, who's supported us over patreon over the last I think we've been doing patreon for a year and a half now. Thank you so much. Honestly, this podcast would have probably ended without patreon.

Speaker B
Oh, yeah, definitely.

Speaker A
Hunting down ads every week was not something that was going to be possible, but the fact that we could put this patreon up and have you all support us really made a very big difference. And so, from the bottom of our hearts, thank you so much. We will pause the patreon after the 70th episode comes out. So I think the last time people will get billed is probably June 1 will be the last time you're billed, and then the patron will be paused. So you won't get charged, but you'll still have access to that back catalog. So if you want to go back and listen, you can, but you won't be getting charged for it. And we think that's the most fair thing we can do on that front.

Speaker B
Yeah.

Speaker A
So, again, thank you so much. Really, it means the world to us that you helped us make this podcast.

Speaker B
Yeah, thanks for your help. On that note, I'll talk to you next week, sirish.

Speaker A
Sounds good, Chris. Later. Bye.

