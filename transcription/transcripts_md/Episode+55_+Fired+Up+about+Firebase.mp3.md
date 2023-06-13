Speaker A
Any bread updates?

Speaker B
I don't have any bread updates. I know that several of our listeners are are eager to hear bread updates. I guess I do have bread updates, actually, since we talked on the podcast. And then a number of our other listeners are like, please do not talk about bread.

Speaker A
But the bread is very divisive.

Speaker B
I'm very pro bread, personally, so as as you know but our listeners do not know. After we recorded that last podcast, I baked several more loaves of bread, and you helped me with that. I was, like, texting you and FaceTiming you so you could see what my bread looked like. And you gave me some advice, and I think I ended with a pretty good loaf. It I it still didn't rise, I think, as much as it it should have or as much as, like, would have made me happy. But it tasted good, and it was a pretty good, like it was pretty good bread, I thought.

Speaker A
Yeah. The getting the rise to be really, really great is tough. I'm noticing that it depends on a lot of factors, but as long as it tastes good and you're eating it.

Speaker B
Yeah, it wasn't like it didn't rise and it was fine. So I ended up making a bunch of changes from the Times recipe to the point where the ingredients are the same, but the amounts of ingredients and the way that they're prepared and the length of time they're cooked is just not what the recipe.

Speaker A
So you just totally did your own thing.

Speaker B
I mean, I evolved my own thing from the Times recipe as a starting point.

Speaker A
Nice.

Speaker B
But yeah, I ended with a process that doesn't involve so many flour covered towels because things kept sticking. It involves parchment paper now and cornmeal and like, a very different fermentation and what's the second part? Proofing.

Speaker A
Yeah. Fermentation and proofing.

Speaker B
Yeah, like, different times and temperatures for those. I came up with methods of roughly controlling the temperatures for those via putting things on the top of my stove, all the oven preheats, and putting things closer or further from heating vents in my apartment. And I had thermometers involved. It turned into a whole thing.

Speaker A
You can really get obsessed with bread. That's part of why I like it. It's like four ingredients. Not that much effort on your part, but does take a lot of time and you can just go really deep on it.

Speaker B
Yeah. So at one of these weekends when I have a little free time, I should try again. And then you were suggesting maybe branch out into dough that actually requires kneading and things like that.

Speaker A
Right.

Speaker B
And that may help me get a little bit more of a rise.

Speaker A
It's not clear to me how important kneading is. Yeah. Because you can make no need bread, and it's pretty good. And I make a no need for kasha where you just kind of mix the ingredients put it in the fridge for two days and then pull it out and it just like it has had enough time to do its magic. I will put the no need for casual recipe in the show notes. It came out pretty good just considering I just left in the fridge for two days and then ate it. Can you put a picture of your bread?

Speaker B
I can put a picture of my bread and I can post somewhere the recipe or the process that I ended up following to achieve that bread.

Speaker A
Nice.

Speaker B
If that would be interesting.

Speaker A
Yeah, you might as well like, worst case, just put it in Gist and put it in the show notes in case people want to see it.

Speaker B
I think that'll be what I do.

Speaker A
Because while there are people that don't like the bread stuff, there are people that do like the bread stuff and some for everyone. That's right.

Speaker B
We got bread firebase. Oh, also exciting week last week. I guess this is not bread related, but we officially launched a startup, which is cool.

Speaker A
Cool. What is your startup called?

Speaker B
It's called Census, which is spelled C-E-N-S-Y-S census. Yeah. And it's named that because that kind of reminds you of taking an inventory or a survey of everything that's connected to the internet. All the systems right, connected to the internet system.

Speaker A
I like that. Okay, so this is the group that you're working with at the university, spun out their research as a startup.

Speaker B
Yes.

Speaker A
So do you work for this startup yet?

Speaker B
So I'm currently a university employee, most of whose time is going to start the startup project as part of the tech transfer process by which things get spin out of the university. Nice. I will at some point in the next several months end up officially working for the startup.

Speaker A
Very cool.

Speaker B
Yeah.

Speaker A
We could talk quite a bit about this.

Speaker B
We could I don't know how much is actually I don't have a whole lot of interesting software stuff to talk about, but I'm sure you could ask questions and we'd come up with interesting things or I'm curious about Firebase too, like it's something that I really haven't worked with very much.

Speaker A
Yeah. How about we do this? As you do more and more stuff with this startup, we can talk about it over the next coming months and you can tell me what that's kind of been like.

Speaker B
Okay, yeah.

Speaker A
Sweet.

Speaker B
Yeah, that sounds good.

Speaker A
Cool. A couple of months ago we talked about you, I think it was the grab bag episode, which was patreon only. You talked about writing what was called like an Amazon lambda, which is like a node JS function that your Alexa can trigger, basically.

Speaker B
Oh, yeah.

Speaker A
And you get to install your own node modules and then kind of work from there. Firebase functions are a lot like that, but they are listeners for when Firebase data changes okay, so Firebase is Google's.

Speaker B
Sort of like, I don't know, Parse follow up if you remember Parse, where you store data in the cloud and it's kind of your app's back end as a service. Right.

Speaker A
Although Parse went to Facebook, right. Digital Balkanization of all of our services here.

Speaker B
Yeah.

Speaker A
So Firebase is a number of services. It's. Google analytics got rebranded as Firebase. It's a real time database which is just a big JSON dictionary where you can just store stuff and then other apps can listen to it in real time and as they change.

Speaker B
Okay, I was going to say, what's a real time database and how does that differ from an imaginary time database?

Speaker A
The idea is basically as things change, you get notifications and you get the fresh data as it updates.

Speaker B
Okay.

Speaker A
Yeah.

Speaker B
So these Firebase functions let you do things with that data as new data appears on the server.

Speaker A
Exactly. So you can basically write this firebase function and then you can say sort of database and then you describe the path that you want and then you do like on write and then that's an event that you can then handle. And that event gives you access to all the data that just changed and lets you do interesting things. So one of my clients has stuff in Firebase, and then when this report reporting system and so when a report gets updated or created, I have to generate a PDF. That sounds pretty tough and I wasn't really sure how it was going to work, but it actually ends up being pretty straightforward. You kind of listen for this event and then there's a bunch of node modules that you can get through NPM and whatever your favorite package manager is. And from that you can generate a PDF and then that PDF then goes back up into another part of Firebase, which is called Firebase storage, which is kind of like s three. So that's basically what I spent the last week or so doing.

Speaker B
Okay, cool.

Speaker A
Yeah.

Speaker B
So you now have a system that lets you produce PDFs on the server side when data shows up in Firebase?

Speaker A
Yes, exactly.

Speaker B
All right.

Speaker A
Yeah.

Speaker B
Nice.

Speaker A
Pretty dope. Pdfing is real weird.

Speaker B
I totally believe that. How so?

Speaker A
It's like everything is absolutely positioned, which is kind of annoying, and then it's really hard to do really interesting layouts. Depending on which node module you use, it will handle some of that stuff for you. So the one I'm using kind of has this concept of like where you're laying text out and will kind of update that as you add text. And it gives you the ability to do columns and stuff too, which is nice, but it doesn't handle Pagination automatically. So you have to size the text and then create your own page breaks. It's very weird and not cool. Fortunately, we don't have any data that needs to worry about Pagination, but you can just create arbitrary new pages, which is nice. Yeah. PDF, it's a hideous world out there. There are some modules that I think we will switch to eventually, which will let you take an HTML page, render it in something like Phantom JS, like a headless browser, and then render that into a PDF and then just we'd be able to provide that to the user.

Speaker B
That sounds crazy.

Speaker A
Yeah, but that's the beauty of Node. There's a package for everything.

Speaker B
Yeah, I guess that's true. Okay, so you have code that manual lays out code and measures and paginates and everything. That sounds like a lot. What was your experience working with Firebase? So. I've never worked with firebase functions. You've never worked with an Amazon Lambda, but what was your I mean, maybe given our previous discussion of writing the Echo skill within Amazon Lambda, how do you think the Firebase function compares and what's the deployment process like?

Speaker A
Yeah, clone is a very harsh term, but they're very similar, I think. So the deployment process is you basically install a command line tool and then you log into Firebase using that command line tool, and then you just type like Firebase deploy. And that's it when you're in the right folder on your desktop.

Speaker B
Nice.

Speaker A
Yeah. And it handles basically it checks everything for you in terms of does everything, like, does the syntax all look right? But I don't know if there's a way to actually test the code without deploying it. And so I've done a lot of deploys over the last few days trying to get this stuff to work.

Speaker B
I found for Lambda, I found this just random node package, but that puts just enough sort of machinery around it to mock out the environment that it runs on in the AWS cloud. And that's really useful for testing. I'd be shocked if something similar didn't exist for Firebase.

Speaker A
Yeah, I think you're right. I just haven't gone looking for it. But that's probably a good next step.

Speaker B
And I don't think that this is like an official package or something that's officially supported. I think it's just something that someone put together that I guess that running one of these functions or one of these little applications takes very little in the way of, like, infrastructure surrounding it.

Speaker A
Right. Because it's just one function, essentially, that gets called.

Speaker B
Right, yeah.

Speaker A
One interesting question that kind of came up. I mean, one thing that came up is that I still hate JavaScript. I'm writing es six. I think it's horrible. Yeah, it's good. Function syntax is really ugly. If you want to make just a function that just takes void and returns void, it's like open paren, closed paren, and then like a hash rocket, like an equal sign and then an arrow and then braces, and inside the braces go your function. So it's like a bunch of extra pointless characters that something like Swift just doesn't have. Right. With Swift, you just have the two braces and you're done that's the whole function?

Speaker B
Yeah. I think that's kind of clumsy. Have you looked at all at using any of the Es Seven to Es Six?

Speaker A
Oh, my God, I'm so behind already. This is the JavaScript feeling.

Speaker B
Es Seven is a version that brings like async await. Right. Am I making this up?

Speaker A
No, that's correct. And you can get it using something called babel, right?

Speaker B
Yeah, this is definitely es seven. So there are tools that will take Es Seven and compile it down to something that can be run in AW in a lambda or with node Six, right?

Speaker A
Yeah.

Speaker B
I started down this path with my Amazon Echo skill and quickly realized I don't understand how to set up this tool chain. And for this stupid little project, it's just not worth it. I'll just write boring JavaScript without async await.

Speaker A
Yeah, I think that's probably the best thing. I'm looking at the Es Seven stuff now. It doesn't look like anything I have to have Async Await, which is kind of nice and actually would make some of this code a little cleaner. They add observables. They add, like, nice abilities to merge objects and destructure them and stuff. I don't really care about that. Async Await would make this code much nicer.

Speaker B
So what I ended up doing was using promises in some places rather than Async Await.

Speaker A
Yeah, I'm definitely leaning heavily on promises.

Speaker B
Yeah, I mean, that's not great, but it's fine. Cool.

Speaker A
One other thing that I noticed here is now, for this client, I've done an iOS app, I've done an Android app. We have someone working on a Web app, and we also have this PDF thing. So that's like, four different platforms that this report needs to be rendered in, like, four different clients for this one set of data. So we end up duplicating a lot of the logic around displaying a report. So one of the things we do is we provide summary statistics. So how many of the components of this report have this kind of condition? How many things have safety hazards? Even simple stuff like a report is made up of a bunch of images. So you need to have some logic that's like, okay, well, if the number of images is one, then write one image, but if it's any other number, write N images. Right. The pluralization code. And so in iOS, you can kind of use, like, Nslooklife string, but then Android has its own thing, and then Web has its own thing. And then this PDF generator in a dream world would use the same rendering code as the Web and then PDF that so that I could actually knock out one platform that way. But at this point, I have four different places where all this logic is implemented multiple times and no real clear way to deduplicate it, really. So I have a couple of options, right? One option is when you create the report, I could run through and generate all of the associated display data and store it in the database and then everybody would have access to it. Another option that I have is I could create like a report type in JavaScript and then every platform would just run. It would like hydrate a report with the report data, and then you would have access to these read only properties that would be computed and would have all this display data. That's the second option. I don't really see any other approach. Yeah, I mean, for something that needs to work for this PDF render and web, which are both JavaScript and iOS, which is objective C, and Android, which is which is kotlin, isn't that interesting? And it's like not that much code, so it's not horrible, but it's also not great.

Speaker B
Yeah, no, that's not there must be a better solution here. I think I may have to go back and relisten to this conversation and think about it for a little while too.

Speaker A
Yeah, if you have any insight, I'd be over there because obviously the logic is really simple, but it's glaringly duplicated and there's a lot of it. So some reports have the email of the person who assessed the report, but some don't. So you want to display like email, not set, like you want a nice string for that. But the ones that do, obviously you can use a string. So that's like one bit of logic that's duplicated four times. Then there's like pluralization logic four times. Date math is another one. So the dates in the database are stored as seconds from the Unix epic, but we need to convert that into something human readable, basically.

Speaker B
And doing that in a localized way is platform dependent.

Speaker A
Well, unless we use JavaScript, which has locale sensitive date generation that we could tap into. Yeah, but yeah, it's using date formatter on Android, NS date formatter on iOS, and then what's the thing in JavaScript? It's two locale date string to which you can pass a bunch of options.

Speaker B
So I wonder if I'm understanding you so far. The problem is that you have the data. I assume there's some sort of data structure that underlies one of these reports. Yeah, it's available on each platform, but the rendering and specifically rendering in a device and platform and locale aware way is really duplicated.

Speaker A
I'm less worried about locale for now. I will have to worry about locale eventually, but if I could just deduplicate it without considering myself a locale, I would do that.

Speaker B
So the thing that is coming to mind, which I'm a little bit nervous to even suggest this, but something like react native, that may provide you with a way to write some platform independent code that handles some of the formatting and all that jazz and still can render out to native views. Because I know that react native isn't quite like a write once run everywhere solution, but it would allow you to share a lot more of the sort of business logic and probably formatting logic. And I know that they do have sort of platform independent shims in place for at least some of this stuff. So that is a JavaScript related solution. True. But it might be something to look at. And even on the server side, if you move to a phantom JS based PDF generation system, then obviously generating a page with React native and then rendering that to PDF would be plausible.

Speaker A
Yeah. So I'm definitely not opposed to using JavaScript everywhere because that is the one language that will work in every situation.

Speaker B
Yeah, well, so you got Swift on the server, you can do Swift interop on Android.

Speaker A
Well, yeah, and then like render Swift into ASM and then run that in the browser. Nailed it.

Speaker B
Yeah, no, that's true.

Speaker A
No, just JavaScript I think is the right answer if I really do want to deduplicate this logic. Our web version is React, so that's a point in the React columns favor.

Speaker B
Okay, so you could see how much of that could be reused on iOS and Android.

Speaker A
Well, see, that's the thing. I don't think React native and React can use the same components, but I think you can like they can use the same JavaScript objects.

Speaker B
Yeah, they surely can use the same sort of model and the same sort of things that process your model into something that is closer to DUI.

Speaker A
Yeah. And then how would I structure that? Would that be like its own git repo? That would be like a sub module of all the other ones. Or mono repo.

Speaker B
I mean, I'm always going to go full mono repo and say that this should be a mono repo, but barring that, well, it needs to be open.

Speaker A
Sourced at some point. So there is some sensitivity to exactly how it's structured. It's not just like whatever I feel like, but it's not impossible to do on a repo.

Speaker B
Yeah. Or get sub modules that are painful to work with but like a plausible solution here.

Speaker A
Yeah. Or maybe a node module somehow.

Speaker B
Yeah. And that could still be like you'd probably still include that with a sub module, right?

Speaker A
Well, no, you would like NPM install it.

Speaker B
Yeah, that could work. The considerations to weigh there are the same as having an internal Cocoa pod or a Carthage package versus just having a bunch of code that you include in your project via sub module.

Speaker A
Yeah.

Speaker B
You have maybe a little bit more structure and process around it and it's a little bit more self contained. And the trade off is wait, what's the trade off?

Speaker A
Well, the trade off is that I end up with this.

Speaker B
Yeah. This internal I guess them having more process around it is the trade off.

Speaker A
Right. So if you want to change something about how the iOS app is rendered, you end up having to install Gulp or whatever. So I have this really creakily constructed network of dependencies. It would be weird and it's like, is that really worth it to deduplicate simple logic? Like, I have one image here and two images there.

Speaker B
Yeah, I wonder. Although, as this gets more complex, you probably will want some way to describe, to describe these really like business rules to model them in a way that's platform independent.

Speaker A
I could use a lot more the other option that we talked about, I could use a lot more database storage for it.

Speaker B
How so?

Speaker A
Right, so let's say you upload a report and then when that happens, I would also generate at that time all the little strings that you need and then just save that into the database so that when you read the database, you can just read those strings. Now, to do that in a locale sensitive way, you have to save it multiple times, once for each language.

Speaker B
Yeah, I'm not sure that that's a great solution.

Speaker A
Yeah. But like is yeah, it's not a.

Speaker B
Great given a choice between like, tightly coupling your database to how these things are formatted and just duplicating simple formatting code, I would definitely go with duplicating simple formatting code.

Speaker A
Right. And it's so simple as the thing, but there's a lot of it. So I just had to rewrite it for the third time and I know somebody else has written the fourth time and it's like they're each one in a different language and it's kind of silly. I think there was supposed to be some kind of dream where you could download an object.

Speaker B
Like some kind of what?

Speaker A
When small talk was being invented or whatever, it was kind of supposed to be the way that, like, you could just say, I need access to this, like, object. And yeah, you would just it would just come down with its behavior. Like, it would come down from the network with its behavior and its data together.

Speaker B
Yeah.

Speaker A
And that would be a cool solution to this. But that doesn't really exist. But then maybe you could download the JavaScript class.

Speaker B
Right. I think that something JavaScript de react nativey is probably the closest you're going to get to that today.

Speaker A
Yeah.

Speaker B
And I think we'd be remiss right. If we didn't give a shout out to I think the concurrency manifesto where Chris Lattner outlined some far, far future dreams of the things that Swift could enable with some of the concurrency principles and primitives that he outlined. When one of those was distributed objects in a much more transparent way that actually worked and took care of a lot of the remote procedure. Call sort of machinery around accessing stuff over the network like this. And obviously you can't use this today. And it's unclear exactly how much it would help, but that small talk dream of just breaking down these boundaries is still alive.

Speaker A
Yeah, that's an interesting idea, because what I could do with that is I guess the report object would just live somewhere else, and I wouldn't care where it lived. And they could all talk to the same server that would tell it how to render a report.

Speaker B
Yeah, there are a bunch of stupid requirements here. Like what happens if the user on a slow network, right. Or is on the subway with no Internet connection?

Speaker A
Right? That would be bad. And the other thing is, as swift, quote unquote, takes over the world or whatever, having it be runnable in more places could mean that I could just run this swift code on Android, and I could run the swift. Code in the iOS app. And then I could also kind of either transpile or fully compile the Swift code into JavaScript or ASM and have it just run in the browser as well.

Speaker B
By ASM you mean web ASM, of course. Right?

Speaker A
Yeah. Is it ASM JS is not the.

Speaker B
Maybe I'm pretty out of the loop here. I don't know.

Speaker A
Yeah. Web ASM. I think ASM JS and web ASM are maybe the same thing. Maybe interchangeable, maybe not.

Speaker B
Maybe Asmj on Asmjs implements a WebAssembly.

Speaker A
Is faster than ASM JS, I think.

Speaker B
Is WebAssembly maybe like native support and Asmjs is a library.

Speaker A
Yeah, that makes sense. The link in the show notes also put it in my instant paper so that I can read it.

Speaker B
Sounds great.

Speaker A
Yeah.

Speaker B
I think that's all I've got for you. I mean, it definitely sounds like you have a problem here. I think that something you find some way to share some of this stuff. If it's really this much of a pain point, that may well be some sort of JavaScript based thing, even if it's not react native. Maybe it's just JavaScript that you interact with through JavaScript core or something like that.

Speaker A
That's also a definite possibility. The other thing is it's not really clear how much this code will change. Definitely it'll change when localization comes into play and it'll have to change on four platforms four different times. That'll be really bad. Other than that, I guess the model will change a little bit. I think we're hoping to do a 2.0 with like a slightly different model, so it may change there as well. Maybe that's the time that I would like rewrite everything to be in some kind of base JavaScript state. And then the other thing, somebody has to pick this up after I'm done with it. I hope to work on this project for a long time, but if I don't, I can't leave it with this crazy build process.

Speaker B
Right? It has to be something understandable and well documented.

Speaker A
Yeah, exactly.

Speaker B
Can I leave you with a couple of teasers about things that we could talk about that are startup related?

Speaker A
Yes, I would love to.

Speaker B
Future teasers. So what we're doing, let me just describe what we're doing and some of the engineering problems should present themselves pretty quickly. And I should also give a disclaimer here that none of this is really my original work. This is stuff that people in this research group have been working on for the past several years, since like 2014. I've come in relatively recently to try to improve the service and the code that runs all this. What we're doing is it's an internet wide scanning project on a bunch of different protocols we connect to or we scan and try a handshake at the application level to every IPV four address, so 4.2 billion addresses. We scan all these protocols at least once a week. The common protocols will do once a day. While we're doing this, we'll do a handshake and do like an Https handshake. Do the beginning part of an SSH handshake important to call out that we don't try to guess passwords or anything like that. So at the point where the server asks us for a password, we just drop the connection. That seems obvious, but it's important to call that out. And we gather all of this data and make it searchable via a web interface where you can enter, do full text searches, search for specific things in specific fields. Maybe you're interested in looking just for all Https servers that are presenting certificates that use a specific public key. You can answer that. And we also have some other data sources. So in addition to collecting just everything that we can see via scans on a whole bunch of protocols and we're working on adding more protocols constantly, we gather all the SSL certificates that we see from scans as well as from something called certificate transparency logs and we can put some reading on that into the show notes. And I mean, as you know, Https is getting more popular and so we are adding now several hundred million certificates every year to our database and that's just going to continue to keep growing. So a lot of really interesting and really fun to work on engineering problems just related to, first of all, managing a data pipeline where we take all this scan data and process it and put it in database and make it all available for full text searching and distributing this data to other researchers who are using this data for academic research. It's cool stuff. It really is.

Speaker A
That is pretty crazy. So the idea is then if you want access to this giant database, you pay the startup and that's how the startup makes money.

Speaker B
Yes, exactly. So our initial product here is this. So like several years ago, the students in this group put together a pretty simple web interface to let them query this data just because it was useful for research, right? It turns out that that's useful not just for researchers, but for people who are interested in seeing what is exposed on their network that they're defending or. People who are maybe looking at malware and want to discover things about whatever servers malware they see, malware connecting to all kinds of uses like that. And so we have this website now which is available for for commercial use. There there's a free account level with some, you know, that has that has a pretty strict quota on it. And if you want to do more searches every month, you can pay the startup money and query to your heart's content.

Speaker A
Pretty nuts.

Speaker B
Yeah.

Speaker A
I think we're going to have a lot of cool stuff to talk about with this with all these new things you're working on.

Speaker B
Yeah, I think so. This is really different from iOS development, but I'm really excited about it.

Speaker A
Are you still mostly doing Python?

Speaker B
Still mostly python. Yeah.

Speaker A
Nice. Cool. Well, we'll talk about it soon.

Speaker B
Yeah. I still don't really like Python that much.

Speaker A
Yeah. Got to say, it's also hard to find languages that you do like that one likes. You know what I mean?

Speaker B
Yeah, I was going to say, did you mean you like me specifically?

Speaker A
I don't want to presume to speak for you, but for me, I feel like every language is like a trade off in its own way.

Speaker B
Yeah, that's definitely true.

Speaker A
Yeah.

Speaker B
Okay.

Speaker A
Yeah. Sweet.

Speaker B
Well, that's what I've got.

Speaker A
We did it, Chris. We did another one.

Speaker B
Yeah. Always good to talk to you.

Speaker A
Yeah, talk to you soon. Bye.

