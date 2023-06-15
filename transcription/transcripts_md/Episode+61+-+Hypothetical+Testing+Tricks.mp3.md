Chris Dzombak
How's it going?

Soroush Khanlou
Pretty good. Pretty good. What's up with you?

Chris Dzombak
Not a whole lot. And I'm looking forward to the weekend. It's nice here and I'm going to go for a walk in the woods this afternoon and ride bikes tomorrow.

Soroush Khanlou
That sounds pretty pleasant.

Chris Dzombak
Not a bad weekend. How about you?

Soroush Khanlou
I am going to it's Saturday, March something 10th as we record this. I'm going to Atlanta tomorrow for a conference.

Chris Dzombak
Nice. And you're going to be speaking at this conference, right?

Soroush Khanlou
Yes, I am doing the you deserve nice things, which will have a little interesting topical addendum because of all this Swift Evolution like toggling of Bulls discussion and how should we think about this stuff and how does it fit in? So be a nice little addition.

Chris Dzombak
Are you wanting to talk about more of the discussion over tone of Swift Evolution discussion, or do you want to cover the addition itself?

Soroush Khanlou
Some of it. I'm not sure if I can express this point as well as I want to, and I'll depend on how I write it. But I really want to understand what is the reticence that some people have to adding stuff like this? Like just pure helpers and convenience stuff, because some people consider it almost like an affront of like, we don't need this extra stuff. Like, I can write this myself. And it's like, well, if it's there, you don't have to move your keys and go to a different file and you just write the code that you want to write in line. And so I want to try to tease out, why are some people so reddit add this kind of thing and why are some people more open to it? I'm very interested in that.

Chris Dzombak
Yeah, I mean, I know we talked about this a little bit in episode 59. At the very end of that episode. I think my reticence is just like the more stuff you add, there's just more surface area to learn. And that's not necessarily a problem, especially with something like toggle where it's pretty clear based on the name, what's going to happen.

Soroush Khanlou
Yeah, and it's optional. Like you don't have to use it if you think your code is better served or you don't know about it, you can just write my bull equals not my bull.

Chris Dzombak
Yeah, I mean, that's absolutely true. My other concern was just that it encourages code that tends to violate the law of demeter, which isn't great.

Soroush Khanlou
So that's true of this particular change, but there's other changes that make code more expressive or don't have crutches like that one might.

Chris Dzombak
Yeah. And I'm going to say in general, I'm in favor of adding those. I definitely appreciated the point of your, like, you deserve nice things talk. And we'll throw a link to that in the show notes.

Soroush Khanlou
Have you ever done my array equals myarray filter with this test? Like you want to filter in place?

Chris Dzombak
I mean, I can't think offhand, but I'm sure that I have. Right.

Soroush Khanlou
Yeah. I don't know. It's like stuff like that. I feel like when that's there, you would want it to be there, but I don't know because that's in some sense, like less duplication of thing equals thing filter.

Chris Dzombak
Yeah, definitely. Again, I feel like this is a case where do we want to encourage people to mutate things in place, or do we want to encourage a more functional style of thinking about things?

Soroush Khanlou
Right.

Chris Dzombak
And I mean, I guess Swift really isn't swift has some functional capabilities and you can pass functions around. Right. But it's not a functional language. So maybe adding stuff that lets you mutate in place is fine.

Soroush Khanlou
Yeah, well, there are some cases in which it's like the code is just better if you add mutating versions. I have a blog post that's kind of about this. So some of the Affine transform functions are some of them are mutating and some are not mutating. If you rotate by pi over two, let's say, rotate a few on its side right now you have to do like view transform equals view transform rotated by pi, which is pretty readable, but just view transform rotate by pi is a little bit better. And then if you're doing that inside an animation block, there are cases where we do rely on mutation as we write our code, and to ignore those, I think, is a little bit of folly.

Chris Dzombak
Yeah, I'll allow that. Yeah.

Soroush Khanlou
The other part of it is like the APIs just aren't consistent between should they be mutating or should they be not?

Chris Dzombak
Do you mean with things like UI kit or core graphics specifically, or just.

Soroush Khanlou
Not in general, even in pure Swift? So if you're looking at appending something to an array, if you want to create a new array that you've appended to the idiomatic swift way to do that is take your array, use the plus operator, and then wrap the object that you want to add onto it in brackets to create an array literal. And then append those two arrays together. There's no array appending, but there is an array append.

Chris Dzombak
I hadn't realized.

Soroush Khanlou
Yeah, and that's like, why is that mutating but and not not mutating?

Chris Dzombak
Yeah, I guess I guess that's fair. I wonder if there like I mean, again, common theme here. I haven't really followed the Swift evolution discussion, but I wonder if there has been discussion on the theory in Swift of how we decide what things get like mutating and non mutating counterparts and what things are just one or the other.

Soroush Khanlou
Yeah, I tried to kind of explore this in that post, and I think some of it is like when you want to insert or remove something from a collection that's almost always mutating for some reason, there's no array removing this object. There's no set inserting this object. You have to union it with another set that already includes that object. So I think it's like there is a pattern behind it, but I just am not sure about any consistency behind that pattern. One other note on the bull thing. On toggling bulls is I heard one other justification that I hadn't considered that I think is really good, which is if you have, like, an optional object and you have a bool on that optional object, if you want to flip that, like, optional object and then question mark, bool equals not optional object. Question mark bool doesn't work because you can't use the not operator on an optional pool because that's what you get when you do optional chaining.

Chris Dzombak
Okay.

Soroush Khanlou
So you end up having to guard it, unwrap it, and then flip it or do question mark, question mark false, and then wrap the whole thing in parentheses, which is ugly and talking. It's just way nicer than that's.

Chris Dzombak
Not great. I think that that may be the most convincing argument for this proposal that I've heard. I wish that that had been an example given in the motivation for the proposal, because I do find this more convincing than, like, sometimes you have to write MyObject object bool twice.

Soroush Khanlou
Yeah. I definitely feel that. Optionals make things weird. Optionals make things weird. Yeah. So heading to Atlanta, that's going to be fun. I'm excited to see a bunch of people and maybe some listeners of the show. If you're there, hit me up. Yeah, I guess this comes out.

Chris Dzombak
This will come out after the conference.

Soroush Khanlou
Yeah, this will come out next Friday, and the conference will be over. Well, I hope I will have talked to some of you. I expect to have talked to some of you. The whole thing is, like, tiki and Hawaiian themed, so that should be interesting. There's, like, a luau and should be cool.

Chris Dzombak
I don't know if we've ever been to a luau.

Soroush Khanlou
I also have not been to a luau. I have not been to non mainland United States, if that makes sense. I've never been to Alaska and Hawaii.

Chris Dzombak
Nor have I. I would like to I really want to go to Alaska at some point.

Soroush Khanlou
Yeah. Seems like a cool place.

Chris Dzombak
It does. I want to go in the summer, I think.

Soroush Khanlou
Yeah, that's probably right. Yeah. There's a lot of really good wilderness stuff out there.

Chris Dzombak
There is. Yeah. We have so many good national parks just in the US. Like, I'm a huge national parks fan and advocate.

Soroush Khanlou
Alaska has the only national park pretty sure this is right. That you cannot drive to.

Chris Dzombak
Really?

Soroush Khanlou
Yeah. Gates of the Arctic National Park. You have to hike to the edge of it. You have to park outside of it and then hike to the edge of it.

Chris Dzombak
That's awesome.

Soroush Khanlou
Yeah, it's pretty cool. And it's huge. Yeah, it's probably bigger than some states, I would guess.

Chris Dzombak
I'm googling gates.

Soroush Khanlou
Yeah. I think the way that most people get to the interior is they take an air taxi. So you just pay someone a couple of fly you and your gear out to some hilltop. Basically it's the second largest national park. It has a slightly larger area than Belgium.

Chris Dzombak
I'm just googling. So it's 13,238 sq mi and I'm on Wikipedia's list of US. States and territories by area. Okay. So it is bigger than several states here. It's bigger than DC, guam, american, samoa, the virgin islands, rhode island, northern mariana islands, delaware, puerto rico, connecticut, new jersey, new hampshire, vermont, massachusetts, hawaii and maryland. Maryland is no, it's slightly smaller than Maryland. Sorry.

Soroush Khanlou
Okay, so it's about the same size as Maryland. That's the national park.

Chris Dzombak
That's awesome. Oh man. And the Google search results for this click over.

Soroush Khanlou
Gorgeous results. Yeah, gates, the Arctic is incredible, man. I would love to go there sometime.

Chris Dzombak
Let's go.

Soroush Khanlou
Yeah, let's do it.

Chris Dzombak
So other stuff to talk about.

Soroush Khanlou
Yeah, let's talk about.

Chris Dzombak
So national parks are cool if you are visiting if you live in the US. And you don't visit national parks, you should check out whatever national parks are near you. If you're visiting the US. At some point, take some time to go to one of the national parks that's near to wherever you're going to be visiting.

Soroush Khanlou
I cried when I went to Yosemite.

Chris Dzombak
I've actually never been to Yosemite.

Soroush Khanlou
I've really good. I know.

Chris Dzombak
So other stuff that we wanted to talk about. I know that we discussed briefly ideas or your idea about an interesting thing you could do with dynamic callable, which is that it seems like we could make a pretty flexible reusable mock object using the dynamic callable and dynamic member lookup, right?

Soroush Khanlou
Yeah. In general, I think dynamic callable is so unreasonably powerful that we haven't even begun to scratch the surface of the crazy things that we can build with it. One idea that I threw out the other day was like you could build mocks that could just accept any message.

Chris Dzombak
Right. And then you can verify, I mean, much like you do in any mocking framework, verify that you received x message with Y parameters or verify that the code actually used this property.

Soroush Khanlou
Right, exactly. And is mock the right term here? I know there's like doubles, spies, mocks and stubs.

Chris Dzombak
So in this case I believe that mock is the correct term for what we're describing, something that records accesses to it and validates or allows you to validate what accesses were made to the mock object.

Soroush Khanlou
Cool.

Chris Dzombak
I will throw an article about mocks versus stubs in the show notes.

Soroush Khanlou
Cool. I can never remember the difference. And I used the word mock. We were talking about this in Slack and I was like, is that right? Is somebody going to get pedantic on me? So I got pedantic on myself prematurely so that nobody could do it.

Chris Dzombak
So mock objects. So after just a quick googling here, mock objects are objects programmed with expectations about the calls they're going to receive. Stubs are objects that provide canned answers to something, to calls that are made during the test. If you had a stub network client, you would say, when I make this network call, give me this response. It doesn't actually hit the network or anything. So in this case, we were talking about a stub. And then, if I'm remembering right, test double is just like any sort of pretend object. We had a mock or a stub that we use in tests.

Soroush Khanlou
Got it. So mock should technically only return void.

Chris Dzombak
I don't know if that's true. I think that you probably have a mock object that can return a value right. Because you need to do that in order to test interaction with at least some APIs. Right, right.

Soroush Khanlou
But doesn't that make it a stub then?

Chris Dzombak
I mean, these aren't super formal and exclusive definitions.

Soroush Khanlou
Got you.

Chris Dzombak
Okay, here we go. Martin Fowler. Mocks aren't stubs. We'll put that in the show notes.

Soroush Khanlou
Generally, if you have an object that can respond to any message, then it's really easy to say, okay, well, here's my mock. It's a dynamic callable. I expect it to hear this selector, and I expect it to have these things for parameters. Like, maybe you could pass in some special enum that says, like, oh, this can be any object. I don't care what this is. This needs to be this specific object. This needs to be an object that passes this test. I don't know what the API looks like exactly, but you could basically pass all this stuff to the mock ahead of time and say, like, hey, I expect these messages. And when you get these messages, you can return this value. And because it just accepts any message, it conforms to every protocol. It just works everywhere. And it's something that we really couldn't do in Swift before. Right. Because you had to have totally. Yeah.

Chris Dzombak
So the idea here is that you just have this single object that you can conform to any protocols that you need to conform to in order to inject this into whatever API you're using. And just by nature of the fact that it accepts any method, calls it conforms to any of these protocols. I think that the thing to call out here is that unlike in, say, Objective C, where you could just cast a mock object to any, like, pretend that it's any type in Swift, you would still need to have an API that accepts a protocol rather than a concrete type.

Soroush Khanlou
Right, right. Yes. You do have to do that.

Chris Dzombak
So if I want to have a mock object for let's continue for a network client class and pass that to something that uses a network client to verify interaction with that network client, that API can't accept a concrete network client class, it still has to accept a protocol that we can conform this mock to.

Soroush Khanlou
Right, right. Yes, it does open a question of once we have dynamic callable and dynamic overlookup, can you just conform them to every protocol?

Chris Dzombak
I forget whether there was anything about this specifically in the dynamic callable proposal, but I think that you could.

Soroush Khanlou
Yeah, I think that would end up being a really important part of it.

Chris Dzombak
I think that's key to an important part of just that dynamic callable functionality or an important part of being able to do this mocking specifically.

Soroush Khanlou
Well, both, but I think you want your Python object to be able to conform to some protocols, like if you're bringing them in.

Chris Dzombak
Yeah, I think that's definitely true. I think this makes sense thinking through I mean, unless I'm missing something, I don't see why having something defined in a protocol would mean that it can't be something that gets implemented or provided by a dynamic call or dynamic member lookup.

Soroush Khanlou
Right. And then it also gives you some type safety where you're saying like, this is the set of messages that it expects. It will handle all of them dynamically, and if it doesn't, it will crash.

Chris Dzombak
Right.

Soroush Khanlou
But you still get autocomplete because it's being represented as this protocol and so you still get some of the safety that you would expect. Yeah. So do you think this is a good idea? Like if dynamic callable were to land and I were to need some some mock objects to do some testing, do you think I should do this?

Chris Dzombak
Yeah, I don't see why not. I mean, think about the alternative here if you want to. I want something that conforms to my network client protocol that I can verify interactions on. I'm going to have to go through and manually implement the methods in that network client protocol and manually provide ways to verify these interactions. And maybe there's some clever code gen you could do with something like sorcery there, but I don't see a reason not to make one of these mock objects and use it for testing like this. This seems like a really cool idea to me and something that would really be legitimately useful.

Soroush Khanlou
Yeah, nice. Yeah, it was just something I threw out. I really think dynamic callable is going to completely change the way you write Swift. I mean, it's like more flexible than objective C in some ways.

Chris Dzombak
I mean, it is I think using it is maybe a little bit you.

Soroush Khanlou
Can see it kind of frowned upon.

Chris Dzombak
Well, I think it'll probably be frowned upon if you're using it everywhere in the code. And I also think that using it like dealing with arguments seemed like it might be a little bit clumsy, but.

Soroush Khanlou
Not more clumsy than defining your own object.

Chris Dzombak
No, definitely not. I think this is a good idea. Plus, it's not like this is going to be like you're not shipping this mock object in your app in production. This is like a tool to make testing easier any downside.

Soroush Khanlou
Yeah. In something like JavaScript, most of the test runners will interpret any Throne exception as a test failure. Right. And I assume this holds true probably for Ruby and maybe even Python, but I know it's true for JavaScript. And so what it means is that you can write a mock that accepts, let's say it accepts some parameters and then it verifies those parameters, like some qualities about those parameters, like maybe it's an integer that needs to be in this range. And if it's not, you just throw. And since you can throw from anywhere in the language, that will eventually bubble up to your test and cause a failure on that exact line with whatever message you give it. Because Swift doesn't really have anything like that. Right. Like all you can do in Swift is you can throw an error, which means that your type signature has to change or you have to basically trap, which means your whole process gets brought down, which I think in every case your tests are running in the same process. Maybe in the future that could change. But the idea is basically you don't really have a way of creating a test object and then a mock object and then verifying the parameters inside of that mock. You know what I mean? Does that make any sense?

Chris Dzombak
I'm not sure. Typically, you would have a you'd have in addition to just conforming it to whatever protocols you're trying to test, you'd have methods that are like, expect that such and such method gets called and then like, a method that just is like verify. And that method would be like throwing or would return, like true or false based on whether those expectations get fulfilled.

Soroush Khanlou
So I guess you would put a bunch of bulls in there and then say like, oh, was the int in the correct range true or false? And you could check that stuff later.

Chris Dzombak
Yeah, I mean, you'd have to come up with some way for the mock to remember what expectations were set up and then well, you'd be writing it.

Soroush Khanlou
Manually in this case. I'm saying like in current day Swift. I'm sorry, it would be really cumbersome.

Chris Dzombak
Oh, yeah. It is not pleasant to do this in current day Swift at all.

Soroush Khanlou
Yeah. So I think this is going to be really weird and I think we're going to think of even more goofy is the wrong word, but just like clever and interesting uses of dynamic callable and dynamic verbal lookup, it's going to be weird.

Chris Dzombak
Totally. I think clever is the right word here.

Soroush Khanlou
Yeah. With all of its somewhat negative connotations.

Chris Dzombak
Yeah. I mean, honestly. Yeah. But there are positive clever things you can do too.

Soroush Khanlou
Yeah. So I have one other question about this issue okay. Which is I can't seem to find it, but do you remember a while ago this is kind of more of a theoretical how should I test things question. I sent you an article that was like testing too specifically proves nothing, or something like that.

Chris Dzombak
Yeah, I forget exactly what I sent.

Soroush Khanlou
To you in Slack or Imessage I can't find.

Chris Dzombak
And the idea is maybe use the phrase tautology tests or something like that.

Soroush Khanlou
Yeah, that's right. That's what it was.

Chris Dzombak
Yeah. Okay, so what's your question here?

Soroush Khanlou
So my question is the thing that the person raised in this post was like, okay, well, we can write tests that say, like, this method was called and then this method was called, and then this method was called. But what you're really doing at that point is you're testing that the implementation is written in a specific way, not that the inputs and outputs match up in a specific way. And that test is actually not that useful because it causes a lot of churn. As in any time you could change the implementation to like, let's say, handle a new case, all those original tests are going to break. And so you're relying on these internal details of the class and it's collaborators to say, hey, this order, and this is how things must happen when this object works. And so my question is essentially, if we build mocks like this, isn't that kind of falling into this exact trap of saying, okay, well, verify that fetch Auth token was called on the data store, then this is fucking network example. Then verify that this method was called on the URL session. Then verify that this was called on this JSON Object Builder. This was called on the JSON Object Builder. And it's like, well, that's actually really tying us to this specific implementation. And maybe what we really want is to be able to, let's say, test this interface to ensure that anytime we plot pass in this URL, we get back this fully fledged object or something. Are we proving too much with this test?

Chris Dzombak
Well, I don't know. Kind of like a non answer here is it depends what test you're writing. You're right that this is definitely a tool you could use to effectively verify that every line of code in your actual implementation is there and is called. And obviously that test is going to be very brittle and will change when your implementation changes. So really it's a question of and I feel like we've talked about this before. It's a question of coming up with tests that are at a high enough level, that are testing more like interaction between APIs at a higher level in your application, rather than verifying that an implementation is what it currently is. Right? Really, you want to try to find properties, find and test for properties that should hold true with this API, rather than testing the details of whatever API you're testing does. And this sounds super abstract, and it's definitely something that takes a little bit of thinking and a little bit of practice.

Soroush Khanlou
Yeah, I think it's a bit of a dark art.

Chris Dzombak
Yeah, kind of. Yeah. But you're totally right that you could use this to write brittle tests that can be hard to maintain. I don't know exactly where to go from here on this train of thought, but you want to write tests where if the implementation changes for some reason, but the expectation that the test is looking for doesn't change, that the test doesn't have to change.

Soroush Khanlou
Right. And I think there's a lot of thought that's involved in, okay, how do I design this API such that I feel like I had one test in my JavaScript node API days where I needed the API to always return something in a very specific format. What was it? It was like something where it was like some hex digits and then a hyphen and then some other string. And so instead of texting holding the randomness to be steady and always checking for the same result string, I would like split on the hyphen and then check that the first half was hex and the second half could be like kind of whatever. It wasn't exactly that, because that sounds really stupid, but it was something like that where it was like I was trying to be really broad in what I expected, but as narrow as possible.

Chris Dzombak
Right.

Soroush Khanlou
That makes sense.

Chris Dzombak
I think that does make sense. It's all about trying to find trying to find that balance. So, as an example, earlier this week, I was changing some code in our sort of subscription and subscription handling business logic, like kind of boring code, but was testing some behavior around what happens when a subscription type changes, like someone upgrades or downgrades their plan for our application. And started out actually pairing with friend of the show andrew started out by writing a test that describes what is supposed to happen when the subscription changes when you call set subscription. Given these starting points and this ending point, what do we expect the state of this user's plan to look like at the end of this? And you could imagine testing that in terms of testing that with a mock, confirm that it calls these methods that change the database in these ways, but that really would be testing more the implementation. Right. So instead, the thing that we end up testing is actually the thing that is easier to test, which is just like, okay, set up a user who has this plan, who has this subscription, and then set it to this different subscription, and then read properties out about the user and verify that they're what we expect for the new subscription. So it's about finding a place where we're testing almost the public API on user rather than digging into the implementation to see to test how it works, if that makes sense.

Soroush Khanlou
It does make sense. It does make sense.

Chris Dzombak
Okay.

Soroush Khanlou
One of the tips that the writer of this post gives is keep I O separate from logic. And I think that's also a big part of it, of essentially saying, okay, we'll mock your objects that have to do any I O. So I hit the database, hit the network, whatever. You can mock those, but don't mock the objects that are, like, doing logic. Don't mock.

Chris Dzombak
Yeah.

Soroush Khanlou
So I think that's an important part. I do want to say also, shout out to Just Dave. He was the one that interests me, this article. He has this really cool Twitter account. I think it's what Just Dave reads and we got in the show notes, and it's everything that I think he likes on Instaper or maybe everything he reads in Instapaper. And it just gets auto posted to this account. And so I've actually subscribed to it and I find tons of really interesting stuff to it. And that's how I found this.

Chris Dzombak
Yeah, this is a great I think I'm following this Twitter account as well. Not logged into my normal Twitter account here, but yeah, there's some really interesting stuff comes across this feed. Something else that I wanted to note based on that example that I just gave is that what we're doing to verify this little change to how we handle subscription changes is an example of TDD, of test driven development. And I just wanted to call out here that a lot of the time people talk about TDD as this thing that you have to do top down, and this is how you develop your whole application. And it's this all encompassing, overarching methodology. But it can also just be a tool that you use sometimes, not all the time. Just when you have something, you're trying to make a change or fix a bug and there's like a clear spec and you're like, you know what, I'm just going to write a test that says when I set this property, this is the like, I end up in this state. And so just write like, a two line test that calls a property setter that doesn't even exist yet and then reads a property and asserts that things are the way you expect them to be. And then just write some stupid code that gets you to that point. And then look at your implementation, think, can this be improved? How can this be improved? But that's not how we have developed this entire application. Far from it. But it's just one of many useful tools that you have at your disposal. Writing software. It doesn't have to be this intimidating, all encompassing thing that you do all day, every day, right? It's just a tool for knowing, have I fixed the thing that this ticket says I need to fix yet?

Soroush Khanlou
Yeah, sometimes I really like it when you have a case where, say, like a parser or you have something, it has a bunch of different inputs and outputs, and you're going to need to be able to handle more complex cases than. You're handling right now, but you don't want to break the simpler cases that you've already written. And so it can be really nice to just say, okay, well, let's just do really simple tests for the simple cases. And then as I change this implementation internally, I want to be able to make the code more complex to handle the more complex cases and not break those early ones. And I'll keep running the tests every time. And that can be a really small part of your app, especially in iOS, since it's so hard to test UI stuff, breaking that stuff out into logic components or classes, instructs that do logic and then testing those to make sure that they don't break for the cases that already work, and they continue to handle newer and newer cases. And I found that to be like, the best way to do sort of TDD in an iOS environment.

Chris Dzombak
Definitely. Yeah, that totally makes sense.

Soroush Khanlou
So one time I have one little funny story about testing. Some people yelled at me about it, but I still think it was a good idea. I don't know if you remember, but back in the day when you had an NS data, if you called description on it, right, to just print it to whatever, it would return like an opening angle bracket, and then like eight hex digits and then a space, and then eight more hex digits and a space and so on until it printed the whole data. Do you remember this?

Chris Dzombak
Yeah, I do. And then this is how everyone was doing push notifications. And then everyone's push notifications broke.

Soroush Khanlou
Yes. So when Swift came out, they actually changed the representation. When you call description on Swift's data struct, right? So it's not NS data anymore. It's data struct. So it's a new type. So I feel like they were like, okay, this is a chance to fix this description that could print out tons and tons of stuff into your console if you just try to print this data. Like, maybe they don't want that. So they're like, all right, well, we're going to change it right now. So they changed it to it now prints data and then number of bytes, like 216 or something. It just prints like a number. I think that's what it prints. So this, of course, broke a lot of, as you said, push notification stuff. And because I essentially was working on an app at the time where we were moving fast, you're always moving fast. And I was like, well, whatever. I'll just strip out the angle brackets and the spaces, and I'll just send that up to the server. And then I was kind of thinking, I was like, you know what, this really is brittle, and this really could break. So what I did was I had a test and I assured that when I called whatever push notification token generate string version, that it would always be the correct hexadecimal string representation of that data. And I encoded that into a test, not really expecting it ever to break, but knowing that if it ever did break, we would know that the implementation of the description method changed and we couldn't rely on it anymore. Lo and behold, Swift Three rolls around and the test works perfectly. Catches the bug as we're doing the migration, and then we're running the tests, and then we see, like, oh, hey, this changed and this test doesn't work anymore. And at that time, that's when we wrote the correct you're supposed to map over it, actually turn every byte into, like, whatever you're supposed to actually use, like, a real formatter. And so I would love some validation in you telling me that what I did was right, or I would accept a little heaping of scorn as well. I would accept either.

Chris Dzombak
I don't have any scorn for you. That's a perfectly reasonable thing to do, I think, especially if you're doing something like that that, you know, is kind of a hack or like, this isn't really how we're supposed to do this, but we're going to do this because we have to ship this. If you can put a test around it quickly like that, it does provide a safety net there. Right. Even if you're not doing this exactly as you should be doing, you'll have some awareness when that test starts failing that something's wrong, and you need to go back and revisit that decision. And clearly this worked for you. This was a good idea, and it saved you from shipping something with this error in it.

Soroush Khanlou
Yeah, I thought it was a good idea, but some people told me that it was a bad idea, so I wasn't really sure if I did the right thing or the wrong thing.

Chris Dzombak
I mean, it stopped you from shipping a bug, right?

Soroush Khanlou
Yeah.

Chris Dzombak
Well, yeah, seems like the right thing.

Soroush Khanlou
Yeah. We had push token tests. I will put a correct implementation of how to generate the correctly formatted string.

Chris Dzombak
Into the show notes, because that definitely is the correct thing to do. But yeah, I mean, given the situation you're in, you like how to hack this together. Yeah. Put a test around it just to verify that expectation.

Soroush Khanlou
Yeah, seems reasonable. Cool. I think that about wraps it up.

Chris Dzombak
Yeah, I think we're at about half an hour ish.

Soroush Khanlou
Yeah, that was a cool topic.

Chris Dzombak
Yeah. Always fun to talk to you and.

Soroush Khanlou
Catch you next week. Catch you after Atlanta.

Chris Dzombak
Yeah. Enjoy your conference. I'll talk to you next week.

Soroush Khanlou
Sweet. Taxi, sir.

