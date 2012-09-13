#!/usr/bin/python2.6
import fact_query

def main():
    #enter main command line loop
    while True:
        user_input = raw_input("QUERY@CIA_FACTBOOK>>> ")
        if user_input == '':
            break

        parse_and_execute_command(user_input)

    
def parse_and_execute_command(user_input):
    matching_countries = set()

    #check for special command
    if user_input[0:2] == "DO":
        print "SPECIAL COMMAND ISSUED. EXECUTING."
        if user_input.split(":")[0].strip() == "DO=lat_lon_vaca":
            matching_countries = fact_query.special_find_lat_lon_capital_vacation(int(user_input.split(":")[1]))

        for country in matching_countries:
            print country

        return

    #separate main refiners and clean them up
    main_refiners = map(str.strip, user_input.split(","))
    first_match = True

    for refiner in main_refiners:
        attribute = None
        operator = None
        value = None

        #break up refiner into attribute / operator / value
        if '=' in refiner:
            attribute, value = refiner.split('=')
            operator = "="
        elif '>' in refiner:
            attribute, value = refiner.split('>')
            operator = ">"
        else:
            print "ERROR: no operator in refiner '" + refiner + "'"

        # have first matching initialize the set to intersect
        if first_match:
            matching_countries = set(fact_query.fetch_matching_countries(attribute, operator, value))
            first_match = False
        else:
            matching_countries.intersection(fact_query.fetch_matching_countries(attribute, operator, value))

    print "\n\n QUERY RETURNED THESE COUNTRIES:"

    for country in matching_countries:
        print country + "\n"


if __name__=="__main__":
    main()
