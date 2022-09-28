from pypinyin import lazy_pinyin
zh_phrase_set = set()
en_phrase_set = set()
en_word_set = set()
with open("calculus.txt", "r") as src_file:
    for line in src_file.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        line = line.split(' ')
        zh_word, en_word = line[0], line[1:]

        en_word = ' '.join(en_word)
        zh_phrase_set.add(zh_word)
        en_phrase_set.add(en_word)
    src_file.close()
with open("../caculus.extended/calculus_zh.dict.yaml", "w") as dstZH:
    dstZH.write(
        "---\nname: calculus_zh\nversion: \"2021.10.13\"\nsort: by_weight\nuse_preset_vocabulary: true\n...\n\n")
    for zh_word in zh_phrase_set:
        zh_word = ''.join(filter(str.isalpha, zh_word))
        dstZH.write(zh_word +'\n')
        # zh_word_spell = ' '.join(lazy_pinyin(zh_word))
        # dstZH.write(zh_word + '\t' + zh_word_spell+'\n')
    dstZH.close()
with open("../caculus.extended/calculus_en_phrase.dict.yaml", "w") as dstENPhrase:
    dstENPhrase.write(
        "---\nname: calculus_en_phrase\nversion: \"2021.10.13\"\nsort: by_weight\nuse_preset_vocabulary: false\n...\n\n")
    for en_phrase_set in en_phrase_set:
        en_phrase_spell = ''.join(filter(str.isalpha, en_phrase_set))
        dstENPhrase.write(en_phrase_set+'\t'+en_phrase_spell+'\n')
        for en_word in en_phrase_set.split(' '):
            if en_word.find('-') != -1:
                for en_word_tmp in en_word.split('-'):
                    if str.isalpha(en_word_tmp):
                        continue
                    en_word_set.add(en_word_tmp.lower())
            else:
                en_word_set.add(en_word.lower())
    dstENPhrase.close()
with open("../caculus.extended/calculus_en_word.dict.yaml", "w") as dstENWord:
    dstENWord.write(
        "---\nname: calculus_en_word\nversion: \"2021.10.13\"\nsort: by_weight\nuse_preset_vocabulary: false\n...\n\n")
    for en_word in en_word_set:
        en_word_spell = ''.join(filter(str.isalpha, en_word))
        dstENWord.write(en_word+'\t'+en_word_spell+'\n')
    dstENWord.close()
