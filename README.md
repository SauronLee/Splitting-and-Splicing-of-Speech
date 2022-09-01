# Triple-S: Splitting and Splicing of Speech  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Tiog2nW4cLNg5bYG15C9imzzaYN_8m2n?usp=sharing)

This repository contains code and models for the poster: [wav2vecモデルによる方言音声資料のテキスト化 (LRW2022)](https://clrd.ninjal.ac.jp/lrw2022-programme-c.html). 

- We propose **Splitting and Splicing of Speech (Triple-S)** Method for **Speech Recognition**, Triple-S can improve the recognition of multi-speaker conversations. 

<p align="center">
<img src=main_illustration.png width=800/>
</p>

## 学習済みデータ

[t9.zip](https://drive.google.com/file/d/1KzrC1mQo2XVtVOrHpwbaWDQlOWYzxr1N/view?usp=sharing)

[t10.zip](https://drive.google.com/file/d/18zBbNjhFJC8SJugSR-_Yi2k-2y0Na8vy/view?usp=sharing)

```
📦t9                         #T9 data
┣ 📂2_speakers               #Speech separation based on two speakers
┃ ┣ 📂clean                 #Ambient sound not included (The result of the "noisy" file after noise suppression.)
┃ ┃ ┣ 📜c_s_0_1.wav          #speaker_1
┃ ┃ ┣ 📜c_s_0_2.wav          #speaker_2
┃ ┃ ┣ ...
┃ ┃ ┣ 📜c_s_370_1.wav        #speaker_1
┃ ┃ ┗ 📜c_s_370_1.wav        #speaker_2
┃ ┣ 📂noisy                  #Contains ambient sound (original sound)
┃ ┃ ┣ 📜s_0_1.wav            #speaker_1
┃ ┃ ┣ 📜s_0_2.wav            #speaker_2
┃ ┃ ┣ ...
┃ ┃ ┣ 📜s_370_1.wav          #speaker_1
┃ ┗ ┗ 📜s_370_1.wav          #speaker_2
┣ 📂3_speakers               #Speech separation based on three speakers
┃ ┣ 📂clean
┃ ┃ ┣ 📜c_s_0_1.wav          #speaker_1
┃ ┃ ┣ 📜c_s_0_2.wav          #speaker_2
┃ ┃ ┣ 📜c_s_0_3.wav          #speaker_3
┃ ┃ ┣ ...
┃ ┃ ┣ 📜c_s_370_1.wav        #speaker_1
┃ ┃ ┣ 📜c_s_370_2.wav        #speaker_2
┃ ┃ ┗ 📜c_s_370_3.wav        #speaker_3
┃ ┣ 📂noisy
┃ ┃ ┣ 📜s_0_1.wav            #speaker_1
┃ ┃ ┣ 📜s_0_2.wav            #speaker_2
┃ ┃ ┣ 📜s_0_3.wav            #speaker_3
┃ ┃ ┣ ...
┃ ┃ ┣ 📜s_370_1.wav          #speaker_1
┃ ┃ ┣ 📜s_370_2.wav          #speaker_2
┃ ┗ ┗ 📜s_370_3.wav          #speaker_3
┣ 1.wav                      #raw data (mix)
┣ 2.wav
┣ ...
┗ 370.wav
 
 
📦t10                        #T10 data
┣ 📂2_speakers
┃ ┣ 📂clean
┃ ┃ ┣ 📜c_s_0_1.wav
┃ ┃ ┣ 📜c_s_0_2.wav
┃ ┃ ┣ ...
┃ ┃ ┣ 📜c_s_370_1.wav
┃ ┃ ┗ 📜c_s_370_1.wav
┃ ┣ 📂noisy
┃ ┃ ┣ 📜s_0_1.wav
┃ ┃ ┣ 📜s_0_2.wav
┃ ┃ ┣ ...
┃ ┃ ┣ 📜s_370_1.wav
┃ ┗ ┗ 📜s_370_1.wav
┣ 📂3_speakers
┃ ┣ 📂clean
┃ ┃ ┣ 📜c_s_0_1.wav
┃ ┃ ┣ 📜c_s_0_2.wav
┃ ┃ ┣ 📜c_s_0_3.wav
┃ ┃ ┣ ...
┃ ┃ ┣ 📜c_s_370_1.wav
┃ ┃ ┣ 📜c_s_370_2.wav
┃ ┃ ┗ 📜c_s_370_3.wav
┃ ┣ 📂noisy
┃ ┃ ┣ 📜s_0_1.wav
┃ ┃ ┣ 📜s_0_2.wav
┃ ┃ ┣ 📜s_0_3.wav
┃ ┃ ┣ ...
┃ ┃ ┣ 📜s_370_1.wav
┃ ┃ ┣ 📜s_370_2.wav
┃ ┗ ┗ 📜s_370_3.wav
┣ 1.wav                      #raw data (mix)
┣ 2.wav
┣ ...
┗ 370.wav
```


## Requirements

- torch
- tqdm
- transformers
- nltk
- scikit-learn
- huggingsound
- pydub
- speechbrain
- torchaudio

## Development

```shell
# for speechbrain
pip install -qq torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 torchtext==0.12.0
pip install -qq speechbrain==0.5.12

# pyannote.audio
pip install -qq https://github.com/pyannote/pyannote-audio/archive/develop.zip

# for visualization purposes
pip install -qq moviepy ipython==7.34.0

# other
pip install huggingsound
pip install pydub
pip install transformers
```

## Introduction
### instantiate pretrained speaker diarization pipeline
```python
from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
import shutil
from pydub import AudioSegment
import os
speakers_dict = {}
with open("t10_test.txt","r") as f:
    for line in f:
        id = line.split("\t")[0]
        speakers_list = line.split("\t")[1].strip().split(" ||| ")
        speakers_dict[id] = speakers_list

if len(speakers_dict) != 30:
    print("error!")
for id, sentences in speakers_dict.items():

    short_list = []

    cut_list_1 = []
    filename_1 = "./data/t10_test/"+ str(id) +"_1.wav"   
    wav_1 = AudioSegment.from_wav(filename_1)

    diarization = pipeline(filename_1)
    for j, (turn, _, _) in enumerate(diarization.itertracks(yield_label=True)):
        cut_list_1.append([turn.start,turn.end])
    for cut_time in cut_list_1:
        short_list.append(cut_time[0])
        wav_1[cut_time[0]*1000 : cut_time[1]*1000].export("./segment/"+ str(cut_time[0]) +".wav")
    #-------------------------------------
    cut_list_2 = []
    filename_2 = "./data/t10_test/"+ str(id) +"_2.wav"
    wav_2 = AudioSegment.from_wav(filename_2)
    diarization = pipeline(filename_2)
    for j, (turn, _, _) in enumerate(diarization.itertracks(yield_label=True)):
        cut_list_2.append([turn.start,turn.end])
    for cut_time in cut_list_2:
        short_list.append(cut_time[0])
        wav_2[cut_time[0]*1000 : cut_time[1]*1000].export("./segment/"+ str(cut_time[0]) +".wav")
    #-------------------------------------
    short_list = sorted(short_list)

    output = AudioSegment.from_file("./segment/"+str(short_list[0])+".wav")
    for time_name in short_list[1:]:
      output += AudioSegment.from_file("./segment/"+str(time_name)+".wav")
    output.export("./t10_c/"+str(id)+".wav", format="wav")
    shutil.rmtree('./segment')  
    os.mkdir('./segment')  
```

### For Separation
```python
from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio
from tqdm import tqdm
model = separator.from_hparams(source="speechbrain/sepformer-whamr16k", savedir='pretrained_models/sepformer-whamr16k')
for i in tqdm([w for w in range(371)]):
    est_sources = model.separate_file(path="t10/"+ str(i) +".wav")
    torchaudio.save("t10_sep2_16k/"+ str(i) +"_1.wav", est_sources[:, :, 0].detach().cpu(), 16000)
    torchaudio.save("t10_sep2_16k/"+ str(i) +"_2.wav", est_sources[:, :, 1].detach().cpu(), 16000)
```

### For Evaluation
```python
from huggingsound import SpeechRecognitionModel
model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-japanese")
speakers_dict = {}
with open("t9_test.txt","r") as f:
    for line in f:
        id = line.split("\t")[0]
        speakers_list = line.split("\t")[1].strip().split(" ||| ")
        speakers_dict[id] = speakers_list
if len(speakers_dict) != 30:
    print("error!")
references = []
for id, sentences in speakers_dict.items():
    references.append({
        "path": "./t09/"+ id +".wav",
        "transcription": " ".join(sentences)
    })
evaluation = model.evaluate(references)
```

# speech_separation_japanese
 
