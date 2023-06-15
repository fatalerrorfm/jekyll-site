import json

with open(f"./episode_list.json", "r") as f:
    episodes = json.load(f)

def speaker(id, episode):
    if episode["speaker_count"] == 2:
        if first_speaker_is_chris(episode) and id == "A" or not first_speaker_is_chris(episode) and id == "B":
            return "Chris Dzombak"
        else:
            return "Soroush Khanlou"
    else:
        return f"Speaker {id}"

def first_speaker_is_chris(episode):
    chris_first_eps = [
#         "314582 175-fatalerrorfm-episode-23-objective-c-vs-swift.mp3",
#         "66._Sequence_and_Collection_and_Iterator_Oh_My.mp3",
        "E29+-+Protocols+with+Associated+Types.mp3",
        "E35+-+The+Ownership+Manifesto.mp3",
        "E51_Aftershow.mp3",
#         "Ep+68+-+Teaser.mp3",
#         "Ep_68_-Negotiating.mp3",
        "Episde+45+-+Fault+Tolerance+with+Actors.mp3",
        "Episode 12 - Swift 3 Migration.mp3",
        "Episode+10+-+Why+This+All+Matters.mp3",
        "Episode+11+-+Codegen.mp3",
        "Episode+13+-+The+Law+of+ Demeter.mp3",
#         "Episode+15+-+Not+Invented+Here.mp3",
        "Episode+17+-+Testing+Network+Layers.mp3",
        "Episode+19+-+Playgrounds+Conference.mp3",
#         "Episode+2+-+View+Models.mp3",
        "Episode+21+-+Try%21+Swift+Tokyo.mp3",
#         "Episode+25+-+Erica+and+Sara.mp3",
#         "Episode+26+-+Persistence+%28Teaser%29.mp3",
#         "Episode+27+-+Core+Data.mp3",
#         "Episode+28+-+The+String+Manifesto+Teaser.mp3",
#         "Episode+3+-+View+Models%2C+Again.mp3",
#         "Episode+31+-+Swift+4.mp3",
#         "Episode+32+-+Getting+Started+in+a+New+Codebase+Teaser.mp3",
        "Episode+33+-+Server-side+Swift+in+Practice.mp3",
#         "Episode+34+-+Promises+%E2%80%A6%C2%A0in+Objective-C+Teaser.mp3",
        "Episode+36+-+Conferences+%26+Talks+%28%26+Blogging%29+Teaser.mp3",
        "Episode+37+-+Soroush%E2%80%99s+Swift+Evolution+Proposal.mp3",
        "Episode+38+-+Third-Party+Dependencies+Teaser.mp3",
#         "Episode+39+-+Our+First+Apps.mp3",
        "Episode+4+-+Promises.mp3",
        "Episode+40+-+Async-Await+Teaser.mp3",
#         "Episode+41+-+Talking+Swift-Evolution+with+Kelvin.mp3",
        "Episode+42+-+Actors+Teaser.mp3",
#         "Episode+43+-+Jason+Brennan+on+Beach.mp3",
        "Episode+44+-+Grab+Bag+Teaser.mp3",
#         "Episode+46+-+Reflecting+on+Swift+and+Objective-C+Teaser.mp3",
        "Episode+47+-+Strange+Loop.mp3",
#         "Episode+48+-+Productivity+Teaser.mp3",
#         "Episode+49+-+Chris+Writes+Python.mp3",
        "Episode+5+-+Reactive+Programming.mp3",
#         "Episode+50+-+Internet+of+Things+Teaser.mp3",
        "Episode+51+-+Ticks+and+Trips.mp3",
#         "Episode+52+-+Spooked+about+Spectre+Teaser.mp3",
        "Episode+53+-+Android.mp3",
#         "Episode+54+-+Ecstatic+about+Enums+Teaser.mp3",
#         "Episode+55_+Fired+Up+about+Firebase.mp3",
#         "Episode+56+-+A+Chris+Shaped+Scream+Teaser.mp3",
#         "Episode+57+-+Lattnerianly+In-Depth.mp3",
#         "Episode+58+-+Pi%2C+Delicious+Pi+Teaser.mp3",
        "Episode+59+-+Why+did+they+even+hire+Chris_.mp3",
#         "Episode+6+-+Singletons.mp3",
#         "Episode+60+-+Soroush+in+the+Standard+Library+Teaser.mp3",
        "Episode+61+-+Hypothetical+Testing+Tricks.mp3",
#         "Episode+62+-+Convergent+Swift+Evolution+Teaser.mp3",
#         "Episode+63+-+Two+People+Who+Like+Type+Systems.mp3",
#         "Episode+64+-+AI+Apoptosis+Teaser.mp3",
        "Episode+65+-+Times+That+Do+Not+Exist.mp3",
        "Episode+66+-+Teaser.mp3",
#         "Episode+67+-+The+Whatever+Planet+From+The+Sun.mp3",
#         "Episode+69+-+null.mp3",
        "Episode+7+-+The+Single+Responsibility+Principle.mp3",
        "Episode+70+-+teaser.mp3",
        "Episode+8+-+Domain-Driven+Design.mp3",
#         "Episode+9+-+Getting+Started+with+Testing.mp3",
        "Episode_14_-_Tests_and_Types.mp3",
#         "Episode_16_-_Swifty_Error_Handling.mp3",
        "Episode_18_-_Code_Review.mp3",
#         "Episode_20_-_Simple_Made_Easy.mp3",
        "Episode_22_-_Optional_Properties.mp3",
        "Episode_24_-_Fileprivate.mp3",
#         "Episode_26_-_Persistence.mp3",
#         "Episode_28_-_The_String_Manifesto.mp3",
        "Episode_30_-_Server-Side_Swift.mp3",
#         "Episode_32_-_Getting_Started_in_a_New_Codebase.mp3",
        "Episode_34_-_Promises_..._in_Objective-C.mp3",
        "Episode_36_-_Conferences__Talks__Blogging.mp3",
#         "Episode_38_-_Third-Party_Dependencies.mp3",
        "Episode_40_-_Async-Await.mp3",
#         "Episode_42.5_Apple_Event_2.mp3",
        "Episode_42_-_Actors.mp3",
#         "Episode_44_-_Grab_Bag.mp3",
#         "Episode_46_-_Reflecting_on_Swift_and_Objective-C.mp3",
        "Episode_48_-_Productivity.mp3",
#         "Episode_50_-_Internet_of_Things.mp3",
#         "Episode_52_-_Spooked_about_Spectre.mp3",
        "Episode_54_-_Ecstatic_about_Enums.mp3",
        "Episode_56_-_A_Chris_Shaped_Scream.mp3",
#         "Episode_58_-_Pi_Delicious_Pi.mp3",
        "Episode_60_-_Soroush_in_the_Standard_Library.mp3",
#         "Episode_62_-_Convergent_Swift_Evolution.mp3",
        "Episode_64_-_AI_Apoptosis.mp3",
        "Episode_70_The_Finale.mp3",
        "Fatal+Error+-+Episode+1.mp3",
     ]
    return episode["filename"] in chris_first_eps

for episode in episodes:
    filename = episode["filename"]
    print(f"Doing {filename}")
    
    transcript = []
    
    with open(f"./transcripts_json/{filename}.json", "r") as f:
        data = json.load(f)
        
    for utterance in data["utterances"]:
        speaker_id = utterance["speaker"]
        speaker_name = speaker(speaker_id, episode)
        transcript.append(f"{speaker_name}")
        transcript.append("\n")
        transcript.append(utterance["text"])
        transcript.append("\n")
        transcript.append("\n")


    transcript_string = "".join(transcript)

    with open(f"./transcripts_md/{filename}.md", "w") as outfile:
       outfile.write(transcript_string)
