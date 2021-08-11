*** Settings ***
Library    SeleniumLibrary
Test Setup  Open Browser    ${appurl}    ${browser}
Test Teardown  Close Browser
*** Variables ***
${appurl}  https://opensource-demo.orangehrmlive.com/
${browser}  Firefox
*** Keywords ***
ValidateLogin
    Input Text    id:txtUsername    Admin
    Input Text    name:txtPassword    admin123
    Click Button    xpath://input[@value='LOGIN']
VerifyDashboard
    ${url}  Get Location  
    Should Contain    ${url}    dashboard           
*** Test Cases ***
LogInValidateTest
    [Tags]  Smoke 
    ValidateLogin
    VerifyDashboard
    Click Link    partial link:Welcome 
    Sleep    5s    
    Click Link  link:Logout    