# CSS10: A Collection of Single Speaker Speech Datasets for 10 Languages

## Abstract
We describe our development of CSS10, a collection of single
speaker speech datasets for ten languages. It is composed of
short audio clips from LibriVox audiobooks and their aligned
texts. To validate its quality we train two neural text-to-speech
models on each dataset. Subsequently, we conduct Mean Opinion
Score tests on the synthesized speech samples. We make our
datasets, pretrained models, and test resources publicly available.
We hope they will be used for future speech tasks.

For details, check [this](css10.v.1.0.pdf).

## Environments & Dependencies

* Linux
* Python 2.X or 3.X
* TensorFlow == 1.3
* NumPy
* Librosa
* Matplotlib
* tqdm
* scipy

## Audiobooks & Datasets

|Code|Language|Audiobook|Running Time|Reader|Dataset|
|--|--|--|--|--|--|
|de|German|1. [Meister Floh](https://librivox.org/meister-floh-by-eta-hoffmann/) <br>2. [Die acht Gesichter am Biwasee](https://librivox.org/die-acht-gesichter-am-biwasee-by-max-dauthendey/) <br>3. [Auswahl aus Die Serapionsbrüder](https://librivox.org/die-serapionsbrueder-by-eta-hoffmann/)|16:42:45|Hokuspokus |[CSS German](http://kaggle.com/bryanpark/german-single-speaker-speech-dataset)|
|el|Greek|[Παραμύθι χωρίς όνομα (Tale Without Name)](https://librivox.org/paramythi-horis-onoma-by-penelope-delta/)|04:08:14| Rapunzelina|[CSS Greek](http://kaggle.com/bryanpark/greek-single-speaker-speech-dataset)|
|es|Spanish|1. [Bailén](https://librivox.org/bailen-by-benito-perez-galdos/) <br>2. [El 19 de Marzo y el 2 de Mayo](https://librivox.org/el-19-de-marzo-y-el-2-de-mayo-by-benito-perez-galdos/)<br>3. [La Batalla de los Arapiles](https://librivox.org/la-batalla-de-los-arapiles-by-benito-perez-galdos/)|23:49:49|Tux  |[CSS Spanish](http://kaggle.com/bryanpark/spanish-single-speaker-speech-dataset)|
|fi|Finnish|1. [Gulliverin matkat kaukaisilla mailla](https://librivox.org/gulliverin-matkat-kaukaisilla-mailla-by-jonathan-swift/) <br>2. [Ensimmäiset novellit](https://librivox.org/ensimmaeiset-novellit-by-juhani-aho/) <br>3. [Kaleri-orja](https://librivox.org/kaleri-orja-by-heinrich-zschokke/) <br>4. [Salmelan heinätalkoot](https://librivox.org/salmelan-heinaetalkoot-by-olli-wuorinen/)|10:32:03|Harri Tapani Ylilammi  |[CSS Finnish](http://kaggle.com/bryanpark/finnish-single-speaker-speech-dataset)|
|fr|French|1. [Les Misérables - tome 5 .](https://librivox.org/les-miserables-tome-5-jean-valjean-by-victor-hugo/)<br> 2. [Arsène Lupin contre Herlock Sholmès](https://librivox.org/arsene-lupin-contre-herlock-sholmes-by-maurice-leblanc/)|19:09:03|Gilles G. Le Blanc |[CSS French](http://kaggle.com/bryanpark/french-single-speaker-speech-dataset)|
|hu|Hungarian|[Egri csillagok](https://librivox.org/egri-csillagok-by-geza-gardonyi/)|10:00:25|   Diana Majlinger|[CSS Hungarian](http://kaggle.com/bryanpark/hungarian-single-speaker-speech-dataset)|
|ja|Japanese|[明暗 (Meian)](https://librivox.org/meian-by-soseki-natsume/)|14:55:36|ekzemplaro|[CSS Japanese](http://kaggle.com/bryanpark/japanese-single-speaker-speech-dataset)|
|nl|Dutch|[20.000 Mijlen onder Zee](https://librivox.org/20-000-mijlen-onder-zee-by-jules-verne/)|14:06:40|Bart de Leeuw  |[CSS Dutch](http://kaggle.com/bryanpark/dutch-single-speaker-speech-dataset)|
|ru|Russian|1. [Ice March - Ледяной поход](https://librivox.org/ice-march-by-roman-gul/)<br>2. [Early Short Stories](https://librivox.org/early-short-stories-by-zeev-jabotinsky/) <br>3. [Short Stories for Children and Adults](https://librivox.org/p-short-stories-for-children-and-adults-by-vsevolod-garshin/)|21:22:10 |Mark Chulsky|[CSS Russian](http://kaggle.com/bryanpark/russian-single-speaker-speech-dataset)|
|zh|Chinese|1. [朝花夕拾 (Chao Hua Si She))](https://librivox.org/chao-hua-si-she-by-lu-xun/)<bt>2. [呐喊 (Call to Arms)](https://librivox.org/call-to-arms-by-xun-lu/)|06:27:04|Jing Li |[CSS Chinese](http://kaggle.com/bryanpark/chinese-single-speaker-speech-dataset)|


## Pretrained Models & Audio Samples

|Code|Lanuage|Pretrained Models|Audio Samples|
|--|--|--|--|
|de|German|[DCTTS](https://www.dropbox.com/s/nfwv48bnovidnod/de_logdir.zip?dl=0) \| [TACOTRON](https://www.dropbox.com/s/81dt66qylfskw1g/de_logdir.zip?dl=0)|[DCTTS](https://soundcloud.com/kyubyong-park/sets/ms10_de_d) \| [TACOTRON](https://soundcloud.com/kyubyong-park/sets/ms10_de_t)|
|el|Greek|[DCTTS](https://www.dropbox.com/s/sd92n1k374p8fks/el_logdir.zip?dl=0)|[DCTTS](https://soundcloud.com/kyubyong-park/sets/ms10_el_d)|
|es|Spanish|[DCTTS](https://www.dropbox.com/s/1zpkojc8hvvkprx/es_logdir.zip?dl=0) \| [TACOTRON](https://www.dropbox.com/s/eyx8fztqulnhijr/es_logdir.zip?dl=0)|[DCTTS](https://soundcloud.com/kyubyong-park/sets/ms10_es_d) \| [TACOTRON](https://soundcloud.com/kyubyong-park/sets/ms10_es_t)|
|fi|Finnish|[DCTTS](https://www.dropbox.com/s/n6uiy9rdvfv6bpy/fi_logdir.zip?dl=0) \| [TACOTRON](https://www.dropbox.com/s/oqa36ixagwvrao3/fi_logdir.zip?dl=0)|[DCTTS](https://soundcloud.com/kyubyong-park/sets/ms10_fi_d) \| [TACOTRON](https://soundcloud.com/kyubyong-park/sets/ms10_nl_t)|
|fr|French|[DCTTS](https://www.dropbox.com/s/6zpcqzu6hbxg2eb/fr_logdir.zip?dl=0) \| [TACOTRON](https://www.dropbox.com/s/2vaa73jbjyhcfhl/fr_logdir.zip?dl=0)|[DCTTS](https://soundcloud.com/kyubyong-park/sets/ms10_fr_d) \| [TACOTRON](https://soundcloud.com/kyubyong-park/sets/ms10_fr_t)|
|hu|Hungarian|[DCTTS](https://www.dropbox.com/s/gtzzf79c351ovre/hu_logdir.zip?dl=0) \| [TACOTRON](https://www.dropbox.com/s/ogy6rqwirosf3mw/hu_logdir.zip?dl=0)|[DCTTS](https://soundcloud.com/kyubyong-park/sets/ms10_hu_d) \| [TACOTRON](https://soundcloud.com/kyubyong-park/sets/ms10_hu_t)|
|ja|Japanese|[DCTTS](https://www.dropbox.com/s/dkva7kc4r72pz3z/ja_logdir.zip?dl=0) \| [TACOTRON](https://www.dropbox.com/s/gh1wyfhnyf1j4fb/ja_logdir.zip?dl=0)|[DCTTS](https://soundcloud.com/kyubyong-park/sets/ms10_ja_d) \| [TACOTRON](https://soundcloud.com/kyubyong-park/sets/ms10_ja_t)|
|nl|Dutch|[DCTTS](https://www.dropbox.com/s/dgmx28zh82187cs/nl_logdir.zip?dl=0) \| [TACOTRON](https://www.dropbox.com/s/30l4xpt0xedd58n/nl_logdir.zip?dl=0)|[DCTTS](https://soundcloud.com/kyubyong-park/sets/ms10_nl_d) \| [TACOTRON](https://soundcloud.com/kyubyong-park/sets/ms10_nl_t)|
|ru|Russian|[DCTTS](https://www.dropbox.com/s/0u6q3mv2qhbgwei/ru_logdir.zip?dl=0) \| [TACOTRON](https://www.dropbox.com/s/mg5jv06p8ucwq6s/ru_logdir.zip?dl=0)|[DCTTS](https://soundcloud.com/kyubyong-park/sets/ms10_ru_d) \| [TACOTRON](https://soundcloud.com/kyubyong-park/sets/ms10_ru_t)|
|zh|Chinese|[DCTTS](https://www.dropbox.com/s/coy57a9ueenq9sk/zh_logdir.zip?dl=0) \| [TACOTRON](https://www.dropbox.com/s/7wf4hd73f4nc1dk/zh_logdir.zip?dl=0)|[DCTTS](https://soundcloud.com/kyubyong-park/sets/ms10_zh_d) \| [TACOTRON](https://soundcloud.com/kyubyong-park/sets/ms10_zh_t)|



By Kyubyong Park, Tommy Mulc
