# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com. 
https://www.github.com/kyubyong/tacotron
'''
class Hyperparams:
    '''Hyper parameters'''
    
    # pipeline
    lang = 'fr'

    prepro = True  # if True, run `python prepro.py` first before running `python train.py`.
    
    # ␀: Padding ␃: End of Sentence
    if lang == 'fr':
        vocab = u'''␀␃ !"',-.:;?AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzàâæçèéêëîïôùûœ–’'''
    if lang == 'it':
        vocab = u'''␀␃ !',-.:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÈàèéìíîïòôù'''
    if lang == 'nl':
        vocab = u'''␀␃ !',-.:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'''
    if lang == 'el':
        vocab = u'''␀␃ !',-.:;ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyzΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩάέήίαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώ'''
    if lang == 'de':
        vocab = u'''␀␃ !',-.:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÄÖÜßàäéöü–'''
    if lang == 'es':
        vocab = u'''␀␃ !',-.:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz¡¿ÁÅÉÍÓÚáæèéëíîñóöúü—'''
    if lang == 'fi':
        vocab = u'''␀␃ !',-.:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÄÖäéö'''
    if lang == 'ru':
        vocab = u'''␀␃ !',-.:;?êАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё—'''
    if lang == 'zh':
        vocab = u'''␀␃ abcdefghijklmnopqrstuvwxyz·àáèéìíòóùúüāēěīōūǎǐǒǔǚǜ—、。！，－：；？'''
    if lang == 'jp':
        vocab = None
    #vocab = "PE abcdefghijklmnopqrstuvwxyz'.?" # P: Padding E: End of Sentence

    # data
    #data = "fr/"
    #data = "../data/{}".format(lang)
    data = "/data/public/rw/speech/{}".format(lang)
    #data = "/data/private/voice/LJSpeech-1.0"
    #test_data = 'harvard_sentences.txt'
    test_data = '../MOS/sents/{}.txt'.format(lang)
    max_duration = 10.0

    # signal processing
    sr = 22050 # Sample rate.
    n_fft = 2048 # fft points (samples)
    frame_shift = 0.0125 # seconds
    frame_length = 0.05 # seconds
    hop_length = int(sr*frame_shift) # samples.
    win_length = int(sr*frame_length) # samples.
    n_mels = 80 # Number of Mel banks to generate
    power = 1.2 # Exponent for amplifying the predicted magnitude
    n_iter = 50 # Number of inversion iterations
    preemphasis = .97 # or None
    max_db = 100
    ref_db = 20

    # model
    embed_size = 256 # alias = E
    encoder_num_banks = 16
    decoder_num_banks = 8
    num_highwaynet_blocks = 4
    r = 5 # Reduction factor. Paper => 2, 3, 5
    dropout_rate = .5

    # training scheme
    lr = 0.001 # Initial learning rate.
    logdir = "{}/logdir".format(lang)
    sampledir = '{}/samples'.format(lang)
    batch_size = 32
    num_iterations = 400000

    # synth scheme
    syn_logdir = "logdir_{}".format(lang)
    EOS_char = '␃'




