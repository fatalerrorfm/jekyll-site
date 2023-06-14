Soroush Khanlou
Hello and welcome to Fatal Error episode 28. I'm, sirish. Khanlo.

Chris Dzombak
And I'm Chris De Zomback.

Soroush Khanlou
So today we wanted to talk about strings and strings in Swift. Specifically, there's a document in the Apple Swift repo called The String Manifesto more with a more detailed title of string Processing for Swift Four. And this is kind of it's not a proposal, but it's like a broad strokes outline of how they want to handle strings going into the future. So we both read it and we want to talk about it a little bit with each other. How does that sound, Chris?

Chris Dzombak
That sounds great. Yeah, I feel like, well, you can definitely talk for 30 minutes about the stuff that's in this document, that is.

Soroush Khanlou
The tagline of this show. We can definitely talk for 30 minutes about this.

Chris Dzombak
We should actually put that on the website.

Soroush Khanlou
Yeah, I think that'd be really good. So Chris, I know you care a lot about strings. I know you've given a short talk at your work about strings and how we should use different strings for different things. Can you talk a little bit about that?

Chris Dzombak
Sure. So right, I gave this short talk about a 20 minutes talk at work a little while ago, a little while probably at least a year ago at this point, with the thesis sort of that a string is a very general purpose type. It's general purpose in the same way that, say, integer is a general purpose type. We use it to represent all kinds of things from like email addresses to SQL statements to user facing localized text. Right. And the same way that you might use an integer to reflect everything from speed to acceleration to the width of an image. So in some way there should be sort of units attached to these. Right? And if we have an integer, we often know whether it represents the width of an image or velocity of something, and we often know that with strings too. But with both of these, actually, you can end up making some stupid programming mistakes that the type system could save you from. For example, you may write something accidentally that injects unescaped user input into a SQL statement, or you may accidentally output some debug description of some object out into the UI somehow. And my whole thesis was just that maybe we should have different string types to represent these different concepts. Maybe we should have different integer types to represent different concepts too. Right? Basically, we should have some notion of almost like units to these very general purpose data types in the same way that if you're doing like a physics or chemistry calculation by hand, you write units next to every number and watch the units, like, cancel each other out and be converted into other units.

Soroush Khanlou
Right? Yeah. What was the name of that?

Chris Dzombak
It was like dimensional analysis.

Soroush Khanlou
Dimensional analysis, that's what it was. That's good.

Chris Dzombak
Right? And so you imagine you're doing a calculation, you're say like, I don't know, some sort of chemistry equation, right? You are making sure that all your units check out through that whole calculation. If you're just doing something with like integers in programming or taking a string of input and putting it somewhere else, there's no verification. Like the type checker can't help you verify that you're doing things correctly because everything is just blobs of data. Right.

Soroush Khanlou
So for example, if you had a piece of user facing text, you might have a function attached to it to localize it for the current user. Whereas if you had a path, you might have a function attached to it to append some extra component onto the end of the path. Whereas if you had a SQL statement, you would have some method of binding variables to things and handling injection attacks. And so each of these things requires a slightly different domain. And so you would want different types to handle that stuff and you would never want to be able to mix them the way you can with strings. Right?

Chris Dzombak
Exactly. It makes no sense to say append a path component to a SQL statement, and yet if everything's just a string, you can totally do that and the compiler is like, all right, yeah, I.

Soroush Khanlou
Don'T know any better, let's do it.

Chris Dzombak
That's something that would obviously take support both with some niceties at the language level and in the frameworks that we're dealing with. Right, dealing with UI kit or like with Coco Touch retrofitting it to actually do that would be a huge project. But if you're creating a new framework for some programming domain, really think about this, please.

Soroush Khanlou
Yeah, for sure. So what you're talking about is more broadly known as primitive obsession, where people use strings and dictionaries and integers, where they could be using more rich types. I'm going to drop two links into the show notes that are interesting reads on that topic. One in Ruby and one in Swift. Both of those are really cool. And so this kind of brings us back to the string manifesto, because in the string manifesto, they talk about what they call the quote unquote default behavior of string. And I'll actually just read this, although this isn't well known, the most accessible form of many operations on Swift, strings are really only appropriate for text that is intended to be processed for and consumed by machines. So that means not user facing text, things that are more like SQL statements and more like paths that you can manipulate in different ways. And so they say all the things that they talk about are sort of more directed at machine processing rather than any of these other behaviors that we might use strings for. So I think that kind of sets the tone for the string manifesto. It's all about how to make strings work with strings between computers, right? Not strings between humans.

Chris Dzombak
Well, I think that's mostly what they're saying. This was something that really struck me while I was reading this document. What I read this as is them saying not that strings shouldn't support all the proper localization and other concerns that come with handling Unicode strings that are human readable and human accessible, but that those don't necessarily have to be the default behaviors. Right.

Soroush Khanlou
That's a better way.

Chris Dzombak
Right. And that lets them make a number of simplifying and performance enhancing assumptions in the sort of default case for the simplest parts of the string API. For really a lot of parts of the string API.

Soroush Khanlou
Right, right. So the idea is by default, we will just not worry about localization, not worry about language or any of that stuff, any of the user facing stuff, and only worry about machine processing. And then you can kind of add that stuff on.

Chris Dzombak
Right. So as one example, like the Unicode specification, and they mentioned this in the collation semantics section of the document here, the Unicode defines an algorithm for collating or for sorting, equality, hashing, these Unicode strings. Right. And this is a fairly computationally intensive and slightly memory intensive process, but it's not something that you want to do all the time. So we can take this assumption that we're making that strings are mainly for a machine, like for the machine, not for the human, and that this lets them make some simplifying assumptions and cut out a lot of these steps in the default case for a lot of string APIs.

Soroush Khanlou
Right. And so I actually didn't fully understand what is collation. They talk about the Unicode collation algorithm and it's not really clear to me what it is. And the description of how it works.

Chris Dzombak
Is also, I think collation is let's look it up exactly here, but my intuition is that that's basically, like, you take things that are out of order and put them in some sort of order.

Soroush Khanlou
Interesting, it says what Unicode says about collation, which is used in the less than operator, the equal to operator, and hashing. So it seems like it's like those three operations, you have to do these sort of normalization steps that they're calling collation before you can do these other operations less than equal to or hash. That's unray.

Chris Dzombak
Yeah. Well, this is the process for collation, which the dictionary here says is collect and combine texts, information or sets of figures in proper order. So this tells us how to take two random Unicode strings and put them in what Unicode considers proper order in a I'm blanking on the word. What's the word? That a standardized way, right, in a standardized, predictable, definitive way.

Soroush Khanlou
Deterministic, maybe.

Chris Dzombak
Deterministic, yeah, that's the word.

Soroush Khanlou
Yeah, I guess that makes sense. And you have to do this stuff right, otherwise you won't be able to compare the e with the acute sign up of it, with the string that has the e and the acute sign separate right. Where they are only brought together when it's being drawn.

Chris Dzombak
Yeah.

Soroush Khanlou
Okay, cool.

Chris Dzombak
So assuming that these still may be Unicode strings, but that they're not necessarily like, if you're just trying to sort to Unicode strings and you don't tell it that this needs to be like a localized sort, then a couple of these steps can be skipped and you'll get a consistent behavior, basically, which is good enough for the machine.

Soroush Khanlou
That makes sense.

Chris Dzombak
Yeah. So I thought that was interesting because this is one of the reasons that the string API is so relatively complex in Swift Three right. Is that they were concerned about performance with some of these things. So I think that with one of the things we're doing with this manifesto is coming around to understanding that there are simplifying assumptions we can make in a lot of cases because a lot of string processing is not something that's done for the users and something that's going to show up in the UI.

Soroush Khanlou
Right. It seemed like before they wanted to get the correctness nailed down before worrying about the ergonomics of the APIs, where the ergonomics are sort of how easy they are to use. And now that they kind of feel comfortable with the ergonomics or with the correctness, and they feel like they've maybe gone too far in that direction, they want to kind of dial it back and make it easy to use without losing that correctness.

Chris Dzombak
Yeah, I think that's right. Or they've realized that they haven't gone too far, but well, yeah, I guess in some cases they have and that we can tweak this balance to benefit more ergonomics and performance while maintaining correctness in all use cases. Right.

Soroush Khanlou
That checks out. So the biggest change to me seems to be that string characters is gone and string itself is now a collection of characters.

Chris Dzombak
That's absolutely a huge change.

Soroush Khanlou
So in Swift Two, string was a collection and then they changed it for Swift Three to make it not a collection, and now it's before they shouldn't get back to be a collection.

Chris Dzombak
So my understanding for that change in Swift Three was that they changed it to not be a collection because of performance concerns around treating a string like a collection of Unicode graphene clusters.

Soroush Khanlou
Right, right.

Chris Dzombak
But they don't really mention that here. And I got a little bit confused while I was reading this section. The only thing they mentioned, I think, about the cause, like about the rationale for that change in Swift Three was that during Swift 2.0 development, we realized that correct string concatenation could occasionally merge distinct graphene clusters at the start and end of combined strings. So what this means is that if you had two strings and you're treating them as collections of these Unicode graphene clusters and you concatenate them, it would be possible in some cases that you'd end up with some new unintended character in the middle where those two strings got concatenated, right?

Soroush Khanlou
So if you had like an emoji of a guy, an emoji of another guy, and then you merge them together with some kind of zero joiner or whatever you need, you could end up with one character of the two guys together.

Chris Dzombak
Right, except what they, I think, land on in the manifesto here is that that's actually probably not something that we need to worry about very much because that almost should never happen. Right. If you have a string that ends with a zero with joiner, that's kind of a weirdly broken string already, right, right.

Soroush Khanlou
Or a string that starts with like an acute sign that will get merged with an E to make an E acute. Like, why would a string start with an acute? Right.

Chris Dzombak
And they specifically call out that class of error. Or note that that class of error is called out in the Unicode Standard specifically, and that that's not got you. So so they've decided that that's not something they're going to worry about. And this seems to be the only rationale they put into here that was a reason for that change in Swift Three. And I was curious at why they didn't go into any of the sort of performance concerns that I had thought were the reason for that change.

Soroush Khanlou
Well, and that's an interesting thing too, because I feel like Swift string is a minefield of performance consideration. Because depending on how you write your algorithms that work with strings, they can end up being accidentally quadratic. Sam Giddens turned me out to this one shout out to Sam Gidden's, friend of the show. He was saying that because you don't know how long each character is going to be in terms of its physical size and memory. Some of them might be eight bits, some of them might be 16 and so on. You can't do a random Access collection. You can only do a regular collection. So you can't just jump to a place in the middle of the string. So if you try to write, let's say, a comparison between two strings for equality. If you try to compare like, okay, check the zero th character, then check the first characters, and then check the second characters. Each time checking that the characters are equal, you will end up with a situation where if you ask for the fifth character, it will have to go through the first, 2nd, 3rd, 4th characters just to get to the fifth one. And it'll have to do it again to get to the 6th one and so on. The better thing to do is zip the characters together and then compare that equality sort of member wise that way. And so I think since Swift string and string in general is kind of a minefield of performance anyway, maybe they just don't care.

Chris Dzombak
Well, so as you were saying that, I realized that they don't say that Swift that string will become a Random Access Collection anywhere.

Soroush Khanlou
Right. It becomes a bi directional collection, which I found weird. I thought it would probably be a regular collection before it would be a bi directional collection.

Chris Dzombak
I mean, you can still walk forward and back in, what, linear time, right?

Soroush Khanlou
Well, but you can't walk backwards because let's say you start with a character that's one byte, and then you want to go back one character. You don't know how many bytes that character is going to be before you.

Chris Dzombak
Is it possible for it to just keep walking backward until you I guess it's hard to tell where complete a character.

Soroush Khanlou
Yeah, you wouldn't know. But they do talk about string being bi directionally. Like iterable I guess, and I don't know why that is. That stuck out to me as kind of odd.

Chris Dzombak
Yeah, that definitely is odd. I'm realizing that my understanding here, I was assuming that they were making a Random Access Collection, which just doesn't make sense.

Soroush Khanlou
Right. They can't do that unless you made every character the same size in a given string, and then you have the problem of you're using 32 bytes or 32 bits when you only need or whatever.

Chris Dzombak
Okay, well, that makes a little more sense. So they're just folding that character's view back into string, basically.

Soroush Khanlou
Yeah, exactly. String is now the character view, pretty.

Chris Dzombak
Much, which makes sense. I remember back a few months ago, one of my friends was working on a Swift application. He's not an iOS developer. Really? Well, he is. He was writing an iOS app, but he has not been doing this very long. And he wanted to take the last character off the end of a string in Swift Three. And I had to go back and think, well, you're not going to like this answer.

Soroush Khanlou
Yeah, it's not pretty. It's not pretty. Although now, does that problem space get a little simpler in Swift Four?

Chris Dzombak
I don't have to explain why there's a character view now.

Soroush Khanlou
That's good. So basically the proposal in this is that for slicing up strings, that means taking a string and saying, I want these indexes in this range, that it would return a new type called substring. And string and substring would be related in the same way that array and array slice are related.

Chris Dzombak
And that relationship is, thanks for teeing.

Soroush Khanlou
It up for me. Basically that the substring in this case holds on to the original string and only maintains the start and end sort of pointers to what range that substring represents in the original string. The reason for this is then you don't need to unnecessarily copy a string just to work with its substring.

Chris Dzombak
Right. So the idea here is that you have a string, or let's say an array in memory, and you want to work with some substring or some part of this array. Then rather than remembering that we have this range, this start and end and this applies to this string. You just have a substring which references the original string and has that range sort of baked in, right?

Soroush Khanlou
Exactly.

Chris Dzombak
This is another nice example of just sort of removing room for programmer error, right?

Soroush Khanlou
Yeah, exactly. Although there is one gotcha with doing.

Chris Dzombak
It this way and that gotcha would.

Soroush Khanlou
Be thanks for seeing that again. So in this particular case, if you hold onto the substring, that substring will and hold on to the larger string. So if you have a situation where, let's say you have a very long original string and you take a small, small piece of it, let's say five characters from 100,000, your five characters, quote unquote substring is going to also hold a reference to your 100,000 character superstring. And so to basically get around this problem, you have to know that this exists and basically convert your substring into a full on string and then it will basically perform a copy at that time.

Chris Dzombak
So when you take a substring and convert it back to a string that copies that range from the original string exactly. And the original potentially much larger string can be freed from memory, right?

Soroush Khanlou
Exactly. There is a funny blog post or something where somebody was doing this issue, exact same issue was happening in JavaScript where the Chromium v eight implementation of substrings for Node, because Node is basically based on Chrome's, JavaScript engine was maintaining a reference to the original string. And so they were basically keeping these things around in memory long term. And like the server would crash because it would run out of memory because it was holding onto these huge strings.

Chris Dzombak
Right. So especially if you're parsing large JSON files or something, you should absolutely be aware of this. Now, I think that this is actually not going to be something that you have to worry about that often because pretty much all the APIs that you write are going to traffic in string. Right?

Soroush Khanlou
Yes.

Chris Dzombak
And so you're really only going to encounter substring when you're in the middle of some string processing algorithm. Right. The output is still going to be a proper string.

Soroush Khanlou
Almost definitely.

Chris Dzombak
This is my sort of intuitive understanding here anyway. So I'm thinking that similar to when you're dealing with array slices which have the same problem, and I think there's a warning in the documentation somewhere about this, but in practice you probably don't end up having to worry about this.

Soroush Khanlou
That often for memory leaks with substrings.

Chris Dzombak
Right, because you're almost never going to hold onto a substring long term.

Soroush Khanlou
Yes.

Chris Dzombak
You're going to hold onto a string.

Soroush Khanlou
I think it's basically more for it would be an inferred type rather than an explicitly declared type.

Chris Dzombak
Yeah, but as soon as you hit like a function boundary yeah, exactly.

Soroush Khanlou
You're going to have to write string explicitly.

Chris Dzombak
Well, you actually may not have to write string explicitly. This is a cool thing about this that I wanted to mention, you may not have to write well, so you'd have to explicitly return a string. Right. But this proposal, or this manifesto also proposes that substring should be a subtype of string. Just like int is a subtype of optional int. So you can pass an int into wait.

Soroush Khanlou
Yeah, you can pass an int where something expects an optional int and you can return an int where something expects an optional int.

Chris Dzombak
Right.

Soroush Khanlou
And so in the same way, I think they're saying they're going to special.

Chris Dzombak
Case this so that anything that expects a string, you can pass a substring and it'll be magically converted back into a string.

Soroush Khanlou
Yeah, I have a couple of thoughts on this one. This definitely stuck out to me too. If you want to find an undocumented, you could comment F for to ease the pain of type mismatches if the listener wants to follow along.

Chris Dzombak
Oh, no, I was just saying that would make a great, like, Twitter bio.

Soroush Khanlou
To ease the pain of type mismatches. That would be really good. One, I would love them for them to formalize this and put this in the language so that I can use it for my own stuff is one thing that I was thinking when I was reading this. And two, I was wondering, does this happen for array and array slice as well?

Chris Dzombak
That's a good question. I actually don't know whether it does, right?

Soroush Khanlou
Like if it doesn't, it should, especially if it's going to happen for string and substring.

Chris Dzombak
Although they do mention just before this, it's likely that this would be a significantly bigger problem than it is with array and array slice, since slicing a string is very common and I guess slicing an array is not as common. So maybe that's the justification. Right? They maybe want to avoid special casing, too many things.

Soroush Khanlou
Yeah, it's definitely possible. I just tested it does not work with well, actually, maybe I forgot the term generic type. Yeah, I don't think this works. Yeah. Cannot convert value of type array slice of string to type, to specify type array of string. So this doesn't work with arrays, but it might work with strings.

Chris Dzombak
Well, in Swift for it sounds like it will probably work with strings.

Soroush Khanlou
Right, I've got part of that.

Chris Dzombak
This is something that requires like special compiler support, right?

Soroush Khanlou
Yes.

Chris Dzombak
And this is something that I know you've had feelings about before. You want to cover that again?

Soroush Khanlou
Yeah, for sure. So I wrote this blog post called My Least Favorite Thing about Swift, which is all about essentially specialcasing these things in the language and then not letting users take advantage of them. Pretty much. And this would be another example of that. It's a weird case too, because I think a language like Scala has this and basically users will add their own subtypes so that things get automatically converted and you can kind of specify a conversion function that just happens naturally. And so you end up having with chains of these things and it gets very complicated and hard to parse. So I can imagine this getting abused really badly, but operator overloading and operator creation is also abused pretty badly and people do it and it's part of the language and it's fine. So I think I would just be down with it. I'll make sure to add a link to the show notes to the blog post. My least favorite thing about Swift yeah.

Chris Dzombak
That would be a cool addition if it could be exposed in language somehow.

Soroush Khanlou
Yeah. And then that way if you had your own types, you could take advantage of this yourself. I have to think about some examples, but there's definitely a bunch of stuff where you might want things to just be able to kind of naturally promote themselves to other types. And then the other benefit of it is the special casing gets to come out of the compiler and then all these cases of subtyping are sort of handled by writing code within the language itself.

Chris Dzombak
Yeah, absolutely. Continuing the theme that much of what we call Swift is actually the Swift Standard Library.

Soroush Khanlou
Yeah, exactly.

Chris Dzombak
So one other thing that I wanted to mention, this manifesto is that they've given some thought to handling something that I think we've talked about on this podcast before, which is the awkwardness of dealing with an objective C API that deals with a string and a range. We've talked about this before. Right?

Soroush Khanlou
I'm not sure if we have talked about this on the podcast maybe in person that's possible.

Chris Dzombak
So we have objective C APIs that take strings and ranges, right?

Soroush Khanlou
Well, they take NS ranges, right? Sure.

Chris Dzombak
Okay, so they take NS range and they take an NS string. The implication is that this range refers to some range of characters in that string. And it's really, really awkward to work with these APIs in Swift.

Soroush Khanlou
Right, because they aren't the same indexes that you would expect to get from the range of indexes of Swift strings is different than the NS range that belongs to NS string. They're different. And so to bridge them over is like a huge pain in the butt.

Chris Dzombak
Do you mean they're different types or the numbers themselves are different?

Soroush Khanlou
They literally represent different things. Yeah, because NS ranges are just two integers, and in Swift there are two string indexes, and string indexes are not exactly integers because of that width mismatch thing that I mentioned earlier. And so they're just not the same thing. And so to get to from one to the other, you have to literally call string index, like start index advanced by this many things to get to the same equivalent of NS range. It's just a totally different ball game. It's really awful.

Chris Dzombak
And so in this manifesto, they propose adding some interop magic so that those objective C APIs get represented or get bridged into Swift as accepting just a substring.

Soroush Khanlou
Right.

Chris Dzombak
That would be really because a substring, like we just talked about, is basically a beginning and end index along with a reference to the string that it refers to.

Soroush Khanlou
Right, right. Which is pretty much an NS string. NS range pair.

Chris Dzombak
Right.

Soroush Khanlou
Yeah. That's kind of elegant and nice. I really do like that.

Chris Dzombak
So as someone who's worked with, say, NS regular expression in Swift, and I'm pretty sure that it's correct, there's a lot of unit test coverage on that code.

Soroush Khanlou
Yeah.

Chris Dzombak
But I would very much welcome this change.

Soroush Khanlou
I think this is part of the whole, like, we got to fix strings, and one of the things we got to fix is regular expressions.

Chris Dzombak
Now, later in this, they do say addressing regular expressions is out of scope for this proposal, which is a shame. But I guess this is already an 18 page document and we can't expect them to cover everything.

Soroush Khanlou
There are quite a few more things covered in this that we should talk about. One is they talk about, like, basically there are these operations on strings, such as see if this regular expression matches, see if lowercase this thing, compare this thing to this other thing. And each of those comparison. And Swift is typically done with a less than or whatever operator. Right. But with strings, you sometimes need to pass additional parameters. So you might need to compare it in a specific language. You might need to compare it with a specific case sensitivity. There are different options that you would need to pass to do this. So you can't just use the regular operators. So they propose kind of a structure around functions like that so that you can compare something and then also provide those options that you'll need.

Chris Dzombak
Right. And it's important to note that while this is a start toward a pattern matching system for strings that resolves a few problems that are currently in the Swift language, this isn't really a detailed proposal about how that should be implemented.

Soroush Khanlou
Yeah.

Chris Dzombak
Although they do link to a pattern matching prototype written in Swift in the Swift repository, which I haven't really had a chance to review in any detail, but we'll throw a link to this in the show notes, too.

Soroush Khanlou
Protocol pattern. Whoa.

Chris Dzombak
Right. So I don't know exactly what this is, but it seems like it's maybe sort of a proof of concept as to how this could one day look in the Swift Standard Library.

Soroush Khanlou
Right. That's very interesting.

Chris Dzombak
That's something that may be interesting to take a look at if pattern matching strings is really something you're really interested in.

Soroush Khanlou
Yeah. And this also just goes back to, like, if you're trying to pattern match. Like, this is very much about machines processing machine strings, not about user facing.

Chris Dzombak
User facing 100%. One thing that I found interesting, just toward the end of the document were a couple of questions around. Description versus debug description. And so the two questions that I thought were interesting, should these be creating localized or non localized representations?

Soroush Khanlou
Right.

Chris Dzombak
And the other one is debug description pulling the weight of the API surface area that it adds.

Soroush Khanlou
Yeah.

Chris Dzombak
So is it worth having debug description and description?

Soroush Khanlou
My feeling on this is honestly that Ruby gets this right. You just call two S on anything and it just does something sensible. Maybe it's not exactly what you want, but you can further process it later. So my feeling is just like it should be called two string or whatever.

Chris Dzombak
Well, it should be called description so that it's parallel with objective C right?

Soroush Khanlou
Well or something. And then debug description, I think you can add extra data and it's like then it feels like I feel like right now description almost isn't pulling its weight and description almost acts as debug description, especially like when you code gen something or when you print the default of an object. It really looks more like a debug description than anything else. So maybe it's just that regular description isn't pulling its way correctly.

Chris Dzombak
Yeah, I think this is kind of my feeling too. Description is weird because it's not like an object is going to know how to create a user facing representation of itself.

Soroush Khanlou
Right, exactly.

Chris Dzombak
These are both programmer facing, even though description does get called if you try to interpolate this into a string. But that's not user facing, that's still basically programmer facing. Right.

Soroush Khanlou
There are cases. Yeah.

Chris Dzombak
And I guess I could see maybe if you're making some CLI tool or something.

Soroush Khanlou
Right, yeah. I feel like description was basically mostly for debugging anyway, and so that's kind of where my hot take comes from.

Chris Dzombak
Yeah. Should it be creating whatever ends up in the language? Should it be creating localized or non localized representations for that one?

Soroush Khanlou
I don't know because I don't know what that actually means. Like, does it mean if I have a specific string, it might be printed differently if I'm in a German locale versus in a swahili locale?

Chris Dzombak
Yeah.

Soroush Khanlou
That's weird.

Chris Dzombak
Yeah. Especially if it's a debugging tool. I feel like it should.

Soroush Khanlou
Right. That really answers that question for debugging. Just like always give me the same thing. If it's for actually printing, for putting it on screen, then it matters.

Chris Dzombak
Yeah.

Soroush Khanlou
So description is just not a good name for the two string function in my mind. Yeah.

Chris Dzombak
What else did you find interesting in this document?

Soroush Khanlou
The last thing that I found interesting was basically they want string and substring, these two types that we talked about earlier, to be able to share a bunch of code. And so the way that they want to do that is by making a Unicode type that is a protocol with a bunch of default implementations and stuff. And I feel like I don't really like that name, Unicode, but otherwise I think it's basically a good idea.

Chris Dzombak
Yeah, I think the Unicode name is weird. I'm trying to find this part of the document.

Soroush Khanlou
Can I call extract base?

Chris Dzombak
Maybe, although that's also a really bad name.

Soroush Khanlou
Yeah.

Chris Dzombak
I guess you have to share code between those types somehow.

Soroush Khanlou
Right. And the other weird thing about it is that it has an associated type which is its encoding and with that actually several associated types. I didn't notice these. And what that means is that you won't be able to refer to Unicode objects directly. They only exist as a method to share code. Otherwise you would need a type eraser. And they talk about like, are we going to build a type eraser? And the answer is no, we're not going to.

Chris Dzombak
I mean, I feel like that's probably fine since you're going to use this protocol via either substring or string. And those aren't necessarily interchangeable, right. They exist for a reason and you should know which one you're using.

Soroush Khanlou
Right? I feel like yeah, but sometimes I just want to say, this is text representable. And then I want to be able to say, as you said at the top of the show, I want to be able to make a path and then I want to be able to take that path and pass it to some system API that just expects some string. And maybe I want to bring my own path type, maybe I want to bring something else entirely. Maybe it's an S URL, but maybe it's like some other representable path in that case.

Chris Dzombak
Well, I mean, using a string is bad to represent all these different things, but a little bit earlier in the document there's a small heading guidance for API designers and it says if user is unsure about which type to use, string is always a reasonable default. So I mean, I don't know, it would be nice if you could use the Unicode protocol on its own, but I feel like that's probably not worth being upset about.

Soroush Khanlou
No, and it's not that I'm upset about it, it's just that it's a thing that I've always thought would be really nice to have even from back in the objective C days, which you kind of could do with class clusters. Right. You could say like if you were working with paths, you would get an NS path store two, which is a special NS string subclass that behaves more efficiently for paths. I kind of want that to be more formalized so that I can also bring my own and it would all be great. But here I feel like I was going to say that we could have this, but also we lost it in a sense. We had it for objective C and then we lost it. So I don't know. It's not to say that this is required, it's just to say I can imagine a lot of really useful cases where I would want to do this a lot. We work with strings so much. Yeah, a lot. Like, imagine if your JSON type could just be also a string, and when you pass it to the string API, that's when it got converted for you automatically. I guess there's issues there of, like, what if it doesn't convert? That would throw an error. What happens? The error, et cetera. But I don't know. We traffic in strings so much that I want to be able to have different types that all act as strings.

Chris Dzombak
Yeah, okay. I guess I could kind of see that.

Soroush Khanlou
And that's kind of why Ruby's two S method is so good, is because whatever you have, you just call two S on it and it basically works.

Chris Dzombak
I think I kind of see what you're saying. I feel like that implicit, implicit conversion between types that we talked about earlier would be maybe a more general approach to this, though.

Soroush Khanlou
Yeah, definitely. That's actually a great point. If we could have that, then this would really solve.

Chris Dzombak
And we don't need class clusters.

Soroush Khanlou
Yeah, I mean, class clusters were the solution they had at the time for this thing, but yeah. Cool. This is a really super interesting manifesto. I'm interested to see what parts of this get implemented. Strap yourselves in. It's going to be a wild ride.

Chris Dzombak
Me, too. I hope all of it gets implemented. And I also hope we get regular expressions natively in Swift. And I would also like a unicorn.

Soroush Khanlou
And I would like a pony. And I would like I'll feed it.

Chris Dzombak
And take care of it. So it's been fun talking with you, sirsh, as always.

Soroush Khanlou
As always. Great. And this is a Patreon episode, so I just want to shout out to the Patreon people, thank you so much for supporting the show. We hit our first goal on Patreon, which is super big. We may be maybe getting some new gear. We'll see how that all shakes out. Could be cool. But yes. Thank you so much.

Chris Dzombak
Yeah. Your support really means a lot to us and is letting us put together this podcast without dealing with ads and sponsors and all that stuff. You are the sponsors, so thank you.

Soroush Khanlou
Cool. Talk to you soon, Chris.

Chris Dzombak
Yeah, I'll see you later.

