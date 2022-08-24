## ファイル説明

* [予測時の文あたりのWER（T9_concat）](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/concat_wer_t9.txt)
* [予測時の文あたりのCER（T10_concat）](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/concat_cer_t10.txt)
* [予測時の文あたりのWER（T9_raw）](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/raw_wer_t9.txt)
* [予測時の文あたりのCER（T10_raw）](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/raw_cer_t10.txt)
* [Targetファイル（T9）](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/target_t9.txt)
* [Targetファイル（T10）](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/target_t10.txt)
* [concat音声で認識した文（T9）](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/concat_t9.txt)
* [raw音声で認識した文（T9）](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/raw_t9.txt)
* [concat音声で認識した文（T10）](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/concat_t10.txt)
* [raw音声で認識した文（T10）](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/raw_t10.txt)
* [評価方法](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/w2v_Inference.py)
----
updata: 2022.8.24
* [音素CER(T10_concat)](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/phone_concat_t10_cer.txt)
* [音素CER(T9_concat)](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/phone_concat_t9_cer.txt)
* [音素CER(T10_raw)](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/phone_raw_t10_cer.txt)
* [音素CER(T9_raw)](https://github.com/SauronLee/Splitting-and-Splicing-of-Speech/blob/main/Results/phone_raw_t9_cer.txt)

## 結果
### WER & CER
| metrics | concat_t9 | raw_t9   | concat_t10 | raw_t10   |
|---------|-----------|----------|------------|----------|
| WER     | 0.963336  | 0.968272 | 0.988349   | 0.988399 |
| CER     | 0.982670  | 0.873524 | 0.924721   | 0.826784 |
| CER_phone     | 0.952380  | 0.840811 | 0.892825   | 0.690177 |

## 予測の例
### T9
| Id | Concat                                                                                                                                                                                                                     | Raw                                                                                                | Target                                                               |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| 13 | 鉄との乱行へでって回にむララった力くの名行へでっ回にむクラった努力くカーデラートのマーガンアの末プエ・グライウアるあ乾駅ってっだあ駅でって                                                                                 | なん清子の面行で千暴でくる虚ねこ惑くばがるパーデアーーツマプェー・ヴィア上あるあや単駅でっよ       | そいで外の向こうでからねうんありゃあそのきつねであれたぬきですよ     |
| 17 | 国薬のごなめ天網撃駅なとってにまった持とぼて局薬分ななめ天皇をきとってになったとてぼえてブール                                                                                                                             | 住力でけの飲みをノボートモたけの幕はこぼたらデモルゴスロットをもだ                                 | こうもろこし畑ん中もろこしを食うもんだうんうん                       |
| 22 | ーーとマップやトッパートむ弾洗イタってっけったあーン古んだっくッルのが一ってマバーウとパイぴやちッパーむ今う玉イドタって見っっあローンの門っポップルルの行一ってどのカポカって行ってったあーン古面だっホっぺルの行が一って | ア荒とプラネトトョフターツ人はぶ今本もママノラーブッタといるくオ飲も古リバムとれずトに数のんと上ろ | あれはその種ってやつを2つああそううん必ず2つ入れてさありゃだもんだで |
| 25 | あがらでよむね花はぶったってね                                                                                                                                                                                             | はどうでをな構はぐプさといむる                                                                     | 必ず2ついるね                                                        |

### T10

| Id | Concat                                                                                 | Raw                                                                            | Target                                                           |
|----|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------|
| 13 | ええタロはやウタンロとノ悪学から運間であれてくも一ててるラゲ屋で酒店ア領ー夜ア良いガよ | ええイカのからふノラが飲まれたくだねぼってててて洗剣がねえブランチアゆいくあろ | え井川の生まれ井川生まれどこじゃないだけえがねわしゃあ井川の     |
| 17 | のとのの声度半ぎア枚へラ店を休に多量を漁を買っく彼歌らってえた牛五二三だ王が           | 花卵品のカディー依なへ抱もなる度に牛を建きのこの二歌はふって夕束類ボンーンは   | 話の限りはないだけえがふんとに昔のこの井川ってゆうとかぁ随分まあ |
| 22 | 大映があわすゆってい色の和校をくくってルへかいのリオルー霊はハ手であ歩っ手いな気がよう | オ映枝はとビってい夢のが大ーピくてねったの乳牛はハぴりあ歩っぴいまで何         | 大井川筋ってゆうのは大きくてねあの48里あるって言いますがね       |
| 25 | ので切ってゆれて覚ったライなののが消いたさわ                                           | 冬四名ぴって入れてどのっと海難歩夏でてべててべる                               | ってゆうのね切って入れてずっと買い出したんです                   |
