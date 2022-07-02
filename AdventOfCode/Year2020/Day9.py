#https://adventofcode.com/2020/day/9
#https://adventofcode.com/2020/day/9#part2

# Real data
data = [50,32,17,18,6,12,24,43,14,40,15,25,19,22,44,41,30,21,7,31,35,38,28,46,1,34,64,13,27,29,8,57,20,9,10,26,11,15,12,75,16,37,73,14,25,39,17,18,19,21,30,38,22,42,23,24,27,32,91,83,98,26,28,29,47,53,33,55,31,41,35,36,37,44,43,67,45,73,72,56,100,59,70,86,54,95,57,60,62,74,107,76,66,68,71,81,79,99,87,151,114,104,166,110,155,113,111,116,178,117,125,119,180,128,134,182,137,283,187,150,196,183,197,191,306,280,405,223,221,224,297,235,504,236,267,330,247,271,494,320,324,287,333,371,341,459,374,471,412,456,444,511,522,518,460,558,610,795,483,571,612,644,591,607,611,835,1088,793,834,715,786,1344,856,872,900,1093,1029,943,1738,1178,1041,1384,1054,1074,1235,1198,1202,1322,1218,1326,2247,1627,1571,2135,1587,1729,1728,1843,2629,3519,2328,1972,1984,2095,2115,2128,2256,2252,2272,2400,3450,3618,2540,2789,2913,3158,3198,3315,3712,3559,3457,4067,4240,4351,3956,4761,4079,6856,4210,4243,5286,4508,4652,7850,11300,9396,6772,5329,6655,6071,11806,7438,6874,7016,7769,7413,13179,8035,8307,11623,14068,10734,12012,8718,10579,9160,11424,15932,15473,13098,16176,11400,11984,18147,13087,13890,14454,15592,19435,15182,20319,16342,16753,22786,21805,17878,29927,20560,19297,34209,20584,22824,28326,43384,44502,23384,24487,26438,57838,26977,33060,29636,40079,31524,34479,61884,33095,34631,37175,44855,38438,39857,39881,42121,43408,43968,47311,47871,76379,62925,49822,74848,60072,56613,58501,72917,109474,86089,64619,67574,67726,72976,71806,98510,78295,79738,81978,116685,100581,131461,91279,95182,97693,106435,123120,147892,118573,115114,179352,126075,132193,132345,179411,173257,135300,163085,144782,204128,158033,160273,182559,186461,195763,223701,251217,239171,277104,212807,221549,233687,244648,263355,241189,258268,258420,264538,267645,298385,293333,331243,302815,344494,318306,378322,342832,537556,410162,445250,480452,434356,830889,466197,446494,455236,512293,485837,499457,979909,516688,585951,532183,560978,591718,804143,675737,830599,662800,912691,721154,788082,844518,901730,945951,1031640,1343975,1933370,921433,987419,1041187,985294,1002525,1016145,1776550,1048871,1336326,1093161,1282132,1436236,1338537,1383954,1450882,1507318,2346500,1509236,1632600,1746248,2635125,1867384,3442606,1906727,1908852,1923958,1972713,3541452,2558107,2385197,2648745,2142032,2331003,2375293,2431698,2943554,3205921,2845855,2834836,3083482,3881565,3840097,4254961,3652975,3613632,6516690,4237730,6045330,3830685,3832810,4303716,4114745,5221148,4517325,4473035,4573730,4987887,4706296,5210129,11034015,5778390,5680691,6459487,9046765,7198227,7266607,7444317,7446442,7483660,7663495,11435957,15550702,9876015,9893135,7947555,12935442,9091055,9505212,8990360,9916425,22828577,9694183,10386987,22748929,18984190,17322457,12140178,13657714,14642544,14890759,14710924,16436802,14930102,16474020,35684371,16937915,26413512,17452767,17038610,18495572,18081415,33874949,18684543,18906785,31749534,20081170,22527165,29601683,34555435,30131734,49485537,25797892,28300258,46679636,31828674,31147726,31366904,31868017,33512630,64761051,33976525,65343429,50913559,37591328,36765958,49832269,38765713,38987955,45879062,59310522,52128848,57164796,59733417,54098150,104109142,63696691,56945618,67913684,62514630,62976400,63015743,86598227,99319954,102003698,70742483,75753913,138268543,138730313,74357286,69316178,133667808,77753668,84867017,98007910,106226998,117794841,111043768,134699286,117074550,132331921,119460248,119922018,125491030,147882760,125992143,140058661,143673464,212989642,145070091,195675931,147069846,152110954,154183195,159224303,188797436,211421476,162620685,215082460,204234908,225687246,245743054,277601984,249406471,236996568,307690776,272560876,245413048,302065955,445739419,266050804,299253286,306294149,292139937,299180800,301253041,392812900,351418121,425794004,321844988,448418044,441231476,366855593,579667939,429922154,714468848,482409616,486403039,591393223,503047372,511463852,517973924,666108879,558190741,565231604,692066186,598434086,591320737,658995530,1021242891,623098029,1109294661,1047641220,688700581,751767142,796777747,1076695456,1025851123,988112895,912331770,1470522511,1152511918,1710702659,1828462598,2494571477,1076164665,1083205528,1214418766,2458635406,1250316267,1189754823,1548544889,1280021318,1282093559,2102086593,3018217421,1440467723,1485478328,2956000839,1827931807,3965093988,1900444665,1938182893,1988496435,2265919488,2159370193,3014347558,4228766324,2272960351,2326480932,2333521795,2297624294,3548013047,2440071090,2469776141,2675233151,2562114877,4705990578,4297707948,3706387211,4314977367,3378650616,5865757404,5448457712,3728376472,5316833509,4261456786,3926679328,4147866628,4425289681,4432330544,5347869353,4660002727,4570584645,10013624032,5940765493,5818721706,5002185967,10867943371,6859822825,6936689937,15361493385,7434763683,7107027088,7803940297,9709914498,9076245825,7655055800,7876243100,15650679991,8074545956,8359009872,11677611733,9434516511,8857620225,9002915189,9662188694,9230587372,15939605126,10820907673,14821636895,11862008792,11938875904,13796512762,14043717025,14371453620,21112128244,14983270188,18068924370,15729601756,16657970989,15531298900,15950789056,16235252972,16433555828,16932166181,32174858098,17860535414,26162753553,18088207597,18233502561,21169463276,20051495045,25642544568,42995765771,31657048176,23800884696,25735388666,29526114518,30606706592,29354723808,32384344884,30514569088,32608760045,31766551872,31482087956,31964854728,46465358144,34521763425,42076100396,51377933234,41889092293,77540686787,36321710158,38139702642,60122594854,41220958321,72521880289,67665817160,53155608504,49536273362,53326999214,65847824676,58880838326,59869292896,76410855718,89517635876,61996657044,85857983520,63248639828,63446942684,102863272576,70843473583,84058036787,74461412800,105336034977,89477318662,77542668479,79360660963,91295311146,90757231683,94376566825,142258680394,115323656258,102691881866,112983216046,112207837540,172077130436,118750131222,121865949940,198276805658,137710052628,125245296872,165940521694,126695582512,145304886383,148386142062,279968733022,204278527192,180772629808,156903329442,167019987141,234073787480,317382016819,484247260214,256697753377,197068448691,214899719406,215675097912,224557831806,245445713734,292980467348,240616081162,275653460664,248561532452,251940879384,262955349500,270550183255,272000468895,275081724574,323923316583,428836358998,337675959250,423717740518,347792616949,353971778133,382695085053,411968168097,449009328075,442514162425,412743546603,421626280497,430574817318,440232929718,500211292470,486061794896,489177613614,492556960546,500502411836,514896228884,522491062639,533505532755,542550652150,547082193469,599005041157,784546595451,685468576199,946797658106,868868007017,1311382169442,736666863186,794663253150,912954839073,834369827100,843318363921,852201097815,921837572967,870807747036,926294724614,993059372382,975239408510,989680025450,1039639154015,1270172395941,1037387291523,1574244449667,1331628788920,1284473617356,1460037032542,1955640972140,1422135439385,1480131829349,1531330116336,1571036690286,1579985227107,2029319179465,1707618092223,1982739397832,1677688191021,2192009968908,1778495822429,2441844437322,1797102471650,1901534133124,1964919433960,2307559687464,3445051263309,2764605446705,2321860908879,2791665821462,2616102406276,2862958905256,2706609056741,2882172471927,3553776088118,4499569656372,3544904661067,3328432587986,3151021917393,3358481049536,3672537526183,3486113914652,6814546502638,3456184013450,4100356731308,3575598294079,3698636604774,5229966721110,3866453567084,4272479121424,4629420596343,5204033380806,5556271268167,5569567961997,7245523002619,5322711463017,5588781528668,5857630974134,6033194389320,11087597695244,6695926578460,6479454505379,6509502966929,7184750519426,6814665062986,6942297928102,9268204566771,10662614985663,12847859452306,8729777327651,7442051861163,9859387317453,8138932688508,8495874163427,8901899717767,11145052796835,12284708107128,12531079456770,10892279425014,11621975917988,10911492991685,11446412502802,11890825363454,12512648894699,19022151861628,21159029930225,15544442390637,22372036212152,16801685245555,33690109386995,14384349789265,15937926024590,21807667782498,33283529203837,15580984549671,48864513753508,16634806851935,17040832406275,25130681015362,33429643700486,39412868618427,21803772416699,23424141886384,22338691927816,22357905494487,22802318355139,52451795562114,24403474258153,26896998683964,31125426940308,31425182195540,29928792179902,29965334338936,30322275813855,37384756966370,31019156641200,31518910574261,32215791401606,70838050813967,40058948738319,38438579268634,33675639258210,38844604822974,52027679699326,44161677911186,69166880636829,44142464344515,45141010282955,44696597422303,45160223849626,47205792613292,74661931761239,51300472942117,58322180879504,60251067993757]
# Test data
#data = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]


def lookForSum(i_, preamble_, target_):
    for x in range(i_, i_ + preamble_ - 1):
        for y in range(x + 1, i_ + preamble_):
            if data[x] + data[y] == target_:
                return True
    return False


def solution1():
    preamble = 25
    for i in range(0, len(data) - preamble):
        target = data[i+preamble]
        
        # If we find a number that isn't a sum of 2 prior numbers, that's the answer
        if not lookForSum(i, preamble, target):
            return target


def solution2():
    target = solution1()

    for i in range(0, len(data)-1):
        for j in range(i, len(data)):
            s = sum(data[i:j+1])
            
            if s == target:
                return min(data[i:j+1]) + max(data[i:j+1])
    print("FAIL")
    return -1

    
print("Year 2020, Day 9 solution part 1:", solution1())
print("Year 2020, Day 9 solution part 2:", solution2())
