import re

name_not  = "profession|overview|concept|hindi|french|laude|pyscholog|event|skill|plan|social|media|profit|publication|list|arabic|county|technologies|problem|russian|influence|saving|healthcare|expertise|learning|github|presentation|strateg|role|minor|linkedin|spanish|basics|studio|english|adobe|creative|microsoft|instructor|office|website|award|design|mission|manage|consult|domain|respons|excel|mobile|resource|budget|fundrais|produ|certi|profil|area|special|software|service|business|synopsis|~|&|tool|course|contact|detail|degree|phone|honor|descript|title|sales|designer|care|goal|cell|name|organization|intro|qualif|father|developer|educat|exam|year|institu|academ|internship|internship|work|chinese|german|work|employ|www|http|employ|career|career|employment|employer|language|employer|project|summary|technical|skill|engineer|place|ltd|company|skills|experience|declaration|personal|activities|projects|story|objective|professional|summary|history|personal|@|email|background|internship|technical|freelance|community|activities|work|exposure|strength|achievements|career|pvt|private|ltd|limited|llc|corp|industr|solutions|school|college|university|bachelor|master|training"

US_human_names = "SMITH|HASAN|NAIK|REDDY|GOWDA|JAIN|SINGH|MODI|MANJU|RAMESH|RAMA|AASHIK|NAIDU|THAKUR|TRIPATHI|THAKAR|THACKERAY|TAPAR|SINHA|SAWANT|EMILY|CHARLOTTE|JANE|ERIC|FLAVIA|JOHNSON|EVELYN|WILLIAMS|JESSICA|BROWN|JONES|MILLER|DAVIS|GARCIA|RODRIGUEZ|WILSON|MARTINEZ|ANDERSON|TAYLOR|THOMAS|HERNANDEZ|MOORE|MARTIN|JACKSON|THOMPSON|WHITE|LOPEZ|LEE|GONZALEZ|HARRIS|CLARK|LEWIS|ROBINSON|WALKER|PEREZ|HALL|YOUNG|ALLEN|SANCHEZ|WRIGHT|KING|SCOTT|GREEN|BAKER|ADAMS|NELSON|HILL|RAMIREZ|CAMPBELL|MITCHELL|ROBERTS|CARTER|PHILLIPS|EVANS|TURNER|TORRES|PARKER|COLLINS|EDWARDS|STEWART|FLORES|MORRIS|NGUYEN|MURPHY|RIVERA|COOK|ROGERS|MORGAN|PETERSON|COOPER|REED|BAILEY|BELL|GOMEZ|KELLY|HOWARD|WARD|COX|DIAZ|RICHARDSON|WOOD|WATSON|BROOKS|BENNETT|GRAY|JAMES|REYES|CRUZ|HUGHES|PRICE|MYERS|LONG|FOSTER|SANDERS|ROSS|MORALES|POWELL|SULLIVAN|RUSSELL|ORTIZ|GUTIERREZ|PERRY|BUTLER|BARNES|FISHER|HENDERSON|DAN|COLEMAN|SIMMONS|PATTERSON|JORDAN|REYNOLDS|HAMILTON|GRAHAM|KIM|GONZALES|ALEXANDER|RAMOS|WALLACE|GRIFFIN|WEST|COLE|HAYES|CHAVEZ|GIBSON|BRYANT|ELLIS|STEVENS|MURRAY|FORD|MARSHALL|OWENS|MCDONALD|HARRISON|RUIZ|KENNEDY|WELLS|ALVAREZ|WOODS|MENDOZA|CASTILLO|OLSON|WEBB|WASHINGTON|TUCKER|BURNS|HENRY|VASQUEZ|SNYDER|SIMPSON|CRAWFORD|JIMENEZ|PORTER|MASON|SHAW|GORDON|WAGNER|HUNTER|ROMERO|HICKS|DIXON|HUNT|PALMER|ROBERTSON|BLACK|HOLMES|STONE|MEYER|BOYD|MILLS|WARREN|FOX|ROSE|RICE|MORENO|SCHMIDT|PATEL|FERGUSON|NICHOLS|HERRERA|MEDINA|RYAN|FERNANDEZ|WEAVER|DANIELS|STEPHEN|GARDNER|PAYNE|KELLEY|DUNN|PIERCE|ARNOLD|TRAN|SPENCER|PETERS|HAWKINS|GRANT|HANSEN|CASTRO|HOFFMAN|HART|ELLIOTT|CUNNINGHAM|KNIGHT|BRADLEY|CARROLL|HUDSON|DUNCAN|ARMSTRONG|BERRY|ANDREWS|JOHNSTON|RAY|LANE|RILEY|CARPENTER|PERKINS|AGUILAR|SILVA|RICHARDS|WILLIS|MATTHEWS|CHAPMAN|LAWRENCE|GARZA|VARGAS|WATKINS|WHEELER|LARSON|CARLSON|HARPER|GEORGE|GREENE|BURKE|GUZMAN|MORRISON|MUNOZ|JACOBS|OBRIEN|LAWSON|FRANKLIN|LYNCH|BISHOP|CARR|SALAZAR|AUSTIN|MENDEZ|GILBERT|JENSEN|WILLIAMSON|MONTGOMERY|HARVEY|OLIVER|HOWELL|DEAN|HANSON|WEBER|GARRETT|SIMS|BURTON|FULLER|SOTO|MCCOY|WELCH|CHEN|SCHULTZ|WALTERS|REID|FIELDS|WALSH|LITTLE|FOWLER|BOWMAN|DAVIDSON|MAY|DAY|SCHNEIDER|NEWMAN|BREWER|LUCAS|HOLLAND|WONG|BANKS|SANTOS|CURTIS|PEARSON|DELGADO|VALDEZ|PENA|RIOS|DOUGLAS|SANDOVAL|BARRETT|HOPKINS|KELLER|GUERRERO|STANLEY|BATES|ALVARADO|BECK|ORTEGA|WADE|ESTRADA|CONTRERAS|BARNETT|CALDWELL|SANTIAGO|LAMBERT|POWERS|CHAMBERS|MIKE|NUNEZ|CRAIG|LEONARD|LOWE|RHODES|BYRD|GREGORY|SHELTON|FRAZIER|BECKER|MALDONADO|FLEMING|VEGA|SUTTON|COHEN|JENNINGS|PARKS|MCDANIEL|WATTS|BARKER|NORRIS|VAUGHN|VAZQUEZ|HOLT|SCHWARTZ|STEELE|BENSON|NEAL|DOMINGUEZ|HORTON|TERRY|WOLFE|HALE|LYONS|GRAVES|HAYNES|MILES|PARK|WARNER|PADILLA|BUSH|THORNTON|MCCARTHY|MANN|ZIMMERMAN|ERICKSON|FLETCHER|MCKINNEY|LAUREN|DAWSON|JOSEPH|MARQUEZ|REEVES|KLEIN|ESPINOZA|BALDWIN|MORAN|LOVE|ROBBINS|HIGGINS|BALL|CORTEZ|LE|GRIFFITH|BOWEN|SHARP|CUMMINGS|RAMSEY|HARDY|SWANSON|BARBER|ACOSTA|LUNA|CHANDLER|BLAIR|DANIEL|SIMON|DENNIS|OCONNOR|QUINN|GROSS|NAVARRO|MOSS|FITZGERALD|DOYLE|MCLAUGHLIN|ROJAS|RODGERS|STEVENSON|SINGH|YANG|FIGUEROA|HARMON|NEWTON|PAUL|MANNING|GARNER|MCGEE|REESE|FRANCIS|BURGESS|ADKINS|GOODMAN|CURRY|BRADY|CHRISTENSEN|POTTER|WALTON|GOODWIN|MULLINS|MOLINA|WEBSTER|FISCHER|CAMPOS|AVILA|SHERMAN|TODD|CHANG|BLAKE|MALONE|WOLF|HODGES|JUAREZ|GILL|FARMER|HINES|GALLAGHER|DURAN|HUBBARD|CANNON|MIRANDA|WANG|SAUNDERS|TATE|MACK|HAMMOND|CARRILLO|TOWNSEND|WISE|INGRAM|BARTON|MEJIA|AYALA|SCHROEDER|HAMPTON|ROWE|PARSONS|FRANK|WATERS|STRICKLAND|OSBORNE|MAXWELL|CHAN|DELEON|NORMAN|HARRINGTON|CASEY|PATTON|LOGAN|BOWERS|MUELLER|GLOVER|FLOYD|HARTMAN|BUCHANAN|COBB|FRENCH|KRAMER|MCCORMICK|CLARKE|TYLER|GIBBS|MOODY|CONNER|SPARKS|MCGUIRE|LEON|BAUER|NORTON|POPE|FLYNN|HOGAN|ROBLES|SALINAS|YATES|LINDSEY|LLOYD|MARSH|MCBRIDE|OWEN|SOLIS|PHAM|LANG|PRATT|LARA|BROCK|BALLARD|TRUJILLO|SHAFFER|DRAKE|ROMAN|AGUIRRE|MORTON|STOKES|LAMB|PACHECO|PATRICK|COCHRAN|SHEPHERD|CAIN|BURNETT|HESS|CERVANTES|OLSEN|BRIGGS|OCHOA|CABRERA|VELASQUEZ|MONTOYA|ROTH|MEYERS|CARDENAS|FUENTES|WEISS|HOOVER|WILKINS|NICHOLSON|UNDERWOOD|SHORT|CARSON|MORROW|COLON|HOLLOWAY|SUMMERS|BRYAN|PETERSEN|MCKENZIE|SERRANO|WILCOX|CAREY|CLAYTON|POOLE|CALDERON|GALLEGOS|GREER|RIVAS|GUERRA|DECKER|COLLIER|WALL|WHITAKER|BASS|FLOWERS|DAVENPORT|CONLEY|HOUSTON|HUFF|COPELAND|HOOD|MONROE|MASSEY|ROBERSON|COMBS|FRANCO|LARSEN|PITTMAN|RANDALL|SKINNER|WILKINSON|KIRBY|CAMERON|BRIDGES|ANTHONY|RICHARD|KIRK|BRUCE|SINGLETON|MATHIS|BRADFORD|BOONE|ABBOTT|CHARLES|ALLISON|SWEENEY|ATKINSON|HORN|JEFFERSON|ROSALES|YORK|CHRISTIAN|PHELPS|FARRELL|CASTANEDA|NASH|DICKERSON|BOND|WYATT|FOLEY|CHASE|GATES|VINCENT|MATHEWS|HODGE|GARRISON|TREVINO|VILLARREAL|HEATH|DALTON|VALENCIA|CALLAHAN|HENSLEY|ATKINS|HUFFMAN|ROY|BOYER|SHIELDS|LIN|HANCOCK|GRIMES|GLENN|CLINE|DELACRUZ|CAMACHO|DILLON|PARRISH|ONEILL|MELTON|BOOTH|KANE|BERG|HARRELL|PITTS|SAVAGE|WIGGINS|BRENNAN|SALAS|MARKS|RUSSO|SAWYER|BAXTER|GOLDEN|HUTCHINSON|LIU|WALTER|MCDOWELL|WILEY|RICH|HUMPHREY|JOHNS|KOCH|SUAREZ|HOBBS|BEARD|GILMORE|IBARRA|KEITH|MACIAS|KHAN|ANDRADE|WARE|STEPHENSON|HENSON|WILKERSON|DYER|MCCLURE|BLACKWELL|MERCADO|TANNER|EATON|CLAY|BARRON|BEASLEY|ONEAL|PRESTON|ZAMORA|MACDONALD|VANCE|SNOW|MCCLAIN|STAFFORD|OROZCO|BARRY|ENGLISH|SHANNON|KLINE|JACOBSON|WOODARD|HUANG|KEMP|MOSLEY|PRINCE|MERRITT|HURST|VILLANUEVA|ROACH|NOLAN|LAM|YODER|MCCULLOUGH|LESTER|SANTANA|VALENZUELA|WINTERS|BARRERA|LEACH|ORR|BERGER|MCKEE|STRONG|CONWAY|STEIN|WHITEHEAD|BULLOCK|ESCOBAR|KNOX|MEADOWS|SOLOMON|VELEZ|ODONNELL|KERR|STOUT|BLANKENSHIP|BROWNING|KENT|LOZANO|BARTLETT|PRUITT|BUCK|BARR|GAINES|DURHAM|GENTRY|MCINTYRE|SLOAN|MELENDEZ|ROCHA|HERMAN|SEXTON|MOON|HENDRICKS|RANGEL|STARK|LOWERY|HARDIN|HULL|SELLERS|ELLISON|CALHOUN|GILLESPIE|MORA|KNAPP|MCCALL|MORSE|DORSEY|WEEKS|NIELSEN|LIVINGSTON|LEBLANC|MCLEAN|BRADSHAW|GLASS|MIDDLETON|BUCKLEY|SCHAEFER|FROST|HOWE|HOUSE|MCINTOSH|HO|PENNINGTON|REILLY|HEBERT|MCFARLAND|HICKMAN|NOBLE|SPEARS|CONRAD|ARIAS|GALVAN|VELAZQUEZ|HUYNH|FREDERICK|RANDOLPH|CANTU|FITZPATRICK|MAHONEY|PECK|VILLA|MICHAEL|DONOVAN|MCCONNELL|WALLS|BOYLE|MAYER|ZUNIGA|GILES|PINEDA|PACE|HURLEY|MAYS|MCMILLAN|CROSBY|AYERS|CASE|BENTLEY|SHEPARD|EVERETT|PUGH|DAVID|MCMAHON|DUNLAP|BENDER|HAHN|HARDING|ACEVEDO|RAYMOND|BLACKBURN|DUFFY|LANDRY|DOUGHERTY|BAUTISTA|SHAH|POTTS|ARROYO|VALENTINE|MEZA|GOULD|VAUGHAN|FRY|RUSH|AVERY|HERRING|DODSON|CLEMENTS|SAMPSON|TAPIA|BEAN|LYNN|CRANE|FARLEY|CISNEROS|BENTON|ASHLEY|MCKAY|FINLEY|BEST|BLEVINS|FRIEDMAN|MOSES|SOSA|BLANCHARD|HUBER|FRYE|KRUEGER|BERNARD|ROSARIO|RUBIO|MULLEN|BENJAMIN|HALEY|CHUNG|MOYER|CHOI|HORNE|YU|WOODWARD|ALI|NIXON|HAYDEN|RIVERS|ESTES|MCCARTY|RICHMOND|STUART|MAYNARD|BRANDT|OCONNELL|HANNA|SANFORD|SHEPPARD|CHURCH|BURCH|LEVY|RASMUSSEN|COFFEY|PONCE|FAULKNER|DONALDSON|SCHMITT|NOVAK|COSTA|MONTES|BOOKER|CORDOVA|WALLER|ARELLANO|MADDOX|MATA|BONILLA|STANTON|COMPTON|KAUFMAN|DUDLEY|MCPHERSON|BELTRAN|DICKSON|MCCANN|VILLEGAS|PROCTOR|HESTER|CANTRELL|DAUGHERTY|CHERRY|BRAY|DAVILA|ROWLAND|LEVINE|MADDEN|SPENCE|GOOD|IRWIN|WERNER|KRAUSE|PETTY|WHITNEY|BAIRD|TERESA|HOOPER|POLLARD|ZAVALA|JARVIS|HOLDEN|HAAS|HENDRIX|MCGRATH|BIRD|LUCERO|TERRELL|RIGGS|JOYCE|MERCER|ROLLINS|GALLOWAY|DUKE|ODOM|ANDERSEN|DOWNS|HATFIELD|BENITEZ|ARCHER|HUERTA|TRAVIS|MCNEIL|HINTON|ZHANG|HAYS|MAYO|FRITZ|BRANCH|MOONEY|RITTER|ESPARZA|FREY|BRAUN|GAY|RIDDLE|HANEY|KAISER|HOLDER|CHANEY|MCKNIGHT|GAMBLE|VANG|COOLEY|CARNEY|COWAN|FORBES|FERRELL|DAVIES|BARAJAS|SHEA|OSBORN|BRIGHT|CUEVAS|BOLTON|MURILLO|LUTZ|DUARTE|KIDD|KEY|COOKE|GOFF|DEJESUS|MARIN|DOTSON|BONNER|COTTON|MERRILL|LINDSAY|LANCASTER|MCGOWAN|FELIX|SALGADO|SLATER|CARVER|GUTHRIE|HOLMAN|FULTON|SNIDER|SEARS|WITT|NEWELL|BYERS|LEHMAN|GORMAN|COSTELLO|DONAHUE|DELANEY|ALBERT|WORKMAN|ROSAS|SPRINGER|JUSTICE|KINNEY|ODELL|LAKE|DONNELLY|LAW|DAILEY|GUEVARA|SHOEMAKER|BARLOW|MARINO|WINTER|CRAFT|KATZ|PICKETT|ESPINOSA|DALY|MALONEY|GOLDSTEIN|CROWLEY|VOGEL|KUHN|PEARCE|HARTLEY|CLEVELAND|PALACIOS|MCFADDEN|BRITT|WOOTEN|CORTES|DILLARD|CHILDERS|ALFORD|DODD|EMERSON|WILDER|LANGE|GOLDBERG|QUINTERO|BEACH|ENRIQUEZ|QUINTANA|HELMS|MACKEY|FINCH|CRAMER|MINOR|FLANAGAN|FRANKS|CORONA|KENDALL|MCCABE|HENDRICKSON|MOSER|MCDERMOTT|CAMP|MCLEOD|BERNAL|KAPLAN|MEDRANO|LUGO|TRACY|BACON|CROWE|RICHTER|WELSH|HOLLEY|RATLIFF|MAYFIELD|TALLEY|HAINES|DALE|GIBBONS|HICKEY|BYRNE|KIRKLAND|FARRIS|CORREA|TILLMAN|SWEET|KESSLER|ENGLAND|HEWITT|BLANCO|CONNOLLY|PATE|ELDER|BRUNO|HOLCOMB|HYDE|MCALLISTER|CASH|CHRISTOPHER|WHITFIELD|MEEKS|HATCHER|FINK|SUTHERLAND|NOEL|RITCHIE|ROSA|LEAL|JOYNER|STARR|MORIN|DELAROSA|CONNOR|HILTON|ALSTON|GILLIAM|WYNN|WILLS|JARAMILLO|ONEIL|NIEVES|BRITTON|RANKIN|BELCHER|GUY|CHAMBERLAIN|TYSON|PUCKETT|DOWNING|SHARPE|BOGGS|TRUONG|PIERSON|GODFREY|MOBLEY|JOHN|KERN|DYE|HOLLIS|BRAVO|MAGANA|RUTHERFORD|NG|TUTTLE|LIM|ROMANO|ARTHUR|TREJO|KNOWLES|LYON|SHIRLEY|QUINONES|CHILDS|DOLAN|HEAD|REYNA|SAENZ|HASTINGS|KENNEY|CANO|FOREMAN|DENTON|VILLALOBOS|PRYOR|SARGENT|DOHERTY|HOPPER|PHAN|WOMACK|LOCKHART|VENTURA|DWYER|MULLER|GALINDO|GRACE|SORENSEN|COURTNEY|PARRA|RODRIGUES|NICHOLAS|AHMED|MCGINNIS|LANGLEY|MADISON|LOCKE|JAMISON|NAVA|GUSTAFSON|SYKES|DEMPSEY|HAMM|RODRIQUEZ|MCGILL|XIONG|ESQUIVEL|SIMMS|KENDRICK|BOYCE|VIGIL|DOWNEY|MCKENNA|SIERRA|WEBBER|KIRKPATRICK|DICKINSON|COUCH|BURKS|SHEEHAN|SLAUGHTER|PIKE|WHITLEY|MAGEE|CHENG|SINCLAIR|CASSIDY|RUTLEDGE|BURRIS|BOWLING|CRABTREE|MCNAMARA|AVALOS|VU|HERRON|BROUSSARD|ABRAHAM|GARLAND|CORBETT|CORBIN|STINSON|CHIN|BURT|HUTCHINS|WOODRUFF|LAU|BRANDON|SINGER|HATCH|ROSSI|SHAFER|OTT|GOSS|GREGG|DEWITT|TANG|POLK|WORLEY|COVINGTON|SALDANA|HELLER|EMERY|SWARTZ|CHO|MCCRAY|ELMORE|ROSENBERG|SIMONS|CLEMONS|BEATTY|HARDEN|HERBERT|BLAND|RUCKER|MANLEY|ZIEGLER|GRADY|LOTT|ROUSE|GLEASON|MCCLELLAN|ABRAMS|VO|ALBRIGHT|MEIER|DUNBAR|ACKERMAN|PADGETT|MAYES|TIPTON|COFFMAN|PERALTA|SHAPIRO|ROE|WESTON|PLUMMER|HELTON|STERN|FRASER|STOVER|FISH|SCHUMACHER|BACA|CURRAN|VINSON|VERA|CLIFTON|ERVIN|ELDRIDGE|LOWRY|CHILDRESS|BECERRA|GORE|SEYMOUR|CHU|FIELD|AKERS|CARRASCO|BINGHAM|STERLING|GREENWOOD|LESLIE|GROVES|MANUEL|SWAIN|EDMONDS|MUNIZ|THOMSON|CROUCH|WALDEN|SMART|TOMLINSON|ALFARO|QUICK|GOLDMAN|MCELROY|YARBROUGH|FUNK|HONG|PORTILLO|LUND|NGO|ELKINS|STROUD|MEREDITH|BATTLE|MCCAULEY|ZAPATA|BLOOM|GEE|GIVENS|CARDONA|SCHAFER|ROBISON|GUNTER|GRIGGS|TOVAR|TEAGUE|SWIFT|BOWDEN|SCHULZ|BLANTON|BUCKNER|WHALEN|PRITCHARD|PIERRE|KANG|BUTTS|METCALF|KURTZ|SANDERSON|TOMPKINS|INMAN|CROWDER|DICKEY|HUTCHISON|CONKLIN|HOSKINS|HOLBROOK|HORNER|NEELY|TATUM|HOLLINGSWORTH|DRAPER|CLEMENT|LORD|REECE|FELDMAN|KAY|HAGEN|CREWS|BOWLES|POST|JEWELL|DALEY|CORDERO|MCKINLEY|VELASCO|MASTERS|DRISCOLL|BURRELL|VALLE|CROW|DEVINE|LARKIN|CHAPPELL|POLLOCK|KIMBALL|LY|SCHMITZ|LU|RUBIN|BARRIOS|PEREIRA|PHIPPS|MCMANUS|NANCE|STEINER|POE|CROCKETT|JEFFRIES|AMOS|NIX|NEWSOME|DOOLEY|PAYTON|ROSEN|SWENSON|CONNELLY|TOLBERT|SEGURA|ESPOSITO|COKER|BIGGS|HINKLE|THURMAN|DREW|IVEY|BULLARD|BAEZ|NEFF|MAHER|STRATTON|EGAN|DUBOIS|GALLARDO|BLUE|RAINEY|YEAGER|SAUCEDO|FERREIRA|SPRAGUE|LACY|HURTADO|HEARD|CONNELL|STAHL|ALDRIDGE|AMAYA|FORREST|ERWIN|GUNN|SWAN|BUTCHER|ROSADO|GODWIN|HAND|GABRIEL|OTTO|WHALEY|LUDWIG|CLIFFORD|GROVE|BEAVER|SILVER|DANG|HAMMER|DICK|BOSWELL|MEAD|COLVIN|OLEARY|MILLIGAN|GOINS|AMES|DODGE|KAUR|ESCOBEDO|ARREDONDO|GEIGER|WINKLER|DUNHAM|TEMPLE|BABCOCK|BILLINGS|GRIMM|LILLY|WESLEY|MCGHEE|PAINTER|SIEGEL|BOWER|PURCELL|BLOCK|AGUILERA|NORWOOD|SHERIDAN|CARTWRIGHT|COATES|DAVISON|REGAN|RAMEY|KOENIG|KRAFT|BUNCH|ENGEL|TAN|WINN|STEWARD|LINK|VICKERS|BRAGG|PIPER|HUGGINS|MICHEL|HEALY|JACOB|MCDONOUGH|WOLFF|COLBERT|ZEPEDA|HOANG|DUGAN|KILGORE|MEADE|GUILLEN|DO|HINOJOSA|GOODE|ARRINGTON|GARY|SNELL|WILLARD|RENTERIA|CHACON|GALLO|HANKINS|MONTANO|BROWNE|PEACOCK|OHARA|CORNELL|SHERWOOD|CASTELLANOS|THORPE|STILES|SADLER|LATHAM|REDMOND|GREENBERG|COTE|WADDELL|DUKES|DIAMOND|BUI|MADRID|ALONSO|SHEETS|IRVIN|HURT|FERRIS|SEWELL|CARLTON|ARAGON|BLACKMON|HADLEY|HOYT|MCGRAW|PAGAN|LAND|TIDWELL|LOVELL|MINER|DOSS|DAHL|DELATORRE|STANFORD|KAUFFMAN|VELA|GAGNON|WINSTON|GOMES|THACKER|CORONADO|ASH|JARRETT|HAGER|SAMUELS|METZGER|RAINES|SPIVEY|MAURER|HAN|VOSS|HENLEY|CABALLERO|CARUSO|COULTER|NORTH|FINN|CAHILL|LANIER|SOUZA|MCWILLIAMS|DEAL|SCHAFFER|URBAN|HOUSER|CUMMINS|ROMO|CROCKER|BASSETT|KRUSE|BOLDEN|YBARRA|METZ|ROOT|MCMULLEN|CRUMP|HAGAN|GUIDRY|BRANTLEY|KEARNEY|BEAL|TOTH|JORGENSEN|TIMMONS|TIMOTHY|MILTON|TRIPP|HURD|SAPP|WHITMAN|MESSER|BURGOS|MAJOR|WESTBROOK|CASTLE|SERNA|CARLISLE|VARELA|CULLEN|WILHELM|BERGERON|BURGER|POSEY|BARNHART|HACKETT|MADRIGAL|EUBANKS|SIZEMORE|HILLIARD|HARGROVE|BOUCHER|THOMASON|MELVIN|ROPER|BARNARD|FONSECA|PEDERSEN|QUIROZ|WASHBURN|HOLLIDAY|YEE|RUDOLPH|BERMUDEZ|COYLE|GIL|GOODRICH|PINA|ELIAS|LOCKWOOD|CABRAL|CARRANZA|DUVALL|CORNELIUS|MCCOLLUM|STREET|MCNEAL|CONNORS|ANGEL|PAULSON|HINSON|KEENAN|SHELDON|FARR|EDDY|SAMUEL|LEDBETTER|RING|BETTS|FONTENOT|GIFFORD|HANNAH|HANLEY|PERSON|FOUNTAIN|LEVIN|STUBBS|HIGHTOWER|MURDOCK|KOEHLER|MA|ENGLE|SMILEY|CARMICHAEL|SHEFFIELD|LANGSTON|MCCRACKEN|YOST|TROTTER|STORY|STARKS|LUJAN|BLOUNT|CODY|RUSHING|BENOIT|HERNDON|JACOBSEN|NIETO|WISEMAN|LAYTON|EPPS|SHIPLEY|LEYVA|REEDER|BRAND|ROLAND|FITCH|RICO|NAPIER|CRONIN|MCQUEEN|PAREDES|TRENT|CHRISTIANSEN|PETTIT|SPANGLER|LANGFORD|BENAVIDES|PENN|PAIGE|WEIR|DIETZ|PRATER|BREWSTER|LOUIS|DIEHL|PACK|SPAULDING|AVILES|ERNST|NOWAK|OLVERA|ROCK|MANSFIELD|AQUINO|OGDEN|STACY|RIZZO|SYLVESTER|GILLIS|SANDS|MACHADO|LOVETT|DUONG|HYATT|LANDIS|PLATT|BUSTAMANTE|HEDRICK|PRITCHETT|GASTON|DOBSON|CAUDILL|TACKETT|BATEMAN|LANDERS|CARMONA|GIPSON|URIBE|MCNEILL|LEDFORD|MIMS|ABEL|GOLD|SMALLWOOD|THORNE|MCHUGH|DICKENS|LEUNG|TOBIN|KOWALSKI|MEDEIROS|COPE|KRAUS|QUEZADA|OVERTON|MONTALVO|STALEY|WOODY|HATHAWAY|OSORIO|LAIRD|DOBBS|CAPPS|PUTNAM|LAY|FRANCISCO|ADAIR|BERNSTEIN|HUTTON|BURKETT|RHOADES|RICHEY|YANEZ|BLEDSOE|MCCAIN|BEYER|CATES|ROCHE|SPICER|QUEEN|DOTY|DARLING|DARBY|SUMNER|KINCAID|HAY|GROSSMAN|LACEY|WILKES|HUMPHRIES|PAZ|DARNELL|KEYS|KYLE|LACKEY|VOGT|LOCKLEAR|KISER|PRESLEY|BRYSON|BERGMAN|PEOPLES|FAIR|MCCLENDON|CORLEY|PRADO|CHRISTIE|DELONG|SKAGGS|DILL|SHEARER|JUDD|STAPLETON|FLAHERTY|CASILLAS|PINTO|HAYWOOD|YOUNGBLOOD|TONEY|RICKS|GRANADOS|CRUM|TRIPLETT|SORIANO|WAITE|HOFF|ANAYA|CRENSHAW|JUNG|CANALES|CAGLE|DENNY|MARCUS|BERMAN|MUNSON|OCAMPO|BAUMAN|CORCORAN|KEEN|ZIMMER|FRIEND|ORNELAS|VARNER|PELLETIER|VERNON|BLUM|ALBRECHT|CULVER|SCHUSTER|CUELLAR|MCCORD|SHULTZ|MCRAE|MORELAND|CALVERT|WILLIAM|WHITTINGTON|ECKERT|KEENE|MOHR|HANKS|KIMBLE|CAVANAUGH|CROWELL|RUSS|FELICIANO|CRAIN|BUSCH|MCCORMACK|DRUMMOND|OMALLEY|ALDRICH|LUKE|GRECO|MOTT|OAKES|MALLORY|MCLAIN|BURROWS|OTERO|ALLRED|EASON|FINNEY|WELLER|WALDRON|CHAMPION|JEFFERS|COON|ROSENTHAL|HUDDLESTON|SOLANO|HIRSCH|AKINS|OLIVARES|SONG|SNEED|BENEDICT|BAIN|OKEEFE|HIDALGO|MATOS|STALLINGS|PARIS|GAMEZ|KENNY|QUIGLEY|MARRERO|FAGAN|DUTTON|ATWOOD|PAPPAS|BAGLEY|MCGOVERN|LUNSFORD|MOSELEY|READ|OAKLEY|ASHBY|GRANGER|SHAVER|HOPE|COE|BURROUGHS|HELM|AMBROSE|NEUMANN|MICHAELS|PRESCOTT|LIGHT|DUMAS|FLOOD|STRINGER|CURRIE|COMER|FONG|WHITLOCK|LEMUS|HAWLEY|ULRICH|STAPLES|BOYKIN|KNUTSON|GROVER|HOBSON|CORMIER|DORAN|THAYER|WOODSON|WHITT|HOOKER|KOHLER|ADDISON|VANDYKE|SCHRADER|HASKINS|WHITTAKER|MADSEN|GAUTHIER|BURNETTE|KEATING|PURVIS|ALEMAN|HUSTON|HAMLIN|PIMENTEL|GERBER|HOOKS|SCHWAB|HONEYCUTT|SCHULTE|ALONZO|ISAAC|CONROY|ADLER|EASTMAN|COTTRELL|OROURKE|HAWK|GOLDSMITH|CRANDALL|RADER|REYNOSO|SHOOK|ABERNATHY|BAER|OLIVAS|GRAYSON|BARTLEY|HENNING|PARR|DUFF|BRUNSON|BAUM|ENNIS|LAUGHLIN|FOOTE|VALADEZ|ADAMSON|BEGAY|STOVALL|LINCOLN|CHEUNG|MALLOY|RIDER|GIORDANO|JANSEN|LOPES|ARNETT|PENDLETON|GAGE|BARRAGAN|KEYES|NAVARRETE|AMADOR|HOFFMANN|HAWTHORNE|SCHILLING|PERDUE|SCHREIBER|AREVALO|NAYLOR|DELUCA|MARCUM|ALTMAN|MARK|CHADWICK|DOAN|EASLEY|LADD|WOODALL|BETANCOURT|SHIN|MAGUIRE|BELLAMY|QUINTANILLA|HAM|SORENSON|MATTSON|BRENNER|MEANS|FAUST|CALLOWAY|OJEDA|MCNALLY|DIETRICH|RANSOM|HARE|FELTON|WHITING|BURKHART|CLINTON|SCHWARZ|CLEARY|WETZEL|REAGAN|STJOHN|CHOW|HAUSER|DUPREE|BRANNON|LYLES|PRATHER|WILLOUGHBY|SEPULVEDA|NUGENT|PICKENS|JOINER|MOSHER|STONER|DOWLING|TRIMBLE|VALDES|CHEEK|SCRUGGS|COY|TILLEY|BARNEY|SAYLOR|NAGY|HORVATH|LAI|COREY|RUTH|SAUER|BARON|THAO|ROWELL|GRUBBS|HILLMAN|SCHAEFFER|SAMS|HOGUE|HUTSON|BUSBY|NICKERSON|BRUNER|PARHAM|ANDERS|RENDON|LOMBARDO|IVERSON|KINSEY|EARL|BORDEN|JEAN|TITUS|TELLEZ|BEAVERS|CORNETT|SOTELO|KELLOGG|BURNHAM|MCNAIR|SILVERMAN|JERNIGAN|ESCAMILLA|BARROW|COATS|LONDON|REDDING|RUFFIN|YI|BOUDREAUX|GOODSON|DOWELL|FENTON|MOCK|DOZIER|BYNUM|GALE|JOLLY|BECKMAN|GODDARD|CRAVEN|WHITMORE|LEARY|MCCLOUD|GAMBOA|KERNS|BRUNNER|HOUGH|NEGRON|CUTLER|LEDESMA|PYLE|MONAHAN|TABOR|BURK|LEONE|STAUFFER|HAYWARD|DRIVER|RUFF|TALBOT|SEALS|BOSTON|CARBAJAL|FAY|PURDY|MCGREGOR|SUN|ORELLANA|GENTILE|MAHAN|BROWER|PATINO|THURSTON|SHIPMAN|AARON|TORREZ|CALL|WEINER|WILBURN|OLIVA|HAIRSTON|COLEY|HUMMEL|ARREOLA|WATT|SHARMA|LENTZ|ARCE|POWER|LONGORIA|WAGONER|BURR|HSU|TINSLEY|BEEBE|WRAY|NUNN|PRIETO|GERMAN|ROWLEY|BRITO|GRUBB|ROYAL|VALENTIN|BARTHOLOMEW|SCHULER|ARANDA|FLINT|HEARN|VENEGAS|UNGER|MATTINGLY|BOLES|BARGER|CASAS|JULIAN|DOW|DOBBINS|VANN|CHESTER|STRANGE|LEMON|KAHN|MCKINNON|GANNON|WAGGONER|CONN|MEEK|CAVAZOS|SKELTON|LO|KUMAR|TOLEDO|LORENZ|VALLEJO|STARKEY|KITCHEN|REAVES|DEMARCO|FARRAR|STEARNS|MICHAUD|HIGGINBOTHAM|FERNANDES|ISAACS|MARION|GUILLORY|PRIEST|MEEHAN|OLIVEIRA|PALMA|OSWALD|GALVEZ|LOOMIS|LIND|MENA|STCLAIR|HINDS|REARDON|ALLEY|BARTH|CROOK|BLISS|NAGEL|BANUELOS|PARISH|HARMAN|DOUGLASS|KEARNS|NEWCOMB|MULLIGAN|COUGHLIN|WAY|FOURNIER|LAWLER|KAMINSKI|BARBOUR|SOUSA|STUMP|ALANIZ|IRELAND|RUDD|CARNES|LUNDY|GODINEZ|PULIDO|DENNISON|BAUMANN|BURDICK|DOVE|STODDARD|LIANG|DENT|ROARK|BOWSER|MCMAHAN|PARNELL|MAYBERRY|WAKEFIELD|ARNDT|OGLE|WORTHINGTON|DURBIN|ESCALANTE|PEDERSON|WELDON|VICK|KNOTT|RYDER|ZARATE|IRVING|CLEMENS|SHELLEY|SALTER|JACK|DASILVA|MUHAMMAD|SQUIRES|RAPP|DAWKINS|POLANCO|CHATMAN|MAIER|YAZZIE|GRUBER|STATON|BLACKMAN|MCDONNELL|DYKES|LAWS|WHITTEN|PFEIFFER|VIDAL|EARLY|KELSEY|BAUGHMAN|DIAS|STARNES|CRESPO|KILPATRICK|LOMBARDI|DEATON|SATTERFIELD|WILES|WEINSTEIN|ROWAN|DELOSSANTOS|HAMBY|ESTEP|DAIGLE|ELAM|CREECH|CHAVIS|HECK|ECHOLS|FOSS|TRAHAN|STRAUSS|VANHORN|WINSLOW|REA|FAIRCHILD|HEATON|MINTON|HITCHCOCK|LINTON|HANDY|CROUSE|COLES|FOY|UPTON|HERRINGTON|HWANG|MCCLELLAND|RECTOR|LUTHER|KRUGER|SALCEDO|CHANCE|GUNDERSON|THARP|GRIFFITHS|GRAF|BRANHAM|HUMPHREYS|RENNER|LIMA|ROONEY|MOYA|ALMEIDA|GAVIN|COBURN|OUELLETTE|GOETZ|SEAY|PARROTT|HARMS|ROBB|STOREY|BARBOSA|BARRAZA|LOYD|MERCHANT|DONOHUE|CARRIER|DIGGS|CHASTAIN|SHERRILL|WHIPPLE|BRASWELL|WEATHERS|LINDER|CHAPA|BOCK|OH|LOVELACE|SAAVEDRA|FERRARA|CALLAWAY|SALMON|TEMPLETON|CHRISTY|HARP|DOWD|FORRESTER|LAWTON|EPSTEIN|GANT|TIERNEY|SEAMAN|CORRAL|DOWDY|ZARAGOZA|MORRISSEY|ELLER|CHAU|BREEN|HIGH|NEWBERRY|BEAM|YANCEY|JARRELL|CERDA|ELLSWORTH|LOFTON|THIBODEAUX|POOL|RINEHART|ARTEAGA|MARLOW|HACKER|WILL|MACKENZIE|HOOK|GILLILAND|EMMONS|PICKERING|MEDLEY|ANDREW|WILLEY|SHELL|RANDLE|BRINKLEY|PRUETT|TOBIAS|EDMONDSON|GRIER|ASKEW|BATISTA|SALDIVAR|MOELLER|AUGUSTINE|CHAVARRIA|TROYER|LAYNE|MCNULTY|SHANK|DESAI|HERRMANN|HEMPHILL|BEARDEN|SPEAR|KEENER|HOLGUIN|CULP|BRADEN|BRISCOE|BALES|GARVIN|STOCKTON|ABREU|SUGGS|MCCARTNEY|FERRER|RHOADS|HA|NEVAREZ|SINGLETARY|CHONG|ALCALA|CHENEY|WESTFALL|DAMICO|SNODGRASS|DEVRIES|LOONEY|HEIN|LYLE|LOCKETT|JACQUES|BARKLEY|WAHL|APONTE|MYRICK|BOLIN|HOLM|SLACK|MARTINO|SCHERER|BACHMAN|ELY|NESBITT|MARROQUIN|BOUCHARD|MAST|JAMESON|HILLS|MIRELES|BUENO|PEASE|VITALE|ALARCON|LINARES|SCHELL|LIPSCOMB|ARRIAGA|BOURGEOIS|BONDS|MARKHAM|IVY|WISNIEWSKI|OLDHAM|FALLON|WENDT|JOY|STAMPER|BABB|STEINBERG|ASHER|FUCHS|BLANK|WILLETT|HEREDIA|CROFT|LYTLE|LASSITER|BARRIENTOS|CONDON|BARFIELD|DARDEN|ARAUJO|GUINN|NOONAN|BURLESON|BELANGER|MAIN|TRAYLOR|MESSINA|ZEIGLER|DANIELSON|MILLARD|KENYON|RADFORD|GRAFF|BEATY|BAGGETT|CRISP|SALISBURY|TROUT|LORENZO|PARSON|GANN|GARBER|ADCOCK|COVARRUBIAS|SCALES|ACUNA|THRASHER|CARD|VAN|MABRY|MOHAMED|MONTANEZ|REDD|STOCK|WILLINGHAM|REDMAN|ZAMBRANO|GAFFNEY|HERR|DEVLIN|PRINGLE|SCHUBERT|CASPER|HOUCK|REES|WING|EBERT|JETER|CORNEJO|GILLETTE|SHOCKLEY|AMATO|GIRARD|LEGGETT|CHEATHAM|BUSTOS|EPPERSON|DUBOSE|SEITZ|EAST|FRIAS|SCHOFIELD|STEEN|ORLANDO|MYLES|CARON|GREY|DENNEY|ONTIVEROS|BURDEN|JAEGER|REICH|WITHERSPOON|NAJERA|FRANTZ|HAMMONDS|XU|LEAVITT|GILCHRIST|ADAM|BARONE|FORMAN|CEJA|RAGSDALE|SISK|TUBBS|ELIZONDO|PRESSLEY|BOLLINGER|LINN|HUNTLEY|DEWEY|GEARY|CARLOS|RAGLAND|MIXON|BAUGH|MCARTHUR|TAM|NOBLES|CLEVENGER|FOUST|LUSK|COONEY|TAMAYO|ROBERT|LONGO|OVERSTREET|OGLESBY|MACE|CHURCHILL|MATSON|HAMRICK|ROCKWELL|TRAMMELL|WHEATLEY|CARRINGTON|FERRARO|RALSTON|CLANCY|MONDRAGON|CARL|HU|HOPSON|BREAUX|MCCURDY|MARES|CHISHOLM|MAI|MATLOCK|AIKEN|CARY|LEMONS|ANGUIANO|HERRICK|CRAWLEY|MONTERO|HASSAN|ARCHULETA|COTTER|FARIAS|PARRIS|FELDER|LUU|PENCE|GILMAN|KILLIAN|NARANJO|DUGGAN|EASTER|SCARBOROUGH|SWANN|RICKETTS|FRANCE|BELLO|NADEAU|STILL|RINCON|CORNWELL|SLADE|FIERRO|MIZE|CHRISTIANSON|GREENFIELD|MCAFEE|LANDRUM|ADAME|DINH|LANKFORD|LEWANDOWSKI|RUST|BUNDY|WATERMAN|MILNER|MCCRARY|HITE|CURLEY|DONALD|DUCKWORTH|CECIL|CARRERA|SPEER|BIRCH|DENSON|BECKWITH|STACK|DURANT|DORMAN|LANTZ|CHRISTMAN|SPANN|MASTERSON|HOSTETLER|KOLB|BRINK|SCANLON|NYE|BEVERLY|WYLIE|WOO|SPURLOCK|SHELBY|SOMMER|REINHARDT|ROBLEDO|ASHTON|BERTRAND|CYR|EDGAR|DOE|HARKINS|BRUBAKER|STOLL|DANGELO|ZHOU|MOULTON|HANNON|FALK|RAINS|BROUGHTON|APPLEGATE|HUDGINS|SLONE|FARNSWORTH|YOON|PERALES|REEDY|MILAM|FRANZ|PONDER|RICCI|FONTAINE|IRIZARRY|NEW|PUENTE|SELBY|CAZARES|DOUGHTY|MOFFETT|BALDERAS|FINE|SMALLEY|CARLIN|TRINH|DYSON|GALVIN|VALDIVIA|BENNER|TURPIN|LYMAN|BILLINGSLEY|JIM|MCADAMS|CARDWELL|FRALEY|PATTEN|HOLTON|SHANKS|MCALISTER|CANFIELD|SAMPLE|HARLEY|CASON|TOMLIN|AHMAD|COYNE|FORTE|RIGGINS|LITTLEJOHN|FORSYTHE|BRINSON|HALVERSON|BACH|STUCKEY|FALCON|TALBERT|WENZEL|CHAMPAGNE|MCHENRY|VEST|SHACKELFORD|ORDONEZ|COLLAZO|BOLAND|SISSON|BIGELOW|HYMAN|WHARTON|BRUMFIELD|OATES|MESA|BECKETT|MORRELL|REIS|ALVES|CHIU|LARUE|STREETER|GROGAN|BLAKELY|BROTHERS|HATTON|KIMBROUGH|LAUER|WALLIS|JETT|PEPPER|HILDEBRAND|RAWLS|MELLO|NEVILLE|BULL|STEFFEN|BRAXTON|COWART|SIMPKINS|MCNEELY|BLALOCK|SPAIN|SHIPP|LINDQUIST|BUTTERFIELD|OREILLY|PERRIN|QUALLS|HAVENS|LUONG|SWITZER|TROUTMAN|FORTNER|TOLLIVER|MONK|POINDEXTER|RUPP|FERRY|NEGRETE|MUSE|GRESHAM|BEAUCHAMP|BARCLAY|SCHMID|CHUN|BRICE|FAULK|WATTERS|BRIONES|GUAJARDO|HARWOOD|GRISSOM|HARLOW|WHELAN|BURDETTE|PALUMBO|PAULSEN|CORRIGAN|GARVEY|LEVESQUE|DOCKERY|DELGADILLO|GOOCH|CAO|MULLIN|RIDLEY|STANFIELD|NORIEGA|CEBALLOS|NUNES|NEWBY|BAUMGARTNER|HUSSAIN|WYMAN|CAUSEY|GOSSETT|NESS|WAUGH|CHOATE|CARMAN|DAILY|DEVORE|IRBY|KONG|BREEDEN|WHATLEY|ELLINGTON|LAMAR|FULTZ|BAIR|ZIELINSKI|COLBY|HOUGHTON|GRIGSBY|FORTUNE|PAXTON|MCMILLIAN|HAMMONS|BRONSON|KECK|WELLMAN|AYRES|WHITESIDE|MENARD|ROUSH|WARDEN|ESPINO|STRAND|HAGGERTY|BANDA|FABIAN|KREBS|BOWIE|BRANSON|LENZ|BENAVIDEZ|KEELER|NEWSOM|EZELL|JEFFREY|PULLIAM|CLARY|BYRNES|GARDINER|SOMMERS|FENNELL|MANCINI|OSULLIVAN|SEBASTIAN|BRUNS|GIRON|BOYLES|KEEFE|MUIR|SHULER|VERGARA|PEMBERTON|BROWNLEE|BROCKMAN|FANNING|ROYER|HERZOG|MORLEY|BETHEA|NEEDHAM|ROQUE|MOJICA|FRANCOIS|KUNTZ|SNOWDEN|WITHERS|HARLAN|SEIBERT|LIMON|KIEFER|ALLAN|SKIDMORE|DUNAWAY|FINNEGAN|WOLFORD|SEELEY"


def name_extractor(text,terms,email_id,file_type):
    try:
        temp_terms = []
        for i in range(len(terms)):
            if not re.search(name_not,terms[i].lower()):
                temp_terms.append(terms[i])
        q =0

        terms = temp_terms

        name_text =""
        linkedin_name_text ="" 
        text_linkedinname= ""
        if name_text == "":
            linkedin_name_text  = linkedin_name(text)
            text_linkedinname = re.sub("\s|\d","",linkedin_name_text)
            text_linkedinname = text_linkedinname[:3]
            
        if name_text == "":
            name_text = first_line_extract(text,terms)
            q  =0
            print(name_text)
            if  not text_linkedinname.lower() in name_text.lower() and text_linkedinname != "":
                name_text = ""
                q  =1 

        if name_text == "":
            name_text = us_name_check(terms)
            q  =0
            print(name_text)
            if  not text_linkedinname.lower() in name_text.lower() and text_linkedinname != "":
                name_text = ""
                q = 1
        if name_text == "":
            name_text = indian_name_check(terms)

        if name_text == "":
            name_text = email_id_check(terms,email_id)

        if name_text =="":
            for i in range(len(terms)):
                if re.search("[A-Z]",terms[i]):
                    name_text= terms[i]

        if q ==1  and linkedin_name_text != "":
            name_text =linkedin_name_text.upper()

        if len(name_text.split())== 1:
            name_text = get_second_name(name_text,terms)

        # remove the digits

        name_split = name_text.split()
        temp_name = ""
        for i in range(len(name_split)):
            if not re.search("\d",name_split[i]) :
                temp_name  = temp_name + " " + name_split[i]

        name_text= temp_name
        name_text =re.sub("Name|NAME|CELL|Cell|Phone|PHONE","",name_text)

        return name_text
    except:
        return ""
    

def us_name_check(terms):
    name_text =""
    
    for i in range(len(terms)):
        if  len(terms[i].split())<5 or (len(terms[i].split())<8 and len(terms[i])<25):
            if re.search("[A-Z]",terms[i]) and not re.search(name_not,terms[i].lower()):
                if re.search(US_human_names,terms[i].upper()) :
                    
                    if len(re.search(US_human_names,terms[i].upper())[0])>3:
                        name_text = terms[i]
                        break


    return name_text 


def indian_name_check(terms):
    name_text = ""
        
        
    for i in range(len(terms)):
        if re.search("personal",terms[i].lower()) and "P" in terms[i]:
            start = i
            break

    terms = terms[i:]
    
    for i in range(len(terms)):
        if re.search("name|n ame",terms[i].lower()) and not re.search("father|project|mother|company",terms[i].lower()) :
            name_text  = terms[i].lower()
            name_text = re.sub("name|n ame",name_text)
            name_text = re.sub("\.|:|="," ",name_text)

    return name_text

def email_id_check(terms,email_id):
    name_text = ""
    if re.search("@",email_id):
            username = email_id[:email_id.index("@")]
            # text = re.sub(":|\.|\-|\/"," ",text)
            res =[]
            temp_username = ""
            if len(username)>3:
                username = username.lower()
                temp_username = username
                username = re.sub("\s+","",username)
                username = username[:3]

                for i in range(len(terms)):
                    if re.search(username,terms[i].lower()) and len(terms[i].split())<5 and re.search("[A-Z]",terms[i]):
                        name_text= terms[i]
                        break
                username =temp_username

                if name_text =="" and len(username)>5:
                    username = re.sub("[^a-z]+","",temp_username)
                    username  = username[-4:]

                    for i in range(len(terms)):
                        if re.search(username,terms[i].lower()) and re.search("[A-Z]",terms[i]):
                            name_text = terms[i]
                            break

    return name_text


def get_second_name(name_text,terms):
    index = -1 
    temp_name_text = name_text
    for i in range(len(terms)):
        if re.search(name_text,terms[i]):
            index = i
    if index != -1 :
        try:
            if terms[index+1][0].isupper() and len(terms[index+1].split())<3:
                name_text = name_text + " "+ terms[index+1]
        except:
            name_text = temp_name_text
        try:
            if terms[index-1][0].isupper() and len(terms[index-1].split())<3 and len(name_text)<3:
                name_text =  terms[index-1] + " "+name_text
        except:
            name_text =temp_name_text


    return name_text

def first_line_extract(text,terms):

    res  =  text.split("\n")
    res = res[:min(5,len(res))]
    name_text =""
    text_term =""
    # result = text.index('\n')

    # text_term = text[:result]
    i =0
    while len(res[i])<3 or len(res[i].split())>5 or re.search(name_not,res[i].lower()) :
        i +=1 
        if i == len(res)-1:
            break

    print(res[i])
    text_term =res[i]
    text_term = re.sub("\n|\.|\-|\+|,|(|)|\d"," ",text_term)
    name_terms = text_term.split()
   
    for i in range(len(name_terms)):
        if re.search(name_not,name_terms[i].lower()):
            name_text =""
            break
        if name_terms[i][0].isupper() and len(name_terms[i])>3:
            name_text  = name_text +" "+name_terms[i]

    return name_text

def linkedin_name(text):
    res = text.split()
    name_text = ""
    start = -1
    for i in range(len(res)):
        if re.search("linkedin.com",res[i].lower()):
            print(res[i])
            name_text = re.sub("www|\.","",res[i])
            name_text = re.sub("linkedincom/in/","",name_text)
            name_text = re.sub("\-"," ",name_text)
            name_text = name_text.upper()
            break
    return name_text
