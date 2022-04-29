from time import time
from typing import List
from heapq import *


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        # TLE
        #
        # ans = [-1]
        # n = len(heights)
        # m = len(heights[0])
        # dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        #
        # def climb(i, j, cur, seen):
        #     if i == n - 1 and j == m - 1:
        #         ans[0] = cur if ans[0] == -1 else min(ans[0], cur)
        #         return
        #     if ans[0] != -1 and cur >= ans[0]:
        #         return
        #     heap = []
        #     heapq.heapify(heap)
        #     for x, y in dirs:
        #         if 0 <= i + x < n and 0 <= j + y < m and (i + x, j + y) not in seen:
        #             heapq.heappush(heap, (max(cur, abs(heights[i][j] - heights[i + x][j + y])), i + x, j + y))
        #     while heap:
        #         curcur, ii, jj = heapq.heappop(heap)
        #         climb(ii, jj, curcur, seen | {(ii, jj)})
        #
        # climb(0, 0, 0, {(0, 0)})
        # return ans[0]

        # I like this solution, but TLE again
        #
        # n, m = len(heights), len(heights[0])
        # dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        # seen = set()
        # heap = [(0, 0, 0)]
        # heapify(heap)
        # while heap:
        #     cur, i, j = heappop(heap)
        #     if i == n - 1 and j == m - 1:
        #         return cur
        #     seen |= {(i, j)}
        #     for x, y in dirs:
        #         dx, dy = i + x, j + y
        #         if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in seen:
        #             heappush(heap, (max(cur, abs(heights[i][j] - heights[dx][dy])), dx, dy))

        n, m = len(heights), len(heights[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def possible_to_go_with_k(k, i, j):
            if i == n - 1 and j == m - 1:
                return True
            seen.add((i, j))
            for x, y in dirs:
                dx, dy = i + x, j + y
                if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in seen:
                    effort = abs(heights[i][j] - heights[dx][dy])
                    if effort <= k:
                        if possible_to_go_with_k(k, dx, dy):
                            return True
            return False

        beg, end = 0, max(max(heights, key=max))
        while beg < end:
            mid = (beg + end) // 2
            seen = set()
            if possible_to_go_with_k(mid, 0, 0):
                end = mid
            else:
                beg = mid + 1
        return beg


start_time = time()

_heights = [[1,2,2],[3,8,2],[5,3,5]]
_heights = [[876152,480136,914305,818785,744219,482979,803034,224126,795699,612972,431503,650200,819501,878173,117519,911971,530299,511070,332967,464758,473678,336858,576080,142257,431902,953017,276039,946828,617285,809125,875219,915600,116826,949029,734733,496152,454662,945192,587521,393008,91056,491827,983229,541842,530615,370176,373018,372680,721423,691136,277853,946141,781544,340278],[828513,253737,132657,676643,861797,179520,443807,777647,471903,975891,61085,111340,953163,340998,428463,898115,379770,773460,215540,392731,553132,181221,33587,373650,430933,799566,401867,689219,458247,547835,602000,231142,609570,186083,597077,546736,44835,269651,366520,106341,594364,76673,265870,984707,480318,327081,459132,982250,619838,764702,675125,531001,450352,692830],[286403,26253,491802,675415,242889,491095,946974,403351,675228,299034,68601,861564,975151,596498,647048,54852,938436,275891,334362,24407,81829,682588,110159,993142,415501,350251,554403,173684,523489,28764,338384,846732,298022,634375,384678,922302,781542,584221,559098,956366,695252,238468,178528,743068,908459,373261,51326,26505,554297,683672,687860,864035,409775,760769],[846167,72302,465131,667049,848077,943700,929925,701424,357815,678987,741601,171980,520316,174640,569453,727574,640318,945351,861571,931354,405945,917398,408382,409271,513104,332742,594756,42800,400754,794103,458879,211829,314924,134259,241698,560603,240199,6133,389624,220553,414402,615987,531896,513041,158840,631550,573462,500857,720909,904379,66122,992486,476658,128118],[96213,10874,50959,141337,729441,479597,898942,471706,484515,891679,450654,132625,436211,512074,653147,121108,150188,302750,871721,310224,541034,676114,233861,583288,42784,321684,832918,533659,627371,214334,815909,990926,501534,551114,264777,913375,202081,958725,929385,610412,972029,301333,722244,493869,526702,550029,786464,898358,217766,971802,971075,427878,910185,87923],[621051,234554,964172,32317,187197,927546,85928,303419,209893,644199,391596,81449,654240,389565,397022,944498,864011,526517,560839,737281,935890,354791,933509,944294,883936,902514,740011,343056,455045,405952,462167,32330,204948,304982,74449,714522,470470,124231,502150,797090,819545,960690,938679,933070,11545,71158,762515,44022,391882,849505,316455,682370,81067,546335],[902793,107842,63536,386863,310571,740760,815908,682770,730935,572735,693535,476043,684278,241118,814544,704525,360302,25569,285290,829078,308950,983131,380492,256493,248359,427769,164753,367837,264404,610302,665006,110402,618756,289141,762924,117876,713780,824508,475848,182263,262631,135355,701586,474906,227697,538210,958364,815318,40958,421642,151371,156475,119465,124095],[512811,611820,745671,442868,268027,896274,139645,211612,870641,597560,698270,680598,647411,394297,407772,977397,846283,177944,627039,157517,832836,288540,669587,369677,875567,962094,144921,849859,73735,230190,276588,210802,868671,216945,871536,64969,484565,15359,463342,889401,803446,564710,981655,364550,952556,291398,327959,723564,518385,892492,311245,937746,203165,890807],[492224,582273,594570,915633,589139,115877,850490,176384,46434,481230,230473,126408,333659,523784,908187,214814,737174,400953,914907,370454,696726,219774,809987,732560,628943,234059,279788,961292,984653,214839,15379,207498,586197,942635,71221,594177,975645,739031,836092,589730,267575,7753,521101,406134,747958,971865,530161,162908,532586,584249,15985,203139,584187,849733],[150102,512040,85344,34725,688930,830618,740196,762292,131539,812114,193305,167104,480021,623967,841801,205547,659998,998921,184590,594021,220696,333747,360322,650392,157717,577667,156859,931533,267555,604633,872640,269340,913094,655644,690647,851950,924328,461013,537715,70646,187082,421817,800897,210428,269066,518853,212855,581059,706965,821610,849203,454848,458926,769242],[303557,730357,172977,609706,48890,885812,800273,103915,710316,835855,964020,368211,342418,39801,251102,302571,212844,605776,112033,108923,496802,714602,997876,5270,685152,882450,441207,968663,317334,60610,649270,186925,884913,523746,216997,613194,877304,982894,317754,726669,912593,816847,350416,320212,620526,804555,246081,306094,842815,40990,770012,716636,38640,532132],[628330,558330,737521,93039,873545,683728,891226,146454,410673,825254,760886,237450,764903,682482,266023,551428,200963,145430,970750,596649,24210,250782,918244,79312,471402,857686,198980,16586,404088,36388,995985,686347,531695,897851,906574,38880,347701,501971,43778,183599,199063,142931,844225,168737,114082,38018,84875,102336,814660,158814,711772,64807,378133,645130],[926979,976814,39101,815508,586505,359459,975431,626871,173393,232158,67298,487582,787855,314525,707113,910538,359714,274175,475372,437459,360650,323441,575932,873898,184469,500431,372777,660741,981310,286177,237579,320462,756397,609852,663117,969655,408085,390380,697264,920851,115435,282636,90862,545361,974334,34687,488175,735264,926322,940915,514623,383261,687313,586444],[277924,379718,85802,253818,213702,58315,519658,21363,272276,574707,746615,217932,23313,351484,382582,905730,407125,828063,624208,307903,84767,32222,161739,789476,532291,628578,921784,806174,470509,497808,330645,158764,3983,955284,172722,413861,803535,892278,565678,938023,951792,796235,924340,376765,118745,835822,882760,413951,63861,141674,439333,147678,76343,198675],[434023,497533,877816,83006,772380,173132,499929,322440,15622,350548,390159,124342,646058,369654,544447,102298,466901,626134,987549,524209,387583,819282,247813,484364,447306,559917,107384,873017,630164,894913,721024,166838,560037,167982,879443,87090,673078,922528,971961,802014,63723,281825,774272,182836,720735,227095,625392,224486,395833,249845,20685,784119,562364,33007],[100860,346040,291707,747067,345335,496494,70635,370064,718010,617736,973348,162026,641845,113791,578717,107780,712172,465586,610034,878300,877463,899952,451479,507757,243672,341830,482815,207498,742525,359209,919266,973547,308250,187293,10769,472437,978978,808506,478562,97404,567987,683383,998198,142032,257414,352168,756658,45027,205507,597794,119108,640261,897593,622644],[320249,424093,215216,174512,771006,117250,817380,437002,959817,338317,188760,349355,592929,49434,23855,5892,676275,843381,833306,633089,928477,405625,613623,264453,865499,591361,126367,599260,438839,609419,400331,602497,712869,345615,509999,537302,288373,643506,629789,705944,75155,852725,825610,356719,263622,468460,873686,404322,249074,815711,203155,660976,266768,720706],[794692,103985,57537,808479,14331,950922,963013,42513,328286,979862,158608,17954,901656,376162,431818,855273,181586,470753,782776,690579,821729,962482,410164,489071,443156,486678,197296,207741,892761,571200,161557,527107,728845,298363,279790,640312,302840,674666,805767,188880,891002,56917,32019,696243,287158,396769,800728,526866,918974,431771,916718,762919,917216,301530],[817526,633624,922098,953705,795515,290202,21162,286579,28453,667253,426000,37450,985090,964540,62561,529396,159354,756832,235753,303877,428394,128065,643417,215047,645397,411673,999477,919433,8981,412968,642883,923101,248834,282554,845198,447820,60794,863117,955842,17865,832587,841468,472699,609736,618177,400550,133267,650757,218571,899872,983018,351037,518680,508691],[747672,65711,507470,999036,214150,248114,508700,722125,348546,292893,113924,674727,676553,735821,726379,952859,116884,121355,555846,918183,43958,653218,316425,952431,474274,779952,310732,605791,569302,415897,900201,214408,160305,987821,805828,910316,313202,123697,349891,906479,186516,542262,565402,768560,674257,345990,6243,983849,65941,471425,578601,35217,645352,421196],[272148,80297,384262,358770,480855,890468,670214,448685,909283,969533,415993,400477,76138,513144,22405,103780,980639,159454,425411,719178,600950,860174,821202,448432,982871,166250,777235,510635,259844,81407,156887,839435,259261,955919,870167,294496,502340,104191,300443,684136,892822,810931,71271,590307,139232,930515,678879,470028,576302,61042,813975,225632,146715,939049],[45433,444464,210990,959514,881142,50615,501175,621496,416835,691798,442019,613137,684021,567858,169341,467774,730375,340077,797855,324814,902481,472512,396107,391181,180746,43504,978803,22166,965974,607235,700718,515668,661557,162882,212705,504087,566235,39305,297388,796594,631506,680070,543693,219352,69689,717816,696135,357250,890723,254130,704986,272295,745234,122354],[170207,859449,269415,719125,897037,465685,338669,90473,440221,857499,168977,170759,758130,511649,469391,948141,44133,478785,893219,793703,412302,59189,547064,198415,970004,6499,474808,55812,95364,150571,323855,817352,89819,461905,877671,772855,761541,148611,241305,244690,545177,946435,806152,405890,541971,798202,387818,339804,672529,682059,847180,418963,986946,280566],[93198,812418,823593,376893,978902,955578,924711,430600,684368,647552,119914,253054,619154,531779,343122,777037,819395,207861,613391,838132,599555,520098,395103,756757,536389,144685,300881,679439,588040,106497,536872,343974,112029,627988,678178,456666,366615,977070,778676,278505,80951,996057,121656,344625,42859,2729,843845,566798,515849,233487,323950,326357,957024,754261],[905438,838252,370038,935586,645212,652815,757581,768712,189499,896081,324570,137895,576294,396331,320042,804531,603273,886056,224250,994701,176694,274166,295871,368883,21226,566994,558161,350225,777215,807892,326349,988116,704302,409354,246468,29106,787646,297638,399471,590546,351000,508740,271384,801800,740677,579501,99457,124231,254727,985891,708608,369140,540433,265096],[476239,463615,278708,20064,942701,753876,251204,722324,701990,818413,589233,813596,846433,88531,809761,575459,760965,723401,442542,109698,118346,521129,685755,337502,389613,956746,334775,983265,834151,263290,803785,993137,45525,63099,622780,963391,867569,254738,269349,538480,938927,501610,337759,602803,797433,509527,752787,54763,664348,289058,260290,990115,111258,428465],[307464,791219,949775,488395,781223,716324,242764,442898,31353,54962,230219,593910,865773,843281,160928,927199,765166,144079,818164,32797,4643,715244,838525,119898,315256,625686,406986,276263,407587,254956,413414,559500,699771,832285,12314,904640,739678,517078,932558,386400,522773,735250,191496,367402,775266,511257,698455,390966,876999,799593,604266,843083,994896,998641],[426894,583514,18021,96685,205085,456515,288085,682784,307081,178368,907957,658988,89383,315504,616327,831667,272774,522407,700117,534649,268041,551106,766906,35661,913185,104725,373507,478614,475811,436230,246840,564115,350740,930398,240923,586554,591013,121023,972402,895551,239831,542314,956874,331549,396313,769078,62996,413358,590714,196319,77755,437670,682235,126540],[62034,210684,640416,860525,202648,367756,943119,802088,472776,337352,570325,659753,216786,794045,344993,726774,3998,930163,629989,790239,557861,127136,45544,267339,315693,118549,696149,586255,168764,577865,648436,599693,440952,867347,368474,431787,948016,112084,535558,125006,425421,931914,611852,430700,556910,277536,909894,451393,942665,631249,142915,189143,551247,77734],[676227,212680,988041,547929,216286,692538,743426,348969,135017,416952,846475,229728,172561,776925,774481,511348,826627,775073,300708,510754,936580,218926,210264,443697,380324,242380,758420,83626,806054,626727,583405,574906,342897,63389,126281,963183,648326,986643,555110,540895,744602,740901,858698,690372,724067,796054,285811,994893,668534,325403,889262,976856,439568,490190],[592878,24014,959277,130322,980523,276380,418025,987379,347626,769601,899513,544425,528255,570773,908191,371039,946034,907913,834202,137322,155260,811022,707996,350087,644743,811897,413341,702201,463060,981205,528332,164514,177586,665925,729846,116882,520457,373877,12541,58805,975641,362376,195934,729747,655812,826682,427866,255391,984410,420407,735168,659621,85448,102578],[547486,434451,172820,973632,611401,490788,457220,869722,361512,286432,459025,654497,278607,894669,211149,954886,134970,436917,837017,51372,544576,101037,612436,837484,661720,868976,179762,530890,751140,876057,514957,705445,59788,736237,124101,247667,711142,988737,913924,278512,291659,885894,605865,51203,318642,173503,849013,131258,502441,991410,626354,892193,234248,33824],[209855,639946,905486,149500,253848,409325,561513,234334,771711,777979,145558,653606,731555,686738,447785,8208,811587,762060,913542,551451,814994,142444,308946,154735,406673,649585,976269,399433,513802,493229,790680,177911,812615,409589,966267,298149,879602,45162,508304,217581,393385,476824,138427,618332,647882,71427,498054,223994,852062,119674,775381,681447,543542,699129],[444309,905633,689648,101297,667170,893741,294200,115896,271080,85144,481240,131817,174484,540277,531509,287139,939428,5020,96887,958201,164807,60195,645443,76342,76894,522200,459378,825606,873364,179272,237480,426343,505902,464114,481423,95953,924079,158580,505901,178249,260123,153237,496684,861484,553617,216338,337121,794180,208361,626797,923912,183793,275963,183835],[821204,430934,784240,273182,619945,844268,328465,374194,261071,198633,986141,531922,24673,645588,256265,33786,354104,809934,384941,927629,336952,271306,938182,808222,80040,818614,583095,308267,849607,455484,555590,482618,122044,714500,306143,170880,231603,186507,263072,45398,103603,502097,224468,417565,502244,52378,891256,239417,732809,932505,385966,257483,215024,933958],[839947,667290,235728,399571,826954,405458,915555,857755,163762,12991,829984,587743,375339,415218,762837,862855,47891,610716,830723,731885,349481,992744,517993,540381,746321,743685,163212,601292,233755,888617,48509,340879,86135,106770,50962,678810,143394,90150,147919,471864,250732,527072,160724,369862,834103,600800,529311,735779,745966,300469,534373,512894,73529,237021],[973869,922291,571033,152595,314413,800259,238891,93204,934943,120845,739919,532230,482429,63658,573427,257309,25183,223999,345898,654052,772298,968284,406910,633037,508893,48329,26797,456507,69285,885135,803886,647517,57226,439513,393685,594836,978333,525067,320820,518335,299998,542263,450070,943900,114772,228871,327475,125438,99817,953846,901253,966027,994278,296630],[103038,300699,691987,825035,438521,598123,445559,899349,782327,692565,214779,751414,259542,171586,89145,242,919529,558520,653694,375595,849350,725427,288421,24468,571641,991239,823241,502867,374094,523962,626948,615306,515770,916506,441840,118266,274158,460448,14951,917393,446527,641012,857818,680709,179037,794962,894320,248083,451045,278267,312737,22655,680088,638749],[91439,355719,18830,589156,916804,188781,533059,4016,959598,886389,920362,739711,156831,832795,438889,178661,209892,127721,460036,761845,575344,27002,40008,65753,475015,400347,80144,57204,510665,46388,112917,831380,400518,74909,881371,219212,278606,496171,661137,285618,68929,9100,12190,2168,66435,488799,862824,418682,624758,942751,116993,190835,670820,780313],[664833,573262,579033,389258,891241,729427,22675,869143,31869,178336,159378,651660,774916,188960,435420,646077,325432,944364,138830,880342,1674,248169,375087,753712,291160,601237,437218,62570,308187,38063,293850,714706,279844,500901,92698,478075,977534,583820,649726,413927,416916,462755,677636,45248,441621,777395,812264,588059,758513,946729,413094,16309,361328,442629],[663253,826348,267331,840542,580668,123132,918339,211525,666318,794085,382138,954915,48905,717195,561694,637067,844308,382568,256874,218596,480151,458625,95979,185068,366263,352973,38033,463834,81315,171333,686618,272667,431133,693274,657627,144934,873227,569132,584982,156429,452072,275285,454258,497331,550824,676281,545995,73348,746593,898872,500827,454506,755575,446582],[626104,53280,632347,969040,207077,474598,536373,605278,920818,601557,186596,280896,157249,505665,470786,373901,227017,579569,940813,178139,923911,385667,617046,574198,789014,16528,906198,484354,541582,564622,986841,458122,69904,435775,292944,68171,249205,863863,822154,489660,441699,666401,461930,979754,710662,924498,318149,740717,979646,975940,719872,354669,666330,628946],[897610,441744,345540,37801,999091,603265,135471,634527,543204,580814,184463,789784,10442,801927,745810,215268,927670,584394,831224,180966,946964,991869,369322,335020,689873,153711,240805,514911,156976,51544,780441,253488,727461,455191,817674,339945,746444,929818,429393,85989,773007,420131,564808,736524,105876,268629,413413,619696,167046,96849,91803,459956,799559,832513],[736950,422098,18989,335885,459390,217120,550109,318655,182100,770149,61230,888786,143368,83028,215948,800484,386959,897587,383751,525502,512136,442757,984900,28084,326157,575170,970840,22672,589482,975202,200444,659951,70733,355937,344112,818047,516316,622165,516912,539727,980043,908268,652267,978042,755754,754836,844660,563200,891677,573563,660856,30466,469470,944472],[169961,523011,437523,481727,621849,734067,546476,625757,851948,597043,226530,580563,623772,51635,481609,154179,306055,849091,332385,556502,670968,898825,919581,567773,616049,43419,530942,983352,579968,379372,868924,763227,610875,921746,510519,487688,101351,30812,676662,607779,60736,552212,81138,571611,227794,681202,360597,364901,562395,480501,472066,306818,853067,489724],[742129,770092,493802,273869,897362,153651,168619,950298,952964,501910,630708,669728,595885,848072,892103,245951,95327,274607,39289,121174,155956,107385,217255,685862,797632,685331,669827,663480,223270,146569,289804,367519,306434,455169,724075,431320,196261,748941,135770,966950,601453,572110,652749,980360,374682,820405,95524,721856,693627,883915,20944,142398,815862,531368],[17320,909643,898632,468284,432960,580630,642525,35329,186478,260125,785237,54843,110807,204783,304487,238006,31284,192031,860571,774292,974833,933455,705116,805560,67604,982374,417981,181784,604900,366370,739247,979778,745128,257538,377998,725746,611824,68838,20009,90482,855261,319143,634267,13292,730904,69438,488840,962079,965778,571924,941082,402342,767425,191990],[99957,914442,16432,401270,744733,655882,652433,154108,814714,872214,207267,17897,598383,764952,614057,777808,111082,640963,545580,457133,691503,411631,831756,918529,723216,825876,106910,150622,989909,668184,63607,679080,625828,864148,311693,355709,215368,508019,155877,846758,953967,880094,67415,480919,967208,974499,783164,622602,903746,300058,325258,646644,906728,592340],[347089,240099,280065,468385,158642,971023,989065,81639,726754,400605,224696,698225,539475,35999,896265,377057,530350,296905,138102,216058,474310,448073,959294,192691,830677,901581,420189,274566,902117,246136,438563,325147,577636,898002,32060,335773,560072,369488,127618,898296,342481,77772,513648,779674,44939,823161,764161,935378,291378,984701,232646,146361,757591,697151],[605800,131132,362262,895347,610090,41209,726495,339947,141346,893363,632123,607267,472966,559761,438976,505096,847235,408773,721660,127321,34319,842583,814521,538224,769051,72474,3665,830034,639310,83347,610160,756583,883554,383328,245260,346997,823223,737266,891683,610881,760245,922482,9149,179637,160157,513939,78820,957051,601958,569787,213471,731314,811536,124832],[757064,258008,501127,282541,925626,496237,828593,67845,222848,552271,754545,780217,325485,382546,549358,604950,891893,304057,55683,813892,924760,374211,718350,33817,81622,215063,503741,820960,605774,414944,897883,864118,532018,769582,350995,76226,855902,392337,59767,695757,702907,160924,924867,360226,496946,419020,130788,757036,619037,867600,594913,633089,64370,222528],[794072,880827,578275,36222,283097,204071,863707,416324,811458,958989,44703,418584,584167,763785,755317,981287,882022,170035,81078,755880,583338,26581,161153,983630,929354,355631,922053,524160,776661,167747,14548,735080,539789,69325,678944,383950,837787,881272,956229,608483,885257,937640,789524,888499,241451,534844,607250,39435,961605,503484,633506,167106,357164,677942],[532473,26085,563439,241512,233618,653473,604856,767139,326474,267512,506271,908812,881670,925073,244812,660776,468906,255564,148735,267698,566157,682877,631785,200389,874271,346407,949522,256177,177346,849217,724331,162894,881224,270166,749365,540820,100469,859341,18330,320811,667160,915908,545264,232144,416594,221309,332089,778688,568081,680036,905072,180661,31269,546981],[878207,882794,425875,337046,610660,926155,660345,583883,945674,242809,480053,316693,622917,636619,445128,433650,940934,121949,23845,954598,784205,372531,788878,305446,965400,112945,730537,208901,792141,326509,181391,797963,920253,630777,417758,76047,558307,46583,142999,850111,683527,753844,254945,825361,78400,95989,991272,19700,369897,207470,63271,511614,553388,584282],[669134,772839,183595,790667,632720,94419,236373,576120,555701,994440,699462,649228,204607,928256,478829,767986,824605,652895,978527,625740,821828,250687,956404,734603,789862,249000,855113,149364,500788,493708,438440,462534,663829,355556,787234,297495,816438,692169,26273,64272,220323,2084,930553,55334,352862,706572,22320,691874,188683,933883,700041,736113,590585,696174],[590405,861610,130116,414475,25787,914571,958237,505601,701155,943623,124189,757436,131005,45462,632132,484404,505533,479079,113652,793280,372964,37273,170502,436445,732395,399376,658834,761642,639771,621542,325712,955098,654609,518909,185280,202678,257426,740696,337196,963908,61540,848582,516279,492411,966122,469775,191771,216622,673171,134360,715404,369252,881535,281942],[25685,470030,442417,860064,877809,945112,151506,802096,519454,538302,821175,523386,908362,581456,775849,627312,126491,428237,29598,637316,625883,5100,995838,852310,357364,171166,495417,468407,962511,952092,7540,373963,944182,257580,798008,586053,441740,516132,317365,401957,768557,420856,909188,969795,324533,435253,771455,512024,664188,524879,549415,986850,470321,2087],[285366,567057,988806,110568,971076,47641,589334,436076,410769,33892,261515,407750,185201,562744,840237,483625,546798,837106,546773,196839,745177,705659,930877,403266,530404,245790,809586,735445,68665,419014,819385,379453,717837,544074,23318,645982,505558,950144,1894,480872,353854,643695,801266,899758,599811,196478,617700,204041,430765,87560,23931,120514,875224,174693],[816222,893056,206859,431274,937040,713338,410461,687050,161138,44791,193871,421213,628648,370642,353796,73061,340966,728790,74133,890501,410387,405660,396284,522936,670512,900421,353548,793439,378195,894233,721148,379489,57816,950975,918739,2150,152373,776106,206199,212110,629064,13993,979483,932668,281301,608941,540084,384063,516941,266288,465933,750854,97361,616931],[796807,794939,993439,417932,115649,271211,909387,237262,110465,388335,437203,548018,146011,90414,745976,70496,370573,954591,890610,103334,401697,573851,904512,391198,660680,488950,115124,909113,564622,999626,874750,971801,154086,99795,35435,363093,572579,705420,267467,397030,414386,121743,315794,391851,420117,567026,644190,340008,140044,729946,293205,404442,686230,942423],[550956,274655,822987,487247,269394,77253,370142,855111,498625,420185,719394,424310,853575,384689,521423,748838,769659,934804,891462,669785,496777,590086,283438,308669,662732,772833,683875,606428,852092,480990,555744,114717,704536,109379,4655,545098,740559,138440,717393,329765,931760,931914,118341,83582,856773,94151,130888,587353,860287,847869,216918,745353,465429,363228],[107404,352344,223009,989054,128238,765534,836643,433915,459828,783359,686577,774929,854977,904142,700557,522769,736373,337960,717762,26128,154895,956765,671565,870026,518470,671906,34106,361678,836802,708944,312107,128490,393778,255563,973619,298778,40616,571923,453981,830769,610357,389472,586391,777870,551902,554556,240001,43263,536461,410787,724214,750671,51397,861815],[259258,184080,41033,718294,261902,2350,658404,967179,353750,836453,278557,416634,641862,251230,92946,577436,205832,922789,77854,582807,78517,366773,546885,237939,876567,330753,562865,377566,43758,974869,578536,30020,587221,418752,461119,800912,83874,523043,661992,489905,512948,224762,53814,830819,407881,677763,370181,546219,123518,713364,133835,974241,737746,299954],[433392,859814,121284,516367,94686,273009,637021,158822,802035,411948,262223,121563,49673,786601,206873,853224,230173,938182,227795,670698,724454,840181,48146,754302,84108,466432,965717,61918,408529,460208,27882,296161,318929,450443,525307,573916,161706,101230,313356,78450,387336,175409,603155,966079,857130,253545,937167,262070,166827,704444,466275,940307,638304,712270],[700818,638218,10002,928429,149473,953534,757451,781773,571441,935871,505749,947984,21868,957661,723442,765561,122486,943729,633622,40141,483728,197198,103111,539156,492322,341709,464811,966627,768317,840832,683745,214683,433036,87673,627620,405419,113668,504134,822581,316110,266548,208961,483238,505053,600813,260361,879902,68493,361201,157426,418923,393710,427495,900265],[378258,182579,481185,792774,657115,778998,484751,830866,110745,374587,192428,541654,938358,281325,768663,560464,363737,82862,399586,41371,462336,63547,606813,862971,886571,927142,391957,134680,106993,269874,742105,671905,261556,885063,294981,700792,44573,764314,100250,27996,143583,854737,686021,914939,2851,883644,251962,614143,322890,169604,597192,928961,262408,935593],[103904,934124,687843,756770,632800,441292,941160,168896,798352,580787,434866,423046,142148,704740,293292,334972,317074,420269,272388,54858,516804,180286,26199,623197,482351,932712,847469,756035,986136,744832,466037,548673,613954,395709,700324,988453,258498,20871,9367,827611,171795,946512,581103,340103,899318,505712,111780,566343,826803,345958,917458,350642,569655,191946],[332112,686767,667376,222427,771641,29949,144574,686999,249308,929685,331049,620142,250421,512630,858770,531769,73390,781631,562995,291446,655941,443357,448363,649888,746501,432782,131906,761202,635480,946541,977288,5776,964101,233125,207320,948772,686168,920789,426121,11296,885485,77575,254119,221777,315696,597493,696263,468771,634583,388009,656878,494156,765021,511335],[530315,835803,405756,849161,858674,703947,968222,553208,815347,603184,600463,719935,339058,638085,43670,498453,433998,583456,517721,709803,13936,597672,676858,481593,973021,243620,429645,558788,160959,129092,97717,70711,168434,476450,421659,158788,740114,718109,557880,735847,19692,55611,310447,818211,895680,511654,950828,405029,248350,367239,449024,583803,485057,491903],[725830,485762,772272,988287,107451,763414,30188,596120,540602,132396,626023,489288,1468,911058,378822,768113,227098,594351,827970,597623,297081,784167,430314,494700,412992,853966,635829,759259,416922,417895,168297,462999,904728,419499,891821,880921,789260,276382,787633,369992,46387,484068,37670,118263,103147,647749,715116,321526,584965,351587,901830,327991,51100,669225],[998278,969990,600453,288026,495709,836916,239220,837246,325071,744581,235595,134067,3908,301974,450203,506917,441376,458634,632857,218428,364274,318880,431828,475953,22035,251384,294334,639004,760744,745598,850668,382405,654647,569578,487211,329813,139755,695347,170999,758965,59694,126366,247106,978187,665217,266957,993485,72290,787034,859353,454376,629144,971080,682762],[701211,138401,352538,360639,406273,361075,899929,169418,877138,805425,942903,924762,789439,313443,975197,618698,408148,364174,610668,953263,460445,73465,130783,479780,39058,484168,300916,672614,956853,511812,828692,732213,393114,192809,549199,212389,753213,857786,656654,251536,708279,181145,823911,721343,58930,110460,738796,155942,886515,550658,511597,1810,925227,491626],[597534,518980,273309,356462,206731,151027,33626,665906,778112,913981,829565,340359,855887,879989,673660,994814,574210,448000,762580,868532,144036,594380,762509,499471,126619,563679,88409,777522,208935,384369,868366,32011,268123,48482,793997,644688,114162,101563,603052,672837,202581,701540,996477,465710,581879,946100,260449,390790,427554,409317,701597,437171,969155,886664],[664147,899672,447091,592500,461006,630711,259500,993227,985710,988780,49377,69010,31053,201533,220318,683102,682450,848598,133800,164896,190174,782822,857951,772927,762581,531192,227273,909691,11610,258323,487408,204842,219762,246595,250636,474176,800421,475308,158785,252360,991034,169988,716712,569526,616512,11511,394935,139592,215410,138424,578125,186330,569891,310816],[834438,277565,437188,915120,779035,268025,550937,186412,344121,988914,5146,627854,227554,939189,663515,943638,522408,448450,493033,567261,434618,749947,916809,662379,206211,985827,519083,205601,204098,605090,964391,246997,668843,933750,483187,838192,401456,382634,617561,273382,531760,400511,680115,730236,479318,374242,14053,629623,716319,690682,967796,630054,257236,838942],[433435,47268,752294,273316,321593,456654,421768,525024,655896,42837,298203,169212,307970,173475,952106,4057,847129,264284,624814,165039,572734,368537,561117,505357,791529,235523,455694,133868,185978,158966,281657,610601,214471,262444,901441,570158,334939,740595,625923,416954,432767,803741,120191,904544,572636,155972,969720,777860,561116,403457,495360,594842,674190,300311],[373407,993181,287673,432266,307283,385617,206086,696654,703953,669725,595933,861804,149542,615042,265947,544249,866251,783367,356654,804039,458433,870978,399445,119117,437229,502981,978186,574330,427123,235254,674111,728002,388543,676097,491373,670256,833393,506599,607426,204974,870423,766717,641393,384611,790800,761687,119021,971101,889999,712148,514810,957077,71421,306210],[770239,946334,808619,517751,529968,646884,425108,618355,861423,825685,438299,878599,700868,229743,913333,316274,822942,145771,650061,995992,524097,796286,712950,987588,782326,946720,774055,655066,674822,872677,852983,55231,367671,588594,709141,781103,560057,474807,84960,652816,913228,990247,486825,196913,342013,200624,30610,752441,219493,614812,509414,583797,601513,571805],[448414,343839,675297,763515,150520,228225,689544,100090,206417,171746,997458,233462,430824,627105,517890,805768,787977,49613,724222,528737,15201,769421,974340,467611,929141,466087,303663,73730,729925,578307,277334,946174,338298,738558,983580,696540,81218,429785,233613,645262,579424,483156,486895,404968,438757,288454,929289,418329,32162,708770,370915,543745,654138,590013],[679265,447724,183023,198465,720324,560098,161537,790286,952250,946162,186029,65296,697749,160713,982996,567841,750132,781710,826368,547151,775894,134155,475022,558831,859851,881811,526892,44697,971409,993784,762231,193366,720227,219523,693371,332693,376424,24382,427512,25115,984089,742874,305750,172061,39787,879982,174780,520382,146701,168818,907368,321649,637234,811301],[680599,549407,899124,169052,12849,212332,9128,368382,147443,554263,319344,753713,928712,884731,918929,131188,511346,984178,328600,934609,315676,114376,294249,753252,724069,29761,230163,13316,794936,40741,178197,265239,661749,234256,885406,924931,882990,122567,742346,979402,198622,86275,655169,218830,787549,295019,202715,993334,283172,801170,778626,913677,76801,816408],[340785,79475,265480,794816,176087,304037,325909,14127,655598,73363,100576,296274,275911,949212,221198,758346,625921,32119,371588,876152,202581,904109,278038,191807,556573,710581,251058,794243,855937,719512,820728,204615,606168,940972,471407,683254,340458,75869,246442,854183,516261,300873,933200,136937,170951,120994,39590,58654,947302,423790,498760,102641,951872,386256],[514065,614169,558936,779979,841655,446030,893437,363243,516789,364036,529704,669263,74188,545983,592486,162457,366365,269789,515016,166589,901334,884356,368182,470793,576206,352722,978144,709533,48863,159994,292091,170800,843121,856750,128395,627475,327373,693084,501578,55136,959026,256501,323934,978951,926793,849929,421494,337059,830318,126626,336574,507913,875963,537847],[841756,522264,684972,551510,930136,342493,705129,621517,16379,430758,617290,153318,359154,704400,320368,605146,902580,102033,599500,293241,390385,593865,26208,830140,7834,841053,81678,78027,223900,205741,351318,328798,655149,510091,99670,369618,990420,462718,569177,482353,517762,704758,611777,649272,990376,68138,953808,266475,821020,420212,233385,612888,917800,366254],[222369,72450,592482,751655,741573,810246,621882,869167,931162,580800,688680,761940,44730,36962,290388,798816,952094,662641,872083,609870,787085,459998,663407,581065,251381,668271,316127,388094,893675,960065,433627,200557,590584,812276,277863,235555,66556,767828,245458,574933,226584,627023,813180,966862,27630,247363,480588,137711,909997,154785,999163,368092,645557,681207]]
# _heights = [[1,10,6,7,9,10,4,9]]
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

print(Solution().minimumEffortPath(_heights))

print("--- %s seconds ---" % (time() - start_time))
