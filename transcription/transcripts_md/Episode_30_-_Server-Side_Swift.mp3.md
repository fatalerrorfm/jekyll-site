Speaker A
No, that's a sentence.

Speaker B
That's right.

Speaker A
It's really weird to do this with people.

Speaker B
Usually we don't even see right.

Speaker A
It's weird enough. Yeah.

Speaker B
Hello and welcome to Fatal Error, episode 30. This is the last episode of season two.

Speaker A
That's right. So at the end of.

Speaker B
I can look at Chris because we're in the same room. Chris has come for a visit, and we've actually gathered a few friends together here for a live studio recording.

Speaker A
As you were saying. Right. This is episode 30, which means this is the last episode of our second season. We arbitrarily decided we were going to do a 20 episode, 20 week season, and this is the end of that. So after this, we're going to put Patreon on pause so that you won't be charged for June.

Speaker B
June.

Speaker A
And then you'll be charged again in July. And episodes will start going up July 6.

Speaker B
That's right.

Speaker A
And that'll be season three.

Speaker B
Yes. Cool. Yeah. We really want to thank you for supporting our patreon and helping us with editing costs and hosting costs. It really means a lot that people even listen to this podcast and that they appreciate us enough to pay us a little bit of money.

Speaker A
Yeah, absolutely. And if it weren't for you Patreon, then we would not be doing season three because we would have been paying a whole lot of money for editing.

Speaker B
Do we have any other erotic to cover before we odds and shods, as they say.

Speaker A
I think that's everything. Those are all the odds and SOS that I had written down.

Speaker B
Cool. Great. This week we wanted to talk about Swift on the server.

Speaker A
That's right. So as I understand, Rich, you have recently started a Swift on the server project.

Speaker B
Yes.

Speaker A
What are you doing?

Speaker B
I am starting a little project. It needs an API, and so we basically have a postgres database and a little bit of massaging of data, and that's basically it. So a very simple project, really, I think good for building our Swift on the server.

Speaker A
I guess a good place to start would be why did you choose Swift on the server to start?

Speaker B
I'm sick of node JS Ruby is fine, but I want all the niceties of Swift.

Speaker A
I want a type system.

Speaker B
I want type system so bad. I want enabs and protocols. I want all of the stuff. And I like swift, and I'm good at it. And I know how to make good stuff happen in Swift, and I just want to be able to leverage that on the server as well.

Speaker A
Okay, cool. That totally makes sense. So as I understand, there are a number of server side Swift frameworks. I've not used any of them or done any server side Swift work. So what did you look at when you were starting this project?

Speaker B
Yeah, so like I said, there are a few we kind of held off on this topic. I think both of us kind of were curious about it, but since neither was having experience, we held off for a while. But I started this project maybe like a week ago.

Speaker A
Okay.

Speaker B
So now that we have some literally days of experience, I have many days of experience with Swift on the server. So there are some different frameworks. One of them so there's Vapor, which is the one that I chose. There is perfect. There's IBM's, Coutura. There's one called zero, which I think is around zero.

Speaker A
That sounds great.

Speaker B
There's a couple of other smaller ones like we talked about, friend of the show, Kyle Fuller's Frank, which is another server writing library that he wrote.

Speaker A
Right. And we mentioned that in the Japan episode. Right?

Speaker B
Yeah, that's where I met and got the hang of Kyle. Okay, so there's a couple you have a lot of different choices, but in terms of ecosystem and in terms of the available libraries and everything perfect. And Vapor are the ones that are really high up there. We have some friends that use that have used Coutura, and they say it's good as well. But the main thing that drew me to Vapor was that they have the most installs of anybody, so I figured they would have hit the most problems, and they had a thriving clock community with thousands of people in it that I could actually ask questions of.

Speaker A
That totally makes sense. Thousands of people. Really? Thousands of people are so how many people actually writing Swift on this server now?

Speaker B
According to my analytics, I'm not really sure.

Speaker A
Well, I mean, like, is it thousands, hundreds of thousands?

Speaker B
I would guess maybe tens of thousands. I think in terms of active projects that are actively serving daily requests, probably closer to hundreds, maybe thousands. Yeah, that's my guess.

Speaker A
That's still pretty good. Yeah.

Speaker B
And here's my thing. I feel like if somebody had written, like, a critical service for their app or their API in Swift, they would have bragged about it. They would have said, oh, we're in Swift here, and aren't you proud of us?

Speaker A
Yeah.

Speaker B
And so since I haven't seen anything like that, I'm kind of thinking that there's fewer, like, really serious production, deploys mostly side projects and stuff like that.

Speaker A
That was kind of my thinking.

Speaker B
Yeah, that's my guess.

Speaker A
You've been writing Swift on the server for several days now, right?

Speaker B
At least four.

Speaker A
At least four days. What have you gotten done so far?

Speaker B
I have OAuth working with Twitter.

Speaker A
Is there a library that you used for OAuth?

Speaker B
Okay.

Speaker A
Yeah.

Speaker B
So that's kind of why it took a long time. So Login working and then this thing relies on your Twitter mutual. So I have basically a calculation that intersects the arrays of your followers and what Twitter calls your friends, which is the people who are following.

Speaker A
Okay. All right. So that's a not trivial amount of interaction with another API.

Speaker B
Yeah. So I work with web services and then I've been working with our database as well, so I have a little bit of both sides of that coin. Okay, yeah.

Speaker A
How's that gone?

Speaker B
So the documentation is terrible.

Speaker A
The documentation on Vapor side, on Apple.

Speaker B
Side, on Vapor side mostly. But then there's also lots of other stuff. The documentation is terrible. The library support is really bad. Trying to solve anything involves digging into the source code to figure out exactly what's going on. The foundation frameworks are not implemented. So if you want a URL session, you can't get URL session shared, can't make an ephemeral configuration. There's lots of date math that's not implemented, stuff like that.

Speaker A
Those are the things that there's the ongoing foundation rewrite in Swift. Right?

Speaker B
Right, exactly. The Cordless Foundation rewrite, all of that stuff is true, but I'm having the time of my life.

Speaker A
Okay.

Speaker B
It's really, really fun because you're writing Swift. It's on the server.

Speaker A
That's awesome. I'm really glad to hear that. So you mentioned library support and you dig into the source code. Are these problems with the frameworks that are available now? Is this something that the Swift team could do more to support? What source code are you digging into to find problems?

Speaker B
Yeah, so like, for example, when I started this project, it was on Vapor 1.5 because I picked the template at random just to get something going. And Vapor 2.0 had actually come out by then.

Speaker A
Okay.

Speaker B
So when I looked up how to do shell one hashing for the OAuth signature, it just didn't work with the syntax that looks like should work from the GitHub repo. Turns out it's changed in Favor 2.0 and I needed to use the Vapor 1.5 syntax, which I didn't realize. You can't command click on anything because you can't really use Xcode. You can. It's tough because there's a weird thing of like, if you want to run on your Mac, then you're using the Mac version of foundation, but then when you deploy it, it's not going to work because all those pieces of foundation are not there. Then you run on Linux, it's going to target like when you build it's going to build using the Linux build system. And so Xcode doesn't know about that. And so the wrong things from syntax highlighted and it just doesn't work.

Speaker A
Right. How's? Writing swift outside of Xcode.

Speaker B
Just in general, I really miss Autocomplete honestly. Option clicking on stuff for types are autocomplete command clicking on types to see what can we do with this type? What is this, how does it work? And being able to export the graph of types that we have is just like sorely sorely miss that.

Speaker A
Although it works in Xcode half the time anyway.

Speaker B
Yeah, Xcode is broken. It's always yeah. You asked basically what libraries, like, who could fix the libraries, right?

Speaker A
Like, what library support issues are you running into and who can contribute fixes here?

Speaker B
Right? Basically it's everybody's fault. Apple could do better by finishing foundation. I don't know how long it would take, but it would be really nice if we could use all the parts of foundation. And then the Vapor team, their documentation, they have documentation for some stuff, but they really, really could do a much better job. There's things where it's like really basic stuff like you want to know how to join two tables for like a menu to many connection and you want to use custom foreign keys. Should not document it anywhere. I don't even think it's possible that's like the next thing that I have to figure out and they don't say because not that many people run into that problem.

Speaker A
Are you sending documentation pull requests as you're encountering these?

Speaker B
Well, I know library maintain the end user. Yeah. So Vapor could step up their documentation game a lot. And the other thing is Vapor is broken onto many, many different git repos and many different modules. So there's like Vapor core, vapor JSON, vapor node, which is not node JS, the different nodes that they use. It's weird. And then there's a Vapor engine which is like the HTP stuff and all these components. So you go digging for something. So you're like you have to search the GitHub to find it because you can't really reliably find it any other way. But let's say it's not in that repo. Then you have to go look somewhere else and eventually you track it down and then it doesn't make sense, like I said, because you were looking at the 2.0 version of the code and you need it to be the 1.5 version. So that stuff is challenging. So Vapor could definitely work on just unifying the thing, making the documentation better. The people I've talked to on the Vapor team said they are working on that. They have a brand new documentation page coming. But that's just like it's a flog and it's like the stuff that happens when you get more and more users and more and more contributors and stuff like that.

Speaker A
Yeah. And so you're a fairly young project, right? Yeah.

Speaker B
And then lastly, there's the third party developers who make libraries just throw them off GitHub and put a Pod file in there and say my job is done.

Speaker A
I have definitely done that.

Speaker B
But the thing is those don't necessarily work on they don't work on Linux. So that's part of the reason I rewrote OAuth thing. One, because I want to learn how OAuth worked and two, because you can't. Like really the thing I needed was the ability to build the OAuth signature, which is like the thing that signs all the parameters and query parameters and URL and method and everything and gives you one thing that the server can check to make sure that the request wasn't tampered with. But that doesn't exist as like a standalone component anywhere. So I had to kind of extract it from this other project called Swifter, which is the Twitter client written in Swift. It took a little while to get everything to work, and it's not really that person's fault because why would they expect to be used on the server? Like, why would a server be making connections to Twitter? Like, this stuff's brand new. But at the same time, this was another hurdle that you kind of have to get across if you're going to use this stuff.

Speaker A
Okay, that makes sense. So one of the things that you've mentioned, you mentioned pod files, you've mentioned that Vapor split into several modules, right. What does package management look like in Swift on the server world?

Speaker B
Right. So I don't know quite enough about it, but definitely we're not using Cocoa Pods. Everything is Swift package manager based. When you load that vapor template, it gives you a package that Swift file, and Vapor is one of the included dependencies. So when you run the build oh, builds are really slow too. That was another negative. I didn't say oh. And testing is really hard too. You got to make up a separate module. You can't test the actual executable that you make.

Speaker A
Doesn't Swift have the Swift PM have some testing facility built in?

Speaker B
It is, but the way you do it is by extracting all your domain logic into a separate module, and then your app module or your app module is the one that gets to execute, and then your domain logic module is the one that you can build into a library that is testable.

Speaker A
Okay, interesting. So you're using Swift PM, right?

Speaker B
Swift PM, so I haven't had to install any other packages yet. And you know me, I'm a little wary of other people's code. So far it's just in Vapor, I haven't used any third party networking libraries, third party Twitter libraries. Vapor comes with a postgres adapter, so that part is kind of taken care of for you.

Speaker A
Okay.

Speaker B
It comes with this thing called Fluid, which is their basically RM. So I've been using that stuff.

Speaker A
Foundation's Nsurl session isn't like rewritten in Swift. So Vapor has done their own Http.

Speaker B
Yeah, so URL session does work. I am using it for the Twitter.

Speaker A
Okay.

Speaker B
But it's only certain parts of URL session that are missing. But I don't think URL session will handle receiving a request and sending a response. I think that's what their quote unquote engine is for.

Speaker A
Okay, all right. Makes sense.

Speaker B
So one really interesting, weird thing that's been fun is Vapor is totally synchronous.

Speaker A
Okay, so what does that mean exactly?

Speaker B
So it means that basically you register a function for every route, and that function takes a request and it returns a response.

Speaker A
And it returns like, some responses getting sent back to the browser. To the API client.

Speaker B
Exactly.

Speaker A
And that function is synchronous.

Speaker B
That function is synchronous. Okay, so the way the node works, node has like, it'll give you a request object that you can read parameters off of, but it'll also give you a response object that you can send data to. Right, so you can do Async stuff and then just grab a reference to that response object and just send it the thing and then tell us that it's completed.

Speaker A
Right.

Speaker B
Vapor doesn't work like that. I'm given to understand that Katura does and Perfect maybe does, but vapor doesn't. And so what that means is it's a lot like writing Ruby on Rails. Everything is synchronous. So when you make a network request, it can just be a function that you call and just return the value.

Speaker A
That you want, like beautifully straightforward.

Speaker B
Yeah, there's no netting, there's no indenting process. And then the function is also throws so you can handle your errors there.

Speaker A
Okay.

Speaker B
Which is also cool. And almost every function in vapor is marked as throws so that you can basically throw from anywhere and it'll get handled correctly in terms of should it be a 404, should it be a 500 or whatever.

Speaker A
Okay.

Speaker B
Yeah. They have certain codes that if you have certain error types that if you return them, it will automatically turn them into a like 404 or four three right. The right Http or whatever, all that stuff. Cool.

Speaker A
All right.

Speaker B
So the synchronicity basically means that since all your networks now don't need to have completed blocks, promises or anything, they can just return stuff. So I basically code just reads really nicely. It's like, hey, get the followers from Twitter, hey, get the following from Twitter and intersect those and it's just like one after another and you're done.

Speaker A
If you wanted to say, get your followers from Twitter and your friends from Twitter Asynchronously at the same time and then what sort of concurrency tools do you have available if you want to do something like that?

Speaker B
Right? So the one thing that you can do is if you do necessarily you want to be Asynchronous and you want two things happen or you want them to be parallel, let's say, right? They give you a special thing that you can return and it's called like response Async, and then you pass a block to that. Then that block is a parameter that you can tell when you're done, basically.

Speaker A
Okay.

Speaker B
Kind of like nodes, like response, you'll tell it when you're done.

Speaker A
Okay.

Speaker B
What that basically does is it will just block the thread until you are done.

Speaker A
That's what I was saying. Use GCD too.

Speaker B
Do you have GCD available to you do have GCD. I'm giving out. Not as. Good. Because GCD is built on some specific BSD component that I forget the name of. It does better on iOS and Mac platforms.

Speaker A
Okay.

Speaker B
Very Darwin core thing. But you do have GCD and it does work.

Speaker A
Okay.

Speaker B
Yeah. So that's how my network client works is it calls into URL session and then just blocks it some before until it's done.

Speaker A
Yeah. Okay, cool. That makes sense.

Speaker B
Yeah.

Speaker A
So are there any other interesting things about Vapor? About the Swift on the server ecosystem that you want to mention?

Speaker B
Yeah, I would just say if you want to get into it, I recommend having a blast. But you just need to serve on patients because Stacker philanthropy is limited. The help, the people in Slack are helpful, but they have lives. They're trying to lose their lives. And your question may not get answered. You're going to have to hack on stuff. You're going to have to since you don't have types that you can option click on and find out what you're looking at, you're going to have to print a lot.

Speaker A
Okay.

Speaker B
I don't think you have breakpoints. I don't really know if there's any way to make the breakpoint thing work. There's a lot of stuff that you kind of feel like you're back to the stone Age. You just have to be patient and work with it and be thoughtful while you're debugging and get through it.

Speaker A
Okay.

Speaker B
I know that is a real pain in the ass.

Speaker A
That's absolutely true. Where are you deploying this?

Speaker B
So that's another really interesting question. I tried to do like an EC Two thing so that I wouldn't have to set up multiple environments on all my computers. I could just SSH into edit and then get commit right from there.

Speaker A
Do it live.

Speaker B
Yeah, do it live, exactly. Well, yeah, that was like environment and there was like a separate production that ended up being terrible. So I picked up Docker, and Docker is actually super easy to use. I thought it was a whole new tool I would have used, but it's actually really straightforward.

Speaker A
Okay.

Speaker B
So I'm using Docker to run locally on my computer and then eventually I think Heroku will probably be the simplest thing to deploy on.

Speaker A
Okay, yeah. Cool.

Speaker B
Yeah.

Speaker A
So that's I think, pretty much all that I have to ask you about. That's everything that has come to mind. And since we have a live studio audience here with us, we thought we might do Q and A. If anyone here has questions about Swift.

Speaker B
On the server, if you're curious, if you think about trying it and you want to know how some part of it works or something that didn't make much sense, come forward, ask questions, and I'll try to answer it. Hey, I'm Mike Libertor. You mentioned before that you can't really use Xcode for this. What are you using? And can you go into a little bit of detail of why you can't use Xcode for this project? So the Xcode thing, this may be tractable problem, I'm not 100% sure, but basically when I tried to create an Xcode project with all the files that I needed to make the thing work, vapor gives you really nice tool. They have like a toolbox mandling tool. You can do like vapor Xcode, and it will automatically create that Xcode project for you, which is great. So you double click on that and open it. And when you go to build it'll, go to build a thing. And I guess one of the configurations is wrong. Or when you installed that particular version of Swift for that particular directory in Docker, you installed Linux version. So when it goes to build, it goes and tries to find a specific library. I think it was I don't remember which library it was and I can't remember if it was looking for the Mac one and couldn't find it because the Linux one was installed or looking for the linux one and couldn't find it because now it was in a Mac environment instead of a Linux environment.

Speaker A
That definitely seems like something that could be fixed.

Speaker B
Yeah, and my git repo is just the code, so I think that I could make a separate version outside of the docker folder directory on my computer, install the necessary dependencies there and run it straight from there. And then from that, then I would have all the libraries I need. To run the thing and build the thing in Xcode and do the testing xcode and everything. The problem there is one I haven't built in enough to know if that's impossible. And two, as I develop and as I like, I'll be like write code, write tests just to check my stuff works. And then when I go to run it, it works, and then when I go to put it on Linux, then certainly then at that point certain libraries might not be there or certain parts of foundation might not be there and it will like fatal error. So that's the reason that I can't use Xcode. If one of our listeners does know about this and has done this in the past. Definitely I will hear about that. And then as for what I am using basically text me. That's what I do all my node stuff in. So I'm comfortable like writing server code there. It feels like a natural home for that. And then to build and test, just this command line, basically. Build and tests are pretty slow. So like a cold. So if you if you do a clean that actually blows. Away your dependencies folder. And so you have to refresh everything. That takes about ten to 15 minutes to actually do a cold build, an incremental build, which is not as fast as an expert incremental build that just like doesn't fetch those dependencies will take maybe 15 to 20 seconds. So the loop of write code compile it, test it is pretty slow. And then testing is roughly in the same boat. The vapor has commands for both vapor. Build and vapor test. And they just call into the specific swift commands. Like, you could write swift tests, you could write swift build, and it will do pretty much the same thing. And the test command takes about the same. About 15 minutes to build everything and then the running of the test is really fast, but it's just getting everything together before you can before you can run it.

Speaker A
One of the things that you mentioned is Docker. Do you want to give a brief overview of what Docker does?

Speaker B
Yeah. Do you know more about Docker than me? I don't know because I don't know much about Docker.

Speaker A
Neither do I.

Speaker B
But my understanding is that it's like a configuration system for a virtual machine. It's like a template for a virtual machine. So you write this thing and then you tell docker to run this thing. And regardless of whether you're running on Linux, on Macro, Windows or whatever, it will set up everything so that you have postgres, so that you have Swift, so that you have playing, so that you have vapor, all your little sub dependencies and all your little subservices. You can put them all one place and tell it to set them all up, and it will set everything up and have a running instance for you.

Speaker A
And I would note that it's like, it runs it in not a full blown virtual machine, but some sort of container at least like the kernel and maybe some other stuff is shared between your containers and the host. And so that makes it a lot a little bit faster. There's a good diagram of exactly what is shared on the docker website and how it differs from a full blown VM.

Speaker B
Right, I read that too, but I don't understand how I could be running an Ubuntu. It is definitely Ubuntu, but also it's still using my Mac kernel. I don't really get how that works, but whatever wizardry it is, it's working.

Speaker A
One of us is definitely wrong.

Speaker B
No, I've heard that. You're definitely right. It's in there. I just have no idea how it works. But it's definitely widget. So they're doing some kind of some.

Speaker A
Kind of magic, really informative podcast. Yeah.

Speaker B
Any other questions?

Speaker A
Hey, it's Matt. Quick question. I think I remember there being a Swift on the server WWDC talk last year. Have you watched that? Was there anything useful in there or has that affected what you're doing at all?

Speaker B
I remember watching that talk because I was super interested in it, but it was a while ago and now that I've learned so much other stuff, I don't remember learning anything specifically in that that was like, oh, this makes more sense now. It is pretty much what it is on the tin. But it's also possible that I've read so many blog posts and stuff after that, that information ended up being not as useful. I've read it, I just don't remember. I've seen the talks. I just don't remember there being that much useful stuff in there.

Speaker A
Hey, M Tamar. Question. Speaking of Swift on the server, do you think teams should aspire to be language specific rather than platform specific. So do you think teams should organize around a language that they use rather than working on client back end iOS Android?

Speaker B
I think that's actually a good question for both.

Speaker A
So I think my answer here is a bit influenced by the Times, which is a larger organization, right. We tend to organize around individual product teams and where product teams are generally supported by shared, like a few different server and service teams that we all communicate with. And so I don't know, at least for a large organization, I don't know if organizing people by language makes a lot of sense since, I don't know, I think it does work fairly well to have like to still divide things up by some idea of like, products. And maybe if you're a company that makes one, like one product that happens to have a website and mobile apps, then the answer may be a little bit different. But I haven't thought about that and that's not like the world that I've been living in for the past couple of years.

Speaker B
Yeah, it's a super interesting question. One answer is that regardless of the language, there's still a lot to learn from the platform itself. So you can imagine a lot of people that's from our iOS developers we could write Mac apps, but there would be a lot to learn. There's a ton of stuff in app kit, there's a ton of different considerations on that platform that we just don't have to think about on iOS. And of course considerations, we have an iOS that just don't end up mattering in app kit. So I think it's kind of a similar thing there where you're still going to have to learn all the platforms and all the vapor stuff and what the limitations are on Linux and all of that. But that being said, I think it's all upside if you organize your team, like Chris was saying in terms of product teams and you have a lot of services for your API layer, having the ability to say, well, our team is actually just going to make our service in Swift is just much better than your client. Team can access that code and tweak it as needed. So the ability to have this thing, no matter how you're set up, if you're just one developer and you are writing both a client and a server, seems like we have a little bit of a win there. And like other contexts and other ways you structure your team, it just gives you more options. And I think those options in a lot of cases are really good, especially for iOS developers.

Speaker A
There's a good point that whatever you're doing, you're going to be learning not just a language, but whatever frameworks and libraries that you need to know. You want to be familiar with at least a little bit with the domain of whatever your product is doing. And if you zoom out enough on. That the specific language is almost kind of an implementation detail. I don't know if it makes sense to organize to actually put organizational structure in place around that so much as like, whatever happens to be meaningful to your organization, if that makes sense.

Speaker B
Right, but I do think if your organization does choose to make switch services, it's just a total boom for certain developers. Like the people listen to this podcast and like the people in this room because now you can mess around with more stuff.

Speaker A
Hey, I'm Josh. So I was wondering if you something that excites me about Swift on the server is being able to share code between the two or find some ways you can optimize that. Have you identified anything yet? Like maybe models or things that you can share between both back end, front end and have some time savings and that's a really good question for sure.

Speaker B
I've been thinking about this a lot since before I was writing server stuff, which was five days ago roughly. And my feeling on it is that your database representations on the server and you're basically like persistent representation, maybe that's core data or realm or that's coding or whatever on the client are going to be wildly different. Like you're probably not going to run a postgres server on your client so that you can reuse the same code that you get to use on your server. They kind of have to mirror each other in some ways.

Speaker A
You made the same model objects in memory though, right?

Speaker B
But there's functions that you attach they do, but the functions that you attach to those and the abilities that they're going to have. So in vapor's case, your models will have to conform to protocol and maybe you could do that across some kind of model boundary.

Speaker A
Could you add that protocol conformance right. In a separate non shared module?

Speaker B
Right? Yeah, that's what I'm thinking. It's like you have your shared model module and then you have your web app domain module and that thing would have all of your like that would have that conformance in there. But there's still implementations that kind of leak out. Like for the vapor, it's called model is the name of the protocol. You have to have a variable called exists that returns true for it to have some kind of implementation detail thing that they need. I think it's for soft deleting or something like that. So you could do a computer property that just always returns true. But really you probably want that to be on the original thing so that if you ever do need to mutate it so that implementation will link up to your shared module. My thinking on this is though, that even on the client there are many different representations that you're going to need. You're going to need JSON representation, you're going to need coding or core data representation. You might need certain presentable representations, different stuff like that. And my thinking is that the right way to do this is to make each of your models a protocol and then have source iterate through all those protocols and iterate through their properties and generate every type that you need. So if you need something for postgres on the server, done, generated. If you need something for JSON on the client, generated. And at that point, with the sort of annotations or whatever annotation method you have, you can say the JSON key for this. Like, let's say it's ID or whatever in JSON, maybe lowercase ID and your app would be capital ID. You can make sure that those always match because they will be generated for the same thing. So that part would be really nice. And another related thing that I think is worth talking about is that we are trying to mono repo thing with this project.

Speaker A
Oh, cool.

Speaker B
API goes in one folder, iOS is in another folder, and they're both in the same repo. And so if we do want to do code gender, we do want to do anything that we're trying to set up to do, you're set up really well for that.

Speaker A
I'm really curious to hear on that goes, because that is something that I think makes sense. And I've never actually convinced any company that I'm working for to do it, but I feel like it's really interesting.

Speaker B
Yeah, we haven't been doing it for long enough for it to make sense or for it to have any benefit. There's not really much cross talk between the API and client at this point, but I expect there will be.

Speaker A
Maybe we'll cover this in season three.

Speaker B
There you go.

Speaker A
Okay, well, unless you had anything else to cover, sirish, I think that pretty much wraps it up.

Speaker B
Yeah, no, that's it for me.

Speaker A
All right, well, again, thank you so much to all of you who support us on Patreon. It really means a lot to us. And you're making fatal error possible.

Speaker B
We had a great season two, and we're really excited to get back to you for season three.

Speaker A
And if my math is right, that will be July 6.

Speaker B
July 6. So talk to you soon. Bye.

