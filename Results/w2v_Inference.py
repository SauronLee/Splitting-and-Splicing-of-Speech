from huggingsound import SpeechRecognitionModel
import re
from datasets import load_metric
wer = load_metric("wer.py") # https://github.com/jonatasgrosman/wav2vec2-sprint/blob/main/wer.py
cer = load_metric("cer.py") # https://github.com/jonatasgrosman/wav2vec2-sprint/blob/main/cer.py

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-japanese")

DATA = "t9"
CHARS_TO_IGNORE = [",", "?", "¿", ".", "!", "¡", ";", "；", ":", '""', "%", '"', "�", "ʿ", "·", "჻", "~", "՞", " ",
                   "؟", "،", "।", "॥", "«", "»", "„", "“", "”", "「", "」", "‘", "’", "《", "》", "(", ")", "[", "]",
                   "{", "}", "=", "`", "_", "+", "<", ">", "…", "–", "°", "´", "ʾ", "‹", "›", "©", "®", "—", "→", "。",
                   "、", "﹂", "﹁", "‧", "～", "﹏", "，", "｛", "｝", "（", "）", "［", "］", "【", "】", "‥", "〽",
                   "『", "』", "〝", "〟", "⟨", "⟩", "〜", "：", "！", "？", "♪", "؛", "/", "\\", "º", "−", "^", "'", "ʻ", "ˆ"]

chars_to_ignore_regex = f"[{re.escape(''.join(CHARS_TO_IGNORE))}]"
speakers_dict = {}
with open(DATA+"_test.txt","r") as f:
    for line in f:
        id = line.split("\t")[0]
        speakers_list = line.split("\t")[1].strip().split(" ||| ")
        speakers_dict[id] = speakers_list

if len(speakers_dict) != 30: print("error!")
wav_list = []
wav_list_c = []
refer_list = []
#evaluation_data = []
#evaluation_data_c = []

for id, sentences in speakers_dict.items():
    wav_list_c.append("./"+DATA+"_c/"+ id +".wav")
    wav_list.append("./"+DATA+"/" + id + ".wav")
    refer_list.append(re.sub(chars_to_ignore_regex, "", "".join(sentences)))
    #evaluation_data.append({
    #    "path": "./"+DATA+"/"+ id +".wav",
    #    "transcription": re.sub(chars_to_ignore_regex, "", "".join(sentences))
    #})
    #evaluation_data_c.append({
    #    "path": "./"+DATA+"_c/"+ id +".wav",
    #    "transcription": re.sub(chars_to_ignore_regex, "", "".join(sentences))
    #})
transcriptions = model.transcribe(wav_list)
transcriptions_c = model.transcribe(wav_list_c)

#evaluation_data_c = model.evaluate(evaluation_data_c)
#evaluation_data = model.evaluate(evaluation_data)
transcriptions = [s["transcription"] for s in transcriptions]
transcriptions_c = [s["transcription"] for s in transcriptions_c]


predictions_c = [x.upper() for x in transcriptions_c]
predictions = [x.upper() for x in transcriptions]
references = [x.upper() for x in refer_list]

#print("Raw")
#print(f"WER: {wer.compute(predictions=predictions, references=references, chunk_size=1000) * 100}")
#print(f"CER: {cer.compute(predictions=predictions, references=references, chunk_size=1000) * 100}")
#print("Concat")
#print(f"WER: {wer.compute(predictions=predictions_c, references=references, chunk_size=1000) * 100}")
#print(f"CER: {cer.compute(predictions=predictions_c, references=references, chunk_size=1000) * 100}")

#with open("transcriptions_"+DATA+"","w") as f:
#    for i, (id, _ ) in enumerate(speakers_dict.items()):
#        f.write("Id:"+ id +"\tConcat:\t" + transcriptions_c[i] + "\n")
#        f.write("Id:" + id + "\tRaw:\t" + transcriptions[i] + "\n")
#        f.write("Id:" + id + "\tGroundtruth:\t" + raw_text[i] + "\n")
    #f.write("\n")
    #f.write("Concat\twer:" + str(evaluation_data_c["wer"]) + "\tcer:" + str(evaluation_data_c["cer"]) + "\n")
    #f.write("Raw\twer:" + str(evaluation_data["wer"]) + "\tcer:" + str(evaluation_data["cer"]) + "\n")

with open("./pretrained_models/concat_"+DATA+".txt","w") as f:
    for i, (id, _ ) in enumerate(speakers_dict.items()):
        f.write(transcriptions_c[i] + "\n")
with open("./pretrained_models/raw_" + DATA +".txt", "w") as f:
    for i, (id, _) in enumerate(speakers_dict.items()):
        f.write(transcriptions[i] + "\n")
with open("./pretrained_models/target_" + DATA +".txt", "w") as f:
    for i, (id, _) in enumerate(speakers_dict.items()):
        f.write(refer_list[i] + "\n")


#wer concat t10
#word_error_total/words_total
#1018 / 1030 = 0.9883495145631068


#wer raw t10
#word_error_total/words_total
#852 / 862 = 0.988399071925754


# cer concat t10
#総文字数:1076  総誤り文字数:995  文字誤り率:0.9247211895910781

# cer raw t10
#総文字数:1247  総誤り文字数:1031  文字誤り率:0.8267842822774659

#wer concat t9
#word_error_total/words_total
#1051 / 1091 = 0.9633363886342805

#wer raw t9
#word_error_total/words_total
#824 / 851 = 0.9682726204465335

# cer raw t9
#総文字数:1186  総誤り文字数:1036  文字誤り率:0.8735244519392917

# cer concat t9
#総文字数:1558  総誤り文字数:1531  文字誤り率:0.9826700898587933
