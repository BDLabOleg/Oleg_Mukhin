
def listn(names):
    names_list = ["({}, {})".format(*reversed(name.split(":"))).upper()
                            for name in names.split(";")]

    return "".join(sorted(names_list))
    
s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
print (listn(s))


