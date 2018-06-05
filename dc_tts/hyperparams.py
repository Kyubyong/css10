# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com. 
https://www.github.com/kyubyong/multi-speech-corpora/dc_tts
'''
class Hyperparams:
    '''Hyper parameters'''
    lang = "hu"

    # pipeline
    prepro = True  # if True, run `python prepro.py` first before running `python train.py`.
    
    # signal processing
    sr = 22050  # Sampling rate.
    n_fft = 2048  # fft points (samples)
    frame_shift = 0.0125  # seconds
    frame_length = 0.05  # seconds
    hop_length = int(sr * frame_shift)  # samples. =276.
    win_length = int(sr * frame_length)  # samples. =1102.
    n_mels = 80  # Number of Mel banks to generate
    power = 1.5  # Exponent for amplifying the predicted magnitude
    n_iter = 50  # Number of inversion iterations
    preemphasis = .97
    max_db = 100
    ref_db = 20

    # Model
    r = 4 # Reduction factor. Do not change this.
    dropout_rate = 0.05
    e = 128 # == embedding
    d = 256 # == hidden units of Text2Mel
    c = 512 # == hidden units of SSRN
    attention_win_size = 3

    # data
    data = "/data/private/speech/{}".format(lang)
    test_data = "../MOS/sents/{}.txt".format(lang)
    if lang=="fr":
        vocab = u'''␀␃ !"',-.:;?AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzàâæçèéêëîïôùûœ–’'''  # ␀: Padding, ␃: End of Text
        max_N, max_T = 478, 684
    elif lang=="jp":
        vocab = u'''␀␃ '-abcdefghijkmnoprstuvwxyz―、。々？'''
        max_N, max_T = 251, 324
    elif lang=="zh":
        vocab = u'''␀␃ abcdefghijklmnopqrstuvwxyz·àáèéìíòóùúüāēěīōūǎǐǒǔǚǜ—、。！，－：；？'''
        max_N, max_T = 375, 496
    elif lang=="el":
        vocab = u'''␀␃ !',-.:;ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyzΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩάέήίαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώ'''
        max_N, max_T = 401, 534
    elif lang=="it":
        vocab = u'''␀␃ !',-.:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÈàèéìíîïòôù'''
        max_N, max_T = 324, 410
    elif lang=="nl":
        vocab = u'''␀␃ !',-.:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'''
        max_N, max_T = 393, 507
    elif lang=="ru":
        vocab = u'''␀␃ !',-.:;?êАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё—'''
        max_N, max_T = 569, 988
    elif lang=="fi":
        vocab = u'''␀␃ !',-.:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÄÖäéö'''
        max_N, max_T = 275, 449
    elif lang=="es":
        vocab = u'''␀␃ !',-.:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz¡¿ÁÅÉÍÓÚáæèéëíîñóöúü—'''
        max_N, max_T = 382, 522
    elif lang=="de":
        vocab = u'''␀␃ !',-.:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÄÖÜßàäéöü–'''
        max_N, max_T = 279, 435
    elif lang=="hu":
        vocab = u'''␀␃ !,-.:;?ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyzÁÉÍÓÖÚÜáéíóöúüŐőŰű'''
        max_N, max_T = 298, 427

    # max_N = 180 # Maximum number of characters.
    # max_T = 210 # Maximum number of mel frames.

    # training scheme
    lr = 0.001 # Initial learning rate.
    logdir = "{}/logdir".format(lang)
    sampledir = '{}/samples'.format(lang)
    B = 16 # batch size
    num_iterations = 400000
