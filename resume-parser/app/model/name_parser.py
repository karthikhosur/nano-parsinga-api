import re
import spacy
from Levenshtein import ratio, distance, hamming

nlp = spacy.load("en_core_web_sm")

states = " AL | AZ | AR | CA | CO | CT | DE | FL | GA | ID | IL | IA | KS | KY | LA | ME | MD | MA | MI | MN | MS | MO | MT | NE | NV | NH | NJ | NM | NY | NC | ND | OH | OK | OR | PA | RI | SC | SD | TN | TX | UT | VT | VA | WA | WV | WI | WY "
name_designation = " PMP | PHD | MBA | DR. | MSC | CSPO | CSM | CPA "


job_titles = " marketing specialist | CEO | freelance | coach | VP | assistant vice president | software architect | marketing manager | marketing director | graphic designer | hr |marketing research analyst | marketing communications manager | marketing consultant | product manager | public relations | social media assistant | brand manager | seo manager | content marketing manager | copywriter | media buyer | digital marketing manager | ecommerce marketing specialist | brand strategist | vice president of marketing | media relations coordinator | administrative assistant | receptionist | office manager | auditing clerk | bookkeeper | account executive | branch manager | business manager | quality control coordinator | administrative manager | chief executive officer | business analyst | risk manager | human resources | office assistant | secretary | office clerk | file clerk | account collector | administrative specialist | executive assistant | program administrator | program manager | administrative analyst | data entry | team leader | manager | assistant manager | executive | director | coordinator | administrator | controller | officer | organizer | supervisor | superintendent | head | overseer | chief | foreman | controller | principal | president | software developer | designer | developer | software engineer | engineer | computer scientist | it professional | ux designer & ui developer | sql developer | web designer | web developer | help desk worker/desktop support | software engineer | data entry | devops engineer | computer programmer | network administrator | information security analyst | artificial intelligence engineer | cloud architect | it manager | technical specialist | application developer | sales associate | sales representative | sales manager | retail worker | store manager | sales representative | sales manager | real estate broker | sales associate | cashier | store manager | account executive | account manager | area sales manager | direct salesperson | director of inside sales | outside sales manager | sales analyst | market development manager | b2b sales specialist | sales engineer | marchandising associate | construction worker | taper | plumber | heavy equipment operator | vehicle or equipment cleaner | carpenter | electrician | painter | welder | handyman | boilermaker | crane operator | building inspector | pipefitter | sheet metal worker | iron worker | mason | roofer | solar photovoltaic installer | well driller | principal | owner | president | founder | administrator | director | partner | proprietor | human resource | accountant | supervisor | quality control | receptionist | virtual assistant | customer service | customer support | concierge | help desk | customer service manager | technical support specialist | account representative | client service specialist | customer care associate | operations manager | operations assistant | operations coordinator | operations analyst | operations director | operations professional | scrum master | continuous improvement lead | continuous improvement consultant |    •  credit authorizer | benefits manager | credit counselor | accountant | bookkeeper | accounting analyst | accounting director | accounts payable/receivable clerk | auditor | budget analyst | controller | financial analyst | finance manager | economist | payroll manager | payroll clerk | financial planner | financial services representative | finance director | commercial loan officer | engineer | mechanical engineer | civil engineer | electrical engineer | assistant engineer | chemical engineer | chief engineer | drafter | engineering technician | geological engineer | biological engineer | maintenance engineer | mining engineer | nuclear engineer | petroleum engineer | plant engineer | production engineer | quality engineer | safety engineer | sales engineer | researcher | research assistant | data analyst | business analyst | financial analyst | biostatistician | researcher | market researcher | medical researcher | mentor | tutor/online tutor | teacher | teaching assistant | substitute teacher | preschool teacher | test scorer | online esl instructor | professor | assistant professor | graphic designer | artist | interior designer | video editor | video or film producer | playwright | musician | novelist/writer | computer animator | photographer | camera operator | sound engineer | motion picture director | actor | music producer | director of photography | nurse | travel nurse | nurse practitioner | doctor | caregiver | cna | physical therapist | pharmacist | pharmacy assistant | medical administrator | medical laboratory tech | physical therapy assistant | massage therapy | dental hygienist | orderly | personal trainer | massage therapy | medical laboratory tech | phlebotomist | medical transcriptionist | telework nurse/doctor | reiki practitioner | housekeeper | flight attendant | travel agent | hotel front door greeter | bellhop | cruise director | entertainment specialist | hotel manager | front desk associate | front desk manager | concierge | group sales | event planner | porter | spa manager | wedding coordinator | cruise ship attendant | casino host | hotel receptionist | reservationist | events manager | meeting planner | lodging manager | director of maintenance | valet | waiter/waitress | server | chef | fast food worker | barista | line cook | cafeteria worker | restaurant manager | wait staff manager | bus person | restaurant chain executive | political scientist | chemist | conservation scientist | sociologist | biologist | geologist | physicist | astronomer | atmospheric scientist | molecular scientist | scientist | call center representative | customer service | telemarketer | telephone operator | phone survey conductor | dispatcher for trucks or taxis | customer support representative | over the phone interpreter | phone sales specialist | mortgage loan processor | counselor | mental health counselor | addiction counselor | school counselor | speech pathologist | guidance counselor | social worker | therapist | life coach | couples counselor | beautician | hair stylist | nail technician | cosmetologist | salon manager | makeup artist | esthetician | skin care specialist | manicurist | barber | journalist | copy editor | editor/proofreader | content creator | speechwriter | communications director | screenwriter | technical writer | columnist | public relations specialist | proposal writer | content strategist | grant writer | video game writer | translator | film critic | copywriter | travel writer | social media specialist | ghostwriter | warehouse worker | painter | truck driver | heavy equipment operator | welding | physical therapy assistant | housekeeper | landscaping worker | landscaping assistant | mover | animal breeder | veterinary assistant | farm worker | animal shelter worker | dog walker / pet sitter | zoologist | animal trainer | service dog trainer | animal shelter manager | animal control officer | delivery driver | school bus driver | truck driver | tow truck operator | ups driver | mail carrier | driver | recyclables collector | courier | bus driver | cab driver | animal shelter board member | office volunteer | animal shelter volunteer | hospital volunteer | youth volunteer | food kitchen worker | homeless shelter worker | conservation volunteer | meals on wheels driver | habitat for humanity builder | emergency relief worker | red cross volunteer | community food project worker | women’s shelter jobs | suicide hotline volunteer | school volunteer | community volunteer jobs | sports volunteer | church volunteer | volunteer | recruiter | paralegal | attorney | translator | architect | locksmith | operator | teller | tehnician | specialist | manager | director | designer | analyst | consultant | assistant | copywriter | buyer | strategist | coordinator | president | vice president | analyst | receptionist | clerk | bookkeeper | executive | coordinator | manager | officer | secretary | clerk | collector | administrator | data entry | chief | team leader | representative | attendant"

name_not = "profession|overview|concept|hindi|french|laude|pyscholog|event|skill|plan|social|media|profit|publication|list|arabic|county|technologies|problem|russian|influence|saving|healthcare|expertise|learning|github|presentation|strateg|role|minor|linkedin|spanish|basics|may|studio|english|adobe|creative|microsoft|instructor|office|website|award|performance||client|design|mission|manage|consult|review|date|domain|respons|excel|mobile|resource|budget|fundrais|produ|certi|profil|devops|unix|program|script|area|special|software|service|business|synopsis|system|sept|~|&|tool|course|contact|detail|degree|phone|honor|descript|title|sales|designer|care|goal|cell|name|organization|intro|qualif|father|developer|educat|exam|year|institu|academ|internship|internship|work|chinese|german|work|employ|www|http|employ|career|career|employment|employer|language|employer|project|summary|technical|skill|engineer|place|ltd|company|skills|experience|declaration|personal|data|activities|projects|story|objective|professional|azure|data|summary|history|personal|@|email|background|internship|technical|freelance|community|activities|work|exposure|strength|achievements|career|pvt|private|ltd|limited|llc|corp|industr|solutions|school|college|university|bachelor|master|training"

US_human_names = " SAI | ARJUN | ROY | SUMAN | SMITH | HASAN | NAIK | REDDY | GOWDA | JAIN | SINGH | MODI | MANJU | RAMESH | RAMA | AASHIK | NAIDU | NEIL | THAKUR | TRIPATHI | THAKAR | THACKERAY | TIFFANY | TAPAR | SINHA | SAWANT | EMILY | CHARLOTTE | JANE | ERIC | FLAVIA | JOHNSON | EVELYN | WILLIAMS | JESSICA | BROWN | JONES | MILLER | DAVIS | GARCIA | RODRIGUEZ | WILSON | MARTINEZ | ANDERSON | TAYLOR | THOMAS | DYLAN | HERNANDEZ | MOORE | MARTIN | JACKSON | THOMPSON | WHITE | LOPEZ | LEE | GONZALEZ | HARRIS | CLARK | LEWIS | ROBINSON | WALKER | PEREZ | HALL | YOUNG | ALLEN | SANCHEZ | WRIGHT | KING | SCOTT | GREEN | BAKER | ADAMS | NELSON | HILL | RAMIREZ | CAMPBELL | MITCHELL | ROBERTS | CARTER | PHILLIPS | EVANS | TURNER | TORRES | PARKER | COLLINS | EDWARDS | STEWART | FLORES | MORRIS | NGUYEN | MURPHY | RIVERA | COOK | ROGERS | MORGAN | PETERSON | COOPER | REED | BAILEY | BELL | GOMEZ | KELLY | HOWARD | WARD | COX | DIAZ | RICHARDSON | WOOD | WATSON | BROOKS | BENNETT | GRAY | JAMES | REYES | CRUZ | HUGHES | PRICE | MYERS | LONG | SANDRA | FOSTER | SANDERS | ROSS | MORALES | POWELL | SULLIVAN | RUSSELL | ORTIZ | GUTIERREZ | PERRY | BUTLER | BARNES | FISHER | HENDERSON | DAN | COLEMAN | SIMMONS | PATTERSON | JORDAN | REYNOLDS | HAMILTON | GRAHAM | KIM | GONZALES | ALEXANDER | RAMOS | WALLACE | GRIFFIN | WEST | COLE | HAYES | CHAVEZ | GIBSON | BRYANT | ELLIS | STEVENS | MURRAY | FORD | MARSHALL | OWENS | MCDONALD | HARRISON | RUIZ | KENNEDY | WELLS | ALVAREZ | MENDOZA | CASTILLO | OLSON | WEBB | WASHINGTON | TUCKER | BURNS | HENRY | VASQUEZ | SNYDER | SIMPSON | CRAWFORD | JIMENEZ | PORTER | MASON | SHAW | GORDON | WAGNER | HUNTER | ROMERO | HICKS | DIXON | HUNT | PALMER | ROBERTSON | BLACK | HOLMES | STONE | MEYER | BOYD | MILLS | WARREN | FOX | ROSE | RICE | MORENO | SCHMIDT | PATEL | FERGUSON | NICHOLS | HERRERA | MEDINA | RYAN | FERNANDEZ | WEAVER | DANIELS | STEPHEN | GARDNER | PAYNE | KELLEY | DUNN | PIERCE | ARNOLD | TRAN | SPENCER | PETERS | HAWKINS | GRANT | HANSEN | SEN | CASTRO | HOFFMAN | HART | ELLIOTT | CUNNINGHAM | KNIGHT | BRADLEY | CARROLL | HUDSON | DUNCAN | ARMSTRONG | BERRY | ANDREWS | JOHNSTON | RAY | RILEY | CARPENTER | PERKINS | AGUILAR | SILVA | RICHARDS | WILLIS | MATT | MATTHEWS | CHAPMAN | LAWRENCE | GARZA | VARGAS | WATKINS | WHEELER | LARSON | CARLSON | HARPER | GEORGE | GREENE | BURKE | GUZMAN | MORRISON | MUNOZ | JACOBS | OBRIEN | LAWSON | FRANKLIN | RENEE | LYNCH | BISHOP | CARR | SALAZAR | AUSTIN | MENDEZ | GILBERT | JENSEN | WILLIAMSON | MONTGOMERY | HARVEY | OLIVER | HOWELL | DEAN | HANSON | WEBER | GARRETT | SIMS | BURTON | FULLER | SOTO | MCCOY | WELCH | CHEN | SCHULTZ | WALTERS | REID | FIELDS | WALSH | LITTLE | FOWLER | BOWMAN | DAVIDSON | MAY | DAY | SCHNEIDER | NEWMAN | BREWER | LUCAS | HOLLAND | WONG | BANKS | SANTOS | CURTIS | PEARSON | DELGADO | VALDEZ | PENA | RIOS | DOUGLAS | SANDOVAL | BARRETT | HOPKINS | KELLER | GUERRERO | STANLEY | BATES | ALVARADO | BECK | ORTEGA | WADE | ESTRADA | CONTRERAS | BARNETT | CALDWELL | SANTIAGO | LAMBERT | POWERS | CHAMBERS | MIKE | NUNEZ | CRAIG | LEONARD | PABBA | LOWE | RHODES | BYRD | GREGORY | SHELTON | FRAZIER | BECKER | SHARON | MALDONADO | FLEMING | VEGA | SUTTON | COHEN | JENNINGS | PARKS | MCDANIEL | WATTS | BARKER | NORRIS | VAUGHN | VAZQUEZ | HOLT | SCHWARTZ | STEELE | BENSON | NEAL | DOMINGUEZ | HORTON | TERRY | WOLFE | HALE | LYONS | GRAVES | HAYNES | MILES | PARK | WARNER | PADILLA | BUSH | THORNTON | MCCARTHY | MANN | ZIMMERMAN | ERICKSON | FLETCHER | MCKINNEY | LAUREN | DAWSON | JOSEPH | MARQUEZ | REEVES | KLEIN | ESPINOZA | BALDWIN | MORAN | LOVE | ROBBINS | HIGGINS | BALL | CORTEZ | LE | GRIFFITH | BOWEN | SHARP | CUMMINGS | RAMSEY | HARDY | SWANSON | BARBER | ACOSTA | LUNA | CHANDLER | BLAIR | DANIEL | SIMON | DENNIS | OCONNOR | QUINN | GROSS | NAVARRO | MOSS | FITZGERALD | DOYLE | MCLAUGHLIN | ROJAS | RODGERS | JUAN | STEVE | STEVENSON | SINGH | YANG | FIGUEROA | HARMON | NEWTON | PAUL | MANNING | GARNER | MCGEE | REESE | FRANCIS | BURGESS | ADKINS | GOODMAN | CURRY | BRADY | CHRISTENSEN | POTTER | WALTON | GOODWIN | MULLINS | MOLINA | WEBSTER | FISCHER | CAMPOS | AVILA | SHERMAN | TODD | CHANG | BLAKE | MALONE | WOLF | HODGES | JUAREZ | GILL | FARMER | HINES | GALLAGHER | DURAN | HUBBARD | CANNON | MIRANDA | WANG | SAUNDERS | TATE | MACK | HAMMOND | CARRILLO | TOWNSEND | WISE | INGRAM | BARTON | MEJIA | AYALA | SCHROEDER | HAMPTON | ROWE | PARSONS | FRANK | WATERS | STRICKLAND | OSBORNE | MAXWELL | CHAN | DELEON | NORMAN | HARRINGTON | CASEY | PATTON | LOGAN | BOWERS | MUELLER | GLOVER | FLOYD | HARTMAN | BUCHANAN | COBB | FRENCH | KRAMER | MCCORMICK | KIRAN | KUMAR | CLARKE | TYLER | GIBBS | MOODY | CONNER | SPARKS | MCGUIRE | LEON | BAUER | NORTON | POPE | FLYNN | HOGAN | ROBLES | SALINAS | YATES | LINDSEY | LLOYD | MARSH | MCBRIDE | OWEN | SOLIS | PHAM | LANG | PRATT | LARA | BROCK | BALLARD | TRUJILLO | SHAFFER | DRAKE | ROMAN | AGUIRRE | MORTON | STOKES | LAMB | PACHECO | PATRICK | COCHRAN | SHEPHERD | CAIN | BURNETT | HESS | CERVANTES | OLSEN | BRIGGS | OCHOA | CABRERA | VELASQUEZ | MONTOYA | ROTH | MEYERS | CARDENAS | FUENTES | WEISS | HOOVER | WILKINS | NICHOLSON | UNDERWOOD | SHORT | CARSON | MORROW | COLON | HOLLOWAY | SUMMERS | BRYAN | PETERSEN | MCKENZIE | SERRANO | WILCOX | CAREY | CLAYTON | POOLE | CALDERON | GALLEGOS | GREER | RIVAS | GUERRA | DECKER | COLLIER | WALL | WHITAKER | BASS | FLOWERS | DAVENPORT | CONLEY | HOUSTON | HUFF | COPELAND | HOOD | MONROE | MASSEY | ROBERSON | COMBS | FRANCO | LARSEN | PITTMAN | RANDALL | SKINNER | WILKINSON | KIRBY | CAMERON | BRIDGES | ANTHONY | RICHARD | KIRK | BRUCE | SINGLETON | MATHIS | BRADFORD | BOONE | ABBOTT | CHARLES | ALLISON | SWEENEY | ATKINSON | HORN | JEFFERSON | ROSALES | YORK | CHRISTIAN | PHELPS | FARRELL | CASTANEDA | NASH | DICKERSON | BOND | WYATT | FOLEY | CHASE | GATES | VINCENT | MATHEWS | HODGE | GARRISON | TREVINO | VILLARREAL | HEATH | DALTON | VALENCIA | CALLAHAN | HENSLEY | ATKINS | HUFFMAN | ROY | BOYER | SHIELDS | LIN | HANCOCK | GRIMES | GLENN | CLINE | DELACRUZ | CAMACHO | DILLON | PARRISH | ONEILL | MELTON | BOOTH | KANE | BERG | HARRELL | PITTS | SAVAGE | WIGGINS | BRENNAN | SALAS | MARKS | RUSSO | SAWYER | BAXTER | HUTCHINSON | LIU | WALTER | MCDOWELL | MUSTAFA | WILEY | RICH | HUMPHREY | JOHNS | KOCH | SUAREZ | HOBBS | BEARD | GILMORE | IBARRA | KEITH | MACIAS | KHAN | ANDRADE | WARE | STEPHENSON | HENSON | WILKERSON | DYER | MCCLURE | BLACKWELL | MERCADO | TANNER | EATON | AFZAL | CLAY | BARRON | BEASLEY | ONEAL | PRESTON | ZAMORA | MACDONALD | VANCE | SNOW | MCCLAIN | STAFFORD | OROZCO | CHANDRASHEKAR | TINU | ANAND | BARRY | MISHRA | ENGLISH | SHANNON | KLINE | JACOBSON | WOODARD | HUANG | KEMP | MOSLEY | PRINCE | MERRITT | HURST | VILLANUEVA | ROACH | NOLAN | LAM | YODER | MCCULLOUGH | LESTER | SANTANA | VALENZUELA | WINTERS | BARRERA | LEACH | ORR | BERGER | MCKEE | STRONG | CONWAY | STEIN | WHITEHEAD | BULLOCK | ESCOBAR | KNOX | MEADOWS | SOLOMON | VELEZ | ODONNELL | KERR | STOUT | BLANKENSHIP | BROWNING | KENT | LOZANO | BARTLETT | PRUITT | BUCK | BARR | GAINES | DURHAM | GENTRY | MCINTYRE | SLOAN | MELENDEZ | ROCHA | HERMAN | SEXTON | MOON | HENDRICKS | RANGEL | STARK | LOWERY | HARDIN | HULL | SELLERS | ELLISON | CALHOUN | GILLESPIE | MORA | KNAPP | MCCALL | MORSE | DORSEY | WEEKS | NIELSEN | LIVINGSTON | LEBLANC | MCLEAN | BRADSHAW | GLASS | MIDDLETON | BUCKLEY | SCHAEFER | FROST | HOWE | HOUSE | MCINTOSH | HO | PENNINGTON | REILLY | HEBERT | MCFARLAND | HICKMAN | NOBLE | SPEARS | CONRAD | ARIAS | GALVAN | VELAZQUEZ | HUYNH | FREDERICK | RANDOLPH | CANTU | FITZPATRICK | MAHONEY | PECK | MICHAEL | DONOVAN | MCCONNELL | WALLS | BOYLE | MAYER | ZUNIGA | GILES | PINEDA | PACE | HURLEY | MAYS | MCMILLAN | CROSBY | AYERS | CASE | BENTLEY | SHEPARD | EVERETT | PUGH | DAVID | MCMAHON | DUNLAP | BENDER | HAHN | HARDING | ACEVEDO | RAYMOND | BLACKBURN | DUFFY | LANDRY | DOUGHERTY | BAUTISTA | SHAH | POTTS | ARROYO | VALENTINE | MEZA | GOULD | VAUGHAN | FRY | RUSH | AVERY | HERRING | DODSON | CLEMENTS | SAMPSON | TAPIA | BEAN | LYNN | CRANE | FARLEY | CISNEROS | BENTON | ASHLEY | MCKAY | FINLEY | BEST | BLEVINS | FRIEDMAN | MOSES | SOSA | BLANCHARD | HUBER | FRYE | KRUEGER | BERNARD | ROSARIO | RUBIO | MULLEN | BENJAMIN | HALEY | CHUNG | MOYER | CHOI | HORNE | YU | WOODWARD | ALI | NIXON | HAYDEN | RIVERS | ESTES | MCCARTY | RICHMOND | STUART | MAYNARD | JOAN | ROTHSCHILD | BRANDT | OCONNELL | HANNA | SANFORD | SHEPPARD | CHURCH | BURCH | LEVY | RASMUSSEN | COFFEY | PONCE | FAULKNER | DONALDSON | SCHMITT | NOVAK | COSTA | MONTES | BOOKER | CORDOVA | WALLER | ARELLANO | MADDOX | MATA | BONILLA | STANTON | COMPTON | KAUFMAN | DUDLEY | MCPHERSON | BELTRAN | DICKSON | MCCANN | VILLEGAS | PROCTOR | HESTER | CANTRELL | DAUGHERTY | CHERRY | BRAY | DAVILA | ROWLAND | LEVINE | MADDEN | SPENCE | GOOD | IRWIN | WERNER | KRAUSE | PETTY | WHITNEY | BAIRD | TERESA | HOOPER | POLLARD | ZAVALA | JARVIS | HOLDEN | HAAS | HENDRIX | MCGRATH | BIRD | LUCERO | TERRELL | RIGGS | JOYCE | MERCER | ROLLINS | GALLOWAY | DUKE | ODOM | ANDERSEN | DOWNS | HATFIELD | BENITEZ | ARCHER | HUERTA | TRAVIS | MCNEIL | HINTON | ZHANG | HAYS | MAYO | FRITZ | BRANCH | MOONEY | RITTER | ESPARZA | FREY | BRAUN | GAY | RIDDLE | HANEY | KAISER | HOLDER | CHANEY | MCKNIGHT | GAMBLE | VANG | COOLEY | CARNEY | COWAN | FORBES | FERRELL | DAVIES | BARAJAS | SHEA | OSBORN | BRIGHT | CUEVAS | BOLTON | MURILLO | LUTZ | DUARTE | KIDD | KEY | COOKE | GOFF | DEJESUS | MARIN | DOTSON | BONNER | COTTON | MERRILL | LINDSAY | LANCASTER | MCGOWAN | FELIX | SALGADO | SLATER | CARVER | GUTHRIE | HOLMAN | FULTON | SNIDER | SEARS | WITT | NEWELL | BYERS | LEHMAN | GORMAN | COSTELLO | DONAHUE | DELANEY | ALBERT | WORKMAN | ROSAS | SPRINGER | JUSTICE | KINNEY | ODELL | LAKE | DONNELLY | LAW | DAILEY | GUEVARA | SHOEMAKER | BARLOW | MARINO | WINTER | CRAFT | KATZ | PICKETT | ESPINOSA | DALY | MALONEY | GOLDSTEIN | NAYAK | CROWLEY | VOGEL | KUHN | PEARCE | HARTLEY | CLEVELAND | PALACIOS | MCFADDEN | BRITT | WOOTEN | CORTES | DILLARD | CHILDERS | ALFORD | DODD | EMERSON | WILDER | LANGE | GOLDBERG | QUINTERO | BEACH | ENRIQUEZ | QUINTANA | HELMS | MACKEY | FINCH | CRAMER | MINOR | FLANAGAN | FRANKS | CORONA | KENDALL | MCCABE | HENDRICKSON | MOSER | MCDERMOTT | CAMP | MCLEOD | BERNAL | KAPLAN | MEDRANO | LUGO | TRACY | BACON | CROWE | RICHTER | WELSH | HOLLEY | RATLIFF | MAYFIELD | TALLEY | HAINES | DALE | GIBBONS | HICKEY | BYRNE | KIRKLAND | FARRIS | CORREA | TILLMAN | KESSLER | ENGLAND | HEWITT | BLANCO | CONNOLLY | PATE | BRUNO | HOLCOMB | HYDE | MCALLISTER | CHRISTOPHER | WHITFIELD | MEEKS | HATCHER | FINK | SUTHERLAND | NOEL | RITCHIE | ROSA | LEAL | JOYNER | STARR | MORIN | DELAROSA | CONNOR | HILTON | ALSTON | GILLIAM | WYNN | WILLS | JARAMILLO | ONEIL | NIEVES | BRITTON | RANKIN | BELCHER | GUY | CHAMBERLAIN | TYSON | PUCKETT | DOWNING | SHARPE | BOGGS | TRUONG | PIERSON | GODFREY | MOBLEY | JOHN | KERN | HOLLIS | BRAVO | MAGANA | RUTHERFORD | TUTTLE | ROMANO | ARTHUR | TREJO | KNOWLES | LYON | SHIRLEY | QUINONES | DOLAN | REYNA | SAENZ | HASTINGS | KENNEY | CANO | FOREMAN | DENTON | VILLALOBOS | PRYOR | SARGENT | DOHERTY | HOPPER | PHAN | WOMACK | LOCKHART | VENTURA | DWYER | MULLER | GALINDO | GRACE | SORENSEN | COURTNEY | PARRA | RODRIGUES | NICHOLAS | AHMED | MCGINNIS | LANGLEY | MADISON | LOCKE | JAMISON | NAVA | GUSTAFSON | SYKES | DEMPSEY | HAMM | RODRIQUEZ | MCGILL | XIONG | ESQUIVEL | SIMMS | KENDRICK | BOYCE | VIGIL | DOWNEY | MCKENNA | SIERRA | WEBBER | KIRKPATRICK | DICKINSON | COUCH | BURKS | SHEEHAN | SLAUGHTER | PIKE | WHITLEY | MAGEE | CHENG | SINCLAIR | CASSIDY | RUTLEDGE | BURRIS | BOWLING | CRABTREE | MCNAMARA | AVALOS | VU | HERRON | BROUSSARD | ABRAHAM | GARLAND | CORBETT | CORBIN | STINSON | CHIN | BURT | HUTCHINS | WOODRUFF | LAU | BRANDON | SINGER | HATCH | ROSSI | SHAFER | GOSS | GREGG | DEWITT | TANG | POLK | WORLEY | COVINGTON | SALDANA | HELLER | EMERY | SWARTZ | CHO | MCCRAY | ELMORE | ROSENBERG | SIMONS | CLEMONS | BEATTY | HARDEN | HERBERT | BLAND | RUCKER | MANLEY | ZIEGLER | GRADY | LOTT | ROUSE | GLEASON | MCCLELLAN | ABRAMS | ALBRIGHT | MEIER | DUNBAR | ACKERMAN | PADGETT | MAYES | TIPTON | COFFMAN | PERALTA | SHAPIRO | ROE | WESTON | PLUMMER | HELTON | STERN | FRASER | STOVER | FISH | SCHUMACHER | BACA | CURRAN | VINSON | VERA | CLIFTON | ERVIN | ELDRIDGE | LOWRY | CHILDRESS | BECERRA | GORE | SEYMOUR | CHU | FIELD | AKERS | CARRASCO | BINGHAM | STERLING | GREENWOOD | LESLIE | GROVES | MANUEL | SWAIN | EDMONDS | MUNIZ | THOMSON | CROUCH | WALDEN | SMART | TOMLINSON | ALFARO | GOLDMAN | DMITIRI | MCELROY | YARBROUGH | FUNK | PORTILLO | LUND | ELKINS | STROUD | MEREDITH | MCCAULEY | ZAPATA | GEE | GIVENS | CARDONA | SCHAFER | ROBISON | GUNTER | GRIGGS | TOVAR | TEAGUE | SWIFT | BOWDEN | SCHULZ | BLANTON | BUCKNER | WHALEN | PRITCHARD | PIERRE | KANG | BUTTS | METCALF | KURTZ | SANDERSON | TOMPKINS | INMAN | CROWDER | DICKEY | HUTCHISON | CONKLIN | HOSKINS | HOLBROOK | HORNER | NEELY | TATUM | HOLLINGSWORTH | DRAPER | CLEMENT | LORD | REECE | FELDMAN | KAY | HAGEN | CREWS | BOWLES | JEWELL | DALEY | CORDERO | MCKINLEY | VELASCO | MASTERS | DRISCOLL | BURRELL | VALLE | CROW | DEVINE | LARKIN | CHAPPELL | POLLOCK | KIMBALL | LY | SCHMITZ | LU | RUBIN | NANCY | BARRIOS | PEREIRA | PHIPPS | MCMANUS | NANCE | STEINER | POE | CROCKETT | JEFFRIES | AMOS | NIX | NEWSOME | DOOLEY | PAYTON | BILL | HOLTZ | ROSEN | SWENSON | CONNELLY | TOLBERT | SEGURA | ESPOSITO | COKER | BIGGS | HINKLE | THURMAN | IVEY | BULLARD | BAEZ | NEFF | MAHER | STRATTON | EGAN | DUBOIS | GALLARDO | BLUE | RAINEY | YEAGER | SAUCEDO | FERREIRA | SPRAGUE | LACY | HURTADO | HEARD | CONNELL | STAHL | ALDRIDGE | AMAYA | FORREST | ERWIN | GUNN | SWAN | BUTCHER | ROSADO | GODWIN | GABRIEL | OTTO | WHALEY | LUDWIG | CLIFFORD | GROVE | BEAVER | DANG | DICK | BOSWELL | MEAD | COLVIN | OLEARY | MILLIGAN | GOINS | AMES | DODGE | KAUR | ESCOBEDO | ARREDONDO | GEIGER | WINKLER | DUNHAM | TEMPLE | BABCOCK | BILLINGS | GRIMM | LILLY | WESLEY | MCGHEE | PAINTER | SIEGEL | BOWER | PURCELL | BLOCK | AGUILERA | NORWOOD | SHERIDAN | CARTWRIGHT | COATES | DAVISON | REGAN | RAMEY | KOENIG | KRAFT | BUNCH | ENGEL | TAN | WINN | STEWARD | LINK | VICKERS | BRAGG | PIPER | HUGGINS | MICHEL | HEALY | JACOB | MCDONOUGH | WOLFF | COLBERT | ZEPEDA | HOANG | DUGAN | KILGORE | MEADE | GUILLEN | HINOJOSA | GOODE | ARRINGTON | GARY | SNELL | WILLARD | RENTERIA | CHACON | GALLO | HANKINS | MONTANO | BROWNE | PEACOCK | OHARA | CORNELL | SHERWOOD | CASTELLANOS | THORPE | STILES | SADLER | LATHAM | REDMOND | GREENBERG | COTE | WADDELL | DUKES | DIAMOND | BUI | MADRID | ALONSO | SHEETS | IRVIN | HURT | FERRIS | SEWELL | CARLTON | ARAGON | BLACKMON | HADLEY | HOYT | MCGRAW | PAGAN | LAND | TIDWELL | LOVELL | HUGO | MINER | DOSS | DAHL | DELATORRE | STANFORD | KAUFFMAN | VELA | GAGNON | WINSTON | GOMES | THACKER | CORONADO | ASH | JARRETT | HAGER | MYERS | SAMUELS | METZGER | RAINES | SPIVEY | MAURER | HAN | VOSS | HENLEY | CABALLERO | CARUSO | COULTER | NORTH | FINN | CAHILL | LANIER | SOUZA | MCWILLIAMS | DEAL | SCHAFFER | URBAN | HOUSER | CUMMINS | ROMO | CROCKER | BASSETT | KRUSE | BOLDEN | YBARRA | METZ | MCMULLEN | CRUMP | HAGAN | GUIDRY | BRANTLEY | KEARNEY | BEAL | TOTH | JORGENSEN | TIMMONS | TIMOTHY | MILTON | TRIPP | HURD | SAPP | WHITMAN | MESSER | BURGOS | MAJOR | WESTBROOK | CASTLE | SERNA | CARLISLE | VARELA | CULLEN | WILHELM | BERGERON | BURGER | POSEY | BARNHART | HACKETT | MADRIGAL | EUBANKS | SIZEMORE | HILLIARD | HARGROVE | BOUCHER | THOMASON | MELVIN | ROPER | BARNARD | FONSECA | PEDERSEN | QUIROZ | WASHBURN | HOLLIDAY | YEE | RUDOLPH | BERMUDEZ | COYLE | GIL | GOODRICH | PINA | ELIAS | LOCKWOOD | CABRAL | CARRANZA | DUVALL | CORNELIUS | MCCOLLUM | STREET | MCNEAL | CONNORS | ANGEL | PAULSON | HINSON | KEENAN | SHELDON | FARR | EDDY | SAMUEL | LEDBETTER | RING | BETTS | FONTENOT | GIFFORD | HANNAH | HANLEY | PERSON | FOUNTAIN | LEVIN | STUBBS | HIGHTOWER | MURDOCK | KOEHLER | MA | ENGLE | SMILEY | CARMICHAEL | SHEFFIELD | LANGSTON | MCCRACKEN | YOST | TROTTER | STORY | STARKS | LUJAN | BLOUNT | CODY | RUSHING | BENOIT | HERNDON | JACOBSEN | NIETO | WISEMAN | LAYTON | EPPS | SHIPLEY | LEYVA | REEDER | BRAND | PANDEY | NAIDU | PRIYANKA | NIKITA | FARAH | ROLAND | FITCH | RICO | NAPIER | CRONIN | MCQUEEN | PAREDES | TRENT | CHRISTIANSEN | CHRIS | PETTIT | SPANGLER | LANGFORD | BENAVIDES | PENN | PAIGE | WEIR | DIETZ | PRATER | BREWSTER | LOUIS | DIEHL | PACK | SPAULDING | AVILES | ERNST | NOWAK | OLVERA | ROCK | MANSFIELD | AQUINO | OGDEN | STACY | RIZZO | SYLVESTER | GILLIS | SANDS | MACHADO | LOVETT | DUONG | HYATT | LANDIS | PLATT | BUSTAMANTE | HEDRICK | PRITCHETT | GASTON | DOBSON | CAUDILL | TACKETT | BATEMAN | LANDERS | CARMONA | GIPSON | URIBE | MCNEILL | LEDFORD | MIMS | ABEL | SMALLWOOD | THORNE | MCHUGH | DICKENS | LEUNG | TOBIN | KOWALSKI | MEDEIROS | COPE | KRAUS | QUEZADA | OVERTON | MONTALVO | STALEY | WOODY | HATHAWAY | OSORIO | LAIRD | DOBBS | CAPPS | PUTNAM | LAY | FRANCISCO | ADAIR | BERNSTEIN | HUTTON | BURKETT | RHOADES | RICHEY | YANEZ | BLEDSOE | MCCAIN | BEYER | CATES | ROCHE | SPICER | QUEEN | DOTY | DARLING | DARBY | SUMNER | KINCAID | HAY | GROSSMAN | LACEY | WILKES | HUMPHRIES | PAZ | DARNELL | KEYS | KYLE | LACKEY | VOGT | LOCKLEAR | KISER | PRESLEY | BRYSON | BERGMAN | MCCLENDON | CORLEY | PRADO | CHRISTIE | DELONG | SKAGGS | DILL | SHEARER | JUDD | STAPLETON | FLAHERTY | CASILLAS | PINTO | HAYWOOD | YOUNGBLOOD | TONEY | RICKS | GRANADOS | CRUM | TRIPLETT | SORIANO | WAITE | HOFF | ANAYA | CRENSHAW | JUNG | CANALES | CAGLE | DENNY | MARCUS | BERMAN | MUNSON | OCAMPO | BAUMAN | CORCORAN | KEEN | ZIMMER | FRIEND | ORNELAS | VARNER | PELLETIER | VERNON | BLUM | ALBRECHT | CULVER | SCHUSTER | CUELLAR | MCCORD | SHULTZ | MCRAE | MORELAND | CALVERT | WILLIAM | WHITTINGTON | ECKERT | KEENE | MOHR | HANKS | KIMBLE | CAVANAUGH | CROWELL | RUSS | FELICIANO | CRAIN | BUSCH | MCCORMACK | DRUMMOND | OMALLEY | ALDRICH | LUKE | GRECO | MOTT | OAKES | MALLORY | MCLAIN | BURROWS | OTERO | ALLRED | EASON | FINNEY | WELLER | WALDRON | CHAMPION | JEFFERS | COON | ROSENTHAL | HUDDLESTON | SOLANO | HIRSCH | AKINS | OLIVARES | SONG | SNEED | BENEDICT | BAIN | OKEEFE | HIDALGO | MATOS | STALLINGS | PARIS | GAMEZ | KENNY | QUIGLEY | SATISH | MARRERO | FAGAN | DUTTON | ATWOOD | PAPPAS | BAGLEY | MCGOVERN | LUNSFORD | MOSELEY | READ | OAKLEY | ASHBY | GRANGER | SHAVER | HOPE | COE | BURROUGHS | HELM | AMBROSE | NEUMANN | MICHAELS | PRESCOTT | DUMAS | STRINGER | CURRIE | COMER | FONG | WHITLOCK | LEMUS | HAWLEY | ULRICH | STAPLES | BOYKIN | KNUTSON | GROVER | HOBSON | CORMIER | DORAN | THAYER | WOODSON | WHITT | HOOKER | KOHLER | ADDISON | VANDYKE | SCHRADER | HASKINS | WHITTAKER | MADSEN | GAUTHIER | BURNETTE | KEATING | PURVIS | ALEMAN | HUSTON | HAMLIN | PIMENTEL | GERBER | HOOKS | SCHWAB | HONEYCUTT | SCHULTE | ALONZO | ISAAC | CONROY | ADLER | EASTMAN | COTTRELL | OROURKE | HAWK | GOLDSMITH | CRANDALL | RADER | REYNOSO | SHOOK | ABERNATHY | BAER | OLIVAS | GRAYSON | BARTLEY | HENNING | PARR | DUFF | BRUNSON | BAUM | ENNIS | LAUGHLIN | FOOTE | VALADEZ | ADAMSON | BEGAY | STOVALL | LINCOLN | CHEUNG | MALLOY | RIDER | NAIR | GIORDANO | JANSEN | LOPES | ARNETT | PENDLETON | GAGE | BARRAGAN | KEYES | NAVARRETE | AMADOR | HOFFMANN | HAWTHORNE | SCHILLING | PERDUE | SCHREIBER | AREVALO | NAYLOR | DELUCA | MARCUM | ALTMAN | MARK | CHADWICK | DOAN | EASLEY | LADD | WOODALL | BETANCOURT | SHIN | MAGUIRE | BELLAMY | QUINTANILLA | SORENSON | MATTSON | BRENNER | MEANS | FAUST | CALLOWAY | OJEDA | MCNALLY | DIETRICH | RANSOM | HARE | FELTON | WHITING | BURKHART | CLINTON | SCHWARZ | CLEARY | WETZEL | REAGAN | STJOHN | CHOW | HAUSER | DUPREE | BRANNON | LYLES | PRATHER | WILLOUGHBY | SEPULVEDA | NUGENT | PICKENS | JOINER | MOSHER | STONER | DOWLING | TRIMBLE | VALDES | CHEEK | SCRUGGS | COY | TILLEY | BARNEY | SAYLOR | NAGY | HORVATH | LAI | COREY | RUTH | SAUER | BARON | THAO | ROWELL | GRUBBS | HILLMAN | SCHAEFFER | SAMS | HOGUE | HUTSON | BUSBY | NICKERSON | BRUNER | PARHAM | ANDERS | RENDON | LOMBARDO | IVERSON | KINSEY | EARL | BORDEN | JEAN | TITUS | TELLEZ | BEAVERS | CORNETT | SOTELO | KELLOGG | BURNHAM | MCNAIR | SILVERMAN | JERNIGAN | ESCAMILLA | BARROW | COATS | LONDON | REDDING | RUFFIN | YI | BOUDREAUX | GOODSON | DOWELL | FENTON | MOCK | DOZIER | BYNUM | GALE | JOLLY | BECKMAN | GODDARD | CRAVEN | WHITMORE | LEARY | MCCLOUD | GAMBOA | KERNS | BRUNNER | HOUGH | NEGRON | CUTLER | LEDESMA | PYLE | MONAHAN | TABOR | BURK | LEONE | STAUFFER | HAYWARD | DRIVER | RUFF | TALBOT | SEALS | BOSTON | CARBAJAL | FAY | PURDY | MCGREGOR | SUN | ORELLANA | GENTILE | MAHAN | BROWER | PATINO | THURSTON | SHIPMAN | AARON | TORREZ | CALL | WEINER | WILBURN | OLIVA | HAIRSTON | COLEY | HUMMEL | ARREOLA | WATT | SHARMA | LENTZ | ARCE | POWER | LONGORIA | WAGONER | BURR | HSU | TINSLEY | BEEBE | WRAY | NUNN | PRIETO | GERMAN | ROWLEY | BRITO | GRUBB | ROYAL | VALENTIN | BARTHOLOMEW | SCHULER | ARANDA | FLINT | HEARN | VENEGAS | UNGER | MATTINGLY | BOLES | BARGER | CASAS | JULIAN | DOW | DOBBINS | VANN | CHESTER | STRANGE | LEMON | KAHN | MCKINNON | GANNON | WAGGONER | CONN | MEEK | CAVAZOS | SKELTON | LO | KUMAR | TOLEDO | LORENZ | VALLEJO | STARKEY | KITCHEN | REAVES | DEMARCO | FARRAR | STEARNS | MICHAUD | HIGGINBOTHAM | FERNANDES | ISAACS | MARION | GUILLORY | PRIEST | MEEHAN | OLIVEIRA | PALMA | OSWALD | GALVEZ | LOOMIS | LIND | MENA | STCLAIR | HINDS | REARDON | ALLEY | BARTH | CROOK | BLISS | NAGEL | BANUELOS | PARISH | HARMAN | DOUGLASS | KEARNS | NEWCOMB | MULLIGAN | COUGHLIN | WAY | FOURNIER | LAWLER | KAMINSKI | BARBOUR | SOUSA | STUMP | ALANIZ | IRELAND | RUDD | CARNES | LUNDY | GODINEZ | PULIDO | DENNISON | BAUMANN | BURDICK | DOVE | STODDARD | LIANG | ROARK | BOWSER | MCMAHAN | PARNELL | MAYBERRY | WAKEFIELD | ARNDT | OGLE | WORTHINGTON | DURBIN | ESCALANTE | PEDERSON | WELDON | VICK | KNOTT | RYDER | ZARATE | IRVING | CLEMENS | SHELLEY | SALTER | JACK | DASILVA | MUHAMMAD | SQUIRES | RAPP | DAWKINS | POLANCO | CHATMAN | MAIER | YAZZIE | GRUBER | STATON | BLACKMAN | MCDONNELL | DYKES | LAWS | WHITTEN | PFEIFFER | VIDAL | EARLY | KELSEY | BAUGHMAN | DIAS | STARNES | CRESPO | KILPATRICK | LOMBARDI | DEATON | SATTERFIELD | WILES | WEINSTEIN | ROWAN | DELOSSANTOS | HAMBY | ESTEP | DAIGLE | ELAM | CREECH | CHAVIS | HECK | ECHOLS | FOSS | TRAHAN | STRAUSS | VANHORN | WINSLOW | REA | FAIRCHILD | HEATON | MINTON | HITCHCOCK | LINTON | HANDY | CROUSE | COLES | FOY | UPTON | HERRINGTON | HWANG | MCCLELLAND | RECTOR | LUTHER | KRUGER | SALCEDO | CHANCE | GUNDERSON | THARP | GRIFFITHS | GRAF | BRANHAM | HUMPHREYS | RENNER | LIMA | ROONEY | MOYA | ALMEIDA | GAVIN | COBURN | OUELLETTE | GOETZ | SEAY | PARROTT | HARMS | ROBB | STOREY | BARBOSA | BARRAZA | LOYD | MERCHANT | DONOHUE | CARRIER | DIGGS | CHASTAIN | SHERRILL | WHIPPLE | BRASWELL | WEATHERS | LINDER | CHAPA | BOCK | OH | LOVELACE | SAAVEDRA | FERRARA | CALLAWAY | SALMON | TEMPLETON | CHRISTY | HARP | DOWD | FORRESTER | LAWTON | EPSTEIN | GANT | TIERNEY | SEAMAN | CORRAL | DOWDY | ZARAGOZA | MORRISSEY | ELLER | CHAU | BREEN | HIGH | NEWBERRY | BEAM | YANCEY | JARRELL | CERDA | ELLSWORTH | LOFTON | THIBODEAUX | POOL | RINEHART | ARTEAGA | MARLOW | HACKER | WILL | MACKENZIE | HOOK | GILLILAND | EMMONS | PICKERING | MEDLEY | ANDREW | WILLEY | SHELL | RANDLE | BRINKLEY | PRUETT | TOBIAS | EDMONDSON | GRIER | ASKEW | BATISTA | SALDIVAR | MOELLER | AUGUSTINE | CHAVARRIA | TROYER | LAYNE | MCNULTY | SHANK | DESAI | HERRMANN | HEMPHILL | BEARDEN | SPEAR | KEENER | HOLGUIN | CULP | BRADEN | BRISCOE | BALES | GARVIN | STOCKTON | ABREU | SUGGS | MCCARTNEY | FERRER | RHOADS | HA | NEVAREZ | SINGLETARY | CHONG | ALCALA | CHENEY | WESTFALL | DAMICO | SNODGRASS | DEVRIES | LOONEY | HEIN | LYLE | LOCKETT | JACQUES | BARKLEY | WAHL | APONTE | MYRICK | BOLIN | HOLM | SLACK | MARTINO | SCHERER | BACHMAN | ELY | NESBITT | MARROQUIN | BOUCHARD | MAST | JAMESON | HILLS | MIRELES | BUENO | PEASE | VITALE | ALARCON | LINARES | SCHELL | LIPSCOMB | ARRIAGA | BOURGEOIS | BONDS | MARKHAM | IVY | WISNIEWSKI | OLDHAM | FALLON | WENDT | JOY | STAMPER | BABB | STEINBERG | ASHER | FUCHS | BLANK | WILLETT | HEREDIA | CROFT | LYTLE | LASSITER | BARRIENTOS | CONDON | BARFIELD | DARDEN | ARAUJO | GUINN | NOONAN | BURLESON | BELANGER | MAIN | TRAYLOR | MESSINA | ZEIGLER | DANIELSON | MILLARD | KENYON | RADFORD | GRAFF | BEATY | BAGGETT | CRISP | SALISBURY | TROUT | LORENZO | PARSON | GANN | GARBER | ADCOCK | COVARRUBIAS | SCALES | ACUNA | THRASHER | CARD | VAN | MABRY | MOHAMED | MONTANEZ | REDD | STOCK | WILLINGHAM | REDMAN | ZAMBRANO | GAFFNEY | HERR | DEVLIN | PRINGLE | SCHUBERT | CASPER | HOUCK | REES | WING | EBERT | JETER | CORNEJO | GILLETTE | SHOCKLEY | AMATO | GIRARD | LEGGETT | CHEATHAM | BUSTOS | EPPERSON | DUBOSE | SEITZ | EAST | FRIAS | SCHOFIELD | STEEN | ORLANDO | MYLES | CARON | GREY | DENNEY | ONTIVEROS | BURDEN | JAEGER | REICH | WITHERSPOON | NAJERA | FRANTZ | HAMMONDS | XU | LEAVITT | GILCHRIST | ADAM | BARONE | FORMAN | CEJA | RAGSDALE | SISK | TUBBS | ELIZONDO | PRESSLEY | BOLLINGER | LINN | HUNTLEY | DEWEY | GEARY | CARLOS | RAGLAND | MIXON | BAUGH | MCARTHUR | TAM | NOBLES | CLEVENGER | FOUST | LUSK | COONEY | TAMAYO | ROBERT | LONGO | OVERSTREET | OGLESBY | MACE | CHURCHILL | MATSON | HAMRICK | ROCKWELL | TRAMMELL | WHEATLEY | CARRINGTON | FERRARO | RALSTON | CLANCY | MONDRAGON | CARL | HU | HOPSON | BREAUX | MCCURDY | MARES | CHISHOLM | MAI | MATLOCK | AIKEN | CARY | LEMONS | ANGUIANO | HERRICK | CRAWLEY | MONTERO | HASSAN | ARCHULETA | COTTER | FARIAS | PARRIS | FELDER | LUU | PENCE | GILMAN | KILLIAN | NARANJO | DUGGAN | EASTER | SCARBOROUGH | SWANN | RICKETTS | FRANCE | BELLO | NADEAU | STILL | RINCON | CORNWELL | SLADE | FIERRO | MIZE | CHRISTIANSON | GREENFIELD | MCAFEE | LANDRUM | ADAME | DINH | LANKFORD | LEWANDOWSKI | RUST | BUNDY | WATERMAN | MILNER | MCCRARY | HITE | CURLEY | DONALD | DUCKWORTH | CECIL | CARRERA | SPEER | BIRCH | DENSON | BECKWITH | STACK | DURANT | DORMAN | LANTZ | CHRISTMAN | SPANN | MASTERSON | HOSTETLER | KOLB | BRINK | SCANLON | NYE | BEVERLY | WYLIE | WOO | SPURLOCK | SHELBY | SOMMER | REINHARDT | ROBLEDO | ASHTON | BERTRAND | CYR | EDGAR | DOE | HARKINS | BRUBAKER | STOLL | DANGELO | ZHOU | MOULTON | HANNON | FALK | RAINS | BROUGHTON | APPLEGATE | HUDGINS | SLONE | FARNSWORTH | YOON | PERALES | REEDY | MILAM | FRANZ | PONDER | RICCI | FONTAINE | IRIZARRY | NEW | PUENTE | SELBY | CAZARES | DOUGHTY | MOFFETT | BALDERAS | FINE | SMALLEY | CARLIN | TRINH | DYSON | GALVIN | VALDIVIA | BENNER | TURPIN | LYMAN | BILLINGSLEY | JIM | MCADAMS | CARDWELL | FRALEY | PATTEN | HOLTON | SHANKS | MCALISTER | CANFIELD | SAMPLE | HARLEY | CASON | TOMLIN | AHMAD | COYNE | FORTE | RIGGINS | LITTLEJOHN | FORSYTHE | BRINSON | HALVERSON | BACH | STUCKEY | FALCON | TALBERT | WENZEL | CHAMPAGNE | MCHENRY | VEST | SHACKELFORD | ORDONEZ | COLLAZO | BOLAND | SISSON | BIGELOW | HYMAN | WHARTON | BRUMFIELD | OATES | MESA | BECKETT | MORRELL | REIS | ALVES | CHIU | LARUE | STREETER | GROGAN | BLAKELY | BROTHERS | HATTON | KIMBROUGH | LAUER | WALLIS | JETT | PEPPER | HILDEBRAND | RAWLS | MELLO | NEVILLE | BULL | STEFFEN | BRAXTON | COWART | SIMPKINS | MCNEELY | BLALOCK | SPAIN | SHIPP | LINDQUIST | BUTTERFIELD | OREILLY | PERRIN | QUALLS | HAVENS | LUONG | SWITZER | TROUTMAN | FORTNER | TOLLIVER | MONK | POINDEXTER | RUPP | NEGRETE | MUSE | GRESHAM | BEAUCHAMP | SCHMID | CHUN | BRICE | FAULK | WATTERS | BRIONES | GUAJARDO | HARWOOD | GRISSOM | HARLOW | WHELAN | BURDETTE | PALUMBO | PAULSEN | CORRIGAN | GARVEY | LEVESQUE | DOCKERY | DELGADILLO | GOOCH | CAO | MULLIN | RIDLEY | STANFIELD | NORIEGA | CEBALLOS | NUNES | NEWBY | BAUMGARTNER | HUSSAIN | WYMAN | CAUSEY | GOSSETT | NESS | WAUGH | CHOATE | CARMAN | DAILY | DEVORE | IRBY | KONG | BREEDEN | WHATLEY | ELLINGTON | LAMAR | FULTZ | BAIR | ZIELINSKI | COLBY | HOUGHTON | GRIGSBY | FORTUNE | PAXTON | MCMILLIAN | HAMMONS | BRONSON | KECK | WELLMAN | AYRES | WHITESIDE | MENARD | ROUSH | WARDEN | ESPINO | STRAND | HAGGERTY | BANDA | FABIAN | KREBS | BOWIE | BRANSON | LENZ | BENAVIDEZ | KEELER | NEWSOM | EZELL | JEFFREY | PULLIAM | CLARY | BYRNES | GARDINER | SOMMERS | FENNELL | MANCINI | OSULLIVAN | SEBASTIAN | SHANKAR | BRUNS | GIRON | BOYLES | KEEFE | MUIR | SHULER | VERGARA | PEMBERTON | BROWNLEE | BROCKMAN | FANNING | ROYER | HERZOG | MORLEY | BETHEA | NEEDHAM | ROQUE | MOJICA | FRANCOIS | KUNTZ | SNOWDEN | WITHERS | HARLAN | SEIBERT | LIMON | KIEFER | ALLAN | SKIDMORE | DUNAWAY | FINNEGAN | WOLFORD | SEELEY "

not_names = "email|phone|name|SUMMARY|professional|experience|education|job|personal|information|Objective|contact|profile|careers|objectives|experience|education|description|date|internal|administration|Phone"


def name_extractor(text, terms, email_id, file_type, filename, phone):
    # try:
    name_text = ""
    
    name_text = name_search_common(terms)
        
    
    if name_text == "": 
        name_text = name_extractor_main(
            text, terms, email_id, file_type, filename, phone)
    name_text = re.sub(
        not_names, " ", name_text, re.IGNORECASE)

    print("name_v1", name_text)
    if name_text == "":

        for t in terms:
            if "name" in t.lower():
                name_text == t
                break

    if name_text == "":
        name_text2 = name_extractor_next(
            text, terms, email_id, file_type, filename, phone)
        return name_text2

    if re.search("Name|NAME|name", name_text, re.IGNORECASE):
        name_text = re.sub("Name|NAME|name", "", name_text)

    name_text = re.sub(r"[^a-zA-Z\s]", "", name_text)
    name_text = re.sub(
        not_names, " ", name_text, re.IGNORECASE)
    return name_text
    # except:
    #     name_text = name_extractor_next(
    #         text, terms, email_id, file_type, filename, phone)
    #     return name_text


def name_extractor_main(text, terms, email_id, file_type, filename, phone):

    temp_terms = []
    for t in terms:
        if re.search(not_names, t, re.IGNORECASE):
            temp_terms.append(re.sub(not_names, "", t, re.IGNORECASE))
        else:
            temp_terms.append(t)
    terms = temp_terms

    start_tokens = terms[:3]

    end_tokens = terms[-2:]
    # word.lower() in nlp.vocab

    name_list = []
    for token in start_tokens:
        name_temp = ""
        for t in token.split():
            if t.lower() not in nlp.vocab and len(t) > 1 and not any(char.isdigit() for char in t):
                if "." in t or t[0].isupper():
                    name_temp += t + " "
        if name_temp != "":
            name_list.append(name_temp)

    print(name_list)
    for token in end_tokens:
        name_temp = ""
        for t in token.split():
            if len(t) > 1 and not any(char.isdigit() for char in t) and '@' not in t:
                if "." in t or t[0].isupper():
                    if t.lower() not in nlp.vocab:
                        name_temp += t + " "
        if name_temp != "":
            name_list.append(name_temp)
    print(name_list)

    # Get user name from email
    username = ""
    if email_id != "" and "@" in email_id:
        username = email_id.split('@')[0]
    print("name_list", username)

    for name in name_list:
        if name != "" and "@" not in name:
            print(name)
            print(jaccard_similarity(name.lower(), username.lower()))
            if jaccard_similarity(name.lower(), username.lower()) > 0.3:
                return name
            if len(username) == 0:
                return name
    if len(name_list) > 0:
        return name_list[0]

    return ""


def name_extractor_next(text, terms, email_id, file_type, filename, phone):
    try:
        name_text = ""
        text = re.sub("SUMMARY|PROFILE|Works|WORKS|HIGHEST|Highest|Qualification|QUALIFICATION|Profile|EXPERIENCE|Experience|Mail|MAIL|Summary|Contact|CONTACT|OVERVIEW|PROFESSIONAL|Professional|Overview", " ", text)
        terms = text.split("\n")
        name_list = []

        # Take the line 1
        name_list.append(name_from_line(text))

        #  Name with title
        name_text = name_from_title(terms)
        if name_text != "" and not re.search(states, name_text):
            name_list.append(name_from_title(terms))
            return name_text

        name_list.append(name_from_filename(filename, terms))

        # First Line Name in DOc or docx
        if re.search("doc|docx|ocx|oc", file_type.lower()):
            name_list.append(name_from_doc(terms))

        # First line name in pdf
        if re.search("pdf|df", file_type.lower()):
            name_list.append(name_from_pdf(terms))

        # Linkedin Name Extract
        if re.search("linkedin", text.lower()):
            name_list.append(name_from_linkedin(text))

        # Email Name Extract
        if re.search("@", email_id):
            name_list.append(name_from_email_id(terms, email_id))

        # US Name Extract
        name_list.append(name_from_us(terms))

        # Indian Name Extract
        name_list.append(name_from_india(terms))
        temp = ""
        terms = []

        for i in range(len(name_list)):
            if not re.search(states, name_list[i]) and not re.search(job_titles, name_list[i].lower()) and not re.search("HIGHEST|Highest|QUALIFICATION|Qualification|NAME|Name|PERSONAL|Personal|SUMMARY|PROFILE|Profile|EXPERIENCE|Experience|Summary|Contact|CONTACT|OVERVIEW|PROFESSIONAL|Professional|Overview|Roles|ROLES|English|ENGLISH|FRENCH|SPANISH|French|Spanish", name_list[i]):
                temp = re.sub("\s+", " ", name_list[i])
                terms.append(temp)

        name_list = terms
        # print(name_list)
        name_text = select_name_list(name_list, filename, phone)
        name_text = name_text_edit(name_text)

        return name_text
    except:
        return ""


def name_from_doc(terms):
    try:
        name_text = ""

        for i in range(len(terms)):
            temp = re.sub('[^a-zA-Z]+', "", terms[i])
            if len(temp) > 2:
                if temp[0].isupper() and len(terms[i].split()) < 10:
                    name_text = terms[i]
                    break

        return name_text
    except:
        return ""


def name_from_pdf(terms):
    try:
        res = terms[:min(5, len(terms))]
        name_text = ""
        text_term = ""
        i = 0
        while len(res[i]) < 3 or len(res[i].split()) > 5 or re.search(name_not, res[i].lower()):
            i += 1
            if i == len(res)-1:
                break

        text_term = res[i]
        text_term = re.sub("\n|\.|\-|\+|,|(|)|\d", " ", text_term)
        name_terms = text_term.split()

        for i in range(len(name_terms)):
            if re.search(name_not, name_terms[i].lower()):
                name_text = ""
                break
            if name_terms[i][0].isupper() and len(name_terms[i]) > 3:
                name_text = name_text + " "+name_terms[i]

        return name_text
    except:
        return ""


def name_from_linkedin(text):
    try:
        res = text.split()
        name_text = ""
        start = -1
        for i in range(len(res)):
            if re.search("linkedin.com", res[i].lower()):
                name_text = res[i].lower()
                if not re.search("linkedin.com/in/\n[a-z]|linkedin.com/in/[a-z]", res[i].lower()):
                    name_text = res[i+1].lower()
                name_text = re.sub("www|\.|http|:|\/|https", "", name_text)
                name_text = re.sub("linkedincomin", "", name_text)
                name_text = re.sub("\-|\n", " ", name_text)
                name_text = re.sub('[^a-zA-Z\s]+', "", name_text)
                name_text = name_text.upper()
                break
        return name_text
    except:
        return ""


def name_from_email_id(terms, email_id):
    try:
        name_text = ""
        back_up_username = ""
        res = []
        if re.search("@", email_id):
            username = email_id[:email_id.index("@")]
            username = re.sub("[^a-zA-Z\._]+", "", username)
            back_up_username = username
            if re.search("[a-z]\.[a-z]|[a-z]_[a-z]", username):
                name_text = username
                name_text = re.sub("\.|_", " ", name_text.upper())
            else:
                temp_username = ""
                if len(username) > 3:
                    username = username.lower()
                    temp_username = username
                    username = re.sub("\s+", "", username)
                    username = username[:3]

                    for i in range(len(terms)):
                        if re.search(username, terms[i].lower()) and len(terms[i].split()) < 5 and re.search("[A-Z]", terms[i]) and not re.search("@", terms[i]):
                            name_text = terms[i]
                            break
                    username = temp_username

                    if name_text == "" and len(username) > 5:
                        username = re.sub("[^a-z]+", "", temp_username)
                        username = username[-3:]

                        for i in range(len(terms)):
                            if re.search(username, terms[i].lower()) and re.search("[A-Z]", terms[i]) and not re.search("@", terms[i]):
                                name_text = terms[i]
                                break

        if name_text == "":
            name_text = back_up_username

        return name_text
    except:
        return ""


def name_from_us(terms):
    try:
        name_text = ""

        for i in range(len(terms)):
            if len(terms[i].split()) < 5 or (len(terms[i].split()) < 8 and len(terms[i]) < 25):
                if re.search("[A-Z]", terms[i]) and not re.search(name_not, terms[i].lower()):
                    if re.search(US_human_names, terms[i].upper()):

                        if len(re.search(US_human_names, terms[i].upper())[0]) > 3:
                            name_text = terms[i]
                            break

        return name_text
    except:
        return ""


def name_from_india(terms):
    try:
        name_text = ""

        for i in range(len(terms)):
            if re.search("personal", terms[i].lower()) and "P" in terms[i]:
                start = i
                break

        terms = terms[i:]

        for i in range(len(terms)):
            if re.search("name|n ame", terms[i].lower()) and not re.search("father|project|mother|company", terms[i].lower()):
                name_text = terms[i].lower()
                name_text = re.sub("name|n ame", " ", name_text)
                name_text = re.sub("\.|:|=", " ", name_text)

        return name_text
    except:
        return ""


def name_from_title(terms):
    try:
        temp = ""
        name_text = ""

        for i in range(5):
            temp = terms[i].upper()
            temp = re.sub(",", " ", temp)
            temp = re.sub("\.", " ", temp)
            if re.search(name_designation, temp):
                name_text = terms[i]
                name_text = re.sub(",|\.", " ", name_text)
                name_text = re.sub("PMP|PHD|MBA|MSC|CSM|CPA",
                                   " ", name_text.upper())
                break
        return name_text
    except:
        return ""


def name_from_line(text):
    try:
        name_text = ""
        res = text.split("\n")
        if re.search("[A-Z]", res[0]) and len(res[0]) > 4:
            name_text = res[0]

        return name_text
    except:
        return ""


def name_from_filename(filename, terms):
    try:
        filename = re.sub("[^a-zA-Z]+", "", filename)

        filename = filename.lower()
        filename = re.sub("resume|abc|xyz|pqr|def|", "", filename)
        filename = filename[:min(4, len(filename))]
        # print(filename)
        if len(filename) > 5:
            for i in range(len(terms)):
                if filename in terms[i].lower() and len(terms[i].split()) < 10:
                    name_text = terms[i]
                    return name_text
        return ""
    except:
        return ""


def select_name_list(name_list, filename, phone):

    temp = ""
    terms = []

    back_up = name_list

    for i in range(len(name_list)):
        res = name_list[i].split()
        temp = ""
        for j in range(len(res)):
            if not re.search(name_not, res[j].lower()):
                temp = temp + " " + res[j]
        if re.search("[a-zA-Z]", temp) and len(temp) > 3:
            terms.append(temp)

    name_list = terms

    for i in range(len(name_list)):
        if len(name_list[i]) > 1 and not re.search(states, name_list[i]):
            terms.append(name_list[i])

    name_list = terms
    name_text = ""
    temp = ""
    terms = []
    temp = ""
    terms = []
    for i in range(len(name_list)):
        if len(name_list) > 1:
            if re.search("[a-zA-Z]", name_list[i]) and (len(name_list[i].split()) < 10 or len(name_list[i]) < 25):
                temp = re.sub("[0-9]|:", "", name_list[i])
                temp = re.sub(
                    "Email:|Tel:|Name:|NAME|PERSONAL|DATA|Personal|Data|EMAIL|CONTACT|Contact", "", temp)
                res = temp.split()
                temp = ""
                for j in res:
                    if not "@" in j:
                        temp = temp + " " + j
                terms.append(temp)
    name_list = terms

    if len(name_list) < 1:
        name_list = back_up

    # US Name Pickup
    if name_text == "":
        for i in range(len(name_list)):
            temp = re.sub("\.|,", " ", name_list[i])
            temp = re.sub("[^a-zA-Z\s]+", " ", temp)
            temp = " " + temp + " "
            if re.search(US_human_names, temp.upper()):
                if len(re.search(US_human_names, temp.upper())[0]) > 3:
                    name_text = name_list[i]
                    return name_text

    # CHeck if there are similar words in file or list
    terms = []
    for i in range(len(name_list)):
        temp = re.sub("[^a-z]+", "", name_list[i].lower())
        terms.append(temp)

    # print(name_list)

    filename = re.sub("[^a-zA-Z]+", "", filename)

    filename = filename.lower()
    filename = re.sub("resume|abc|xyz|pqr|def|", "", filename)
    filename = filename[:min(4, len(filename))]
    if len(filename) > 3:
        for i in range(len(terms)):
            if filename in terms[i]:
                name_text = name_list[i]
                if len(name_text) > 2:
                    return name_text

    for i in range(len(terms)):
        for j in range(len(terms)):
            if terms[i] == terms[j] and terms[i] != "" and i != j:
                name_text = name_list[i]
                return name_text

    # Last go to
    if name_text == "":
        for i in range(len(name_list)):
            if len(name_list[i]) > 2 and re.search("[A-Z]", name_list[i]):
                return name_list[i]

    return name_text


def name_text_edit(name_text):
    try:
        name_text = re.sub("\s+|\-|\|\.", " ", name_text)
        name_text = re.sub("[^a-zA-Z\s]+", " ", name_text)
        res = name_text.split()
        name_text = ""
        for i in range(len(res)):
            if res[i][0].isupper():
                name_text = name_text+" " + res[i]

        if len(name_text.split()) > 3 and len(name_text) > 22:
            res = name_text.split()
            temp = ""
            for i in range(0, 3):
                temp = temp + " " + res[i]
            name_text = temp

        return name_text
    except:
        return ""


def jaccard_similarity(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    if not union:
        return 0.0

    similarity = len(intersection) / len(union)
    return similarity

def name_search_common(terms):
    common_indian_names  = "Patel|Sharma|Dhawan|Shah|Chauhan|Chavan|Chaudhari|Chaudhary|Chaudhry|Singh|Patel|Reddy|Konda|Kumar|Gupta|Yadav|Agarwal|Pandey|Mukherjee|Chatterjee|Kapoor|Mehta|Tyagi|Khan|Desai|Joshi|Mehta|Srinivasan|Iyer|Nair|Malhotra|Verma"
    for i in range(len(terms)):
        if re.search(common_indian_names,terms[i], re.IGNORECASE):
            print("Searched")
            print(len(terms[i].split()))
            if len(terms[i].split()) > 1 and len(terms[i].split()) < 7:
                return terms[i]
    return ""