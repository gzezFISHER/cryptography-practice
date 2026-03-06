from collections import defaultdict
def vigenere_encryption(plaintext, key):
    ciphered_list=[-1]*len(plaintext)
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet_dict={}
    reverse_dict={}
    is_valid=True
    for letter in key:
        if letter not in alphabet:
            is_valid=False
    for i in range(len(alphabet)):
        alphabet_dict[i]=alphabet[i]
        reverse_dict[alphabet[i]]=i
    for i in range(len(plaintext)):
        if plaintext[i] not in alphabet and plaintext[i]!=" ":
            is_valid=False
        if is_valid:
            plain_letter=plaintext[i]
            if plain_letter==" ":
                ciphered_list[i]=" "
                continue
            key_letter=key[i%len(key)]
            ciphered_list[i]=alphabet_dict[(reverse_dict[plain_letter]+reverse_dict[key_letter])%len(alphabet)]
    if is_valid:
        ciphered="".join(ciphered_list)
        return ciphered
    raise RuntimeError("Invalid plaintext or key.")

def vigenere_decryption(ciphered, epsilon=0.009):
    IOC=0.065
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet_dict={}
    reverse_dict={}
    for i in range(len(alphabet)):
        alphabet_dict[i]=alphabet[i]
        reverse_dict[alphabet[i]]=i
    def get_len(ciphered):
        len_percentage={}
        for i in range(1, len(alphabet)):
            all_result=[defaultdict(int) for _ in range(i)]
            for j in range(len(ciphered)):
                all_result[j%i][ciphered[j]]+=1
            matched_num=0
            total_num=0
            for result in all_result:
                total_count = 0
                for count in result.values():
                    matched_num+=count*(count-1)//2
                    total_count+=count
                total_num+=total_count*(total_count-1)//2
            percentage=matched_num/total_num
            len_percentage[i]=abs(percentage-IOC)
        for index, per in len_percentage.items():
            if per<epsilon:
                first_possible=index
                break
        key_length=first_possible
        return key_length

    def get_key(ciphered, length):
        key=[-1]*length
        all_result=[[] for _ in range(length)]
        counter=0
        letter_frequencies = {
            'a': 0.08167,
            'b': 0.01492,
            'c': 0.02782,
            'd': 0.04253,
            'e': 0.12702,
            'f': 0.02228,
            'g': 0.02015,
            'h': 0.06094,
            'i': 0.06966,
            'j': 0.00153,
            'k': 0.07720,
            'l': 0.04025,
            'm': 0.02406,
            'n': 0.06749,
            'o': 0.07507,
            'p': 0.01929,
            'q': 0.00095,
            'r': 0.05987,
            's': 0.06327,
            't': 0.09056,
            'u': 0.02758,
            'v': 0.00978,
            'w': 0.02360,
            'x': 0.00150,
            'y': 0.01974,
            'z': 0.00074
        }
        for letter in ciphered:
            all_result[counter%length].append(letter)
            counter+=1

        def get_best_shift(sub_cipher):
            total=len(sub_cipher)
            observed_freq = defaultdict(float)
            for letter in sub_cipher:
                observed_freq[letter]+=1/total
            if total==0:
                return 0
            best_shift=0
            min_diff=float('inf')
            for shift in range(len(alphabet)):
                diff_sum=0
                for letter in alphabet:
                    shifted_letter=alphabet[(reverse_dict[letter]+shift)%len(alphabet)]
                    diff_sum+=(observed_freq[shifted_letter] - letter_frequencies[letter]) ** 2
                if diff_sum<min_diff:
                    min_diff=diff_sum
                    best_shift=shift
            return best_shift

        for i in range(length):
            shift = get_best_shift(all_result[i])
            key[i] = alphabet_dict[shift]
        return key
    key_length=get_len(ciphered)
    key=get_key(ciphered, key_length)
    print(f"for test:\nkey_length {key_length}\nkey {key}")
    def get_plaintext(ciphered, key):
        plaintext_list=[-1]*len(ciphered)
        for i in range(len(ciphered)):
            key_letter=key[i%len(key)]
            plaintext_list[i]=alphabet_dict[(reverse_dict[ciphered[i]]-reverse_dict[key_letter])%len(alphabet)]
        plaintext="".join(plaintext_list)
        return plaintext
    plaintext=get_plaintext(ciphered, key)
    return plaintext

key="testkey"
plaintext="artificialintelligenceisrapidlychangingthewayweliveandworkfromvoiceassistantsinourhomestosophisticatedalgorithmsrecommendingwhattowatchnextthistechnologyhaswovenitselfintothefabricofdailylifemachinelearningasubsetofaiallowssystemstolearnfromdataandimprovetheiroverperformancewithoutbeingexplicitlyprogrammedthishasledtobreakthroughsinfieldslikemedicalresearchwhereaicanalyzewastamountsofpatientdatatoidentifypatternsinvisiblyehumaneyesandassistindiagnosingdiseasesearlierthaneverbeforeintheautomotiveindustryselfdrivingcarsrelyoncomplexaisystemstointerpretsensordatamakerealsplitseconddecisionsandnavigateroadssafelythispromisestoreducetrafficaccidentscausedbyhumanerrorandtransformurbantransportationmoreoveraiplaysacrucialroleincombatingclimatechangebyoptimizingenergyconsumptioninpowergridsandsmartercitiesitalsohelpsscientistsmodelcomplexclimatesystemsanddevelopmoresustainablematerialsandeducationisalsobenefitingfromaipoweredtutoringplatformsthatadapttoeachstudentsuniquelearningpacefillingknowledgegapsandprovidingpersonalizedfeedbackintheworldofartandcreativityaigenerativemodelscannowproduceimagesmusicandtextopeningnewavenuesforexpressionandcollaborationbetweenhumansandmachineshoweverthesedvancesraiseprofoundquestionsaboutethicsjobdisplacementandthefutureofprivacyasaibecomesmorecapableitisessentialtodevelopitresponsiblyensuringitbenefitsallofhumanitywhilemitigatingpotentialrisksultimatelythejourneyofaiisoneofthemostsignificantendeavorsofourtimeofferingtremendousopportunitytoprovideglobalsolutionsifguidedbycarefulthoughtandinclusiveprinciplesfosteringabetterfutureforeveryone"
ciphered=vigenere_encryption(plaintext, key)
cracked_plaintext=vigenere_decryption(ciphered)
correct_num=0
for i in range(len(plaintext)):
    if plaintext[i]==cracked_plaintext[i]:
        correct_num+=1
correct_percentage=f"{(correct_num/len(plaintext)):.2%}"
print(f"correct percentage {correct_percentage}")