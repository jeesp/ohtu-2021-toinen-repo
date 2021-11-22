*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallekalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Not Succeed

Register With Valid Username And Too Short Password
    Set Username  kal
    Set Password  kall3
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Not Succeed

Register With Nonmatching Password And Password Confirmation
    Set Username  kal
    Set Password  kall3kal
    Set Password Confirmation  kalle1234
    Submit Credentials
    Register Should Not Succeed

Login After Successful Registration
    Set Username  kallekallea
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed
    Go to Main Page
    Logout
    Set Username  kallekallea
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Not Succeed
    Go To Login Page
    Set Username  ka
    Set Password  kalle123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
Submit Credentials
    Click Button  Register
Submit Login Credentials
    Click Button  Login
Logout
    Click Button  Logout
Go To Login Page
    Click Link  Login
Go To Main Page
    Click Link Continue to main page
Register Should Succeed
    Welcome Page Should Be Open
Register Should Not Succeed
    Register Page Should Be Open
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}