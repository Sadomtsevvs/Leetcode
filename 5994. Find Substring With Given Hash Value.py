from time import time
from functools import cache


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        abc = {}
        count = 1
        for a in 'abcdefghijklmnopqrstuvwxyz':
            abc[a] = count
            count += 1

        @cache
        def part(symb, p, i):
            return abc[symb] * p**i

        @cache
        def hash(s, p, m):
            sum = 0
            for i in range(len(s)):
                sum += part(s[i], p, i)
            return sum % m

        for i in range(len(s) - k + 1):
            if hash(s[i:i+k], power, modulo) == hashValue:
                return s[i:i+k]



start_time = time()

# _s = "leetcode"
# _power = 7
# _modulo = 20
# _k = 2
# _hashValue = 0
# _s = "fbxzaad"
# _power = 31
# _modulo = 100
# _k = 3
# _hashValue = 32
# _s = "kfedcbdngvlykqyrbvwbnaassgjifjxtawlafhcpjtpzfnbsqfasohevbbhkwmtnmixolfepkjmcbadqcljmsbonrngsgfqwzqiisbiwiqgtqtq" \
#      "ddukgtjymbxzmtxrobuhkdxmdmqccrauzkrjisstznnkhupiandekzcchsrzwintkkzhvqomqmnbasynmvtxwydcvwoukqmgrpmgzqancuzapgn" \
#      "casxnbyznlrdvcbomdptjftgxdzeqzyavfdpseoxpvohpxtikyjfvskxyqbubgnseraxtrcrwjxloxymhqgaxwbbvzhjsbncqrlpdbiuakdjzjr" \
#      "bclhxgnjjyfrqyjchlsdrcwtdoktviqwjctlmzqemumgmjufcbixkfhzkugsvnkrrakccguybwhmuexiemqusltaaqrswsezccqzaputgaabrjd" \
#      "eihmkpzbojnusmhkwjdxvgiexwdkkazhhmlalgzvxgqgncfytrxuhkwhwcxhmlbvkhjcnyztepwnlpthozdqexvhxpvheopjrsjzkqrstczffkh" \
#      "kikelwydcbnghfiibeyabgegdgaqvasujmggltkvokmnsmontjzsmzoeeqenafvurbnbwqbizvaqxfgnoxasctfrwvqmoufvpajdkethlvbhbeh" \
#      "xahcpcizocbchwfznhuqtblwepeqdhycrovqosmxxeeqaffjvvclmpcqdugndexexcykyusetuamymszlteobxkestwbzubpstbwrstuovlybyc" \
#      "evedzgurqvlgkouvavcukccgixixsrndurvrkfegegnchbhockujlafxexlxhgysraviztkjymiqxrlldcixvfnzrpserrqycbfmesqbltywman" \
#      "dcqtluccbisfqzosbvedqhsxepdjevaasylvjmfpvyxqvclaalgxytiukyarojmzyovmiunkvqhkouhxxhbemavagrhteofpowvlpdunjjpwgcj" \
#      "ibagfswrzwkgrwklppchvtukzncvoqorlsskyghkhrazwvyqqjfygmduhsfkrseddgmtdvlqeruxogmyttdqmdpmscspatkoifauivwjtbwisii" \
#      "qztrllfqnjvbagrfylrpjudjmvwhdkhahyxlsfbkuuyofryfgblllzeacfiqqawridcbtqnroxwuqhyspqmwhxmjztqokofnkfvupcykszthicd" \
#      "gjbrgafpztktrcwtayoulnjaazigkinnpttghhyboiczvtswenshlmqyelnwhzqlswblqssiiynypfcxerlykpiyimkoodimdfdlzbwmlwflylc" \
#      "qwaflivqeonjswvowxgeoafmppodmfbvooodtnzgmhfnchenaaywqevklrpgajbmbxgiopofghlouhjfarjxlclcullsgyzhohowtragbkaebrv" \
#      "bkmxfxughlirtikheojbrrgxtqldfdnqxndzvfgajiltnqnuwavxbrvuiycsizunlglwnivpseyfwmgydmmpzhxkdtpuzpddacjmjhvncdoiced" \
#      "kimdgaqobdfagpggvjemstqbsshynyvhdyslgldvkapqgusmnuroqxcivjifkhrotomxodficktxmcytkbqitrlalpbtphowfgtzgfacabjodvi" \
#      "vgykorvmxhzpqvskolkbfpbdgowlighossrlwiomgohfhgklmlnekniqfjmvvqvmimkeddfxnxwzzroospxvndynetghkgrakuslukqsrdtmjkb" \
#      "lwrmwhzzojcwwogrjvnftdwwpoqcjqimvjbwgqgpeffjnwlzdyhkhwmvpwpcmjmdqneexqwcrvdxsfsnidwyflwxwngczklprhoazeeqwclrqvn" \
#      "icfvrtbqailbwrqxadxslouwdjycidupemdwhpkqekaxxprtdtmjficrhlvqidvgwkllaowyyajkxugqiztbpzvjqtpuyugkvdfcaczzruskvuc" \
#      "sxtvroljnjojuzncatgnypbzwvilbajqqnjovqxcfunwwbxgshrjlajwveaswqegidfnedpxqdreddvawrpbllkcshlafnxyocbmwacytvgtoon" \
#      "lkukqhxwbfxcfnbgmrfcnkvtxmygiyjoyoljd"
# _power = 71717
# _modulo = 94536
# _k = 1149
# _hashValue = 39999
_s = "idmqbuxyodnfjqqkvbufbrbleswpxgjcsdmiipyulasthaiidlatjfjquzjwwigvtraqnpcsmkjtpktoscxpyrobesfoyxxmqvrbiaqhxgennfn" \
     "svjfobrxihlisswspqshucfjhumhpyxhqmonmuqwpfubazjolsafewrewkhsqksygeboxusjhittltndcgdftoxzfbcajfqlhtsscnsplcykicw" \
     "jrvnlbknptxkmudwismybeugsreotxrafzwhykgodiyrfutqqmlncqhuakhwsitskoblancgyzzgytyfhbbauwdmndeooaxtkrwkhkpvksfmavp" \
     "koylimzrgchlxqhgeahhgubrsnbvsgczlhoivyfmsdtwvftwyjjhzufxbqwzovfvyibgmvgyigfxyywguciqwzylvqpazcdfjsjpgiokxsibwbl" \
     "sprmuxlcdevuxuisdxgxlehjdqnwfzduzrqfbdpraezgcmhzkklmpdrmvxjcukxtpnwqnoexuhhcegjceboickgfdyxcwunmfpmhppqcjwqkxoi" \
     "fiilwtwkhrueosqfezdrtttukuibwjvuozgulqzehqdmvacfzbrhdlpmslyyhxtvotpynxadfetjojxrvnlxzuvmsnqefsgcbfnkaxrpbekleyz" \
     "cftfbvzzrnoqicjalqxcgjeicrpozvdlzwoowucfdzehzboehplcxtbbghsgzfyyuxmrkvzoscytxwsssztcbzeggvsuwucuhedcnwmrmoaewar" \
     "gudoxdmwvtohqxkmpsygyxhllfmyuljnhazierdkbkahyapscovmocigsnvthmiksdchkvxfmlglacjquowfxuotvdmbxetfvyavbhqdjjddbrd" \
     "owepligxhjvbsytcqicwjnqiawqxddaitffpkcsccyutoqpunivybnrzlkbuxxocujvefwecomadianminlfsllsjvxmcofbsqpltfubfdhfqce" \
     "cwjgrjhimxefxfquinaxxnouaqfxjfimlalzqddjcjdcuslhsqeoiuuhrxhsqznczrkbdeultcatzpnkppwhdrzztppephifmhxjiepvabjoiht" \
     "gczuunmsgqoqaqkkqliurcqbrtzvkghswigwybzxxgrobsfjdlpejwrhddpqsaylswcyurhrwohwyasongbdnwyoonlbtigkgchdbcscsfzutoq" \
     "plyauqrdrbyxoyrfxbzhnpzyaskncyqneoisayjzebxkiwzxakmbovomujosxjkrchvsxrwtkniyeincdwntccwtxfmyyyktddepbzazrrdqgwf" \
     "vxvkkfcdymabdwihvmkrtqeksrthblurbuhtqlsomvsinrqybluytaxxoglaecbpddgvqdfvycsvqxapxmdpyqwfapdqzmsvhimzrhlpmuzebpz" \
     "dfbvjloiatohbhuosmltwhpuankinmqotncevtzhezbivugsfsnxttahvbapjmaqzfhgljicnjehprgkdzvekepqotfwvtjlvuheavwnvurjisf" \
     "lldrjfawtizvlarqxjbdwgqtpoyukinfzslxathhsaxwdcnsiiygauzmjhoskwbypvkssascznuysbyfsapbutahyrpbvroyavrynkrqpnoosxe" \
     "wbfbnppwoeihdccitjtlufkexzzpbncjecmqzhqhghseeqpvvmzgnkeyzayjskhtxrvpfijilebltqzocxeygexsyxhvksysqanlylxrravnxyk" \
     "jbkqikvwrnxvovbjjzijjioblcyqotbyortwwystderalkeogbgezpucvxljlrbtprquemedhtnwdvpfpxhxcoydsfgpezezivyqlbnexndehiy" \
     "sjwxryyktiritonkqxpsgjspsarcrulfcropkftmscwftgdvgnaxucrykcbijknetkpnribtkihlyggbpqwnvqkppcuhoxzuokdcxgopnxhtnjm" \
     "hygtmbehrqsvhtjixlzwecifoeyetjhfaeonnxltaeiwynpnwqmsyyixutlndxcgfowljpbgxrwctvudiajhrlkllmeqlycricnkrubpeombjmx" \
     "mkbwvjfocjxbjfrqycmqyvoautdetbyellieygwmtlmanltchsbexhsrmcfpigfvsotraobcpmkrolxebqlwdlxprsoixqmpcrzwmmuoqbptnlv" \
     "xdfyvazbyehonigoelbifkjlrntvzlqkxwshudiiehuclgtitrccuzvmoiiwvrnlfdniundxdmltghpjeehjtctmrzgxmcgjfblhjrykqgbmhsz" \
     "jjurrtyttsiuzuzpgjkbsgwfnwzabwtesynsjdtslrrkwezieilymdlehugejqluccbclqoxjupiwnqjpgluzyugzndwryotvsypbhyqzdaadgs" \
     "aogpspzurboljduqjwxgvrkrqkqkzhxwxvqqepzhxmspdapjzpagqmnjdaeydjbfatxqthqnyiffopzkdstxupwroxefcfososryfssxckfvdad" \
     "zideicysanlhragokbojzehrqcddskzoqjftdzzmcvuyvqjxnrywgdmzoifecuejplkjoedbeizpkbomugclusvgdjcfssixjdvumdocigvqbnu" \
     "fpvpgyajtucuurgvmdcjvuykrebziefsjywtphqpncvdklxhutgiwdnizgwukiykghbiwdjpbuqxqvvcpqofqvrhnstahpbofxcnjewxfzhfwec" \
     "deulovbeukodtpovztzebqpixedfoqvzhyeibdmkdjsdsqgcapscfjrwjqkfoeqbguqpngvlfyfxppvethvzbltkhjgithlbkcqritevqamczoh" \
     "zkhumnzvexsyhasohcnkvlxbjmwfysffjukzmqehkabkmjdcbnokdctvdlgnjoirtamllenswaiswilekhnashjwaxeuthsetkojtvtgnrwkwha" \
     "tsmogmkatjoxkhbzwarxiiluvhitspquvavuipytljvxhehtcynrcncwswqeepyiglnpspmxknrkohmyulfswdjngcjqwfruvyoiatkzdmgchhz" \
     "zdhhdqnwyvnbvvyzwlowevborfmsgxfocwzyzznhagtaeikfkokokbtrlpxyrhwdgscihkzcmgbluhbnlzdqphvmmejhnyvsvkaktxbcogkkiqi" \
     "rusrendsmpmrrfabocerfellzpwxwdndhsfdmsvjzysyqdyanxovfnnluetiokwzpeorbvklhwozhmwjidiloudszgcqvpxguwvxaytpviqxapj" \
     "vllcjsgxdkfpnvgqtojryldytepnuvrruebazfdrvfnysbzkgfyxhtyqrgsognhtqjchxblzeolfzazrpeixwqxqwrgbmsirwhmcthahoiihczn" \
     "eubrfdhjvuabcdzpogpzhhsphsqmcobabxeaykqqitgzekwkzfzculeuygukfgbkeghdxypqesnuvcvjjjjmcflajgbctklooztmddveadrlbqm" \
     "ltpvyywcvrqccxgzikbtpbedraouaymnuabresamptxbtxbhrjoznunetpviaprkytrcehplnlggddsjecspmkaigoypryfygsnzecdgcvxfpdo" \
     "fnihglkwdrodvvcqqgcqmvmbybssrxmrrdnwdekfryohzivojxpmmsxmqkiqonsythefzsxgdvlweyqqnkxujvkgvlgnsfcptihqqkitdrwwnrs" \
     "xscrhlxkfuxfbrymqxagyotmsmmtnkysqusibsxuckrgbvvpnyflcfswzulyjqwuynlhzanjcqbbolonbcpcpigbnnimdqbiwgoyltytwyieajj" \
     "qwqddxjymgmyzncbeuvmwthbspxlqawnadmgbkhflxeloefbtvybxneumivdebbffskuhphlxbobyrpdqacsaywdkmlyxhqmgptgbeorxdyrdpd" \
     "vvzqrjmhugkcwvfujxzcuacwgnfverkzalvrqbkvurksqmyjqpnnamscxtjufiqvbxicxnidnfwinnmvmrgewarhdjeoldapnvbevhlggjocjmo" \
     "guzcgwqxfhbxqmnblpjllqxtmuyxmobxuunlxtbuxgicopiglbikjaghebptgemwvfeeebdxlzqtqcwbqvoabcocdvjfggpmbkoqlzuwdmaepsy" \
     "lhcqcnzktkqjumgbfyuycmoiqcsrzdogdkybvqlrwdwcpiusirtzscbkydmfcepaphdtmtslvjlhlpgeydzafyuafivqukhulngxpbkmgsrjxdw" \
     "qoswfqecpichuavxotishfscacvvyeixsqktbfwwqikktxjnkekitcebsdrztjbonrlfstgpudqhyjuggklyozstnrhzhzopndaoybxtxfkvmbc" \
     "lqtdecrnjeqpcgzwcbtthltbzmtsfpviizcatpajjcvmtepcibbqdaymopqjuanqrzluggvirbwoihccmoeqofgyqqbihasgnzxxczqaudlitwn" \
     "gfehysawevbhhmijgwvxtcctcaalshxzxwtwlvvkgubbptgfdzfkryexskmuyggroyzceytdkeoogkjcrrgeuhcmwfxlhgiwvdmrkyhnuwmuxjt" \
     "vhruxkpnpldysyxqmaofhvawpguevrlovtqgxsotjokczkiehpnpemcwaabworfysqtgwhcvatdxtnvfggiifhhrhrzhbimtzxmlfz"
_power = 9252
_modulo = 90083
_k = 3697
_hashValue = 86173

# Input: s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0
# Output: "ee"
# Explanation: The hash of "ee" can be computed to be hash("ee", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0.
# "ee" is the first substring of length 2 with hashValue 0. Hence, we return "ee".

print(Solution().subStrHash(_s, _power, _modulo, _k, _hashValue))

print("--- %s seconds ---" % (time() - start_time))