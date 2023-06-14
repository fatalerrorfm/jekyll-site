Chris Dzombak
Oh, man, this is going to be great.

Soroush Khanlou
All right, thanks, everyone, for coming.

Chris Dzombak
Yeah, thank you for coming. This is way more people than I expected to show up.

Soroush Khanlou
Chris has very low expectations of all of you.

Chris Dzombak
Not what I meant.

Soroush Khanlou
So how many people are regular listeners of the show? Cool. We got a few. Got a few. All right, cool. We got some follow up to do.

Chris Dzombak
We do, yeah.

Soroush Khanlou
So if everybody was listening to the show, strap yourselves in.

Chris Dzombak
So one of the things we talked about, one of the episodes that we got a lot of great feedback about, that we really appreciated, was where we talked about what all did we cover? Imposter syndrome.

Soroush Khanlou
Yeah, kind of like starting a new job and not really knowing your where on the code base and kind of having to feel it out and having to figure out where you fit in and how to properly contribute to a new team, basically.

Chris Dzombak
Yeah, absolutely. So just as follow up, I had a story from last week now, totally non tech related, but very impostor syndrome related, and I thought I would share that.

Soroush Khanlou
Yeah, fire up. Let's go.

Chris Dzombak
All right. So some friends and I were doing a long bike ride last Saturday, and ahead of this, I was having some pain with my right shoulder. And one of my friends recommended that I go see this sports massage therapist that she really likes. And so I get to this place Thursday morning, and this is totally a new experience for me. There's, like, exercise equipment everywhere. There's, like, metal music playing in this place.

Soroush Khanlou
You went to a gym? That's called the gym.

Chris Dzombak
It's a new experience for me. And I get there and I walk in. I'm just like, wow, I so do not belong here. Like, this is for people who are, like, athletes and, like, do athletic things. And like, that's totally that's imposter syndrome again, right? Like, I'm here because I'm preparing for this, like, big athletic thing.

Soroush Khanlou
Don't you like dozens of miles a weekend on a regular basis?

Chris Dzombak
On a regular basis, yeah.

Soroush Khanlou
And so that's that kicking in, right?

Chris Dzombak
Yeah, totally. Like, I totally belong here. But, like, this new thing and there's this music, and this guy is people wearing workout clothes.

Soroush Khanlou
Very intimidating.

Chris Dzombak
Yeah. I don't know what the point here is. Just like, impostor syndrome is a real thing and affects everybody. So you got this, you're cool.

Soroush Khanlou
We talked to someone who even had imposter syndrome in this city in this nine block radius of just like, well, do I know the right things to talk to the right people? And how does this all make me feel? And I think that it just pops up everywhere. Cool. Other little follow up, we usually do a lot more technical stuff, a lot more programming stuff. And for the most part, we're talking about, like, design patterns, coding, which is really fun to do. Over, like just audio. We have no images, no anything. One time we put a code block in the show notes. That was pretty useful.

Chris Dzombak
I think we must have done that more than once.

Soroush Khanlou
We did it literally once. Yeah, it was just like that's.

Chris Dzombak
Probably for the best.

Soroush Khanlou
The galaxy brain enum. We had like small brain, medium brain, galaxy brain. So we wanted to kind of start off with the WWDC stuff and we wanted to talk about Swift and kind of where it's going and what we learned.

Chris Dzombak
Yeah. I don't know exactly where to start here, like, what we want to cover because we've covered a lot of the stuff that's new in Swift over the last several months because it's been like an open development process. So I don't know what you I.

Soroush Khanlou
Think the big thing that we didn't know was exactly what was going on with the versions. We thought that API stability was going to happen in the fall with Swift Five, but what we learned was that is happening next spring. They're pushing that off, which makes a lot of sense, honestly.

Chris Dzombak
Yeah. I mean, that's fine. Deadlines slip in big software projects. And this especially, I think, is something where you want to get it right.

Soroush Khanlou
Yeah, right. I remember opening that, the Swift code base, like add stuff and make pull requests. And I'm pretty sure it's the biggest software project I've ever opened on my computer.

Chris Dzombak
I think that's true of me too.

Soroush Khanlou
That seems right. I don't think we've done any messing with Linux or whatever. No, we learned that Swift 4.2 was coming actually, like a week ago, I asked someone and I said, hey, I've been hearing about Swift 4.2, but there's no release page for it. There's no date. What's happening? And this person was just like, I cannot comment on unreleased software. And I was just like, oh, okay, so there's something going on here. That's what we learned. We learned 4.2 is coming out in the fall and it's going to have a bunch of little tiny things and then five, which is going to be kind of the bigger abi stability things can happen in the spring.

Chris Dzombak
Yeah.

Soroush Khanlou
Do we want to take any bets on whether five and abi stability will slip again?

Chris Dzombak
I'd take bets. Yeah. I don't know.

Soroush Khanlou
Which side would you take and what kind of odds can you give me?

Chris Dzombak
I think they'll probably hit spring.

Soroush Khanlou
I think so. I think they're going to miss it. Yeah. Unfortunately, this podcast is ending, so you'll never find out.

Chris Dzombak
What you should do is subscribe to Swift Unwrapped instead, which I think has always done it.

Soroush Khanlou
Yeah. Subscribe to two people who are smarter than us and know more about this stuff than us.

Chris Dzombak
Yeah, that's going to be a safe bet.

Soroush Khanlou
And then that's like the kind of Swift follow up. And then the other thing that we love to talk about is animoji.

Chris Dzombak
Right.

Soroush Khanlou
We got to do a little animoji segment before we move on.

Chris Dzombak
Ios twelve. Adds memoji.

Soroush Khanlou
Right.

Chris Dzombak
How many people here have ever used animoji?

Soroush Khanlou
Who sent an animo?

Chris Dzombak
Most of the room.

Soroush Khanlou
We should tell the people who are listening to the recording. How many people I just said it's.

Chris Dzombak
Most of the room.

Soroush Khanlou
Most of the room.

Chris Dzombak
That's good. Okay.

Soroush Khanlou
All right. My bad.

Chris Dzombak
How many people use animoji on any sort of regular basis, though? That's about what I four people, sir. How often do you use animoji?

Soroush Khanlou
I probably do it's, like, when I send them. I send, like, six in a row, but that's like, every two months.

Chris Dzombak
Okay, that sounds about right.

Soroush Khanlou
Yeah. So we got four new characters, and we got the memoji. Yeah, I was in a memoji today.

Chris Dzombak
I haven't been in a memoji yet. I don't have iOS twelve on anything.

Soroush Khanlou
Friend of the show, Curtis Herbert, we were hanging out, and he was setting up his phone. He actually put iOS what are we on? Twelve onto his phone. Who put iOS twelve on their phone? These polls are good. Let's do more polls. Like five people. Okay.

Chris Dzombak
On your daily it's really great audio content.

Soroush Khanlou
It seems like it's not so bad. I might do it soon. Live life on the edge. Yeah, maybe after ice ones.

Chris Dzombak
Yeah, that sounds like probably after ice ones.

Soroush Khanlou
Don't go on an international trip with a beto. It'll never end well. And so Curtis pointed the selfie camera at us, and he had his memoji on him, and I was in the other, like, half of the picture. And then memoji swapped over, and it became my face.

Chris Dzombak
Whoa.

Soroush Khanlou
So I stuck my tongue out. We took a picture.

Chris Dzombak
All right. Because there's tongue detection.

Soroush Khanlou
Yeah. Tongue detection. So tongue detection is huge. No inappropriate jokes.

Chris Dzombak
That's going to bring an emoji back, I think, is tongue detection.

Soroush Khanlou
That's what we need.

Chris Dzombak
That's what's been holding me back.

Soroush Khanlou
Do you think the skull is going to have a tongue?

Chris Dzombak
That's a really good question. Can someone all right. Thank you, Curtis.

Soroush Khanlou
Curtis is on it. Is it a bone tongue or a regular tongue?

Chris Dzombak
So many.

Soroush Khanlou
The ghost has a tongue in the regular emoji, right?

Chris Dzombak
Yeah.

Soroush Khanlou
He's kind of we're waiting with bated breath. Yes, it has a tongue. Pink tongue.

Chris Dzombak
That's really weird. Will you send us a screenshot of that, please?

Soroush Khanlou
Will you send us an emoji? Okay, that'd be great.

Chris Dzombak
Thank you.

Soroush Khanlou
Nice. We'll put that in the show notes.

Chris Dzombak
Great content. We will do that. Yeah.

Soroush Khanlou
Nice. Cool. All right. Yeah. So we thought we would kick off WWDC, kind of like a little recap some thoughts and feelings.

Chris Dzombak
Yeah. By the way, this is by far, I think, the most preparation we've done for absolutely any episode. We talked about what we were going to do here for, like, almost ten minutes. That's the wrong note.

Soroush Khanlou
Yeah. How did I do that?

Chris Dzombak
I know.

Soroush Khanlou
Cool. Or something.

Chris Dzombak
Okay, we're back.

Soroush Khanlou
Full screen. Cool. Yeah. So probably biggest announcement WDC thing everybody's most excited for.

Chris Dzombak
Absolutely. A measure app.

Soroush Khanlou
Yeah, definitely a measure. App.

Chris Dzombak
Yeah. Or voice memos in icloud.

Soroush Khanlou
I actually lied down on the pavement yesterday and had someone measure up my body and see how tall I am.

Chris Dzombak
How tall are you?

Soroush Khanlou
Six one.

Chris Dzombak
Wait, you're tall?

Soroush Khanlou
I'm six one.

Chris Dzombak
Okay.

Soroush Khanlou
Yeah, actually worked out pretty good.

Chris Dzombak
Okay, good.

Soroush Khanlou
I might lie and say I'm 62, but I'm six one.

Chris Dzombak
Okay. Measure app. Good.

Soroush Khanlou
Measure up pretty good.

Chris Dzombak
Voice memos and icloud, those will be on your iPad. Seems good.

Soroush Khanlou
And your mac, I think.

Chris Dzombak
Really?

Soroush Khanlou
Yeah, I think that's one of the Mars Band apps.

Chris Dzombak
Oh, cool.

Soroush Khanlou
Yeah. There you go.

Chris Dzombak
Nice.

Soroush Khanlou
Do you listen to the platform State of the Union?

Chris Dzombak
I got like a third of the way into it.

Soroush Khanlou
How far did you get?

Chris Dzombak
I got through. They just wrapped up the marzipan discussion.

Soroush Khanlou
All right, cool. So you missed the most boring part of the platform, state of the Union. They just talked about Air Kit and Corml for like 30 minutes. It was so boring. I literally, literally left the room. I was like, I can't pay attention to any more of this.

Chris Dzombak
So this is something like I don't totally understand the emphasis on on device machine learning here.

Soroush Khanlou
On device machine learning to me seems like that is Apple doing. Like they're they're doing a thing that they want to do, which is we're not going to send your data to the cloud.

Chris Dzombak
Right.

Soroush Khanlou
And literally every other startup, every other company is going to not listen to that advice and just do it on the server.

Chris Dzombak
I'm really curious how many people outside of Apple are actually using Core ML?

Soroush Khanlou
See, this is the thing, because I think it makes sense if you have a really small app and you're in Indy or whatever, right? But if you're in Indie, you still have to train the model. You can either use a pre built model, like, oh, this is a bird, this is a plant, or whatever, but not that useful. There's like ten apps in the world that need that. And it's not going to be differentiating feature because everybody can do it for free, basically. So you can maybe make a model of Shakespeare text and spit out random Shakespeare text. That's kind of funny. But then why do you need to do that advice? And then who is this for? It's not for small indies. It's not for medium companies, it's not for big companies. What is this for?

Chris Dzombak
So it's totally possible that I'm missing something, but I mostly agree and I just keep coming back to like, there's no way that on device ML, on battery powered devices going to compete with Google's racks of servers that are specifically designed and optimized for this GP is.

Soroush Khanlou
And you could do that in Swift now.

Chris Dzombak
Yeah.

Soroush Khanlou
I'm really curious where it's very strange to me. I don't know anybody who cares about it.

Chris Dzombak
Yeah.

Soroush Khanlou
And then AR kit, similarly boring. Maybe useful for, like, I don't have.

Chris Dzombak
A big enough table.

Soroush Khanlou
I have apps. Yeah. I don't know, maybe if there's like some kind of I don't know, it's just like we've had a year of AR kit and I haven't played a single cool AR kit game. Yeah, I did the measuring thing once as a gag. That's it. What is this for?

Chris Dzombak
That's really all I have to say. Again, I really hope that I'm missing something here and that someone comes up with some really cool stuff that I just am not seeing or that I'm missing.

Soroush Khanlou
Yeah. I'm not sure what it's for. Yeah, it's very strange. And they spent so long in the Platform City unit, it was insanely boring.

Chris Dzombak
Yeah. I can't say. Yeah, I got 25 minutes into it. Something happened with playgrounds and Repls and I am out of the loop here.

Soroush Khanlou
Okay, the way that I'm pretty sure that this works is there's a button at the bottom of the playground where you can stop it and run it manually, or you can have it automatically run every time you change the code. Right, okay. So I think there's a new mode that's the REPL, and so it will only evaluate new lines of code at the bottom of the playground.

Chris Dzombak
Okay.

Soroush Khanlou
And so the stated purpose of this is, like, if you do do Corml, you train a model, it takes 18 minutes on the fastest Mac Pro or Imac Pro, and then you don't want to run that again, but you want to use that data. So you want to be able to write new lines of code without interpreting and executing lines of code above it.

Chris Dzombak
Okay, yeah, I can see that.

Soroush Khanlou
So that's like, one case where this is useful. Remember we talked about word ladders and graph search? So basically I had to download like, a big dictionary and then process this dictionary a little bit and then find passive words through the dictionary as, like, a graph. And that downloading of the downloading the file and processing and everything took like 10 seconds every time. And I would have loved to not have to do that each time I made a small change in the code.

Chris Dzombak
Yeah, that totally makes sense. Okay, so this lets you do playgrounds stuff but keep data around.

Soroush Khanlou
Right, but I think this is not important. If playgrounds aren't going to be stable, if you can actually work in playgrounds, then this is great. But they've been a disaster for me for the past, like, six months.

Chris Dzombak
Really?

Soroush Khanlou
Yeah. They have this super fun bug where if you leave it open for long enough, it will spin up like three processes that just, like, kick your fans on high and peg all your CPUs and they just have to work like that. It's horrible. You can kill them and they'll come back. And so it was just like really bad. They're just super broken.

Chris Dzombak
Yeah. As regular listeners know, I've not really been doing iOS development for the last year. I've barely opened Xcode in the last year. So I'm pretty out of the loop on playgrounds and most Xcode related things.

Soroush Khanlou
So I'm curious, do you do REPL stuff for Python to figure out? What's this? API.

Chris Dzombak
Yeah. To explore APIs. Does this actually work? Yeah.

Soroush Khanlou
Okay.

Chris Dzombak
For that I've been using there's an app called Code Runner, which I think you can get from the Mac app store. Yeah, that is nice for just doing Quick, playground, like stuff in basically any language.

Soroush Khanlou
Yeah. Code Runner is really good. And I meant to switch to it instead of Playgrounds and then I totally forgot until you mentioned it right now.

Chris Dzombak
You should switch instead of Playgrounds.

Soroush Khanlou
I really should. It's good. It runs really fast and doesn't crash or stop running your code or have to launch the simulator to run your code. It's good.

Chris Dzombak
Yeah, it's a useful tool.

Soroush Khanlou
Yeah. So Playgrounds, hopefully they're going to be more stable. Seems good to me. Let's do Mac. Let's do Mac.

Chris Dzombak
So you use QuickLook?

Soroush Khanlou
I use Quickbook all the time.

Chris Dzombak
I use QuickLook all the time. I don't want to do things in it. Like annotate yeah. I've never annotated anything because it's not a window. Like as soon as I accidentally touch anything, it disappears and I lose my place and my board.

Soroush Khanlou
Yeah, that's fair. I don't think I've ever tried to do work in a Quick look window because you click the desktop and then disappears and you're like, great, I was looking at that.

Chris Dzombak
Right. Or I hit an arrow key and then I'm looking at something completely different.

Soroush Khanlou
Yeah.

Chris Dzombak
Here's a giant image of a folder.

Soroush Khanlou
Super useful.

Chris Dzombak
Annotate this?

Soroush Khanlou
Yeah. So you're not going to use Quickbook? Annotations.

Chris Dzombak
Maybe I will. I don't know. I'm just like I'm not sold on doing anything that doesn't that takes more than like 2 seconds in Quick Look.

Soroush Khanlou
What do you think their definition of pro is? If a pro is someone who uses Quick look? Annotations I a pro is someone who uses a mouse.

Chris Dzombak
I don't know.

Soroush Khanlou
Yeah, it's very strange.

Chris Dzombak
I have nothing for you.

Soroush Khanlou
Pros. Use Dark mode and quickbook. Annotations check them out.

Chris Dzombak
I will definitely be trying Dark mode.

Soroush Khanlou
Yeah. I think that's going to be like a permanent. I want iOS more than anything.

Chris Dzombak
If apps support it widely enough, then I'll use it. But I can't deal with some things being dark, some things being light, and just huge changes in brightness as I'm like context switching.

Soroush Khanlou
The other thing is that websites, they have to reveal websites somehow because otherwise it'll be miserable. I go to Sephora, I'd be like.

Chris Dzombak
Yeah, I'm actually skeptical as to whether I'll want to use this interesting full time.

Soroush Khanlou
Yeah.

Chris Dzombak
But I also use like a light theme in my text editor. So I'm in the minority here.

Soroush Khanlou
There are a few other people in.

Chris Dzombak
Here that use like there are dozens of us.

Soroush Khanlou
Yeah, you are crazy.

Chris Dzombak
But there's dark mode, so for everyone else.

Soroush Khanlou
So does dark mode change the color of Xcode's code as well, or does anybody know and set dark mode?

Chris Dzombak
Exactly.

Soroush Khanlou
Weird. Yeah. So Joe says that if you switch to dark mode, that Xcode will switch, assuming you're using the default theme, but if you're not, then it won't switch for you. Which I guess is like, not worse than the status quo.

Chris Dzombak
That makes sense.

Soroush Khanlou
Dark mode, text, all that. Or light mode. Crazy people.

Chris Dzombak
Yeah, whatever.

Soroush Khanlou
So what else? What other mac stuff? We got Marzipan.

Chris Dzombak
There's marzipan apparently. Or we will have Marzipan in late 2019. This seems kind of early to announce that to me, but I don't know. Seems cool. If it's shipping in late 2019, it seems like they could announce it at WDC next year, but I guess there have been rumors about it too.

Soroush Khanlou
Maybe it leaked. And they're like, yeah, we got to.

Chris Dzombak
Just we have to acknowledge this.

Soroush Khanlou
Yeah, it's really weird because I don't think there's been I can't think of anything else that's like this, that's like, oh, we are going to do this thing. It's very half picked right now. Half the controls aren't even ported over. But here it is, like the very first OSN. Oh. The developer preview of OSN. Yeah. Or like, Siri was in beta for a while. That kind of count.

Chris Dzombak
Yeah.

Soroush Khanlou
I don't know. Siri. It's just really weird.

Chris Dzombak
Yeah. So what do we actually know about Marzipan? We know it exists. We know that it doesn't replace App Kit. They made sure to say that they are not deemphasizing App Kit. But this works, I guess, in tandem with App Kit.

Soroush Khanlou
I think the way it works is I've been, like, basically following Steve Stratton Smith on Twitter, so I have a lot of original research to share with you here. So it's like two render servers and they run in parallel. And then I think you can basically host a UI kit sub view in an App Kit super view, but you can't go back to UI kit and down deeper in the tree. So that's kind of how it works.

Chris Dzombak
Okay.

Soroush Khanlou
And then some of this stuff is ported over, so if you fire a UI alert controller, it shows up as an NS alert. Okay, but if you have, like, a date picker, it looks like an iOS date picker.

Chris Dzombak
I mean, this is something that we're just going to have to wait and see. And this is not by any means an original take. I'm really curious how this is actually going to work in practice. How well does an iOS date picker work on the Mac?

Soroush Khanlou
There's obviously, like, three more months of they can polish stuff up, but in.

Chris Dzombak
The there's longer than that. They have a whole year to polish this up before.

Soroush Khanlou
No, but HomeKit, the Home app is shipping, and that uses Marspan. Same with news.

Chris Dzombak
Right? They can just not use the things that aren't polished up yet.

Soroush Khanlou
Right, exactly. So I think that as it currently stands, there are UI pickers in the Home app that are still, like, iOS style, where you would, like, click and drag to move around. Or maybe you could scroll them, but they look like iOS UI picker views.

Chris Dzombak
Interesting.

Soroush Khanlou
Yeah, I think it is just, like, not finished. But are they going to ship a HomeKit app? By the way, I am excited about a HomeKit app because I want to use I don't have a modern iPad, and I don't have a modern Apple TV. I have too many smart lights that don't work, and I need them to work. Yeah, they're not very smart at all.

Chris Dzombak
I just have light switches in my apartment. They work all the time.

Soroush Khanlou
Fancy light switches. Really great fun fact. So, again, long time listeners show Know, my girlfriend, who came on Episode 50 to talk about this, is very upset with our smart lights.

Chris Dzombak
Don't blame her in the least.

Soroush Khanlou
I mean, you were there, and she texted me the other day, and I guess she was in bed, and she was, like, feeling very lazy. And she was like, hey, can you turn off the bathroom? I was like, I'm in California. She was like, yeah, I know, but I'm in bed. Most of the lights in the house are we most. And those work, like, over the Internet. But my Hue bridge is, like, fucked up and doesn't work over the Internet. And so I could do it through HomeKit, but I need the iPad or the Apple TV. And so I told her no. She was kind of upset. What's the one of these smart lights if you can't turn them off for me? So I'm hoping that if I can run HomeKit on the Mac, you'll be.

Chris Dzombak
Able to use your home's lights from California.

Soroush Khanlou
Well, I'll be able to solve my relationship problems.

Chris Dzombak
That checks out. Yeah.

Soroush Khanlou
So I have that Mac mini that sits on that runs that Python server that controls the lights.

Chris Dzombak
Yeah, just like normal.

Soroush Khanlou
That's right. It's called home assistant. It's great. And people come over and they look at our TV and they're like, what's that code in the corner? It's like a terminal window running, like Home Assistant. I'm like, don't worry about it. It's for the lights. And maybe if the Mac mini can be the HomeKit hub, then I can finally turn the lights off from California. Okay, so we got a little listener feedback. Yvonne says that that's not the case. You can't run.

Chris Dzombak
The Mac will not be a HomeKit.

Soroush Khanlou
So the Mac can't be a HomeKit Hub, which seems like a huge waste. Yeah, I don't know. I have one, and I would really like to use it as a HomeKit Hub.

Chris Dzombak
Good luck.

Soroush Khanlou
Yeah, HomeKit seems good news. I'll never use Mars Band. Seems fine. It was really weird to see the back button next to the Mac toolbar was really native, and that looked good. And you would expect to see the backforward in the top left, and instead you see an iOS style back button, and it was like, what is that doing there? This does not make any sense at all.

Chris Dzombak
This is going to be interesting.

Soroush Khanlou
Yeah. So they said four apps. It's like home stocks news. And another one.

Chris Dzombak
Yeah.

Soroush Khanlou
Voice Memos.

Chris Dzombak
Thank you, audience.

Soroush Khanlou
Yeah. They got our backs. And so we're going to see the rough edges of this, I guess.

Chris Dzombak
Yeah.

Soroush Khanlou
And I guess the other reason to announce it, to kind of jump back to our earlier point was, like, if somebody decompiles or I don't know what these people do to the apps, but if they do something that apps look at what's inside, they're going to see, like, oh, this is like a UI image view.

Chris Dzombak
That's true. Yeah. You would not be the secret for very long.

Soroush Khanlou
Secrets out.

Chris Dzombak
Yeah.

Soroush Khanlou
Be kind of fun. It'd be a kind of cool way to release the release it.

Chris Dzombak
Yeah.

Soroush Khanlou
I don't know. Be kind of nice.

Chris Dzombak
Yeah. Just have, like, a second. I don't know. Like a surprise event two weeks later.

Soroush Khanlou
As you may have noticed, as Guillermo Rambo has discovered. Yeah. Cool. So Marzipan seems fine, and I don't.

Chris Dzombak
Know how we can have anything else to say about it until we actually.

Soroush Khanlou
Get this whole keynote. Is basically, like seems fine.

Chris Dzombak
Yeah, that's kind of my impression so far.

Soroush Khanlou
Another big one. Shortcuts. We played with this on my iPhone Seven briefly.

Chris Dzombak
Yeah, we tried.

Soroush Khanlou
We tried. I couldn't find a way to add a new shortcut. I heard you need the Workflow app installed to be able to add a new shortcut. So this is workflow, right?

Chris Dzombak
Yeah, I think so. Really? Is workflow like DNA, right?

Soroush Khanlou
Yeah. So is the workflow bundle. ID now like part of apple. I guess, probably, yeah. All right, that seems good.

Chris Dzombak
There was a demo where during I think this was during the keynote, maybe during this I think it was during the keynote where the presenter had the Kayak the Kayak app and asked the phone to create a shortcut for her travel plans. Right. And I have so many questions about what happened here.

Soroush Khanlou
Happened to make that work.

Chris Dzombak
Right, right. And I haven't had a chance to dig into I don't know. Have you had a chance to actually read about how it's got to be.

Soroush Khanlou
An NS user activity? I would think, yeah, that's, like, the obvious place to hook it in.

Chris Dzombak
But then I thought there were multiple things on screen. And then later she asked for her travel plans and Kayak seemed to present the thing that was relevant at the time. So is that, like, the Kayak app noting that okay, it's like whatever time. So it seems like this hotel reservation is the most relevant thing. Is there some deeper OS level support or is this just like storing, remembering that travel plans means this user activity?

Soroush Khanlou
Right. Well, in workflow, you can also take data from a thing and turn into your own string. And so that could also be baked into the shortcut itself. So like a number of different levels on which it could work.

Chris Dzombak
Yeah.

Soroush Khanlou
So there's a class called an intent maker and then that can be parameterized and let you pass in whatever data.

Chris Dzombak
This is something for if your app is working with Siri, right? Like with the whole Siri, the new Siri, like, you've custom intents, which we'll throw a link to the show notes to this thread from Jake Marsh on Twitter. He has some screenshots of the Xcode UI for editing this. And you can totally parameterize like, what soup do you want? Quantity, other options.

Soroush Khanlou
So you publish the intent as the owner of the app rather than as the user of the workflow thing. Okay, I see.

Chris Dzombak
Right.

Soroush Khanlou
Interesting.

Chris Dzombak
I am curious how this works with NS user activity too. I again haven't had a didn't get a chance to date mechanism. What?

Soroush Khanlou
Maybe it's just a totally different mechanism.

Chris Dzombak
Maybe.

Soroush Khanlou
Yeah, it is cool.

Chris Dzombak
Okay. Audience says it is sweet. Why are we doing a podcast? Everyone here that's seems cool. Also, Marco will be happy. It seems like there's a play intent now, so maybe you'll be able to ask the system to play something.

Soroush Khanlou
It will be nice to be able to say, hey, start playing my podcast.

Chris Dzombak
Yeah, absolutely.

Soroush Khanlou
I wanted that.

Chris Dzombak
Start playing podcasts that we're no longer doing that's.

Soroush Khanlou
Right.

Chris Dzombak
Yeah.

Soroush Khanlou
So another big thing we dove into a little bit was iOS notification stuff.

Chris Dzombak
Yeah. This is also something that we tried to get working on your iPhone Seven.

Soroush Khanlou
And we got a little bit into it.

Chris Dzombak
Yeah.

Soroush Khanlou
So one of the things I wasn't clear on was I thought that when you go into that manage mode and you say, hey, make this make this quiet, I thought that was like a new thing you could do to notifications.

Chris Dzombak
Yeah, but it's totally not. All these options exist already. They're just buried like four screens down.

Soroush Khanlou
You can do all this stuff. It's just surfacing. It like a different UI.

Chris Dzombak
Yeah, which is totally which is great because who besides people like me, go in and actually customize those options for all the apps that send them notifications.

Soroush Khanlou
Right. I basically will turn them off and that's like the main thing. Or like, turn off the badges.

Chris Dzombak
I totally go in. Like, okay, this app gets sounds, but not badges and doesn't show on the lock screen. But this app knows.

Soroush Khanlou
So then the only thing that's actually new is the grouping.

Chris Dzombak
I think that that is true. Yeah.

Soroush Khanlou
Seems fine. I think the grouping, like playing with it on. The test phone, there was only like a couple of charges that got grouped and it was like that's, whatever, but I think on your real phone it'll matter more.

Chris Dzombak
Yeah. You were saying we were talking about this earlier before we recording that some of the API that this relies on exists already, but I forget exactly.

Soroush Khanlou
Thread IDs, which is different than this. This rolls up by app, but thread IDs are like a totally different thing.

Chris Dzombak
Okay.

Soroush Khanlou
So a thread ID will let you update one notification to have different content as new content comes in. And that's different from this. This just like updates based on the.

Chris Dzombak
App in your application. You can also have things group by thread rather than just by application. Okay, that makes sense. And that is actually new API, right?

Soroush Khanlou
Cool.

Chris Dzombak
Oh yeah. One of the things that I'm most excited about, I guess mostly as a user of iOS, is some improvements around password management and one time passcode management. And this looks super cool based on watching this was in the platform State of Union for whatever reason. So, first of all is that in app, when you have a password field, if you have a domain associated with the app, you'll automatically, I guess, get the same sort of strong password generation that Safari gives you now, which I think is great. And it's going to be stored in Icloud keychain and synced just like any other password.

Soroush Khanlou
Right. So the syncing is what happens through the current domain bundle ID stuff. And once you've associated domain, you can sync them. But you couldn't make the new passwords until this release.

Chris Dzombak
Not like within an app yet.

Soroush Khanlou
Right, exactly.

Chris Dzombak
Yeah. And then also, somehow I'm totally unclear on how you get to this UI, but there's some sort of user interface for checking for password reuse, which is cool. That's something that one password does, which I really like. There's a new extension point for password managers, so when the little password button pops up in your keyboard, that'll be able to hook right into one password, which is awesome. And then finally when you get a text that has a one time authentication code for two factor auth that will show up right in the keyboard. So you don't have to leave the app and copy or try to remember your six digit code.

Soroush Khanlou
Right.

Chris Dzombak
Which is good. Even though as a security mechanism, there's so many problems with using SMS at all. It turns out if you really want to, it's pretty easy to just hijack SMS for a phone number for a little while.

Soroush Khanlou
Really scary. I really don't want that to be the case.

Chris Dzombak
That's totally the case, I'm sorry.

Soroush Khanlou
Yeah, it's like you can hijack a SIM card, right?

Chris Dzombak
The other person, yeah, you can trick. The phone network is large and complicated, and if you can connect to it through some sketchy telecom provider somewhere, you can just say, I'm receiving SMS for a little while.

Soroush Khanlou
Yeah, it seems fine, right. Why? Could go wrong.

Chris Dzombak
Yeah, we'll throw a couple of links about that in the show notes too.

Soroush Khanlou
That I have bookmarked and so the say of the art of you doing two factor is like a Ubikey, right?

Chris Dzombak
Yeah, definitely Ubiquit for a few reasons. First of all, you can't intercept that. Second of all is it something like a Ubikey, like a hardware security key can't really be phished either because it knows that this code or this one time off key is good for this domain. And so you have your web browser talking with this piece of hardware. And so if you're on a phishing site and you even try to tell your Ubikey authenticate this, it won't do it because it knows a different domain.

Soroush Khanlou
Because it's a different domain. That's cool. Yeah. There was a social engineering thing that floated around on Twitter a couple of weeks ago where someone got texted like, hey, I used to have this phone number. You're about to get an unlock code. Can you send it to me? And then they would unlock the targets with the password, and then they would send the second factor over SMS, and then they would just take it and use it. Even if you're not Ubikey, you would know like, no, this is my UB key. You're not getting your codes on my Ubikey.

Chris Dzombak
And other problems with one time passcodes via SMS, even if you don't want to do a relatively intense SMS hijacking thing, you can just social engineer it really quickly.

Soroush Khanlou
Turns out everything's social engineering also attacked.

Chris Dzombak
Yeah. Also kind of related to Ubikeys, there's some code that got committed to Chromium recently from Google that will let you, at least sometime in the future, will let you use the touch ID on a MacBook as your like, whoa. Yeah.

Soroush Khanlou
How does that work?

Chris Dzombak
I mean, I don't know exactly how it works.

Soroush Khanlou
The show chris, come on.

Chris Dzombak
I looked at Twitter before I came to the show. Isn't that enough?

Soroush Khanlou
I mean, I didn't do much more.

Chris Dzombak
Than that either, but that'll be really cool because that's built into your like, this is going to authenticate that you're using this trusted device, which that's the whole idea. Right.

Soroush Khanlou
And so Google then is like, basically the two factor. Google app is basically replicating in Chrome, and then when you do that, some.

Chris Dzombak
Part of it's replicated using the hardware security features that you get from that. Right.

Soroush Khanlou
That's pretty tight.

Chris Dzombak
Yeah. Also, Chromebooks that you buy, the Google Pixel book, I think has a secret Ubikey basically built in, really, that there's just no API for. But Google use internally fun facts so.

Soroush Khanlou
That they can evaluate their own stuff, but third parties can't. That's super interesting.

Chris Dzombak
Well, just because they want to have this for their employees to use as their second factor, but it's just like undocumented. Yeah, fun facts.

Soroush Khanlou
That's pretty cool. Cool.

Chris Dzombak
So okay. That's automatic. Strong passwords and other security stuff.

Soroush Khanlou
Yeah, I'm really excited for not having Share buttons everywhere.

Chris Dzombak
Yeah, absolutely. That's another thing. So in Safari, we'll remove like, the Facebook or at least tracking via the Facebook share buttons and stuff.

Soroush Khanlou
Yeah, security stuff seems pretty good.

Chris Dzombak
Yeah. Also worth noting that macOS will require user consent for location photos, contents, contacts, access.

Soroush Khanlou
That's just catching up with iOS.

Chris Dzombak
Totally. Yeah. There will be new API around that for you to deal with.

Soroush Khanlou
I'm sure it's a good update.

Chris Dzombak
Yeah, I'm looking forward to it. I'm looking forward to running, like, the, what? Ten point, 1414 point, like two on my laptop.

Soroush Khanlou
So you're not going to update for a while?

Chris Dzombak
No.

Soroush Khanlou
Interesting.

Chris Dzombak
Okay. I need my laptop to work.

Soroush Khanlou
Yeah, that's right.

Chris Dzombak
At least as well as it does now. Unlike my lights, I can type all of the letters. I can type all the letters but G right now, and I don't need the software breaking things.

Soroush Khanlou
Did you get a can of compressed there?

Chris Dzombak
It's so far gone. It's fine.

Soroush Khanlou
So, general thoughts? WWC, how do you feel?

Chris Dzombak
I mean, it seems solid. It seems really incremental, assuming that there's actually as much of an emphasis on performance and on these nice improvements. Like, again, privacy enhancements, security enhancements, stuff like that. I think that's good usability enhancements to the notification settings that already exist. What else? A lot of these are things I.

Soroush Khanlou
Actually was kind of surprised by because, I don't know, I think as developers, we run on latest or near latest hardware, and it's easy to forget that there's people out there with iPhone Ses. There are people out there with iPhone Sixes, and if you talk to them, they're like, yeah, our devices are crazy slow and this is completely unbearable. And I just had no idea, and really didn't realize until Tim Cook came out, said, like, we worked on performance. I was like, what else did you do? But apparently the performance was a super, super big problem for a lot of people. And I feel like they did this with, like, snow leopard too. They've done this on the Mac a couple of times.

Chris Dzombak
Yeah.

Soroush Khanlou
So I didn't realize just on account of like, as a developer, you make the excuse of like, oh, I have to get the latest hardware. It's for my work. So you get it and then it works great. And it's so fast.

Chris Dzombak
Everything shiny and rainbows.

Soroush Khanlou
One of our projects, we started doing iPhone se first, just because squeezing everything onto an iPhone Se is hard, especially if you've done plus size or iPhone X size first.

Chris Dzombak
Yeah, I mean, this plays out in things that aren't, like, performance related. Just right.

Soroush Khanlou
Just like layout.

Chris Dzombak
Yeah, layout, screen size, design, all that.

Soroush Khanlou
Other WWDC thoughts? You enjoy being here for 36 hours?

Chris Dzombak
I'm enjoying being here for 36 hours. Had we planned this earlier, I would have planned to be here longer, but I'm going to be out of town for quite a while at the end of the month and I didn't want.

Soroush Khanlou
To take a little bit better or nothing.

Chris Dzombak
Yeah. It's been fun catching up with people, though.

Soroush Khanlou
Yeah, it's good to see everybody. Yeah. WWC seemed fine. It seemed much more consumer focused. Like, we looked at the API Dips for UI kit and it was like just Siri stuff. Basically makes it easier for us.

Chris Dzombak
Yeah, definitely.

Soroush Khanlou
There's safe area and sets. No new craziness.

Chris Dzombak
As someone who's not currently an iOS developer yeah. Seems easy enough for me.

Soroush Khanlou
So we've been doing this show for two years.

Chris Dzombak
Yeah. Which is a long time. I did like two years is a while.

Soroush Khanlou
You had a podcast before this?

Chris Dzombak
We had like, six episodes. But technically that is true.

Soroush Khanlou
Yeah. Six episodes. I mean, you know, and I don't know, I just remember when we started it, this podcast was like I don't know. It was an experiment. It was like, I don't know if anybody's going to want to listen to this.

Chris Dzombak
Yeah.

Soroush Khanlou
I don't know if anybody will care.

Chris Dzombak
I don't know why anyone.

Soroush Khanlou
But we started it and we did, what, ten episodes? We did like a neutral FM thing.

Chris Dzombak
Yeah. I think that was our first quote unquote season.

Soroush Khanlou
Yeah. And there was, like, good feedback and people liked it. So we did another experiment. We did the Patreon thing.

Chris Dzombak
Yeah. I guess we've been doing that for, what, since beginning of 2017.

Soroush Khanlou
That's right.

Chris Dzombak
And 2016, maybe.

Soroush Khanlou
No, we started the pocket.

Chris Dzombak
Wait. What is June? Yeah. 2017.

Soroush Khanlou
So early 2017. Yeah, we started that. And the Patreon never made, like, boatloads of Money. And that was fine.

Chris Dzombak
I don't think we expected it to make Boatloads of Money.

Soroush Khanlou
Yeah. It paid for our sound engineer, Joe. Shout out to Joe. Joe's been editing the podcast since episode 16. He gets to listen to the podcast for everybody else. It paid for new mics. It paid for the hosting of the thing. And honestly, I don't think we would have done it if we had to keep doing the editing or paying for the editing ourselves.

Chris Dzombak
Oh, yeah. Definitely not. I do not have time to edit this every week.

Soroush Khanlou
And yeah, I remember when you were doing the editing.

Chris Dzombak
Also, I'm not very good at Joe.

Soroush Khanlou
Is Joe way better than Chris? Yeah. And the podcast was just like an experiment that we did. And we kind of were like, well, when it feels like it's time to end it, we'll end it.

Chris Dzombak
Yeah. And I mean, that's partly why we did the breaking this up into Seasons with a little bit of a break in between is so that we have a chance every once in a while to kind of reflect, think, like, do we want to keep doing this? Was this working? Do we still have stuff to talk about?

Soroush Khanlou
That's right. And that recharge time was like, I don't think we would have gone for 70 episodes if we didn't build in.

Chris Dzombak
Oh, yeah. Having that, like, what, about a month of recharge time between seasons was crucial.

Soroush Khanlou
Yeah. And we kind of realized as we hit rounded out like 60 and 65, we're like this podcast.

Chris Dzombak
We were really starting to like, I don't know what we're going to talk about this week.

Soroush Khanlou
The thing I love about Seinfeld is like, this is a bit random. They were on fire. Season seven, I thought was like, great. Season eight was even better. Nine was great. And then they just stopped. They were just like, all right, we're done. We're dropping the mic, and we've done all we can. And if we keep doing this, it's going to be bad. And so we're not going to do it.

Chris Dzombak
And there's so many TV shows that don't do do that. And they're like, that's a great five seasons to stop watching after season six. It's terrible.

Soroush Khanlou
Season four. Fringe, anybody?

Chris Dzombak
No?

Soroush Khanlou
Apparently nobody watched Fringe. Season four was really bad. Season one through three, excellent. And so we didn't want to keep pushing it if it wasn't working. And we rounded out our stuff.

Chris Dzombak
We didn't want to keep pushing it to the point where it wasn't working.

Soroush Khanlou
Exactly. And we were getting there, getting towards the end, and we were like, you know what? I think it's time to end the show. And so WDC was coming up and we were like, one crazy thing would be if we did episode 70 at WWDC.

Chris Dzombak
What if we could do a live show?

Soroush Khanlou
What if we did a live show? What if our friends came, our listeners came, and everybody sat a big room and we talked about computers.

Chris Dzombak
Yeah.

Soroush Khanlou
And we did it. And we're very happy that we got a chance to do it. And we got happy we got a chance to talk in front of all you all. Yeah. It's been a special two years.

Chris Dzombak
It really has been. It's been a lot of fun. This has been.

Soroush Khanlou
Yeah, man, every Patreon episode, we're like, shout out to Patreons. And they're great. They're really like, I don't know. I've said this before, and I'll say it again, when you listen to NPR and they say this show is made possible by listeners like you, and the made possible is really literally true. We just could not do this if it weren't for people.

Chris Dzombak
Yeah. I mean, especially in this case.

Soroush Khanlou
We're willing to help us do a show without ads. Like, how many podcasts are there without ads? And we're so grateful that we didn't have to try to track down ads and try to track down companies that we weren't allowed to talk bad about because they gave us money.

Chris Dzombak
Because honestly, the just level of effort that that would take for us, that just wouldn't have happened.

Soroush Khanlou
Yeah. It was it was not going to be really feasible. So thank you to all the patreons. Thank you to everybody that came to this live show. We love you all.

Chris Dzombak
You have made this possible.

Soroush Khanlou
Yeah.

Chris Dzombak
Also, there's so many more of you than I expect.

Soroush Khanlou
We want to give a special shout out also to the Hotel Clariana, which we're all in. And also a second shout out to Jesse Char, who actually put this together. We were hunting for a venue, and she was able to find this for us and put it together. And I think it's actually a perfect size venue for us.

Chris Dzombak
Yeah, absolutely.

Soroush Khanlou
One more. Thank you, Joe Chaplinsky. Thank you so much.

Chris Dzombak
Yeah.

Soroush Khanlou
You've been editing for so many, like, what, a year and a half now?

Chris Dzombak
That sounds about right. Yeah.

Soroush Khanlou
And he puts up with my awful.

Chris Dzombak
Plosives and your inconsistent distance to the microphone.

Soroush Khanlou
Microphone distance. My terrible mic technique, and makes it sound smart every week. And we really appreciate it, Joe. You did so much for us.

Chris Dzombak
Yeah, thank you so much.

Soroush Khanlou
He brought these mics for us, too.

Chris Dzombak
Yeah, we tried a live show once before. It did not go well. Technically.

Soroush Khanlou
The people who were there, they remember how bad it was. We had a zoom, and then the lapel mics just didn't work, so we had to use the big microphone in the middle. And it was like, all this noise. It was really bad.

Chris Dzombak
Yeah. Imagine that. You record a podcast in, like, an echoey room with a microphone set on a table, like, 6ft away from the people who were speaking, and we had.

Soroush Khanlou
Lapel mics on the whole time. We're like, this is great.

Chris Dzombak
This is going to go so well.

Soroush Khanlou
And we're going to sound great.

Chris Dzombak
So bad this time. We tested these microphones earlier before we recorded.

Soroush Khanlou
Yes, I learned this word, sound check. You can probably come in and test.

Chris Dzombak
Stuff before you all thanks to Joe.

Soroush Khanlou
Yeah. Thank you, Joe. Thank you so much. I think that about wraps it up.

Chris Dzombak
Yeah, I think so. Like, we have in so many episodes. I'll just echo sirish. Like, thank you so much to all of you who quite literally have made this show possible and who have come out to listen and support this. This really means a lot to us.

Soroush Khanlou
Yeah, we love it. Yeah. So that was fatal error. I'm Sirous.

Chris Dzombak
I'm Chris and bye.

Soroush Khanlou
Later. So so there's a scene in Mission Impossible. Mission Possible. One is very different from the rest of them.

Chris Dzombak
I've never seen any of them. That's surprising. Nobody here.

Soroush Khanlou
So one is extremely good. It's a Brian De Palma movie. He did, like, Scarface. It's like a good ass movie, right? Two is insanely bad. It's like a John Wu like, kung fu action. It's very weird. And then three, four, five, and now six are all the same style of, like, Brad Bird, JJ. Abrams, like, running around huge stakes. Everything blowing up, jumping off buildings. Like running off the side of a.

Chris Dzombak
Building stereotypical action movie, right?

Soroush Khanlou
Very much so. But, like, in a very intense way that I think is I think they do a good job with them.

Chris Dzombak
Yeah.

Soroush Khanlou
But one is in a league of its own. It's very spy thrillery, so it's very cerebral, and it's less like punching and running.

Chris Dzombak
And when did Mission Possible one come out?

Soroush Khanlou
93.

Chris Dzombak
Okay.

Soroush Khanlou
Yeah.

Chris Dzombak
So there's a long running.

Soroush Khanlou
Yeah, very much so. Well, and then before that, it was a show in the 70s. It was a show I didn't know this. With the same premise. And so he hasn't seen he doesn't know any of it. John Void plays. He plays Jim Phelps. And Jim Phelps is like the leader of the IMF, the impossible mission force. And in his show, they do all these things, or that it's, like, steal goals from the Colombian cartel. They got to do all this great.

Chris Dzombak
Shit as you do.

Soroush Khanlou
Yeah, obviously. And then in the movie, try to spoil it for him. Jim Phelps turns out to be a mole, a traitor, and everybody who grew up with the show was, like, really mad about this. It's like making a James Bond movie where, like, James Bond works for the Soviets.

Chris Dzombak
Yeah.

Soroush Khanlou
Like, it's crazy, but you only find.

Chris Dzombak
Out, like, way, like, after there have been several James Bond movies.

Soroush Khanlou
Yeah, exactly. Exactly. And it's a really good movie. It's got a ton of good quotes in it. There's this part where Tom Cruise. It's like, Why, Jim? Why? And he says, Sometimes you just wake up and the country is different all around you, and the goddamn president stopped asking you for permission. It's really good. Yeah, that's right. It's such a cool movie, and it's, like, really well done. And honestly, the first five or six times I saw it, like, I noticed a new thing in it each time of, like, who's doing what behind the scenes to make the final plot happen.

Chris Dzombak
The first five or six times you see how many times have you seen it?

Soroush Khanlou
Easily a dozen.

Chris Dzombak
Okay.

Soroush Khanlou
It's really good. And the cinematography and the style they do it. You experience Tom Cruise's feelings of trying to figure out who the trader is because they know there's a mall. They don't know who it is. And you experience very viscerally, like, he doesn't know what's going on. He's trying to piece together who did this part, why did this car blow up, and who ran across this bridge, or whatever. And you figure it out with him, and you get to see what he's thinking. Cool. It's really well made.

Chris Dzombak
I watch this. Yeah.

