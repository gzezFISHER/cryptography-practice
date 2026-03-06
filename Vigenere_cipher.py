'''
This is a naive personal explore and practice related to Vigenere cipher,
including its encryption and decryption. 
Some classic methods, IOC and letter frequencies for instance, are employed in this programme,
though not fully consistent with classic programme.
The correct percentage can reach 85% in best cases and holds a worst record of 50%.
Although somewhat ugly, the programme can be, and should be treated seriously in light of the
courage and diligence from a novice in computer science. 
'''
from collections import Counter
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
    else:
        return "Error: invalid plaintext or key."

def vigenere_decryption(ciphered, epsilon=0.009):
    IOC=0.065
    random_IOC=0.0385
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet_dict={}
    reverse_dict={}
    for i in range(len(alphabet)):
        alphabet_dict[i]=alphabet[i]
        reverse_dict[alphabet[i]]=i
    def get_len(ciphered):
        len_percentage={}
        for i in range(1, len(alphabet)):
            all_result=[[] for _ in range(i)]
            for j in range(len(ciphered)):
                all_result[j%i].append(ciphered[j])
            matched_num=0
            total_num=0
            for result in all_result:
                for m in range(len(result)):
                    for n in range(m+1, len(result)):
                        total_num+=1
                        if result[m]==result[n]:
                            matched_num+=1
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
    'e': 0.12702,
    't': 0.09056,
    'a': 0.08167,
    'o': 0.07507,
}
        for letter in ciphered:
            all_result[counter%length].append(letter)
            counter+=1
        def get_top_4_letters(some_list):
            some_dict={}
            some_percentage_dict={}
            for letter in alphabet:
                some_dict[letter]=0
                some_percentage_dict[letter]=0
            for letter in some_list:
                some_dict[letter]+=1
            for letter in alphabet:
                some_percentage_dict[letter]=some_dict[letter]/len(some_list)
            top_4_letters=sorted(some_percentage_dict, key=some_percentage_dict.get, reverse=True)[:4]
            return top_4_letters
        for i in range(length):
            top_4_letters=get_top_4_letters(all_result[i])
            move_steps_num=[]
            for j in range(len(letter_frequencies)):
                move_steps_num.append((reverse_dict[top_4_letters[j]]-reverse_dict[list(letter_frequencies.keys())[j]])%len(alphabet))
            mode=Counter(move_steps_num).most_common(1)[0][0]
            key[i]=alphabet_dict[mode]
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