**Problem Set 1**

**Handedout:**Monday,September12,2016. **Due:11:59PM,Tuesday,September20,2016**

ThisproblemsetwillintroduceyoutousingcontrolflowinPythonandformulatingacomputational solutiontoaproblem.Itwillalsogiveyouachancetoexplorebisectionsearch.Thisproblemsethas **three**problems.Youshouldsaveyourcodeforthefirstproblemas**ps1a.py**,thesecondproblemas **ps1b.py**andthethirdproblemas**ps1c.py**,andmakesuretohandinallthreefiles.Don'tforgetto includecommentstohelpusunderstandyourcode!

**Collaboration**

You may work with other students; however, each student should write up and hand in his or her assignment separately. Be sure to indicate with whom you have worked in a comment at the start of eachfile.

**BeforeYouStart:ReadtheStyleGuide**

Readthestyleguidesections1,2,and3.

**PartA:HouseHunting**

YouhavegraduatedfromMITandnowhaveagreatjob!YoumovetotheSanFranciscoBayAreaand decidethatyouwanttostartsavingtobuyahouse.AshousingpricesareveryhighintheBayArea, yourealizeyouaregoingtohavetosaveforseveralyearsbeforeyoucanaffordtomakethedown paymentonahouse.InPartA,wearegoingtodeterminehowlongitwilltakeyoutosaveenough moneytomakethedownpaymentgiventhefollowingassumptions:

1. Callthecostofyourdreamhome**total\_cost**.
1. Calltheportionofthecostneededforadownpayment**portion\_down\_payment**.For simplicity,assumethatportion\_down\_payment=0.25(25%).
1. Calltheamountthatyouhavesavedthusfar**current\_savings**.Youstartwithacurrent savingsof$0.
1. Assumethatyouinvestyourcurrentsavingswisely,withanannualreturnof**r**(inotherwords, attheendofeachmonth,youreceiveanadditional**current\_savings\*r/12**fundstoputinto yoursavings–the12isbecause**r**isanannualrate).Assumethatyourinvestmentsearna returnofr=0.04(4%).
1. Assumeyourannualsalaryis**annual\_salary**.
1. Assumeyouaregoingtodedicateacertainamountofyoursalaryeachmonthtosavingfor thedownpayment.Callthat**portion\_saved**.Thisvariableshouldbeindecimalform(i.e.0.1 for10%).
1. Attheendofeachmonth,yoursavingswillbeincreasedbythereturnonyourinvestment, plusapercentageofyour **monthlysalary**(annualsalary/12).

Writeaprogramtocalculatehowmanymonthsitwilltakeyoutosaveupenoughmoneyforadown payment.Youwillwantyourmainvariablestobefloats,soyoushouldcastuserinputstofloats.

Yourprogramshouldasktheusertoenterthefollowingvariables:

1. Thestartingannualsalary(annual\_salary)
1. Theportionofsalarytobesaved(portion\_saved)
1. Thecostofyourdreamhome(total\_cost)

**Hints**

Tohelpyougetstarted,hereisaroughoutlineofthestagesyoushouldprobablyfollowinwritingyour code:

- Retrieveuserinput.Lookatinput()ifyouneedhelpwithgettinguserinput.Forthisproblemset, youcanassumethatuserswillentervalidinput(e.g.theywon’tenterastringwhenyouexpect anint)
- Initializesomestatevariables.Youshoulddecidewhatinformationyouneed.Becarefulabout valuesthatrepresentannualamountsandthosethatrepresentmonthlyamounts.

Trydifferentinputsandseehowlongittakestosaveforadownpayment.**Pleasemakeyour programprintresultsintheformatshowninthetestcasesbelow.**

**TestCase1**

\>>>

Enteryourannualsalary:120000 Enterthepercentofyoursalarytosave,asadecimal:.10 Enterthecostofyourdreamhome:1000000 Numberofmonths:183

\>>>

**TestCase2**

\>>>

Enteryourannualsalary:80000 Enterthepercentofyoursalarytosave,asadecimal:.15 Enterthecostofyourdreamhome:500000 Numberofmonths:105

\>>>

**PartB:Saving,witharaise** Background

InPartA,weunrealisticallyassumedthatyoursalarydidn’tchange.ButyouareanMITgraduate,and clearlyyouaregoingtobeworthmoretoyourcompanyovertime!Sowearegoingtobuildonyour solutiontoPartAbyfactoringinaraiseeverysixmonths.

In**ps1b.py**,copyyoursolutiontoPartA(aswearegoingtoreusemuchofthatmachinery).Modify yourprogramtoincludethefollowing

1. Havetheuserinputasemi-annualsalaryraise**semi\_annual\_raise**(asadecimalpercentage)
1. Afterthe6thmonth,increaseyoursalarybythatpercentage.Dothesameafterthe12th month,the18thmonth,andsoon.

Writeaprogramtocalculatehowmanymonthsitwilltakeyousaveupenoughmoneyforadown payment.LIkebefore,assumethatyourinvestmentsearnareturnof**r**=0.04(or4%)andthe requireddownpaymentpercentageis0.25(or25%).Havetheuserenterthefollowingvariables:

1. Thestartingannualsalary(annual\_salary)
2. Thepercentageofsalarytobesaved(portion\_saved)
2. Thecostofyourdreamhome(total\_cost)
2. Thesemi­annualsalaryraise(semi\_annual\_raise)

**Hints**

Tohelpyougetstarted,hereisaroughoutlineofthestagesyoushouldprobablyfollowinwritingyour code:

- Retrieveuserinput.
- Initializesomestatevariables.Youshoulddecidewhatinformationyouneed.Besuretobe carefulaboutvaluesthatrepresentannualamountsandthosethatrepresentmonthlyamounts.
- Becarefulaboutwhenyouincreaseyoursalary–thisshouldonlyhappen**after**the6th,12th,18th month,andsoon.

Trydifferentinputsandseehowquicklyorslowlyyoucansaveenoughforadownpayment.**Please makeyourprogramprintresultsintheformatshowninthetestcasesbelow.**

**TestCase1**

\>>>

Enteryourstartingannualsalary:120000 Enterthepercentofyoursalarytosave,asadecimal:.05 Enterthecostofyourdreamhome: 500000 Enterthesemi­annualraise,asadecimal:.03 Numberofmonths:142

\>>>

**TestCase2**

\>>>

Enteryourstartingannualsalary:80000 Enterthepercentofyoursalarytosave,asadecimal:.1 Enterthecostofyourdreamhome: 800000 Enterthesemi­annualraise,asadecimal:.03 Numberofmonths:159

\>>>

**TestCase3**

\>>>

Enteryourstartingannualsalary:75000 Enterthepercentofyoursalarytosave,asadecimal:.05 Enterthecostofyourdreamhome:1500000 Enterthesemi­annualraise,asadecimal:.05 Numberofmonths:261

\>>>

**PartC:Findingtherightamounttosaveaway**

InPartB,youhadachancetoexplorehowboththepercentageofyoursalarythatyousaveeachmonth andyourannualraiseaffecthowlongittakesyoutosaveforadownpayment.Thisisnice,but supposeyouwanttosetaparticulargoal,e.g.tobeabletoaffordthedownpaymentinthreeyears. Howmuchshouldyousaveeachmonthtoachievethis?Inthisproblem,youaregoingtowritea programtoanswerthatquestion.Tosimplifythings,assume:

1. Yoursemi­annualraiseis.07(7%)
1. Yourinvestmentshaveanannualreturnof0.04(4%)
1. Thedownpaymentis0.25(25%)ofthecostofthehouse
1. Thecostofthehousethatyouaresavingforis$1M.

Youarenowgoingtotrytofindthebestrateofsavingstoachieveadownpaymentona$1Mhousein 36months.Sincehittingthisexactlyisachallenge,wesimplywantyoursavingstobewithin$100of therequireddownpayment.

In**ps1c.py**,writeaprogramtocalculatethebestsavingsrate,asafunctionofyourstartingsalary. Youshoulduse**bisectionsearch**tohelpyoudothisefficiently.Youshouldkeeptrackofthenumberof stepsittakesyourbisectionssearchtofinish.Youshouldbeabletoreusesomeofthecodeyouwrote forpartBinthisproblem.

Becausewearesearchingforavaluethatisinprincipleafloat,wearegoingtolimitourselvestotwo decimalsofaccuracy(i.e.,wemaywanttosaveat7.04%­­or0.0704indecimal–butwearenot goingtoworryaboutthedifferencebetween7.041%and7.039%).Thismeanswecansearchforan **integer**between0and10000(usingintegerdivision),andthenconvertittoadecimalpercentage (usingfloatdivision)tousewhenwearecalculatingthe**current\_savings**after36months.Byusing thisrange,thereareonlyafinitenumberofnumbersthatwearesearchingover,asopposedtothe infinitenumberofdecimalsbetween0and1.Thisrangewillhelppreventinfiniteloops.Thereasonwe use0to10000istoaccountfortwoadditionaldecimalplacesintherange0%to100%.Yourcode shouldprintoutadecimal(e.g.0.0704for7.04%).

Trydifferentinputsforyourstartingsalary,andseehowthepercentageyouneedtosavechangesto reachyourdesireddownpayment.Alsokeepinminditmaynotbepossiblefortosaveadown paymentinayearandahalfforsomesalaries.Inthiscaseyourfunctionshouldnotifytheuserthatit isnotpossibletosaveforthedownpaymentin36monthswithaprintstatement.**Pleasemakeyour programprintresultsintheformatshowninthetestcasesbelow.**

***Note:Therearemultiplerightwaystoimplementbisectionsearch/numberofstepssoyour resultsmaynotperfectlymatchthoseofthetestcase.***

**Hints**

- Theremaybemultiplesavingsratesthatyieldasavingsamountthatiswithin$100ofthe requireddownpaymentona$1Mhouse.Inthiscase,youcanjustreturnanyofthepossible values.
- Dependingonyourstoppingconditionandhowyoucomputeatrialvalueforbisectionsearch, yournumberofstepsmayvaryslightlyfromtheexampletestcases.
- Watchoutforintegerdivisionwhencalculatingifapercentagesavedisappropriateandwhen calculatingfinaldecimalpercentagesavingsrate.
- Remembertoresettheappropriatevariable(s)totheirinitialvaluesforeachiterationofbisection search.

**TestCase1**

\>>> Enterthestartingsalary:150000 Bestsavingsrate:0.4411 Stepsinbisectionsearch:12 >>>

**TestCase2**

\>>> Enterthestartingsalary:300000 Bestsavingsrate:0.2206 Stepsinbisectionsearch:9 >>>

**TestCase3**

\>>>

Enterthestartingsalary:10000 Itisnotpossibletopaythedownpaymentinthreeyears. >>>

5

MIT OpenCourseWare <https://ocw.mit.edu>

6\.0001 Introduction to Computer Science and Programming in Python

Fall 2016

For information about citing these materials or our Terms of Use, visit: <https://ocw.mit.edu/terms>.

