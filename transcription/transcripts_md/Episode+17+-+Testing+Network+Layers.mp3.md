Speaker A
Welcome, everyone, to Fatal Error. I'm Chris De Zomback.

Speaker B
And I'm Sirish Khanlon, and today we.

Speaker A
Thought we would talk about testing your network layer. A network layer is something which appears in, I'm going to say, pretty much every iOS app, and yet it's something that often doesn't get the attention that it really deserves in automated testing, especially because it's something so core to the functionality of our applications. And I think that's probably because it's really a fairly hard thing to test.

Speaker B
Yeah, it's inherently global, so that part of it lends itself, kind of to single, tiny design, and it's also inherently asynchronous. And those two parts of it, I think, make it like those are two, like death knells, basically, for testing. So just that it's naturally challenging to test and it's such an important part of so many apps, I think makes it a great topic to really crack, a great nut to crack for testing for us.

Speaker A
Yeah, absolutely. So I know that you have been thinking about this a little bit lately and came up with sort of a few different parts of a network layer that deserve testing. Do you want to break those down and then we can dive into how you might go about testing each of them?

Speaker B
Yeah, for sure. Broadly, there are two main approaches to testing your network layer. One is to create a mock for something like a URL session using a protocol inject that in and have everything go through that mock. And then you can have it just return dummy data and then test all the components of your network layer. And the other approach is to use something like, Ohhttp, Stubs by a friend of the show, Olivier Elegan. And that will basically let you intercept the network call at the network layer and then wait as long as you like and return whatever data you want. I tend towards the former rather than the latter, just because I would rather not have a bunch of JSON strings, like, all over my app. I would rather work in actual real types and then convert them to JSON sort of as needed. But I'm curious to know if you have any opinions on basically the choice between those two paths.

Speaker A
I'm a little bit confused about why one of them entails having JSON strings throughout your app. Like, those are kind of separate.

Speaker B
Well, for the second one, you have to have a fixture to return, basically. So you have to have some JSON just in a file that you read out and return as part of your response.

Speaker A
Okay.

Speaker B
If you're faking the whole network layer, that's true. Whereas you have a little bit less of that with the other approach.

Speaker A
Right. Although if you're really testing the same sort of code path, then you're still going to have more or less the same fixtures, I feel like. Right, so we actually take both of these approaches and various projects at work for different reasons. So we do use Ohhttp Stubs to test some code, which is our own network library that's built on top of Nsurl Session. And the nature of that is just so I mean, it it helps us deal with Nsurl Sessions background functionality and add some other sugar around Nsurl Session APIs. And we do use Ohhttb Stubs to test that pretty extensively because it would be very hard for us to redo that in a way that Nsurl Session is injected. It actually manages URL sessions under the hood for us.

Speaker B
Right. I would say the difference between the two approaches is one is very unit testy where you test, okay, here I'm building a request, here I'm sending a request, and here I'm parsing response. And the other approach is more integrationy, where you're testing the whole top to bottom of like, I'm going to start with the inputs, and I'm going to verify that the outputs are what I expect, and hopefully everything in between works correctly.

Speaker A
Well, you don't necessarily have to conflate testing your networking layer with testing Model Parsing. Right. You could unit test your networking API and make sure that and use Ohhttp Stubs to intercept those requests and then make sure that the data that comes back is the data that you expect from the fixture that you're using.

Speaker B
Right. You could have a fixture that's not a real model in your app. That's just simpler.

Speaker A
Right. I mean, that's something that I think is totally feasible, even though it is a little bit cleaner of an approach to had a protocol that covers URL Session and build a sort of test double for URL session and use that for testing. You do have a maintenance project there, because now, like any future Nsurl Session API changes, which I guess there shouldn't be too many of those, but you're going to have to take those changes into account in your Nsurl Session protocol.

Speaker B
Right. Or like, if you want to use a different part of Nsurl Session, like you now want to do data upload tasks.

Speaker A
Right.

Speaker B
You now have to mock that out as well.

Speaker A
Right. Another approach would be to define an interface that doesn't necessarily shadow Nsurl Sessions interface and have just very thin Nsurl Session adapter.

Speaker B
Right. That could work too.

Speaker A
Right.

Speaker B
Basically, the way that I break this stuff down, I mentioned a little earlier there's about three components. I have some data that can represent a request, and I need to turn that into a URL request, like foundation object that the URL handling system knows how to work with that's one piece. The second piece is when Nsurl Session usually returns to you with data and an Http URL response. And so I want to take those things and combine them. I want to read the data into JSON Parse, the JSON check if there's any API errors to handle, any status code issues to handle, and all that kind of becomes the response side of things. And then there's one piece in the middle which is just sort of like testing the actual network client itself, which you pass it the request data, it turns into a URL request. It fires that request with a dummy URL session, and then it creates that response. And you guys test the thing from end to end. Pretty much, yeah.

Speaker A
I mean, that sounds like three different things to test. Right?

Speaker B
Right. That's three I would call. The first and last are definitely units. The middle one might be an integration test. I'm not sure. Depends on how you define integration test, I think.

Speaker A
Yeah, I'm not going to spend too much time worrying about that here.

Speaker B
Yeah, so the first one is not too bad. Usually make each of these things has like its own each of these components has its own type. So I usually make a request builder, and a request builder is initialized with a request, which is a protocol that it has just a method, a path and parameters. And you just have to provide those things and it will fully build out. If it's a get request, it'll do query parameters. If it's a post request, it'll do turns the JSON, all that stuff. It'll do all that stuff for you. And I have code to check all the paths of that, including like, hey, I want to make sure that if the host of the URL is Nil, that's not a valid request return nil. So I'll write a test for that case. If anything else comes out and fails, I have tests for all those little tiny cases, 123456 tests. Like nothing crazy, but just basically every case, all the paths through the thing are tested. So multiple query parameters, single query parameters, make sure it has a path, make sure it has a URL, make sure it has all those things. So that's the first component. The last component is the response, and that's the thing that handles. Like, sometimes an API will return like an error key, and then the error key will have specific data about how it failed. So you want to turn that into like a rich, swift maybe like a struct that represents the thing and conforms the error protocol. So this response object does all that stuff.

Speaker A
Okay, cool. And those seem like two things which we already know how to test in a very traditional unit testing fashion.

Speaker B
Right, exactly. Yeah. So since it's so, like, data in, data out, it's very straightforward to say, like, create these things, run them through the code, and then assert that they look right on the way out.

Speaker A
Right.

Speaker B
One little trick that is nice is that you can make your own Http URL responses by just passing it a URL status code, an HT version, and any headers you want. It does come back as optional, but you can just force and wrap it because I force and wrap in tests.

Speaker A
Yeah, I will do the same thing in tests a lot of the time. Yeah.

Speaker B
So you can basically make your own Http URL responses, return those, and use that in testing these response objects. And I think testing your sort of like model constructors is a separate part as well. So like your user model, like you want to initialize that with JSON. I think that's a separate part of your test suite entirely. Like you don't want that to be touching this stuff.

Speaker A
Right, that's a separate problem. So then what exactly are we trying to test? We're trying to test the part that takes a request and actually sends it to the network, right?

Speaker B
No, just that it sends it to the URL session. And I trust that the URL session works, but I haven't covered that part of it. I've just covered the request building and the response building.

Speaker A
Right.

Speaker B
Basically going from really simple foundation E types like strings and instant data, to objects that richer objects the foundation understands. And then taking the result of that from the network side, which is the data and the URL response, and creating the rich objects that I want to work with, which is like actual errors that represent errors in my API that the JSON is parsed from being just data into being an actual rich object. It's all type parameterized as well, so that you can get your type info out of it. And then that just leaves testing the network client itself.

Speaker A
Right, which is what I was trying to get to with that question, is, let's get to the part that's actually a little more difficult to do.

Speaker B
Yeah, that puts it all together. So my network client, if you were being really strict, you would say that it has three responsibilities, maybe four. The first responsibility is build the network request. It gets like a request type that I've devised, just the path and the parameters and the method, and it combines that with a base URL that the network client knows and creates like a URL request objects. That's responsibility number one.

Speaker A
Okay?

Speaker B
Responsibility number two is send. That responsibility number three is build the response that comes back from the data and the response. And then responsibility four is something I actually blogged about recently, but it's this thing that I'm calling Request Behaviors. And the idea is just that you can encode different side effects that you want to have happen when a certain request fires, such as specialized headers, such as the network indicator at the top. I have a blog post about this. I'll put in the show notes. I won't spend too much time on it, but basically it also handles working with those request behaviors. So between those four responsibilities, I have maybe ten tests and it's basically just there's a happy path test, which is just create a simple request and mock the URL session and make sure that it comes back successful. Test that the JSON coming at the other side is correct test with the JSON coming outside is incorrect test, bad status codes, et cetera. And then there's a couple of tests for the request behavior stuff. So that's pretty much how I handle testing the network client itself. The network client is only about 50 lines of code, so it's not too too bad.

Speaker A
No, that's good.

Speaker B
Yeah. Like you say, a thin wrapper around URL, URL session.

Speaker A
How exactly are you testing this? You are taking the approach where you have a protocol that covers some of the Nsurl session API, right?

Speaker B
There are two things in the protocol. One is invalidate and cancel, which is necessary to cancel inflight requests when the person logs out for certain apps. And then there's also pretty much just data with request and that just returns a promise and so it will basically return to you. Like that's just the basic network request thing and the promise version I have in an extension on URL session. And then I also make a mock and the mock basically takes it's initialized with the status code and any data of JSON that you want to return. And then it'll turn the JSON dictionary that you pass it into actual data and it'll construct a Http URL response from the status code and then pass that back to you when you call data with request after some delay that you can also specify so that's how that part of it is mocked out. And then the network client is initialized with one of those mock URL sessions. And I use the Xcode asynchronous the XT test asynchronous stuff, which I think is actually pretty nice. Like I don't bring in any other libraries for this. So you have expectation with description and that is basically the thing that will be fulfilled to verify it. And then you call wait for expectations with some timeout and it ensures that fulfill is called on that expectation object that you have within that timeout. And if it doesn't, that's like a failure. And then I just add then and catch handlers onto the promise and succeed or fail, depending on if it's supposed to succeed or fail or fail and succeed, if that makes sense.

Speaker A
Okay, so why did you opt not to use something like ohhtttp Stubs to test this?

Speaker B
I've done that stuff in the past and it feels a little too like I kind of don't want to muck around at that level, which is like I have to have JSON fixtures and you have to make sure that your test is setting that stuff up. That stuff is very global as well. So you run into the problems of making sure that you do set that stuff up in setup and tear down instead of in init for the test, stuff like that.

Speaker A
Sure.

Speaker B
And I just would rather test the data of my objects rather than testing that it actually hits the network layer.

Speaker A
Okay, fair. That's fair enough.

Speaker B
But you all do choose the Ohhtp Stubs approach. So why do you choose that instead of the sort of mock and stub approach?

Speaker A
So we use Ohhttp Stubs to test a network client, which adds queuing and prioritization of requests on top of Nsurl session.

Speaker B
Got you.

Speaker A
And so it's very tightly tied to Nsurl Session. And Ohhtttp Stubs actually works pretty nicely to verify that the requests that the network sees are actually the requests that we expect from this library.

Speaker B
What level do you verify at? Do you check the status code every single time? Do you check the headers? What level do you check that stuff at?

Speaker A
We're not testing to verify that nsurl Session attaches the right headers. Right. We will verify that if you hand the network client some headers that they make it through to the other side.

Speaker B
Right.

Speaker A
So in that way, I guess it's a little bit more of more, quote unquote integration test. Although this doesn't really feel like anywhere near a full scale integration style test.

Speaker B
Yeah, it's definitely a very blurry definitional thing.

Speaker A
Yeah. So we use Ohhtp Stubs to verify that that sort of networking library works correctly, and then we do use more of, like a protocol Stub based approach to verify interactions with that networking library, if that makes sense.

Speaker B
Got you. Yeah.

Speaker A
So our applications test use a stubbed out version of that network client to verify the application's interactions with that network client. But then we test the actual network client with Ohhttp Stubs just to verify end to end that requests show up on the network in the correct priority order and things like that.

Speaker B
Got you. So you don't test the prioritization directly? You test it sort of indirectly through the fact that it hit the network at the right times, basically.

Speaker A
Yeah.

Speaker B
Interesting. Yeah. The prioritization stuff is interesting, too, because I feel like the rules for prioritization are often very blurry and very like, well, we kind of just see what happens. You have to set up a policy for that. So do you always do the high priority ones before? Do you do some high priority ones and then some low priority ones and then back to high priority, or however you want to balance it?

Speaker A
Yeah, there's a lot to consider there if you're actually building this out.

Speaker B
Yeah, for sure.

Speaker A
While we're talking about Ohhttp Stubs, I do want to mention a few caveats that you have to be aware of if you're using that, which aren't because of that library, which is really great, but because of limitations in Nsurl protocol, which it uses under the hood. That's the Apple Core Networking API that it uses. You can't use this to test to test requests on background URL sessions because those happen out of process and so your process can't inject a new URL protocol for those.

Speaker B
Right.

Speaker A
And you also can I guess this isn't so much a limitation with Ohhtttp Stubs, because I don't know when this would come up. But that same limitation applies with Wk WebView. Like, with an older UI WebView that ran in your process, you could use that same Nscrl protocol API to intercept requests. And you can't do that with Wk WebView anymore, right?

Speaker B
Because it's just happening in a totally different place that you don't have access to.

Speaker A
Right. Yeah. So some things to be aware of, by and large, that http stubbing library does work out pretty well. All right, well, I don't think I really have anything else to add. This seems like there are basically two approaches to testing the networking part of your app, and I feel like we've talked enough about them.

Speaker B
Yeah, for sure. Yeah. Basically, either check it at the network level or check it at the URL session level. That's pretty much it.

Speaker A
Right? And we'll add a link to the show notes about creating a protocol that shadows NSRL session, which you can refer to.

Speaker B
Cool. Great.

Speaker A
That's all I've got. Sweet as always. It's been fun.

Speaker B
Serous yes. And thanks, listeners. And I'll talk to you next week. Turn.

