Chris Dzombak
Ah, I can see like pros and cons for each of these. This is not we may not solve this tonight.

Soroush Khanlou
I don't know, Chris. I think if we do maybe another two or 3 hours of this podcast.

Chris Dzombak
I think we can get there. Welcome to failure.

Soroush Khanlou
Really tough.

Soroush Khanlou
Really tough problem.

Chris Dzombak
Yeah. Like I see an argument for sort of centralizing this failure logic at like a high level in the application, but then your application is going to have to track what things may be waiting on this actor and go deal with that. And number two, let me force more boilerplate. But also that means your application has to track less state potentially and understand and doesn't have to work backwards through its dependency graph when something crashes.

Soroush Khanlou
Right. And I feel like.

Chris Dzombak
There'S different kinds.

Soroush Khanlou
Of actors as well. I think the model of if you want your server to be responding to requests and spinning off a new actor, if you want to hear the rest of this episode and all of our even numbered episodes, you can subscribe to our Patreon. Subscribing to the Patreon gives you access to our entire back, catalog the rest of this episode and future private episodes. We use the money from the Patreon to pay for things like editing costs, hosting costs, and other incident holes. Our podcast is sponsored free and we'd really love to keep it that way. Details on how to become a supporter are in the show notes or you can visit Fatalairror FM.

