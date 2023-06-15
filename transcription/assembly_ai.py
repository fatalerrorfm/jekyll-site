import requests
import json
import time

base_url = "https://api.assemblyai.com/v2"

headers = {
    "authorization": "513f45417677479780ea2db749f01b46" 
}

with open(f"./episode_list.json", "r") as f:
    episodes = json.load(f)


for episode in episodes:
    print(f"Doing {episode.filename}")
    upload_url = f"https://fatalerror.fm/attachments/{episode.filename}" 

    data = {
        "audio_url": upload_url,
        "speaker_labels": True,
        "speakers_expected": episode.speaker_count,
    }

    url = base_url + "/transcript"
    response = requests.post(url, json=data, headers=headers)

    transcript_id = response.json()['id']
    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

    while True:
      transcription_result = requests.get(polling_endpoint, headers=headers).json()

      if transcription_result['status'] == 'completed':
        break

      elif transcription_result['status'] == 'error':
        raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

      else:
        time.sleep(3)
    
    print(polling_endpoint)

    # Serializing json
    json_object = json.dumps(transcription_result, indent=4)
 
    # Writing to sample.json
    with open(f"{filename}.json", "w") as outfile:
        outfile.write(json_object)
