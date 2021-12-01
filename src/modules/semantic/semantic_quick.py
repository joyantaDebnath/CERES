# import os
# from datetime import *
# from subprocess import *
#
# from modules.helper import *
# from modules.x509_ds import *
#
#
# # def generate_smtlib_formulas(cert_list, dsl_parser, lfsc, purposes, ca_store, ca_store_sizes, only_smt, sym_chain_len):
# #     global only_smt_global
# #     global MAX_CHAIN_LENGTH
# #
# #     assignment_formulas = []
# #     property_formulas = []
# #     assignment_asserts = []
# #     property_asserts = []
# #     only_smt_global = only_smt
# #
# #     if only_smt_global and sym_chain_len >= 1:
# #         MAX_CHAIN_LENGTH = sym_chain_len
# #
# #     # generate property formulas
# #     for k in range(0, MAX_CHAIN_LENGTH):
# #         # single cert
# #         p_formulas, p_asserts = create_property_formulas_single(k)
# #         property_formulas.extend(p_formulas)
# #         property_asserts.extend(p_asserts)
# #
# #     return errors
# #
# # def create_assignment_formulas(parsedCert, k, n):
# #     bc_present_flag = False
# #     ku_present_flag = False
# #     san_present_flag = False
# #     policy_present_flag = False
# #     crl_dist_present_flag = False
# #     eku_present_flag = False
# #     aki_present_flag = False
# #     ski_present_flag = False
# #     assignment_formulas = []
# #     assignment_asserts = []
# #     #
# #     Id = parsedCert.SignatureAlgorithm.Value.Id
# #     param = parsedCert.SignatureAlgorithm.Value.Parameter
# #     if param is None:
# #         param = [0, 0, 0]
# #     else:
# #         if param.Value is None:
# #             param = [param.Type, 0, 0]
# #         else:
# #             param = [param.Type, int(param.Value, 16), len(param.Value)]
# #
# #     a1_1 = ck.Cert_sign_algo_id.Equals(Int(Id[0]))
# #     assignment_formulas.append(a1_1)
# #     assignment_asserts.append(to_smtlib_assert(a1_1))
# #     a1_2 = ck.Cert_sign_algo_id_size.Equals(Int(Id[1]))
# #     assignment_formulas.append(a1_2)
# #     assignment_asserts.append(to_smtlib_assert(a1_2))
# #     a1_3 = ck.Cert_sign_algo_param_type.Equals(Int(param[0]))
# #     assignment_formulas.append(a1_3)
# #     assignment_asserts.append(to_smtlib_assert(a1_3))
# #     a1_4 = ck.Cert_sign_algo_param.Equals(param[1])
# #     assignment_formulas.append(a1_4)
# #     assignment_asserts.append(to_smtlib_assert(a1_4))
# #     a1_5 = ck.Cert_sign_algo_param_size.Equals(param[2])
# #     assignment_formulas.append(a1_5)
# #     assignment_asserts.append(to_smtlib_assert(a1_5))
# #
# #     Id = parsedCert.TbsCertificate.SignatureAlgorithm.Value.Id
# #     param = parsedCert.TbsCertificate.SignatureAlgorithm.Value.Parameter
# #     if param is None:
# #         param = [0, 0, 0]
# #     else:
# #         if param.Value is None:
# #             param = [param.Type, 0, 0]
# #         else:
# #             param = [param.Type, int(param.Value, 16), len(param.Value)]
# #
# #     a1_6 = ck.Tbs_sign_algo_id.Equals(Int(Id[0]))
# #     assignment_formulas.append(a1_6)
# #     assignment_asserts.append(to_smtlib_assert(a1_6))
# #     a1_7 = ck.Tbs_sign_algo_id_size.Equals(Int(Id[1]))
# #     assignment_formulas.append(a1_7)
# #     assignment_asserts.append(to_smtlib_assert(a1_7))
# #     a1_8 = ck.Tbs_sign_algo_param_type.Equals(Int(param[0]))
# #     assignment_formulas.append(a1_8)
# #     assignment_asserts.append(to_smtlib_assert(a1_8))
# #     a1_9 = ck.Tbs_sign_algo_param.Equals(param[1])
# #     assignment_formulas.append(a1_9)
# #     assignment_asserts.append(to_smtlib_assert(a1_9))
# #     a1_10 = ck.Tbs_sign_algo_param_size.Equals(param[2])
# #     assignment_formulas.append(a1_10)
# #     assignment_asserts.append(to_smtlib_assert(a1_10))
# #
# #     if str(type(parsedCert.TbsCertificate.SubjectPKI.PublicKey)) == "<class 'modules.x509_ds.RSAkey'>":
# #         a31 = ck.RSA_pk_present
# #         assignment_formulas.append(a31)
# #         assignment_asserts.append(to_smtlib_assert(a31))
# #     else:
# #         a31 = ck.RSA_pk_present.Iff(False)
# #         assignment_formulas.append(a31)
# #         assignment_asserts.append(to_smtlib_assert(a31))
# #
# #     if parsedCert.TbsCertificate.Extensions is not None:
# #         a2_1 = ck.Extensions_present
# #         assignment_formulas.append(a2_1)
# #         assignment_asserts.append(to_smtlib_assert(a2_1))
# #
# #         j = 0
# #         for ex in parsedCert.TbsCertificate.Extensions.List:
# #             a12 = Equals(ck.ExtensionsList[j], Int(ex.ExtnId[0]))
# #             a_ex_crit = ck.ExtensionsCriticalsList[j].Iff(Bool(ex.Critical))
# #             a_ex_knwn = ck.ExtensionsKnownList[j].Iff(
# #                 Bool(str(type(ex.ExtnValue)) != "<class 'modules.x509_ds.Unknown_extension'>"))
# #             assignment_formulas.append(a12)
# #             assignment_asserts.append(to_smtlib_assert(a12))
# #             assignment_formulas.append(a_ex_crit)
# #             assignment_asserts.append(to_smtlib_assert(a_ex_crit))
# #             assignment_formulas.append(a_ex_knwn)
# #             assignment_asserts.append(to_smtlib_assert(a_ex_knwn))
# #
# #             j = j + 1
# #
# #             if ex.ExtnId[0] == 5578003:
# #                 bc_present_flag = True
# #                 a7_2 = ck.CA_present.Iff(Bool(ex.ExtnValue.CA))
# #                 assignment_formulas.append(a7_2)
# #                 assignment_asserts.append(to_smtlib_assert(a7_2))
# #                 if ex.ExtnValue.PathLen is not None:
# #                     a17 = And(Equals(ck.BC_pathlen, BV(ex.ExtnValue.PathLen[0], 5)),
# #                               ck.BC_pathlen_present.Iff(True))
# #                     assignment_formulas.append(a17)
# #                     assignment_asserts.append(to_smtlib_assert(a17))
# #                 else:
# #                     a17 = ck.BC_pathlen_present.Iff(False)
# #                     assignment_formulas.append(a17)
# #                     assignment_asserts.append(to_smtlib_assert(a17))
# #             elif ex.ExtnId[0] == 5577999:
# #                 ku_present_flag = True
# #                 kubits = ex.ExtnValue.Purposes
# #                 a8_1 = ck.ExKUdigitalSignature.Iff(Bool("digitalSignature" in kubits))
# #                 a8_2 = ck.ExKUnonRepudiation.Iff(Bool("nonRepudiation" in kubits))
# #                 a8_3 = ck.ExKUkeyEncipherment.Iff(Bool("keyEncipherment" in kubits))
# #                 a8_4 = ck.ExKUdataEncipherment.Iff(Bool("dataEncipherment" in kubits))
# #                 a8_5 = ck.ExKUkeyAgreement.Iff(Bool("keyAgreement" in kubits))
# #                 a8_6 = ck.ExKUkeyCertSign.Iff(Bool("keyCertSign" in kubits))
# #                 a8_7 = ck.ExKUcRLSign.Iff(Bool("cRLSign" in kubits))
# #                 a8_8 = ck.ExKUencipherOnly.Iff(Bool("encipherOnly" in kubits))
# #                 a8_9 = ck.ExKUdecipherOnly.Iff(Bool("decipherOnly" in kubits))
# #                 assignment_formulas.append(a8_1)
# #                 assignment_asserts.append(to_smtlib_assert(a8_1))
# #                 assignment_formulas.append(a8_2)
# #                 assignment_asserts.append(to_smtlib_assert(a8_2))
# #                 assignment_formulas.append(a8_3)
# #                 assignment_asserts.append(to_smtlib_assert(a8_3))
# #                 assignment_formulas.append(a8_4)
# #                 assignment_asserts.append(to_smtlib_assert(a8_4))
# #                 assignment_formulas.append(a8_5)
# #                 assignment_asserts.append(to_smtlib_assert(a8_5))
# #                 assignment_formulas.append(a8_6)
# #                 assignment_asserts.append(to_smtlib_assert(a8_6))
# #                 assignment_formulas.append(a8_7)
# #                 assignment_asserts.append(to_smtlib_assert(a8_7))
# #                 assignment_formulas.append(a8_8)
# #                 assignment_asserts.append(to_smtlib_assert(a8_8))
# #                 assignment_formulas.append(a8_9)
# #                 assignment_asserts.append(to_smtlib_assert(a8_9))
# #             elif ex.ExtnId[0] == 5578021:
# #                 eku_present_flag = True
# #                 ekus = ex.ExtnValue.Purposes
# #                 a88_1 = ck.ExEKUserverauth.Iff(Bool("serverAuth" in ekus))
# #                 a88_2 = ck.ExEKUclientauth.Iff(Bool("clientAuth" in ekus))
# #                 a88_3 = ck.ExEKUcodesign.Iff(Bool("codeSigning" in ekus))
# #                 a88_4 = ck.ExEKUemailpro.Iff(Bool("emailProtection" in ekus))
# #                 a88_5 = ck.ExEKUtimestamp.Iff(Bool("timeStamping" in ekus))
# #                 a88_6 = ck.ExEKUocspsign.Iff(Bool("OCSPSigning" in ekus))
# #                 assignment_formulas.append(a88_1)
# #                 assignment_asserts.append(to_smtlib_assert(a88_1))
# #                 assignment_formulas.append(a88_2)
# #                 assignment_asserts.append(to_smtlib_assert(a88_2))
# #                 assignment_formulas.append(a88_3)
# #                 assignment_asserts.append(to_smtlib_assert(a88_3))
# #                 assignment_formulas.append(a88_4)
# #                 assignment_asserts.append(to_smtlib_assert(a88_4))
# #                 assignment_formulas.append(a88_5)
# #                 assignment_asserts.append(to_smtlib_assert(a88_5))
# #                 assignment_formulas.append(a88_6)
# #                 assignment_asserts.append(to_smtlib_assert(a88_6))
# #             elif ex.ExtnId[0] == 5578001:
# #                 san_present_flag = True
# #                 a9_1 = ck.SanCritical.Iff(Bool(ex.Critical))
# #                 assignment_formulas.append(a9_1)
# #                 assignment_asserts.append(to_smtlib_assert(a9_1))
# #                 a9_2 = ck.SanSizenozero.Iff(Bool(len(ex.ExtnValue.Value) > 0))
# #                 assignment_formulas.append(a9_2)
# #                 assignment_asserts.append(to_smtlib_assert(a9_2))
# #             elif ex.ExtnId[0] == 5578016:
# #                 policy_present_flag = True
# #                 i = 0
# #                 for policy in ex.ExtnValue.Value:
# #                     a15 = Equals(ck.PolicyIdsList[i], Int(policy.PolicyIdentifier[0]))
# #                     assignment_formulas.append(a15)
# #                     assignment_asserts.append(to_smtlib_assert(a15))
# #                     i = i + 1
# #             elif ex.ExtnId[0] == 5578019:
# #                 if ex.ExtnValue.KeyId is not None:
# #                     aki_present_flag = True
# #             elif ex.ExtnId[0] == 5577998:
# #                 if ex.ExtnValue.KeyId is not None:
# #                     ski_present_flag = True
# #             elif ex.ExtnId[0] == 5578015:
# #                 crl_dist_present_flag = True
# #                 i = 0
# #                 for distpoint in ex.ExtnValue.Value:
# #                     a18_1 = ck.DistpointnamesList[i].Iff(
# #                         Bool(distpoint.DistributionPoint is not None))
# #                     a18_2 = ck.DistpointreasonsList[i].Iff(Bool(distpoint.Reasons is not None))
# #                     a18_3 = ck.DistpointcrlissuersList[i].Iff(Bool(distpoint.CRLIssuer is not None))
# #                     assignment_formulas.append(a18_1)
# #                     assignment_asserts.append(to_smtlib_assert(a18_1))
# #                     assignment_formulas.append(a18_2)
# #                     assignment_asserts.append(to_smtlib_assert(a18_2))
# #                     assignment_formulas.append(a18_3)
# #                     assignment_asserts.append(to_smtlib_assert(a18_3))
# #                     i = i + 1
# #     else:
# #         a2_1 = ck.Extensions_present.Iff(False)
# #         assignment_formulas.append(a2_1)
# #         assignment_asserts.append(to_smtlib_assert(a2_1))
# #
# #     e1 = ck.Bc_present.Iff(bc_present_flag)
# #     assignment_formulas.append(e1)
# #     assignment_asserts.append(to_smtlib_assert(e1))
# #     e2 = ck.Ku_present.Iff(ku_present_flag)
# #     assignment_formulas.append(e2)
# #     assignment_asserts.append(to_smtlib_assert(e2))
# #     e3 = ck.San_present.Iff(san_present_flag)
# #     assignment_formulas.append(e3)
# #     assignment_asserts.append(to_smtlib_assert(e3))
# #     e4 = ck.Policy_present.Iff(policy_present_flag)
# #     assignment_formulas.append(e4)
# #     assignment_asserts.append(to_smtlib_assert(e4))
# #     e5 = ck.Crl_dist_present.Iff(crl_dist_present_flag)
# #     assignment_formulas.append(e5)
# #     assignment_asserts.append(to_smtlib_assert(e5))
# #     e6 = ck.Eku_present.Iff(eku_present_flag)
# #     assignment_formulas.append(e6)
# #     assignment_asserts.append(to_smtlib_assert(e6))
# #     e7 = ck.Aki_keyid_present.Iff(aki_present_flag)
# #     assignment_formulas.append(e7)
# #     assignment_asserts.append(to_smtlib_assert(e7))
# #     e8 = ck.Ski_keyid_present.Iff(ski_present_flag)
# #     assignment_formulas.append(e8)
# #     assignment_asserts.append(to_smtlib_assert(e8))
# #
# #     a2_2 = ck.Version.Equals(Int(parsedCert.TbsCertificate.Version[0]))
# #     assignment_formulas.append(a2_2)
# #     assignment_asserts.append(to_smtlib_assert(a2_2))
# #
# #     a4_1 = ck.Serial_size.Equals(Int(parsedCert.TbsCertificate.Serial[1]))
# #     a4_2 = ck.Serial.Equals(Int(parsedCert.TbsCertificate.Serial[0]))
# #     a4 = And(a4_1, a4_2)
# #     assignment_formulas.append(a4)
# #     assignment_asserts.append(to_smtlib_assert(a4))
# #
# #     a10_1 = ck.Issueruniid_present.Iff(Bool(parsedCert.TbsCertificate.IssuerUID is not None))
# #     assignment_formulas.append(a10_1)
# #     assignment_asserts.append(to_smtlib_assert(a10_1))
# #
# #     a10_2 = ck.Subjectuniid_present.Iff(Bool(parsedCert.TbsCertificate.SubjectUID is not None))
# #     assignment_formulas.append(a10_2)
# #     assignment_asserts.append(to_smtlib_assert(a10_2))
# #
# #     p = -1
# #     Issuer = Symbol("Issuer_{}".format(k), ArrayType(INT, ArrayType(INT, ArrayType(INT, INT))))
# #     Issuer_rdns_size = Symbol("Issuer_rdns_size_{}".format(k), ArrayType(INT, INT))
# #     for rdnset in parsedCert.TbsCertificate.Issuer.List:
# #         p = p + 1
# #         q = -1
# #         IssuerRDN = Symbol("IssuerRDN_{}_{}".format(k, p), ArrayType(INT, ArrayType(INT, INT)))
# #         if rdnset != None:
# #             for attbt in rdnset.List:
# #                 q = q + 1
# #                 oid = attbt.Id[0]
# #                 valtype = attbt.Value.Type
# #                 value = call_stringprep(attbt.Value.Value, valtype)
# #                 if value is None:
# #                     errors.append(
# #                         "Issuer : LDAP string perparation error in certificate {} set {} attribute {}".format(k, p, q))
# #                     return [], []
# #
# #                 IssuerRDNNA = Symbol("IssuerRDNNA_{}_{}_{}".format(k, p, q), ArrayType(INT, INT))
# #                 IssuerRDNNA = Store(IssuerRDNNA, Int(0), Int(oid))
# #                 IssuerRDNNA = Store(IssuerRDNNA, Int(1), Int(valtype))
# #                 IssuerRDNNA = Store(IssuerRDNNA, Int(2), Int(value))
# #                 IssuerRDN = Store(IssuerRDN, Int(q), IssuerRDNNA)
# #             Issuer = Store(Issuer, Int(p), IssuerRDN)
# #             Issuer_rdns_size = Store(Issuer_rdns_size, Int(p), Int(q + 1))
# #     a_iss1 = ck.Issuer.Equals(Issuer)
# #     a_iss2 = ck.Issuer_rdns_size.Equals(Issuer_rdns_size)
# #     a_iss3 = ck.Issuer_length.Equals(Int(p + 1))
# #     a_iss = And(a_iss1, a_iss2, a_iss3)
# #
# #     assignment_formulas.append(a_iss)
# #     assignment_asserts.append(to_smtlib_assert(a_iss))
# #
# #     p = -1
# #     Subject = Symbol("Subject_{}".format(k), ArrayType(INT, ArrayType(INT, ArrayType(INT, INT))))
# #     Subject_rdns_size = Symbol("Subject_rdns_size_{}".format(k), ArrayType(INT, INT))
# #     for rdnset in parsedCert.TbsCertificate.Subject.List:
# #         p = p + 1
# #         q = -1
# #         SubjectRDN = Symbol("SubjectRDN_{}_{}".format(k, p), ArrayType(INT, ArrayType(INT, INT)))
# #         if rdnset != None:
# #             for attbt in rdnset.List:
# #                 q = q + 1
# #                 oid = attbt.Id[0]
# #                 valtype = attbt.Value.Type
# #                 value = call_stringprep(attbt.Value.Value, valtype)
# #                 if value is None:
# #                     errors.append(
# #                         "Subject : LDAP string perparation error in certificate {} set {} attribute {}".format(k, p, q))
# #                     return [], []
# #
# #                 SubjectRDNNA = Symbol("SubjectRDNNA_{}_{}_{}".format(k, p, q), ArrayType(INT, INT))
# #                 SubjectRDNNA = Store(SubjectRDNNA, Int(0), Int(oid))
# #                 SubjectRDNNA = Store(SubjectRDNNA, Int(1), Int(valtype))
# #                 SubjectRDNNA = Store(SubjectRDNNA, Int(2), Int(value))
# #                 SubjectRDN = Store(SubjectRDN, Int(q), SubjectRDNNA)
# #             Subject = Store(Subject, Int(p), SubjectRDN)
# #             Subject_rdns_size = Store(Subject_rdns_size, Int(p), Int(q + 1))
# #     a_sub1 = ck.Subject.Equals(Subject)
# #     a_sub2 = ck.Subject_rdns_size.Equals(Subject_rdns_size)
# #     a_sub3 = ck.Subject_length.Equals(Int(p + 1))
# #     a_sub = And(a_sub1, a_sub2, a_sub3)
# #
# #     assignment_formulas.append(a_sub)
# #     assignment_asserts.append(to_smtlib_assert(a_sub))
# #
# #     NByr, NBmon, NBday, NBhr, NBmin, NBsec = Timedecoder(parsedCert.TbsCertificate.Validity.NotBefore)
# #     NAyr, NAmon, NAday, NAhr, NAmin, NAsec = Timedecoder(parsedCert.TbsCertificate.Validity.NotAfter)
# #
# #     current_time = datetime.utcnow()
# #     Curyr, Curmon, Curday, Curhr, Curmin, Cursec = int(current_time.year), int(current_time.month), int(
# #         current_time.day), int(current_time.hour), int(current_time.minute), int(current_time.second)
# #
# #     a21_1 = And(ck.NotbeforeYr.Equals(BV(NByr, 14)), ck.NotbeforeMon.Equals(BV(NBmon, 4)),
# #                 ck.NotbeforeDay.Equals(BV(NBday, 5)), ck.NotbeforeHr.Equals(BV(NBhr, 5)),
# #                 ck.NotbeforeMin.Equals(BV(NBmin, 6)), ck.NotbeforeSec.Equals(BV(NBsec, 6)))
# #     a21_2 = And(ck.NotafterYr.Equals(BV(NAyr, 14)), ck.NotafterMon.Equals(BV(NAmon, 4)),
# #                 ck.NotafterDay.Equals(BV(NAday, 5)), ck.NotafterHr.Equals(BV(NAhr, 5)),
# #                 ck.NotafterMin.Equals(BV(NAmin, 6)), ck.NotafterSec.Equals(BV(NAsec, 6)))
# #     a21_3 = And(ck.CurtimeYr.Equals(BV(Curyr, 14)), ck.CurtimeMon.Equals(BV(Curmon, 4)),
# #                 ck.CurtimeDay.Equals(BV(Curday, 5)), ck.CurtimeHr.Equals(BV(Curhr, 5)),
# #                 ck.CurtimeMin.Equals(BV(Curmin, 6)), ck.CurtimeSec.Equals(BV(Cursec, 6)))
# #     a21 = And(a21_1, a21_2, a21_3)
# #     assignment_formulas.append(a21)
# #     assignment_asserts.append(to_smtlib_assert(a21))
# #
# #     return assignment_formulas, assignment_asserts
#
#
# def create_property_formulas_single(k):
#     property_formulas = []
#     property_asserts = []
#     ck = chain_smtVariables[k]
#
#     ## assign Index
#     f0 = ck.Index.Equals(BV(k, 5))
#     property_formulas.append(f0)
#     property_asserts.append(to_smtlib_assert(f0))
#
#     # signatureAlgorithm field MUST contain the same algorithm identifier as the
#     # signature field in the sequence tbsCertificate.
#     f1_1 = ck.Cert_sign_algo_id.Equals(ck.Tbs_sign_algo_id)
#     f1_2 = ck.Cert_sign_algo_id_size.Equals(ck.Tbs_sign_algo_id_size)
#     f1_3 = ck.Cert_sign_algo_param_type.Equals(ck.Tbs_sign_algo_param_type)
#     f1_4 = ck.Cert_sign_algo_param.Equals(ck.Tbs_sign_algo_param)
#     f1_5 = ck.Cert_sign_algo_param_size.Equals(ck.Tbs_sign_algo_param_size)
#     f1 = And(f1_1, f1_2, f1_3, f1_4, f1_5)
#     property_formulas.append(f1)
#     property_asserts.append(to_smtlib_named_assert(f1, 'signatureAlgorithm_mismatch_in_certificate_{}'.format(k)))
#     #
#     # Extension field MUST only appear if the Version is 3
#     f2 = ck.Extensions_present.Implies(ck.Version.Equals(2))
#     property_formulas.append(f2)
#     property_asserts.append(to_smtlib_named_assert(f2, 'extension_appears_in_older_version_certificate_{}'.format(k)))
#
#     # At a minimum, conforming implementations MUST recognize Version 3 certificates.
#     # Generation of version 2 certificates is not expected by implementations based on this profile.
#     f3 = Or(ck.Version.Equals(0), ck.Version.Equals(2))
#     property_formulas.append(f3)
#     property_asserts.append(to_smtlib_named_assert(f3, 'unsupported_version_in_certificate_{}'.format(k)))
#
#     # The Serial number MUST be a positive integer assigned by the CA to
#     # each certificate. Certificate users MUST be able to
#     # handle SerialNumber values up to 20 octets. (we will consider 50 octet)
#     f4_1 = And(GE(ck.Serial_size, Int(1)), LE(ck.Serial_size, Int(50)))
#     f4_2 = GT(ck.Serial, Int(0))
#     f4 = And(f4_1, f4_2)
#     property_formulas.append(f4)
#     property_asserts.append(to_smtlib_named_assert(f4, 'serial_not_in_range_in_certificate_{}'.format(k)))
#     #
#     # The issuer field MUST contain a non-empty distinguished name (DN).
#     f5 = GT(ck.Issuer_length, Int(0))
#     property_formulas.append(f5)
#     property_asserts.append(to_smtlib_named_assert(f5, 'empty_issuer_rdn_in_certificate_{}'.format(k)))
#     #
#     # if the subject is a CA (e.g., the basic constraints extension, is present and the value of cA is
#     # TRUE), then the subject field MUST be populated with a non-empty
#     # distinguished name.
#     f7 = And(ck.Bc_present, ck.CA_present).Implies(GT(ck.Subject_length, Int(0)))
#     property_formulas.append(f7)
#     property_asserts.append(to_smtlib_named_assert(f7, 'empty_subject_rdn_in_ca_certificate_{}'.format(k)))
#     #
#     # Unique Identifiers fields MUST only appear if the Version is 2 or 3.
#     # These fields MUST NOT appear if the Version is 1.
#     f10_1 = ck.Issueruniid_present.Implies(Or(ck.Version.Equals(1), ck.Version.Equals(2)))
#     f10_2 = ck.Subjectuniid_present.Implies(Or(ck.Version.Equals(1), ck.Version.Equals(2)))
#     f10_3 = ck.Version.Equals(0).Implies(ck.Issueruniid_present.Iff(False))
#     f10_4 = ck.Version.Equals(0).Implies(ck.Subjectuniid_present.Iff(False))
#     f10 = And(f10_1, f10_2, f10_3, f10_4)
#     property_formulas.append(f10)
#     property_asserts.append(to_smtlib_named_assert(f10, 'unique_identifier_in_version_1_certificate_{}'.format(k)))
#     #
#     # Where it appears, the pathLenConstraint field
#     # MUST be greater than or equal to zero.
#     f17 = And(ck.Bc_present, ck.BC_pathlen_present).Implies(BVUGE(ck.BC_pathlen, BV(0, 5)))
#     property_formulas.append(f17)
#     property_asserts.append(to_smtlib_named_assert(f17, 'pathLenConstraint_not_in_range_in_certificate_{}'.format(k)))
#     #
#     # If the subject is a CRL issuer (e.g., the key usage extension, is present
#     # and the value of cRLSign is TRUE), then the subject field MUST be populated with a non-empty
#     # distinguished name.
#     f8 = And(ck.Ku_present, ck.ExKUcRLSign).Implies(GT(ck.Subject_length, Int(0)))
#     property_formulas.append(f8)
#     property_asserts.append(to_smtlib_named_assert(f8, 'empty_subject_rdn_in_crl_certificate_{}'.format(k)))
#     #
#     # When the keyUsage extension appears in a certificate, at least one of the bits MUST be set to 1.
#     f14 = ck.Ku_present.Implies(Or(ck.ExKUdigitalSignature, ck.ExKUnonRepudiation, ck.ExKUkeyEncipherment,
#                                    ck.ExKUdataEncipherment, ck.ExKUkeyAgreement, ck.ExKUkeyCertSign,
#                                    ck.ExKUcRLSign, ck.ExKUencipherOnly, ck.ExKUdecipherOnly))
#     property_formulas.append(f14)
#     property_asserts.append(to_smtlib_named_assert(f14, 'no_key_usage_purpose_in_certificate_{}'.format(k)))
#     #
#     # If subject naming information is present only in the subjectAltName extension , then the subject
#     # name MUST be an empty sequence and the subjectAltName extension MUST be critical.
#     f9 = And(ck.San_present, ck.SanSizenozero, Equals(ck.Subject_length, Int(0))).Implies(ck.SanCritical)
#     property_formulas.append(f9)
#     property_asserts.append(to_smtlib_named_assert(f9, 'wrong_usage_of_subjectAltName_in_certificate_{}'.format(k)))
#     #
#     # If the subjectAltName extension is present, the sequence MUST contain at least one entry.
#     f16 = ck.San_present.Implies(ck.SanSizenozero)
#     property_formulas.append(f16)
#     property_asserts.append(to_smtlib_named_assert(f16, 'subjectAltName_is_empty_in_certificate_{}'.format(k)))
#     #
#     # If the keyCertSign bit is asserted, then the cA bit in the basic
#     # constraints extension MUST also be asserted.
#     # If the cA boolean is not asserted, then the keyCertSign bit
#     # in the key usage extension MUST NOT be asserted.
#     f13 = And(ck.Ku_present, ck.Bc_present).Implies(Or(Not(ck.ExKUkeyCertSign), ck.CA_present))
#     property_formulas.append(f13)
#     property_asserts.append(to_smtlib_named_assert(f13, 'keycertsign_in_non_ca_certificate_{}'.format(k)))
#     #
#     # A certificate MUST NOT include more than one instance of a particular extension.
#     f12 = ck.Extensions_present.Implies(AllDifferent(ck.ExtensionsList))
#     property_formulas.append(f12)
#     property_asserts.append(to_smtlib_named_assert(f12, 'repeated_extensions_in_certificate_{}'.format(k)))
#
#     # A certificate-using system MUST reject the certificate if it encounters
#     # a critical extension it does not recognize or a critical extension
#     # that contains information that it cannot process.
#     for p in range(0, MAX_EXTENSIONS):
#         f12_crit_ext = And(ck.Extensions_present, ck.ExtensionsCriticalsList[p]).Implies(ck.ExtensionsKnownList[p])
#         property_formulas.append(f12_crit_ext)
#         property_asserts.append(
#             to_smtlib_named_assert(f12_crit_ext,
#                                    'unknown_critical_extension_{}_in_certificate_{}'.format(p, k)))
#     #
#     # A certificate policy OID MUST NOT appear more than once in a certificate policies extension.
#     f15 = ck.Policy_present.Implies(AllDifferent(ck.PolicyIdsList))
#     property_formulas.append(f15)
#     property_asserts.append(to_smtlib_named_assert(f15, 'repeated_policies_in_certificate_{}'.format(k)))
#     #
#     # While each of these fields is optional, a DistributionPoint MUST NOT
#     # consist of only the reasons field; either distributionPoint or
#     # cRLIssuer MUST be present
#     for i in range(0, MAX_DISTPOINT):
#         f18 = And(ck.Crl_dist_present, ck.DistpointreasonsList[i]).Implies(
#             Or(ck.DistpointnamesList[i], ck.DistpointcrlissuersList[i]))
#         property_formulas.append(f18)
#         property_asserts.append(to_smtlib_named_assert(f18,
#                                                        'wrong_structure_1_of_CRL_distribution_point_{}_in_certificate_{}'.format(
#                                                            i, k)))
#
#     #
#     # The certificate validity period includes the current time.
#     f21_1 = generate_time_constraints(ck.NotbeforeYr, ck.NotbeforeMon, ck.NotbeforeDay,
#                                       ck.NotbeforeHr, ck.NotbeforeMin, ck.NotbeforeSec,
#                                       ck.CurtimeYr, ck.CurtimeMon, ck.CurtimeDay,
#                                       ck.CurtimeHr, ck.CurtimeMin, ck.CurtimeSec)
#     f21_2 = generate_time_constraints(ck.CurtimeYr, ck.CurtimeMon, ck.CurtimeDay,
#                                       ck.CurtimeHr, ck.CurtimeMin, ck.CurtimeSec,
#                                       ck.NotafterYr, ck.NotafterMon, ck.NotafterDay,
#                                       ck.NotafterHr, ck.NotafterMin, ck.NotafterSec)
#     f21 = And(f21_1, f21_2)
#     property_formulas.append(f21)
#     property_asserts.append(to_smtlib_named_assert(f21, 'expired_certificate_{}'.format(k)))
#
#     return property_formulas, property_asserts
#
#
# # call LDAP
# def call_stringprep(Value, ValType):
#     try:
#         if ValType == 30:  # bmpstring
#             Value = bytes(Value).decode('utf-16-be')
#         elif ValType == 19:  # printablestring
#             Value = bytes(Value).decode('us-ascii')
#         elif ValType == 12:  # UTF8String
#             Value = bytes(Value).decode('utf-8')
#         elif ValType == 28:  # universalstring
#             Value = bytes(Value).decode('utf-32-be')
#         elif ValType == 20:  # teletexstring
#             Value = bytes(Value).decode('iso-8859-1')
#     except:
#         return None
#
#     stringprep = Popen(
#         ["{}/stringprep/runStringPrep".format(extra_location), Value],
#         stdout=PIPE)
#     (output, err) = stringprep.communicate()
#     stringprep.wait()
#     Value = output[1:len(output) - 2]
#     if Value == b'ERROR!!':
#         return None
#
#     return int.from_bytes(Value, byteorder='big')
#
#
# def generate_time_constraints(Yr1, Mon1, Day1, Hr1, Min1, Sec1, Yr2, Mon2, Day2, Hr2, Min2, Sec2):
#     # time1 <= time2
#     f21_12 = Ite(Equals(Sec1, Sec2), Bool(True), Bool(False))
#     f21_11 = Ite(BVULT(Sec1, Sec2), Bool(True), f21_12)
#     f21_10 = Ite(Equals(Min1, Min2), f21_11, Bool(False))
#     f21_9 = Ite(BVULT(Min1, Min2), Bool(True), f21_10)
#     f21_8 = Ite(Equals(Hr1, Hr2), f21_9, Bool(False))
#     f21_7 = Ite(BVULT(Hr1, Hr2), Bool(True), f21_8)
#     f21_6 = Ite(Equals(Day1, Day2), f21_7, Bool(False))
#     f21_5 = Ite(BVULT(Day1, Day2), Bool(True), f21_6)
#     f21_4 = Ite(Equals(Mon1, Mon2), f21_5, Bool(False))
#     f21_3 = Ite(BVULT(Mon1, Mon2), Bool(True), f21_4)
#     f21_2 = Ite(Equals(Yr1, Yr2), f21_3, Bool(False))
#     f21_1 = Ite(BVULT(Yr1, Yr2), Bool(True), f21_2)
#     return f21_1
import sys
import traceback
from datetime import datetime

from modules.x509_ds import GenericTime


def Implies(p, q):
    return (not p) or q


def Ite(cond, p1, p2):
    if cond:
        return p1
    else:
        return p2


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
        assert (Implies(extensions != None, version == 2)), "version must be 3 (2) when extensions are present"

        ## serial > 0
        assert (serial > 0), "serial number must be positive"

        ## certSignAlgo == tbsSignAlgo
        assert (certSignAlgo.Id[0] == tbsSignAlgo.Id[0]), "Signature Algorithm OIDs must match"
        if (certSignAlgo.Parameter == None or tbsSignAlgo.Parameter == None):
            assert (certSignAlgo.Parameter == tbsSignAlgo.Parameter), "Signature Algorithm Parameters must match"
        else:
            assert (
                    certSignAlgo.Parameter.Type == tbsSignAlgo.Parameter.Type), "Signature Algorithm Parameters must match"
            assert (
                    certSignAlgo.Parameter.Value == tbsSignAlgo.Parameter.Value), "Signature Algorithm Parameters must match"

        ## notBefore <= curtime <= notAfter
        utime = datetime.utcnow()
        curtime = GenericTime(int(utime.year), int(utime.month), int(utime.day),
                              int(utime.hour), int(utime.minute), int(utime.second))
        nb_le_cur = time_check(validity.NotBefore, curtime)
        cur_le_na = time_check(curtime, validity.NotAfter)
        assert (nb_le_cur and cur_le_na), "Incorrect certificate validity"
    except AssertionError as e:
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        _, _, _, text = tb_info[-1]
        msg = text.split("), ")[1]
        result = "Failure : semantic error; reason - " + msg
    return result
