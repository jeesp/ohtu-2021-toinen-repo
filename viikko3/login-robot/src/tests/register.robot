***Settings***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallle  kalle123123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle1
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Invalid password
    
*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle1234
    Input Register Command