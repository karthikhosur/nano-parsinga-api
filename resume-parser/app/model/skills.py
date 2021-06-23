import re
import os 


skills_re = [ "  \.net "  , " \.net compact framework "  , "  \.net framework "  , " \.net micro framework "  , " .net remoting "  , " \.test "  , " µ processor "  , " µclinux "  , " 2d animation "  , " 3d equalizer "  , " 3d graphics "  , " 3ds max studio "  , " 3g "  , " 3gp "  , " 3gpp "  , " 5axcore "  , " 802protocols "  , " 89c51 microcontrollers "  , " 8d "  , " a/rose "  , " a7 "  , " abaqus "  , " abend-aid "  , " ab-slc500 "  , " accountancy "  , " ac-dc drivers "  , " acp "  , " action script "  , " active desktop "  , " active directory "  , " activemovie "  , " activex "  , " actuate "  , " ada "  , " adabas "  , " adams "  , " adatest 95 "  , " adexa "  , " ado\.net "  , " adobe acrobat "  , " adobe flash "  , " adobe golive "  , " adobe photoshop "  , " adobe premier "  , " adso "  , " adsp "  , " advanced java "  , " aero engine design "  , " aero structure design "  , " afopera "  , " afp "  , " after effects "  , " agp "  , " airo peek "  , " aix administrator "  , " alef "  , " algol "  , " algol 60 "  , " algol 68 "  , " algol w "  , " alias "  , " alias studiotools "  , " alibre design "  , " alice "  , " allegro "  , " alphacam "  , " alphamosaic "  , " amd64 "  , " analysis "  , " anatomy "  , " animating "  , " antenna design "  , " anysys "  , " apache derby "  , " api "  , " apl "  , " applescript "  , " apptest "  , " apqp "  , " aqtest "  , " architectural desktop "  , " arcnet "  , " argon "  , " arm "  , " arp "  , " as 400 "  , " as 9100 "  , " as9100 qms "  , " ascential datastage "  , " asic/fpga "  , " asn\.1 "  , " asp "  , " asp\.net "  , " zeke "  , " assembler "  , " z format "  , " xsltunit "  , " ata/atapi "  , " atheros "  , " atlas autocode "  , " xsl "  , " atmel "  , " atmel 8051 "  , " xns "  , " audio streaming "  , " xmlunit "  , " xml "  , " xmk "  , " audio video "  , " xilleon-226 "  , " aunit "  , " xilinx ise "  , " authenticode "  , " xilinx "  , " auto desk "  , " xhtml basic "  , " autocad "  , " xhtml "  , " autocue "  , " xenon "  , " xenomai "  , " autodesk inventor "  , " xaml "  , " autolisp "  , " x10 "  , " avaya acd "  , " x\.25 "  , " avi "  , " wtvml "  , " wrap "  , " awk "  , " world soft "  , " awt "  , " worknc "  , " b\.lu bos "  , " backoffice "  , " work bench "  , " bacnet "  , " wordprocessingml "  , " bash "  , " basic "  , " wordperfect "  , " wmv "  , " basic systems "  , " wmqi "  , " basic09 "  , " wml "  , " bcpl "  , " wlan "  , " berkeley db "  , " wlam "  , " winrunner "  , " beta "  , " bgp "  , " bi tools "  , " bigwig "  , " bikecad "  , " bi-sas "  , " bittorrent "  , " biztalk server "  , " bluetooth "  , " board design "  , " bobcadcam "  , " bootp "  , " borland c "  , " borland c++ "  , " boujou "  , " bounds checker "  , " bpo services "  , " brew "  , " brio "  , " broadband technologies "  , " bs 7799 "  , " bsd unix "  , " bsp "  , " buildprofessional "  , " burroghs extended algol "  , " business intelligence "  , " business objects "  , " c "  , " c-- "  , " c# "  , " c++ "  , " c++test "  , " c55x "  , " ca-1 "  , " ca-11 "  , " ca7 "  , " cache "  , " cache basic "  , " cache objectscript "  , " cad "  , " cadd "  , " caddie "  , " cadds 5 "  , " cadds 5i "  , " cadence "  , " cadstar "  , " cae "  , " cal "  , " caliber "  , " calypso "  , " can2\.0b "  , " cantata "  , " cantata++ "  , " cap "  , " capros "  , " carbon "  , " catia "  , " catia v4 "  , " catia v5 "  , " catia-knowledgeware "  , " catos "  , " ccda "  , " ccna "  , " ccnp "  , " ccs "  , " ccsa "  , " ccse "  , " cdma "  , " cdp "  , " cgi "  , " changeman "  , " chariot "  , " chorusos "  , " c-html "  , " cifs "  , " cisa "  , " cisco ios "  , " cissp "  , " clarify "  , " clear case "  , " cloverleaf "  , " clp "  , " cls "  , " cmiip "  , " cml "  , " cmm "  , " cmms "  , " cms "  , " cobalt "  , " cobol "  , " cobol/400 "  , " cobol/cics "  , " cocoa "  , " code charge "  , " code composer "  , " code warrior "  , " codecs "  , " codefactory "  , " cognos "  , " coidng "  , " coldfusion "  , " com+ "  , " comal "  , " comit "  , " common lisp "  , " compiler "  , " component pascal "  , " compression "  , " compute "  , " concurrent euclid "  , " consulting "  , " context "  , " contiki "  , " control plans "  , " control-m "  , " cool 360 "  , " cool 3d "  , " cool:2e "  , " coolgen "  , " coral "  , " core java "  , " corel draw "  , " corel photopaint "  , " corel ventura "  , " corn "  , " cosmos "  , " coverage tools "  , " coyote "  , " wingdings "  , " coyotos "  , " cpl "  , " winfx "  , " cppunit "  , " winflp "  , " crossmark "  , " css "  , " windowsos "  , " csunit "  , " windows nt "  , " windows xp embedded "  , " cta++ "  , " windows xp "  , " ctb "  , " windows vista "  , " ctv middleware "  , " windows server 2003 "  , " cunit "  , " windows server "  , " cut "  , " windows powershell "  , " windows nt "  , " windows media "  , " windows me "  , " windows device drivers "  , " windows ce "  , " windows 98se "  , " windows 98 "  , " windows 95 "  , " windows 2000 server "  , " windows 2000 "  , " windows "  , " window driver "  , " windchill "  , " winbatch "  , " win64 "  , " win32 api "  , " win32 "  , " win2k servers "  , " win api "  , " win 2k sql dba "  , " wimax "  , " wildpackets "  , " wikipedia "  , " wi-fi "  , " websphere "  , " weblogic "  , " cygwin "  , " webdav "  , " d2k "  , " web technologies "  , " data formats "  , " web methods "  , " data mapping "  , " web logic "  , " data mining "  , " wds "  , " data modelling "  , " data stage "  , " data stream "  , " wcdma "  , " watfor "  , " data warehousing "  , " watfiv "  , " datacom "  , " watbol "  , " datastage "  , " wap "  , " db/400 "  , " wan unix "  , " db2 "  , " vxworks rtoss "  , " db4o "  , " vxworks "  , " dba "  , " vtune "  , " dbase "  , " dcap "  , " dcc "  , " dcom "  , " ddk "  , " ddp "  , " ddr ram "  , " ddr2 "  , " ddr3 "  , " ddts "  , " delphi "  , " designing "  , " desk tops "  , " device drivers "  , " dhcp "  , " dhtml "  , " diameter "  , " dibol "  , " dict "  , " digidebug "  , " digital fusion "  , " digital video broadcast "  , " direct show "  , " direct3d "  , " directanimation "  , " directdraw "  , " directinput "  , " directmusic "  , " directplay "  , " directshow "  , " directsound "  , " directx "  , " discreet "  , " dita "  , " dm207 "  , " dmalloc "  , " docbook "  , " dotunit "  , " doublespace "  , " dreamweaver "  , " drivespace "  , " dsa "  , " dsp "  , " dtv decorder "  , " dunit "  , " dvb "  , " dvd "  , " ead "  , " eam "  , " easycase "  , " easymock "  , " easytrieve "  , " e-carrier "  , " eclipse "  , " ecmascript "  , " econet "  , " ecos "  , " jboss "  , " edgecam "  , " egp "  , " eiffel "  , " ejb "  , " e-language "  , " electric fence "  , " emacs lisp "  , " embedded "  , " embedded firmware "  , " embedded linux "  , " embedded networking "  , " embos "  , " emi/emc "  , " ems "  , " encarta encyclopedia "  , " endeavour "  , " enps "  , " enriched text "  , " epm "  , " eprom "  , " eros "  , " essbase "  , " ether peck "  , " ethereal "  , " ethernet "  , " etl tools "  , " euclid "  , " euclid-is "  , " euphoria "  , " exapt "  , " exchange server "  , " expeditor "  , " fastcam "  , " fddi "  , " featurecam "  , " femap "  , " nss "  , " file system driver "  , " fileaid "  , " finger "  , " firebird "  , " fireworks "  , " firmware "  , " fix protocol "  , " flash "  , " flash drive "  , " flash paper "  , " flex and bison "  , " fluid effects "  , " fmea "  , " fmea/qfd "  , " focal "  , " formac "  , " fortran "  , " fortran 2003 "  , " fortran 77 "  , " fortran 90 "  , " fortran 95 "  , " fortran ii "  , " fortran iv "  , " foundry "  , " fpga "  , " frame relay "  , " framemaker "  , " freedos "  , " freertos "  , " frontpage "  , " ftp "  , " fts "  , " gcc "  , " gdb "  , " gdi "  , " gdi+ "  , " gdp "  , " gds "  , " ge-smallworld "  , " gif "  , " gis "  , " gjtester "  , " glee "  , " gml "  , " gmlc "  , " gniit "  , " gnu "  , " gnutella "  , " gopher "  , " gprof "  , " gprs "  , " grandtestauto "  , " graphite "  , " greenhill "  , " greenplum "  , " groovy "  , " gsm "  , " gui "  , " guideml "  , " guile "  , " gwos "  , " h\.323 "  , " h2 "  , " harddisk "  , " hardware "  , " hardware design "  , " harnessit "  , " haskell "  , " hawk "  , " hdlc "  , " hdml "  , " helios "  , " helix "  , " helpml "  , " hercules "  , " high end server technologies "  , " hitron "  , " hp open view "  , " hps hp-ux "  , " hp-ux "  , " html "  , " htmlunit "  , " http "  , " https "  , " httpunit "  , " hyperion "  , " hyperion dba "  , " hypermesh "  , " hypermill "  , " hypertalk "  , " hypertex "  , " hytime "  , " i2c protocol "  , " icmp "  , " icon "  , " i-deas "  , " ieee 802\.11 "  , " igmp "  , " iis "  , " illustrator "  , " imap "  , " ims "  , " ims db "  , " ims dc "  , " indesign "  , " inferno "  , " infineon "  , " informatica "  , " informix "  , " infrared "  , " ingres "  , " in-process qa "  , " install shield "  , " in-sysn "  , " intec "  , " intel "  , " intel 8085/86 "  , " intel 80x "  , " intel v tune "  , " intellimirror "  , " intellimouse "  , " interbase "  , " intuity audix "  , " ios-xr "  , " ipf "  , " ipsec "  , " ipv4 "  , " ipv6 "  , " irda "  , " is standards "  , " isdn "  , " isdn itu "  , " is-is "  , " iso 13485 "  , " iso 14001 "  , " iso 9000 "  , " iso 9001 "  , " iso 9001:2000 "  , " iso/ts16949 "  , " isodraw "  , " ispf "  , " j# "  , " j2ee "  , " j2me "  , " j98 "  , " jabber "  , " jai "  , " java "  , " java 1\.1 "  , " java 2\.0 "  , " java 3d "  , " java applets "  , " java beans "  , " java card "  , " java porting "  , " javaapplets "  , " javascript "  , " javascript assertion unit "  , " javascript osa "  , " javaspaces "  , " jcl "  , " jdbc "  , " jdmk "  , " jdo "  , " jfc "  , " jini "  , " jiro "  , " jmf "  , " jmi "  , " jml "  , " jmx "  , " jndi "  , " jni "  , " jogl "  , " join java "  , " joss "  , " joy "  , " jpeg "  , " jscript\.net "  , " jsf "  , " jsml "  , " jsp "  , " jsunit "  , " jta "  , " jtestcase "  , " junit "  , " junitee "  , " junitx "  , " junos "  , " just basic "  , " jxta "  , " kaizen "  , " kanban "  , " keil "  , " keil-89c51 "  , " kenan-bp "  , " keykos "  , " kgdb "  , " ksh "  , " ktiicad "  , " kti-icad "  , " kylix "  , " l2f "  , " l2tp "  , " labview "  , " labwindows "  , " lan "  , " lapd "  , " latex "  , " layer 7 "  , " ldap "  , " liberty basic "  , " lilypond "  , " limbo "  , " lingounit "  , " linkbuilder "  , " linter "  , " linux "  , " linux certification "  , " linux device drivers "  , " linux intervals "  , " linux kernal internals "  , " linux kernel programming "  , " linux server "  , " linuxdoc "  , " lisp "  , " lldp "  , " lldp-med "  , " loadrunner "  , " localtalk "  , " lotus "  , " lotus workflow "  , " lout "  , " lpc "  , " lua "  , " lunix "  , " lwjgl "  , " lynxos "  , " lynxos rtos "  , " mac "  , " mac os "  , " mac osx "  , " mac tools "  , " machineworks "  , " machining strategist "  , " macintosh "  , " macromedia director "  , " magma "  , " magna "  , " mail messaging "  , " mainframe servers "  , " maml "  , " manugistics "  , " map "  , " mapinfo "  , " mathml "  , " matlab "  , " matrixone "  , " maximo "  , " maya "  , " mc6800 "  , " mcnp "  , " mcp "  , " mcpl "  , " mcs-51 series "  , " mcsa "  , " mcse "  , " mechanical desktop "  , " mediaexpress "  , " mediation "  , " mediation tools amd/sas-comptel "  , " mediaware "  , " mediawiki "  , " medusa "  , " megaco "  , " mentor graphics "  , " menuetos "  , " mercury "  , " message notes exchange "  , " messaging nt "  , " metasolv "  , " metroethernet "  , " mfc "  , " mib "  , " micro cadam "  , " micro code "  , " microchip "  , " microcontrollers "  , " microcos "  , " micrologix "  , " micronas sda55xx "  , " microprocessors "  , " microsoft access "  , " microsoft certification "  , " microsoft exchange "  , " microsoft press "  , " microsoft quickbasic "  , " microsoft visual test "  , " microstation "  , " microstrategy "  , " mif "  , " mime "  , " mimer sql "  , " minix "  , " minunit "  , " mips "  , " miranda "  , " misra "  , " mitron "  , " mitsubishi-fx "  , " mks "  , " mmi "  , " mms "  , " mmsc "  , " mmx/sse/sse2 "  , " mobile app "  , " mobile platforms "  , " mobilinux "  , " mock creator "  , " mock objects "  , " mockmaker "  , " mockry "  , " modbus "  , " modeling "  , " modelsim "  , " modula-2 "  , " modula-3 "  , " moldflow "  , " monetdb "  , " monta vista linux "  , " motherboard "  , " mov "  , " mp lab "  , " mp3 "  , " mp4 "  , " mpc "  , " mpeg "  , " mpeg-2 "  , " mpeg4 "  , " mpls "  , " mq series "  , " mqsi "  , " ms excel "  , " ms groove "  , " ms infopath "  , " ms office "  , " ms outlook "  , " ms powerpoint "  , " ms projects "  , " ms publisher "  , " ms visio "  , " ms visio design "  , " ms word "  , " msc nastran "  , " msc patran "  , " msde "  , " msdn "  , " ms-dos "  , " ms-dos batch files "  , " msm "  , " msn "  , " ms-office "  , " msvc "  , " multiice "  , " multimedia "  , " multisurf "  , " multithreading "  , " mumps "  , " musicxml "  , " mvs "  , " mvs-consoles "  , " my sql "  , " mysap crm "  , " mysql "  , " n+ "  , " napa "  , " nastran "  , " natural "  , " nbap "  , " ncp "  , " ndt "  , " nesl "  , " netbsd "  , " netmeeting "  , " network lan "  , " network processors "  , " networking "  , " networking expertise "  , " newtonscript "  , " nfs "  , " nice server "  , " nig "  , " nms "  , " nntp "  , " nortel "  , " nortel pbx "  , " norti4 "  , " novell "  , " novell netware "  , " nrs "  , " ns-2 "  , " nsis "  , " ntegrity "  , " ntp "  , " nucleus "  , " null "  ," network ", " nunit "  , " nupas-cadmatic "  , " nx "  , " nx nastran "  , " oberon (oberon-1) "  , " oberon-2 "  , " objcunit "  , " ocaml "  , " occam "  , " ocean "  , " ocunit "  , " oes "  , " ofdm "  , " office open xml "  , " olap "  , " oltp "  , " oma "  , " omap "  , " omc flasher "  , " omcs "  , " omdoc "  , " omegamon "  , " omnicad "  , " one world xe "  , " onecnc "  , " onespace drafting 2007 "  , " onespace modeling "  , " onespace modeling 2007 "  , " ooad "  , " open gl "  , " openbsd "  , " opendocument "  , " opengl "  , " openlink virtuoso "  , " openmath "  , " openoffice\.org xml "  , " opentype "  , " openvg "  , " operating system embedded "  , " optical communication "  , " oracle "  , " oracle eam "  , " oracle 10g "  , " oracle 11i crm "  , " oracle 6 "  , " oracle adf "  , " oracle application express "  , " oracle applications 11\.x dba "  , " oracle apps dba "  , " oracle apps opm "  , " oracle apps otr "  , " oracle dba "  , " oracle eam "  , " oracle ebusiness suite "  , " oracle enterprise manager "  , " oracle express "  , " oracle express server "  , " oracle finance "  , " oracle hrms "  , " oracle jdeveloper "  , " oracle manufacturing "  , " oracle rdb "  , " oracle spatial "  , " oracle/forms 6i/reports 6 "  , " oracle8i "  , " oracle-forms 6i other domains "  , " orcad "  , " organic modeling "  , " os porting "  , " os20 "  , " os-9 "  , " osa "  , " oscilloscopes "  , " ose "  , " osek "  , " osekworks "  , " osgi "  , " ospf "  , " ospfv2 "  , " other domains "  , " outlook express "  , " pagemaker "  , " paging and swapping "  , " paintshop pro "  , " palmos "  , " palmunit "  , " panvalet "  , " paradox "  , " par-os "  , " particles "  , " pascal "  , " patran "  , " pbunit "  , " tomcat "  , " pc104 "  , " pci "  , " pci-express "  , " pcmm "  , " pcschematic elautomation "  , " pcschematic electronics "  , " pcschematic powerdistribution "  , " pcschematic tele "  , " pd30 emulator "  , " pdca "  , " pdca cycle "  , " pdh "  , " people soft crm "  , " people tools "  , " peps "  , " perfect "  , " performance optimization "  , " performance tuning "  , " performance tuning-java "  , " performance tuning-oracle "  , " performance tuning-sap "  , " performance tuning-siebel "  , " performance tuning-sql "  , " performance tuning-websphere "  , " performancetuning websphere "  , " perl "  , " perl test "  , " perlunit "  , " phoenix-rtos "  , " photo impact "  , " photoshop "  , " php "  , " phpasserunit "  , " phpunit "  , " pic18f452 "  , " vtp "  , " pico "  , " pike "  , " pix os "  , " vss "  , " pl/1 "  , " vsam "  , " pl/c "  , " vs cobol ii "  , " pl/i "  , " pl/m "  , " vrtx "  , " pl/m-86 "  , " vpls "  , " pl/sql "  , " plain old documentation "  , " voip "  , " plc "  , " plumtree "  , " voice logger "  , " png "  , " voice data convergence "  , " poka yoke "  , " vlsi "  , " pop3 "  , " vitira "  , " visual studio\.net "  , " posix "  , " visual studio "  , " visual foxpro "  , " postgresql "  , " visual fortran "  , " power builder "  , " power center "  , " visual dsp "  , " powercadd "  , " visual basic\.net "  , " visual basic "  , " powermill "  , " visi-series "  , " visionplus "  , " vision probe "  , " powerpc "  , " virtuoso "  , " powerpoint "  , " viper "  , " ppap "  , " vignette "  , " ppap submission "  , " video streaming "  , " ppc "  , " vhdl "  , " ppp "  , " pptp "  , " verilog "  , " verifault "  , " precision rtl "  , " vericut "  , " presentationml "  , " velosity "  , " printer domain "  , " vectorcast "  , " printer driver "  , " vc++/mfc "  , " printers "  , " vc++ "  , " vbunit3 basic "  , " prism "  , " vbscript "  , " prkernal "  , " vba "  , " prkernel v4 "  , " vb\.net "  , " pro*c "  , " valgrind "  , " uwb "  , " usp "  , " pro/concept "  , " pro/designer "  , " pro/desktop "  , " pro/engineer "  , " pro/mechanica "  , " process flow chart (pfc)\. "  , " process mapping "  , " processpoweroil and gas "  , " product design "  , " product lifecycle mgmt "  , " pro-e "  , " pro-e wildfire "  , " progress "  , " prolog "  , " promjet rom emulator "  , " ps - finance "  , " ps - hrms "  , " ps finance "  , " ps hrms "  , " psos "  , " psosystem "  , " pspice "  , " purify "  , " push to talk "  , " python "  , " pyunit "  , " q\.700-q\.709 "  , " q\.920 "  , " q\.921 "  , " q\.931 "  , " qbasic "  , " qmf "  , " qms "  , " qnx "  , " qos "  , " qs 9000 "  , " qtp "  , " qtunit "  , " quakec "  , " quality circles "  , " quality management systems "  , " quality systems - iso and ts "  , " quantify "  , " quartus "  , " quartz "  , " quickbasic "  , " quickjob "  , " radius "  , " ranap "  , " rarp "  , " ratfor "  , " rational robot "  , " rational rose "  , " rational test realtime unit testing "  , " real flow "  , " real view "  , " realbasic "  , " refal "  , " remedy "  , " reportml "  , " resource builder "  , " revolution "  , " rexx "  , " rf systems "  , " rhino "  , " rigging "  , " rip "  , " risk management "  , " rlogin "  , " rmi "  , " robohelp "  , " rom "  , " rom-dos "  , " rotoscopy "  , " routeros "  , " routing protocol "  , " rox "  , " rpc "  , " rpg/400 "  , " rs-232 "  , " rsvp "  , " rsync "  , " rtai "  , " rtems "  , " rtf "  , " rtke "  , " rtl "  , " rtlinux "  , " rtml "  , " rtos "  , " rtos osek "  , " rtospsos "  , " rtosqnx "  , " rtosvrtx "  , " rtosvxworks "  , " rtp "  , " rtp/rtcp "  , " rtsp "  , " rtxc "  , " ruby "  , " ruby test::unit "  , " ruby/mock "  , " rvds "  , " s1000d "  , " s2 "  , " s8710 server "  , " sales analyzer "  , " salvo "  , " san/nas admin "  , " sap abap "  , " sap abap/4 "  , " sap apo "  , " sap basis "  , " sap bc "  , " sap bw "  , " sap cfm "  , " sap co "  , " sap crm "  , " sap ebp/srm "  , " sap ecatt "  , " sap ehs "  , " sap ep "  , " sap fico "  , " sap fs "  , " sap fscm "  , " sap hr "  , " sap is oil "  , " sap is telecom "  , " sap isutilities "  , " sap its "  , " sap j2cc "  , " sap km "  , " sap mercator "  , " sap mm "  , " sap mobile infra "  , " sap netweaver "  , " sap performance tuning "  , " sap plm "  , " sap pm "  , " sap pp/pi "  , " sap san/nas admin "  , " sap-apo "  , " sap-basis "  , " sap-bc "  , " sap-biw "  , " sap-bw "  , " sap-cfm "  , " sap-co "  , " sap-crm "  , " sap-ebp/srm "  , " sap-ecatt "  , " sap-ehs "  , " sap-ep "  , " sap-fico "  , " sap-fs "  , " sap-fscm "  , " sap-gts "  , " sap-hr "  , " sap-is oil&gas/utilities/retail/telecom etc\. "  , " sapis retail "  , " sap-its "  , " sap-j2cc "  , " sap-km "  , " sap-mercator "  , " sap-mm "  , " sap-mobile infra "  , " sap-plm "  , " sap-pp/pi "  , " sap-ps "  , "  sap - qm "  , " sap-scm "  , "  sap - sd "  , " sap-sem "  , " sap-sm "  , " sap-was "  , " sap-wf "  , " sap-wm "  , " sap-xi "  , " sar "   , " satellite communication "  , " sather "  , " savrs "  , " sbc "  , " scada "  , " scaners "  , " scanner driver "  , " schematic design "  , " scheme "  , " sco unix "  , " scos unixware "  , " screenos "  , " sctp "  , " sd ram "  , " sdh "  , " sdlc "  , " sdp "  , " sed "  , " seebeyond "  , " seed7 "  , " servlets "  , " set top box "  , " setl "  , " shake lighting "  , " sharepoint "  , " shell scripts "  , " sidewinder "  , " siebel "  , " silk testing "  , " simpletest "  , " simula "  , " simulink "  , " sinec h1 "  , " sip "  , " six sigma "  , " six sigma black belt "  , " six sigma green belt "  , " slate "  , " sld "  , " slip "  , " smalltalk "  , " smartcam "  , " smat "  , " smb "  , " sms "  , " smsc "  , " smtp "  , " sna "  , " snap gear "  , " snmp "  , " snobol "  , " soap "  , " socket programming "  , " socks "  , " softice "  , " software administration "  , " solaris "  , " solid works "  , " solidcam "  , " solidedge "  , " sonet "  , " sp/k "  , " spark "  , " spc "  , " spectrum "  , " spreadsheetml "  , " sprutcam "  , " spufi "  , " spx "  , " sql "  , " sql server "  , " sqlite "  , " ss7 "  , " ssh "  , " st20 "  , " standard ml sml "  , " starlan "  , " statistical tools "  , " stb "  , " sti5518 board "  , " sti7109 "  , " stmicro "  , " storage media "  , " stp "  , " stretchy bones "  , " strim "  , " structured/oops "  , " stun "  , " sun solaris "  , " sunit "  , " suns solaris "  , " supplier quality assurance "  , " surfcam "  , " suse "  , " svg "  , " swift 3d "  , " swing "  , " swish "  , " swishmax "  , " switches "  , " swodniw "  , " sybase "  , " sybase iq "  , " symbian "  , " syncsort "  , " synon "  , " synopsis "  , " system integration "  , " systemc "  , " t2 sde "  , " tagunit "  , " tally "  , " tam "  , " tandem "  , " tanner "  , " tax "  , " tbrun "  , " tcap "  , " t-carrier "  , " tck relq "  , " tcl "  , " tcl/tk "  , " tcp "  , " tcp/ip "  , " tdm "  , " tebis "  , " technical faculty "  , " technical writing "  , " teco "  , " tei "  , " telcomp "  , " telecom billing "  , " telnet "  , " telon-online "  , " teradata "  , " teraterm "  , " tessy "  , " test director "  , " test mentor - java edition "  , " testgen4j "  , " testing tool "  , " tex "  , " texturing "  , " tftp "  , " thomson "  , " threadx "  , " ti code "  , " ti dsp "  , " tibco "  , " tiff "  , " timesten "  , " tina "  , " tms320c54x "  , " token ring "  , " topsolid cam "  , " topsolid design "  , " topsolid mold "  , " topsolid wood "  , " tornado "  , " toshiba "  , " tps "  , " tqm "  , " tqm audits "  , " troff "  , "  groff "  , " tron "  , " truebasic "  , " tso/ispf "  , " turbo c "  , " turbo c++ "  , " turbo pascal "  , " turing "  , " turing plus "  , " tv manager "  , " uart "  , " ubercode "  , " uclinux "  , " ucos-ii "  , " udi "  , " udp "  , " ultraxml "  , " uml "  , " uml 2 "  , " umts "  , " unicon "  , " uniform office format "  , " unigraphics "  , " unigraphics-grip/ug-open ufunc "  , " unit test "  , " unit++ "  , " unix "  , " unix shell programming "  , " unix utilities "  , " unix-hp-ux-solaris "  , " unixservers "  , " upnp "  , " usb "  , " usenix "  , " java ee "  , " java me "  , " acca "  , " ashrae - member "  , " ccie "  , " cfa "  , " cibse - member "  , " cis "  , " cisco "  , " ciw "  , " cma "  , " cpa "  , " hvac "  , " mcdba "  , " mcsd\.net "  , " nasd "  , " pmp "  , " scnp "  , " other certification/professional qualification "  , " microsoft office "  , " microsoft excel "  , " microsoft word "  , " microsoft powerpoint "  , " financial analysis "  , " financial modeling "  , " data science "  , " linear regression "  , " machine learning "  , " project management "  , " hadoop "  , " data visualization "  , " nlp "  , " business analytics "  , " derivatives "  , " smartstream data mode "  , " financial statement analysis "  , " batch log analysis "  , " business data analytics "  , " investment banking "  , " corporate finance "  , " financial services "  , " statutory audit "  , " credit valuation "  , " oracle pl/sql "  , " agile sdlc methodologie "  , " oracle reports "  , " git "  , " jira "  , " oracle 11g "  , " microsoft suite "  , " sales and marketing "  , " marketing executive "  , " sales executive "  , " sales and marketing executive "  , " corporate secretarial "  , " corporate legal "  , " fund raising "  , " equity & ncds "  , " equity "  , " hr tools "  , " hrbp "  , " matrix environment "  , " talent acquisition/capacity building "  , " talent acquisition "  , " stakeholder management "  , " employee engagement and communication planning "  , " employee engagement "  , " hr automation "  , " hrss "  , " hr analytics "  , " hris "  , " hr shared services "  , " hrss hr operations "  , " hr and operations "  , " organization design "  , " culture and change diagnosis "  , " psychometric profiling "  , " total reward strategy "  , " total reward strategy and evp "  , " hr audit "  , " labour laws "  , " statutory compliance "  , " human resource management "  , " acquisition and integration "  , " acquisition "  , " budget preparation "  , " risk mapping "  , " hrss (hr-ops) "  , " analyst "  , " private equity "  , " sourcing and execution "  , " sourcing "  , " capital market transactions "  , " capital market "  , " capital structuring "  , " credit derivatives "  , " credit suisse "  , " finance and accounts "  , " budgetary control "  , " mis management "  , " taxation "  , " auditing "  , " mis and budgeting "  , " trade finance "  , " financial management "  , " p&l account "  , " accounting systems "  , " fund flow statements "  , " ledgers and balance sheet "  , " balance sheet "  , " tax audit "  , " r&d "  , " mis reports "  , " sap "  , " client servicing "  , " internal auditing "  , " transition management "  , " system migration "  , " iso 9001:2008 "  , " iso 14001:2004 "  , " ohsas 18001:2007 "  , " iso/iec 27001:2005 "  , " iso/ts 16949:2009\. "  , " sales support "  , " b2b sales "  , " financial modelling "  , " valuation "  , " portfolio analysis "    , " monitoring portfolio "  , " end-to-end supply chain "  , " strategic partnership "  , " banking "  , " project finance "  , " merger and acquisition financial analysis "  , " acquisition financial analysis "  , " business strategy "  , " credit rating "  , " project risk identification "  , " measurement and mitigation strategies "  , " mitigation strategies "  , " oil and gas "  , " risk identification "  , " risk mitigation strategies "  , " audit report "  , " profit and loss account "  , " tax audit report "  , " internal audit "  , " leadership and team handling "  , " wealth management "  , " manpower management "  , " liability management "  , " cross sell of third party products "  , " recruitment "  , " customer relationship management "  , " asset management "  , " product management "  , " training and development "  , " product life cycle "  , " strategy and roadmap "  , " tracking market trends "  , " competition monitoring "  , " business strategies "  , " acquisition trends "  , " thomsonib "  , " factiva "  , " bloomberg "  , " murex "  , " capital iq "  , " portfolio analytics "  , " customer care centre "  , " fair credit reporting "  , " sales and service delivery "  , " process improvement and control "  , " business development "  , " stakeholder relationship and partnership "  , " people engagement and development "  , " analytics and research "  , " performance management "  , " operations management "  , " cost and p&l management "  , " hr operations and analytics "  , " hr operations "  , " data science "  , " big data "  , " executive leadership and strategy "  , " business process reengineering "  , " implementing standards and procedures "  , " business relationship management "  , " change management "  , " budgeting and cost optimization procurement "  , " itil "  , " itsm governance sox and security management "  , " contract/sla management "  , " cross functional team leadership "  , " project / program management & delivery "  , " erp "  , "  crm implementation "  , " it org design and talent management "  , " talent management "  , " local/regional and global outsourcing "  , " application portfolio management "  , " digital roadmap & strategy "  , " it policy and governance "  , "  licensing "  , " shared service models and centres "  , " crm "  , " sfa "  , " dms "  , " customer loyalty "  , " e-commerce "  , " trade connect portals "  , " digital supply chain "  , " manufacturing automation "  , " vendor portals "  , " compliance management "  , " quality management "  , " product development & plm "  , " cloud private "  , "  public "  , "  hybrid "  , "  sas "  , "  contracting and governance "  , " social media strategy "  , " social media strategy and enablement "  , " social analytics "  , " sap ecc "  , " sap afs "  , " sap s4 fashion/hana "  , " sap apo "  , " sap bi/bo "  , " sap ariba "  , " sap success factors "  , " sap c4c "  , " security firewalls "  , " rpa tools "  , " ai/ml platforms "  , " iot "  , " analytics platforms with predictive capabilities "  , " data leak prevention "  , " cloud security "  , " identity & access mgmt "  , " hr bp "  , " plant hr & sales hr "  , " sales hr "  , " service tax "  , " sap developments "  , " risk matrix "  , " channel sales "  , " leadership and teamwork "  , " customer relationship "  , " effective communication and presentation skills "  , " regulatory and support to legal "  , " risk assessment "  , " revenue generation "  , " international business "  , " sales & marketing "  , " p&l management "  , " human resources "  , " equity research analyst "  , " debt capital markets "  , " artificial intelligence "  , " biostatistics "  , " clinical data management "  , " cdisc "  , " sas programmer "  , " medical writer "  , " clinical research "  , " clinical trails "  , " clinical operations "  , " safety drug "  , " pharmacovigilance "  , " base sas "  , " sas functions "  , " sas procedure "  , " advance sas "  , " basic knowledge of ms office "  , " base sas 9\.4 "  , " sas enterprise "  , " pharmacokinetics "  , " pharmacodynamics analyses "  , " clinical data analysis "  , " sas macros "  , " r software "  , " systat "  , " minitab "  , " sas procs "  , " proc glm "  , " proc mixed "  , " proc means "  , " proc freq "  , " proc univariate "  , " sas sql procedure "  , " macro techniques "  , " sdtm "  , " adam dataset "  , " oncology phase iii/iv trial "  , " proc power "  , " proc plan "  , " proc surveymeans "  , " proc reg "  , " proc npar1way "  , " proc gplot "  , " proc sql "  , " proc export "  , " proc import "  , " proc print "  , " proc report "  , " proc tabulate "  , " icsrs "  , " clinical research procedures "  , " gcp "  , " ich "  , " pharmacovigilance process "  , " content writing "  , " regulatory requirement "  , " safety database "  , " sas software "  , " argus software "  , " clinical sas "  , " preparation of sop "  , " quality management "  , " audit "  , " quality parameters "  , " handling of deviation "  , " case quality review "  , " aegis 9 "  , " oracle argus 6\.0 "  , " 8\.01 "  , " clinical services "  , " narrative writing "  , " clinical safety "  , " sops "  , " quality review "  , " apqr "  , " sas program "  , " sas programming "  , " data processing "  , " data collection "  , " quantitative "  , " qualitative data analysis "  , " sas strategies "  , " statistical analysis "  , " psur/pbrer sections "  , " drugs "  , " oracle argus safety database 6\.0 "  , " clinical development "  , " ich/gcp principles "  , " us pharmacovigilance "  , " safety policies "  , " writing/aggregate reporting "  , " psur "  , " pbrer "  , " dsur "  , " pader "  , " psur addendum "  , " clinical study reports (csrs) "  , " ich-gcp "  , " schedule-y "  , " us fda "  , " cdsco directives "  , " meddra "  , " who drug "  , " spss and systat "  , " gclp "  , " glp "  , " gpvp "  , " application architecture "  , " audits "  , " iso regulations "  , " process audits "  , " software architecture "  , " cro systems audits "  , " it systems audits "  , " ctsm (drug) depots "  , " meddra "  , "  who-dd "  , " ms office (ms word "  , "  ms powerpoint "  , "  ms excel) "  , " software caliber lims "  , " moda "  , " icdas "  , " facility pro "  , " android sdk "  , " rest "  , " json "  , " phonegap "  , " reactnative "  , " flutter "  , " kotlin "  , " svn "  , " android studio "  , " ionic "  , " react js "  , " angular js "  , " cordova "  , " firebase "  , " xamarin "  , " appcelerator "  , " jenkins "  , " cocoa touch "  , " objective-c "  , " swift "  , " ios "  , " restful api "  , " react "  , " redux "  , " ecosystem "  , " redux-saga "  , " redux-thunk "  , " typescript "  , " ui design "  , " bootstrap "  , " semantic-ui "  , " antd "  , " testing frameworks as jest "  , " enzyme "  , " agile "  , " devops "  , " threading "  , " mutiproc programming "  , " agile/scrum "  , " mvc "  , " mvvm "  , " java development "  , " golang "  , " spring framework "  , " jquery "  , " relational datebase "  , " mssql "  , " nosql database "  , " mongodb "  , " docker "  , " kubernetes "  , " azure "  , " logic apps "  , " data factory "  , " sql database "  , " azure paas "  , " azure cli "  , " oracle plsql "  , " cloud development "  , " cloud deployments "  , " gitlab "  , " angular 5 "  , " restful web services "  , " sharepoint technical developer "  , " sharepoint technical architect "  , " sharepoint online "  , " development and scripting architecture "  , " java microservices "  , " spring "  , " hibernate "  , " jee "  , " micro services "  , " spring boot "  , " artifactory "  , " nexus "  , " spark and nosql db "    , " unix scripting "  , " query languages "  , " hive "  , " sqoop "  , " sparksql "  , " sap posdm "  , " sap pd "  , " sap qm "  , " sap sd "  , " sap hana "  , " sap hrpayroll "  , " sap saphr ess_mss "  , " sap appsna "  , " agile development methodologies "  , " basic framework of agile "  , " unit test case "  , " agile-based software development life cycle "  , " technical architect "  , " kafka "  , " dockerization images "  , " computer vision "  , " design aspects "  , " putty "  , " microservices "  , " unix shell scripting "  , " jda "  , " rdbms "  , " git for version control "  , " supply chain domain "  , " adobe experience manager "  , " adobe cq "  , " cms concepts "  , " web content management "  , " drupal cms development "  , " apigee drupal portal "  , " web development "  , " php development "  , " java 8 "  , " reactive programing "  , " couchbase "  , " service gateway and service discovery "  , " integration test "  , " jmeter "  , " netstrom "  , " hbase "  , " netcloud "  , " splunk "  , " prometheus "  , " grafana "  , " cloud "  , " user interface "  , " transactional "  , " dynatrace "  , " jaeger "  , " datadog "  , " pinpoint "  , " elk "  , " stack driver "  , " app insight "  , " salesforce architecture "  , " data model and salesforce industry verticals-sales "  , " health clouds "  , " soql "  , " sosl "  ]


def skills_extract(text):
    try:
        skills = []
        
        text =  re.sub("\.|,"," ", text )
        temp_text =text 
        text = text.lower()
        for i in range(len(skills_re)):
             if skills_re[i] in text:
                if len(skills_re[i])<4:
                    if skills_re[i][1].upper() in temp_text and skills_re[i][len(skills_re[i])-2 ].upper() in temp_text :
                        skills.append(re.search(skills_re[i],text)[0])
                else:
                    skills.append(re.search(skills_re[i],text)[0])
        return skills
    except:
        return []

