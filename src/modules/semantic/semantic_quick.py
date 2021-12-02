from datetime import datetime

from modules.x509_ds import GenericTime


def Implies(p, q):
    return (not p) or q


def Ite(cond, p1, p2):
    if cond:
        return p1
    else:
        return p2


def Assert(cond, msg):
    if not cond:
        raise Exception(msg)


def getVersion(c):
    return c.TbsCertificate.Version[0]


def getSerial(c):
    return c.TbsCertificate.Serial[0]


def getCertSignAlgo(c):
    return c.SignatureAlgorithm.Value


def getTbsSignAlgo(c):
    return c.TbsCertificate.SignatureAlgorithm.Value


def getValidity(c):
    return c.TbsCertificate.Validity


def getExtensions(c):
    return c.TbsCertificate.Extensions


def getIssuer(c):
    return c.TbsCertificate.Issuer


def getSubject(c):
    return c.TbsCertificate.Subject


def time_check(x, y):
    ## returns x<=y
    m12 = Ite(x.Second == y.Second, True, False)
    m11 = Ite(x.Second < y.Second, True, m12)
    m10 = Ite(x.Minute == y.Minute, m11, False)
    m9 = Ite(x.Minute < y.Minute, True, m10)
    m8 = Ite(x.Hour == y.Hour, m9, False)
    m7 = Ite(x.Hour < y.Hour, True, m8)
    m6 = Ite(x.Day == y.Day, m7, False)
    m5 = Ite(x.Day < y.Day, True, m6)
    m4 = Ite(x.Month == y.Month, m5, False)
    m3 = Ite(x.Month < y.Month, True, m4)
    m2 = Ite(x.Year == y.Year, m3, False)
    m1 = Ite(x.Year < y.Year, True, m2)
    return m1


def check(cert):
    result = "Success : No semantic failure"

    certSignAlgo = getCertSignAlgo(cert)
    version = getVersion(cert)
    serial = getSerial(cert)
    tbsSignAlgo = getTbsSignAlgo(cert)
    # issuer = getIssuer(cert)
    # subject = getSubject(cert)
    validity = getValidity(cert)
    extensions = getExtensions(cert)

    try:
        ## if extensions present, version must be 3
        Assert(Implies(extensions != None, version == 2), "version must be 3 (2) when extensions are present")

        ## serial > 0
        Assert(serial > 0, "serial number must be positive")

        ## certSignAlgo == tbsSignAlgo
        Assert(certSignAlgo.Id[0] == tbsSignAlgo.Id[0], "Signature Algorithm OIDs must match")
        if (certSignAlgo.Parameter == None or tbsSignAlgo.Parameter == None):
            Assert(certSignAlgo.Parameter == tbsSignAlgo.Parameter, "Signature Algorithm Parameters must match")
        else:
            Assert(
                certSignAlgo.Parameter.Type == tbsSignAlgo.Parameter.Type, "Signature Algorithm Parameters must match")
            Assert(
                certSignAlgo.Parameter.Value == tbsSignAlgo.Parameter.Value,
                "Signature Algorithm Parameters must match")

        ## notBefore <= curtime <= notAfter
        utime = datetime.utcnow()
        curtime = GenericTime(int(utime.year), int(utime.month), int(utime.day),
                              int(utime.hour), int(utime.minute), int(utime.second))
        nb_le_cur = time_check(validity.NotBefore, curtime)
        cur_le_na = time_check(curtime, validity.NotAfter)
        Assert(nb_le_cur and cur_le_na, "Incorrect certificate validity")
    except Exception as e:
        result = "Failure : semantic error; reason - " + str(e)
        pass
    return result
