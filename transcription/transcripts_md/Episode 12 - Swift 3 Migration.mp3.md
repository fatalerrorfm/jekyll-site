Speaker A
It. Welcome, listeners, to Fatal Error. I'm Krista Zomback.

Speaker B
And I'm Sirish Khanlou.

Speaker A
And today we're going to talk about migrating from Swift Two to Swift Three. Before we dig into the episode, I wanted to thank all of you who are supporting us on Patreon. This is our first private episode, our first Patreon only episode. And just want to say again that your support really does mean a lot to us. We've been very surprised by the level of support that we've gotten so far just in the past week or so.

Speaker B
One of the things I wanted to say for a while is that I really like the fact that it means we can continue to be ad free, but I don't know if this is the right venue to say it. So what I will say is the outpouring of support, we hadn't even posted a single private episode until this one. And we've gotten plenty of people already subscribing, plenty of people that subscribe to Patreon just to support us. And it really, really means a lot. And it means that we can keep doing this show and we can keep making the show awesome.

Speaker A
Yeah, absolutely. So that being said, let's talk about migrating from Swift Two to Swift Three. So this is something that we've been doing at work recently over the past couple of weeks. Sirusha, is this something that you've gone through before? Have you been writing? Swift three. Have you migrated an app from swift two to three?

Speaker B
So I was in a very interesting place. Before we dig in, I think we should say that the reason that this is a big deal, some of our listeners might not be writing Swift yet. The reason that this is a big deal is that Swift 2.2 was the last version that was supported on the last Xcode. Swift 2.3 is supported on this version of Xcode, which is a couple of minor, minor changes. And then Swift Three is like a ton of changes that you have to make to make sure that your app continues to compile. So when you upgrade Xcode, you do have to do the small shift over to 2.3, but you didn't have to do the 2.3 to 3.0 jump. And they said that Xcode 8.2 is going to be the last Xcode that supports Swift 2.3. And so that kind of lit a fire under everybody and made everybody we have to do the Swift Three migration kind of now because the next version of Xcode that comes out our app just won't compile it anymore. So the clock is kind of ticking on that stuff. Everybody I know has either done it or is like, I got to find some time to squeeze this in. I was in a weird situation because I was switching clients at the exact time that the switch happened. So I left one client and then the next client was a brand new app. So we just started in Swift Three, which was really painless. We did have about a week of Swift 2.2 code that we had to migrate, but it was like maybe 1000 lines of code, and it was really quite a quick switch. I did do code review for a couple of teams that did the switch. I've helped those teams solve bugs that were caused by the 2.3 to 3.0 switch. But I haven't done the entire migration myself, except for a very tiny one, the thousand line one. Yeah.

Speaker A
Okay. I'd be curious to hear what some of the bugs that you were helping discover were, because that seems like something that we could probably learn from.

Speaker B
Yeah, it's a lot of really edge Casey stuff. One of the things that changes is things like dates and data, things like that. They all move to be value types instead of reference types. Right. So there's like, little subtle bugs that could be caused because of that. The one we were dealing with, one of them was because the description of NS data changed when it became data, and it used to print out like a hex representation of itself. And a lot of apps rely on that to send that hex representation to the server. So when you got a token for push notifications, you would just use data description and then send that to the server. It was kind of a lazy way of getting out of the fact that you don't want to manually have to calculate this thing. The description had it for you, so why not?

Speaker A
I remember years ago at this point, maybe two, three, four years ago, reviewing some code that handled push notifications, and someone had written that code that took the data description just in order to get the hex value. And I remember calling out, this seems like this isn't necessarily great, and this probably isn't the way to do this. And now here, for like, years down the road, it turns out that I was right. I think that we still ended up taking the shortcut back then, but that's good. I will check our push notification code to be sure it does things correctly.

Speaker B
For sure. When I wrote that code, I wrote a test specifically that checks that that parsing works correctly. And that test broke. And that's how we knew that it was broken.

Speaker A
Oh, nice.

Speaker B
And I was kind of aware. I was like, you know what? This is the kind of thing that could change. We're relying on almost implicit behavior here, so let's just throw a test in here, and that way if it changes, it'll be immediately obvious. And it did change, and it was obvious, and that's how we knew to fix it. But yeah, that's the kind of bug that could happen. And it could just secretly be in your code base. And you wouldn't know because you don't touch push notification code very often.

Speaker A
Right? Yeah, absolutely. Once it's working, just that's right.

Speaker B
Don't touch it.

Speaker A
Right. So that's one of the sort of I don't know if I'd even call that a semantics breaking change, but it is a breaking change in language. What Swift Three is sort of notorious for are a lot of syntax breaking changes and a lot of changes in how objective C APIs get imported into Swift.

Speaker B
The rough rule that I've been seeing is about half of the lines of Swift in your code base will change. They don't change very much necessarily, but they will change all the enums. Now, the first letter is lowercase all of the collection APIs, like where you might have had object at, index it's, now object and then inputhencies at it's. Like little tiny changes like that all happen, but you'll end up with a big difference. I'm curious. So you guys just did yours, right?

Speaker A
So we've been working for the last week and a half or so on migrating our in progress application from Swift 2.3 to Swift Three. I think when you include tests and everything else, we're migrating around 25,000 lines of code, which is a lot. It's not the biggest Swift app out there by far, but it's a good amount of code to migrate. So maybe first we'll go over the strategy that we've taken for this. Last week was the week between Christmas and New Year's, so only a few of us were in the office. And so we started working out which of our dependencies needed to be, like, still needed to be migrated to Swift Three. A number of internal dependencies that we had were written in Swift 2.3, and there was one external dependency which we ended up forking and migrating to Swift Three.

Speaker B
Classic.

Speaker A
Yeah. In Swift so far, there's no Abi application, binary interface compatibility. So all of your frameworks that get linked into the application have to be built with the same Swift tool chain, which is something that the Swift team is aiming to solve somewhere down the road after they have hit source stability. My understanding is that, like syntax, source code stability is the priority. But someday you'll be able to take a Swift library and link it into your app without having to know that they were built with exactly the same Swift tool chain.

Speaker B
Right. But that day is not today.

Speaker A
That day is not today. So we spent a good amount of time last week on that, on migrating dependencies. Now, dependencies are something that obviously you can parallelize that conversion, that migration between team members. You have each team member take a dependency. Right?

Speaker B
Right. New branch doesn't affect the old stuff. Make sure all the tests are passing.

Speaker A
Right. So starting at the end of last week, beginning of this week, one of our developers really took on the bulk of the work in running the Swift Migrator on our application itself and at least getting it to compile and getting most of the tests to pass. And that was something that took him a couple, maybe two solid days of work. I would say just getting it to a state where it's something that we could again split up areas of the app to have other people work on review and clean up.

Speaker B
Right.

Speaker A
So that's how we've gone about this so far. I guess we could talk about. Well, if you have any questions so far, we can go over that.

Speaker B
No, no questions so far.

Speaker A
Okay, then maybe I'll just go over some of the other stuff that we've noticed, which are other things that either the compiler noticed but we had to fix manually or things that we noticed while reading diffs that you'll. Want to look for when migrating from Swift 2.3 to Swift Three and some other stuff that is kind of in the same vein as your Data Description bug.

Speaker B
That sounds like a good plan. I also have a couple of small things that we ran into, although it's such a big thing that I think some of the things you ran into, we won't run into and vice versa.

Speaker A
Sure.

Speaker B
But I'm still interested to hear what those things are that you all ran into.

Speaker A
Yeah, and I'll note that we're not quite done with this, so it's possible that I will take your list of things that you ran into and check our code base for them tomorrow.

Speaker B
Yeah, I can give a couple of the things that we ran into. So I mentioned the data description. One, that was a weird one. Another one is in Swift Three, optionals are no longer comparable by default, which is a really good change, but because the way it worked before is nil was always less than everything, no matter what the type was, which doesn't really make any sense, so they removed that. But if you do rely on that behavior, the migrator will actually add an extra optional comparison operator for you in that file and make it like file private. And then you can either dedup it and make there just be one optional comparison operator and slowly remove them all over time, or you can leave them file private and remove them one at a time. But it was definitely a little annoying thing that was just like, oh, we do rely on this behavior, and this behavior is now gone. So what do we do? Did you guys have any we had.

Speaker A
A few places where we were comparing, I think optional dates in particular. We noticed that those comparisons were added to our code base in a few places at the file private access level. And we haven't really worried about that too much yet since the behavior that we were working on is the behavior that we're expecting, at least. Right?

Speaker B
Yeah.

Speaker A
And we assume that the code that was added is pretty much copied out of the previous standard library.

Speaker B
Right. It should continue to work just fine.

Speaker A
Right. We're not too worried about that. Did you opt to deduplicate those out and have that in your application?

Speaker B
Yeah.

Speaker A
Or are you leaving those? Okay.

Speaker B
Yeah, that's an app and a team I no longer work on. They're an old client and so I don't know what they're doing now, but I would like to think that eventually they kind of work their way out of each of those optional comparison operators and then we're eventually able to delete that.

Speaker A
Okay. I think we're going to err on the side of not deduplicating those, leaving the private definition in the file everywhere that it's used just because that sort of removes the temptation to add more usage of it going forward.

Speaker B
Right. In retrospect, that might be the right answer.

Speaker A
I think it probably is, yeah. All right, let's see. I've been keeping notes from the migration, so just going down the list here.

Speaker B
Nice. Yeah, hit me.

Speaker A
So some of the methods that used to return optionals will now return empty strings. In some cases, last path component is no longer optional. That'll return an empty string if the path is an empty string or I guess if it can't be split into path components. The same thing applies to absolute string path and the path components property that would give you an array of path components. Those are no longer optional. So those would return, I assume, either an empty string or in the case of path components, an empty array.

Speaker B
Right. Do you think that's a good change?

Speaker A
I'm not sure.

Speaker B
Yeah, that's one that we're going to have to sit on and think about.

Speaker A
I haven't actually thought about that very much. I do think that path components returning a non optional array makes sense, which I think is something you'll agree with.

Speaker B
Well, yeah, and there's always been this question, I've written about it on my blog a couple of times in Swift of things that have multiple ways of being empty. So an optional string can either be nil or it can be an empty array. And they both mean emptiness, and sometimes they mean emptiness in different ways. And so that's important. But in the case of path components, like an empty array and a nil array for that, is there a semantic difference there? Do each of those mean something different? I kind of don't think so. So I think that that change is definitely good. It's definitely easier to work with when it doesn't return an optional.

Speaker A
Well, it's easier to work with, but you can still run into the behavior that you were getting with optionals before where you're getting back in nonsensical value. Right. You just have to know if that's possible and check for it and handle it.

Speaker B
You kind of have to know that the sentinel now, instead of being nil, is an empty array. And if it's an empty array, that means something semantically.

Speaker A
Right. And I mean, this is nicer because you might have cases where a URL came from some hard coded path or like an NS file manager path that you know is going to be built up of path components. And so now you don't have to deal with unwrapping an optional that you know will never be the none case.

Speaker B
Yeah, that's right. As a slight tangent, I do think that one of the ways that this could be solved is if the different types of URL were separated into different actual types.

Speaker A
Oh, yeah.

Speaker B
So there's no reason that a mail to URL should be represented with the same type as like a URL that takes you to a web page and that shouldn't be the same type as a URL that represents a local file. And the fact that they're all kind of overloaded into this one type called URL means that, well, in some cases, since this could be a mail to URL, we have to handle this thing specially and now this thing has to return optional where it didn't before and stuff like that.

Speaker A
Right. So I actually have taken a step toward resolving this in our application. There are a lot of cases in our app where we deal with file URLs specifically, right, and we pass these between various internal APIs inside the app. And I was writing a lot of code to work with this and noticing that it was really clumsy to get a URL that I knew was a file URL and deal with Inswift 2.3 unwrapping this optional that I knew would never be optional or that I knew would never be Nil. And it was really annoying. And so I used have you seen the library called Validated from Ben G? I forget what his last name is.

Speaker B
I think that's Benjamin Inks.

Speaker A
Yes, that is correct.

Speaker B
I have seen Validated, but yes.

Speaker A
So it's a really cool library that uses Swift's support for generics to attach basically Validators to a type. And so in this case, I defined a validator for a URL called is File URL. And so now rather than writing APIs that take a plain old NS URL, I take in URLs that are wrapped in this sort of validated file URL type. And I also added some syntactic sugar for the methods that I was using that no longer returned optional since I knew that they would never return Nil given that the URL they were operating on was a file URL.

Speaker B
Right. That's super interesting. I'd never considered using this library like that.

Speaker A
I really like that in our app. It really cleaned up a lot of redundant code and a lot of code that were code paths that we knew were never going to get hit and that we're just like if this is Nil, then Fatal error. Because this is like an application support directory path and it will never the last path component will never be Nil.

Speaker B
It was basically just to satisfy the type checker that you added the stuff right. And you were able to remove that. That's really nice. You should tell Ben about that because that would be a really nice thing for the README as well.

Speaker A
I think I probably should. And it's not very much code and it's not anything that's specific to my company. I'll see. If it's something that we could throw up in a gist for the show notes.

Speaker B
Yeah, even a gist would be great. Yeah. The other thing I was going to bring up is, have you seen Kyle Fuller's Path kit?

Speaker A
That sounds vaguely familiar. I don't know that I've actually reviewed it though.

Speaker B
It's a little library that gives you a type called Path, which just represents the path and that's like a local file URL and it has extra abilities attached to it. So you could do like Path exists instead of having to use NS file or a regular file manager, which depending on your style, you could take that or leave that. But the idea is basically just instead of using URLs to represent this stuff, you can use paths to represent this stuff. It's a type that really knows what it is and it's very focused. So it's kind of a similar solution to what you came up with, although slightly less like composed than your solution.

Speaker A
Okay, cool. That makes a lot of sense.

Speaker B
We could throw that in the show notes.

Speaker A
Yeah, all this stuff that we've talked about will be in the show notes, of course, which you can find at Fatal Error FM. No, that's a lie.

Speaker B
Yeah. Oh, no, you can't because this is patreon. It'll also be in your podcast listener app, so that's a good place to find it. But if you do want the show notes, you have to go to the patreon. So it's Patreon.com fatalairror and then find posts for episode twelve.

Speaker A
Right. I'll have to get in the habit of thinking more in this Patreon plus Fatal Error site of mind. Anyway, let's move on from this. I will definitely take a look at Pathkit, but we have a lot more stuff to go over for Swift Three for sure.

Speaker B
On the other hand, we could talk about URLs for another 45 minutes. It works for me.

Speaker A
Be a really interesting podcast.

Speaker B
So what else did you guys find?

Speaker A
It was not URL related, so I've had a couple really simple things to check for. The migrator tends to change all of your private definitions to file Private, which in some cases may be right, and in some cases maybe locking things down even further and changing that back to Private will make sense. The file private access level is new in Swift Three and it means basically what Private did in Swift Two and earlier. That is that something that's Private can be accessed anywhere in the file where it's declared. Now that's the new file private declaration, and they've added a new private access control below file private. And that means that that type is only accessible within the scope where it's declared, and we'll add a link explaining that to the show notes because it's a little bit hairy to talk through here.

Speaker B
Yeah, I think that change was really a mistake and I think they've been talking about rolling it back, so that may actually happen.

Speaker A
I haven't worked with this quite enough to have a strong opinion on that yet. We'll see.

Speaker B
Yeah, that's definitely one we're going to have to see as Swift Three shakes out. It's like, is this actually useful or do we just really need one type? One.

Speaker A
So, in a similar vein, the migrator will also elevate a number of your public types up to being open, or I guess public classes to being open. Open means that it's a class that something outside of your module can subclass and can possibly override things. And this is something where previously that would just be any non final public class in your module would be a class that users of your module can subclass and extend. And now you have to specifically declare that that class can be extended with the open keyword. So the migrator will apply that to cases where something's just declared as public. But again, if something was declared public and not public final, just as an oversight, you may not want it to become open. So searching your code base for open after the migration is probably going to be a good thing.

Speaker B
Right. So anything that is public and not final becomes open.

Speaker A
I'm not totally sure if that's true because I didn't see very many opens that got added to our code base.

Speaker B
That's odd. I wonder what the rule is then.

Speaker A
It could be that and just that most of our things were properly declared as public and final.

Speaker B
Right.

Speaker A
I'm not totally sure about what the underlying rule is.

Speaker B
Yeah, interesting. Yeah. That's another one to keep looking out for. I mean, I feel like all of the different access levels are just really extreme now and it was nicer when it was simpler.

Speaker A
I can kind of see the argument for open, at least more than I can see the argument for file private. Although although I understand that I would just recommend after you run the migration, just search for your code base for the keywords open and file private, because these are new in Swift Three, and so if you see one there, you know the migrator added it. So just look and see if it makes sense in that context.

Speaker B
Right, right.

Speaker A
That doesn't have to be a project. That takes a long time. Another thing we noticed is that with notifications, not only has the NS prefix been removed from the notification type, and I think that notification is another of the things that got value semantics. Is that right?

Speaker B
I think that's right, yeah.

Speaker A
Okay. Notification names are no longer plain old strings, but there's a type notification name which is just a type alias for a string.

Speaker B
I don't think that it is a type alias for a string. I think it's actually a brand new type because you have to use raw value to instantiate it.

Speaker A
That is true. What is it? I swear I dug into it, and it was a type alias for a string.

Speaker B
That's super odd. Yeah.

Speaker A
Let me check that out while you check that out. I'll keep reviewing. So anywhere that you're using notification, the migrator will add a, like, initializing a notification name from a raw value at the point where you use it, and that is really not correct. Really what you should do is look for those diffs, look for those conversions in your diff and undo them and instead go back to wherever that notification name is declared and change those to be the notification name type. And then that symbol can continue to be used just normally, as you would expect in Notification APIs, without initializing a notification name from a raw value everywhere in your code base.

Speaker B
Yeah. And if you just put the dot in front of it, it'll auto fill all of the potential things it could be, and you'll get autocomplete. You'll get everything.

Speaker A
Yeah.

Speaker B
So the situation with notification name is very weird because in objective C, it is a type alias for a string. But something happened in Swift Three where there are things that are kind of enum esque, but they're actually strings under the hood.

Speaker A
Oh, that's right. We're talking about the Nsxtensible string enum thing that you can attach in. Right?

Speaker B
Right. Yeah. And so that becomes notification name, and then since that's now when you import it into Swift, it becomes its own type. It's actually a struct. It's not a string that it's broad representable with, like, a string backing type. And so that's the thing that you're extending and that you're adding the extra static values to.

Speaker A
Okay, that makes sense.

Speaker B
Yeah. The weird thing about the notification changes is Notification Center lost its NS prefix, which is fine. That makes sense because it seems like anything that lost its NS prefix is, like, necessary for working with things on Linux. Right. But then NS notification didn't lose its NS prefix, and it's still a class.

Speaker A
Well, Swift NS notification is still around, but there's also a notification type in Swift.

Speaker B
Let's see if I can find that. Is it for use with NS Notification Center?

Speaker A
Yeah, it is. It's the same. So, like, with Data, NS data still exists as a reference type, but data is like value type that's bridged over to NS data. It's the same situation with notification and NS notification.

Speaker B
Okay. Yeah. My bad. I was just looking in the wrong place. There is a struct called Notification with no NS. Yeah, NS notification. I don't know. It's weird. So you can just use Notification Center with regular notifications.

Speaker A
You're going to have to be more specific. Do you mean you can use Notification Center no NS prefix with regular notifications.

Speaker B
No NS prefix?

Speaker A
Yeah.

Speaker B
Oh, I guess we just screwed that up. But you can still use it with the NS prefix, which is not true for NS Notification Center, you have to drop the NS.

Speaker A
Maybe. I think I changed autocomplete everything I encountered to plain old notification. No NS prefix and Notification Center no NS prefix and all the tests around that are passing. So I think it's right, but I don't know if you want to intermix the two, how it works.

Speaker B
Right. So it is right. It's just that the other way, if you wanted to add NS prefixes to everything, you can't do because there is no NS notification center anymore. It's only Notification Center.

Speaker A
Got you.

Speaker B
But NS notification does exist. This is really confusing.

Speaker A
Such a clear language.

Speaker B
Yeah. I don't know. I guess it's the same as the NS data thing and the NS string string thing, but it's very confusing to me.

Speaker A
Right. I think the takeaway here is use Notification Center with no NS because the NS notification center no longer exists in Swift Three.

Speaker B
Right.

Speaker A
Use the old notification type if you want value semantics, which you pretty much always do, I think, especially with notifications.

Speaker B
Now are notifications, NS notifications mutable. I was wondering this while we were talking about it as well.

Speaker A
I don't know if I've ever mutated and I don't think so.

Speaker B
You shouldn't be able to mutate it. Let me look at the original source. I don't think you ever read only object read only NS dictionary. Copy the name. Read only? Yeah, it's read only because I don't.

Speaker A
Think you ever create a notification. You tell a notification center how to create one, right?

Speaker B
Yeah, I think that's no, there is an initializer. You can in it with name, object, user info, but once you init it, you can't change it. So it basically does have value semantics in the fact that it's immutable.

Speaker A
Okay.

Speaker B
So, yeah, basically the rule is drop NS anywhere you can unless you're doing.

Speaker A
Something really weird, like using a switch.

Speaker B
Don't do things that are really weird.

Speaker A
Attach something to an notification. Then you still need to reference semantics double yikes.

Speaker B
Yeah. You will.

Speaker A
I did that once. It was a whole thing.

Speaker B
I'm sure you had a good reason.

Speaker A
It was an objective C two. Yeah.

Speaker B
Okay, so NS certification is super weird.

Speaker A
It is super weird, but maybe not as weird as we initially thought. Apologies to you, our listener, for having to deal with that.

Speaker B
That was a crazy roundabout.

Speaker A
The worn, unused result annotation, which you could apply to a function or method that returns something that really shouldn't be ignored. That's gone now, because that's the default in Swift Three. What you have to do is annotate a function or method that returns something that can be ignored. Does that make sense?

Speaker B
Right. Yeah. So instead of warning when the. Result is unused. You warn when it's intended to be unused, so you flip it.

Speaker A
You mean instead of annotating.

Speaker B
Right, right.

Speaker A
Yeah. Right. So it's just exactly flipped around. The thinking being that by default, something that returns a value probably doesn't mean for you to throw that value away, and sometimes it does, but that's probably the special case, not the former.

Speaker B
That's one of those changes that I thought I might be annoyed by. But it seems to be fine in practice.

Speaker A
Super on board with it.

Speaker B
Yeah. It's called discardable result in Swift Three now.

Speaker A
Right. So one thing that I've caught there is that if you have SwiftLink set up to warn you about having more than one line of vertical white space, worn unused result will go away. The migrator will take the worn unused result annotation away, but leave the line that it was on. So you can end up with an extra empty line there between your documentation and your methods declaration.

Speaker B
Oh, that's super weird.

Speaker A
Yeah, it's a little bit weird. And SwiftLint might warn you about that. Or if there was no documentation attached to that method, you'll end up with multiple lines of white space and SwiftLint will give you a nice little warning there. And that's something that's obviously not critical, but it's something to be aware of.

Speaker B
Right.

Speaker A
We found that if you have code that uses the word extension or default or other keywords, particularly if they're enumeration cases, those get converted to a lowercase. Right. And so the migrator will go through and try to convert your default enumeration case to lowercase everywhere. And then, because that's a keyword, it'll add back ticks around it wherever it adds that. And in a lot of cases, that's not necessary. It doesn't hurt anything, but it can be a little bit just a little bit weird to read or disconcerting to come across. And so in many cases, those back ticks that the migrator adds can be removed.

Speaker B
Interesting. I wish I knew when you needed the back ticks and when you don't.

Speaker A
If you get a compiler error because something's reserved, then you need the back ticks.

Speaker B
Right. I wish there was a way to know before I wrote the code. Yeah.

Speaker A
I don't know. Offhand, that seems like something that could actually change between compiler versions. Right. Depending on how it's parsing.

Speaker B
Right.

Speaker A
Maybe the back ticks should well, whatever.

Speaker B
I think it's probably safe to take the back ticks away.

Speaker A
It's probably safe to take them away, but it's also completely not necessary. It's a nitpicky styling thing.

Speaker B
Right, right. And it does look kind of weird when there's backticks in there.

Speaker A
Yeah, it does. I think that's really the bulk of what we've noticed. There is a potential pitfall when dealing with method names that changed in Objective C protocols that have optional methods.

Speaker B
Oh, yeah. This one's brutal.

Speaker A
And we're going to put a link to a blog post about this in the Show Notes rather than having me try to try to go into detail here. The gist is that if you've implemented a method that's an optional method from an Objective C protocol, then its name could change and the compiler wouldn't freak out because that method is optional. Right?

Speaker B
Right.

Speaker A
And so if the Migrator changed the name in a way that doesn't match up with the protocol's definition anymore, or if the way that protocol's definition changes because Swift Three changes how things get imported from objective C into swift, but it misses changing that method as declared in your code base. Then it'll be like your object no longer conforms to that protocol, or it contains that method from that protocol.

Speaker B
And you won't be warned and you.

Speaker A
Won'T be warned about it.

Speaker B
Right.

Speaker A
And so that's something to really look out for. And as I said, this is a difficult thing to explain verbally, and we'll put a blog post about it in the Show Notes.

Speaker B
Yeah, it's definitely super insidious because there's no way to know that it's failing except to actually just test your whole app. Especially like I think table view protocols are especially prone to this.

Speaker A
Right.

Speaker B
So stay woke, people.

Speaker A
And speaking of testing your whole app, this sort of thing is a case where having unit tests covering a good portion of your app really comes in handy. We have something like 68 or 69% code coverage in our application target right now.

Speaker B
That is crazy. That's so many percent.

Speaker A
It's a lot of percent. And I am so thankful because otherwise I do not know how I would have confidence in the results of this migration. I mean, I guess I would review things carefully and hope and pray, but having good test coverage has given me so much more confidence in performing this migration.

Speaker B
For sure. We had maybe like 15 tests, maybe 20 tests, like not a lot of tests at all. And like four of them caught something and it's like, imagine what I wish I had more tests. Yeah, I mean, it's crazy. So write to test people. Do you have any custom collections in your code base?

Speaker A
Offhand, I do not think that we did.

Speaker B
You'll know, because you have to add an extra method. Because let's say you have something like API Error collection and it's just like something that you want to act as a collection or an array, basically, but it maybe has an array and you want to act as an array so you can map over it or get things from indexes or whatever. In Swift Three, you now have to implement another method called index after on the collection itself. So we had a little bit of trouble with that and making sure that all of our conformances were still good there. That was one little thing we ran into. And we ran into one other little thing that I can't quite explain, but basically NS coding acted really goofy. Somebody else fixed this bug, so I don't know the details. Shout out to Brian. Michelle. I remember the fix, but I don't remember why the fix was happening. The comment says, decode a double from a key to archive regardless of what Swift version was running, and there's a what stack overflow thread. It's very weird. It's like if you have a double, you first have to check, like, decode objects for key, and then you have to check decode double for key. So if you have NS coding in your app, that's a really good place where you can just throw some tests down because it's super easy to just convert something to data and then back again and just verify that all the properties are equal. And that's how we caught these and we knew that something was wrong. It took us a while to figure out what exactly was wrong, but I would check your NS codings as well. If you have any of those, please.

Speaker A
Throw that stack overflow article into the show notes.

Speaker B
That is a great idea.

Speaker A
That definitely sounds like something that we do have fairly good test coverage around, but certainly bears checking manually.

Speaker B
Let me pop that in the show notes.

Speaker A
Cool. And I don't think that I really have anything else to add here.

Speaker B
So I do have one question for you. Kind of a broader, higher level thing is what do you think of this migration in general? Do you think Apple did the right thing with all the stuff that they changed? Do you think they could have written better migrations? Do you think that it should have been spread over time or it was good that it was smashed up into one big migration? What's your general feeling about the fact that our entire industry just went through, like, a giant upheaval in this migration?

Speaker A
That's a big question. I'll try to take that in part. I'll take the last part of the question first. I think in the grand scheme of things, this is kind of painful, but it's not really that huge of a it's not that huge of a change for the industry. Let's take a step back and realize that what's happened is we have some new value types where previously we had reference types, and we have some new naming conventions that we think we like better in the long term.

Speaker B
Right, right.

Speaker A
So it's definitely a painful conversion. I don't know that it's necessarily a really big deal in the long term. Right.

Speaker B
I mean, it's hard to say what the added cost of it is of just like my fear is not all apps have moved over to Swift, which is true. I think it's only like 11% of top apps or something like that. But it's a big chunk of people and it's a big chunk of time, and it's very disruptive. Like, you had people working over their Christmas breaks. It wasn't nothing. It wasn't just.

Speaker A
To be clear, for my company, we didn't have people working over their Christmas breaks, people who decided not to take time off in that week.

Speaker B
Got you. Yeah, right. I wasn't impugn anybody. And I know people who did do that. They said, I'll take two extra vacation days, I'll work over Christmas, the company will give me two extra vacation days elsewhere just so I can do this migration when nobody else is working. So that our merges are not totally crazy.

Speaker A
Right. Yeah. That is one thing. You pretty much have to freeze all future development while this conversion is going on. Let's see other parts of the question. I do think that if you take as given that all of these changes in naming conventions, et cetera, were going to happen, I think that putting them together in one big go is probably a good thing. Although I'll temper that by saying that I maybe would have liked to see the purely naming changes separated out from changes that are like semantic changes. Right. Value versus reference semantics.

Speaker B
Because it's easy for those collections changed several things changed. Like a deeper level. Yeah, in a deeper way.

Speaker A
Right. It would have been nice to not have those things that changed in a deeper way and in a more semantic, behavioral way.

Speaker B
Right.

Speaker A
It would be nice if those hadn't gotten lost in the more mundane parameter naming or first parameter naming changes. Right?

Speaker B
Yeah, for sure. And there's like a bunch of changes around any which are really subtle and I couldn't even explain. But any is basically the thing you use instead of any object. Now in a lot of cases it's very weird. There's a bunch of stuff like that that's not purely naming. It actually really changes how the language works at a fundamental level.

Speaker A
Right. And I guess I could see an argument for separating the naming stuff out from those more meaningful changes.

Speaker B
Right.

Speaker A
That obviously, as I said, is taken as given that these changes would happen at all. And I do feel like Swift is going in a positive direction here, so I'm happy to accept that as a given for that argument.

Speaker B
Right, yeah.

Speaker A
And what was the first part of your question? Oh, could Apple have done a better job providing migration tooling? So with a caveat that I was not the person who sort of ran the Migrator on the largest part of our code base and spent a couple of days getting it all to build and getting tests to pass. So that the rest of us could sort of come in and clean up and look for other problems and really go over most of the app with a fine tooth comb.

Speaker B
Right.

Speaker A
I know that he mentioned that the migrator would catch new things and migrate new things the second and third times that you ran it on the same code base and that really seems pretty unfortunate. So the migrator also would try to change your enumeration cases to be a lowercase first letter instead of uppercase, which was the convention earlier. But in a number of cases where those cases were used, it missed changing the first letter to lowercase. And so that was something that we had to go in and do manually in a number of cases. And so I do think that the tooling for performing this migration could be better. Obviously it's difficult to you can't really write a tool that will convert things from reference semantics to value semantics everywhere with 100% correctness. But effectively performing a search and replace across a code base for an enumeration case should be fairly straightforward.

Speaker B
Yeah, that shouldn't break.

Speaker A
I mean, I get that it's complicated, it's not as simple as doing a search and replace, but even so, that's the sort of thing that should be performed completely automatically. I had heard that the migrator is pretty much running like is performing string processing on source files and isn't working from the AST to sort of augment.

Speaker B
Its knowledge of the I would believe that. I would definitely believe that.

Speaker A
Which seems right based on what I've seen. I do wonder if there would be room it's probably not worth it from Apple's perspective, but I do wonder if there would be room to provide a sort of like Parser augmented migrator. So you could at least parser and the first couple of steps of compiling, just because it seems like having some more semantic knowledge about the code that you're migrating would be really useful.

Speaker B
Yeah, there were definitely some cases where we had something that I saw what the migrator was trying to do in its replacement of text, but it came out super garbled. Yeah, I mean, I don't want to cut Apple too much slack here. They're a giant company, they should be able to do this well. But on some level, I feel like Switch was a victim of its own success where they kind of put this thing in the world and they were like, okay, well, we made this thing. We're really still figuring it out. Use it please, but also use it at your own risk. We are going to change it. And then it became this wildly successful thing that everybody felt like they had to be using. And because of that, there's so much serious heavy production code that's written in it that there's no nice way to get from that 2.2 state to the 2.3 to the 3.0 state that they wanted to be in without just going through. As they say, the only way out is through. There's nothing else you can do. And if it had been less successful and it was maybe just a bunch of side projects, it could have been a little bit easier. But yeah, I don't know, they had a tough problem and it's really frustrating because migration code, like, have you ever written migration code for a database or something that you write to on disk. It's like the most boring kind of code because you know it's going to run once and never be run again. And you're like, well, I wish I could just delete.

Speaker A
But it better run, right?

Speaker B
Yeah, but it better run, right. People will be mad if it ruins their data. Thank god for Source Control. Thank God for statically typed languages. Those ones made this a lot easier.

Speaker A
I forget who someone posted in Slack. God save the compiler while we're doing this. Yeah. And automated testing, I think, were really useful in this process.

Speaker B
For sure. It was an interesting thing. I'm glad I'm kind of done with it. I don't envy people who still have to do it. I'm glad you all are done with it, but I think it kind of had to happen and there's just no other way.

Speaker A
Yes.

Speaker B
As unfortunate as that is.

Speaker A
And in the grand scheme of things, it's not that unfortunate.

Speaker B
Yeah. I mean, I just think about all the get bisects that we can no longer do.

Speaker A
Yeah, that is true. That is really unfortunate.

Speaker B
And just old code that if you want to pull up an old project somebody wrote or just a sample code or something, it's just like now you have to migrate it before you can use it. And that might be trivial, but it might not. There is a cost to these things. I hope there's never one that's as bad as this.

Speaker A
I think that was sort of the idea was rip off the Band Aid now and any future source breaking changes should be very small.

Speaker B
Yeah, exactly. And really well reasoned and well defended and stuff has to be for a really good reason.

Speaker A
Yeah. I think that these, like, I don't want to say that these changes were not well reasoned and well defended. Right.

Speaker B
Some of them were real forced, I thought, but I don't think they made the migration much worse than it was already.

Speaker A
I think that's probably true. Yeah.

Speaker B
This one's going kind of long. Yeah, we should anything else?

Speaker A
No, I don't think I have anything else to add and yeah, I guess we're going a little bit long. Thank you to everybody who has listened through this episode. I hope it's been at least somewhat useful.

Speaker B
Yeah. Or maybe a little cathartic, knowing that we suffered the same way you suffered.

Speaker A
Right. You're not alone.

Speaker B
Yeah. And thanks again to the Patreon listeners. It really means a lot that you all have been supporting the show.

Speaker A
Yeah. Thank you so much for your support and we will talk to you next week with a public episode.

