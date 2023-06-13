Speaker A
I'm just gonna go for it. Let's just let's do it. Dive right in. Welcome, listeners, to another episode of Fatal Error. I'm, sirous. Khanlou.

Speaker B
And I'm Chris De Zomback.

Speaker A
Today, Chris wanted to talk about automated testing.

Speaker B
Yes.

Speaker A
So why do you think automated testing is good?

Speaker B
So let me preface this first by saying about this episode that this will be a sort of high level introduction into automated testing in general, and maybe techniques that you can use to start using automated testing in your app. There's a whole lot of detail that we could get into that we're not going to get into around various techniques and various approaches that you can use to write tests and to handle certain situations that come up when you're testing. We may record more episodes about this in more depth. But for today, why is automated testing good? Man, that in and of itself is a big question. Automated testing is good because it gives you confidence while you're changing software, that you're not breaking the software while you're making changes to it. If it's software that you wrote and principally maintained, that may seem less important. Except that we all know that code that you wrote two years ago, even if you're the only one who has touched the code, is going to be really unfamiliar to you when you come back after not having looked at it for a while. And if you have a large team of developers working on an app, or you're working on a project that has code going back years, and maybe some of the developers who touch the project aren't even with the company anymore, then it can be very, very hard sometimes to figure out how does this code work? How do these pieces interact? What underlying assumptions are made, what inputs are valid, and what functionality is expected given certain inputs, how does this code handle edge cases, all these questions like that. And so if you inherit this code, someone tells you to change this code, add this feature, fix this bug, it can be really, really daunting to come at that. And again, even if it's your code, it can be really daunting sometimes to come at that and say, I need to make this change and I probably need to make it fairly quickly and I want to be able to make that change with confidence. That I'm not breaking an API contract, that I'm not breaking an assumption that the code makes somewhere that I'm not breaking some edge case that the code handles. So that's my sort of pitch for why automated testing is important. It also, of course, helps if you have seen a bug in your application in the past and added a test to catch it, then automated testing can help prevent regressions, which really, really annoy your customers and users. So that's one other useful aspect of this.

Speaker A
Yeah, I find that the part of it where it's like, you wrote some code, and then you're going back to it, and it's like, well, how did this work? And I think when you're writing the code, you have this whole constellation of how these pieces fit together, and it's all kind of in your working memory, day to day. And then I have an API for a project that I work on, the API. I write the API. I'm the sole maintainer of it, but I only work on it a little bit every few months. And so there's tons of little educations and stuff I have to think about and reboot into my brain every time I need to get back into it. And if I forget to boot one of those things into my brain, the test harness for that API will catch and say, hey, actually, you forgot about this little detail over here. And I can say, oh, yeah, turns out I'm a huge idiot, and go back and fix that.

Speaker B
Right. Yeah. So that's another really good point, is you've kind of alluded to this, but I'll point out just very directly that good tests act almost as documentation. In fact, act as documentation for your code. You can write documentation in comments, and that's useful. That is helpful for people consuming your API. Right. But in terms of having I actually disagree with that.

Speaker A
And I'm probably going to be writing a post in the future, as we record, but in the past, probably from when this episode comes out, about how comments are not actually very good documentation because they fall out of sync. They're terrible.

Speaker B
Well, right, exactly. They can easily get out of sync unit tests. If you're running your test suite as part of, say, continuous integration, like Jenkins or Circle CI or Buddy Build or what are the popular ones right now?

Speaker A
Travis.

Speaker B
Travis yeah. Then your unit tests will not fall out of sync with the code. So they provide documentation for what expectations each of your interfaces and how to use it.

Speaker A
If you're going especially into a new project, it's maybe open source, and you say, Well, I want to get this kind of thing out, but I don't know what class to start with. I don't know where to start. I don't know what things to pass into the class. Having a test suite is kind of like a couple of demos of, like, hey, if you do this thing, this thing will come out. And if it's like a well written test case, you can actually very clearly see, like, given this input, pass it into this part of the app, and then expect this output.

Speaker B
Right. Yeah, that's a really good point.

Speaker A
So in your day to day work, as a percentage, maybe, how much of your code do you actually test? Because I feel like it's easy to talk about how good and how important testing is, but it's much harder to actually get started with testing and really get into it and get good at it and do it regularly and reliably. So how much of your code would you say that you actually are testing?

Speaker B
So I should preface this by saying that at work, we're currently working on a ground up rewrite of my application. So it's been easier for us to add tests, given that we're starting from scratch in a test driven fashion, than it would be to add automated testing to an old app. But we can kind of get into how you might start adding testing to an older code base as well.

Speaker A
Right.

Speaker B
In our current app, the test coverage is sitting at right around 70%.

Speaker A
And.

Speaker B
That is probably higher than your average iOS app.

Speaker A
Yeah, I think that's right.

Speaker B
That's as measured by Xcode's code coverage tool. Obviously, some things like Views and View controllers have pretty low coverage. In fact, basically no coverage view models have fairly high coverage. Sort of coordinating logic in the app has high coverage. Our entire modeling and persistence layer has very high code coverage. So all averages out.

Speaker A
How do you check code coverage in Xcode? There is I did not know you could do that.

Speaker B
How do you do that in Xcode? You can somewhere in your project setting, there's a setting for gathering code coverage information, and then there's a report that you can view somewhere. And you can also turn on a little almost right hand gutter in your Xcode editor that shows you what coverage the code that you're working on has.

Speaker A
We found the gutter that's editor, and then the menu item is show code coverage shows up a little. It looks almost like a line number. I'm actually running tests now on this project because I've never I didn't even know Xcode could do this. This is awesome.

Speaker B
Oh, yeah. That's really great. So somewhere either in the scheme or in the project setting, it's been ages since we set this up, so I don't remember. Offhand we'll add a note to the show notes about it, though. But you can turn on an option to gather that code coverage information. And then we actually so our code coverage reports are generated by our whole, like, Jenkins and Fast Lane tool chain and get posted via Danger CI as a comment on every pull request so we can see what files that were touched in the pull request have what coverage. It's a very neat setup.

Speaker A
So basically, you open a pull request and a bunch of machinery does a bunch of work and figures out if test coverage has gone up. Gone down. Exactly. Yeah. I see. Interesting. That's right.

Speaker B
And we'll add some links to the show notes relevant to what tools we're using to achieve that. It's like danger. CI and fast. Lane and Jenkins.

Speaker A
Cool. Very nice. So very, very high test coverage. So if your logic hangs out in your View controller, which is something we talked about a lot on this podcast, it's not as easy to test, right? So to test it, part of the scheme here is to move things into View models. Are there any other things that you all do to give you more testable code? We haven't even gotten to the writing tests part of it. But how do you get the code to be in a state where it's more testable?

Speaker B
So, as you mentioned, the View controllers are difficult to test, and we solve that by taking the non UI parts, the responsibilities that we not UI kit assigned a View controller and pull them out into a View model. And we covered those in episodes two and three. We'll add a link in the show notes. And so those View models then are objects that have no UI kit responsibilities and that we can unit test independently. Other things that will make your code more easily testable dependency injection is something that we've talked about over and over in various episodes. I don't think it's something that we've done an episode on specifically, but the idea sure, not yet.

Speaker A
Yeah, not yet.

Speaker B
But the idea there is that rather than say you're a View model or a coordinator or a View controller reaching out and getting a dependency, say, your core data stack or what other dependencies might you have?

Speaker A
Anything hardware related? Cameras?

Speaker B
Yeah, anything. Sure, yeah, that kind of thing. Rather than a class reaching out and getting one of those dependencies itself, you pass that dependency into the class. And that means that you can substitute a different sort of mock version of that dependency into the class that just maybe, rather than actually doing things, just returns the same value every time.

Speaker A
So I remember in Objective C, when I would do any testing, you could basically take any object and just say you think you're expecting this system? Maybe. Let's say it's a CL location. Manager I'm just going to make my own object that responds to the right messages and just tell you that it's a CL Location Manager. And it'll just work because everything is sort of message passing paste. You just send it a message and as long as it replies the right way, it's good. But in Swift, you can't do that anymore because some of those dynamic features are gone. So how do you solve that problem in Swift? How do you inject your mocks? In Swift?

Speaker B
You're right, that's definitely something that's more challenging in Swift. Let me finish up with why this is important. The idea is just that if you want to test something, you want to test one class or one API, you want to be able to do that in isolation, without dragging, without having to set up a whole bunch of dependencies in some known state. And that gets very complicated very quickly. So you want to be able to test one thing in isolation. And the way that we do that typically is by injecting mock or stub dependencies into an object that we want to test, rather than injecting the real dependencies, which are complicated and slow, actually touch the file system and network and things like that. Right. So you're right. In Swift we can't do that with the same ease that we can in Objective C. And really the best way to do that in Swift is via protocols. So this is an argument for protocol based design. Rather than accepting dependencies of a specific class or structure type, your objects should accept dependencies which are described by protocols. And that means that you can inject in the actual application. You end up injecting the actual instance of, say, a core data stack right. Of a location manager. In your unit tests. You may have a protocol that describes your core data stack or a protocol that describes a Location Manager. And you can just create a very, very simple object that, say, always returns the coordinates of New York and inject that into whatever object you're testing. So that takes care of fulfilling that API contract for your dependency in a very simple and predictable and consistent way. And that lets you test whatever thing you're testing in isolation with known and stable input that you control that doesn't require any external resources.

Speaker A
Right. So as long as you have stable input, you can make sure that your output is stable and you can test and make sure that that is always what you expect it to be given the specific input.

Speaker B
Right.

Speaker A
Awesome.

Speaker B
So something to note there is that that works, obviously for objects that you control. Right. You can design your own applications objects in such a way that it's a very protocol based design. If your dependencies are from frameworks you don't control, like, say, Apple's CL Location Manager, you may end up creating a protocol that duplicates some of the Location Manager API and just saying that CL Location Manager conforms to my new protocol. Or you may define a protocol that defines what your application expects from a Location Manager and writing some sort of adapter or facade that wraps the core location framework. So it is a little bit less elegant than in well, it's a little bit more work than in Objective C. It's probably I don't know, we can argue about how we define elegance.

Speaker A
Right, right. I think it's perfectly elegant. I think it is more work, but I also think it's a little better. CL Location Manager may not necessarily have the exact methods that you need. It may need to be brought together with some other thing. And you can bring those two things together in your own little class and then mock that. And that, I think, can be better in its own way, even if you can't directly mock objects that you don't own.

Speaker B
Right. One rule of thumb in testing is don't mock objects that you don't own just because if you do that, you're going to end up with somewhat of a mess on your hands down the road when the object that you're mocking changes. Right?

Speaker A
So the idea with that is if you have a view controller or sorry, if you want to test UI navigation controller, you wouldn't mock view controllers to insert into it. An example would be if you wanted to test some behavior of your view and you want to add a sub view to it, you wouldn't add a mocked sub view because the things that UI view does to other UI views you can't know about, you can't control. So why try to expect something to happen there that is that making sense?

Speaker B
I think it's making sense, but more the rationale behind this rule of thumb. And we'll put a link to a really good wiki article about this in the show. Notes is that these mocks and stubs and basically test doubles are sort of a generic term for these objects which sort of mirror what is happening in our application is that in test driven development, your tests should be used to help develop sort of focused interfaces between whatever you're testing and the thing that your code depends on. And so if you're just mocking someone else's API, then that hints that you may not be designing the right API for your use case. Right. You are just taking someone else's API, which is liable to change, at which point you'll have to update all your mocks and tests. And that is sort of a smell that maybe you should be inventing your own interface here that does what you want and wrapping that dependency behind that interface.

Speaker A
So that's evidence that maybe instead of creating a custom CL Location Manager protocol that you conform CL Location Manager to you, make your own interface, wrap CL Location Manager and work with it that way.

Speaker B
Right. That's probably going to be a better approach.

Speaker A
Yeah. I've also found that CL Location Manager, along with many other Apple classes, kind of does a lot of stuff. And I don't necessarily want every class that touches CL Location Manager to be able to do all the stuff that CL Location Manager can do.

Speaker B
Right.

Speaker A
It can also be nice in that sense to limit the behavior that it has. Although you can do other protocol too.

Speaker B
You could do that just by selectively including things in your protocol. Yeah. Boy, was that ever tortured. Let's move on to another question.

Speaker A
That sounds good. So we've kind of covered why testing is important so you can be sure about the changes that you make. But I think certainly I can speak for myself. I had a ton of trouble getting started with testing and even trying to understand what is the first test that I should write. What is the first valuable test that I should write? One of the things I want to get into is like, okay, let's say you have a code base with zero tests. How do you even start? Where do you even begin?

Speaker B
Sure, yeah, that's a really good question. As I noted, my current project is we're writing in a test driven fashion from the start, but I can probably provide some thoughts here. So my answer would be not necessarily to go in one morning and say, okay, I'm going to cover this application in tests that may or may not result in something that's useful and you're probably not going to get the time to do that from your project manager anyway. Yeah, checks out. So instead, the thing that is probably going to be very useful to do is the next time you pick up a ticket, a new feature, or a bug that you're fixing, figure out what area of the code you're going to be working in. And in the case of a bug fix, try to write a failing test for that bug. So try to write a test that describes the expected behavior and that test is going to fail given that this bug, that it's not the expected behavior is present in your application. And then fix that bug and see that test pass. And maybe while you're working on this, there are some related methods or related classes that maybe it's also going to seem useful or seem apparent that like, oh, I kind of see what this method is supposed to be doing. I can characterize this with a test and that's going to help me toward fixing this bug. Same, if you're adding a feature, you may find it easy to sort of add whatever interface you think you might need and then write a failing test that describes what you want that interface to do. If you're going to be using or modifying other code in the application, again, try to characterize that code that you're sort of working with or working adjacent to with tests as you're working on this ticket. That's really going to be how over time you build up a meaningful test suite in an application that you've inherited or an application that you wrote that doesn't have tests. Does that kind of make sense? Does that seem intuitively useful?

Speaker A
Yeah, it definitely does make sense. But one of my fears is that that advice is really great for people who write code on the server, where if you think about it, the code on the server is very much like you kind of get a string. And that string is probably JSON, some kind of post data, or it's a URL that you got to parse and do something with, and you parse that URL and that data, and then you turn it into all your model objects. You fetch a bunch of stuff from the database, you do a bunch of work to it, and then you kind of just return another string. And so because it's already like, oh, it's just data going in and data coming out. I'll just have some data that goes in and I will test to make sure it does all the right things and presents me with the right data coming out. But I am kind of worried that the apps that we work on, definitely the apps that I work on, are so UI heavy that you couldn't write a test that's pure code that describes the expected behavior the way you could if we were working on a server app of sorts. And so you have to do something else first to get it to the state where even that type of thing could be tested as your quote unquote first test.

Speaker B
Sure, that's a totally valid point, especially if you're working in an application that doesn't use something like View models heavily. Maybe you have a lot of stuff in a View controller, I feel like is what you're really getting, which I think is common.

Speaker A
Which is really common.

Speaker B
Yeah, which you're right is really common. A couple thoughts here. We'll see if I can get through all of these. First of all, that's definitely true of some problems, maybe not so much of others, or of some new features, maybe not so much of others, particularly if you're adding a feature. If you're adding code, it will be probably easier to write it in a test friendly way, even if that code is going to be using a singleton that's in your app, it doesn't have to reach out to the singleton instance. You can inject the singleton instance into it. Right? We talked about that, I think, in the singleton episode. So that's one case where if you're adding code, then you can at least add that code in a pretty friendly way. Not all code in these apps, not all code in these apps is UI code, right? So occasionally, for example, a ticket that I took today was to update one of our data models and the JSON parsing code to be in line with a new data format from the server. That's something that if you did have to make a change like that, which admittedly is going to be fairly rare, but that is a case where things are pretty easily testable, right? Parsing code is pretty testable. Serialization deserialization code, unless you're doing something very, very strange, is going to be pretty easy to isolate and test. Now, let's say that you got a UI bug in the View controller, and it's a big View controller, and this is going to be a huge mess to get tests around. A few things that come to mind right offhand. First of all, it may be truly a user interface bug. Maybe it's a layout glitch. Maybe it's a bug where some things are on color. What might make more sense is to try to add not a code unit test, but a screenshot test for this view. Once you've fixed the bug, you can at least characterize well, that assumes a lot about what you can inject into that view controller. Yeah, but okay, I'll just say that maybe screenshot testing is going to be harder in a legacy view controller, but it may be something that's worth considering. See if you can do that. The other thought is see if you can extract the problematic area of code. If it's a color, maybe that color is determined by some logic that could be extracted to another object, some sort of formatter. Even if it's you don't have to create a full blown view model. Maybe you can extract just that logic into something that you can cover with tests. Right. And then all that's left in the view controller is binding that code to the view and that's something that down the road. You could maybe even start testing via some interaction testing. If you decided to go down the road of trying to inject dependencies into that view controller, you can verify that the view controller checks with that formatter. Right. So there are ways to sort of start decomposing even a relatively complicated view controller and start teasing it apart, start finding things that you can test. And you're right, maybe there's something of view controller that you don't have time to figure out how to extract and refactor and cover with tests. Like, that's possible. I want to give a shout out to the book working effectively with legacy code. Here we'll have a link in the show Notes by Michael Feathers, which I clearly need to review. I haven't read it in quite a long time, but that's going to be a really useful book for you if you are in the situation where you have quote unquote legacy code, right. That basically code that was not written by you or by someone that you know or wasn't written in a very test friendly fashion. Right?

Speaker A
Yeah. I believe Michael Feather says that any code that doesn't have tests is automatically legacy code. Yeah, I think that's his, like that's his big catchphrase thing, which is a scary thought. I'm worried that I don't think testing should be that scary because that makes you think that, well, if I can't test cover this entire app, then I might as well just do nothing because it's not worth it. And it's like it's not true. It's like that very first test that you write is the most important one. You go from 0% test coverage to non 0%. Yeah. Not zero. It's like an infinite percent jump. It's pretty great.

Speaker B
Yeah, that's how math works.

Speaker A
Yeah, exactly. And like, that first test is that first test is great.

Speaker B
And that's a regression that your users will not report in the future. Right. Because you will catch at least that bug before you ship it again. Or that's an API assumption that you made in some code that you added that some developer down the road won't violate and cause your app to crash in some weird unforeseen edge case. Right.

Speaker A
You brought up an interesting thing, which is you brought up extracting logic from your view controller. And I think that's such a great that's such a great nugget about testing is like if there's an if statement or a switch or a loop, that's a place where a branch is created and a choice is being made. And if you can extract that choice into something else, you can test that choice. And that is so useful. This is a tactic, it's really stupid, but it totally works, right? If you have, let's say, Table view did select sell it index path or whatever, and you have to say, well, if it's in this section, go down this path, and if it's in this other section, go down this path. Make an enum that says like, route to user and route to article or whatever. I'm making up a very boring example, but make an enum that returns two options. Make a struct that takes an index path in its initializer and returns which of the two options that should go down and test it. And you will have made an enum purely for the purpose of testing. And that's okay. Now you have this expectation baked into your app and you have it baked into this object and these tests that work with it and it's just not going to break anymore.

Speaker B
Yeah. Or you've introduced an enum not for the purpose of testing purely, but for the purpose of modeling some part of your application logic.

Speaker A
Right. It helps to decouple the rights, meaning.

Speaker B
And stuff for modeling application logic decoupled from UI Kit.

Speaker A
Right. And then at the call site, it sort of looks like article router or whatever kind of router, where should I route to? And it'll say, well, either the case is you need to route to an article, in which case you'll call a method that has to do with articles, or you'll need to route to a user, which you'll call a method that has to do with routing to users. And that is so much more clear than index path section equal equals zero. Do this next path section equal equal one.

Speaker B
Is that right? So one other thing to note, one other useful technique. If you're trying to characterize some code that's maybe not in a view controller that's in some more sort of application domain object that maybe doesn't lend itself really well to testing directly for some reason, you may still be able to find somewhere one level back, like something that uses this object that you can test, that you can characterize. Like maybe even if you for some reason can't test the thing that is the very root of the bug, maybe you can test the place where the bug shows up. Right, so look at stuff like that. It would be better to test very close to the interface. That's actually a problem. But if that's not possible for some reason, maybe you can test like one level. Up, right? So that's one other thing to look at when you're trying to so how would that work?

Speaker A
So, for example, if you had like, a View controller that does a thing in a certain color, if you can't test that logic in the View controller, you would actually maybe do a screenshot test instead because that's like one level removed.

Speaker B
I'm thinking more outside of the realm of view controllers now, but maybe there's some I can't come up with a very good example offhand, but maybe there's some object that has some complex behavior and is going to be very difficult or impossible to test directly for some reason. But it's used by some other object. Maybe that's kind of a facade to it. Then testing that maybe facade object instead of testing the problematic object directly is maybe not ideal, but that is a viable way to get a test in there, at least, which is better than not having a test at all.

Speaker A
Got you. So one thing I want to give a special shout out to is there's a post by this blogger that pseudonymously, goes by a Pokemon name of Eevee, and it's called Testing for People Who Hate Testing. And it's just it's such a good post. It starts out, I love having tests. I hate writing them. It's tedious, it's boring, it's hard, sometimes harder than writing the code. Worst of all, it doesn't feel like it accomplishes anything. And it just really encapsulates the way that I think I personally feel about tests. I think a lot of people feel about tests, which is just like, yeah, this seems great, but I don't have time to do this. I got to write code. I got to do work. What is this for? And since the benefit that you get from writing a feature is instant, but the benefit that you get from writing a test may pay off, it may save you a month, two years from now, you never know. The incentives aren't quite lined up. And so this person goes into a bunch of details of how to have a good testing harness. So tips that Evie points out are like, write the code that you need to make running your tests easier. Make your tests really fast so that you can run them as often as you want without having to deal with any performance penalty. If it takes minutes, that's bad. If it takes hours, you're basically never going to run them. Make it run automatically. Make it test as small things as you can. Test data coming out rather than side effects. Tons of little tips of just like, how do I just gorilla test this whole thing? I just don't care if it's good. I just really want some tests and I really want to get into it. And I think this post, which we'll put in the show notes is just such a great example of how to approach it and how to think about. Just like tests are great fun to write, I think people pretend that they're really fun to write. They're not art. Do you enjoy it? If you want to hire Chris to write your tests? I don't think he's looking for a job, but I don't know. Writing tests, for me, it's grueling. Maybe there are people out there that enjoy it. For me, it's grueling, and the way that EV approaches this stuff makes me sounds a little bit less terrible.

Speaker B
So for me, testing is it's almost part of the design process, right? Maybe you've already kind of figured out how your interfaces interact, but when you're writing tests, you're really forced to think, okay, really, how do these interfaces work together? Like, you're writing code that uses your interfaces, right? Do my interfaces work well? What inputs and outputs am I expecting? What should happen in this weird Edge case that's, okay, maybe not enjoyable, but surely seems like a very important part of the design process, right? And one of the points that I loved in this EV post, which I'm happy to end this podcast on this note as much as any other, if writing tests is hard, that might be a bug. So one advantage to sort of a test driven development fashion, which I didn't even mention at the beginning, is that writing tests really can push your code to be maybe not cleaner, but can push your interfaces to be more well thought out. To help you enforce a single responsibility principle. To help push you toward erring on the side of dependency injection rather than, say, using singletons for everything.

Speaker A
If you're on the side of small.

Speaker B
Objects, erring on the side of small objects. If the interfaces you're writing are difficult to use in tests, and you're going through just such a hard time setting something up for a test that maybe isn't because testing is hard so much as because you've defined a really, really complex interface or a really complex class or really complex interaction between objects between classes. And that is a problem that you should consider solving, like in your application code.

Speaker A
Right. He writes, if you have a hard time constructing your own objects with some particular state, it might be a sign that your API is hard to use. I think that's really great.

Speaker B
Yeah.

Speaker A
There's a million things I want to talk to you about testing about, just.

Speaker B
Tons and tons of things I would love to talk about so many more of them. We're already at, what, 40 minutes into this podcast. I'm not sure how happy I'm going to be with this episode because there's so much more I would like to say on so many topics, and we kind of threw out some terminology in this episode without actually defining it. That's mostly my fault, but please send us questions. I'll be happy to send interesting articles and thoughts and terminology definitions via Twitter.

Speaker A
Yeah. And if you want us to talk more about testing, we'd be happy to do it. So let us know if you want to hear more about that.

Speaker B
Turn that into a thing, please let us know. We can record as many episodes on this as our listeners want. Things that we didn't even cover today. We didn't really get into screenshot testing. We didn't talk about the sort of behavior driven development style of testing.

Speaker A
I just want to say I still have no idea what BDD is. Well, maybe we should zero CLO.

Speaker B
Well, maybe we should do an episode about it. Maybe we should UI and automation testing, performance testing. You could do an entire episode just on the working effectively with legacy code book. We can talk about testing with various fun libraries like OC, Mach and Ohhttp Stubs. Possibilities are end, by the way.

Speaker A
Great library.

Speaker B
Absolutely. I love that library. So let us know what you would like to hear about and I'll be happy to talk about it.

Speaker A
That sounds pretty edge. Well, this was fun as always, Chris.

Speaker B
Yeah, absolutely. I will talk to you soon.

Speaker A
Sounds good.

