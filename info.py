from sets import Set
from sh import ssh
from sh import grep 
from sh import sort

#ssh gvonlasz@sierra.futuregrid.org module -l avail 2>&1 >/dev/null | grep default | awk '{print $1}'

user="gvonlasz"
#
#"delta.futuregrid.org",
#
#        "foxtrot.futuregrid.org",
#"alamo.futuregrid.org",

hosts=[
       "hotel.futuregrid.org",
       "india.futuregrid.org",
       "sierra.futuregrid.org",
       ]

def get_default_modules(user,host):
    list = {}
    print host
    result = sort(ssh("{0}@{1}".format(user,host), "module", "-l", "avail", "2>&1"))
    print "ok"
    
    for line in result:
        if "default" in line:
            content = line.split()
            print content
            try:
                (module_package, module_version) = content[0].split("/")
                list[module_package] = module_version
            except:
                pass
    return list

allkeys = Set()
modules = {}       
for host in hosts:
    list = get_default_modules(user, host)
    modules[host] =  list
    print modules[host]
    allkeys = allkeys.union(modules[host].keys())

print allkeys

table = []

line = ","
for host in hosts:
    line = line + host + ","
line = line[:-1] + "\n"

for key in sorted(allkeys):
    line = line +  key + ","
    for host in hosts:
        try:
            line = line + modules[host][key]
        except:
            pass
        line = line + ","
    line = line[:-1] + "\n"

#,  >/dev/null | grep default | awk '{print $1}'

f = open ("module-list.rst", "w")
f.write(line)
close(f)
print line

