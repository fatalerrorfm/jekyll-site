Speaker A
Welcome to Fatal Error. I'm, Sirosh. Khanlou.

Speaker B
And I'm chris desombach recording a special.

Speaker A
Episode here from I'm at 360 IDEV in denver.

Speaker B
Yeah, how's the conference going?

Speaker A
Conference is pretty good. I gave the keynote today, which was really fun. I think it went pretty good. Pretty well. I think some of the talking that we it about it last week or however many weeks ago, that was about sort of like what I was going to talk about. Kind of nailed down some of the ideas a little better. So I do appreciate talking about it here. Yeah, it was nice.

Speaker B
Cool. Yeah, I'm glad that was helpful.

Speaker A
Today we were thinking about talking about the first apps that we ever made. I know I, in particular, have some really funny horror stories. The first app that I made, and Chris, I don't know much about the first apps that you've made, so I would love to hear about them, too.

Speaker B
Yeah, we definitely can dig into that. I don't know if I really have horror stories, but we'll see.

Speaker A
Well, so I wasn't really much of a developer before I started, so there was a lot of things that I didn't know. So when did you did you ever release an app, like, under your own name on the App Store?

Speaker B
Yeah, definitely. I've released a couple apps on my own name under the App Store at one point or another, mostly several years ago.

Speaker A
Now, at this point, what did they do?

Speaker B
So I think the first one I'm trying to remember the history here exactly, if I'm remembering right, the first one was a pretty simple app that let you check how many computers were open in U of M's, Engineering Computer Labs, u of M, University of Michigan, where I went to school and where I now work.

Speaker A
Interesting. How did you do that?

Speaker B
So there was a website that you could go to that showed you how many computers were being used in all of the college of Engineering's computer labs. It didn't work for all the computer labs on campus, only the ones that were like the engineering ones. But that was good enough. That was most of the computer labs on the engineering campus. And so on this website, I just looked at, how does this website work and where does it get its data, because I just got this iPhone thing, and it would be kind of cool to have this data on there in an app. And it was just some JSON files that the website was pulling and downloading, and that was open to everyone. So if I'm remembering right, this was a pretty simple app that just pulled down these JSON files or one JSON file I forget even how that was structured and put this stuff into a table view.

Speaker A
Wow. And what year was this? Do you remember?

Speaker B
So this is still on GitHub because everything is on GitHub. And if I scroll through the commit history here. Okay. Initial commit was on January 27, 2012.

Speaker A
Make sure to drop that into the show notes.

Speaker B
Okay. Yeah, we'll put this repo in the show notes. Yeah, man. I'm sure looking at this code, especially the older code, is going to be really interesting. So January 2012 was, I think, right when I was getting into iOS development. Previous to that, I was working part time at a startup in Ann Arbor during college and was doing Android work there. And the guy who was doing our iOS app, my friend Andrew here in Ann Arbor, started teaching me iOS as well so I could work on both the iOS and Android apps at work. And so I think this was a project to, I don't know, project to just help practice my iOS skills and do something fun. Something fun with these skills that would be useful for me.

Speaker A
Nice. That's a pretty good little project, because I remember, I think, especially when you're trying to figure out what could I make? People have a tough time coming up with good project ideas, and that's a really good one.

Speaker B
Yeah. It's hard to come up with a good first project idea, and I think it's critical to have one when you're starting something new. You're like, learning a new language, learning a new framework, learning to write an iOS app, learning to write an Android app. Right. Anything. I really think that you should be at least for me, it works best if I'm trying to get to some goal that I have in mind. And just coming up with a good goal is tricky.

Speaker A
Yeah, for sure. Interesting. And then what's the name of the project?

Speaker B
So the project is called Cane Lab Status, and I will throw a link in the show notes. Cane is an acronym that stands for Computer Aided Engineering Network, I think. And that's just the name of the engineering computer network that ran these labs.

Speaker A
Nice.

Speaker B
Yeah. So if you dig through the commit history here, you will see some of my really earliest iOS code. And this was also I mean, what version of iOS was out in January.

Speaker A
Of 2012 was, I think, iOS five.

Speaker B
Yeah, sounds right. This was definitely pre iOS seven. Yeah. And so if you dig through this commit history, it looks like I actually kept maintaining this for a year or two after I graduated, before I eventually got bored and was like, I'm not supporting this anymore.

Speaker A
What features did it have besides telling you how many computers were sort of in use?

Speaker B
I think that was pretty much the feature you could list. Computer labs. I don't even know if I have screenshots anywhere here. Okay. Yeah. The University of Michigan has two campuses that have engineering computer labs. Anyway, there's North Campus, which is where the engineering school is, along with art and architecture and music and some other I think that's most of what's up there, and central campus, where most of the other, like most of the other colleges are. And so the feature of this app is that you could filter whether you wanted to view all of the labs or just those on one of those campuses, because you're not going to take a bus between campuses to go find a computer. Right, right. And I think it showed you it might have even showed you which specific computers in a lab were open. I'd have to dig through the code, honestly, to remember what all this did. But yeah, if you dig through these commits, I'm sure you'll find some embarrassing.

Speaker A
Code and some well, these are some not bad stuff. I'm looking at the app delegate now. It's not terribly long, which is great. It does have a singleton data controller, which is great. And you prefix all of your categories. So for, like, UI color, if you added a color to it, you prefixed it. So it's really good hygiene.

Speaker B
My friend Andrew is one of the shout out to Andrew Sardone here in Ann Arbor. He taught me well.

Speaker A
Yeah. There you go. That's pretty cool. Yeah. I bet we could go through this stuff and find some really funny things.

Speaker B
If you go through the commit history and find well, I'll link to the initial commit in the show notes as well, because I'll bet I have to click through everything to get the initial commit again here. But I'll bet that the initial commit is maybe a little bit more a little bit less well polished.

Speaker A
Yeah. The GitHub doesn't let you just jump to the last page with the commits. You just have to keep saying older and older, which is kind of annoying.

Speaker B
No, it really doesn't.

Speaker A
Yeah, but it looks like you did quite a bit of work on this. Oh, no.

Speaker B
It looks like the initial commit is just the Xcode project template.

Speaker A
Nice.

Speaker B
I'm impressed with my get hygiene for being a college student.

Speaker A
Oh, man. All your classes have three letter prefixes, which I think even in 2012 was like that was pretty forward looking.

Speaker B
That's all credit to that is to Andrew, obviously, who got me iOS to start with.

Speaker A
And then your lab model has, like, a huge initializer in it with building room, human name, host, count, latitude, longitude. Oh, boy, those days were great.

Speaker B
Where's this? I got to get those Immutable models.

Speaker A
Are they immutable? Yeah, they are only yeah. That's funny. Nice. Really polished. First app, I would say, tells you.

Speaker B
Whether it has color printing there.

Speaker A
Yeah. Good. Shit. Has scanning you. Maybe you want to scan stuff.

Speaker B
That's right.

Speaker A
This is good stuff. This is really good.

Speaker B
I wonder if this even all still compiles. Probably because it's not Swift.

Speaker A
This is very funny. I found something very good in here.

Speaker B
What did I do?

Speaker A
So in DZC host info API client, you set up basically an API client, which like a base URL and you register your AF networking JSON, Operation Class, whatever. You register the default header type for Accept as Traffic, JSON as accept. And the last one is commented, I'm an asshole. And it's setting the user agent to pretend to be, which I assume was necessary for some kind of bug.

Speaker B
Yeah, that might have been necessary. I don't remember why I did that. If I look at blame, the commit message just says, Networking tweaks. See, that's not a very good commit message.

Speaker A
I think it's a great commit commit message. That's really funny.

Speaker B
No. Networking tweaks. Come on. A good commit message would include one Tweak and explain it well.

Speaker A
And a good comment would say why you needed this instead of just so.

Speaker B
That comment was apparently added in a different commit significantly later.

Speaker A
That's also very funny.

Speaker B
Like, almost a year after that code was written.

Speaker A
Nice.

Speaker B
There you go. So, yeah, this was, I think, my first iOS app. Now, obviously, as I've mentioned, I didn't come at this knowing nothing about iOS. I think, at this point, had been doing a little bit of iOS stuff at work for at least a few months before I did this, but I think this was the first app that was totally mine and that I submitted to the store. Like, there's a Bootstrap script in here. Uses cocoa pods.

Speaker A
Cocoa Pods is pretty good. That's a surprise. I wouldn't have necessarily expected you to use cocoa Pods even back in those days, given that everything else in this project is so clean.

Speaker B
I'm looking at commit messages here say, Remove the OD refresh control pod, because I got that was added in when iOS six. Right. The native iOS refresh control.

Speaker A
Yeah, that sounds right.

Speaker B
Yeah. So four years ago.

Speaker A
Blast from the past.

Speaker B
Yeah. So this will definitely throw this in the show notes, and everyone can feel free to critique my ancient code. Look at the there was something clever that I did in here. All right.

Speaker A
Really? Like clever code.

Speaker B
Look at CDZ, table view, split delegates.

Speaker A
Table view, split delegate. Is this like a multicast delegate?

Speaker B
For some reason? There's a good comment. Look at line two of this file, too.

Speaker A
Import objective C runtime. Shit just got real.

Speaker B
So for some reason, I wanted my Table View delegate and Scroll View delegate to be separate objects.

Speaker A
Right.

Speaker B
And I don't remember why that is, but this is like a mediator delegate object. So you could set your Table View delegate to wait, is that true? Yeah, I think that's true. Because UA table View delegate inherits from UI scroll view delegate. Right?

Speaker A
That's right.

Speaker B
Yeah.

Speaker A
Or inherits might not be the right word, but like yeah, that's right. Inherit for sure. Whatever it is, it does come down from it.

Speaker B
Yeah. So I forget why I wanted to do this, but I had forgotten about this until just now. But it was a cool metaprogramming trick.

Speaker A
Yeah, this is great. Runtime code. Super clean, very easy to read. Very nice, man.

Speaker B
Yeah. I'd forgotten about this. I don't remember what this is for. I'm realizing this is probably not super interesting for our listeners since it's literally just us commenting at code that we're looking at.

Speaker A
Yeah, but yeah, no, I think it's cool. And you also changed the prefix at that point, before it was DZC, and then for that one, it was CDZ.

Speaker B
Well, I wonder what that you know why that is?

Speaker A
No, I don't.

Speaker B
The other types in here are specific to this application, whereas this file could, in theory, be reused elsewhere.

Speaker A
I got you. That makes sense.

Speaker B
Other CDZ code bases.

Speaker A
Right. Nice. This is cool.

Speaker B
Yeah, especially for me. I haven't looked at this code in years.

Speaker A
Yeah, this is good. When this goes away, the CDZ or DZC lab status helper.

Speaker B
What's a helper.

Speaker A
What's a helper?

Speaker B
Oh, my God.

Speaker A
Yeah, it is a helper. It's fully a helper. Did you write tests for this code, Chris?

Speaker B
No, I don't think there's test for this.

Speaker A
This is perfect code to write tests for.

Speaker B
Yeah, absolutely. So the idea about to put this.

Speaker A
In the show notes as well so that people can know what we're talking about.

Speaker B
This will definitely go in the show notes. So if I'm remembering the yeah. Oh, this one actually has documentation right at the top, it says this lab status API that I was using doesn't report a status for every lab or every building. I think what that means, and if I'm remembering, vague memories are coming back to me. That meant that some of the labs came back with status, like whether it was open or closed, but not all of them did. So this class would take a lab model and check what building it's in and basically have the hours for that building hard coded in, including dealing with whether it's weekends I didn't get as, like, coding breaks and holidays into here, which I got to draw the line somewhere.

Speaker A
You hard code the Gregorian calendar in here, which would maybe be a bad thing, but this is designed to only be used in Michigan. You maybe would even want to actually hard code the time zone as well.

Speaker B
Yeah, that's true. Yeah. I think this maybe assumes that you're in Eastern. I think the assumption was if you're not on Michigan's campus, this app is probably not super useful to you anyway.

Speaker A
Right?

Speaker B
Yeah.

Speaker A
We have an interesting time zone bug with beacon right now where it's not really a bug. It's like a user interface enhancer that.

Speaker B
We want to do bug. It's a feature. It's working exactly as we wrote the code.

Speaker A
Well, it is working as intended. It's just people don't think about time zones before they make events. So we're using beacon here at 360 IDEV, and the people will make events from their local time zone. So somebody was in Central and made an event for a Donut Run, but they wanted to make it for 730 Mountain Time, but they made it at 730 Central Time, not realizing that the time zones would matter. And then when they got here, it was the wrong time. And so I think we need basically some code that says, hey, if you are not in the time zone that your events venue is in, then we should show you both. We should say your current time zone is this, and that's the time. And then in the time zone that you will be in when this event happens, the time will be this. So that you can adjust and you can see that, oh, there's a concern here. And I made the exact same mistake with my keynote. I made it for 09:30 A.m., but I made it for 09:30 A.m. Eastern Time, which is 730 here.

Speaker B
Yeah. So that's challenging because what happens if the offset between your time zone and the event time zone is different between now and when the event happens? For example, what if the event is in a state that doesn't observe Daylight Saving Time, like Indiana? But I schedule an event from Michigan, which apparently, little known fact, michigan is still in the Eastern Time zones, the same as New York and DC and everything. So what if I create an event in Indiana now for after Daylight Saving Time ends? Then that offset is different.

Speaker A
Right. That is really tough. I don't know if there's any APIs we can lean on for that. Well, that's interesting.

Speaker B
You just have to make sure that the date is correct that you're using for these calculations, too. Right. You can't just do number of hours offset. This seems like something you could solve just with better design. Basically, if you know the location where the event is going to be held, maybe you just only schedule it in local time for that day in that location. Right, right.

Speaker A
That could be right. And it probably would be right more often than it would be wrong. But I think still the best thing to do is tell the user exactly what's happening. If you've ever Google or Apple, I don't know how Google Maps does. I assume they do, but Apple Maps does do this. If you're driving from one time zone to another time zone, it will say, like so I drove from, I think from Vegas, which is in Pacific, to the Hoover Dam, which is like the bridge between the Mountain Time and Pacific Time. And then I went on beyond that to go to Zion National Park. And it said so you would basically be leaving Vegas at, let's say, noon, and then you'd be arriving at it would be an hour and a half drive, but you'd be arriving at Zion at like 1230, and it would say 1230. Comma MST so that you knew that you are also going to go over a time zone switch when you go to this place.

Speaker B
That's interesting. Yeah, I don't know if Google Maps does that, but I assume that anything Apple Maps does, Google Maps does. And probably better.

Speaker A
Probably is it better. I want to add in some basic time zone support here into the app, which would be nice to tell people, especially if it's going to be used for conferences. You're often traveling across time zones to get to conferences.

Speaker B
Yeah, I would just say really consider the design here. And if it were me, I think my first step would be to make the event time zone and date the primary part of this interface and just have maybe a little bit of text underneath that says, by the way, this time is going to be X in your time zone, right, in your current local time zone.

Speaker A
I wonder if there is support for getting the daylight savings time status at a specific date in a specific GPS location. Because there's that old thing about the United States observes daylight Savings time. Arizona does not observe it, but then the Navajo Nation does observe it, which is inside of Arizona, and then the Hopi Nation, which is inside the Navajo Nation, then it's flipped again. And so it's like this many levels nested thing of like, who supports daily savings time? So you can't really just say, well, if you're in Arizona, there's no daily savings time because it's still more complicated than that. So I wonder if there's some kind of like ICU or ICU equivalent thing.

Speaker B
There must be some way to do this. Yeah, I don't know.

Speaker A
Yeah, there's got to be. Or an API like worst case that you can hit and be like, given this GPS location, what time is it going to be there?

Speaker B
What's their offset going to be right on this day?

Speaker A
Yeah, so that'd be interesting thing I should look into. Daily saving time is actually something I had not considered at all when thinking about this feature.

Speaker B
Yeah. What conferences take? When do we switch in the US. Don't we switch back in October now?

Speaker A
It's October now. Yeah.

Speaker B
So that is the potential to affect what conference is it that at least was last year in Philly in the fall? Was that cocoa?

Speaker A
That was cocoa love. Yeah, but I think they're done now, so that's not going to be a thing anymore.

Speaker B
As long as there are no conferences in the fall or winter, then we just don't have to worry about DSP.

Speaker A
Well, the important scary part is the bridge. Like if it's right before daylight saving time, the conference is right after, and then that's the really scary part.

Speaker B
You just have to make sure you're doing your calculations with the date, not just calculating the time zone offset as it is right now.

Speaker A
Right? Yeah. So I will look into that for the future, but I think it'll be a nice little feature to have an app.

Speaker B
So what was your first app or first apps?

Speaker A
There were two apps I did as an indie before doing more like iOS work as an employee or as a contractor. The first one was it was called Markup. I added you to the Git repo. I, unfortunately, can't make it public because it has activation codes for certain paid libraries that I needed, and I don't know the status of being able to show that. But I did add you, so we can talk about it a little bit. And the commit history isn't too bad because there's a lot of interesting stories here.

Speaker B
I'm finding my GitHub notifications here nice. And logging into GitHub.

Speaker A
So basically, what this app did, it was, like, kind of coda for the iPad. So it would let you create these sites. The site had a sort of external URL and then, like, an FTP URL, and then you would use FTP to connect to a given site, browse the files, edit a text file, upload it, and then preview the changes that you made.

Speaker B
Okay.

Speaker A
Yeah. This is an app on the iPad App Store. But I did a lot of really funny, weird things because I had no idea what I was doing. I was, like, the exact opposite of you.

Speaker B
So the first things that stand out to me here, first of all, your commit messages are all just, like, Markup 1.3, markup 2.0.1.

Speaker A
Right. So the reason for that is that I wasn't using Git for tracking this project. What I was doing instead was using Dropbox, because Dropbox has version history, and it was something that I knew how to use.

Speaker B
Okay, yeah, that's fair. I'm glad you're using Git now.

Speaker A
And then each time there was, like, a new version, I would actually make a new folder and just to preserve that version of the code. And then I was able to reverse engineer that here on August 2, 2012, to be a Git history. So I would add all the files from the first version commit, add all the files from the second version commit, and so on.

Speaker B
That explains why all of these commits have the same date.

Speaker A
Yeah.

Speaker B
All right.

Speaker A
So this app I started in 2010.

Speaker B
Oh, that explains why all four commits in this history have the same date. Okay, but so the state of 2010 yes.

Speaker A
And I think the dates of the files will be correct. Yeah. So created by Sush Khan lou on March 9, 2010 One of the things.

Speaker B
That you commented about was using prefixes on my classes. I noticed that you haven't done that. Honestly, we're not using prefixes on classes now. Even in many cases, when they need to interrupt with objective C, even in Swift, if I were starting a new Objective C project today, I don't know that I would add prefixes to all my class names. I definitely would add prefixes to my extensions still, because there's much more potential for conflict there. Right. I'm 50 50 on that now, which I realize is heresy. But we're not writing objective C anymore.

Speaker A
That's right. So I think Swift will basically take care of this for you. And they use their name spacing to just kind of figure out the right thing to do.

Speaker B
Yeah.

Speaker A
But in objective c today I don't prefix the classes. So my second project, I did start prefixing classes. This one I didn't. And I've never prefixed categories because I think it looks really ugly. And that's really the most important thing when it comes to code.

Speaker B
So what are the interesting things that you have going on in this app? Can you direct me to so the.

Speaker A
The most interesting thing is I'm not sure if we can find it in the code. You probably can if you go to the initial commit and no, I guess it would be it's got to be 1.3. I don't know. I don't know exactly where it would be, but essentially I had heard of the concept of a model, but I didn't really know what it was.

Speaker B
Okay.

Speaker A
And I was, like, really figuring this programming stuff out. And one of the things that I ended up doing was I needed a way to store kind of structured data. I had this concept of a site that you could add, and that site had a bunch of important data in it, such as the FTP URL, the password, the username, the port, all that stuff. And I didn't know that I could just make my own object to store this stuff in. And I didn't even think to use a dictionary for this. I literally used an array, and I put each property of the object at a specific index in that array and remember which indexes correspond to which properties.

Speaker B
These aren't even extracted into constants.

Speaker A
No, they're not. They're absolutely not. I didn't know anything.

Speaker B
You've come a long way.

Speaker A
I have come a long way. Yeah. So all over the code, you'll see, this is what is this kinesis of ordering or whatever? All over the code base, you will see site data objected index three, and that represents the server URL. And I just use three represents server URL. There's one place in the app where you can go look up what they all mean. There's one file. I forget which one it is. Yeah.

Speaker B
Must have been really annoying to work with.

Speaker A
It was pretty bad. The thing is, I know I'd heard of model view controller before. I just didn't know how it applied. And I was like, it kind of seems like it fits here, but I don't necessarily know how it fits in. And then so if you go to, I think, 2.0, the code base for 2.0.1 has an actual site model class.

Speaker B
Okay, let me see. We're looking at 1.3 now, and if we skip ahead to the next version, 2.0.1 let's see here.

Speaker A
Yeah. Site dot M. I can send it to you in in Slack. Yeah. This actually has properties for each of the things. They actually have types. They have names, they autocomplete, all that stuff.

Speaker B
Nice. Yeah, this is much better. I see this is a immutable model still.

Speaker A
It is a mutable model. Again, didn't know about any of this Mutability stuff.

Speaker B
That was not really hard.

Speaker A
I do have an enum up here of connection type none, connection type FTP and connection type SFTP.

Speaker B
Very nice.

Speaker A
What else? There's a lot of embarrassing things in this code base.

Speaker B
That's okay. Yeah.

Speaker A
Apple gets pretty big.

Speaker B
It did look like you converted this to Arc. Oh, no, this is still non Arc, isn't it?

Speaker A
Yeah, that's actually another funny story. I didn't really understand what retain and release were doing. Yeah, this is still manual reference cutting. I didn't really still understand it at that point. And so what would happen is, like, I'd be working with it, and the site would and the app would crash, and I'd be like, okay, well, maybe I just need a retain here, and I put a retain in, and then the app would stop crashing. I'd be like, great. Yeah. So that was the first app that I ever made.

Speaker B
Yeah.

Speaker A
A lot of embarrassing stuff in here. Like you said, I've come a long way.

Speaker B
Man.

Speaker A
Yeah. I don't regret making code like this because you got to start from somewhere.

Speaker B
Oh, yeah, absolutely.

Speaker A
Very embarrassing.

Speaker B
Yeah. No, it's fun. Everyone starts somewhere.

Speaker A
Yeah, that's right. I think the important thing is basically recognizing, hey, this array thing is really not working. There's got to be a better way than this. And going off of that and building off of that and figuring out what the solution is for that thing. Likewise with git. I'd heard of Git, and I knew that it was a thing. I just didn't know how to use it, where to get it, especially if you don't have sometimes I feel like not having a CS degree made it so I wouldn't understand that stuff. So not knowing that Git is actually installed on your computer already, it's not the most accessible thing in the world, but it can be used by human beings. Would have been good to know. I was also on a big crunch for this app. I decided to build it, like, a week after the iPad was announced, which was January 2010, and I had to ship it by the time the iPad shipped, which was April 2010. So four months to build this thing.

Speaker B
So you were on time crunch.

Speaker A
I was on a pretty tight timeline. I don't regret using Dropbox for version control. You figure stuff out, you get better.

Speaker B
Yeah, definitely. No, I mean, going back to Git for a second, that isn't really something that I learned in my CS education. I learned that again from working at this startup part time during college and then took that knowledge and evangelized it. To fellow students in the CS program, some of whom thought it just was annoying and pointless. Like, I remember one project where it was a group project, and one of the guys just hated that we were making him use git. And so every commitment, he would just commit a completely random set of changes with the commit message a and push it up to the git server.

Speaker A
Yikes. That's not great.

Speaker B
I assume he's gotten past that since that was like, eight years ago.

Speaker A
Yeah. The funny thing is, I definitely saw some of the value in it because I would go back in time in the dropbox version history and pull out code that I had deleted, and I was using features that I would later use git for. But yeah, I'm glad. Now that I know, now I'm a big boy and I use git, I feel good.

Speaker B
We have a topic on our show Ideas list about just get usage and writing good commit messages and sort of just thinking about how producing documentation is at least part of our jobs in professional software development, right?

Speaker A
Yeah, definitely.

Speaker B
Or at least I think it is. So I can probably talk for half an hour about that.

Speaker A
I would say that'd be a good future episode.

Speaker B
Yeah, absolutely.

Speaker A
Cool.

Speaker B
You mentioned a couple of different first apps. Was there anything else that you wanted to throw in after? What was the app called?

Speaker A
Markup.

Speaker B
Markup.

Speaker A
Markup, yeah. So the second app that I made was it was called Fireside, and it was a podcast app, and it was synced through a service, and you could listen on the web, pause, and then keep listening on your phone. I think it was well ahead of its time. This was around 2012.

Speaker B
Really? You had a podcast app called a podcast related piece of software called Fireside?

Speaker A
I did, yeah. I know that Dan Benjamin now has. Yeah, and it's actually the same URL. Fireside FM used to be the URL of my thing, and I let it go because I was using it. And now he uses Fireside FM for his thing, which is pretty interesting. Maybe I should have kept it and sold to him. But Fireside I will say I can add you to git repo for that too. But Fireside I did start using git, although I used it from within the Xcode interface, which is very funny. I did start using models. I did start prefixing my classes. There were more singletons, which I regret. But we have to go through these phases as we learn to program, I think.

Speaker B
Yeah, absolutely. We'll add a link in our show notes to discussion on singletons.

Speaker A
Yeah, we absolutely will. And I did a manual reference counting to automatic reference counting conversion while I was building that, because that came out while I was working on it.

Speaker B
See, I think when was that? When did Arc first come out?

Speaker A
It was June 2012. Because I remember I started this app. The thing that actually got me to start the second app was the very first episode of Back to Work where Merlin just like, Why haven't you shipped yet? And I was like, Why haven't you shipped yet? Because I haven't started. And I went home that night and started working on this project, and that was January 2012. And I remember shipping in around fall of 2012, so I know the art came out that June.

Speaker B
Okay, cool, man. I think January 2012, at least according to Git, was when I started working on my first app, too.

Speaker A
Nice. It's been a nice walk down memory lane.

Speaker B
Yeah, absolutely. This has been fun.

Speaker A
Yeah. As always, thanks for listening. If you want to support us on Patreon, we would love to have your support. There's a whole bevy of episodes that you haven't heard. All the even numbered episodes are hiding out on Patreon, and it's $5 a month to hear them. The Patreon helps keep our podcast sponsor free, and we really like it that way. So, yeah, if you want to support us, hop over there and subscribe.

Speaker B
Yeah, absolutely. As sir said, it helps keep the podcast sponsor free, which we think is maybe less annoying for people to listen to and pays for editing costs and hosting fees and things like that. And to those of you who are supporting us on Patreon, thank you very much. It really means a lot to us.

Speaker A
Doug, real time follow up. Copyright automatic reference. Copyright John Syracuse. Automatic Reference County actually came out at WWE 2011.

Speaker B
Okay, that sounds bright to me, because when I was looking at even the first commit for my app, I think it was Arc already.

Speaker A
Yeah. I don't know why I hadn't adopted it yet. I don't know what the deal was with that. Maybe I have the timeline wrong. Maybe I started the app in 2011. Who knows? Hard to say.

Speaker B
Anyway, I have to check dropbox.

Speaker A
Oh, I don't have my belt because I'm in Denver. I've got you covered, Chris. This is great as always. Great to talk to you.

Speaker B
I'll talk to you later. Bye.

