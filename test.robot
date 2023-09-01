*** Settings ***
Library     RequestsLibrary

*** Test Cases ***
Get Example Test
    Create Session    ExampleAPI    http://jsonplaceholder.typicode.com
    ${response}    Get Request    ExampleAPI    /posts/1
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json().userId}    1
    Should Be Equal As Strings    ${response.json().id}    1
    Should Be Equal As Strings    ${response.json().title}    "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    Should Be Equal As Strings    ${response.json().body}    "quia et suscipit\nsuscipit..."
    Log    Response: ${response.content}
    [Teardown]    Delete All Sessions
