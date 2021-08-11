***Settings***
Library  SeleniumLibrary
Test Setup      Open Browser    ${appurl}  ${browser}
Test Teardown   Close Browser
***Variables***
${appurl}  https://opensource-demo.orangehrmlive.com/
${browser}  Firefox
*** Test Cases ***
HelloWorld
    Log To Console    Success!!    

LogInTestValid
    [Tags]  Smoke
    Input Text    id:txtUsername    Admin
    Input Text    name:txtPassword    admin123
    Click Button    xpath://input[@value='LOGIN']    
    ${'url'}  Get Location
    Should Contain  ${'url'}  dashboard  
  
LogInTestInValid
    [Tags]  Regression
    Input Text    id:txtUsername    Admin
    Input Text    name:txtPassword    admin124
    Click Button    xpath://input[@value='LOGIN']    
    ${'url'}  Get Location
    Should Contain  ${'url'}  dashboard   