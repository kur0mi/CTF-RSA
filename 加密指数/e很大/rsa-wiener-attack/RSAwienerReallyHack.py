# RSAwienerAttack.py
import ContinuedFractions
import Arithmetic


def hack_RSA(e, n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)

    for (k, d) in convergents:
        # check if d is actually the key
        if k != 0 and (e*d-1) % k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr >= 0):
                t = Arithmetic.is_perfect_square(discr)
                if t != -1 and (s+t) % 2 == 0:
                    print("\nHacked!")
                    return d


def test():
    print('[+] e is too large!!!')
    e = 354611102441307572056572181827925899198345350228753730931089393275463916544456626894245415096107834465778409532373187125318554614722599301791528916212839368121066035541008808261534500586023652767712271625785204280964688004680328300124849680477105302519377370092578107827116821391826210972320377614967547827619
    n = 460657813884289609896372056585544172485318117026246263899744329237492701820627219556007788200590119136173895989001382151536006853823326382892363143604314518686388786002989248800814861248595075326277099645338694977097459168530898776007293695728101976069423971696524237755227187061418202849911479124793990722597
    print("[-] e = {}".format(e))
    print("[-] n = {}".format(n))
    d = hack_RSA(e, n)
    print("[-] d = {}".format(d))

    print('\n\n[+] e is too small!!!')
    e = 3
    n = 0xB0BEE5E3E9E5A7E8D00B493355C618FC8C7D7D03B82E409951C182F398DEE3104580E7BA70D383AE5311475656E8A964D380CB157F48C951ADFA65DB0B122CA40E42FA709189B719A4F0D746E2F6069BAF11CEBD650F14B93C977352FD13B1EEA6D6E1DA775502ABFF89D3A8B3615FD0DB49B88A976BC20568489284E181F6F11E270891C8EF80017BAD238E363039A458470F1749101BC29949D3A4F4038D463938851579C7525A69984F15B5667F34209B70EB261136947FA123E549DFFF00601883AFD936FE411E006E4E93D1A00B0FEA541BBFC8C5186CB6220503A94B2413110D640C77EA54BA3220FC8F4CC6CE77151E29B3E06578C478BD1BEBE04589EF9A197F6F806DB8B3ECD826CAD24F5324CCDEC6E8FEAD2C2150068602C8DCDC59402CCAC9424B790048CCDD9327068095EFA010B7F196C74BA8C37B128F9E1411751633F78B7B9E56F71F77A1B4DAAD3FC54B5E7EF935D9A72FB176759765522B4BBC02E314D5C06B64D5054B7B096C601236E6CCF45B5E611C805D335DBAB0C35D226CC208D8CE4736BA39A0354426FAE006C7FE52D5267DCFB9C3884F51FDDFDF4A9794BCFE0E1557113749E6C8EF421DBA263AFF68739CE00ED80FD0022EF92D3488F76DEB62BDEF7BEA6026F22A1D25AA2A92D124414A8021FE0C174B9803E6BB5FAD75E186A946A17280770F1243F4387446CCCEB2222A965CC30B3929
    print("[-] e = {}".format(e))
    print("[-] n = {}".format(n))
    d = hack_RSA(e, n)
    print("[-] d = {}".format(d))


if __name__ == '__main__':
    import sys
    '''
    if len(sys.argv) == 2 and sys.argv[1] == "test":
        print("[+] testing...")
        test()
        exit(0)
    '''

    print("[+] cracking...")
    e = int(sys.argv[1])
    n = int(sys.argv[2])
    print("[-] e = {}".format(e))
    print("[-] n = {}".format(n))
    d = hack_RSA(e, n)
    print("[-] d = {}".format(d))
