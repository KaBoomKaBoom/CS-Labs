import string
from collections import Counter
import matplotlib.pyplot as plt
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
    substitution_mapping = {sorted_cipher_letters[i]: english_freq[i] for i in range(2)}
    
    return substitution_mapping

# Function to decrypt the ciphertext using the substitution mapping
def decrypt_with_mapping(ciphertext, substitution_mapping):
    decrypted_text = ''
    for char in ciphertext:
        if char.upper() in substitution_mapping:
            decrypted_char = substitution_mapping[char.upper()]
            # Substituted characters in uppercase, non-substituted in lowercase
            decrypted_text += decrypted_char.upper()
        else:
            # Leave non-alphabetic and non-substituted characters unchanged and lowercase
            decrypted_text += char.lower() if char in string.ascii_lowercase else char
    return decrypted_text

def add_mapping(substitution_mapping, cipher_char, english_char):
    # Add a new mapping for the given cipher character
    substitution_mapping[cipher_char] = english_char
    return substitution_mapping


# Function to plot letter frequencies
def plot_letter_frequencies(counter):
    letters = sorted(counter.keys())
    frequencies = [counter[letter] for letter in letters]
    
    plt.bar(letters, frequencies, color='blue')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency Analysis')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# Frequency of letters in the ciphertext for plotting
cipher_cleaned_text = preprocess_text(ciphertext)
cipher_letter_count = frequency_analysis(cipher_cleaned_text)

# Plotting the frequency
plot_letter_frequencies(cipher_letter_count)

# Substitution mapping based on frequency analysis
substitution_mapping = create_substitution_mapping(ciphertext, english_letter_frequency)

# Decrypt the ciphertext
decrypted_text = decrypt_with_mapping(ciphertext, substitution_mapping)
print("\nDecrypted Text:\n", decrypted_text)

add_mapping(substitution_mapping, 'Q', 'H')
add_mapping(substitution_mapping, 'F', 'Y')
add_mapping(substitution_mapping, 'N', 'O')
add_mapping(substitution_mapping, 'T', 'A')
add_mapping(substitution_mapping, 'G', 'N')
add_mapping(substitution_mapping, 'O', 'D')
add_mapping(substitution_mapping, 'I', 'R')
add_mapping(substitution_mapping, 'P', 'S')
add_mapping(substitution_mapping, 'K', 'V')
add_mapping(substitution_mapping, 'X', 'I')
add_mapping(substitution_mapping, 'C', 'F')
add_mapping(substitution_mapping, 'J', 'G')
add_mapping(substitution_mapping, 'H', 'C')
add_mapping(substitution_mapping, 'R', 'W')
add_mapping(substitution_mapping, 'D', 'U')
add_mapping(substitution_mapping, 'S', 'L')
add_mapping(substitution_mapping, 'A', 'B')
add_mapping(substitution_mapping, 'U', 'P')
add_mapping(substitution_mapping, 'M', 'Z')
add_mapping(substitution_mapping, 'Z', 'M')
add_mapping(substitution_mapping, 'L', 'K')
add_mapping(substitution_mapping, 'Y', 'X')
add_mapping(substitution_mapping, 'B', 'Q')


decrypted_text = decrypt_with_mapping(ciphertext, substitution_mapping)
print("Substitution Mapping:", substitution_mapping)
print("\nDecrypted Text:\n", decrypted_text)