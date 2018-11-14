#
# Matt Schettler
# Nov 2018
# 
# https://github.com/ccomings/hft-coding-challenges/blob/master/2018-11-07/EXAMPLE-unique_email_address.md
# 


def main():

    # setup some test data
    testdata = [
        "t.e.s.t.e.m.a.i.l+matt+bob.billy+mark@leetcode.com",
        "t.e.s.t.e.m.a.i.l+matt+jay@leetcode.com",
        "t.e.s.t.e.m.a.i.l+matt@leetcode.com",
        "t.e.s.t.e.m.a.i.l.@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "test.email+alex@leetcode.com",
        "testemail+email.bob.latt@leetcode.com",
        "testemail@leetcode.com",

        "testemail+david@lee.tcode.com",
    ]

    # do the work
    results = {'@'.join((email.partition('@')[0].replace('.', '').partition('+')[0], email.partition('@')[-1])) for email in testdata}

    # output the results
    print('\n'.join(results))
    print('there are {} unique emails'.format(len(results)))


if __name__ == '__main__':
    main()
