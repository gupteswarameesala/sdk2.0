# Rest calls exposed by App

- [Publish App](#publish-app) 
- [Delete App](#delete-app)

## Publish App

```yaml
- METHOD: POST
  URL: https://sdk.app.opsramp.net/api/v2/tenants/f5579204-6697-412a-a762-063fbe9046cd/integrations
  HEADERS:
    - Authorization: Bearer <Token> //OAuth 2.0 Token generated with scope credentials
    - Content-Type: application/json
  BODY: 
    Manifest body
  HEADERS:
   - Authorization: Bearer <Token> //OAuth 2.0 Token generated with scope credentials
  RESPONSE: 
    - status_code: 200
```

## Delete App
```yaml
- METHOD: DELETE
  URL: https://sdk.app.opsramp.net/api/v2/tenants/f5579204-6697-412a-a762-063fbe9046cd/apps/available/sample-app-python-basic
  HEADERS:
    - Authorization: Bearer <Token> //OAuth 2.0 Token generated with scope credentials
  RESPONSE: 
    - status_code: 200
```
