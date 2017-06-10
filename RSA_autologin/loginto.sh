#!/usr/bin/expect -f  
set input1 [lindex $argv 0]
set password "KFWbGnRRbxj2Kz9z"
set ip "10.20.0.60"
set username "chenshaoyue"
set private_key "chenshaoyue.pem"
set JUMP_SERVER_EXIT "q\n"
set DATE [exec date]
spawn ssh $username@$ip -i $private_key
expect {                
    "*assphrase*" { send "$password\n" }
}  

expect {
    "*Last login:*" { send "$input1\n" }
}
expect {
    "*Last login:*" { send "echo now in cache1\n" }
}

#get log files

send "echo $DATE\n"
interact

