# Trigger deploy

This GitHub action allows you to trigger deloyment on render.com

## Usage

```yml
- name: Trigger Deploy
  id: render-deployer
  uses: OneHox/render-deploy-api@v1.0.0
  with:
    serviceId: srv-jkllgo61101c73fk966g
    bearer: rnd_xkQiKVCnuBUzGtySBGKKWSX7G14c
```

**Required Parameters:**

- `serviceId`: The id of the service example: https://api.render.com/v1/services/{serviceId}/deploys
- `bearer`: Authorization token for your profile

**Environmetal variables:**

- Nothing

### Outputs

- `response`: Response text from render api

### [Render Playground](https://api-docs.render.com/)

1. Open [render](https://render.com/) and login

2. Generate an api key
   - Settings > API KEY > rnd_xkQiKVCnuBUzGt\*\*\*
3. Get service id
   - YourApp -> Settings > Deploy Hook > `srv-cknlgo61101c73fk966g`

```bash
curl --request GET \
 --url 'https://api.render.com/v1/services?limit=20' \
 --header 'Accept: application/json' \
 --header 'Authorization: Bearer rnd_xkQiKVCnuBUzGt***'
```
