**6.0001/6.00 Fall 2016 Problem Set 2**

**Handedout:**Tuesday,September20th,2016. **Due:Tuesday,September27th,2016at11:59pm**

ThisproblemsetwillintroduceyoutothetopicofcreatingfunctionsinPython,aswell asloopingmechanismsforrepeatingacomputationalprocessuntilaconditionis reached.

**Note on Collaboration**:

You may work with other students. However, each student should write up and hand in his or her assignment separately. *Be sure to indicate with whom you have worked inthecommentsofyoursubmission.![](Aspose.Words.fe4a9722-f5fa-454c-81c2-1efcf06d0bd7.001.png)*

Problem1:BasicHangman

YouwillimplementavariationoftheclassicwordgameHangman.Ifyouare unfamiliarwiththerulesofthegame,read [http://en.wikipedia.org/wiki/Hangman_(game)](https://en.wikipedia.org/wiki/Hangman_\(game\)).Don’tbeintimidatedbythisproblem­ it'sactuallyeasierthanitlooks!Wewill'scaffold'thisproblem,guidingyouthrough thecreationofhelperfunctionsbeforeyouimplementtheactualgame.

A)GettingStarted

Downloadthefiles“hangman.py”and“words.txt”,and**savethembothinthesame directory**.Runthefilehangman.pybeforewritinganycodetoensureyourfilesare savedcorrectly.Thecodewehavegivenyouloadsinwordsfromafile.Youshould seethefollowingoutputinyourshell:

Loadingwordlistfromfile... 55900wordsloaded.

**Ifyouseetheabovetext,continueontoHangmanGameRequirements.** Ifyoudon’t,doublecheckthatbothfilesaresavedinthesameplace!

B)HangmanGameRequirements

Youwillimplementafunctioncalledhangmanthatwillallowtheusertoplayhangman againstthecomputer.Thecomputerpickstheword,andtheplayertriestoguess lettersintheword. Hereisthegeneralbehaviorwewanttoimplement.Don’tbeintimidated!Thisisjust adescription;**wewillbreakthisdownintostepsandprovidefurther functionalspecslateroninthepsetsokeepreading!**

1. Thecomputermustselectawordatrandomfromthelistofavailablewords thatwasprovidedinwords.txt **Notethatwords.txtcontainswordsinalllowercaseletters.**
1. Theuserisgivenacertainnumberofguessesatthebeginning.
1. Thegameisinteractive;theuserinputstheirguessandthecomputereither:
1. revealstheletterifitexistsinthesecretword
1. penalizetheuserandupdatesthenumberofguessesremaining

4\.Thegameendswheneithertheuserguessesthesecretword,ortheuserruns

outofguesses.![](Aspose.Words.fe4a9722-f5fa-454c-81c2-1efcf06d0bd7.002.png)

Problem2 HangmanPart1:Threehelperfunctions

Beforewehaveyouwritecodetoorganizethehangmangame,wearegoingtobreak downtheproblemintologicalsubtasks,creatingthreehelperfunctionsyouwillneed tohaveinorderforthisgametowork.Thisisacommonapproachtocomputational problemsolving,andonewewantyoutobeginexperiencing.

Thefilehangman.pyhasanumberofalreadyimplementedfunctionsyoucanuse whilewritingupyoursolution.Youcanignorethecodeinthetwofunctionsatthetop ofthefilethathavealreadybeenimplementedforyou,thoughyoushouldunderstand howtouseeachhelperfunctionbyreadingthedocstrings.

1A)Determinewhetherthewordhasbeenguessed

First,implementthefunctionis\_word\_guessedthattakesintwoparameters­a string,secret\_word,andalistofletters(strings),letters\_guessed.Thisfunction returnsaboolean­Trueifsecret\_wordhasbeenguessed(i.e.,allthelettersof secret\_wordareinletters\_guessed),andFalseotherwise.Thisfunctionwillbe usefulinhelpingyoudecidewhenthehangmangamehasbeensuccessfully completed,andbecomesanend­testforanyiterativeloopthatcheckslettersagainst thesecretword.

Forthisfunction,youmayassumethatallthelettersinsecret\_wordand letters\_guessedarelowercase.

**ExampleUsage:**

\>>>secret\_word='apple' >>>letters\_guessed=['e','i','k','p','r','s'] >>>print(is\_word\_guessed(secret\_word,letters\_guessed)) False

1B)Gettingtheuser’sguess

Next,implementthefunctionget\_guessed\_wordthattakesintwoparameters­a string,secret\_word,andalistofletters,letters\_guessed.Thisfunctionreturnsa stringthatiscomprisedoflettersandunderscores,basedonwhatlettersin letters\_guessedarein secret\_word.Thisshouldn'tbetoodifferentfrom is\_word\_guessed!

Wearegoingtouseanunderscorefollowedbyaspace(\_)torepresentunknown letters.Wecouldhavechosenothersymbols,butthecombinationofunderscoreand spaceisvisibleandeasilydiscerned.Notethatthespaceissuperimportant,as otherwiseithardtodistinguishwhether\_\_\_\_isfourelementslongorthree.Thisis called*usability*­it'sveryimportant,whenprogramming,toconsidertheusabilityof yourprogram.Ifusersfindyourprogramdifficulttounderstandoroperate,they won'tuseit!Weencourageyoutothinkaboutusabilitywhendesigningyourprogram.

**Hint:**Indesigningyourfunction,thinkaboutwhatinformationyouwanttoreturn whendone,whetheryouneedaplacetostorethatinformationasyouloopovera datastructure,andhowyouwanttoaddinformationtoyouraccumulatedresult.

**ExampleUsage:**

\>>>secret\_word='apple' >>>letters\_guessed=['e','i','k','p','r','s'] >>>print(get\_guessed\_word(secret\_word,letters\_guessed)) '\_pp\_e'

1C)Gettingallavailableletters

Next,implementthefunctionget\_available\_lettersthattakesinoneparameter­a listofletters,letters\_guessed.Thisfunctionreturnsastringthatiscomprisedof lowercaseEnglishletters­alllowercaseEnglishlettersthatarenotin letters\_guessed.

Thisfunctionshouldreturnthelettersinalphabeticalorder.Forthisfunction,youmay assumethatallthelettersinletters\_guessedarelowercase.

**Hint**:Youmightconsiderusingstring.ascii\_lowercase,whichisastringcomprised ofalllowercaseletters:

\>>>importstring >>>print(string.ascii\_lowercase) abcdefghijklmnopqrstuvwxyz

**ExampleUsage:**

\>>>letters\_guessed=['e','i','k','p','r','s'] >>>printget\_available\_letters(letters\_guessed) abcdfghjlmnoqtuvwxyz![](Aspose.Words.fe4a9722-f5fa-454c-81c2-1efcf06d0bd7.003.png)

Problem3 HangmanPart2:TheGame

Nowthatyouhavebuiltsomeusefulfunctions,youcanturntoimplementingthe functionhangman,whichtakesoneparameter­thesecret\_wordtheuseristoguess. Initially,youcan(andshould!)manuallysetthissecretwordwhenyourunthis function–thiswillmakeiteasiertotestyourcode.Butintheend,youwillwantthe computertoselectthissecretwordatrandombeforeinvitingyouorsomeotheruser toplaythegamebyrunningthisfunction.

CallingthehangmanfunctionstartsupaninteractivegameofHangmanbetweenthe userandthecomputer.Indesigningyourcode,besureyoutakeadvantageofthe threehelperfunctions,is\_word\_guessed,get\_guessed\_word,and get\_available\_letters,thatyou'vedefinedinthepreviouspart!

Belowarethegamerequirementsbrokendownindifferentcategories.Makesure yourimplementationfitsalltherequirements!

GameRequirements

**A. GameArchitecture:**

1. Thecomputermustselectawordatrandomfromthelistofavailablewords thatwasprovidedinwords.txt.Thefunctionsforloadingthewordlistand selectingarandomwordhavealreadybeenprovidedforyouinhangman.py.
1. Usersstartwith6guesses.
1. Atthestartofthegame,lettheuserknowhowmanylettersthecomputer's wordcontainsandhowmanyguessess/hestartswith.
1. Thecomputerkeepstrackofalltheletterstheuserhasnotguessedsofarand beforeeachturnshowstheuserthe“remainingletters”

ExampleGameImplementation:

Loadingwordlistfromfile...

55900wordsloaded.

WelcometothegameHangman! Iamthinkingofawordthatis4letterslong. -------------

Youhave6guessesleft. Availableletters:abcdefghijklmnopqrstuvwxyz

**B.User­ComputerInteraction:**

Thegamemustbeinteractiveandflowasfollows:

1. Beforeeachguess,youshoulddisplaytotheuser:
   1. Remindtheuserofhowmanyguessess/hehasleftaftereachguess.
   1. alltheletterstheuserhasnotyetguessed
1. Asktheusertosupplyoneguessatatime.(Lookattheuserinput requirementsbelowtoseewhattypesofinputsyoucanexpectfromtheuser)
1. Immediatelyaftereachguess,theusershouldbetoldwhethertheletterisin

thecomputer’sword.

4. Aftereachguess,youshouldalsodisplaytotheuserthecomputer’sword,with guessedlettersdisplayedandunguessedlettersreplacedwithanunderscore andspace(\_)
4. Attheendoftheguess,printsomedashes(­­­­­)tohelpseparateindividual guessesfromeachother

ExampleGameImplementation: (Thebluecolorbelowisonlytheretoshowyouwhattheusertypedin,asopposedto whatthecomputeroutput.)

Youhave6guessesleft. Availableletters:abcdefghijklmnopqrstuvwxyz Pleaseguessaletter:a

Goodguess:\_a\_\_

\------------

Youhave6guessesleft. Availableletters:bcdefghijklmnopqrstuvwxyz Pleaseguessaletter:b Oops!Thatletterisnotinmyword:\_a\_\_

**C.UserInputRequirements:**

1. Youmayassumethattheuserwillonlyguessonecharacteratatime,butthe usercanchooseanynumber,symbolorletter.Yourcodeshouldacceptcapital andlowercaselettersasvalidguesses!
1. Iftheuserinputsanythingbesidesanalphabet(symbols,numbers),tellthe userthattheycanonlyinputanalphabet.Becausetheusermightdothisby accident,theyshouldget3warningsatthebeginningofthegame.Eachtime theyenteraninvalidinput,oralettertheyhavealreadyguessed,theyshould loseawarning.Iftheuserhasnowarningsleftandentersaninvalidinput, theyshouldloseaguess.

**Hint#1:**Usecallstotheinputfunctiontogettheuser’sguess.

1. Checkthattheuserinputisanalphabet
1. Iftheuserdoesnotinputanuppercaseorlowercasealphabetletter, subtractonewarningoroneguess.

**Hint#2:**youmayfindthestringfunctionsstr.isalpha(‘yourstring’)and str.lower(‘YourString’)helpful!Ifyoudon’tknowwhatthesefunctionsareyou couldtrytypinghelp(str.isalpha)orhelp(str.lower)inyourSpydershelltoseethe documentationforthefunctions.

**Hint#3:**Sincethewordsinwords.txtarelowercase,itmightbeeasiertoconvertthe userinputtolowercaseatalltimesandhaveyourgameonlyhandlelowercase.

ExampleGameImplementation:

Youhave3warningsleft. Youhave6guessesleft. Availableletters:bcdefghijklmnopqrstuvwxyz Pleaseguessaletter:s Oops!Thatletterisnotinmyword:\_a\_\_

5

Youhave5guessesleft.

Availableletters:bcdefghijklmnopqrtuvwxyz

Pleaseguessaletter:$ Oops!Thatisnotavalidletter.Youhave2warningsleft:\_a\_\_

**D.GameRules:**

1. Theuserstartswith3warnings.
1. Iftheuserinputsanythingbesidesanalphabet(symbols,numbers),tellthe userthattheycanonlyinputanalphabet.
   1. Iftheuserhasoneormorewarningleft,theusershouldloseone warning.Telltheuserthenumberofremainingwarnings.
   1. Iftheuserhasnoremainingwarnings,theyshouldloseoneguess.
1. Iftheuserinputsaletterthathasalreadybeenguessed,printamessage tellingtheusertheletterhasalreadybeenguessedbefore.
   1. Iftheuserhasoneormorewarningleft,theusershouldloseone warning.Telltheuserthenumberofremainingwarnings.
   1. Iftheuserhasnowarnings,theyshouldloseoneguess.
1. Iftheuserinputsaletterthathasn’tbeenguessedbeforeandtheletterisin thesecretword,theuserloses**no**guesses.
1. **Consonants:**Iftheuserinputsaconsonantthathasn’tbeenguessedandthe consonantisnotinthesecretword,theuserloses**one**guessifit’sa consonant.
1. **Vowels:**Ifthevowelhasn’tbeenguessedandthevowelisnotinthesecret word,theuserloses**two**guesses.Vowelsare*a*,*e*,*i*,*o*,and *u*.*y*doesnot countasavowel.

ExampleImplementation:

Youhave5guessesleft. Availableletters:bcdefghijklmnopqrtuvwxyz Pleaseguessaletter:t

Goodguess:ta\_t

\------------

Youhave5guessesleft. Availableletters:bcdefghijklmnopqrtuvwxyz Pleaseguessaletter:e

Oops!Thatletterisnotinmyword:ta\_t

\------------

Youhave3guessesleft. Availableletters:bcdfghijklmnopqrtuvwxyz Pleaseguessaletter:e Oops!You'vealreadyguessedthatletter.Younowhave2warnings: ta\_t

**E.GameTermination:**

1. Thegameshouldendwhentheuserconstructsthefullwordorrunsoutof guesses.
1. Iftheplayerrunsoutofguessesbeforecompletingtheword,tellthemthey lostandrevealthewordtotheuserwhenthegameends.
3. Iftheuserwins,printacongratulatorymessageandtelltheusertheirscore.
3. Thetotalscoreisthenumberofguesses\_remainingoncetheuserhas guessedthesecret\_wordtimesthenumberofuniquelettersinsecret\_word.

**Totalscore=guesses\_remaining\*numberuniquelettersinsecret\_word**

ExampleImplementation:

Youhave3guessesleft. Availableletters:bcdfghijklnopquvwxyz Pleaseguessaletter:c

Goodguess:tact

\------------

Congratulations,youwon! Yourtotalscoreforthisgameis:9

ExampleImplementation:

Youhave3guessesleft. Availableletters:bcdfghijklnopquvwxyz Pleaseguessaletter:n Goodguess:dolphin

\------------

Congratulations,youwon! Yourtotalscoreforthisgameis:21

**F.GeneralHints:**

1. Considerwritingadditionalhelperfunctionsifyouneedthem.
1. Therearefourimportantpiecesofinformationyoumaywishtostore:
1. secret\_word:Thewordtoguess.Thisisalreadyusedastheparameter nameforthehangmanfunction.
1. letters\_guessed:Thelettersthathavebeenguessedsofar.Ifthey guessaletterthatisalreadyinletters\_guessed,youshouldprinta messagetellingthemthey'vealreadyguessedthatbutdonotpenalize themforit.
1. guesses\_remaining:Thenumberofguessestheuserhasleft.Notethat inourexamplegame,thepenaltyforchoosinganincorrectvowelis differentthanthepenaltyforchoosinganincorrectconsonant.
1. warnings\_remaining:Thenumberofwarningstheuserhasleft.Note thatauseronlylosesawarningforinputtingeitherasymboloraletter thathasalreadybeenguessed.

**G.ExampleGame:**

Lookcarefullyattheexamplesgivenaboveofrunninghangman,asthatsuggests examplesofinformationyouwillwanttoprintoutaftereachguessofaletter.

**Note:Trytomakeyourprintstatementsasclosetotheexamplegameas possible!**

Theoutputofa**winning**gameshouldlooklikethis.(Thebluecolorbelowisonly theretoshowyouwhattheusertypedin,asopposedtowhatthecomputeroutput.)

7

Loadingwordlistfromfile...

55900wordsloaded.

WelcometothegameHangman! Iamthinkingofawordthatis4letterslong. Youhave3warningsleft.

\-------------

Youhave6guessesleft. Availableletters:abcdefghijklmnopqrstuvwxyz Pleaseguessaletter:a

Goodguess:\_a\_\_

\------------

Youhave6guessesleft. Availableletters:bcdefghijklmnopqrstuvwxyz Pleaseguessaletter:a Oops!You'vealreadyguessedthatletter.Youhave2warningsleft:

\_a\_\_

\------------

Youhave6guessesleft. Availableletters:bcdefghijklmnopqrstuvwxyz Pleaseguessaletter:s

Oops!Thatletterisnotinmyword.

Pleaseguessaletter:\_a\_\_

\------------

Youhave5guessesleft.

Availableletters:bcdefghijklmnopqrtuvwxyz

Pleaseguessaletter:$ Oops!Thatisnotavalidletter.Youhave1warningsleft:\_a\_\_

\------------

Youhave5guessesleft. Availableletters:bcdefghijklmnopqrtuvwxyz Pleaseguessaletter:t

Goodguess:ta\_t

\------------

Youhave5guessesleft. Availableletters:bcdefghijklmnopqrtuvwxyz Pleaseguessaletter:e

Oops!Thatletterisnotinmyword:ta\_t

\------------

Youhave3guessesleft. Availableletters:bcdfghijklmnopqrtuvwxyz Pleaseguessaletter:e Oops!You'vealreadyguessedthatletter.Youhave0warningsleft: ta\_t

\------------

Youhave3guessesleft.

Availableletters:bcdfghijklmnopqrtuvwxyz

Pleaseguessaletter:e Oops!You'vealreadyguessedthatletter.Youhavenowarningsleft soyouloseoneguess:ta\_t

8
\------------

Youhave2guessesleft. Availableletters:bcdfghijklnopquvwxyz Pleaseguessaletter:c

Goodguess:tact

\------------

Congratulations,youwon! Yourtotalscoreforthisgameis:6

Andtheoutputofa**losing**gameshouldlooklikethis...

Loadingwordlistfromfile...

55900wordsloaded.

WelcometothegameHangman! Iamthinkingofawordthatis4letterslong Youhave3warningsleft.

\-----------

Youhave6guessesleft AvailableLetters:abcdefghijklmnopqrstuvwxyz Pleaseguessaletter:a Oops!Thatletterisnotinmyword:\_\_\_\_

\-----------

Youhave4guessesleft AvailableLetters:bcdefghijklmnopqrstuvwxyz Pleaseguessaletter:b Oops!Thatletterisnotinmyword:\_\_\_\_

\-----------

Youhave3guessesleft AvailableLetters:cdefghijklmnopqrstuvwxyz Pleaseguessaletter:c Oops!Thatletterisnotinmyword:\_\_\_\_

\-----------

Youhave2guessesleft

AvailableLetters:defghijklmnopqrstuvwxyz

Pleaseguessaletter:2 Oops!Thatisnotavalidletter.Youhave2warningsleft:\_\_\_\_ ­­­­­­­­­­­

Youhave2guessesleft AvailableLetters:defghijklmnopqrstuvwxyz Pleaseguessaletter:d Oops!Thatletterisnotinmyword:\_\_\_\_

\-----------

Youhave1guessesleft AvailableLetters:efghijklmnopqrstuvwxyz Pleaseguessaletter:e

Goodguess:e\_\_e

\-----------

Youhave1guessesleft AvailableLetters:fghijklmnopqrstuvwxyz Pleaseguessaletter:f

9

Oops!Thatletterisnotinmyword:e\_\_e ----------- Sorry,youranoutofguesses.Thewordwaselse.

Onceyouhavecompletedandtestedyourcode(whereyouhavemanuallyprovided the“secret”word,sinceknowingithelpsyoudebugyourcode),youmaywanttotry runningagainstthecomputer.Ifyouscrolldowntothebottomofthefilewe provided,youwillseetwocommentedlinesunderneaththetextif\_\_name\_\_==

“\_\_main\_\_”: #secret\_word=choose\_word(wordlist) #hangman(secret\_word)

Theselinesusefunctionswehaveprovided(nearthetopofhangman.py),whichyou maywanttoexamine.Try“uncommenting”theselines,andreloadingyourcode. Thiswillgiveyouachancetotryyourskillagainstthecomputer,whichusesour functionstoloadalargesetofwordsandthenpickoneatrandom.![ref1]

Problem4 HangmanPart3:TheGamewithHints

IfyouhavetriedplayingHangmanagainstthecomputer,youmayhavenoticedthat itisn’talwayseasytobeatthecomputer,especiallywhenitselectsanesotericword (like“esoteric”!).Itmightbeniceifyoucouldaskthecomputerforahint,suchasa listofallthewordsthatmatchwhatyouhavecurrentlyguessed.

Forexample,ifthehiddenwordis“tact”,andyouhavesofarguessedtheletter“t”, sothatyouknowthesolutionis“t\_\_t”,whereyouneedtoguessthetwomissing letters,itmightbenicetoknowthatthesetofmatchingwords(atleastbasedon whatthecomputerinitiallyloaded)are:

tacttarttautteattenttesttextthattilttinttoottorttouttrottufttwit

WearegoingtohaveyoucreateavariationofHangman(wecallthis hangman\_with\_hints,andhaveprovidedaninitialscaffoldforwritingit),withthe propertythatifyouguessthespecialcharacter\*thecomputerwillfindallthewords fromitsloadedlistthatmightmatchyourcurrentguessedword,andprintouteachof them.Ofcourse,wedon’trecommendtryingthisatthefirststep,sincethiswillprint outall55,900wordsthatweloaded!Butifyouaregettingclosetoananswerand arerunningoutofguesses,thismighthelp.

Todothis,wearegoingtoaskyoutofirstcompletetwohelperfunctions:

3A)Matchingthecurrentguessedword

match\_with\_gapstakestwoparameters:my\_wordandother\_word.my\_wordisan instanceofaguessedword,inotherwords,itmayhavesome\_’sinplaces(suchas ‘t\_\_t’).other\_wordisanormalEnglishword.

10

ThisfunctionshouldreturnTrueiftheguessedlettersofmy\_wordmatchthe correspondinglettersofother\_word.ItshouldreturnFalseifthetwowordsarenot ofthesamelengthorifaguessedletterinmy\_worddoesnotmatchthe correspondingcharacterinother\_word.

Rememberthatwhenaletterisguessed,yourcoderevealsallthepositionsatwhich thatletteroccursinthesecretword.Therefore,thehiddenletter(\_) cannotbe one ofthelettersinthewordthathasalreadybeenrevealed.

**ExampleUsage:**

\>>>match\_with\_gaps("te\_t","tact") False >>>match\_with\_gaps("a\_\_le","banana") False >>>match\_with\_gaps("a\_\_le","apple") True >>>match\_with\_gaps("a\_ple","apple") False

**Hint:**Youmaywanttousestrip()togetridofthespacesinthewordtocompare lengths.

3B)Showingallpossiblematches

show\_possible\_matchestakesasingleparameter:my\_wordwhichisaninstanceofa guessedword,inotherwords,itmayhavesome\_’sinplaces(suchas‘t\_\_t’).

Thisfunctionshouldprintoutallwordsinwordlist(noticewherewehavedefined thisatthebeginningofthefile,line51)thatmatchmy\_word.Itshouldprint“No matchesfound”iftherearenomatches.

**ExampleUsage:**

\>>>show\_possible\_matches("t\_\_t") tacttarttautteattenttesttextthattilttinttoottorttouttrottuft twit

\>>>show\_possible\_matches("abbbb\_") Nomatchesfound

\>>>show\_possible\_matches("a\_pl\_") ampleamply

3C)Hangmanwithhints

Nowyoushouldbeabletoreplicatethecodeyouwrotefor hangmanasthebodyof hangman\_with\_hints,thenmakeasmalladditiontoallowforthecasewheretheuser canguessanasterisk(\*),inwhichcasethecomputerwillprintoutallthewordsthat matchthatguess.

Theusershouldnotloseaguessiftheguessisanasterisk. CommentoutthelinesofcodeyouusedtoplaytheoriginalHangmangame:

secret\_word=choose\_word(wordlist)

hangman(secret\_word)

Andun­commentouttheselinesofcodewe’veprovidedatthebottomofthefileto playyournewgameHangmanwithHints:

#secret\_word=choose\_word(wordlist) #hangman\_with\_hints(secret\_word)

**SampleOutput:** Theoutputfromguessinganasteriskshouldlooklikethesampleoutputbelow.All otheroutputshouldfollowtheHangmangamedescribedinPart2above.

Loadingwordlistfromfile...

55900wordsloaded.

WelcometothegameHangman! Iamthinkingofawordthatis5letterslong.

\--------

Youhave6guessesleft. Availableletters:abcdefghijklmnopqrstuvwxyz Pleaseguessaletter:a

Goodguess:a\_\_\_\_

\--------

Youhave6guessesleft. Availableletters:bcdefghijklmnopqrstuvwxyz Pleaseguessaletter:l

Goodguess:a\_\_l\_

\--------

Youhave6guessesleft. Availableletters:bcdefghijkmnopqrstuvwxyz Pleaseguessaletter:\*

Possiblewordmatchesare: addleadultagileaisleambleampleamplyamylsangleankleapple applyaptlyarilsatilt

\--------

Youhave6guessesleft. Availableletters:bcdefghijkmnopqrstuvwxyz Pleaseguessaletter:e

Goodguess:a\_\_le

\--------

Thiscompletestheproblemset!![ref1]

12

MIT OpenCourseWare <https://ocw.mit.edu>

6\.0001 Introduction to Computer Science and Programming in Python

Fall 2016

For information about citing these materials or our Terms of Use, visit: <https://ocw.mit.edu/terms>.

[ref1]: Aspose.Words.fe4a9722-f5fa-454c-81c2-1efcf06d0bd7.004.png
