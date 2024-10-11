# import AnalyzeFrequency

# crypted = """Unsfaxdp tgo nwqvip gvkvi ptxo rqvwqvi tgf nc wqv pdapwxwdwxnghxuqvip wqvf ovphixavo rviv
# thwdtssf dpvo, tgo pn wqv cxipw twwvpwvo dpv ncwqtw jvgiv xg unsxwxhts tcctxip hnzv cinz wqv
# Inztgp — tgo cinz wqv jivtwvpw Inztg nc wqvz tss. EdsxdpHtvpti wqdp xzuivppvo qxp gtzv
# uviztgvgwsf xgwn hifuwnsnjf.Xw zdpw av wqtw tp pnng tp t hdswdiv qtp ivthqvo t hviwtxg
# svkvs,uinatasf zvtpdivo stijvsf af xwp sxwvithf, hifuwnjituqf tuuvtippungwtgvndpsf — tp xwp
# utivgwp, stgjdtjv tgo rixwxgj, uinatasf tspn oxo.Wqv zdswxusv qdztg gvvop tgo ovpxivp wqtw ovztgo
# uixkthf tzngj wrnni zniv uvnusv xg wqv zxopw nc pnhxts sxcv zdpw xgvkxwtasf svto wnhifuwnsnjf
# rqvivkvi zvg wqixkv tgo rqvivkvi wqvf rixwv. Hdswditsoxccdpxng pvvzp t svpp sxlvsf vyustgtwxng
# cni xwp nhhdiivghv xg. pn ztgftivtp, ztgf nc wqvz oxpwtgw tgo xpnstwvo.Wqv Fvmxoxp, tg naphdiv
# pvhw nc tandw 25,000 uvnusv xg, gniwqvig Xitb,dpv t hifuwxh phixuw xg wqvxi qnsf annlp avhtdpv
# wqvf cvti uvipvhdwxng afwqvxi Znpsvz gvxjqanip. Wxavwtgp dpv t lxgo nc hxuqvi htssvo "ixgpudgp"cni 
# nccxhxts hniivpungovghv; xw xp gtzvo cni xwp xgkvgwni Ixg-h'(qqvg-)pudgp(-ut), rqn
# sxkvo xg wqv 1300p. Wqv Gpxaxox pvhivw pnhxvwf nc Gxjvixtlvvup xwp uxhwnjituqxh phixuw
# cinz Vdinuvtgp tp zdhq tp unppxasvavhtdpv xw xp dpvo hqxvcsf wn vyuivpp snkv xg itwqvi oxivhw
# xztjvif, tgoptzusvp tuuvti wn av tw svtpw tp unignjituqxh tp wqvf tiv hifuwnjituqxh.Wqv hifuwnjituqf
# nc Wqtxstgo ovkvsnuvo dgovi Xgoxtg xgcsdvghv. Tgvzaifngxh pwdof nc wqv pdaevhw vkvg tuuvtip
# xg t jitzztwxhts rnilvgwxwsvo Unitgtktlft af Qsdtgj Uitpnw Tlptitgxwx (Uqv). Ngv pfpwvz,htssvo
# "wqv viixgj Pxtzvpv," pdapwxwdwvp ngv ovsxhtwv Pxtzvpv svwwvi cnitgnwqvi. Xg tgnwqvi
# pfpwvz, hngpngtgwp tiv oxkxovo xgwn pvkvg jindup nc cxkv svwwvip;t svwwvi xp xgoxhtwvo af
# rixwxgj wqv Pxtzvpv gdzavi nc xwp jindu tgousthxgj kviwxhts onwp dgovi xw vbdts xg gdzavi wn
# wqv svwwvi'p usthv xg xwpjindu. T pfpwvz htssvo "wqv qvizxw zvwtzniuqnpxgj svwwvip" rixwvp
# wqvwvyw athlrtiop.Xg wqv Vdinuv nc wqv Stwxg tsuqtavw—cinz rqxhq znovig hifuwnsnjfrndso
# puixgj—hifuwnjituqf csxhlvivo rvtlsf. Rxwq wqv hnsstupv nc wqvInztg vzuxiv, Vdinuv qto usdgjvo
# xgwn wqv naphdixwf nc wqv Otil Tjvp.Sxwvithf qto tss adw oxptuuvtivo. Tiwp tgo phxvghvp rviv
# cnijnwwvg, tgohifuwnjituqf rtp gnw vyhvuwvo. Ngsf odixgj wqv Zxoosv Tjvp
# nhhtpxngtsztgdphixuwp, rxwq tg xgcivbdvgw pxjgtwdiv ni jsnpp ni "ovn jitwxtp" wqtw tanivo zngl
# udw xgwn hxuqvi wn tzdpv qxzpvsc, cxwcdssf xssdzxgtwv wqvhifuwnsnjxh otilgvpp, tgo, sxlv t
# pxgjsv htgosv jdwwvixgj xg t jivtwzvoxvkts qtss, wqvxi cvvasv cstixgjp ngsf vzuqtpxmv wqv
# jsnnz.Wqv pfpwvzp dpvo rviv pxzusv xg wqv vywivzv. Uqitpvp rviv rixwwvgkviwxhtssf ni athlrtiop;
# onwp rviv pdapwxwdwvo cni knrvsp;cnivxjg tsuqtavwp, tp Jivvl, Qvaivr, tgo Tizvgxtg, rviv dpvo;
# vthqsvwwvi nc wqv ustxgwvyw rtp ivusthvo af wqv ngv wqtw cnssnrp xw; xg wqv znpwtoktghvo
# pfpwvz, puvhxts pxjgp pdapwxwdwvo cni svwwvip. Cni tsznpw twqndptgo fvtip, cinz avcniv 500
# wn 1400, wqv hifuwnsnjf nc Rvpwvighxkxsxmtwxng pwtjgtwvo""".lower()

# analyzeFrequency = AnalyzeFrequency.AnalyzeFrequency(crypted)

# frequency = analyzeFrequency.get_frequency()
# print(frequency)

import string
from collections import Counter
import difflib 
# Given ciphertext
ciphertext = """
Unsfaxdp tgo nwqvip gvkvi ptxo rqvwqvi tgf nc wqv pdapwxwdwxnghxuqvip wqvf ovphixavo rviv
thwdtssf dpvo, tgo pn wqv cxipw twwvpwvo dpv ncwqtw jvgiv xg unsxwxhts tcctxip hnzv cinz wqv
Inztgp — tgo cinz wqv jivtwvpw Inztg nc wqvz tss. EdsxdpHtvpti wqdp xzuivppvo qxp gtzv
uviztgvgwsf xgwn hifuwnsnjf.Xw zdpw av wqtw tp pnng tp t hdswdiv qtp ivthqvo t hviwtxg
svkvs,uinatasf zvtpdivo stijvsf af xwp sxwvithf, hifuwnjituqf tuuvtippungwtgvndpsf — tp xwp
utivgwp, stgjdtjv tgo rixwxgj, uinatasf tspn oxo.Wqv zdswxusv qdztg gvvop tgo ovpxivp wqtw ovztgo
uixkthf tzngj wrnni zniv uvnusv xg wqv zxopw nc pnhxts sxcv zdpw xgvkxwtasf svto wnhifuwnsnjf
rqvivkvi zvg wqixkv tgo rqvivkvi wqvf rixwv. Hdswditsoxccdpxng pvvzp t svpp sxlvsf vyustgtwxng
cni xwp nhhdiivghv xg. pn ztgftivtp, ztgf nc wqvz oxpwtgw tgo xpnstwvo.Wqv Fvmxoxp, tg naphdiv
pvhw nc tandw 25,000 uvnusv xg, gniwqvig Xitb,dpv t hifuwxh phixuw xg wqvxi qnsf annlp avhtdpv
wqvf cvti uvipvhdwxng afwqvxi Znpsvz gvxjqanip. Wxavwtgp dpv t lxgo nc hxuqvi htssvo "ixgpudgp"cni 
nccxhxts hniivpungovghv; xw xp gtzvo cni xwp xgkvgwni Ixg-h'(qqvg-)pudgp(-ut), rqn
sxkvo xg wqv 1300p. Wqv Gpxaxox pvhivw pnhxvwf nc Gxjvixtlvvup xwp uxhwnjituqxh phixuw
cinz Vdinuvtgp tp zdhq tp unppxasvavhtdpv xw xp dpvo hqxvcsf wn vyuivpp snkv xg itwqvi oxivhw
xztjvif, tgoptzusvp tuuvti wn av tw svtpw tp unignjituqxh tp wqvf tiv hifuwnjituqxh.Wqv hifuwnjituqf
nc Wqtxstgo ovkvsnuvo dgovi Xgoxtg xgcsdvghv. Tgvzaifngxh pwdof nc wqv pdaevhw vkvg tuuvtip
xg t jitzztwxhts rnilvgwxwsvo Unitgtktlft af Qsdtgj Uitpnw Tlptitgxwx (Uqv). Ngv pfpwvz,htssvo
"wqv viixgj Pxtzvpv," pdapwxwdwvp ngv ovsxhtwv Pxtzvpv svwwvi cnitgnwqvi. Xg tgnwqvi
pfpwvz, hngpngtgwp tiv oxkxovo xgwn pvkvg jindup nc cxkv svwwvip;t svwwvi xp xgoxhtwvo af
rixwxgj wqv Pxtzvpv gdzavi nc xwp jindu tgousthxgj kviwxhts onwp dgovi xw vbdts xg gdzavi wn
wqv svwwvi'p usthv xg xwpjindu. T pfpwvz htssvo "wqv qvizxw zvwtzniuqnpxgj svwwvip" rixwvp
wqvwvyw athlrtiop.Xg wqv Vdinuv nc wqv Stwxg tsuqtavw—cinz rqxhq znovig hifuwnsnjfrndso
puixgj—hifuwnjituqf csxhlvivo rvtlsf. Rxwq wqv hnsstupv nc wqvInztg vzuxiv, Vdinuv qto usdgjvo
xgwn wqv naphdixwf nc wqv Otil Tjvp.Sxwvithf qto tss adw oxptuuvtivo. Tiwp tgo phxvghvp rviv
cnijnwwvg, tgohifuwnjituqf rtp gnw vyhvuwvo. Ngsf odixgj wqv Zxoosv Tjvp
nhhtpxngtsztgdphixuwp, rxwq tg xgcivbdvgw pxjgtwdiv ni jsnpp ni "ovn jitwxtp" wqtw tanivo zngl
udw xgwn hxuqvi wn tzdpv qxzpvsc, cxwcdssf xssdzxgtwv wqvhifuwnsnjxh otilgvpp, tgo, sxlv t
pxgjsv htgosv jdwwvixgj xg t jivtwzvoxvkts qtss, wqvxi cvvasv cstixgjp ngsf vzuqtpxmv wqv
jsnnz.Wqv pfpwvzp dpvo rviv pxzusv xg wqv vywivzv. Uqitpvp rviv rixwwvgkviwxhtssf ni athlrtiop;
onwp rviv pdapwxwdwvo cni knrvsp;cnivxjg tsuqtavwp, tp Jivvl, Qvaivr, tgo Tizvgxtg, rviv dpvo;
vthqsvwwvi nc wqv ustxgwvyw rtp ivusthvo af wqv ngv wqtw cnssnrp xw; xg wqv znpwtoktghvo
pfpwvz, puvhxts pxjgp pdapwxwdwvo cni svwwvip. Cni tsznpw twqndptgo fvtip, cinz avcniv 500
wn 1400, wqv hifuwnsnjf nc Rvpwvighxkxsxmtwxng pwtjgtwvo
"""

# Frequency of letters in English
english_letter_frequency = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

# Remove non-alphabetic characters and convert to uppercase
def preprocess_text(text):
    return ''.join([char for char in text.upper() if char in string.ascii_uppercase])

# Function to analyze frequency of letters in the ciphertext
def frequency_analysis(text):
    return Counter(text)

# Function to create substitution mapping based on frequency analysis
def create_substitution_mapping(ciphertext, english_freq):
    # Preprocess text
    cleaned_text = preprocess_text(ciphertext)
    
    # Get frequency of letters in the ciphertext
    cipher_letter_frequency = frequency_analysis(cleaned_text)
    
    # Sort the ciphertext letters by frequency in descending order
    sorted_cipher_letters = [item[0] for item in cipher_letter_frequency.most_common()]
    
    # Create a mapping from the sorted ciphertext letters to the most frequent English letters
    substitution_mapping = {sorted_cipher_letters[i]: english_freq[i] for i in range(3)}
    
    return substitution_mapping

# Function to decrypt the ciphertext using the substitution mapping
def decrypt_with_mapping(ciphertext, substitution_mapping):
    decrypted_text = ''
    for char in ciphertext:
        if char.upper() in substitution_mapping:
            decrypted_char = substitution_mapping[char.upper()]
            # Preserve case
            decrypted_text += decrypted_char.lower() if char.islower() else decrypted_char
        else:
            decrypted_text += char  # Leave non-alphabetic characters unchanged
    return decrypted_text

def update_mapping(substitution_mapping, cipher_char, english_char):
    # Update the mapping for the given cipher character
    substitution_mapping[cipher_char] = english_char
    return substitution_mapping


# Perform frequency analysis and decrypt
substitution_mapping = create_substitution_mapping(ciphertext, english_letter_frequency)
decrypted_text = decrypt_with_mapping(ciphertext, substitution_mapping)

print("Substitution Mapping:", substitution_mapping)
# print("\nDecrypted Text:\n", decrypted_text)

# Function to calculate similarity between two words
def similar(word1, word2):
    return difflib.SequenceMatcher(None, word1, word2).ratio()


# List of trigraphs
trigraphs = ['the', 'and', 'tha', 'ent', 'ing', 'ion', 'tio', 'for', 'nde', 'has', 'nce']

# Split the decrypted text into words
words = decrypted_text.split()
# print(words)
# Flag to check if similar trigraph is found
found = False

# Loop through each word in the decrypted text
for word in words:
    if len(word) == 3:  # Check only 3-letter words
        print("Analyzing word:", word)  
        for trigraph in trigraphs:
            similarity = similar(word, trigraph)
            if similarity > 0.5 and similarity < 1.0:  # Check for similarity threshold
                print(f"Found similar word: '{word}' -> '{trigraph}' (Similarity: {similarity:.2f})")
                for i in range(3):
                    if word[i] != trigraph[i]:
                        substitution_mapping = update_mapping(substitution_mapping, word[i].upper(), trigraph[i].upper())
                found = True
                break  # Exit once a match is found
        if found:
            break  # Exit the outer loop once a match is found

print("Substitution Mapping after trigraph analysis:", substitution_mapping)

decrypted_text = decrypt_with_mapping(ciphertext, substitution_mapping)
print("\nDecrypted Text after trigraph analysis:\n", decrypted_text)