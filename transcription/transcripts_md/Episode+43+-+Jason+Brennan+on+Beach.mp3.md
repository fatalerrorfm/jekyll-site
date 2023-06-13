Speaker A
Hey, everyone. Welcome to Fatal Error. I'm Chris.

Speaker B
And I'm, sirous.

Speaker A
And this week on the podcast we have a special guest friend of the show, Jason Brennan. Jason, you want to say hi? Hey. So this week we thought we thought it would be cool to chat with Jason about a project that he's been working on and sort of his motivations for the project and what makes it really interesting and why why we think it's really cool. Did you have anything else to add before we just dive in?

Speaker B
No, all I want to add is I've seen videos of this project in progress and it's really cool and I'm super excited to talk to Jason about it.

Speaker A
Cool. I've seen just bits and pieces on Twitter, so I look forward to hearing more about it. Where's a good place to start? Jason, do you want to maybe we.

Speaker B
Start in 1964 with like, Alan K's first work?

Speaker A
Well, it depends how much time you got.

Speaker B
So I guess to kick us off, Jason, why don't you tell us a little bit about what the app does and what it is for?

Speaker A
Yeah, so the app is kind of a combination of a lot of things. I've been describing it to people lately as a creative power tool for kids. So it's an app, it's a Mac app and it can do a few things. You can make art, you can make music, you can make interactive art and music and games and simulations. So it's one part, like, drawing app, one part kind of programming environment, and it's also eventually going to be networked so that you can share your projects with other people over the internet. And you can take their projects and play them and you can remix them and copy and paste bits that you like from theirs into yours. So it's a lot of things.

Speaker B
Maybe like juiced up. HyperCard for 2017 is a short way.

Speaker A
Of HyperCard is definitely an inspiration. So for those who haven't heard of HyperCard or aren't familiar with it, it was a Mac app that Apple made in the late eighty s and early ninety s. And it looked kind of like a drawing app, like a Mac Paint or like Ms Paint in that style. But instead of drawing just plain old pictures, you were drawing user interfaces. And they could look like a normal picture, but they could also have buttons in them and different kind of UI elements. And then you would draw out your interface and then you would start adding interactivity to it. So you would say, when this button is clicked, I want you to go to this other page. So in that way, it was kind of like a hypertext. It was like a link to another page. They called them cards, as in HyperCard. And this is before the web, by the way. This is like what the web should have been. Not only was it really easy to make direct links from card to card. But if you were using somebody else's card, like if you brought it over on a floppy disk or whatever, and you really like what Chris made in HyperCard, you could just copy and paste elements from his cards or his stacks into your programs, just like you would copy and paste everything on a Mac, because that's what you do, right? The idea that the web works the way it does today, where you can't just copy and paste a part of a web page into your web page and have it work, you can kind of mess around with the source code if you're lucky. But anyway, so that's what HyperCard was like. And so I am definitely very inspired by that. The idea of just seeing a part of a program or a piece of software that you like and just selecting it, copying it, and pasting it into yours, it's really cool.

Speaker B
That's the dream, right?

Speaker A
Definitely want to yeah, absolutely. This is how I think software should be made.

Speaker B
I remember back in the day, it was like elementary school, and I had to do a presentation on Squids, I think, and I made the whole thing in HyperCard, not really realizing that it could be a programming tool, just like, making a nonlinear slideshow about Squids in HyperCard. And this was, like third grade. Yeah, it was really cool.

Speaker A
That's awesome. And I think that's a really powerful part of it, too, is like, a lot of people just saw HyperCard as something like that. It wasn't like, oh, I'm going to program something. I'm going to make an app, or anything like that. And I think that is kind of part of the beauty and the power of it, is you don't approach it as like, oh, this is just a crappy programming tool, or a stunted programming tool. You're just like, no, this is like a drawing tool on crack. This is HyperCard.

Speaker B
Yeah. I don't even know if I knew what programming was at the time, but I just clicked buttons and put stuff down and made a cool thing and got like I don't know, I made a cool presentation out of it, and.

Speaker A
It was like I think that's kind of the cool thing about hype. And I've never used HyperCard, actually, but I think that's kind of the cool thing.

Speaker B
Right?

Speaker A
You can do these cool things without ever realizing, like, oh, this is programming, kind of, right? I feel like Jason Mason's thoughts about that, too. Yeah, for sure. One of the reasons why I'm excited about that aspect, where there is programming in this system, but it's not like the centerpiece. It's not. The point of this app is because I find as soon as you start calling something programming especially if it's a kids app, especially if it's something for kids, as soon as you invoke the word programming or code if you call it code, then you're kind of falling into this trap where it's now looked upon as like, okay, well, what kind of code is it? Are you learning? Like JavaScript? Are you learning Swift? Are you learning Python or whatever? And so there's that style of app, and then there's the well, it's not Swift. It's like a blocks based app or something like that. As soon as you start calling it programming, the question becomes like, okay, well, how do kids graduate from this into something like Swift or Python or whatever? And I think that's kind of taking it in the completely wrong direction. That's something that I want to avoid. Like, I don't want this to be a learn to code app. I want this to be a creative tool that just happens to have superpowers behind it.

Speaker B
Right, that makes total sense. So what's an example of a small thing that you could make your graphics do?

Speaker A
Yeah, the very basic ones are just small interactivity of jumping from place to place. So kind of like you could rebuild your Squid project in this app. The app is called beach, by the way, which I can explain the name a little bit later. So you could build something like that, sort of like an interactive slideshow, or, like, you could reinvent the game Mist if you wanted. I believe Mist was actually built in HyperCard originally. I might be wrong about that, but I think it was that is bananas.

Speaker B
I did not know that.

Speaker A
Yeah, so you can build very basic things like that in it, but the more interesting things are, well, you have a whole programming engine behind this app, so you can do things like script little objects on a canvas. So let's say the example that I like to go back to is simulating an ant hill. So you make an ant. Maybe it's just the ant emoji or whatever, and then you start giving it behaviors. You tell it to move around. And what do ants like to do? They like to forage for food. So you also add some food objects, maybe like the apple emoji or the flower emoji or whatever ants eat. I'm not really sure. And then you start programming these ants to forage for food. And what's exciting to me about this is that if you learn about how ants actually do this, the actual creatures, there's no centralized control. With ants. There is a queen ant, but the queen ant doesn't instruct the ants on what to do. The ants are kind of self guided partly by evolution and partly by the runtime of just the ant hives. So the ant hill. So they go out and they find food. They kind of just wander aimlessly. They find food, and then when they find it, they they start dropping this pheromone as they walk back towards their their ant hill. Now, other ants that are also wandering will, if they find this pheromone, they'll instead start they'll stop wandering and they'll start following the pheromone, and then they'll find the food faster, and then they'll drop more pheromone, which just kind of has this positive feedback loop. So the other ants foraging will just like you'll find the food a lot faster. Right. So you can build this thing in beach and see it happen right before your eyes.

Speaker B
Yeah. The thing I've always heard with the ants is they're a really good model of emergent behavior. So for an ant hill, you would say to make an ant hill you don't need rules or blueprints or plans. You just say pick up a grain of sand if you're not carrying a grain of sand. And if you are carrying a grain of sand, take it to the highest point and drop it there. And then with those two simple behaviors you can basically simulate not simulate, but you could create an ant hill if you were a large set of ants.

Speaker A
Absolutely. Yeah. There's a great book on this topic of this sort of decentralized thinking and modeling called Turtles, Termites and Traffic Jams and it's by Mitch Resnick. I'll give you a link for the show notes. Anyway, this is a programming book from the 90s about a decentralized programming system. So I'm drawing a little bit of inspiration from there, kind of as nice example projects to push with. But yeah, it's really fascinating to see this sort of behavior emerge with just by programming very simple rules. That's one sort of thing you can build in beach. I certainly don't think that every child is going to want to do that all the time. I wouldn't want to make them do that either. That sounds kind of monotonous, but.

Speaker B
I.

Speaker A
Want it to be able to handle complex things like that so that you can do something really cool. But I also want to allow fun things. So one thing that I'm really pushing for is the ability to program with color is this fascinating thing which is kind of an understatement. So we see color all the time, but a lot of us don't really stop to think about how to think about color. So having it in a creative tool like if you use a drawing app or if you use something like beach, you can kind of explore color for what it is so you can break it apart into color components. If you learn art in school, like in elementary school or something, you probably learn about color pigments, how there's like what is it? Red, blue and yellow are the primary colors and how you can mix them. You learn about the color wheel a little bit about color components or complementary colors and different assortments of colors. If you're a programmer, you also learn about color in terms of color spaces like RGB, red, green, blue, color spaces, how a color can be broken down into numbers and then how you can manipulate those numbers to change the color right. And I find that really fun to work with because, first of all, color is just beautiful. It doesn't matter what numbers I put into a color, into some sort of color scheme like that. I get something that is surprising to me. And then to be able to learn how to work with color more systematically. To learn something like HSL, which is hue, saturation and lightness. To be able to break a color down into that, to vary how bright a color is, to vary how intense a color is and see how you can think about that mathematically is really exciting as well. So I want to enable all sorts of fun and funky art projects. There was this line in Guardians of the Galaxy Two, the sequel that came out this past summer, where the main character, he's on this planet, and he's kind of given these godlike powers where he can make whatever he wants, and he says something to the effect of, like, oh, I'm going to make weird shit. That line really spoke to me. I want every kid to kind of get that feeling when they see this app, like, oh, man, I'm going to make some weird shit. That's awesome. Whether they say it out loud or not, that's up to them.

Speaker B
Yeah. One thing I want to throw in on the color note is, like, this concept even of sort of mixing colors to get other colors that, like red and yellow mix to make orange. I remember learning that in high school and middle school in art classes. But once I got to be an adult, I kind of learned that not everybody learns that, and not everybody just knows that as like, a thing that obviously red and blue make purple or whatever. And so even something that seems like the simplest part of it, of just like, mixing literal paint and getting a color out of it, is something that not everybody gets as part of their education. And if beach gives you the place to play with those colors and figure that stuff out and explore that space, then I don't know, that's the thing that not everybody has and that everybody could have, and it could be really cool.

Speaker A
Yeah. I don't know. Something that's really special about computers is the idea that they can scale ideas like that really easily. Books did that for a long time. You can have a good teacher, a good human teacher, who might be able to teach you about certain things, but say, Socrates. There's only one Socrates, but by writing down his writings like his teachings, then now there's like thousands of copies of Socrates everywhere, right? And these books, these copies of Socrates are kind of ghosts of him. They're not like the real thing. They're not as good as having a human being, but they're kind of the shadow of what he can teach that can reach more people. Now, a computer can do a little bit more. It can reach more people because more people have access to use computers. And seemingly computers are easier to use than books are to read. I don't know if that's a good thing or not, but they're also interactive. So you can imagine having an app like beach that has this kind of library of ideas that you can explore. It's networked, so you can go out, you can find other users, you can find maybe, I don't know, some sort of equivalent of GitHub. But in beach, where you can just find these ideas that you can explore. So, yeah, you have access to learning about color, you have access to learning about ants, you have access to video games. You have access to all these things that's kind of like presentations, would you say Squid presentations? It's possible that there will be a few of those.

Speaker B
If and when you release that. I'm going to make a Squid presentation in your look for, and I'm going to publish it on the Internet.

Speaker A
You should. We'll put it in the demo video. So Apple, I think, had tried to make ibooks into something that enabled this kind of like interactive interactive learning or interactive textbooks of some sort. Right. And I haven't really used any ibooks that do anything like this. And maybe that's just because I don't know any ibooks that I want to read, don't have this behavior in them. Have you used any ibooks that do anything like this or how has that worked, in your view? Yeah, I haven't really used very many. I've explored them a little bit. Like when these kind of enhanced ibooks came out, I played around with them a little bit. There is certainly interesting. It's hard to produce. I imagine Apple does provide an app, or at least used to, called ibooks Author, I think it was a Mac app. And you could create these sort of enhanced books with them. But producing some sort of interactive simulation or some sort of interactive thingy, for lack of a better term, in an ibooks thing, it requires programming. It requires high production values to get something nice. It requires probably like an art team or somebody who can model things with the 3D tool. So that's hard. It doesn't mean it's not worth it. But yeah, I think it's an interesting attempt. But like a lot of things that Apple does, they kind of made it and threw it against the wall and then moved on to something else, which is a shame. Yeah, that's kind of the feeling that I got in beach. Adding behaviors to things doesn't look like traditional programming, like typing commands in what does it look like? How does a user go about adding behavior to some part of their system? Yeah. Okay, so we're all going to have to use our imaginations here a little bit because this is a podcast, and I'm talking about a visual programming environment. Okay.

Speaker B
It's really the best place to talk about a visual programming.

Speaker A
We're all at a little bit of a disadvantage here. Well, Sarish and I have just dictated code at each other before on the podcast. There you go. This will be better than that. This is nothing. Yeah. Okay. The whole environment is graphical. Now. When a lot of people think of graphical programming, they think of boxes and arrows drawn, like a, UML diagram, basically. Right. Because that's what a lot of graphical programming is. It's highly unimaginative and just generally terrible. I also think about, like, I had a Lego Mindstorms robotic thing when I was growing up, and you could program it by dragging, like, blocks into place. And that wasn't exactly, UML but it's similar, right? Right. The nice thing about blocks, I kind of have a love hate relationship with blocks in programming environments. I used to work on an app called Hopscotch. It's a programming environment for kids on the iPad and now iPhone, and it involves a lot of drag and drop blocks. So blocks are wonderful for children in a lot of ways because blocks, it's a rectangle and it has text in it and parameters that you add values to. The beauty of that is that you're not typing any code. So the fact that you're not typing means a few things. It means that, first of all, you don't have to type, which for a child is usually a barrier, so they don't have to learn how to type. You also can't have a syntax error, which is like a huge deal. The program always stays consistent, like, always stays the memory representation is consistent because it's kind of always in the format of a program, which is amazing. You just can't break it. You can still have bugs, of course, but you can't have something that doesn't compile. So those two things are fantastic, but blocks kind of fall short in the sense that a lot of programming environments treat them as like some sort of cure all for difficult programming. And they're not. They're useful, they're necessary, but not sufficient to have a good programming environment. Beach is a little different, where it has the benefits of you don't have to type out your code and you can't have syntax errors in your programs. But because Beaches is a graphical environment, everything that you use is a graphic. So that sounds kind of like a tautology, and it is, but it's something that I have to remind myself of constantly as I'm working with beach. So, in a standard programming language like, say, Swift, your code is just text. It's just plain ASCII or Unicode text, which means that in order to have meaningful symbols, so, like a variable name, or a function name, or a class name or something like that. The only way that you can give identity so that the compiler can match up one symbol with another one is by having the exact same set of characters. It's based solely on the text. So if you use a class name but you spell it wrong somewhere, that's broken. Swift can't figure out what you mean by that. But in a graphical programming environment, you don't need to have things have the same name everywhere because their identity is based on some sort of other identifier. So maybe it's a pointer address, maybe it's a Uuid or something like that. But it means that you can have flexible representations of the same thing. So I might make a block or an instruction of code somewhere and then drop it into a script, like a function for my program for adding behavior to an object. But the nice thing is that doesn't have to look the same as where I got it from. So you can have different representations of things. You can also search for objects, you can pick them out of palettes, you can use the toolbox, you can copy them from other people's programs. The instructions tend to look like text, they tend to look like words. So an example that I was working with the other day would be make the ant. It said ant turn towards the ant hill or something like that. And it reads quite like plain text. It's a sentence. It looks like a piece of UI. You can interact with it. You can click on the parameters. You can add new values or change values.

Speaker B
It sounds like it's kind of and from the screenshots and stuff I've seen, it's like a structured thing where you can kind of stick in parameters to make it act the way you want to act.

Speaker A
Right? Are you familiar with the app Automator that comes on OS Ten? Right?

Speaker B
Yes, I use it for renaming files.

Speaker A
Yeah. So Automator is kind of a little programming environment that Apple ships on Mac. It's relatively straightforward. You pick from a library of functionality. So you have things for doing Actions in Finder, doing Actions in Preview, doing Actions in Keynote, doing Actions in whatever. And then from each application you pick from a list of things that it can do. So Finder can enumerate files, it can rename files, it can open folders, it can copy folders, preview can export images from a PDF or so on. And you kind of just chain these instructions one after another. Now those instructions don't look like code, but it's doing a very similar job. It's a list of ordered instructions that are going to run in time, forming almost like a pipeline. And so beach is kind of similar that way. It doesn't look like Automator, but it follows the same idea of you have a list of instructions. It also can do conditionals, so you can have if statements, it can do branching and loops and so on like that. It won't look foreign to anybody who's programmed before, but it is not text. You're not typing it in. Okay, so it sounds like you're sort of combining the maybe block based philosophy with more text, like less graphical components, maybe that you have more control over that's. Right. Some things are just expressed in text, other things, it's all in flux right now. But I'm working on if you're working with geometry, one thing that I'm really excited about is being able to program with geometry. So maybe you have a circle and you have a square and you have a line. Each of those things has different objects within it. So a rectangle has at least nine objects within it. It has a top left corner, a top middle, a top right corner, and so on, kind of like all nine points of it. And you can think of those as discrete objects. You can also think of the sides of a rectangle as an object. So, like, the left edge and the right edge are two separate objects of that shape. So if you're programming with that, I think it would be great if your actual program showed a picture of that object that you're dealing with. So if you're saying move the center of this circle to this new position, why not show in your program the circle and the center being acted upon instead of it just being text? So I'm experimenting with that right now to try to make it so that your instructions have a lot more connection to the thing that you're working on.

Speaker B
So one thing that I'm not quite following is, is it a representation over time or is it a representation, you said? Okay, well, if I want to move the center of this circle to over here as an instruction, what is that representation that you're looking at over time is like, oh, well, at time, T equals zero, and it made it represent as T equals zero to the user. But whatever. At T equals zero, it looks like this. At T equals five, it looks like this. Or is it a different thing?

Speaker A
It depends. So most of the time, I imagine you'd be writing a script that says that, say, you'll be writing a script that repeats, say, every frame, every 60th of a second or something like that. So it will just be kind of running continuously, applying this behavior over and over.

Speaker B
Right. Like on every tick, essentially, right?

Speaker A
So on every tick do this. There can be other triggers. So, like, when this object is clicked, trigger the script. But one example would be every tick. So these instructions that you're writing are basically like per unit of execution. So, like per tick. So if you have six instructions in your program, those six instructions will run in order, every frame. So if I had one where it was move the center of the circle to the end of my velocity arrow or whatever, right, that would be do that move every time the program executes, which, if you're doing that 60 times a second, it can be kind of hard to imagine how the program is actually going to run. So if you're using a standard programming language or like many blocks programming languages, you're kind of stuck at this point. You have to then imagine what the program is going to do over time. But this environment actually visualizes what the program does over time inside the program itself. So you have a line of code or a line of instruction text and then immediately underneath of that, in the current design at least, is a visualization of what that does, every frame. So you can kind of play through your whole program and see how it executes in line with the code as you're writing it.

Speaker B
Got you. So this is sort of sort of like a Brett Victorian, kind of a stop drawing dead fish kind of thing where you use the representations in the graphical programming language to also represent the values and actions and whatever as well.

Speaker A
Yeah, as best you can. Now, not everything has a graphical representation that makes sense. So it would be kind of silly to do that. There's just straight up math of like, I need to write this formula that doesn't always make sense to do graphically or geometrically. So in that case you would just write it out like a normal math expression. But if it does make sense to do so if it does make sense to work with geometry, then I would love to have you actually work with the geometry in the actual program instructions whenever possible.

Speaker B
I have one question, which is essentially like when I have a Swift program, I hit run and it has some initial state based on how the code is set up and then also based on how the code is set up, it mutates that initial state over time. My understanding I've never programmed in something like small talk, is that your program just is and it is always kind of quote unquote running. And as you add code, you're kind of adding it to the live environment that you're already in. And so the state that the program is currently in is also the initial state. There is no concept of an initial state. So what I'm curious about with your thing is essentially is there an initial state that you set up and then run from that initial state? Or is it like an environment where you are dynamically adding behaviors and removing behaviors to play with a system?

Speaker A
Yeah, so there's no real initial state in this environment as it exists currently. And that's the way I'd like to keep it if I can. So you kind of just have these objects around that always exist and then you can influence them with programs that you write. So if I've got a script that say, makes my aunt Wander for food or whatever, I get to control when that runs. But there's no time. Equals zero. There's just like I'm either running the script or I'm not.

Speaker B
Got you. So you can manipulate the objects with these little programs, but you can also manipulate them directly by just picking them up with your mouse and putting them somewhere else. Just like sketch or whatever.

Speaker A
Absolutely. So it's a lot like a full featured graphical drawing app, which makes for a really fun Hello, World. The Hello World is just drag a text object onto the thing and type Hello, World into it. There's your hello, world. That's it, right? Yeah. Okay. I think this is making more sense to me now. I think not having seen even a video demo like Serous has, I'm coming out this with a pretty blank slate. But I think this makes sense. This sounds really cool. Yeah, it's kind of like just picture an app, like Sketch, a vector drawing app, infinite canvas that also, instead of just graphics, you can make programs in it as well.

Speaker B
Right. Sketch, for example, has some features where you can like, if you make a tape, if you design, like, effectively, what's, a table cell, you can then duplicate it some number of times and insert data into it. Imagine that. But just, like, turned up to eleven.

Speaker A
Yeah. Okay, cool.

Speaker B
So where are you right now? What have you done on this project, and what are you excited to do next on the project?

Speaker A
Yeah, so I've been working on this project full time for about three months now. I started pretty much from scratch. So I have an idea. I have some notes in a notebook, a paper notebook, but I don't have anything else. Like, I don't have any designs. I don't have any prototypes. I don't have anything. So I started from there, and I've just been working off that. So I have kind of gathered my influences. I made a mood board in Sketch of everything that I am inspired by. All of the different programming environments, all of the different other creative power tools, good quotes from papers on education and on childhood development and so on. And I started with that, and I kind of just drew. I drew on paper. I wrote notes to myself. I keep a text file that I update every day. I just kind of write, like, a Dear diary of how my day went, how my development time went, whatever I'm thinking about, whatever I'm stuck on right now. So I keep that every day. And I've just been making designs in Sketch. I love Sketch. It's definitely a huge inspiration for me. So I've been making designs, and then the last month or so, I've been building prototypes. So what I mean by prototype is I have a framework that I use. It's written in swift. It's open source. It's called prototope. I worked on it while I was at Khan Academy. It was started by Andy Machusack at Khan Academy, and I worked on it a little bit more. And then after I left Khan Academy, I took a fork of it, and I've been maintaining a fork of that. So prototope is a swift framework, and it's essentially like a nice wrapper around UI kit and also around app kit. Now, on the Mac, what it does is it lets you do things like get a view hierarchy up really fast. And it does that by making it really easy to just get a picture on screen. So instead of making a view, you make a layer, and you can make a layer with an image, and it's just on screen. You can add interactivity to it really quickly. You can do everything you do for a professional app, but just, like, way faster and hastier, I guess. So I've been working on these prototypes every day, and usually what will happen is I'll have an idea of something I need to explore. So usually I have a graphic done up in sketch, and I say, this isn't good enough to prove whether this is a good idea or not. Or, like, I have a hunch that this will be better once I play with it, or I have a hunch that this will suck once I play with it. Both are kind of interesting things to figure out if I'm right or not. So then I'll code up an interactive prototype that usually just focuses on one aspect, one element. So I've had prototypes that focus on just dragging things around the canvas. I've had prototypes that focus on pausing and running a script. I've had prototypes that work about debugging scripts, like, those sorts of things. So I essentially pick one aspect of a feature and just build out a quick example of it enough that I can get it working and then figure out what's wrong with it, and then iterate on that and fix it the next day.

Speaker B
Nice.

Speaker A
Cool.

Speaker B
And so lots of prototypes is basically where you are now.

Speaker A
That's right, yeah. At this point, there's definitely nothing that I could ship to anybody, but it's enough, basically, to be dangerous for myself.

Speaker B
Nice. So what are the next things that you're really excited to test out?

Speaker A
Yeah, that's actually a great question. The next things that I really have to figure out are basically how to make a program, which not a small thing. I'm ironing out how programs work, what sort of metaphors I want to go with of, like, you know, how how are you supposed to think about this? Like, for example, a variable. Assigning something to a variable. Like, you we would all say this as programmers or as experienced programmers without really thinking about it. Like, oh, yeah, of course, you just assign a value to a variable, like duh. But that's a metaphor. There's not actually a variable that exists inside of your computer. That's an abstraction that we've designed for human beings to understand what the computer is doing better. And so assigning a variable makes sense to us because we've done it and we're experienced with it, but it's not necessarily the best metaphor for that. So there are other metaphors, might be like putting something in a box or labeling something that exists in memory somewhere. So I'm kind of just like exploring these and trying to really get down to the heart of, like, if I'm expecting an eight year old child to build a program with this, then how am I going to meet them? Where they're at with their cognitive abilities, with their life experience, such that this is going to make sense? I don't want to just be like, oh, kids, it's like your algebra class where you have X. You love X.

Speaker B
That's that variable that we all know and love.

Speaker A
That's right. I suspect that most kids don't love X, and so I kind of want to find something better, like, that will translate to them.

Speaker B
What about Y.

Speaker A
Is much more interesting.

Speaker B
That's right.

Speaker A
I mean, I could talk about why for hours, and in fact, I hope that kids will think about why a lot more after using this app.

Speaker B
Pretty good pun.

Speaker A
Yeah. You just kind of touched on this. But one of the questions that I wanted to ask is what's your motivation for working on this project? What are you trying to solve? What are you trying to change? Yeah, so as a software developer, I think computers are amazing. I think we kind of take that for granted sometimes of how incredible this device that we stare at all the time is. But it's very good at simulating things. That's what took off computers in the 80s was the desktop publishing. And if you think about what desktop publishing was, it was a computer like a Macintosh Simulating design studio or layout process or printing press or something like that. It was really good at doing this. You have word processors. You have things like Photoshop start to come around. You have things like Quark that can lay out pages for magazines and books and so on. The computer succeeded at that because it's really good at simulating that. And I think that's the power that everybody should have. I think that being able to simulate things, you shouldn't just depend on what software developers can build for you because then you're beholden to somebody else's imagination and like, hey, I've studied computer science and I know a lot about that, but I don't know a lot about any other domain in the world, basically. So anybody who does have experience with that or expertise with that, they're kind of screwed. Like, they can't just go out and build their own piece of software that can really amplify what they're trying to do. That's what the computer is. It's an amplifier of abilities. So I wanted to make an environment that was about that. That was about amplifying good human abilities to their fullest potential and letting people letting children specifically learn how to do that from a young age. And there are lots of learn to code things for kids. I've talked about some of them. Apple's got one called Swift. They kind of want if you look at their material, their marketing material, they kind of want every kid to learn to code Swift, which is really strange if you think about it. It works in Apple's interest. They've got this bizarre quest to rule the world with Swift. And I'm not exactly sure why, but I think when they talk about that, they mean that every software developer should be using Swift. But they're also swift playgrounds for iPad is also very clearly marketed at getting every kid to learn to program Swift, which is kind of strange.

Speaker B
It's almost kind of futile. We're going to train you to till the fields from a very young age, and then when you're old enough, then.

Speaker A
You can come state sponsored programming. I learned yesterday that at the time of the French Revolution, less than half of the population of France spoke French. It was kind of like a mandated thing by the state that eventually got everybody to learn French.

Speaker B
What did they speak?

Speaker A
French speak. There are like 30 regional dialects of different languages. Anyway, this may be for the bonus according maybe you can edit this out. I don't know. Well, I think it would be great to have more people have the opportunity to join the computer science industry, the software development industry, and that involves getting more children excited about computer science at a young age. I don't think that it's a good idea to get every kid to become a software developer. That's kind of silly, right? And Swift is very much designed to be a language for software development. It's not a language for every person to be able to express ideas in. It's a language about memory, safety and performance and kind of like robustness. But kids don't give a crap about that. No kid cares about if their type is correct when they're trying to make an anthill simulator, they care about their problem that they're working on. They don't care if they have the right enum case. If their program crashes, it's no big deal. They're not trying to make a robust program to help Apple sell iPhones. They're trying to make a project about Squids to get a good grade in their class or to learn about Squids.

Speaker B
So it kind of sounds like instead of software development being the main thing that someone does, and then they learn about a domain in order to solve problems for someone else or for themselves. You're trying to say software development maybe should be more like literacy or more like just this passive thing that maybe anybody could do. And if you're a geologist or a kid who's interested in ants, you could build your own simulation of a thing without requiring a software developer and catapult your understanding further, right?

Speaker A
I will correct you a little bit. Like, I don't think software development should be like literacy, because literacy, we've decided, like, everybody should learn, everybody should become literate. And the reason why we do that isn't because we want everybody to become a journalist or an author or novelist or whatever. Although it's fine if they do. We teach everybody how to learn to read and write because that's how our culture has, like, how it disseminates important ideas. Like, our culture's, big ideas, are in literature, right? And so we want every child to learn how to read. It's very important that they do that. But literature can't talk about every kind of idea. Like, you can describe an ant hill, like, the way that I just talked about it earlier on this podcast, but that's not, like, the best way to understand how an ant hill system works. Seeing it in real life is one aspect, but the benefit of programming it over. Seeing it in real life is that you can pause it, you can rewind it, you can screw around with it. You can ask questions like, what if what if there were a million ants? Like, what if there were like, what if the ants couldn't find the ant hill? Like, you can ask all these questions that you couldn't really ethically do or feasibly do with a live ant hill. So I think that everybody should have this kind of computer literacy. Everybody should learn this way to create simulations with the computer because there are powerful ideas that are better suited for it than they are for books.

Speaker B
Got you.

Speaker A
That makes a lot of sense.

Speaker B
I guess if you don't want to call making simulations with a tool like beach, if you don't want to call that software programming, then fine. But whatever that is, that ability to define and design your own software simulations, you do agree that everybody should have that?

Speaker A
Yeah, I'll call it software programming, just not software development. Like, software development is, like, the professional version.

Speaker B
Right? Yeah. Okay. I think we're on the same page then. I think we're on the same page, yeah. You're saying software development is like being a journalist? Software programming is like being someone who.

Speaker A
Reads the newspaper or you got a bingo.

Speaker B
Yeah. Someone who texts their friend.

Speaker A
Yeah.

Speaker B
Cool.

Speaker A
Yeah. Awesome. Yeah. I am really looking forward to someday getting to play with this environment. Yeah. I really should put it on the Internet somewhere. Every time I send him something, he's like, dude, you got to tweet this. You got to tweet this right now.

Speaker B
Because he sends me these cool things that are not only cool to me, but they're cool to everybody. And I'm just, like, just literally tweet exactly what you just said to me, and people are going to love it.

Speaker A
Yeah, no, I do plan on sharing some of it. I just want to get it a little bit more right. Not in the sense that it's going to be flawless at all, but just some of this stuff is just damn sloppy. Like, these prototypes are written very hastily. The first thing you learn about writing prototypes is like, you have to throw out all of your software developer skills of making sure it's memory safe and making sure that it's abstracted properly. It's supposed to be the nastiest code in the world just to get something out as fast as possible. Sure. Yeah, I bet that's hard.

Speaker B
Or it's hard for me. I don't know if it's hard for you.

Speaker A
It's like a funny, humble brag, right? You're like, oh man, it's so hard to not write good code.

Speaker B
I'm just so burdened by this ability to write beautiful code.

Speaker A
Good at it. Yeah.

Speaker B
I will say sort of on the topic of your prototypes being awful and you being sort of a little reticent to share them, there was a friend of mine who tweeted this really cool thing. It was actually earlier today. And the tweet reads, I think I'm more excited by people's shitty versions of things, sketches, prototypes, et cetera, than the finished, polished thing.

Speaker A
That sounds so familiar.

Speaker B
I'll throw that in the show notes. It's by someone named Jason kinda. I don't know who that is, but that seems relevant.

Speaker A
That's a very insightful tweet.

Speaker B
Yeah.

Speaker A
I have to say that sounds right to me. Yeah, no, I'm actually really interested in figuring that out. I've been following this artist for a little while, brian Lee O'Malley. He's a comic book artist and he did the Scott Pilgrim books. And he's also working on a new book right now. And he shows his sketchbook on Instagram every day. And it's fascinating. It's beautiful to see what he's working on and his rough drafts of things. I'm very much enamored with that idea. I'm trying to figure out what's the programming sketchbook like. I can tweet pictures of things, but the point of software is to see it happen, use it well.

Speaker B
I think videos and pictures get the point across until eventually you write like, the web version of this tool and then I can go click on the equivalent of whatever NPM is or GitHub and say, hey, play this for me. And it just does. And you'll be able to show that eventually. But for now, videos and images are going to have to do as like, lo fi representations of the ideas that you're trying to express.

Speaker A
Yeah, that's true. Maybe I should apply like an Instamax filter on it or whatever. So before we wrap up, I have one more question. Tell me about the name beach. Yeah, so I would be totally lying if I said that I thought of it because it had all this great meaning behind it. The truth is, I was listening to an album by Neil Young. It's called on the beach, and it's my favorite album by him. And I was listening to the titular song, and I was just like, this is like a really great name for a programming environment for some reason, so that's like the original origin of it. But then I thought about it a little more, and it's actually kind of a good metaphor in a lot of ways. So a beach can be a relaxing place. It's a place where you go to unwind. It's also a playful place, especially for children. You can build models of things like sandcastles beaches are often broad, and they face a long, inviting horizon. They let you explore the water, starting out shallow and then going as deep as you want as your skills allow. So I thought it worked really well after I thought about it some more, so I kind of stuck with it. Nice. Cool. Yeah, that makes a lot of sense.

Speaker B
Jason, thank you so much for joining us. And thank you so much for telling us about your cool project. We look forward to seeing more of it. If you want to follow Jason on Twitter at jason Brennan. And we also put his blog in the show notes in case he does decide to share. So maybe more long form stuff about beach. Jason, thank you so much.

Speaker A
Thanks for having me.

Speaker B
Yeah.

Speaker A
Thanks a lot, Jason. It's been great to hear about this project, and great to get to talk to you again. Awesome. My pleasure.

Speaker B
Cool. Take care.

