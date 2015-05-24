
import urllib.parse


def getNiceName(srcurl):
	mapper = {
		'9ethtranslations.wordpress.com'            : 'TheLazy9',
		'a0132.blogspot.com'                        : 'A0132',
		'aflappyteddybird.wordpress.com'            : 'AFlappyTeddyBird',
		'ahoujicha.blogspot.com'                    : 'Roasted Tea',
		'aldnoahextrathetranslation.wordpress.com'  : '(NanoDesu) - Aldnoah Zero',
		'alyschu.wordpress.com'                     : 'Alyschu & Co',
		'amaburithetranslation.wordpress.com'       : '(NanoDesu) - Amagi Brilliant Park ',
		'arkmachinetranslations.com'                : 'Ark Machine Translations',
		'avertranslation.org'                       : 'Avert Translations',
		'azureskytls.blogspot.com'                  : 'Azure Sky Translation',
		'binhjamin.wordpress.com'                   : 'Binhjamin',
		'blazingtranslations.com'                   : 'Blazing Translations',
		'bluesilvertranslations.wordpress.com'      : 'Blue Silver Translations',
		'bureidanworks.wordpress.com'               : 'Burei Dan Works',
		'calicoxtabby.wordpress.com'                : 'Calico x Tabby',
		'cetranslation.blogspot.com'                : 'C.E. Light Novel Translations',
		'choukun.wordpress.com'                     : 'ELYSION Translation',
		'defiring.wordpress.com'                    : 'Defiring',
		'dlingson.wordpress.com'                    : 'Lingson\'s Translations',
		'durandaru.wordpress.com'                   : 'Duran Daru Translation',
		'fateapocryphathetranslation.wordpress.com' : '(NanoDesu) - Fate/Apocrypha',
		'flowerbridgetoo.com'                       : 'Flower Bridge Too',
		'flowerbridgetoo.wordpress.com'             : 'Flower Bridge Too',
		'fuyuugakuenthetranslation.wordpress.com'   : '(NanoDesu) - Fuyuu Gakuen no Alice and Shirley',
		'gekkahimethetranslation.wordpress.com'     : '(NanoDesu) - Gekka no Utahime to Magi no Ou',
		'giraffecorps.liamak.net'                   : 'Giraffe Corps',
		'gjbuthetranslation.wordpress.com'          : '(NanoDesu) - GJ-Bu',
		'gravitytranslations.com'                   : 'Gravity Translation',
		'grimgalthetranslation.wordpress.com'       : '(NanoDesu) - Hai to Gensou no Grimgal',
		'guhehe.net'                                : 'guhehe.TRANSLATIONS',
		'hajiko.wordpress.com'                      : 'Hajiko translation',
		'heartcrusadescans.wordpress.com'           : 'Heart Crusade Scans',
		'hellotranslations.wordpress.com'           : 'Hello Translations',
		'hellping.org'                              : 'Hellping',
		'hendricksensama.wordpress.com'             : 'Hendricksen-sama',
		'hennekothetranslation.wordpress.com'       : '(NanoDesu) - Hentai Ouji to Warawanai Neko',
		'henoujikun.wordpress.com'                  : 'Henouji Translation',
		'hikuosan.blogspot.com'                     : 'ヾ(。￣□￣)ﾂ',   # I can haz UTF-8 source code?
		'hokagetranslations.wordpress.com'          : 'Hokage Translations',
		'hui3r.wordpress.com'                       : 'Fanatical',
		'imoutoliciouslnt.blogspot.com'             : 'Imoutolicious Light Novel Translations',
		'insigniapierce.wordpress.com'              : 'Insignia Pierce',
		'isekaimahou.wordpress.com'                 : 'Isekai Mahou Translations!',
		'istlovesu.blogspot.com'                    : 'Istian\'s Workshop',
		'itranslateln.wordpress.com'                : 'itranslateln',
		'izra709.wordpress.com'                     : 'izra709 | B Group no Shounen Translations',
		'japtem.com'                                : 'Japtem',
		'jawztranslations.blogspot.com'             : 'JawzTranslations',
		'kaezartranslations.blogspot.com'           : 'Kaezar Translations',
		'kamitranslation.wordpress.com'             : 'Kami Translation',
		'kerambitnosakki.wordpress.com'             : 'Kerambit\'s Incisions',
		'kirikotranslations.wordpress.com'          : 'Kiriko Translations',
		'kirileaves.wordpress.com'                  : 'Kiri Leaves',
		'kobatochandaisuki.wordpress.com'           : 'KobatoChanDaiSukiScan',
		'korezombiethetranslation.wordpress.com'    : '(NanoDesu) - Kore wa Zombie Desu ka?',
		'krytykal.org'                              : 'Krytyk\'s Translations',
		'kurenaithetranslation.wordpress.com'       : '(NanoDesu) - Kurenai',
		'kurotsuki-novel.blogspot.com'              : 'Kurotsuki Novel',
		'kyakka.wordpress.com'                      : 'Kyakka',
		'lasolistia.com'                            : 'HaruPARTY',
		'loliquent.wordpress.com'                   : 'Loliquent',
		'lorcromwell.wordpress.com'                 : 'LorCromwell',
		'lordofscrubs.wordpress.com'                : 'LordofScrubs',
		'loveyouthetranslation.wordpress.com'       : '(NanoDesu) - Love★You',
		'lygartranslations.wordpress.com'           : 'LygarTranslations',
		'madospicy.wordpress.com'                   : 'MadoSpicy TL',
		'mahoukoukoku.blogspot.com'                 : 'Mahou Koukoku',
		'mahoutsuki.wordpress.com'                  : 'Mahoutsuki Translation',
		'manga0205.wordpress.com'                   : 'Manga0205 Translations',
		'maoyuuthetranslation.wordpress.com'        : '(NanoDesu) - Maoyuu Maou Yuusha',
		'mayochikithetranslation.wordpress.com'     : '(NanoDesu) - Mayo Chiki',
		'metalhaguremt.wordpress.com'               : '1HP',
		'nakulas.blogspot.com'                      : '[nakulas]',
		'nanodesutranslations.wordpress.com'        : 'NanoDesu Light Novel Translations',
		'natsutl.wordpress.com'                     : 'Natsu TL',
		'neettranslations.wordpress.com'            : 'NEET Translations',
		'nightbreezetranslations.com'               : 'Nightbreeze Translations',
		'nightraccoon.wordpress.com'                : 'Konjiki no Wordmaster',
		'noitl.blogspot.com'                        : 'Translation Treasure Box',
		'ohanashimi.wordpress.com'                  : 'Ohanashimi',
		'ojamajothetranslation.wordpress.com'       : '(NanoDesu) - Ojamajo Doremi',
		'omegaharem.wordpress.com'                  : 'Omega Harem Translations',
		'oniichanyamete.wordpress.com'              : 'お兄ちゃん、やめてぇ！',
		'oregairuthetranslation.wordpress.com'      : '(NanoDesu) - Yahari Ore no Seishun Love Come wa Machigatteiru',
		'oreimothetranslation.wordpress.com'        : '(NanoDesu) - Oreimo',
		'otterspacetranslation.wordpress.com'       : 'otterspacetranslation',
		'pandafuqtranslations.wordpress.com'        : 'pandafuqtranslations',
		'panofitrans.blogspot.com'                  : 'Translations From Outer Space',
		'pikatranslations.com'                      : 'Pika Translations',
		'pikatranslations.wordpress.com'            : 'Pika Translations',
		'pirateyoshi.wordpress.com'                 : 'Ziru\'s Musings | Translations~',
		'pummels.wordpress.com'                     : 'Pummels',
		'putttytranslations.wordpress.com'          : 'putttytranslations',
		'reantoanna.wordpress.com'                  : 'ℝeanとann@',
		'rhinabolla.wordpress.com'                  : 'Rhinabolla',
		'rokkathetranslation.wordpress.com'         : '(NanoDesu) - Rokka no Yuusha',
		'saekanothetranslation.wordpress.com'       : '(NanoDesu) - Saenai Heroine no Sodatekata',
		'sakurahonyaku.wordpress.com'               : '桜翻訳! | Light novel translations',
		'sasamisanthetranslation.wordpress.com'     : '(NanoDesu) - Sasami-San@Ganbaranai',
		'scryatranslations.wordpress.com'           : 'Scrya Translations',
		'seizonthetranslation.wordpress.com'        : '(NanoDesu) - Seitokai no Ichizon',
		'sekaigamethetranslation.wordpress.com'     : '(NanoDesu) - Kono Sekai ga Game Dato Ore Dake ga Shitteiru',
		'setsuna86blog.wordpress.com'               : 'SETSUNA86BLOG',
		'shincodezeroblog.wordpress.com'            : 'Code-Zero\'s Blog',
		'shinsekai.cadet-nine.org'                  : 'Shin Sekai Yori – From the New World',
		'shintranslations.com'                      : 'Shin Translations',
		'shintranslations.wordpress.com'            : 'Shin Translations',
		'shokyuutranslations.wordpress.com'         : 'Shokyuu Translations',
		'skythewood.blogspot.com'                   : 'Skythewood translations',
		'skyworldthetranslation.wordpress.com'      : '(NanoDesu) - Sky World',
		'stcon.wordpress.com'                       : 'Stellar Transformation Con.',
		'swordandgame.blogspot.com'                 : 'Sword and Game',
		'tensaitranslations.wordpress.com'          : 'Tensai Translations',
		'thatguywhosthere.wordpress.com'            : 'ThatGuyOverThere',
		'thenakedsol.blogspot.com'                  : 'Iterations within a Thought-Eclipse',
		'theworsttranslation.wordpress.com'         : 'Bad Translation',
		'thundertranslations.com'                   : 'Thunder Translation',
		'tomorolls.wordpress.com'                   : 'Tomorolls',
		'totobro.com'                               : 'Totokk\'s Translations',
		'tototrans.com'                             : 'Totokk\'s Translations',
		'trippingoverwn.wordpress.com'              : 'Tripp Translations',
		'tsaltranslation.wordpress.com'             : 'Light Novel translations',
		'tsuigeki.wordpress.com'                    : 'Tsuigeki Translations',
		'tu-shu-guan.blogspot.com'                  : '中翻英圖書館 Translations',
		'tusjecht.wordpress.com'                    : 'Tus-Trans',
		'unbreakablemachinedoll.wordpress.com'      : 'Unbreakable Machine Doll',
		'undecentlnt.wordpress.com'                 : 'Undecent Translations',
		'unlimitednovelfailures.mangamatters.com'   : 'Unlimited Novel Failures',
		'untuned-strings.blogspot.com'              : 'Untuned Translation Blog',
		'vaancruze.wordpress.com'                   : 'Maou the Yuusha',
		'voidtranslations.wordpress.com'            : 'Void Translations',
		'wartdf.wordpress.com'                      : 'Raising the Dead',
		'wcctranslation.wordpress.com'              : 'wcctranslation',
		'worldofwatermelons.com'                    : 'World of Watermelons',
		'www.lingson.com'                           : 'Lingson Translations',
		'www.princerevolution.org'                  : 'Prince Revolution!',
		'www.risingdragonstranslation.com'          : 'Rising Dragons Translation',
		'www.sousetsuka.com'                        : 'Sousetsuka',
		'www.taptaptaptaptap.net'                   : 'tap-trans » tappity tappity tap.',
		'www.wuxiaworld.com'                        : 'Wuxiaworld',
		'xcrossj.blogspot.com'                      : 'XCrossJ',
		'yoraikun.wordpress.com'                    : 'Yoraikun Translation',
		'youtsubasilver.wordpress.com'              : 'youtsubasilver\'s Blog',
		'zmunjali.wordpress.com'                    : 'Roxism HQ',

	}

	srcnetloc = urllib.parse.urlparse(srcurl).netloc

	if srcnetloc in mapper:
		return mapper[srcnetloc]

	# print("Unknown netloc?", srcnetloc)
	# print("Src url?", srcurl)
	return False
