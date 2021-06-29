from leads.models import User
from leads import functions

# print(User.objects.all())
# phone_num = '+79058127836'
# session_str = '1ApWapzMBuyhm1ynxKkQ4qL58doxHa27-g-aeN80l6kxSLbsPtaD5me6vNwXEXL5oZGBSVBSDap5R0ART95CtPnmVI55mmQGvC9FFyBe4K4YgrFdRLOOmIWRSz3vBXXTgh8XevtEti1COGlTeP600EL257_ni8Ikh7Ns20DoPYchm9rd61zk6HmLwAzHCQ7t0FiyrDPp3TCCkp6lA-VUYZpZ2fORpy_FlR4szTFVfd-XTcROZYtsm_UetS77alp0dQbWHzjTbb1xW0hBPIpE6kPZVHtr9yHK5MDrB2IfCtxw_fhQRAJWEaO3C9ZPRd1KoXjXQJq-9XB2gUzamQ04ddHXtI4fm1z8='

sessions = [('+3 51912800244', '1BJWap1sBu7_QoWBA9otoznE6UOo8c53z3mU9G0k-YRdKlXiLc_wwL7oskbSFpP9DB64D7QmpteLVZ2gxXxMBbMCgBNQJxtot6hTDFv4xkqOXLBPkgieMlGKrdi3teZ8BFtpm4ESnqjiLG9fHZ5ToK5BKeKxz-WjKZKaRn0k1HH2IuWWd0FzYaVRwovjp_y-zeecGQirR0tdvWPZ7FBtDppHM3KHCZx9XR0evq6sWGcVzr2CX8mtjjHE3VniOR8oUQzrI8EZ50KlfTvItvt7rq13BAbxIu8xhg8tHoQsnJCa3N3ndTzqz7zUVL15UVg8W6Za5byQM4ZNM7lrPbgi8bVdu8tGQM84='),
            ('+3 4642111759',	'1BJWap1sBuzOj_8QzmGtwZbNAPft8N_rMoti0hPPuTTaHZ8xF4vmI584Mm7Ka5QMlLzpPzgWWwM72B3R-1X2MLi4e0AdYW6ThyOSbqTlRVqO0xHyYrBKPVjQ7Grn9_HHRbWzGu6qihn9cOyU-o8LrY0bESe3Wmx-o4eux0GRbmLbR7lA0BxeALvIfwtPy3B5b3TIQdeYk_g-c8UBB7c5SdqcxEuxho8qXjUf1O5M83URhgPgq-c2k7BTTUI3AQpjn61Ff2wrCEI58ovjTefCvF4cKGdo7Gi6ivOsLDD1n7ESCApFiMEA7rnWUlioQnkqkW36RRixjrsHpnvQGAZ0CfcIiv8nBEuE='),
            ('+509 32124018',	'1AZWarzQBuxUGTBaDhHKOm1dSGEcnIFEE0ZwJk37cMSlvP33eyNveXN3ho4WJBiROAsfAz_aPsPOQAL1a4jc6HLBd4lh36MKoAoNT0YDT09j5Xvqv1awfqppZPWU9KpgRR2xlnIZ8DcsKGwEe-0L8LG4KMO2eQGOLrjXB_GwePKNsfaNQWXOYryk1Rf_3raI6YZ_V5hEeFv4m9s5a6L5DTOnd9BlaQkS06x1wqY1G8ilvfx1Fv4bu3PHuaeiW-8GWu6mdzdOkwCcccnryKKpAX3kHqxs-gzvCw6GJYWvNiinHx18vO-Q9YyVl1zV0LW_8SC6EOO_TKayy2ZC1bGpnh-WE6egmbms='),
            ('+46 734843525',	'1BJWap1sBu1YkgNU7CN1YXFyfJCScUtsHjaMTgePxjSU3tS0LJrLGFIK5e14lwhYKjX39G_K1c9M7RYxP22wsuyTv6-dzSC813TlQ2Ducc4GD_ULuVrjN8Zi-bbpZiOoClBDjCJ9iMWkEEkBpOWFbJXHK1Ja24I1SV0wjoih4hACMq8RWEsgmnfcORsL7iNuVccQUEA6nCX-r77qZGDLVl6Z8NchXFpG-I0xiwstakysKnTtsygccA4qEheqSJPfSnIv8b2XZtyKca21Hbb_okOvK-OgUQFapyGGBheZoSlz-I1dhsaMNnDrVV18R7ecX2M8NBrkvb1fQ7FFgNPEevWfKDR84r98='),
            ('+351 911545061',	'1BJWap1sBu30qjKZLlTe4XItfR12duu9d_TTABLvsAL4BJPhafkcTd9fez9oJW7eiYETm9InLv_LauYq-pPRa1sw-l-Qkl2BZhCOoyXbQgqdf5GX5kByjDH7O_R0OU1kPK69UblhEhixBqVuLZnNosr9C6t2LPABV9bkyA4OdUEzpkSIJg9CTVnqohF6meodqfigyqid6zVrFCJth8LGCFBgyvevnUKrdoQ9DeOMphV1yMV_nE8e0C8t2BE7kDyXCXmrnhfutiy5m_hO0OzCALuGZ9gTzGX7xqWgzKTf12xCdHEjS8hXehPcV1Xm4dy6pOo4bKkIFKBKO7Eew2ra-mz00dVvnCwg='),
            ('+46 767027094',	'1BJWap1sBu5XR9FlbH6j_LnUN42rlbNO-xe3_tKKJSLWr-LmO5IO67KbbWpvBtCoaY1Qx_7nx8m2CJwpjczCvXGHgGDTzWM11Mni1G3kDc9Gs9PCI-rfbYguMIOLhTa064RVra2HrpsVqh6xaCkVGrbx0iaqAtPkUg95JnVpg0ThWsLRIrn61xqNNYh5orSH3x9WBci1PFk67KbvLq20UlTm7ptZ74IB6kH_K0eDIsJqDUI2uKQGtdZmkISvO7wO0XDRbRegDBuKhDNDpA2efKJQIc1SsaKeFniLIuZrns_eu-QQCoy5VviYqZAKI7HV9if_uV5v1W991QVaSUbzxee7DRVMUVW8='),
            ('+790 33996725',	'1ApWapzMBuwdDHE_eBRSwN6AJqnEq1hVls-9L3jI4TdT3ENMCn7SucUkjc7zCHXq6SnxcrGTF3IEb-WqLaS4PLfq8HG4G6kmGa6IL4LfkdmipLXwW7_MbmYLsAB6FkAKgQou6q7uC9SC5qr4Ixcqpqqk36HM4kGFHqvHsfzosbqMYSNVAYNb2qNjWfBevJDLbXNneiwvr_lX5QYaEOgjWhmbL8uupB2vRbwFLF9DyiqsOCgWpJG-m0hL2X4RBku_jxEnJ_KrIoYIFa-xVtpt5DGRaKlXMX3Ewl_QmNcw--saWpWPHCl4ULPC-k5fAjF5I9GiHn-mHFgbjP-TMqKMavONAVLA0Fcc=')]
# functions.add_user_session(phone_num, session_str)
# print(functions.get_session_str())
# functions.update_usage_session_str(session_str)
# for phone_num, session_str in sessions:
#     print(phone_num)
#     functions.add_session_str(phone_num, session_str)
# print(functions.add_all_users('XfceDevelopment'))
# functions.generate_message_campaign('cryptoinsiderslimited')
# print(functions.get_leads_to_msg(2, 'cryptoinsiderslimited'))

# functions.check_grps()
# user = User.objects.get(username='y')
# print(functions.get_otp(user))
