import random

text = "qwertyuiopasdfghjklzxcvbnm"

yozuv = [

    "🆀🆆🅴🆁🆃🆈🆄🅸🅾🅿🅰🆂🅳🅵🅶🅷🅹🅺🅻🆉🆇🅲🆅🅱🅽🅼",  #1
     "ɋաɛʀȶʏʊɨօքǟֆɖʄɢɦʝӄʟʐӼƈʋɮռʍ",
    "Ⴓᗯᕮᖇ丅ϤႮᎥѺᎮᗩᔕᕲҒᏀᎻᎫᏦᏞᏃᏃᎭᏉᏰᏁᎷ"
     "𝚚ω𝒆𝓻𝓽ƴ𝑢¡⊙𝖕ⲁ𝚜đꊰġĥⓙҜ𝚕𝘻xc𝚟ᵦח",  
    "𝓆𝓌𝑒𝓇𝓉𝓎𝓊𝒾𝑜𝓅𝒶𝓈𝒹𝒻𝑔𝒽𝒿𝓀𝓁𝓏𝓍𝒸𝓋𝒷𝓃𝓂",  
    "𝓠𝓦𝓔𝓡𝓣𝓨𝓤𝓘𝓞𝓟𝓐𝓢𝓓𝓕𝓖𝓗𝓙𝓚𝓛𝓩𝓧𝓒𝓥𝓑𝓝𝓜",  
    "𝕼𝖂𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒",   
    "𝑄𝑊𝐸𝑅𝑇𝒴𝒰𝐼𝒪𝒫𝒜𝒮𝒟𝑭𝑮𝑯𝑱𝒦𝑳𝒵𝒳𝑪𝒱𝒷𝒩𝑴",  
    "𝐐𝐖𝐄𝐑𝐓𝐘𝐔𝐈𝐎𝐏𝐀𝐒𝐃𝐅𝐆𝐇𝐉𝐊𝐋𝐌", 
    "🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼",  
    "ⓠⓦⓔⓡⓣⓨⓤⓘⓞⓟⓐⓢⓓⓕⓖⓗⓙⓚⓛⓩⓧⓒⓥⓑⓝⓜ",  
    "🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟🅐🅢🅓🅕🅖🅗🅙🅚🅛🅩🅧🅒🅥🅑🅝🅜",  
    # "𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒",   
    # "🅢🅘🅜🅑🅞🅛🅢",  
    "𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪",   #15  
    "𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞",  
    # "𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶", #17
    # "×º°”˜`”°º×",
    "𝑄𝑊𝐸𝑅𝑇𝑌𝑈𝐼𝑂𝑃𝐴𝑆𝐷𝐹𝐺𝐻𝐽𝐾𝐿𝑍𝑋𝐶𝑉𝐵𝑁𝑀",
     "Ɋᗯᗴᖇ丅ƳᑌᎥᗝᑭᗩᔕᗪᖴǤᕼᒎᛕᒪ乙᙭ᑕᐯᗷᑎᗰ",
     "QŴĔŔŤŶÚĨŐРĂŚĎŦĞĤĴĶĹŹЖČVβŃМ",
    "𝑞𝑤𝑒𝑟𝑡𝑦𝑢𝑖𝑜𝑝𝑎𝑠𝑑𝑓𝑔𝑕𝑗𝑘𝑙𝑧𝑥𝑐𝑣𝑏𝑛𝑚", 
    # "🅢🅘🅜🅑🅞🅛🅢",   
    'ợฬєгՇץยเ๏קคร๔Ŧﻮђןкɭչאςש๒ภ๓',
    "qʷᵉʳᵗʸᵘⁱᵒᵖᵃˢᵈᶠᵍʰʲᵏˡᶻˣᶜᵛᵇⁿᵐ",
    "qЩΣЯƬyЦiӨpΛƧdfgΉjkᄂzxᄃvbПm",
    "Ɋ山乇尺ㄒㄚㄩ丨ㄖ卩卂丂ᗪ千Ꮆ卄ﾌҜㄥ乙乂匚ᐯ乃几爪", 
    "ꆰꅐꏂꋪ꓄ꌦ꒤꒐ꄲꉣꋬꇙ꒯ꊰꍌꁝ꒻ꀘ꒒ꁴꉧꉔ꒦ꃳꋊꂵ",
    "𝘲𝘸𝘦𝘳𝘵𝘺𝘶𝘪𝘰𝘱𝘢𝘴𝘥𝘧𝘨𝘩𝘫𝘬𝘭𝘻𝘹𝘤𝘷𝘣𝘯𝘮",
    "ҩω૯Ր੮עυɿ૦ƿคςძԲ૭ҺʆқՆઽ૪८౮ცՈɱ",  #30
    "qwₑᵣ𝚝yᵤᵢₒ𝐩ₐ𝘴𝚍fg𝓱ⱼ𝓴ᄂzₓ𝚌ᵥ𝚋𝚗ᗰ",
    "ϙɯҽɾƚყυισραʂԃϝɠԋʝƙʅȥxƈʋႦɳɱ",
    "ｑώⒺℝ𝓣ч𝕌𝕚ᵒƤＡ𝕤Ⓓ𝕗قĦנｋ𝕃𝕫ˣ𝐜𝕧𝔟ภ𝓶",
    "Q₩ɆⱤ₮ɎɄłØ₱₳₴Đ₣₲ⱧJ₭ⱠⱫӾ₵V฿₦₥", 
    "𝔔𝔚𝔈ℜ𝔗𝔜𝔘𝔓𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏ℨ𝔛ℭ𝔙𝔅𝔑𝔐", 
     "𝖰𝗐𝖾𝗋𝗍𝗒𝗎𝗂𝗈𝗉𝖺𝗌𝖽𝖿𝗀𝗁𝗃𝗄𝗅𝗓𝗑𝖼𝗏𝖻𝗇𝗆",
    "𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝓏𝓍𝓬𝓿𝓫𝓷𝓶",
     "𝐐𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥𝐳𝐱𝐜𝐯𝐛𝐧𝐦",
      "𝑄𝑤𝑒𝑟𝑡𝑦𝑢𝑖𝑜𝑝𝑎𝑠𝑑𝑓𝑔ℎ𝑗𝑘𝑙𝑧𝑥𝑐𝑣𝑏𝑛𝑚",
     "ᑫᗯEᖇTYᑌIOᑭᗩᔕᗪᖴGᕼᒍKᒪᘔ᙭ᑕᐯᗷᑎᗰ",
     "𝔔𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪",
     "𝕼𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒",
     "𝒬𝓌𝑒𝓇𝓉𝓎𝓊𝒾𝑜𝓅𝒶𝓈𝒹𝒻𝑔𝒽𝒿𝓀𝓁𝓏𝓍𝒸𝓋𝒷𝓃𝓂",
     "𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝓏𝓍𝓬𝓿𝓫𝓷𝓂",
     "𝗤𝗪𝗘𝗥𝗧𝗬𝗨𝗜𝗢𝗣𝗔𝗦𝗗𝗙𝗚𝗛𝗝𝗞𝗟𝗭𝗫𝗖𝗩𝗕𝗡𝗠",
    "ꁸꅐꍟ꒓꓅ꐟꐇꂑꆂꉣꋫꌚꁕꄘꁍꑛꀭꀗ꒒ꁴꇓꏸꏝꃃꁹꁒ",
    "ꆰꅏꍟꋪ꓄ꌩꀎꀤꂦꉣꍏꌗꀸꎇꁅꃅꀭꀘ꒒ꁴꊼꉓꃴꌃꈤꂵ",
    "ゐW乇尺ｲﾘひﾉのｱﾑ丂りｷムんﾌズﾚ乙ﾒᄃ√乃刀ﾶ",
     "ᎤᏇᏋᏒᏖᎩᏬᎥᎧᎮᏗᏕᎴᎦᎶᏂᏠᏦᏝፚጀፈᏉᏰᏁᎷ",
     "ҨƜƐ尺ŤϤЦɪØþΛらÐFƓнﾌҚŁẔχㄈƔϦЛ௱",
     "გwპΓནყυἶõρმჰძfცhქκlɀჯეὗჩῆო",
     "𝒒᭙𝒆𝗿†ᥡᶶ¡őᵽ𝕒ṧÐϝ𝑔𝐡ɉ𝐤ₗᴢxc𝔳𝔟𝚗m",
     "qwêr†¥µïðþå§Ð£ghjklzx¢vßñm",
     "q𝔀ⓔᖇ𝕥ｙⓊᎥσｐ𝓪ร∂ᶠᎶђＪⓀ𝓵žx𝒸ⓥ𝕓ⓝⓂ",
    "𝓠𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶",

   
]


def add_stylized_effects(text):
    special_chars = [""]
    result = ""
    for char in text:
        result += char + random.choice(special_chars)
    return result


def nick_generator(name,son=None):
    result = []
    if son:
        fon = yozuv[son-1]
        min_length = max(len(text), len(fon))
        my_name = name.lower()
        for i in range(min_length):
          if i < len(name) and i < len(fon):  
            my_name = my_name.replace(text[i], fon[i])
            
            
        return my_name
    
    else:
        for fon in yozuv:
            min_length = min(len(text), len(fon))
            my_name = name.lower()
            for i in range(min_length):
                my_name = my_name.replace(text[i], fon[i])
            stylized_name = add_stylized_effects(my_name)
            my_name_with_emoji = f" {stylized_name}"
            
            result.append(my_name_with_emoji)
        return result

def transform_text(input_text, styles):
    # Select a random style
    selected_style = random.choice(styles)
    # Map each character in the input text to the corresponding character in the selected style
    translation_table = str.maketrans(text, selected_style)
    # Return the styled text
    return input_text.translate(translation_table)



