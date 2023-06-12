Speaker A
Hey, sir. How's it going?

Speaker B
Pretty good. Can't complain.

Speaker A
Good. Wanna start a show?

Speaker B
Let's do it.

Speaker A
Hi, everyone. Welcome to Fatal Error.

Speaker B
We haven't done that in a while.

Speaker A
No, it's been a long time. Yeah, we've we've been, you know, much less formal. Something that that you've mentioned on previous episode that I was interested in hearing more about was that you were trying to make some change to the standard library. And I think you've mentioned that that ended up not working out. But if you want to talk about it, I'd still like to hear about what you were trying to do and what didn't work out and what the experience was like and what you learned.

Speaker B
Yeah. It's kind of an in progress kind of thing.

Speaker A
Okay.

Speaker B
I'm not doing great on this project right now, so it's like, well, we're kind of at, like, a standstill. Essentially, what's going on is drop last is a function in the standard library for sequence. Right. And I will send you a link to where it's sort of implemented in the standard library so you can actually pull up the GitHub and look at it. Also, drop this in the show notes.

Speaker A
Okay.

Speaker B
And so essentially, the way that this works is you have a sequence, and let's say you're trying to drop five elements off the end of a sequence. What it does is it puts the first five elements of the array into what it calls a ring buffer. It's not important that it's a ring buffer, but I do want to go into that because it's an interesting optimization. But imagine it just puts it into an array, right? And then after those first five elements, it will kind of DQ one off of the front of this little buffer, this little array that it has, add it to a new array, and then grab a new element from the sequence and stick it onto the end of the buffer.

Speaker A
Okay.

Speaker B
And it'll keep doing that until it can't add any more items to the end of this buffer. And that means that the buffer is holding on to, let's say, those five elements that you want to drop. Exactly. And it returns to you the other array that it's slowly been appending to.

Speaker A
Interesting. Okay.

Speaker B
Yeah. And so we were kind of talking about intersperse, which is kind of like it's another function on sequence, where if you have, like, the numbers 1234 and you intersperse a zero in between them, you end up with 102-00-3040. There are no zero at the end. Sorry, I messed that up. But yeah, so basically, you might want to drop the last element off of that. But then I was trying to make a lazy intersperser, and you can't drop last and keep it lazy because drop last consumes all these elements. So you can't drop last off of infinity, for example.

Speaker A
Right.

Speaker B
So that was the problem that I set out to solve. I was like, oh, I think I can do better than this. I think I can make a lazy drop last that doesn't greedily consume every element in the sequence to create the new drop last sequence. That's kind of what I set out to do.

Speaker A
Okay.

Speaker B
Does that make sense? Have I explained the problem?

Speaker A
Well, I think so. That seems like something you could accomplish with a similar design here. Yes. Right. Just not continuing past the first five elements or the first six, I guess, elements of the sequence if you want to drop the last five. Right, exactly.

Speaker B
So I can share with you the implementation that I came up with. I will also drop this into the show notes.

Speaker A
Okay.

Speaker B
So what my implementation does is it keeps that same buffer, except it prefills it with, let's say, five elements. If you're trying to drop five off the end, and then it returns to you a lazy sequence that will give you an element from the front of the buffer and then fill the buffer again. And if it can't fill the buffer, then it will end the lazy sequence.

Speaker A
Okay.

Speaker B
Does that make sense?

Speaker A
That makes sense, yeah.

Speaker B
So I basically wrote up the solution. The code that's in the gist, you can just drop into a playground and test it out. It seems to work great. It seems to work in every situation that you would expect it to. Everything seemed fine. I put it into a slack that has some engineers who work at Apple, and one of them said, hey, this is really good. You should PR this. You should make a pull request into the Apple Swift repo and bring this to everybody. Because it's good, is what he said. All right, so I was like, this is great. I made something that's super useful and that people want to see, and this is awesome. So I was really excited, but I was like, I've never downloaded Swift. I've never tried to run the compiler. I don't know how to do any of that stuff. I've heard it takes hours. I got to set aside some time to do this right.

Speaker A
I'd have no idea where to start on this. And, I mean, I'd have to even look up is there a process for like, do you have to go through some process to pitch something for an addition to the standard library?

Speaker B
So because you're not changing semantics and you're not adding API or removing API or changing what API means, you don't have to propose anything. You can just open a pull request.

Speaker A
Okay. So you were going to figure out how to go through this process of adding something to the standard library and then pull requesting it.

Speaker B
Exactly. So I Googled a bunch of things, google who knows how to do this and can just give me a really short script that I can run that will just do everything for me. And I am very lucky. I have two computers. I have a desktop computer, and I have a laptop computer. So while I was doing my normal work on my desktop computer, I was able to run this sort of on the side on my laptop, which was really nice. So what I did was, through all my googling, I found one thing that was really useful, which is not going to be a surprise. It's Olive Begamin's blog. And he has this blog post called how to Read the Swiss Standard Library source. Because a lot of the stuff in Swiss Standard Library is the code is actually generated through GYB. Generate your boilerplate. You don't necessarily want to read that directly on GitHub. You want to generate it all and then read the generated code.

Speaker A
That makes sense. And this is something that in a lot of cases may change now that we have I'm blanking on the term, but conditional conformances. Right, conditional conformance. Although I assume that GYB will still play some part in the Standard Library for the foreseeable future.

Speaker B
Yeah, my understanding is they dropped a lot of the GYB code, but there's still a decent amount in there.

Speaker A
Okay.

Speaker B
As they add more features to the Standard Library, more GYB code will go away. But I think with the ultimate goal, that GYB will ultimately completely go away.

Speaker A
Which is probably why it's just sort of an internal tool. It's not really something that's public or is available standalone.

Speaker B
Right. So basically, he has some pretty easy instructions for how to install the tools you need, download the source, and compile the source of Swift. So essentially you need to brew, install CMake and Ninja and then clone the repo. And then there's a bash script in the repo that you can just run.

Speaker A
Cool. And so it looks like this post was last updated in October of 2016, but I assume that the build process hasn't changed very much in what, a year and a half?

Speaker B
Yeah, fortunately it totally works. I actually forgot to check the date, so I would have been really mad if the code didn't work. But the script totally worked and I was just able to just run it and just have it do its thing.

Speaker A
Great.

Speaker B
Yeah. So that part of it was pretty easy. It took not too long to clone the repo and set that stuff up. I think it took like under 30 minutes, I want to say took like 15 or 20 minutes, but this was now a couple of weeks ago, so.

Speaker A
I don't remember to do the setup part, not to actually build.

Speaker B
That just sets up the repo to be able to be built. That's the update checkout batch script. So that's only half of the process. Then once you have everything set up, you call the build script the build script script. That's confusing. The script is called Build script. You run it and then there's some options you can pass. One option that he suggests is X, which tells it to generate an Xcode project, and then R, which does a release build, which happens to be faster than a debug build.

Speaker A
Really?

Speaker B
Yeah. He commented on cool, on its surprising nature, but he says, yeah, this is surprisingly to me faster than doing a debug build. Still takes about 25 minutes on a quadcore. I seven from 2013, but it's better than the 70 minutes of a debug build. So I was like, all right, I'm doing it.

Speaker A
Really? Wow. I'm super curious where that time goes for a debug build. Like, I had been under the impression that with optimizations and everything, release build would take longer, but maybe there's, I guess there's processing. Right? I mean, according to this article, the debug build produces 24 gigs of results and the release build tape produces two gigs of results. So I guess it makes sense. Anything that deals with twelve times as much data is going to take more time. Yeah.

Speaker B
And it's only twice as long. So it's not that bad.

Speaker A
Yeah. Quote unquote only. Yeah.

Speaker B
So once that was done, then I need to figure out how to run the tests. And fortunately, tests are also simple. It's the same build script, but I think it's like t or dash dash test or something. I found that in another blog post. I ran that. So that's good. So now I've got the test running and it's like 2000 tests passed, 70 tests skipped. So far so good. So then what I did is I broke the current implementation of Drop last thinking like, okay, if I make this stop working, how does this affect how.

Speaker A
Does that affect the test? Which test should I failure look like?

Speaker B
Break, if I break this function, right?

Speaker A
Yeah. Okay.

Speaker B
So I did that and set it to run and then I went to go see Shape of Water with my girlfriend. Okay, well, I was like, I don't know how long it's going to take. And we got to the movies.

Speaker A
Sure.

Speaker B
Great movie. The lady falls in love with the fish. It's great spoiler. And so I guess do we need a horn? Do we need a spoiler horn?

Speaker A
I mean, I think once a movie has won what award show was yesterday?

Speaker B
Oscars.

Speaker A
Yeah, once a movie's won Oscar, I think then you're allowed to spoil it.

Speaker B
As we record this Oscars for last night. Yeah. Shape of Water, she does fall in love with the fish. I come back and I look at my computer and the tests are stuck at 18%. So they've just been running for two and a half hours and they're just stuck.

Speaker A
Wait, but you said that you would run the tests before this too, right? So clearly how long did that take?

Speaker B
I don't know, 20 minutes?

Speaker A
How exactly did you break this test?

Speaker B
What I did was if you look at the implementation, you see how it returns in any sequence of result, which is like the array that it's built up, I just returned in any sequence of an empty array.

Speaker A
Weird.

Speaker B
Okay, so what it did is, because the tests themselves are written in Swift, it broke something somewhere such that the tests couldn't actually complete, which is good in a sense. It means that I can effectively break these tests. Right. Like, you want to know that there are tests covering the thing that you might change it to my implementation and then no test failed. That could mean that my implementation works, but it also could mean there's just no test covering this function.

Speaker A
Right? Yeah. So now you know that at least something in the test is using this function exactly.

Speaker B
And will not complete if I don't return the correct result. So that's fun, right? Yeah. So I know that it's failing, so I'm like, all right, you know what? I'm just going to drop in my new implementation again, the gist that you can find in the show notes. And it should just work. Everything should just work perfectly, and I will be done and I can open a PR, and then Chris Latner will lift me up on his shoulders and there will be like a ticker tape parade and it'll be a whole big thing.

Speaker A
Ticker tape parade, okay.

Speaker B
Yes. So I drop in my implementation and I run the tests and four of them fail. But it's not four that are related to drop last. It's just four other tests.

Speaker A
One is like and at this point you've reverted your change to drop last.

Speaker B
No, I've added my test to drop last. Sorry.

Speaker A
You've reverted your intentional breakage of drop last and you've added your lazy drop last.

Speaker B
Added my implementation of drop last. Yeah, that's right.

Speaker A
Okay.

Speaker B
Yes. So there's something wrong with my implementation or there's Swift code. That depends on the fact that it's not going to be lazy somehow, and it's weird stuff that I understand. So there's like two of the files are like SIL underscore whatever. Underscore whatever, yeah. So SIL is the switch intermediate language that's a compiler internals that I don't know too much about, and that's basically where I'm stuck right now, is I need to dig in and figure out interesting. Exactly. Is break. Like, what would expect drop last to return a greedy array?

Speaker A
I'm really not sure, but I'm super interested to check this out. Do you have this fork published somewhere where I could pull this down and try to run these tests for myself?

Speaker B
So if you basically drop my implementation into a brand new clone of the Swift thing, you should get the same results.

Speaker A
Okay, but I'm not sure exactly how to do that offhand, but either way.

Speaker B
You'Re going to have to clone a repo and build Swift for sure. The only change I've made is I've pasted my function in here.

Speaker A
That's all I've done, just right alongside the drop last implementation or in place.

Speaker B
So I could publish a fork. Let me know if you need that. But yeah, you should just be able to paste my thing in and it should just work.

Speaker A
Okay, so is this something where is it acceptable from a standard library design standpoint to just replace drop last with a lazy implementation under the hood? Are there other places in the API where some sequence methods are just lazy without you opting into it?

Speaker B
The short answer is should be fine. The long answer is it's really complicated.

Speaker A
Okay.

Speaker B
It's weird because clearly there's some side effect that's happening here and something is depending on the old implementation of drop last. Right. Because these four tests are failing and they're failing reliably. Like, I ran it again, same four tests failed and then I reverted the change and ran again and then no test failed. So it's definitely reliable.

Speaker A
Weird.

Speaker B
Yeah.

Speaker A
Okay.

Speaker B
Part of it is because of any sequence, any sequence is a struct. It's a type eraser for sequence. And so theoretically, what it should do is grab ahold of the make iterator function off of any sequence, any particular sequence that you want, and hold on to it, and that function will have closed over. Like it's a closure over all of the instance variables that it needs from that type. And it's supposed to just hold on to that. But clearly there's something else going on there. It's very interesting. And then correct answer. If I wasn't scared of the Swift Standard library, and I had thought of this earlier is I should take my lazy thing, convert it to an array and then return that wrapped in an any sequence to see if I take my lazy implementation and then compute it all up front and then return that. Is it something in the actual implementation itself or is it an implementation detail of the fact that there's an array under the hood? So I need to check that.

Speaker A
I'm so puzzled by how this detail could leak out through here.

Speaker B
No idea. Yeah, I have no idea. And so it's like are the tests broken or is my implementation broken? And then of course, if this is an observable change, then that is actually a breaking change because somebody else could be relying on this behavior.

Speaker A
Right? Well, I mean, I think clearly someone else could be relying on this contain.

Speaker B
On this behavior, but it's likely that they're relying on it. Like, I've got to bring that up in the pull request and then it's got to be discussed.

Speaker A
Is it a bug that whatever implementation detail they're leaking out now is have you had a chance to discuss this with people who actually know the standard library?

Speaker B
I feel like I'm bothering them, which I know is kind of fake, but they've got shit to do.

Speaker A
Yeah, I totally get that.

Speaker B
The other side of it is because of a quirk of the way that both of our implementations are defined. Okay, this is like a really dark arts part of the Swiss standard library. Okay? So drop last returns a subsequence. Subsequence is an associated type of a sequence, right? Remember, sequence is a protocol, so protocols can have associated types. The only one that you have to define each time is your iterator type, the standard library. If you don't assign a custom subsequence, then the standard library will assign one for you and that subsequence will be any sequence. Are you with me?

Speaker A
Kind of.

Speaker B
So let's say you're implementing your own sequence. If you just provide an iterator, you're done, everything else will be handled right? But if you want to customize your subsequence, then and it's not in any sequence anymore, then you stop getting certain default implementations from the standard library and you have to provide them yourself. Okay, so those methods are drop last, I think prefix while and something else. Yeah, because if it's just a subsequence, the standard library doesn't know how to construct your subsequence. Right? Because let's say you're talking about an array. An array subsequence is an array slice. It doesn't know how to construct that. So you have to bring that implementation yourself.

Speaker A
So are you thinking that there may be custom sequences somewhere in somewhere no, in the tests that are breaking.

Speaker B
Okay, maybe what I'm trying to get at is the fact that this implementation relies on subsequence being in any sequence. My implementation can be changed such that it will return an any sequence for any sequence. That was very confusing. Any possible sequence type in the standard library. Like instead of returning a subsequence for this thing, it could return just an any sequence struct. And that's how mine works or that's how mine could work. So it could actually provide that default implementation for you. Remember, if you change your subsequent, you would lose that implementation. Mine works to fill in that gap, but because that's actually a breaking change, because now dropping the last N elements doesn't give you a subsequence anymore. It gives you a totally different type. It gives you always gives you an any sequence. So that's like a breaking change itself. So I didn't implement that breaking change. I was just trying to get the implementation working. But I wonder, could that possibly affect anything? It's very weird.

Speaker A
Yeah. Interesting. I'm going to have to digest this.

Speaker B
Yeah, so that's kind of where I am. I have a little bit more playing around to do until I figure it out. If anybody this is a Patreon episode, so it's about 150 of you, all our favorite listeners. If any of you have done anything like this, hit me up. I would love to hear your tips and stuff. It's real weird. Yeah.

Speaker A
Okay, cool.

Speaker B
The last thing I want to talk about is this ring buffer.

Speaker A
Oh, yeah, you mentioned that you wanted to talk about this.

Speaker B
Yeah, it's a pretty cool concept that I haven't really used in practice. I can conceive of it, but I haven't really used it in practice. So while I was working on this stuff, I did manage to ask some Swift team members some questions. This is before I started working on the repo itself, while I was still working with just the code and trying to make my own implementation. Swift's array is backed by a contiguous array, right? Which means that it starts somewhere in memory and then the end of it is completely reachable and unbroken from that starting. Right. Makes sense. With NS Mutable array back in the day, if you're working objective C, what it does is it actually lets you like, let's say it buffers ten spots and your array is maybe five elements, but you have a space, you have a capacity of ten spots before it needs to reallocate space. So far, so good. Yeah. What it'll actually do is it'll start your array maybe on maybe in offset five in that ten element capacity. So what can happen then is if you prepend something to the array, it'll put it in offset four, and if you drop something off the front, it'll drop off like offset five. So you can add and remove from both the beginning and the end without having to shift all the elements over. Right. Does that make sense?

Speaker A
Yeah.

Speaker B
And then if you hit the last element in the buffer in the capacity space, it'll roll back over to the zero th element. Does that make sense? Are you seeing it in your mind's eye? So that's really cool. Which means you never have to reallocate space for the elements of the array and then copy them over unless you completely run out of space. Otherwise, if you implemented it kind of naively and you put element zero in offset zero in the memory space, then if you dropped one element off, you would have to shift every element over to fill that space. So NS Mutable array rolls around itself like that array and Swift does not array. And Swift is a contiguous array where element in index zero starts at offset zero of memory and it goes straight through the end and it never has any breaks. It's contiguous.

Speaker A
It's much more of like a traditional array, like you think of it from C or from any other.

Speaker B
Exactly. And the benefit of it is apparently there's certain optimizations that you can add and then like the branch predictor can predict which memory address you're going to get next because it knows where it's gone. And there's other things you can add that are other optimizations that make contiguous array faster. I assume there's like vectorization, there's a bunch of other weird things I don't really know that much about, but the idea is just that if you have a contiguous array, it's faster. So Swift opted for a contiguous array. Now in both this implementation that's currently in the standard library for drop blast. And the one that I wrote rely on something called a ring buffer. A ring buffer acts more like the NS mutable array where it rolls around itself. So that way, like right now, if you have an array and you remove one element off the front, it has to shift everything all the way over because it has to stay contiguous and starting at zero.

Speaker A
Right.

Speaker B
But with this ring buffer, what ends up happening is you basically, let's say you're dropping five elements off the end. It'll fill those five elements. And then let's say you want to DQ off of that. It'll give you the zero th element of that ring buffer. And then the next element coming in, which would be the 6th element, fills in the space of that zero th element and there's a piece of state to keep track of. Okay, I just did that one. Now I'm going to look at index one, which is the second element or whatever.

Speaker A
Right.

Speaker B
And so that ring buffer is a really interesting concept because it means that it's this little optimization that they wrote in here. So that swift's, contiguous array doesn't mean you're continually shifting every element every time you run through the sequence.

Speaker A
Right, yeah.

Speaker B
Pretty cool.

Speaker A
Yeah. It's a useful little concept.

Speaker B
Yeah. And then there's a radar here and it says, and you can see this little comment in the code if you click on the Swift standard library, it says, create a reusable ring buffer. Generic over t. Put elements in this sequence. Put elements from the sequence in a holding tank, a ring buffer of size less than or equal to N. If elements keep coming in, pull them out of the holding tank into the result an array. This saves N times size of element in array because slices keep the entire memory of an array alive.

Speaker A
Right. I mean, I think that's explaining how the drop last function here works.

Speaker B
Right, right. I guess it's two separate comments here. One comment is create the reusable ring buffer, and then the other comment is like how it works.

Speaker A
Yeah. So I think what you're leading up to is there's a little to do item in this code to extract this concept into something that's reusable. Right?

Speaker B
Yeah, exactly. And that could also be like a really nice starter bug or whatever. If I were a little bit more capable in this percentile every, that might be something I would do is totally, yeah. Because you could define this type, expose it publicly or not, and then allow this function. And there's like two other functions that use a ring buffer that are linked with this radar and allow them all to kind of use this ring buffer abstraction so that you don't have to manually keep track of the indexes yourself.

Speaker A
Right. Because we all know that manually keeping track of indexes and stuff, once you get it right, that's fine. But it's more error prone. It's not the main thing that Drop Last should be responsible for.

Speaker B
And if it's a reasonable thing, it's a reasonable thing and we can maybe even make it public and all good.

Speaker A
Yeah. So I'm always kind of every time we hear about a starter bug or starter project in the context of the Swift compiler, Swift Standard library, I was just kind of like chuckle a little bit internally because maybe starter for someone who's interested in compiler, standard library and stuff, but I would have a lot of trouble coming in and starting to work on most anything that isn't marked as a starter bug or like, starter improvement.

Speaker B
Yeah.

Speaker A
You mentioned that you don't think you could dive in right now to this starter, like create reusable ring buffer?

Speaker B
Yeah, I could. I think this one because it's at the Swift level, if it was something at the sea level, I'd be like, I don't know.

Speaker A
Yeah.

Speaker B
So if I can get this thing to work and I can figure out why these tests are failing and I could submit this PR, then I think I'd feel confident enough to go in and say, all right, I'm going to try this ring buffer thing, for example. And then the one other thing I want to add is our friend Caleb, who is a host of Runtime, which was a show that's sadly now over, did this. He found a starter bug and he went in and edited C plus plus, compiled it, run it, added tests, all that stuff, and solved the bug and Pull requested it and I think it's in there now. I think so.

Speaker A
Cool.

Speaker B
So they did an episode about that. I'm going to try to track down that episode.

Speaker A
Yeah, that's right. I remember listening to that episode at the time. Yeah.

Speaker B
Pretty sweet. Pretty sweet. So it's tough. I'm going to to try try to get something done, but I don't know. It's the biggest code base I've ever worked on by far. Like it's huge.

Speaker A
Yeah. Well, it sounds like a fun challenge. I'm going to clone, try to get the Standard Library building here and maybe see if I can at least reproduce the problem you're running into.

Speaker B
I will say building the Standard Library was less hard than I expected.

Speaker A
Okay, well, that's good to know.

Speaker B
So I would say don't worry about that part, but it's kind of inscrutable, like what changes you make and what side effects they have. I would not have expected my change to have side effects. And here we are.

Speaker A
Yeah. And here we are.

Speaker B
Talking through this and kind of using user rubber duck. I have some new ideas for how to debug this thing.

Speaker A
Oh, cool.

Speaker B
I'll try those and see if they can give me any fresh data.

Speaker A
But yeah, hopefully we'll have a follow up episode where you figured out what's going on and and gotten things working.

Speaker B
Yeah, that's the dream.

Speaker A
That's the dream. Yeah.

Speaker B
Cool. I guess that about wraps it up for this episode.

Speaker A
Yeah, I think so. That it's. Been half an hour. Ready somehow. So we could talk about anything.

Speaker B
I guess we can story.

Speaker A
Yeah.

Speaker B
Cool.

Speaker A
Absolutely cool.

Speaker B
I will talk to you next week, Chris.

Speaker A
Yeah. Have a good night, sirish. Bye.

