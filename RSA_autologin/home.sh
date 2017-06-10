#!/usr/bin/wish
#
# netset.tcl
# 03.26.2001 bilbrey
 
set ConFile "./ui.conf"
 
if [catch {open $ConFile r} Conf] {
  puts stderr "Open $ConFile failed"
  return 1
}
 
# parse config, define buttons
set Bcount 0
while {[gets $Conf Cline] >= 0} {
  if {1 == [string match #* $Cline]} continue
  if {[string length $Cline] < 4} continue
 
  set Nend [string wordend $Cline 0]
  incr Nend -1
  set Bname [string range $Cline 0 $Nend]
  set Cbeg [expr $Nend + 2]
  set Bcomd "exec "
  append Bcomd [string range $Cline $Cbeg end]
 
  incr Bcount
  set NextBut "button$Bcount"
  button .$NextBut -text $Bname -command $Bcomd
}
 
if {$Bcount == 1} {
  puts stderr "No buttons defined"
  return 2
}
 
# display buttons
while {$Bcount >= 1} {
  set NextBut "button$Bcount"
  pack .$NextBut -padx 10 -pady 10
  incr Bcount -1
}
 
button .exit -text Exit -command {exit}
pack .exit -padx 10 -pady 10
