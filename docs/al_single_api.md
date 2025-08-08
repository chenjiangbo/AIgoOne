---
title: Inflet API v1.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---


*算法应用列表*

算法应用列表

<h3 id="get__v1_apps-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|label|query|string|false|标签：|
|name|query|string|false|算法应用名称|
|order|query|string|false|排序方式，默认为desc，可选值:|
|order_by|query|string|false|排序字段，默认为created_at，可选值:|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|task_id|query|integer|false|任务ID|
|type|query|string|false|算法应用类型:|

#### Detailed descriptions

**label**: 标签：
* Face - 脸部识别

**order**: 排序方式，默认为desc，可选值:
* desc - 降序
* asc - 升序

**order_by**: 排序字段，默认为created_at，可选值:
* created_at - 创建时间
* updated_at - 更新时间
* name - 算法应用名称

**type**: 算法应用类型:
* image - 图像服务
* video - 视频任务

#### Enumerated Values

|Parameter|Value|
|---|---|
|type|video|
|type|image|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "config_url": "string",
      "cover": "string",
      "created_at": 0,
      "description": "string",
      "expired_at": 0,
      "id": 0,
      "label": "string",
      "limit": 0,
      "module_definitions_url": "string",
      "name": "string",
      "type": "video",
      "updated_at": 0,
      "used": 0
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_apps-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.AppList](#schemamodels.applist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_apps

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/apps \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/apps HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "file": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/apps',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/apps',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/apps', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/apps', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/apps");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/apps", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/apps`

*导入算法应用*

导入算法应用

> Body parameter

```yaml
file: string

```

<h3 id="post__v1_apps-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|object|true|none|
|» file|body|string(binary)|true|算法应用文件，仅支持gem格式|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_apps-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_apps_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/apps/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/apps/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/apps/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/apps/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/apps/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/apps/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/apps/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/apps/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/apps/{id}`

*算法应用详情*

算法应用详情

<h3 id="get__v1_apps_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|算法应用ID|

> Example responses

> 200 Response

```json
{
  "config_url": "string",
  "cover": "string",
  "created_at": 0,
  "description": "string",
  "expired_at": 0,
  "id": 0,
  "label": "string",
  "limit": 0,
  "module_definitions_url": "string",
  "name": "string",
  "type": "video",
  "updated_at": 0,
  "used": 0
}
```

<h3 id="get__v1_apps_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.App](#schemamodels.app)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_apps_{id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/apps/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/apps/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "config": "string",
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/apps/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/apps/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/apps/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/apps/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/apps/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/apps/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/apps/{id}`

*更新算法应用*

更新算法应用

> Body parameter

```json
{
  "config": "string",
  "name": "string"
}
```

<h3 id="put__v1_apps_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|算法应用ID|
|body|body|[models.UpdateAppReq](#schemamodels.updateappreq)|true|body参数|

> Example responses

> 200 Response

```json
{
  "config_url": "string",
  "cover": "string",
  "created_at": 0,
  "description": "string",
  "expired_at": 0,
  "id": 0,
  "label": "string",
  "limit": 0,
  "module_definitions_url": "string",
  "name": "string",
  "type": "video",
  "updated_at": 0,
  "used": 0
}
```

<h3 id="put__v1_apps_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.App](#schemamodels.app)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_apps_{id}

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/apps/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
DELETE /api/inflet/v1/apps/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/apps/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.delete '/api/inflet/v1/apps/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.delete('/api/inflet/v1/apps/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/apps/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/apps/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/apps/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/apps/{id}`

*删除算法应用*

删除算法应用

<h3 id="delete__v1_apps_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|算法应用ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="delete__v1_apps_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_apps_{id}_reset_config

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/apps/{id}/reset_config \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/apps/{id}/reset_config HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/apps/{id}/reset_config',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/apps/{id}/reset_config',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/apps/{id}/reset_config', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/apps/{id}/reset_config', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/apps/{id}/reset_config");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/apps/{id}/reset_config", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/apps/{id}/reset_config`

*重置算法应用配置*

重置算法应用配置

<h3 id="post__v1_apps_{id}_reset_config-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_apps_{id}_reset_config-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-auditlogs">auditlogs</h1>

## get__v1_auditlogs

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/auditlogs \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/auditlogs HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/auditlogs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/auditlogs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/auditlogs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/auditlogs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/auditlogs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/auditlogs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/auditlogs`

*日志列表*

日志列表

<h3 id="get__v1_auditlogs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|content|query|string|false|日志内容|
|end|query|integer|false|结束时间|
|level|query|array[string]|false|日志级别:|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|resource|query|string|false|资源类型|
|start|query|integer|false|起始时间|

#### Detailed descriptions

**level**: 日志级别:
* `Info`-信息
* `Warn`-警告
* `Error`-错误

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "content": "string",
      "created_at": 0,
      "id": 0,
      "level": "string",
      "resource": "string"
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_auditlogs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.AuditLogList](#schemamodels.auditloglist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-cameras">cameras</h1>

## get__v1_camera_preview

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/camera/preview?id=string \
  -H 'Accept: application/json'

```

```http
GET /api/inflet/v1/camera/preview?id=string HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/camera/preview?id=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/inflet/v1/camera/preview',
  params: {
  'id' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/inflet/v1/camera/preview', params={
  'id': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/camera/preview', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/camera/preview?id=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/camera/preview", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/camera/preview`

*摄像头预览*

(http upgrade to websockets)

<h3 id="get__v1_camera_preview-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|query|string|true|摄像头ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="get__v1_camera_preview-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_cameras

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/cameras \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/cameras HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/cameras',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/cameras',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/cameras', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/cameras', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/cameras");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/cameras", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/cameras`

*摄像机列表*

摄像机列表

<h3 id="get__v1_cameras-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|name|query|string|false|摄像机名称|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|status|query|array[string]|false|摄像机状态|

#### Detailed descriptions

**status**: 摄像机状态
* online - 在线
* offline - 离线
* abnormality - 码流异常

#### Enumerated Values

|Parameter|Value|
|---|---|
|status|online|
|status|offline|
|status|abnormality|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "cover_url": "string",
      "created_at": 0,
      "fps": 0,
      "id": "string",
      "name": "string",
      "preview_url": "string",
      "resolution": "string",
      "status": "online",
      "stream_url": "string",
      "updated_at": 0
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_cameras-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.CameraList](#schemamodels.cameralist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_cameras

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/cameras \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/cameras HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "name": "string",
  "stream_url": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/cameras',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/cameras',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/cameras', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/cameras', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/cameras");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/cameras", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/cameras`

*创建摄像机*

创建摄像机

> Body parameter

```json
{
  "name": "string",
  "stream_url": "string"
}
```

<h3 id="post__v1_cameras-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.CreateCameraReq](#schemamodels.createcamerareq)|true|body参数|

> Example responses

> 200 Response

```json
{
  "cover_url": "string",
  "created_at": 0,
  "fps": 0,
  "id": "string",
  "name": "string",
  "preview_url": "string",
  "resolution": "string",
  "status": "online",
  "stream_url": "string",
  "updated_at": 0
}
```

<h3 id="post__v1_cameras-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Camera](#schemamodels.camera)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_cameras_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/cameras/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/cameras/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/cameras/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/cameras/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/cameras/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/cameras/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/cameras/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/cameras/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/cameras/{id}`

*摄像机详情*

摄像机详情

<h3 id="get__v1_cameras_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|摄像机ID|

> Example responses

> 200 Response

```json
{
  "cover_url": "string",
  "created_at": 0,
  "fps": 0,
  "id": "string",
  "name": "string",
  "preview_url": "string",
  "resolution": "string",
  "status": "online",
  "stream_url": "string",
  "updated_at": 0
}
```

<h3 id="get__v1_cameras_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Camera](#schemamodels.camera)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_cameras_{id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/cameras/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/cameras/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/cameras/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/cameras/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/cameras/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/cameras/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/cameras/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/cameras/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/cameras/{id}`

*更新摄像机*

更新摄像机

> Body parameter

```json
{
  "name": "string"
}
```

<h3 id="put__v1_cameras_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|摄像机ID|
|body|body|[models.UpdateCameraReq](#schemamodels.updatecamerareq)|true|body参数|

> Example responses

> 200 Response

```json
{
  "cover_url": "string",
  "created_at": 0,
  "fps": 0,
  "id": "string",
  "name": "string",
  "preview_url": "string",
  "resolution": "string",
  "status": "online",
  "stream_url": "string",
  "updated_at": 0
}
```

<h3 id="put__v1_cameras_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Camera](#schemamodels.camera)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_cameras_{id}

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/cameras/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
DELETE /api/inflet/v1/cameras/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/cameras/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.delete '/api/inflet/v1/cameras/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.delete('/api/inflet/v1/cameras/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/cameras/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/cameras/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/cameras/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/cameras/{id}`

*删除摄像机*

删除摄像机

<h3 id="delete__v1_cameras_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|摄像机ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="delete__v1_cameras_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-config">config</h1>

## get__v1_config_alarm

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/config/alarm \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/config/alarm HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/alarm',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/config/alarm',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/config/alarm', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/config/alarm', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/alarm");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/config/alarm", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/config/alarm`

*获取告警配置*

获取告警配置

<h3 id="get__v1_config_alarm-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "audio_url": "string",
  "enable_audio": true
}
```

<h3 id="get__v1_config_alarm-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.AlarmConfig](#schemamodels.alarmconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_config_alarm

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/config/alarm \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/config/alarm HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "audio_file": "string",
  "enable_audio": true
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/alarm',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/config/alarm',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/config/alarm', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/config/alarm', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/alarm");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/config/alarm", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/config/alarm`

*设置告警配置*

设置告警配置

> Body parameter

```yaml
audio_file: string
enable_audio: true

```

<h3 id="post__v1_config_alarm-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|object|false|none|
|» audio_file|body|string(binary)|false|告警音频文件，仅支持mp3格式|
|» enable_audio|body|boolean|false|告警音频开关|

> Example responses

> 200 Response

```json
{
  "audio_url": "string",
  "enable_audio": true
}
```

<h3 id="post__v1_config_alarm-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.AlarmConfig](#schemamodels.alarmconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_config_device_subscribe

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/config/device_subscribe \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/config/device_subscribe HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/device_subscribe',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/config/device_subscribe',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/config/device_subscribe', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/config/device_subscribe', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/device_subscribe");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/config/device_subscribe", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/config/device_subscribe`

*获取设备订阅配置*

获取设备订阅配置

<h3 id="get__v1_config_device_subscribe-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "app_key_id": "string",
  "app_key_secret": "string",
  "enable_push": true,
  "interval": "string",
  "url": "string"
}
```

<h3 id="get__v1_config_device_subscribe-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.DeviceSubscribeConfig](#schemamodels.devicesubscribeconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_config_device_subscribe

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/config/device_subscribe \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/config/device_subscribe HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "app_key_id": "string",
  "app_key_secret": "string",
  "enable_push": true,
  "interval": "string",
  "url": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/device_subscribe',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/config/device_subscribe',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/config/device_subscribe', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/config/device_subscribe', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/device_subscribe");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/config/device_subscribe", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/config/device_subscribe`

*设置设备订阅配置*

设置设备订阅配置

> Body parameter

```json
{
  "app_key_id": "string",
  "app_key_secret": "string",
  "enable_push": true,
  "interval": "string",
  "url": "string"
}
```

<h3 id="post__v1_config_device_subscribe-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.DeviceSubscribeConfig](#schemamodels.devicesubscribeconfig)|true|body参数|

> Example responses

> 200 Response

```json
{
  "app_key_id": "string",
  "app_key_secret": "string",
  "enable_push": true,
  "interval": "string",
  "url": "string"
}
```

<h3 id="post__v1_config_device_subscribe-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.DeviceSubscribeConfig](#schemamodels.devicesubscribeconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_config_logo

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/config/logo \
  -H 'Accept: application/json'

```

```http
GET /api/inflet/v1/config/logo HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/config/logo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/inflet/v1/config/logo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/inflet/v1/config/logo', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/config/logo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/logo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/config/logo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/config/logo`

*获取logo配置*

获取logo配置

> Example responses

> 200 Response

```json
{
  "day_ico": "string",
  "day_logo": "string",
  "night_ico": "string",
  "night_logo": "string",
  "platform_name": "string",
  "slogan": "string"
}
```

<h3 id="get__v1_config_logo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.LogoConfig](#schemamodels.logoconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_config_logo

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/config/logo \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: */*' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/config/logo HTTP/1.1

Content-Type: multipart/form-data
Accept: */*
Authorization: string

```

```javascript
const inputBody = '{
  "platform_name": "string",
  "slogan": "string",
  "day_ico": "string",
  "night_ico": "string",
  "day_logo": "string",
  "night_logo": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'*/*',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/logo',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => '*/*',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/config/logo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': '*/*',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/config/logo', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => '*/*',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/config/logo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/logo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"*/*"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/config/logo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/config/logo`

*设置logo配置*

设置logo配置

> Body parameter

```yaml
platform_name: string
slogan: string
day_ico: string
night_ico: string
day_logo: string
night_logo: string

```

<h3 id="post__v1_config_logo-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|object|false|none|
|» platform_name|body|string|false|平台名称|
|» slogan|body|string|false|slogan|
|» day_ico|body|string(binary)|false|白天ico文件，仅支持ico格式|
|» night_ico|body|string(binary)|false|晚上ico文件，仅支持ico格式|
|» day_logo|body|string(binary)|false|白天logo文件，仅支持png格式|
|» night_logo|body|string(binary)|false|晚上logo文件，仅支持png格式|

> Example responses

> 200 Response

<h3 id="post__v1_config_logo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.LogoConfig](#schemamodels.logoconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_config_logo

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/config/logo \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
DELETE /api/inflet/v1/config/logo HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/logo',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.delete '/api/inflet/v1/config/logo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.delete('/api/inflet/v1/config/logo', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/config/logo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/logo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/config/logo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/config/logo`

*重置logo配置*

重置logo配置

<h3 id="delete__v1_config_logo-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{}
```

<h3 id="delete__v1_config_logo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_config_menu

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/config/menu \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/config/menu HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/menu',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/config/menu',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/config/menu', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/config/menu', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/menu");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/config/menu", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/config/menu`

*获取菜单配置*

获取菜单配置

<h3 id="get__v1_config_menu-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "enable_audit_log": true,
  "enable_feature_lib": true,
  "enable_image_service": true,
  "enable_monitor": true,
  "enable_reflow": true
}
```

<h3 id="get__v1_config_menu-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.MenuConfig](#schemamodels.menuconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_config_menu

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/config/menu \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/config/menu HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "enable_audit_log": true,
  "enable_feature_lib": true,
  "enable_image_service": true,
  "enable_monitor": true,
  "enable_reflow": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/menu',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/config/menu',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/config/menu', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/config/menu', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/menu");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/config/menu", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/config/menu`

*设置菜单配置*

设置菜单配置

> Body parameter

```json
{
  "enable_audit_log": true,
  "enable_feature_lib": true,
  "enable_image_service": true,
  "enable_monitor": true,
  "enable_reflow": true
}
```

<h3 id="post__v1_config_menu-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.MenuConfig](#schemamodels.menuconfig)|true|body参数|

> Example responses

> 200 Response

```json
{
  "enable_audit_log": true,
  "enable_feature_lib": true,
  "enable_image_service": true,
  "enable_monitor": true,
  "enable_reflow": true
}
```

<h3 id="post__v1_config_menu-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.MenuConfig](#schemamodels.menuconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_config_subscribe

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/config/subscribe \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/config/subscribe HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/subscribe',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/config/subscribe',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/config/subscribe', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/config/subscribe', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/subscribe");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/config/subscribe", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/config/subscribe`

*获取事件订阅配置*

获取事件订阅配置

<h3 id="get__v1_config_subscribe-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "app_key_id": "string",
  "app_key_secret": "string",
  "enable_push_to_gddi": true,
  "enable_push_to_third": true,
  "event_image_with_roi": true,
  "push_in_order": true,
  "upload_type": 1,
  "url": "string"
}
```

<h3 id="get__v1_config_subscribe-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.SubscribeConfig](#schemamodels.subscribeconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_config_subscribe

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/config/subscribe \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/config/subscribe HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "app_key_id": "string",
  "app_key_secret": "string",
  "enable_push_to_gddi": true,
  "enable_push_to_third": true,
  "event_image_with_roi": true,
  "push_in_order": true,
  "upload_type": 1,
  "url": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/subscribe',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/config/subscribe',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/config/subscribe', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/config/subscribe', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/subscribe");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/config/subscribe", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/config/subscribe`

*设置事件订阅配置*

设置事件订阅配置

> Body parameter

```json
{
  "app_key_id": "string",
  "app_key_secret": "string",
  "enable_push_to_gddi": true,
  "enable_push_to_third": true,
  "event_image_with_roi": true,
  "push_in_order": true,
  "upload_type": 1,
  "url": "string"
}
```

<h3 id="post__v1_config_subscribe-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.SubscribeConfig](#schemamodels.subscribeconfig)|true|body参数|

> Example responses

> 200 Response

```json
{
  "app_key_id": "string",
  "app_key_secret": "string",
  "enable_push_to_gddi": true,
  "enable_push_to_third": true,
  "event_image_with_roi": true,
  "push_in_order": true,
  "upload_type": 1,
  "url": "string"
}
```

<h3 id="post__v1_config_subscribe-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.SubscribeConfig](#schemamodels.subscribeconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_config_system

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/config/system \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/config/system HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/system',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/config/system',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/config/system', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/config/system', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/system");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/config/system", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/config/system`

*获取系统配置*

获取系统配置

<h3 id="get__v1_config_system-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "auto_clean_threshold": 0,
  "max_threshold": 0
}
```

<h3 id="get__v1_config_system-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.SystemConfig](#schemamodels.systemconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_config_system

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/config/system \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/config/system HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "auto_clean_threshold": 0,
  "max_threshold": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/system',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/config/system',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/config/system', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/config/system', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/system");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/config/system", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/config/system`

*设置系统配置*

设置系统配置

> Body parameter

```json
{
  "auto_clean_threshold": 0,
  "max_threshold": 0
}
```

<h3 id="post__v1_config_system-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.SystemConfig](#schemamodels.systemconfig)|true|body参数|

> Example responses

> 200 Response

```json
{
  "auto_clean_threshold": 0,
  "max_threshold": 0
}
```

<h3 id="post__v1_config_system-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.SystemConfig](#schemamodels.systemconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_config_test_subscribe

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/config/test_subscribe \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/config/test_subscribe HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/config/test_subscribe',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/config/test_subscribe',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/config/test_subscribe', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/config/test_subscribe', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/config/test_subscribe");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/config/test_subscribe", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/config/test_subscribe`

*测试事件订阅配置*

测试事件订阅配置

<h3 id="post__v1_config_test_subscribe-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "message": "string",
  "pass": true
}
```

<h3 id="post__v1_config_test_subscribe-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.TestSubscribeResponse](#schemamodels.testsubscriberesponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-device">device</h1>

## post__v1_device_change_name

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/device/change_name \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/device/change_name HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/change_name',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/device/change_name',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/device/change_name', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/device/change_name', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/change_name");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/device/change_name", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/device/change_name`

*修改设备名称*

修改设备名称

> Body parameter

```json
{
  "name": "string"
}
```

<h3 id="post__v1_device_change_name-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.ChangeDeviceNameReq](#schemamodels.changedevicenamereq)|true|设备名称|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_device_change_name-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_device_export_gxt

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/device/export_gxt \
  -H 'Accept: application/octet-stream' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/device/export_gxt HTTP/1.1

Accept: application/octet-stream
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/octet-stream',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/export_gxt',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/octet-stream',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/device/export_gxt',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/octet-stream',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/device/export_gxt', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/octet-stream',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/device/export_gxt', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/export_gxt");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/octet-stream"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/device/export_gxt", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/device/export_gxt`

*导出GXT注册文件*

导出GXT注册文件

<h3 id="get__v1_device_export_gxt-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

<h3 id="get__v1_device_export_gxt-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_device_info

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/device/info \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/device/info HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/info',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/device/info',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/device/info', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/device/info', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/info");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/device/info", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/device/info`

*设备信息*

设备信息

<h3 id="get__v1_device_info-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "available_upgrade": true,
  "connected_to_cloud": true,
  "name": "string",
  "registered": true,
  "sn": "string",
  "type": "string",
  "upgrade_progress": 0,
  "version": {
    "property1": "string",
    "property2": "string"
  }
}
```

<h3 id="get__v1_device_info-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.DeviceInfo](#schemamodels.deviceinfo)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_device_logs

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/device/logs \
  -H 'Accept: application/octet-stream' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/device/logs HTTP/1.1

Accept: application/octet-stream
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/octet-stream',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/logs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/octet-stream',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/device/logs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/octet-stream',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/device/logs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/octet-stream',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/device/logs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/logs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/octet-stream"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/device/logs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/device/logs`

*下载程序日志*

下载程序日志日志

<h3 id="get__v1_device_logs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|程序ID|

> Example responses

> 200 Response

<h3 id="get__v1_device_logs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_device_network

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/device/network \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/device/network HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/network',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/device/network',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/device/network', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/device/network', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/network");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/device/network", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/device/network`

*获取网络配置*

获取网络配置

<h3 id="get__v1_device_network-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
[
  {
    "DHCP4": true,
    "address": "string",
    "gateway4": "string",
    "name": "string",
    "nameservers": [
      "string"
    ]
  }
]
```

<h3 id="get__v1_device_network-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<h3 id="get__v1_device_network-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[models.Ethernet](#schemamodels.ethernet)]|false|none|none|
|» DHCP4|boolean|false|none|是否DHCP|
|» address|string|false|none|IP地址|
|» gateway4|string|false|none|网关|
|» name|string|false|none|网卡名称|
|» nameservers|[string]|false|none|DNS|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_device_network

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/device/network \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/device/network HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '[
  {
    "DHCP4": true,
    "address": "string",
    "gateway4": "string",
    "name": "string",
    "nameservers": [
      "string"
    ]
  }
]';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/network',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/device/network',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/device/network', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/device/network', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/network");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/device/network", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/device/network`

*更新网络配置*

更新网络配置

> Body parameter

```json
[
  {
    "DHCP4": true,
    "address": "string",
    "gateway4": "string",
    "name": "string",
    "nameservers": [
      "string"
    ]
  }
]
```

<h3 id="post__v1_device_network-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.Ethernet](#schemamodels.ethernet)|true|body参数|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_device_network-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_device_offline_upgrade

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/device/offline_upgrade \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/device/offline_upgrade HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "file": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/offline_upgrade',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/device/offline_upgrade',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/device/offline_upgrade', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/device/offline_upgrade', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/offline_upgrade");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/device/offline_upgrade", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/device/offline_upgrade`

*离线升级平台*

离线升级平台

> Body parameter

```yaml
file: string

```

<h3 id="post__v1_device_offline_upgrade-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|object|true|none|
|» file|body|string(binary)|true|离线升级文件|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_device_offline_upgrade-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_device_reboot

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/device/reboot \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/device/reboot HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/reboot',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/device/reboot',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/device/reboot', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/device/reboot', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/reboot");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/device/reboot", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/device/reboot`

*重启设备*

重启设备

<h3 id="post__v1_device_reboot-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_device_reboot-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_device_register

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/device/register \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/device/register HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "code": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/register',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/device/register',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/device/register', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/device/register', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/register");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/device/register", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/device/register`

*注册设备*

注册设备

> Body parameter

```json
{
  "code": "string"
}
```

<h3 id="post__v1_device_register-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.RegisterDeviceReq](#schemamodels.registerdevicereq)|true|body参数|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_device_register-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_device_reset

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/device/reset \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/device/reset HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "password": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/reset',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/device/reset',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/device/reset', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/device/reset', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/reset");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/device/reset", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/device/reset`

*重置平台*

重置平台

> Body parameter

```json
{
  "password": "string"
}
```

<h3 id="post__v1_device_reset-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.ResetReq](#schemamodels.resetreq)|true|body参数|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_device_reset-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_device_systime

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/device/systime \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/device/systime HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/systime',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/device/systime',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/device/systime', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/device/systime', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/systime");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/device/systime", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/device/systime`

*获取系统时间*

获取系统时间

<h3 id="get__v1_device_systime-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "ntp_server": "string",
  "sync": true,
  "timestamp": 0
}
```

<h3 id="get__v1_device_systime-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.SysTime](#schemamodels.systime)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_device_systime

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/device/systime \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/device/systime HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "ntp_server": "string",
  "sync": true,
  "timestamp": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/systime',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/device/systime',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/device/systime', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/device/systime', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/systime");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/device/systime", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/device/systime`

*设置系统时间*

设置系统时间

> Body parameter

```json
{
  "ntp_server": "string",
  "sync": true,
  "timestamp": 0
}
```

<h3 id="post__v1_device_systime-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.SysTime](#schemamodels.systime)|true|body参数|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_device_systime-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_device_unregister

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/device/unregister \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/device/unregister HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/unregister',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/device/unregister',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/device/unregister', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/device/unregister', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/unregister");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/device/unregister", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/device/unregister`

*注销设备*

注销设备

<h3 id="post__v1_device_unregister-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_device_unregister-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_device_upgrade

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/device/upgrade \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/device/upgrade HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/device/upgrade',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/device/upgrade',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/device/upgrade', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/device/upgrade', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/device/upgrade");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/device/upgrade", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/device/upgrade`

*升级平台*

升级平台

<h3 id="post__v1_device_upgrade-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_device_upgrade-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-eventreflowjob">EventReflowJob</h1>

## get__v1_eventReflowJobs

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/eventReflowJobs \
  -H 'Accept: application/json'

```

```http
GET /api/inflet/v1/eventReflowJobs HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/eventReflowJobs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/inflet/v1/eventReflowJobs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/inflet/v1/eventReflowJobs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/eventReflowJobs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/eventReflowJobs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/eventReflowJobs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/eventReflowJobs`

*事件回流任务列表*

事件回流任务列表

<h3 id="get__v1_eventreflowjobs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|app_id|query|integer|false|none|
|name|query|string|false|名称|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|status|query|string|false|服务状态:|

#### Detailed descriptions

**status**: 服务状态:
* not_started - 未开始
* running - 运行中
* done - 已完成

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "app_id": 0,
      "app_name": "string",
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "current": 0,
      "days": 0,
      "deadline": 0,
      "id": "string",
      "latest_reflow_time": 0,
      "limit": 0,
      "name": "string",
      "status": "string",
      "tasks": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "uploaded_count": 0
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_eventreflowjobs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.EventReflowJobList](#schemamodels.eventreflowjoblist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_eventReflowJobs

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/eventReflowJobs \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/inflet/v1/eventReflowJobs HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "app_id": 0,
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 1,
  "limit": 100,
  "name": "string",
  "task_ids": [
    0
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/inflet/v1/eventReflowJobs',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/inflet/v1/eventReflowJobs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/inflet/v1/eventReflowJobs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/eventReflowJobs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/eventReflowJobs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/eventReflowJobs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/eventReflowJobs`

*创建事件回流任务*

创建事件回流任务

> Body parameter

```json
{
  "app_id": 0,
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 1,
  "limit": 100,
  "name": "string",
  "task_ids": [
    0
  ]
}
```

<h3 id="post__v1_eventreflowjobs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[models.CreateEventReflowJobParams](#schemamodels.createeventreflowjobparams)|true|创建参数|

> Example responses

> 200 Response

```json
{
  "app_id": 0,
  "app_name": "string",
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "current": 0,
  "days": 0,
  "deadline": 0,
  "id": "string",
  "latest_reflow_time": 0,
  "limit": 0,
  "name": "string",
  "status": "string",
  "tasks": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "uploaded_count": 0
}
```

<h3 id="post__v1_eventreflowjobs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.EventReflowJob](#schemamodels.eventreflowjob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_eventReflowJobs_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/eventReflowJobs/{id} \
  -H 'Accept: application/json'

```

```http
GET /api/inflet/v1/eventReflowJobs/{id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/eventReflowJobs/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/inflet/v1/eventReflowJobs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/inflet/v1/eventReflowJobs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/eventReflowJobs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/eventReflowJobs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/eventReflowJobs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/eventReflowJobs/{id}`

*获取事件回流任务*

获取事件回流任务

<h3 id="get__v1_eventreflowjobs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|事件回流任务ID|

> Example responses

> 200 Response

```json
{
  "app_id": 0,
  "app_name": "string",
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "current": 0,
  "days": 0,
  "deadline": 0,
  "id": "string",
  "latest_reflow_time": 0,
  "limit": 0,
  "name": "string",
  "status": "string",
  "tasks": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "uploaded_count": 0
}
```

<h3 id="get__v1_eventreflowjobs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.EventReflowJob](#schemamodels.eventreflowjob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|未找到|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_eventReflowJobs_{id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/eventReflowJobs/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /api/inflet/v1/eventReflowJobs/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 0,
  "limit": 0,
  "name": "string",
  "task_ids": [
    0
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/inflet/v1/eventReflowJobs/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/api/inflet/v1/eventReflowJobs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/inflet/v1/eventReflowJobs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/eventReflowJobs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/eventReflowJobs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/eventReflowJobs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/eventReflowJobs/{id}`

*更新事件回流任务*

更新事件回流任务

> Body parameter

```json
{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 0,
  "limit": 0,
  "name": "string",
  "task_ids": [
    0
  ]
}
```

<h3 id="put__v1_eventreflowjobs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|事件回流任务ID|
|body|body|[models.UpdateEventReflowJobParams](#schemamodels.updateeventreflowjobparams)|true|更新参数|

> Example responses

> 200 Response

```json
{
  "app_id": 0,
  "app_name": "string",
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "current": 0,
  "days": 0,
  "deadline": 0,
  "id": "string",
  "latest_reflow_time": 0,
  "limit": 0,
  "name": "string",
  "status": "string",
  "tasks": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "uploaded_count": 0
}
```

<h3 id="put__v1_eventreflowjobs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.EventReflowJob](#schemamodels.eventreflowjob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_eventReflowJobs_{id}

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/eventReflowJobs/{id} \
  -H 'Accept: application/json'

```

```http
DELETE /api/inflet/v1/eventReflowJobs/{id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/eventReflowJobs/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/api/inflet/v1/eventReflowJobs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/api/inflet/v1/eventReflowJobs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/eventReflowJobs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/eventReflowJobs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/eventReflowJobs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/eventReflowJobs/{id}`

*删除事件回流任务*

删除事件回流任务

<h3 id="delete__v1_eventreflowjobs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|事件回流任务ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="delete__v1_eventreflowjobs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_eventReflowJobs_{id}_start

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/eventReflowJobs/{id}/start \
  -H 'Accept: application/json'

```

```http
POST /api/inflet/v1/eventReflowJobs/{id}/start HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/eventReflowJobs/{id}/start',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post '/api/inflet/v1/eventReflowJobs/{id}/start',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/api/inflet/v1/eventReflowJobs/{id}/start', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/eventReflowJobs/{id}/start', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/eventReflowJobs/{id}/start");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/eventReflowJobs/{id}/start", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/eventReflowJobs/{id}/start`

*启动事件回流任务*

启动事件回流任务

<h3 id="post__v1_eventreflowjobs_{id}_start-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|事件回流任务ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_eventreflowjobs_{id}_start-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_eventReflowJobs_{id}_stop

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/eventReflowJobs/{id}/stop \
  -H 'Accept: application/json'

```

```http
PUT /api/inflet/v1/eventReflowJobs/{id}/stop HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/eventReflowJobs/{id}/stop',
{
  method: 'PUT',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.put '/api/inflet/v1/eventReflowJobs/{id}/stop',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.put('/api/inflet/v1/eventReflowJobs/{id}/stop', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/eventReflowJobs/{id}/stop', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/eventReflowJobs/{id}/stop");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/eventReflowJobs/{id}/stop", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/eventReflowJobs/{id}/stop`

*停止事件回流任务*

停止事件回流任务

<h3 id="put__v1_eventreflowjobs_{id}_stop-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|事件回流任务ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="put__v1_eventreflowjobs_{id}_stop-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-events">events</h1>

## get__v1_events

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/events \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/events HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/events',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/events',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/events', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/events', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/events");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/events", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/events`

*事件列表*

事件列表

<h3 id="get__v1_events-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|app_id|query|integer|false|算法应用ID|
|end|query|integer|false|结束时间|
|monitor_config_id|query|integer|false|监控配置ID|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|source_id|query|string|false|数据源ID|
|start|query|integer|false|起始时间|
|status|query|integer|false|状态|
|task_id|query|integer|false|任务ID|

#### Detailed descriptions

**status**: 状态
- 0: 未处理
- 1: 有效
- 2: 误报

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_id": 0,
      "app_name": "string",
      "created": 0,
      "id": "string",
      "is_reported": 0,
      "meta_url": "string",
      "preview_url": "string",
      "reason": "string",
      "source_id": "string",
      "source_name": "string",
      "status": 0,
      "task_id": 0,
      "task_name": "string",
      "thumb_url": "string",
      "video_url": "string"
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_events-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.EventList](#schemamodels.eventlist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_events_download

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/events/download \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/events/download HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "app_id": 0,
  "end": 0,
  "id": [
    "string"
  ],
  "monitor_config_id": 0,
  "order": "string",
  "order_by": "string",
  "page": 0,
  "page_size": 0,
  "source_id": "string",
  "start": 0,
  "status": 0,
  "task_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/events/download',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/events/download',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/events/download', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/events/download', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/events/download");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/events/download", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/events/download`

*下载事件*

下载事件

> Body parameter

```json
{
  "app_id": 0,
  "end": 0,
  "id": [
    "string"
  ],
  "monitor_config_id": 0,
  "order": "string",
  "order_by": "string",
  "page": 0,
  "page_size": 0,
  "source_id": "string",
  "start": 0,
  "status": 0,
  "task_id": 0
}
```

<h3 id="post__v1_events_download-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.DownloadEventsReq](#schemamodels.downloadeventsreq)|true|选择下载的事件ID列表, 列表为空时下载全部事件|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_events_download-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_events_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/events/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/events/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/events/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/events/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/events/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/events/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/events/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/events/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/events/{id}`

*事件详情*

事件详情

<h3 id="get__v1_events_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|事件ID|

> Example responses

> 200 Response

```json
{
  "alarm_effect": {
    "content": "string",
    "duration": "string",
    "enable": true
  },
  "app_id": 0,
  "app_name": "string",
  "created": 0,
  "id": "string",
  "is_reported": 0,
  "meta_url": "string",
  "preview_url": "string",
  "reason": "string",
  "source_id": "string",
  "source_name": "string",
  "status": 0,
  "task_id": 0,
  "task_name": "string",
  "thumb_url": "string",
  "video_url": "string"
}
```

<h3 id="get__v1_events_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Event](#schemamodels.event)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_events_{id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/events/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/events/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "status": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/events/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/events/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/events/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/events/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/events/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/events/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/events/{id}`

*更新事件*

更新事件

> Body parameter

```json
{
  "status": 0
}
```

<h3 id="put__v1_events_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|事件ID|
|body|body|[models.UpdateEventReq](#schemamodels.updateeventreq)|true|事件信息|

> Example responses

> 200 Response

```json
{
  "alarm_effect": {
    "content": "string",
    "duration": "string",
    "enable": true
  },
  "app_id": 0,
  "app_name": "string",
  "created": 0,
  "id": "string",
  "is_reported": 0,
  "meta_url": "string",
  "preview_url": "string",
  "reason": "string",
  "source_id": "string",
  "source_name": "string",
  "status": 0,
  "task_id": 0,
  "task_name": "string",
  "thumb_url": "string",
  "video_url": "string"
}
```

<h3 id="put__v1_events_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Event](#schemamodels.event)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_events_{id}

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/events/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
DELETE /api/inflet/v1/events/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/events/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.delete '/api/inflet/v1/events/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.delete('/api/inflet/v1/events/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/events/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/events/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/events/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/events/{id}`

*删除事件*

删除事件

<h3 id="delete__v1_events_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|事件ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="delete__v1_events_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_events_{id}_next

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/events/{id}/next \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/events/{id}/next HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/events/{id}/next',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/events/{id}/next',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/events/{id}/next', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/events/{id}/next', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/events/{id}/next");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/events/{id}/next", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/events/{id}/next`

*下一个事件*

下一个事件

<h3 id="get__v1_events_{id}_next-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|事件ID|
|app_id|query|integer|false|算法应用ID|
|end|query|integer|false|结束时间|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|source_id|query|string|false|数据源ID|
|start|query|integer|false|起始时间|
|status|query|integer|false|状态|
|task_id|query|integer|false|任务ID|

#### Detailed descriptions

**status**: 状态
- 0: 未处理
- 1: 有效
- 2: 误报

> Example responses

> 200 Response

```json
{
  "alarm_effect": {
    "content": "string",
    "duration": "string",
    "enable": true
  },
  "app_id": 0,
  "app_name": "string",
  "created": 0,
  "id": "string",
  "is_reported": 0,
  "meta_url": "string",
  "preview_url": "string",
  "reason": "string",
  "source_id": "string",
  "source_name": "string",
  "status": 0,
  "task_id": 0,
  "task_name": "string",
  "thumb_url": "string",
  "video_url": "string"
}
```

<h3 id="get__v1_events_{id}_next-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Event](#schemamodels.event)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_events_{id}_prev

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/events/{id}/prev \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/events/{id}/prev HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/events/{id}/prev',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/events/{id}/prev',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/events/{id}/prev', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/events/{id}/prev', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/events/{id}/prev");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/events/{id}/prev", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/events/{id}/prev`

*上一个事件*

上一个事件

<h3 id="get__v1_events_{id}_prev-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|事件ID|
|app_id|query|integer|false|算法应用ID|
|end|query|integer|false|结束时间|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|source_id|query|string|false|数据源ID|
|start|query|integer|false|起始时间|
|status|query|integer|false|状态|
|task_id|query|integer|false|任务ID|

#### Detailed descriptions

**status**: 状态
- 0: 未处理
- 1: 有效
- 2: 误报

> Example responses

> 200 Response

```json
{
  "alarm_effect": {
    "content": "string",
    "duration": "string",
    "enable": true
  },
  "app_id": 0,
  "app_name": "string",
  "created": 0,
  "id": "string",
  "is_reported": 0,
  "meta_url": "string",
  "preview_url": "string",
  "reason": "string",
  "source_id": "string",
  "source_name": "string",
  "status": 0,
  "task_id": 0,
  "task_name": "string",
  "thumb_url": "string",
  "video_url": "string"
}
```

<h3 id="get__v1_events_{id}_prev-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Event](#schemamodels.event)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-featurelibs">featurelibs</h1>

## get__v1_featurelibs

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/featurelibs \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/featurelibs HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/featurelibs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/featurelibs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/featurelibs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/featurelibs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/featurelibs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/featurelibs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/featurelibs`

*特征库列表*

特征库列表

<h3 id="get__v1_featurelibs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|name|query|string|false|名称|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|parent_id|query|integer|false|父特征库ID|
|state|query|integer|false|提取状态：|

#### Detailed descriptions

**state**: 提取状态：
* 0 - 全部
* 1 - 进行中
* 2 - 已完成
* 3 - 失败

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "app_id": 0,
      "created_at": 0,
      "extracted_image_count": 0,
      "failed_count": 0,
      "id": 0,
      "image_count": 0,
      "name": "string",
      "support_sub_feature_lib": true,
      "updated_at": 0
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_featurelibs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.FeatureLibList](#schemamodels.featureliblist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_featurelibs

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/featurelibs \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/featurelibs HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "app_id": 0,
  "description": "string",
  "name": "string",
  "parent_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/featurelibs',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/featurelibs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/featurelibs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/featurelibs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/featurelibs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/featurelibs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/featurelibs`

*创建特征库*

创建特征库

> Body parameter

```json
{
  "app_id": 0,
  "description": "string",
  "name": "string",
  "parent_id": 0
}
```

<h3 id="post__v1_featurelibs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.CreateFeatureLibReq](#schemamodels.createfeaturelibreq)|true|特征库信息|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_featurelibs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_featurelibs_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/featurelibs/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/featurelibs/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/featurelibs/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/featurelibs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/featurelibs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/featurelibs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/featurelibs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/featurelibs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/featurelibs/{id}`

*特征库详情*

特征库详情

<h3 id="get__v1_featurelibs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|特征库ID|

> Example responses

> 200 Response

```json
{
  "app_id": 0,
  "created_at": 0,
  "extracted_image_count": 0,
  "failed_count": 0,
  "id": 0,
  "image_count": 0,
  "name": "string",
  "support_sub_feature_lib": true,
  "updated_at": 0
}
```

<h3 id="get__v1_featurelibs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.FeatureLib](#schemamodels.featurelib)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_featurelibs_{id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/featurelibs/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/featurelibs/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "app_id": 0,
  "created_at": 0,
  "extracted_image_count": 0,
  "failed_count": 0,
  "id": 0,
  "image_count": 0,
  "name": "string",
  "support_sub_feature_lib": true,
  "updated_at": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/featurelibs/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/featurelibs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/featurelibs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/featurelibs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/featurelibs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/featurelibs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/featurelibs/{id}`

*更新特征库*

更新特征库

> Body parameter

```json
{
  "app_id": 0,
  "created_at": 0,
  "extracted_image_count": 0,
  "failed_count": 0,
  "id": 0,
  "image_count": 0,
  "name": "string",
  "support_sub_feature_lib": true,
  "updated_at": 0
}
```

<h3 id="put__v1_featurelibs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|特征库ID|
|body|body|[models.FeatureLib](#schemamodels.featurelib)|true|特征库信息|

> Example responses

> 200 Response

```json
{}
```

<h3 id="put__v1_featurelibs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_featurelibs_{id}

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/featurelibs/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
DELETE /api/inflet/v1/featurelibs/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/featurelibs/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.delete '/api/inflet/v1/featurelibs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.delete('/api/inflet/v1/featurelibs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/featurelibs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/featurelibs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/featurelibs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/featurelibs/{id}`

*删除特征库*

删除特征库

<h3 id="delete__v1_featurelibs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|特征库ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="delete__v1_featurelibs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_featurelibs_{id}_import

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/featurelibs/{id}/import \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/featurelibs/{id}/import HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "files": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/featurelibs/{id}/import',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/featurelibs/{id}/import',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/featurelibs/{id}/import', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/featurelibs/{id}/import', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/featurelibs/{id}/import");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/featurelibs/{id}/import", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/featurelibs/{id}/import`

*导入特征库*

导入特征库

> Body parameter

```yaml
files: string

```

<h3 id="post__v1_featurelibs_{id}_import-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|特征库ID|
|body|body|object|true|none|
|» files|body|string(binary)|true|特征库文件|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_featurelibs_{id}_import-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_featurelibs_{id}_items

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/featurelibs/{id}/items \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/featurelibs/{id}/items HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/featurelibs/{id}/items',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/featurelibs/{id}/items',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/featurelibs/{id}/items', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/featurelibs/{id}/items', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/featurelibs/{id}/items");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/featurelibs/{id}/items", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/featurelibs/{id}/items`

*获取特征项列表*

获取特征项列表

<h3 id="get__v1_featurelibs_{id}_items-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|特征库ID|
|name|query|string|false|名称|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|state|query|integer|false|状态, 1: 未提取, 2: 提取中, 3: 提取完成, 4: 提取失败|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "created_at": 0,
      "error": "string",
      "feature_lib_id": 0,
      "id": 0,
      "image_url": "string",
      "name": "string",
      "render": null,
      "state": 0
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_featurelibs_{id}_items-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.FeatureLibItemList](#schemamodels.featurelibitemlist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_featurelibs_{id}_items_{item_id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/featurelibs/{id}/items/{item_id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/featurelibs/{id}/items/{item_id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/featurelibs/{id}/items/{item_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/featurelibs/{id}/items/{item_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/featurelibs/{id}/items/{item_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/featurelibs/{id}/items/{item_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/featurelibs/{id}/items/{item_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/featurelibs/{id}/items/{item_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/featurelibs/{id}/items/{item_id}`

*获取特征项详情*

获取特征项详情

<h3 id="get__v1_featurelibs_{id}_items_{item_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|特征库ID|
|item_id|path|integer|true|特征项ID|

> Example responses

> 200 Response

```json
{
  "created_at": 0,
  "error": "string",
  "feature_lib_id": 0,
  "id": 0,
  "image_url": "string",
  "name": "string",
  "render": null,
  "state": 0
}
```

<h3 id="get__v1_featurelibs_{id}_items_{item_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.FeatureLibItem](#schemamodels.featurelibitem)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_featurelibs_{id}_items_{item_id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/featurelibs/{id}/items/{item_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/featurelibs/{id}/items/{item_id} HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/featurelibs/{id}/items/{item_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/featurelibs/{id}/items/{item_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/featurelibs/{id}/items/{item_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/featurelibs/{id}/items/{item_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/featurelibs/{id}/items/{item_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/featurelibs/{id}/items/{item_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/featurelibs/{id}/items/{item_id}`

*更新特征项*

更新特征项

> Body parameter

```json
{
  "name": "string"
}
```

<h3 id="put__v1_featurelibs_{id}_items_{item_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|特征库ID|
|item_id|path|integer|true|特征项ID|
|body|body|[models.UpdateFeatureItemReq](#schemamodels.updatefeatureitemreq)|true|特征项信息|

> Example responses

> 200 Response

```json
{
  "created_at": 0,
  "error": "string",
  "feature_lib_id": 0,
  "id": 0,
  "image_url": "string",
  "name": "string",
  "render": null,
  "state": 0
}
```

<h3 id="put__v1_featurelibs_{id}_items_{item_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.FeatureLibItem](#schemamodels.featurelibitem)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_featurelibs_{id}_items_{item_id}

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/featurelibs/{id}/items/{item_id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
DELETE /api/inflet/v1/featurelibs/{id}/items/{item_id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/featurelibs/{id}/items/{item_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.delete '/api/inflet/v1/featurelibs/{id}/items/{item_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.delete('/api/inflet/v1/featurelibs/{id}/items/{item_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/featurelibs/{id}/items/{item_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/featurelibs/{id}/items/{item_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/featurelibs/{id}/items/{item_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/featurelibs/{id}/items/{item_id}`

*删除特征项详情*

删除特征项详情

<h3 id="delete__v1_featurelibs_{id}_items_{item_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|特征库ID|
|item_id|path|integer|true|特征项ID|

> Example responses

> 200 Response

```json
{
  "created_at": 0,
  "error": "string",
  "feature_lib_id": 0,
  "id": 0,
  "image_url": "string",
  "name": "string",
  "render": null,
  "state": 0
}
```

<h3 id="delete__v1_featurelibs_{id}_items_{item_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.FeatureLibItem](#schemamodels.featurelibitem)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-auth">auth</h1>

## post__v1_login

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/login \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/inflet/v1/login HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "password": "string",
  "username": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/inflet/v1/login',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/inflet/v1/login',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/inflet/v1/login', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/login', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/login");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/login", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/login`

*登录*

登录

> Body parameter

```json
{
  "password": "string",
  "username": "string"
}
```

<h3 id="post__v1_login-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[models.LoginReq](#schemamodels.loginreq)|true|body参数|

> Example responses

> 200 Response

```json
{
  "token": "string",
  "user": {
    "id": 0,
    "menus": [
      "dashboard"
    ],
    "name": "string",
    "role": "admin"
  }
}
```

<h3 id="post__v1_login-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.LoginResp](#schemamodels.loginresp)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-metrics">metrics</h1>

## get__v1_metrics_camera

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/metrics/camera \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/metrics/camera HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/metrics/camera',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/metrics/camera',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/metrics/camera', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/metrics/camera', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/metrics/camera");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/metrics/camera", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/metrics/camera`

*摄像机状态监控*

摄像机状态监控

<h3 id="get__v1_metrics_camera-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "code_stream_abnormal": 0,
  "offline": 0,
  "online": 0,
  "total": 0
}
```

<h3 id="get__v1_metrics_camera-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.CameraMetrics](#schemamodels.camerametrics)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_metrics_disk

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/metrics/disk \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/metrics/disk HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/metrics/disk',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/metrics/disk',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/metrics/disk', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/metrics/disk', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/metrics/disk");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/metrics/disk", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/metrics/disk`

*磁盘空间监控*

磁盘空间监控

<h3 id="get__v1_metrics_disk-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
[
  {
    "app_used_disk_space": 0,
    "event_used_disk_space": 0,
    "total_disk_space": 0,
    "used_disk_space": 0
  }
]
```

<h3 id="get__v1_metrics_disk-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<h3 id="get__v1_metrics_disk-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[models.DiskMetrics](#schemamodels.diskmetrics)]|false|none|none|
|» app_used_disk_space|integer|false|none|下发应用使用磁盘空间|
|» event_used_disk_space|integer|false|none|事件存储使用磁盘空间|
|» total_disk_space|integer|false|none|磁盘总空间|
|» used_disk_space|integer|false|none|已使用磁盘空间|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_metrics_system

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/metrics/system \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/metrics/system HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/metrics/system',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/metrics/system',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/metrics/system', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/metrics/system', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/metrics/system");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/metrics/system", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/metrics/system`

*系统资源状态监控*

系统资源状态监控

<h3 id="get__v1_metrics_system-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
[
  {
    "cpu_temperature": 0,
    "cpu_usage": 0,
    "gpu_mem_usage": 0,
    "gpu_temperature": 0,
    "gpu_usage": 0,
    "mem_usage": 0
  }
]
```

<h3 id="get__v1_metrics_system-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<h3 id="get__v1_metrics_system-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[models.SystemResourceMetrics](#schemamodels.systemresourcemetrics)]|false|none|none|
|» cpu_temperature|integer|false|none|CPU温度|
|» cpu_usage|integer|false|none|CPU使用率|
|» gpu_mem_usage|integer|false|none|GPU内存使用率|
|» gpu_temperature|integer|false|none|GPU温度|
|» gpu_usage|integer|false|none|GPU使用率|
|» mem_usage|integer|false|none|内存使用率|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_metrics_task

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/metrics/task \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/metrics/task HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/metrics/task',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/metrics/task',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/metrics/task', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/metrics/task', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/metrics/task");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/metrics/task", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/metrics/task`

*任务状态监控*

任务状态监控

<h3 id="get__v1_metrics_task-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "failed": 0,
  "finished": 0,
  "not_started": 0,
  "pending": 0,
  "running": 0,
  "total": 0
}
```

<h3 id="get__v1_metrics_task-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.TaskMetrics](#schemamodels.taskmetrics)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-monitorconfigs">monitorconfigs</h1>

## get__v1_monitorConfig_sync

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/monitorConfig/sync \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/monitorConfig/sync HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/monitorConfig/sync',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/monitorConfig/sync',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/monitorConfig/sync', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/monitorConfig/sync', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/monitorConfig/sync");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/monitorConfig/sync", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/monitorConfig/sync`

*订阅实时监控配置*

订阅实时监控配置(http to websocket) {"type":"PING","payload":""}->{"type":"PING","payload":"PONG"}, {}->{"type":"PREVIEW_CONFIG","payload":"<monitor config>"},{"type":"EVENT","payload":"<event>"}, {"type":"CONF_CHANGE","payload":"id"}->{"type":"PREVIEW_CONFIG","payload":""} {"type":"CONF_UPDATE","payload":"<monitor config>"}->{"type":"PREVIEW_CONFIG","payload":"<monitor config>"}

<h3 id="get__v1_monitorconfig_sync-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|实时监控配置ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="get__v1_monitorconfig_sync-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_monitorConfigs

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/monitorConfigs \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/monitorConfigs HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/monitorConfigs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/monitorConfigs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/monitorConfigs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/monitorConfigs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/monitorConfigs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/monitorConfigs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/monitorConfigs`

*实时监控配置列表*

实时监控配置列表

<h3 id="get__v1_monitorconfigs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|name|query|string|false|名称|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "grid": "string",
      "id": 0,
      "name": "string",
      "positions": {
        "property1": {
          "current_instance_id": "string",
          "id": "string",
          "instances": [
            {
              "app_name": "string",
              "fps": 0,
              "id": "string"
            }
          ],
          "source_name": "string",
          "task_name": "string"
        },
        "property2": {
          "current_instance_id": "string",
          "id": "string",
          "instances": [
            {
              "app_name": "string",
              "fps": 0,
              "id": "string"
            }
          ],
          "source_name": "string",
          "task_name": "string"
        }
      }
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_monitorconfigs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.MonitorConfigList](#schemamodels.monitorconfiglist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_monitorConfigs

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/monitorConfigs \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/monitorConfigs HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "grid": "string",
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/monitorConfigs',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/monitorConfigs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/monitorConfigs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/monitorConfigs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/monitorConfigs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/monitorConfigs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/monitorConfigs`

*创建实时监控配置*

创建实时监控配置

> Body parameter

```json
{
  "grid": "string",
  "name": "string"
}
```

<h3 id="post__v1_monitorconfigs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.CreateMonitorConfigRequest](#schemamodels.createmonitorconfigrequest)|true|请求参数|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_monitorconfigs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_monitorConfigs_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/monitorConfigs/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/monitorConfigs/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/monitorConfigs/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/monitorConfigs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/monitorConfigs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/monitorConfigs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/monitorConfigs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/monitorConfigs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/monitorConfigs/{id}`

*实时监控配置详情*

实时监控配置详情

<h3 id="get__v1_monitorconfigs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|实时监控配置ID|

> Example responses

> 200 Response

```json
{
  "grid": "string",
  "id": 0,
  "name": "string",
  "positions": {
    "property1": {
      "current_instance_id": "string",
      "id": "string",
      "instances": [
        {
          "app_name": "string",
          "fps": 0,
          "id": "string"
        }
      ],
      "source_name": "string",
      "task_name": "string"
    },
    "property2": {
      "current_instance_id": "string",
      "id": "string",
      "instances": [
        {
          "app_name": "string",
          "fps": 0,
          "id": "string"
        }
      ],
      "source_name": "string",
      "task_name": "string"
    }
  }
}
```

<h3 id="get__v1_monitorconfigs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.MonitorConfig](#schemamodels.monitorconfig)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_monitorConfigs_{id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/monitorConfigs/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/monitorConfigs/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "grid": "string",
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/monitorConfigs/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/monitorConfigs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/monitorConfigs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/monitorConfigs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/monitorConfigs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/monitorConfigs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/monitorConfigs/{id}`

*更新实时监控配置*

更新实时监控配置

> Body parameter

```json
{
  "grid": "string",
  "name": "string"
}
```

<h3 id="put__v1_monitorconfigs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|实时监控配置ID|
|body|body|[models.CreateMonitorConfigRequest](#schemamodels.createmonitorconfigrequest)|true|请求参数|

> Example responses

> 200 Response

```json
{}
```

<h3 id="put__v1_monitorconfigs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_monitorConfigs_{id}

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/monitorConfigs/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
DELETE /api/inflet/v1/monitorConfigs/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/monitorConfigs/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.delete '/api/inflet/v1/monitorConfigs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.delete('/api/inflet/v1/monitorConfigs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/monitorConfigs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/monitorConfigs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/monitorConfigs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/monitorConfigs/{id}`

*删除实时监控配置*

删除实时监控配置

<h3 id="delete__v1_monitorconfigs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|实时监控配置ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="delete__v1_monitorconfigs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-rawdatareflowjob">RawDataReflowJob</h1>

## get__v1_rawDataReflowJobs

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/rawDataReflowJobs \
  -H 'Accept: application/json'

```

```http
GET /api/inflet/v1/rawDataReflowJobs HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/rawDataReflowJobs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/inflet/v1/rawDataReflowJobs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/inflet/v1/rawDataReflowJobs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/rawDataReflowJobs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/rawDataReflowJobs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/rawDataReflowJobs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/rawDataReflowJobs`

*原始数据回流任务列表*

原始数据回流任务列表

<h3 id="get__v1_rawdatareflowjobs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|query|string|false|none|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|source_id|query|string|false|输入源名称|
|status|query|string|false|任务状态:|
|userID|query|integer|false|用户ID|

#### Detailed descriptions

**status**: 任务状态:
* not_started - 未开始
* running - 运行中
* done - 已完成

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "current": 0,
      "days": 0,
      "deadline": 0,
      "id": "string",
      "interval": "string",
      "latest_reflow_time": 0,
      "limit": 0,
      "name": "string",
      "source_id": "string",
      "source_name": "string",
      "status": "string",
      "uploaded_count": 0
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_rawdatareflowjobs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.RawDataReflowJobList](#schemamodels.rawdatareflowjoblist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_rawDataReflowJobs

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/rawDataReflowJobs \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/inflet/v1/rawDataReflowJobs HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 1,
  "interval": "string",
  "limit": 100,
  "name": "string",
  "source_id": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/inflet/v1/rawDataReflowJobs',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/inflet/v1/rawDataReflowJobs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/inflet/v1/rawDataReflowJobs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/rawDataReflowJobs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/rawDataReflowJobs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/rawDataReflowJobs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/rawDataReflowJobs`

*创建原始数据回流任务*

创建原始数据回流任务

> Body parameter

```json
{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 1,
  "interval": "string",
  "limit": 100,
  "name": "string",
  "source_id": "string"
}
```

<h3 id="post__v1_rawdatareflowjobs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[models.CreateRawDataReflowJobParams](#schemamodels.createrawdatareflowjobparams)|true|body参数|

> Example responses

> 200 Response

```json
{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "current": 0,
  "days": 0,
  "deadline": 0,
  "id": "string",
  "interval": "string",
  "latest_reflow_time": 0,
  "limit": 0,
  "name": "string",
  "source_id": "string",
  "source_name": "string",
  "status": "string",
  "uploaded_count": 0
}
```

<h3 id="post__v1_rawdatareflowjobs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.RawDataReflowJob](#schemamodels.rawdatareflowjob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_rawDataReflowJobs_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/rawDataReflowJobs/{id} \
  -H 'Accept: application/json'

```

```http
GET /api/inflet/v1/rawDataReflowJobs/{id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/rawDataReflowJobs/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/inflet/v1/rawDataReflowJobs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/inflet/v1/rawDataReflowJobs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/rawDataReflowJobs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/rawDataReflowJobs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/rawDataReflowJobs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/rawDataReflowJobs/{id}`

*获取原始数据回流任务*

获取原始数据回流任务

<h3 id="get__v1_rawdatareflowjobs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|原始数据回流任务ID|

> Example responses

> 200 Response

```json
{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "current": 0,
  "days": 0,
  "deadline": 0,
  "id": "string",
  "interval": "string",
  "latest_reflow_time": 0,
  "limit": 0,
  "name": "string",
  "source_id": "string",
  "source_name": "string",
  "status": "string",
  "uploaded_count": 0
}
```

<h3 id="get__v1_rawdatareflowjobs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.RawDataReflowJob](#schemamodels.rawdatareflowjob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|未找到|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_rawDataReflowJobs_{id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/rawDataReflowJobs/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /api/inflet/v1/rawDataReflowJobs/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 0,
  "interval": "string",
  "limit": 0,
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/inflet/v1/rawDataReflowJobs/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/api/inflet/v1/rawDataReflowJobs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/inflet/v1/rawDataReflowJobs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/rawDataReflowJobs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/rawDataReflowJobs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/rawDataReflowJobs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/rawDataReflowJobs/{id}`

*更新原始数据回流任务*

更新原始数据回流任务

> Body parameter

```json
{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 0,
  "interval": "string",
  "limit": 0,
  "name": "string"
}
```

<h3 id="put__v1_rawdatareflowjobs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|原始数据回流任务ID|
|body|body|[models.UpdateRawDataReflowJobParams](#schemamodels.updaterawdatareflowjobparams)|true|body参数|

> Example responses

> 200 Response

```json
{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "current": 0,
  "days": 0,
  "deadline": 0,
  "id": "string",
  "interval": "string",
  "latest_reflow_time": 0,
  "limit": 0,
  "name": "string",
  "source_id": "string",
  "source_name": "string",
  "status": "string",
  "uploaded_count": 0
}
```

<h3 id="put__v1_rawdatareflowjobs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.RawDataReflowJob](#schemamodels.rawdatareflowjob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_rawDataReflowJobs_{id}

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/rawDataReflowJobs/{id} \
  -H 'Accept: application/json'

```

```http
DELETE /api/inflet/v1/rawDataReflowJobs/{id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/rawDataReflowJobs/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/api/inflet/v1/rawDataReflowJobs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/api/inflet/v1/rawDataReflowJobs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/rawDataReflowJobs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/rawDataReflowJobs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/rawDataReflowJobs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/rawDataReflowJobs/{id}`

*删除原始数据回流任务*

删除原始数据回流任务

<h3 id="delete__v1_rawdatareflowjobs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|原始数据回流任务ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="delete__v1_rawdatareflowjobs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_rawDataReflowJobs_{id}_start

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/rawDataReflowJobs/{id}/start \
  -H 'Accept: application/json'

```

```http
POST /api/inflet/v1/rawDataReflowJobs/{id}/start HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/rawDataReflowJobs/{id}/start',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post '/api/inflet/v1/rawDataReflowJobs/{id}/start',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/api/inflet/v1/rawDataReflowJobs/{id}/start', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/rawDataReflowJobs/{id}/start', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/rawDataReflowJobs/{id}/start");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/rawDataReflowJobs/{id}/start", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/rawDataReflowJobs/{id}/start`

*启动原始数据回流任务*

启动原始数据回流任务

<h3 id="post__v1_rawdatareflowjobs_{id}_start-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|原始数据回流任务ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_rawdatareflowjobs_{id}_start-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_rawDataReflowJobs_{id}_stop

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/rawDataReflowJobs/{id}/stop \
  -H 'Accept: application/json'

```

```http
PUT /api/inflet/v1/rawDataReflowJobs/{id}/stop HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/rawDataReflowJobs/{id}/stop',
{
  method: 'PUT',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.put '/api/inflet/v1/rawDataReflowJobs/{id}/stop',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.put('/api/inflet/v1/rawDataReflowJobs/{id}/stop', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/rawDataReflowJobs/{id}/stop', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/rawDataReflowJobs/{id}/stop");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/rawDataReflowJobs/{id}/stop", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/rawDataReflowJobs/{id}/stop`

*停止原始数据回流任务*

停止原始数据回流任务

<h3 id="put__v1_rawdatareflowjobs_{id}_stop-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|原始数据回流任务ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="put__v1_rawdatareflowjobs_{id}_stop-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-smart_tuning_jobs">smart_tuning_jobs</h1>

## get__v1_smart_tuning_jobs

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/smart_tuning_jobs \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/smart_tuning_jobs HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/smart_tuning_jobs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/smart_tuning_jobs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/smart_tuning_jobs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/smart_tuning_jobs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/smart_tuning_jobs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/smart_tuning_jobs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/smart_tuning_jobs`

*获取智能调参任务列表*

获取智能调参任务列表

<h3 id="get__v1_smart_tuning_jobs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|detail|query|boolean|false|none|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|state|query|array[string]|false|状态：|

#### Detailed descriptions

**state**: 状态：
* None - 当前任务不支持智能调参
* Available - 当前任务可以智能调参
* Configured - 当前任务已配置智能调参
* Ready - 当前任务智能调参已准备好,可以开始
* Running - 当前任务智能调参正在运行
* Finished - 当前任务智能调参已完成

#### Enumerated Values

|Parameter|Value|
|---|---|
|state|None|
|state|Available|
|state|Configured|
|state|Ready|
|state|Running|
|state|Finished|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "app_id": 0,
      "app_name": "string",
      "fp_count": 0,
      "instance_id": "string",
      "labeled_count": 0,
      "name": "string",
      "progress": 0,
      "report_url": "string",
      "state": "None",
      "task_id": 0,
      "task_name": "string",
      "total_count": 0,
      "tp_count": 0
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_smart_tuning_jobs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.SmartTuningJobList](#schemamodels.smarttuningjoblist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_smart_tuning_jobs_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/smart_tuning_jobs/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/smart_tuning_jobs/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/smart_tuning_jobs/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/smart_tuning_jobs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/smart_tuning_jobs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/smart_tuning_jobs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/smart_tuning_jobs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/smart_tuning_jobs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/smart_tuning_jobs/{id}`

*获取智能调参任务*

获取智能调参任务

<h3 id="get__v1_smart_tuning_jobs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|任务ID|

> Example responses

> 200 Response

```json
{
  "app_id": 0,
  "app_name": "string",
  "fp_count": 0,
  "instance_id": "string",
  "labeled_count": 0,
  "name": "string",
  "progress": 0,
  "report_url": "string",
  "state": "None",
  "task_id": 0,
  "task_name": "string",
  "total_count": 0,
  "tp_count": 0
}
```

<h3 id="get__v1_smart_tuning_jobs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.SmartTuningJob](#schemamodels.smarttuningjob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_smart_tuning_jobs_{id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/smart_tuning_jobs/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/smart_tuning_jobs/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "st_action": "Configure"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/smart_tuning_jobs/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/smart_tuning_jobs/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/smart_tuning_jobs/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/smart_tuning_jobs/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/smart_tuning_jobs/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/smart_tuning_jobs/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/smart_tuning_jobs/{id}`

*更新智能调参任务*

更新智能调参任务

> Body parameter

```json
{
  "st_action": "Configure"
}
```

<h3 id="put__v1_smart_tuning_jobs_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|任务ID|
|body|body|[models.UpdateSmartTuningJobReq](#schemamodels.updatesmarttuningjobreq)|true|请求体|

> Example responses

> 200 Response

```json
{
  "app_id": 0,
  "app_name": "string",
  "fp_count": 0,
  "instance_id": "string",
  "labeled_count": 0,
  "name": "string",
  "progress": 0,
  "report_url": "string",
  "state": "None",
  "task_id": 0,
  "task_name": "string",
  "total_count": 0,
  "tp_count": 0
}
```

<h3 id="put__v1_smart_tuning_jobs_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.SmartTuningJob](#schemamodels.smarttuningjob)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_smart_tuning_jobs_{id}_events

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/smart_tuning_jobs/{id}/events \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/smart_tuning_jobs/{id}/events HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/smart_tuning_jobs/{id}/events',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/smart_tuning_jobs/{id}/events',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/smart_tuning_jobs/{id}/events', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/smart_tuning_jobs/{id}/events', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/smart_tuning_jobs/{id}/events");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/smart_tuning_jobs/{id}/events", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/smart_tuning_jobs/{id}/events`

*获取智能调参任务事件列表*

获取智能调参任务事件列表

<h3 id="get__v1_smart_tuning_jobs_{id}_events-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|实例ID|
|labeled_state|query|integer|false|标注状态:|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|

#### Detailed descriptions

**labeled_state**: 标注状态:
- 0: 未处理
- 1: 有效
- 2: 误报

> Example responses

> 200 Response

```json
{
  "false_positive": 0,
  "items": [
    {
      "anno_url": "string",
      "app_id": 0,
      "event_time": 0,
      "id": "string",
      "image_url": "string",
      "instance_id": "string",
      "labeled_state": 0
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_smart_tuning_jobs_{id}_events-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.InstanceEventList](#schemamodels.instanceeventlist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_smart_tuning_jobs_{id}_events_{event_id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/smart_tuning_jobs/{id}/events/{event_id}`

*获取智能调参任务事件*

获取智能调参任务事件

<h3 id="get__v1_smart_tuning_jobs_{id}_events_{event_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|实例ID|
|eventID|path|integer|true|事件ID|

> Example responses

> 200 Response

```json
{
  "anno_url": "string",
  "app_id": 0,
  "event_time": 0,
  "id": "string",
  "image_url": "string",
  "instance_id": "string",
  "labeled_state": 0
}
```

<h3 id="get__v1_smart_tuning_jobs_{id}_events_{event_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.InstanceEvent](#schemamodels.instanceevent)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_smart_tuning_jobs_{id}_events_{event_id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}',
{
  method: 'PUT',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/smart_tuning_jobs/{id}/events/{event_id}`

*更新智能调参任务事件*

更新智能调参任务事件

<h3 id="put__v1_smart_tuning_jobs_{id}_events_{event_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|实例ID|
|eventID|path|string|true|事件ID|
|labeled_state|query|integer|false|标注状态:|

#### Detailed descriptions

**labeled_state**: 标注状态:
- 0: 未处理
- 1: 有效
- 2: 误报

> Example responses

> 200 Response

```json
{
  "anno_url": "string",
  "app_id": 0,
  "event_time": 0,
  "id": "string",
  "image_url": "string",
  "instance_id": "string",
  "labeled_state": 0
}
```

<h3 id="put__v1_smart_tuning_jobs_{id}_events_{event_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.InstanceEvent](#schemamodels.instanceevent)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_smart_tuning_jobs_{id}_events_{event_id}_next

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/next \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/next HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/next',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/next',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/next', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/next', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/next");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/next", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/smart_tuning_jobs/{id}/events/{event_id}/next`

*获取下一个智能调参任务事件*

获取下一个智能调参任务事件

<h3 id="get__v1_smart_tuning_jobs_{id}_events_{event_id}_next-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|实例ID|
|eventID|path|string|true|事件ID|
|labeled_state|query|integer|false|标注状态:|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|

#### Detailed descriptions

**labeled_state**: 标注状态:
- 0: 未处理
- 1: 有效
- 2: 误报

> Example responses

> 200 Response

```json
{
  "anno_url": "string",
  "app_id": 0,
  "event_time": 0,
  "id": "string",
  "image_url": "string",
  "instance_id": "string",
  "labeled_state": 0
}
```

<h3 id="get__v1_smart_tuning_jobs_{id}_events_{event_id}_next-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.InstanceEvent](#schemamodels.instanceevent)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_smart_tuning_jobs_{id}_events_{event_id}_prev

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/prev \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/prev HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/prev',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/prev',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/prev', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/prev', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/prev");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/smart_tuning_jobs/{id}/events/{event_id}/prev", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/smart_tuning_jobs/{id}/events/{event_id}/prev`

*获取上一个智能调参任务事件*

获取上一个智能调参任务事件

<h3 id="get__v1_smart_tuning_jobs_{id}_events_{event_id}_prev-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|实例ID|
|eventID|path|string|true|事件ID|
|labeled_state|query|integer|false|标注状态:|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|

#### Detailed descriptions

**labeled_state**: 标注状态:
- 0: 未处理
- 1: 有效
- 2: 误报

> Example responses

> 200 Response

```json
{
  "anno_url": "string",
  "app_id": 0,
  "event_time": 0,
  "id": "string",
  "image_url": "string",
  "instance_id": "string",
  "labeled_state": 0
}
```

<h3 id="get__v1_smart_tuning_jobs_{id}_events_{event_id}_prev-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.InstanceEvent](#schemamodels.instanceevent)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-sources">sources</h1>

## get__v1_sources

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/sources \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/sources HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/sources',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/sources',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/sources', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/sources', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/sources");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/sources", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/sources`

*输入源列表*

输入源列表

<h3 id="get__v1_sources-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|name|query|string|false|名称|
|order|query|string|false|排序字段|
|orderBy|query|string|false|排序方式:|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|type|query|string|false|类型:|

#### Detailed descriptions

**order**: 排序字段
	* id - 源ID
	* name - 源名称
	* type - 源类型

**orderBy**: 排序方式:
	* asc - 升序
	* desc - 降序

**type**: 类型:
	* camera - 摄像头
	* video - 视频

#### Enumerated Values

|Parameter|Value|
|---|---|
|type|camera|
|type|video|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "id": "string",
      "name": "string",
      "type": "camera"
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_sources-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.SourceList](#schemamodels.sourcelist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_sources_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/sources/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/sources/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/sources/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/sources/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/sources/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/sources/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/sources/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/sources/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/sources/{id}`

*输入源详情*

输入源详情

<h3 id="get__v1_sources_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|输入源ID|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "name": "string",
  "type": "camera"
}
```

<h3 id="get__v1_sources_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Source](#schemamodels.source)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_sources_{id}_snapshot

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/sources/{id}/snapshot \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/sources/{id}/snapshot HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/sources/{id}/snapshot',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/sources/{id}/snapshot',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/sources/{id}/snapshot', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/sources/{id}/snapshot', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/sources/{id}/snapshot");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/sources/{id}/snapshot", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/sources/{id}/snapshot`

*输入源截图*

输入源截图

<h3 id="get__v1_sources_{id}_snapshot-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|摄像头ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="get__v1_sources_{id}_snapshot-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-tasks">tasks</h1>

## post__v1_task_check_resource

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/task/check_resource \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/task/check_resource HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "input_id": "string",
  "instances": [
    {
      "app_id": 0
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/task/check_resource',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/task/check_resource',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/task/check_resource', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/task/check_resource', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/task/check_resource");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/task/check_resource", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/task/check_resource`

*检查任务是否有资源运行*

检查任务是否有资源运行

> Body parameter

```json
{
  "input_id": "string",
  "instances": [
    {
      "app_id": 0
    }
  ]
}
```

<h3 id="post__v1_task_check_resource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.CheckTaskResourceReq](#schemamodels.checktaskresourcereq)|true|body参数|

> Example responses

> 200 Response

```json
{
  "available": true
}
```

<h3 id="post__v1_task_check_resource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.CheckTaskResourceResult](#schemamodels.checktaskresourceresult)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_task_preview

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/task/preview?id=string \
  -H 'Accept: application/json'

```

```http
GET /api/inflet/v1/task/preview?id=string HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/inflet/v1/task/preview?id=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/inflet/v1/task/preview',
  params: {
  'id' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/inflet/v1/task/preview', params={
  'id': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/task/preview', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/task/preview?id=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/task/preview", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/task/preview`

*任务预览*

(http upgrade to websockets)

<h3 id="get__v1_task_preview-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|query|string|true|实例ID|
|scale|query|integer|false|缩放比例,1-原始比例，4-1/4比例，9-1/9比例，16-1/16比例|

#### Enumerated Values

|Parameter|Value|
|---|---|
|scale|1|
|scale|4|
|scale|9|
|scale|16|

> Example responses

> 200 Response

```json
{}
```

<h3 id="get__v1_task_preview-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_tasks

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/tasks \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/tasks HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/tasks',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/tasks', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/tasks', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/tasks", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/tasks`

*任务列表*

任务列表

<h3 id="get__v1_tasks-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|app_id|query|integer|false|算法应用ID|
|input_id|query|string|false|输入源ID|
|input_type|query|string|false|任务输入类型:|
|name|query|string|false|任务名称|
|order|query|string|false|排序字段, 默认为id|
|order_by|query|string|false|排序方式, 默认为desc|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|
|scheduler_type|query|string|false|任务调度类型:|
|status|query|array[string]|false|任务状态:|

#### Detailed descriptions

**input_type**: 任务输入类型:
	* stream - 视频流
	* video - 视频
	* image - 图片

**order**: 排序字段, 默认为id
	* id - 任务ID
	* name - 任务名称
* created_at - 创建时间

**order_by**: 排序方式, 默认为desc
	* desc - 降序
	* asc - 升序

**scheduler_type**: 任务调度类型:
	* daemon - 守护任务
	* cron - 定时任务

**status**: 任务状态:
	* not_started - 未启动
	* pending - 启动中
	* running - 运行中
	* finished - 已完成
	* failed - 失败
	* stream_error - 流异常
	* license_error - 授权异常

#### Enumerated Values

|Parameter|Value|
|---|---|
|input_type|video|
|input_type|image|
|scheduler_type|daemon|
|scheduler_type|cron|
|status|not_started|
|status|pending|
|status|running|
|status|finished|
|status|failed|
|status|stream_error|
|status|license_error|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "cover": "string",
      "created_at": 0,
      "id": 0,
      "input_from": "camera",
      "input_id": "string",
      "input_type": "video",
      "input_url": "string",
      "instances": [
        {
          "alarm_effect": {
            "content": "string",
            "duration": "string",
            "enable": true
          },
          "app_config": "string",
          "app_config_url": "string",
          "app_id": 0,
          "app_label": "string",
          "app_module_definitions": "string",
          "app_module_definitions_url": "string",
          "app_name": "string",
          "cronjob": {
            "duration": "string",
            "start_at": "string"
          },
          "fps": 0,
          "has_app_update": true,
          "id": "string",
          "preview_url": "string",
          "reason": "string",
          "report_url": "string",
          "roi_state": "string",
          "selected_feature_lib": {
            "group_ids": [
              0
            ],
            "id": 0
          },
          "sn": "string",
          "st_state": "None",
          "statistics": {
            "limit": 0,
            "usage": 0
          },
          "status": "not_started"
        }
      ],
      "loop": true,
      "name": "string",
      "scheduler_type": "daemon",
      "status": "not_started",
      "updated_at": 0
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_tasks-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.TaskList](#schemamodels.tasklist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_tasks

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/tasks \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/tasks HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "input_id": "string",
  "instances": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_config": "string",
      "app_id": 0,
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "selected_feature_lib": {
        "group_ids": [
          0
        ],
        "id": 0
      }
    }
  ],
  "loop": true,
  "name": "string",
  "scheduler_type": "daemon",
  "start": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/tasks',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/tasks', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/tasks', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/tasks", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/tasks`

*创建任务*

创建任务

> Body parameter

```json
{
  "input_id": "string",
  "instances": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_config": "string",
      "app_id": 0,
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "selected_feature_lib": {
        "group_ids": [
          0
        ],
        "id": 0
      }
    }
  ],
  "loop": true,
  "name": "string",
  "scheduler_type": "daemon",
  "start": true
}
```

<h3 id="post__v1_tasks-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.CreateTaskReq](#schemamodels.createtaskreq)|true|body参数|

> Example responses

> 200 Response

```json
{
  "cover": "string",
  "created_at": 0,
  "id": 0,
  "input_from": "camera",
  "input_id": "string",
  "input_type": "video",
  "input_url": "string",
  "instances": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_config": "string",
      "app_config_url": "string",
      "app_id": 0,
      "app_label": "string",
      "app_module_definitions": "string",
      "app_module_definitions_url": "string",
      "app_name": "string",
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "fps": 0,
      "has_app_update": true,
      "id": "string",
      "preview_url": "string",
      "reason": "string",
      "report_url": "string",
      "roi_state": "string",
      "selected_feature_lib": {
        "group_ids": [
          0
        ],
        "id": 0
      },
      "sn": "string",
      "st_state": "None",
      "statistics": {
        "limit": 0,
        "usage": 0
      },
      "status": "not_started"
    }
  ],
  "loop": true,
  "name": "string",
  "scheduler_type": "daemon",
  "status": "not_started",
  "updated_at": 0
}
```

<h3 id="post__v1_tasks-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Task](#schemamodels.task)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_tasks_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/tasks/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/tasks/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/tasks/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/tasks/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/tasks/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/tasks/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/tasks/{id}`

*任务详情*

任务详情

<h3 id="get__v1_tasks_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|任务ID|

> Example responses

> 200 Response

```json
{
  "cover": "string",
  "created_at": 0,
  "id": 0,
  "input_from": "camera",
  "input_id": "string",
  "input_type": "video",
  "input_url": "string",
  "instances": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_config": "string",
      "app_config_url": "string",
      "app_id": 0,
      "app_label": "string",
      "app_module_definitions": "string",
      "app_module_definitions_url": "string",
      "app_name": "string",
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "fps": 0,
      "has_app_update": true,
      "id": "string",
      "preview_url": "string",
      "reason": "string",
      "report_url": "string",
      "roi_state": "string",
      "selected_feature_lib": {
        "group_ids": [
          0
        ],
        "id": 0
      },
      "sn": "string",
      "st_state": "None",
      "statistics": {
        "limit": 0,
        "usage": 0
      },
      "status": "not_started"
    }
  ],
  "loop": true,
  "name": "string",
  "scheduler_type": "daemon",
  "status": "not_started",
  "updated_at": 0
}
```

<h3 id="get__v1_tasks_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Task](#schemamodels.task)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_tasks_{id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/tasks/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/tasks/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "input_id": "string",
  "instances": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_config": "string",
      "app_id": 0,
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "selected_feature_lib": {
        "group_ids": [
          0
        ],
        "id": 0
      }
    }
  ],
  "loop": true,
  "name": "string",
  "scheduler_type": "daemon",
  "start": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/tasks/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/tasks/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/tasks/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/tasks/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/tasks/{id}`

*更新任务*

更新任务

> Body parameter

```json
{
  "input_id": "string",
  "instances": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_config": "string",
      "app_id": 0,
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "selected_feature_lib": {
        "group_ids": [
          0
        ],
        "id": 0
      }
    }
  ],
  "loop": true,
  "name": "string",
  "scheduler_type": "daemon",
  "start": true
}
```

<h3 id="put__v1_tasks_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|任务ID|
|body|body|[models.UpdateTaskReq](#schemamodels.updatetaskreq)|true|body参数|

> Example responses

> 200 Response

```json
{
  "cover": "string",
  "created_at": 0,
  "id": 0,
  "input_from": "camera",
  "input_id": "string",
  "input_type": "video",
  "input_url": "string",
  "instances": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_config": "string",
      "app_config_url": "string",
      "app_id": 0,
      "app_label": "string",
      "app_module_definitions": "string",
      "app_module_definitions_url": "string",
      "app_name": "string",
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "fps": 0,
      "has_app_update": true,
      "id": "string",
      "preview_url": "string",
      "reason": "string",
      "report_url": "string",
      "roi_state": "string",
      "selected_feature_lib": {
        "group_ids": [
          0
        ],
        "id": 0
      },
      "sn": "string",
      "st_state": "None",
      "statistics": {
        "limit": 0,
        "usage": 0
      },
      "status": "not_started"
    }
  ],
  "loop": true,
  "name": "string",
  "scheduler_type": "daemon",
  "status": "not_started",
  "updated_at": 0
}
```

<h3 id="put__v1_tasks_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Task](#schemamodels.task)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_tasks_{id}

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/tasks/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
DELETE /api/inflet/v1/tasks/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.delete '/api/inflet/v1/tasks/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.delete('/api/inflet/v1/tasks/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/tasks/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/tasks/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/tasks/{id}`

*删除任务*

删除任务

<h3 id="delete__v1_tasks_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|任务ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="delete__v1_tasks_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_tasks_{id}_check_resource

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/tasks/{id}/check_resource \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/tasks/{id}/check_resource HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks/{id}/check_resource',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/tasks/{id}/check_resource',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/tasks/{id}/check_resource', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/tasks/{id}/check_resource', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks/{id}/check_resource");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/tasks/{id}/check_resource", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/tasks/{id}/check_resource`

*检查任务是否有资源运行*

检查任务是否有资源运行

<h3 id="get__v1_tasks_{id}_check_resource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|任务ID|

> Example responses

> 200 Response

```json
{
  "available": true
}
```

<h3 id="get__v1_tasks_{id}_check_resource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.CheckTaskResourceResult](#schemamodels.checktaskresourceresult)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_tasks_{id}_image_predict

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/tasks/{id}/image_predict \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/tasks/{id}/image_predict HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks/{id}/image_predict',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/tasks/{id}/image_predict',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/tasks/{id}/image_predict', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/tasks/{id}/image_predict', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks/{id}/image_predict");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/tasks/{id}/image_predict", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/tasks/{id}/image_predict`

*图片推理接口文档*

图片推理接口文档

<h3 id="get__v1_tasks_{id}_image_predict-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|任务ID|

> Example responses

> 200 Response

```json
{
  "docs": "string"
}
```

<h3 id="get__v1_tasks_{id}_image_predict-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.ImagePredictDocResp](#schemamodels.imagepredictdocresp)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_tasks_{id}_image_predict

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/tasks/{id}/image_predict \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/tasks/{id}/image_predict HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "additional": null,
  "image": "string",
  "render": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks/{id}/image_predict',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/tasks/{id}/image_predict',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/tasks/{id}/image_predict', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/tasks/{id}/image_predict', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks/{id}/image_predict");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/tasks/{id}/image_predict", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/tasks/{id}/image_predict`

*图片预测*

图片预测(仅支持图片服务类型的任务)

> Body parameter

```json
{
  "additional": null,
  "image": "string",
  "render": true
}
```

<h3 id="post__v1_tasks_{id}_image_predict-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|任务ID|
|body|body|[models.PredictReq](#schemamodels.predictreq)|true|body参数|

> Example responses

> 200 Response

```json
null
```

<h3 id="post__v1_tasks_{id}_image_predict-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<h3 id="post__v1_tasks_{id}_image_predict-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_tasks_{id}_restart

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/tasks/{id}/restart \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/tasks/{id}/restart HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks/{id}/restart',
{
  method: 'PUT',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/tasks/{id}/restart',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/tasks/{id}/restart', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/tasks/{id}/restart', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks/{id}/restart");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/tasks/{id}/restart", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/tasks/{id}/restart`

*重启任务*

重启任务

<h3 id="put__v1_tasks_{id}_restart-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|任务ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="put__v1_tasks_{id}_restart-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_tasks_{id}_start

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/tasks/{id}/start \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/tasks/{id}/start HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks/{id}/start',
{
  method: 'PUT',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/tasks/{id}/start',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/tasks/{id}/start', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/tasks/{id}/start', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks/{id}/start");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/tasks/{id}/start", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/tasks/{id}/start`

*启动任务*

启动任务

<h3 id="put__v1_tasks_{id}_start-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|任务ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="put__v1_tasks_{id}_start-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_tasks_{id}_stop

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/tasks/{id}/stop \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/tasks/{id}/stop HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks/{id}/stop',
{
  method: 'PUT',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/tasks/{id}/stop',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/tasks/{id}/stop', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/tasks/{id}/stop', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks/{id}/stop");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/tasks/{id}/stop", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/tasks/{id}/stop`

*停止任务*

停止任务

<h3 id="put__v1_tasks_{id}_stop-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|任务ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="put__v1_tasks_{id}_stop-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_tasks_{id}_upgrade

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/tasks/{id}/upgrade \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/tasks/{id}/upgrade HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "reserve_roi": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/tasks/{id}/upgrade',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/tasks/{id}/upgrade',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/tasks/{id}/upgrade', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/tasks/{id}/upgrade', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/tasks/{id}/upgrade");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/tasks/{id}/upgrade", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/tasks/{id}/upgrade`

*升级任务配置*

升级任务配置

> Body parameter

```json
{
  "reserve_roi": true
}
```

<h3 id="put__v1_tasks_{id}_upgrade-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|任务ID|
|body|body|[models.UpgradeTaskReq](#schemamodels.upgradetaskreq)|true|body参数|

> Example responses

> 200 Response

```json
{}
```

<h3 id="put__v1_tasks_{id}_upgrade-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-user">user</h1>

## post__v1_user_change_password

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/user/change_password \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/user/change_password HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "new_password": "string",
  "old_password": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/user/change_password',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/user/change_password',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/user/change_password', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/user/change_password', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/user/change_password");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/user/change_password", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/user/change_password`

*修改密码*

修改密码

> Body parameter

```json
{
  "new_password": "string",
  "old_password": "string"
}
```

<h3 id="post__v1_user_change_password-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|[models.ChangePasswordReq](#schemamodels.changepasswordreq)|true|body参数|

> Example responses

> 200 Response

```json
{}
```

<h3 id="post__v1_user_change_password-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_user_info

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/user/info \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/user/info HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/user/info',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/user/info',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/user/info', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/user/info', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/user/info");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/user/info", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/user/info`

*用户信息*

用户信息

<h3 id="get__v1_user_info-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "menus": [
    "dashboard"
  ],
  "name": "string",
  "role": "admin"
}
```

<h3 id="get__v1_user_info-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.UserInfo](#schemamodels.userinfo)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="inflet-api-videos">videos</h1>

## get__v1_videos

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/videos \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/videos HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/videos',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/videos',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/videos', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/videos', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/videos");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/videos", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/videos`

*视频列表*

视频列表

<h3 id="get__v1_videos-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|name|query|string|false|视频名称|
|order|query|string|false|排序方式, 默认为desc|
|order_by|query|string|false|排序字段, 默认为id|
|page|query|integer|false|页码, 默认为1|
|page_size|query|integer|false|每页条数, 默认为10|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "cover_url": "string",
      "created_at": 0,
      "duration": 0,
      "fps": 0,
      "id": "string",
      "name": "string",
      "resolution": "string",
      "size": 0,
      "snapshot_url": "string",
      "updated_at": 0,
      "video_url": "string"
    }
  ],
  "total": 0
}
```

<h3 id="get__v1_videos-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.VideoList](#schemamodels.videolist)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## post__v1_videos

> Code samples

```shell
# You can also use wget
curl -X POST /api/inflet/v1/videos \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
POST /api/inflet/v1/videos HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "file": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/videos',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.post '/api/inflet/v1/videos',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('/api/inflet/v1/videos', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/inflet/v1/videos', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/videos");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/inflet/v1/videos", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /v1/videos`

*上传视频*

上传视频

> Body parameter

```yaml
file: string

```

<h3 id="post__v1_videos-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|body|body|object|true|none|
|» file|body|string(binary)|true|视频文件，仅支持mp4格式|

> Example responses

> 200 Response

```json
{
  "cover_url": "string",
  "created_at": 0,
  "duration": 0,
  "fps": 0,
  "id": "string",
  "name": "string",
  "resolution": "string",
  "size": 0,
  "snapshot_url": "string",
  "updated_at": 0,
  "video_url": "string"
}
```

<h3 id="post__v1_videos-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Video](#schemamodels.video)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## get__v1_videos_{id}

> Code samples

```shell
# You can also use wget
curl -X GET /api/inflet/v1/videos/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
GET /api/inflet/v1/videos/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/videos/{id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.get '/api/inflet/v1/videos/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.get('/api/inflet/v1/videos/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/inflet/v1/videos/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/videos/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/inflet/v1/videos/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /v1/videos/{id}`

*视频详情*

视频详情

<h3 id="get__v1_videos_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|视频ID|

> Example responses

> 200 Response

```json
{
  "cover_url": "string",
  "created_at": 0,
  "duration": 0,
  "fps": 0,
  "id": "string",
  "name": "string",
  "resolution": "string",
  "size": 0,
  "snapshot_url": "string",
  "updated_at": 0,
  "video_url": "string"
}
```

<h3 id="get__v1_videos_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Video](#schemamodels.video)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## put__v1_videos_{id}

> Code samples

```shell
# You can also use wget
curl -X PUT /api/inflet/v1/videos/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
PUT /api/inflet/v1/videos/{id} HTTP/1.1

Content-Type: application/json
Accept: application/json
Authorization: string

```

```javascript
const inputBody = '{
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/videos/{id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.put '/api/inflet/v1/videos/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.put('/api/inflet/v1/videos/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/inflet/v1/videos/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/videos/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/inflet/v1/videos/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /v1/videos/{id}`

*更新视频*

更新视频

> Body parameter

```json
{
  "name": "string"
}
```

<h3 id="put__v1_videos_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|integer|true|视频ID|
|body|body|[models.UpdateVideoReq](#schemamodels.updatevideoreq)|true|body参数|

> Example responses

> 200 Response

```json
{
  "cover_url": "string",
  "created_at": 0,
  "duration": 0,
  "fps": 0,
  "id": "string",
  "name": "string",
  "resolution": "string",
  "size": 0,
  "snapshot_url": "string",
  "updated_at": 0,
  "video_url": "string"
}
```

<h3 id="put__v1_videos_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[models.Video](#schemamodels.video)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

## delete__v1_videos_{id}

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/inflet/v1/videos/{id} \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```http
DELETE /api/inflet/v1/videos/{id} HTTP/1.1

Accept: application/json
Authorization: string

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'string'
};

fetch('/api/inflet/v1/videos/{id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'string'
}

result = RestClient.delete '/api/inflet/v1/videos/{id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.delete('/api/inflet/v1/videos/{id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'string',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/inflet/v1/videos/{id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/inflet/v1/videos/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"string"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/inflet/v1/videos/{id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /v1/videos/{id}`

*删除视频*

删除视频

<h3 id="delete__v1_videos_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|token|
|id|path|string|true|视频ID|

> Example responses

> 200 Response

```json
{}
```

<h3 id="delete__v1_videos_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[code.APISuccess](#schemacode.apisuccess)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|参数错误|[code.APIError](#schemacode.apierror)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|未授权|[code.APIError](#schemacode.apierror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器内部错误|[code.APIError](#schemacode.apierror)|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_code.APIError">code.APIError</h2>
<!-- backwards compatibility -->
<a id="schemacode.apierror"></a>
<a id="schema_code.APIError"></a>
<a id="tocScode.apierror"></a>
<a id="tocscode.apierror"></a>

```json
{
  "code": "string",
  "reason": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|reason|string|false|none|none|

<h2 id="tocS_code.APISuccess">code.APISuccess</h2>
<!-- backwards compatibility -->
<a id="schemacode.apisuccess"></a>
<a id="schema_code.APISuccess"></a>
<a id="tocScode.apisuccess"></a>
<a id="tocscode.apisuccess"></a>

```json
{}

```

### Properties

*None*

<h2 id="tocS_models.AlarmConfig">models.AlarmConfig</h2>
<!-- backwards compatibility -->
<a id="schemamodels.alarmconfig"></a>
<a id="schema_models.AlarmConfig"></a>
<a id="tocSmodels.alarmconfig"></a>
<a id="tocsmodels.alarmconfig"></a>

```json
{
  "audio_url": "string",
  "enable_audio": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|audio_url|string|false|none|告警音频地址|
|enable_audio|boolean|false|none|是否启用告警音频|

<h2 id="tocS_models.AlarmEffect">models.AlarmEffect</h2>
<!-- backwards compatibility -->
<a id="schemamodels.alarmeffect"></a>
<a id="schema_models.AlarmEffect"></a>
<a id="tocSmodels.alarmeffect"></a>
<a id="tocsmodels.alarmeffect"></a>

```json
{
  "content": "string",
  "duration": "string",
  "enable": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|content|string|false|none|特效内容, 最大长度20|
|duration|string|false|none|持续时间（单次）, 例如: 10s, 1m等,范围1s-1m|
|enable|boolean|false|none|启用|

<h2 id="tocS_models.App">models.App</h2>
<!-- backwards compatibility -->
<a id="schemamodels.app"></a>
<a id="schema_models.App"></a>
<a id="tocSmodels.app"></a>
<a id="tocsmodels.app"></a>

```json
{
  "config_url": "string",
  "cover": "string",
  "created_at": 0,
  "description": "string",
  "expired_at": 0,
  "id": 0,
  "label": "string",
  "limit": 0,
  "module_definitions_url": "string",
  "name": "string",
  "type": "video",
  "updated_at": 0,
  "used": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|config_url|string|false|none|算法应用配置|
|cover|string|false|none|算法应用封面|
|created_at|integer|false|none|算法应用创建时间|
|description|string|false|none|算法应用描述|
|expired_at|integer|false|none|算法应用到期时间|
|id|integer|false|none|算法应用ID|
|label|string|false|none|标签：<br>* Face -人脸|
|limit|integer|false|none|算法应用路数限制|
|module_definitions_url|string|false|none|模块定义|
|name|string|false|none|算法应用名称|
|type|[types.InputType](#schematypes.inputtype)|false|none|算法应用类型:<br>* image - 图像服务<br>* video - 视频任务|
|updated_at|integer|false|none|算法应用更新时间|
|used|integer|false|none|算法应用已使用路数|

<h2 id="tocS_models.AppList">models.AppList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.applist"></a>
<a id="schema_models.AppList"></a>
<a id="tocSmodels.applist"></a>
<a id="tocsmodels.applist"></a>

```json
{
  "items": [
    {
      "config_url": "string",
      "cover": "string",
      "created_at": 0,
      "description": "string",
      "expired_at": 0,
      "id": 0,
      "label": "string",
      "limit": 0,
      "module_definitions_url": "string",
      "name": "string",
      "type": "video",
      "updated_at": 0,
      "used": 0
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.App](#schemamodels.app)]|false|none|none|
|total|integer|false|none|none|

<h2 id="tocS_models.AuditLog">models.AuditLog</h2>
<!-- backwards compatibility -->
<a id="schemamodels.auditlog"></a>
<a id="schema_models.AuditLog"></a>
<a id="tocSmodels.auditlog"></a>
<a id="tocsmodels.auditlog"></a>

```json
{
  "content": "string",
  "created_at": 0,
  "id": 0,
  "level": "string",
  "resource": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|content|string|false|none|日志内容|
|created_at|integer|false|none|创建时间|
|id|integer|false|none|日志ID|
|level|string|false|none|日志级别|
|resource|string|false|none|资源类型|

<h2 id="tocS_models.AuditLogList">models.AuditLogList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.auditloglist"></a>
<a id="schema_models.AuditLogList"></a>
<a id="tocSmodels.auditloglist"></a>
<a id="tocsmodels.auditloglist"></a>

```json
{
  "items": [
    {
      "content": "string",
      "created_at": 0,
      "id": 0,
      "level": "string",
      "resource": "string"
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.AuditLog](#schemamodels.auditlog)]|false|none|none|
|total|integer|false|none|none|

<h2 id="tocS_models.Camera">models.Camera</h2>
<!-- backwards compatibility -->
<a id="schemamodels.camera"></a>
<a id="schema_models.Camera"></a>
<a id="tocSmodels.camera"></a>
<a id="tocsmodels.camera"></a>

```json
{
  "cover_url": "string",
  "created_at": 0,
  "fps": 0,
  "id": "string",
  "name": "string",
  "preview_url": "string",
  "resolution": "string",
  "status": "online",
  "stream_url": "string",
  "updated_at": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cover_url|string|false|none|摄像机封面|
|created_at|integer|false|none|创建时间|
|fps|integer|false|none|帧率|
|id|string|false|none|摄像机ID|
|name|string|false|none|摄像机名称|
|preview_url|string|false|none|预览地址|
|resolution|string|false|none|分辨率|
|status|[types.CameraStatus](#schematypes.camerastatus)|false|none|状态:<br>* online - 在线<br>* offline - 离线|
|stream_url|string|false|none|摄像机流地址|
|updated_at|integer|false|none|更新时间|

<h2 id="tocS_models.CameraList">models.CameraList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.cameralist"></a>
<a id="schema_models.CameraList"></a>
<a id="tocSmodels.cameralist"></a>
<a id="tocsmodels.cameralist"></a>

```json
{
  "items": [
    {
      "cover_url": "string",
      "created_at": 0,
      "fps": 0,
      "id": "string",
      "name": "string",
      "preview_url": "string",
      "resolution": "string",
      "status": "online",
      "stream_url": "string",
      "updated_at": 0
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.Camera](#schemamodels.camera)]|false|none|摄像机列表|
|total|integer|false|none|总数|

<h2 id="tocS_models.CameraMetrics">models.CameraMetrics</h2>
<!-- backwards compatibility -->
<a id="schemamodels.camerametrics"></a>
<a id="schema_models.CameraMetrics"></a>
<a id="tocSmodels.camerametrics"></a>
<a id="tocsmodels.camerametrics"></a>

```json
{
  "code_stream_abnormal": 0,
  "offline": 0,
  "online": 0,
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code_stream_abnormal|integer|false|none|码流异常摄像机数|
|offline|integer|false|none|离线摄像机数|
|online|integer|false|none|在线摄像机数|
|total|integer|false|none|摄像机总数|

<h2 id="tocS_models.ChangeDeviceNameReq">models.ChangeDeviceNameReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.changedevicenamereq"></a>
<a id="schema_models.ChangeDeviceNameReq"></a>
<a id="tocSmodels.changedevicenamereq"></a>
<a id="tocsmodels.changedevicenamereq"></a>

```json
{
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|设备名称, 最大长度255|

<h2 id="tocS_models.ChangePasswordReq">models.ChangePasswordReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.changepasswordreq"></a>
<a id="schema_models.ChangePasswordReq"></a>
<a id="tocSmodels.changepasswordreq"></a>
<a id="tocsmodels.changepasswordreq"></a>

```json
{
  "new_password": "string",
  "old_password": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|new_password|string|true|none|新密码|
|old_password|string|true|none|旧密码|

<h2 id="tocS_models.CheckTaskResourceReq">models.CheckTaskResourceReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.checktaskresourcereq"></a>
<a id="schema_models.CheckTaskResourceReq"></a>
<a id="tocSmodels.checktaskresourcereq"></a>
<a id="tocsmodels.checktaskresourcereq"></a>

```json
{
  "input_id": "string",
  "instances": [
    {
      "app_id": 0
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|input_id|string|false|none|输入源ID|
|instances|[object]|false|none|none|
|» app_id|integer|false|none|算法应用ID|

<h2 id="tocS_models.CheckTaskResourceResult">models.CheckTaskResourceResult</h2>
<!-- backwards compatibility -->
<a id="schemamodels.checktaskresourceresult"></a>
<a id="schema_models.CheckTaskResourceResult"></a>
<a id="tocSmodels.checktaskresourceresult"></a>
<a id="tocsmodels.checktaskresourceresult"></a>

```json
{
  "available": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|available|boolean|false|none|是否有资源满足启动任务的条件|

<h2 id="tocS_models.CreateCameraReq">models.CreateCameraReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.createcamerareq"></a>
<a id="schema_models.CreateCameraReq"></a>
<a id="tocSmodels.createcamerareq"></a>
<a id="tocsmodels.createcamerareq"></a>

```json
{
  "name": "string",
  "stream_url": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|摄像机名称|
|stream_url|string|true|none|摄像机流地址|

<h2 id="tocS_models.CreateEventReflowJobParams">models.CreateEventReflowJobParams</h2>
<!-- backwards compatibility -->
<a id="schemamodels.createeventreflowjobparams"></a>
<a id="schema_models.CreateEventReflowJobParams"></a>
<a id="tocSmodels.createeventreflowjobparams"></a>
<a id="tocsmodels.createeventreflowjobparams"></a>

```json
{
  "app_id": 0,
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 1,
  "limit": 100,
  "name": "string",
  "task_ids": [
    0
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|app_id|integer|true|none|算法应用ID|
|cronjob|[models.Cronjob](#schemamodels.cronjob)|true|none|定时任务|
|days|integer|true|none|服务持续时间,1-7|
|limit|integer|true|none|数量上限, 最小100，最大1000|
|name|string|true|none|名称, 任务名称，长度1～20|
|task_ids|[integer]|true|none|*-表示全部，任务ID用逗号分隔|

<h2 id="tocS_models.CreateFeatureLibReq">models.CreateFeatureLibReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.createfeaturelibreq"></a>
<a id="schema_models.CreateFeatureLibReq"></a>
<a id="tocSmodels.createfeaturelibreq"></a>
<a id="tocsmodels.createfeaturelibreq"></a>

```json
{
  "app_id": 0,
  "description": "string",
  "name": "string",
  "parent_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|app_id|integer|false|none|算法应用ID|
|description|string|false|none|描述, 最大长度256|
|name|string|true|none|名称, 最大长度64|
|parent_id|integer|false|none|父特征库ID|

<h2 id="tocS_models.CreateMonitorConfigRequest">models.CreateMonitorConfigRequest</h2>
<!-- backwards compatibility -->
<a id="schemamodels.createmonitorconfigrequest"></a>
<a id="schema_models.CreateMonitorConfigRequest"></a>
<a id="tocSmodels.createmonitorconfigrequest"></a>
<a id="tocsmodels.createmonitorconfigrequest"></a>

```json
{
  "grid": "string",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|grid|string|false|none|网格：<br>* 1x1 - 1x1网格<br>* 2x2 - 2x2网格<br>* 3x3 - 3x3网格<br>* 4x4 - 4x4网格|
|name|string|false|none|名称|

<h2 id="tocS_models.CreateRawDataReflowJobParams">models.CreateRawDataReflowJobParams</h2>
<!-- backwards compatibility -->
<a id="schemamodels.createrawdatareflowjobparams"></a>
<a id="schema_models.CreateRawDataReflowJobParams"></a>
<a id="tocSmodels.createrawdatareflowjobparams"></a>
<a id="tocsmodels.createrawdatareflowjobparams"></a>

```json
{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 1,
  "interval": "string",
  "limit": 100,
  "name": "string",
  "source_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cronjob|[models.Cronjob](#schemamodels.cronjob)|true|none|每天定时任务|
|days|integer|true|none|服务持续天数,1-7|
|interval|string|true|none|抽帧间隔|
|limit|integer|true|none|数据上限|
|name|string|true|none|任务名称, 任务名称，长度1～20|
|source_id|string|true|none|输入源ID|

<h2 id="tocS_models.CreateTaskReq">models.CreateTaskReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.createtaskreq"></a>
<a id="schema_models.CreateTaskReq"></a>
<a id="tocSmodels.createtaskreq"></a>
<a id="tocsmodels.createtaskreq"></a>

```json
{
  "input_id": "string",
  "instances": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_config": "string",
      "app_id": 0,
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "selected_feature_lib": {
        "group_ids": [
          0
        ],
        "id": 0
      }
    }
  ],
  "loop": true,
  "name": "string",
  "scheduler_type": "daemon",
  "start": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|input_id|string|false|none|输入源ID|
|instances|[[models.InstanceReq](#schemamodels.instancereq)]|true|none|算法配置|
|loop|boolean|false|none|循环分析视频，当输入类型为视频且时有效|
|name|string|true|none|任务名称|
|scheduler_type|[types.SchedulerType](#schematypes.schedulertype)|true|none|任务调度类型:<br>	* daemon - 守护任务<br>	* cron - 定时任务|
|start|boolean|false|none|是否启动|

<h2 id="tocS_models.Cronjob">models.Cronjob</h2>
<!-- backwards compatibility -->
<a id="schemamodels.cronjob"></a>
<a id="schema_models.Cronjob"></a>
<a id="tocSmodels.cronjob"></a>
<a id="tocsmodels.cronjob"></a>

```json
{
  "duration": "string",
  "start_at": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|duration|string|false|none|持续时间, 例如: 10m,2h等|
|start_at|string|false|none|启动时间, 例如：08:00|

<h2 id="tocS_models.DeviceInfo">models.DeviceInfo</h2>
<!-- backwards compatibility -->
<a id="schemamodels.deviceinfo"></a>
<a id="schema_models.DeviceInfo"></a>
<a id="tocSmodels.deviceinfo"></a>
<a id="tocsmodels.deviceinfo"></a>

```json
{
  "available_upgrade": true,
  "connected_to_cloud": true,
  "name": "string",
  "registered": true,
  "sn": "string",
  "type": "string",
  "upgrade_progress": 0,
  "version": {
    "property1": "string",
    "property2": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|available_upgrade|boolean|false|none|是否有可用升级|
|connected_to_cloud|boolean|false|none|设备是否连接到互联网|
|name|string|false|none|设备名称|
|registered|boolean|false|none|设备注册状态|
|sn|string|false|none|设备SN|
|type|string|false|none|设备类型|
|upgrade_progress|integer|false|none|升级进度|
|version|object|false|none|软件版本信息|
|» **additionalProperties**|string|false|none|none|

<h2 id="tocS_models.DeviceSubscribeConfig">models.DeviceSubscribeConfig</h2>
<!-- backwards compatibility -->
<a id="schemamodels.devicesubscribeconfig"></a>
<a id="schema_models.DeviceSubscribeConfig"></a>
<a id="tocSmodels.devicesubscribeconfig"></a>
<a id="tocsmodels.devicesubscribeconfig"></a>

```json
{
  "app_key_id": "string",
  "app_key_secret": "string",
  "enable_push": true,
  "interval": "string",
  "url": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|app_key_id|string|false|none|设备订阅AppKeyID|
|app_key_secret|string|false|none|设备订阅AppKeySecret|
|enable_push|boolean|false|none|启动推送到设备订阅|
|interval|string|false|none|推送间隔|
|url|string|false|none|设备订阅地址|

<h2 id="tocS_models.DiskMetrics">models.DiskMetrics</h2>
<!-- backwards compatibility -->
<a id="schemamodels.diskmetrics"></a>
<a id="schema_models.DiskMetrics"></a>
<a id="tocSmodels.diskmetrics"></a>
<a id="tocsmodels.diskmetrics"></a>

```json
{
  "app_used_disk_space": 0,
  "event_used_disk_space": 0,
  "total_disk_space": 0,
  "used_disk_space": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|app_used_disk_space|integer|false|none|下发应用使用磁盘空间|
|event_used_disk_space|integer|false|none|事件存储使用磁盘空间|
|total_disk_space|integer|false|none|磁盘总空间|
|used_disk_space|integer|false|none|已使用磁盘空间|

<h2 id="tocS_models.DownloadEventsReq">models.DownloadEventsReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.downloadeventsreq"></a>
<a id="schema_models.DownloadEventsReq"></a>
<a id="tocSmodels.downloadeventsreq"></a>
<a id="tocsmodels.downloadeventsreq"></a>

```json
{
  "app_id": 0,
  "end": 0,
  "id": [
    "string"
  ],
  "monitor_config_id": 0,
  "order": "string",
  "order_by": "string",
  "page": 0,
  "page_size": 0,
  "source_id": "string",
  "start": 0,
  "status": 0,
  "task_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|app_id|integer|false|none|算法应用ID|
|end|integer|false|none|结束时间|
|id|[string]|false|none|事件ID列表|
|monitor_config_id|integer|false|none|监控配置ID|
|order|string|false|none|排序方式, 默认为desc|
|order_by|string|false|none|排序字段, 默认为id|
|page|integer|false|none|页码, 默认为1|
|page_size|integer|false|none|每页条数, 默认为10|
|source_id|string|false|none|数据源ID|
|start|integer|false|none|起始时间|
|status|integer|false|none|状态<br>- 0: 未处理<br>- 1: 有效<br>- 2: 误报|
|task_id|integer|false|none|任务ID|

<h2 id="tocS_models.Ethernet">models.Ethernet</h2>
<!-- backwards compatibility -->
<a id="schemamodels.ethernet"></a>
<a id="schema_models.Ethernet"></a>
<a id="tocSmodels.ethernet"></a>
<a id="tocsmodels.ethernet"></a>

```json
{
  "DHCP4": true,
  "address": "string",
  "gateway4": "string",
  "name": "string",
  "nameservers": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DHCP4|boolean|false|none|是否DHCP|
|address|string|false|none|IP地址|
|gateway4|string|false|none|网关|
|name|string|false|none|网卡名称|
|nameservers|[string]|false|none|DNS|

<h2 id="tocS_models.Event">models.Event</h2>
<!-- backwards compatibility -->
<a id="schemamodels.event"></a>
<a id="schema_models.Event"></a>
<a id="tocSmodels.event"></a>
<a id="tocsmodels.event"></a>

```json
{
  "alarm_effect": {
    "content": "string",
    "duration": "string",
    "enable": true
  },
  "app_id": 0,
  "app_name": "string",
  "created": 0,
  "id": "string",
  "is_reported": 0,
  "meta_url": "string",
  "preview_url": "string",
  "reason": "string",
  "source_id": "string",
  "source_name": "string",
  "status": 0,
  "task_id": 0,
  "task_name": "string",
  "thumb_url": "string",
  "video_url": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alarm_effect|[models.AlarmEffect](#schemamodels.alarmeffect)|false|none|报警特效|
|app_id|integer|false|none|算法应用ID|
|app_name|string|false|none|算法应用名称|
|created|integer|false|none|事件发生时间|
|id|string|false|none|标识符|
|is_reported|integer|false|none|是否成功上报: 0为无需上报, 1为成功, 2为失败|
|meta_url|string|false|none|MetaURL|
|preview_url|string|false|none|预览地址|
|reason|string|false|none|上报失败原因|
|source_id|string|false|none|数据源ID|
|source_name|string|false|none|数据源名称|
|status|integer|false|none|状态:<br>- 0: 未处理<br>- 1: 有效<br>- 2: 误报|
|task_id|integer|false|none|任务ID|
|task_name|string|false|none|任务名称|
|thumb_url|string|false|none|缩略图|
|video_url|string|false|none|视频地址|

<h2 id="tocS_models.EventList">models.EventList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.eventlist"></a>
<a id="schema_models.EventList"></a>
<a id="tocSmodels.eventlist"></a>
<a id="tocsmodels.eventlist"></a>

```json
{
  "items": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_id": 0,
      "app_name": "string",
      "created": 0,
      "id": "string",
      "is_reported": 0,
      "meta_url": "string",
      "preview_url": "string",
      "reason": "string",
      "source_id": "string",
      "source_name": "string",
      "status": 0,
      "task_id": 0,
      "task_name": "string",
      "thumb_url": "string",
      "video_url": "string"
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.Event](#schemamodels.event)]|false|none|列表|
|total|integer|false|none|总数|

<h2 id="tocS_models.EventReflowJob">models.EventReflowJob</h2>
<!-- backwards compatibility -->
<a id="schemamodels.eventreflowjob"></a>
<a id="schema_models.EventReflowJob"></a>
<a id="tocSmodels.eventreflowjob"></a>
<a id="tocsmodels.eventreflowjob"></a>

```json
{
  "app_id": 0,
  "app_name": "string",
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "current": 0,
  "days": 0,
  "deadline": 0,
  "id": "string",
  "latest_reflow_time": 0,
  "limit": 0,
  "name": "string",
  "status": "string",
  "tasks": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "uploaded_count": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|app_id|integer|false|none|算法应用ID|
|app_name|string|false|none|算法应用名称|
|cronjob|[models.Cronjob](#schemamodels.cronjob)|false|none|定时任务|
|current|integer|false|none|当前数量|
|days|integer|false|none|服务持续时间|
|deadline|integer|false|none|截止时间(可选)|
|id|string|false|none|任务ID|
|latest_reflow_time|integer|false|none|最近一次回流时间|
|limit|integer|false|none|数量上限|
|name|string|false|none|名称|
|status|string|false|none|服务状态:<br>* not_started - 未开始<br>* running - 运行中<br>* done - 已完成|
|tasks|[[models.EventReflowTask](#schemamodels.eventreflowtask)]|false|none|任务列表|
|uploaded_count|integer|false|none|已上传数量|

<h2 id="tocS_models.EventReflowJobList">models.EventReflowJobList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.eventreflowjoblist"></a>
<a id="schema_models.EventReflowJobList"></a>
<a id="tocSmodels.eventreflowjoblist"></a>
<a id="tocsmodels.eventreflowjoblist"></a>

```json
{
  "items": [
    {
      "app_id": 0,
      "app_name": "string",
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "current": 0,
      "days": 0,
      "deadline": 0,
      "id": "string",
      "latest_reflow_time": 0,
      "limit": 0,
      "name": "string",
      "status": "string",
      "tasks": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "uploaded_count": 0
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.EventReflowJob](#schemamodels.eventreflowjob)]|false|none|列表|
|total|integer|false|none|总数|

<h2 id="tocS_models.EventReflowTask">models.EventReflowTask</h2>
<!-- backwards compatibility -->
<a id="schemamodels.eventreflowtask"></a>
<a id="schema_models.EventReflowTask"></a>
<a id="tocSmodels.eventreflowtask"></a>
<a id="tocsmodels.eventreflowtask"></a>

```json
{
  "id": 0,
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|-1表示全部|
|name|string|false|none|任务名称(可选)|

<h2 id="tocS_models.FeatureLib">models.FeatureLib</h2>
<!-- backwards compatibility -->
<a id="schemamodels.featurelib"></a>
<a id="schema_models.FeatureLib"></a>
<a id="tocSmodels.featurelib"></a>
<a id="tocsmodels.featurelib"></a>

```json
{
  "app_id": 0,
  "created_at": 0,
  "extracted_image_count": 0,
  "failed_count": 0,
  "id": 0,
  "image_count": 0,
  "name": "string",
  "support_sub_feature_lib": true,
  "updated_at": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|app_id|integer|false|none|算法应用ID|
|created_at|integer|false|none|创建时间|
|extracted_image_count|integer|false|none|已提取特征的图片数量|
|failed_count|integer|false|none|提取失败的图片数量|
|id|integer|false|none|特征库ID|
|image_count|integer|false|none|图片数量|
|name|string|false|none|名称|
|support_sub_feature_lib|boolean|false|none|是否支持子特征库|
|updated_at|integer|false|none|更新时间|

<h2 id="tocS_models.FeatureLibItem">models.FeatureLibItem</h2>
<!-- backwards compatibility -->
<a id="schemamodels.featurelibitem"></a>
<a id="schema_models.FeatureLibItem"></a>
<a id="tocSmodels.featurelibitem"></a>
<a id="tocsmodels.featurelibitem"></a>

```json
{
  "created_at": 0,
  "error": "string",
  "feature_lib_id": 0,
  "id": 0,
  "image_url": "string",
  "name": "string",
  "render": null,
  "state": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|created_at|integer|false|none|创建时间|
|error|string|false|none|错误信息|
|feature_lib_id|integer|false|none|特征库ID|
|id|integer|false|none|特征库项ID|
|image_url|string|false|none|图片地址|
|name|string|false|none|名称|
|render|any|false|none|渲染数据|
|state|integer|false|none|状态, 1: 未提取, 2: 提取中, 3: 提取完成, 4: 提取失败|

<h2 id="tocS_models.FeatureLibItemList">models.FeatureLibItemList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.featurelibitemlist"></a>
<a id="schema_models.FeatureLibItemList"></a>
<a id="tocSmodels.featurelibitemlist"></a>
<a id="tocsmodels.featurelibitemlist"></a>

```json
{
  "items": [
    {
      "created_at": 0,
      "error": "string",
      "feature_lib_id": 0,
      "id": 0,
      "image_url": "string",
      "name": "string",
      "render": null,
      "state": 0
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.FeatureLibItem](#schemamodels.featurelibitem)]|false|none|none|
|total|integer|false|none|none|

<h2 id="tocS_models.FeatureLibList">models.FeatureLibList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.featureliblist"></a>
<a id="schema_models.FeatureLibList"></a>
<a id="tocSmodels.featureliblist"></a>
<a id="tocsmodels.featureliblist"></a>

```json
{
  "items": [
    {
      "app_id": 0,
      "created_at": 0,
      "extracted_image_count": 0,
      "failed_count": 0,
      "id": 0,
      "image_count": 0,
      "name": "string",
      "support_sub_feature_lib": true,
      "updated_at": 0
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.FeatureLib](#schemamodels.featurelib)]|false|none|none|
|total|integer|false|none|none|

<h2 id="tocS_models.ImagePredictDocResp">models.ImagePredictDocResp</h2>
<!-- backwards compatibility -->
<a id="schemamodels.imagepredictdocresp"></a>
<a id="schema_models.ImagePredictDocResp"></a>
<a id="tocSmodels.imagepredictdocresp"></a>
<a id="tocsmodels.imagepredictdocresp"></a>

```json
{
  "docs": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|docs|string|false|none|接口文档内容|

<h2 id="tocS_models.Instance">models.Instance</h2>
<!-- backwards compatibility -->
<a id="schemamodels.instance"></a>
<a id="schema_models.Instance"></a>
<a id="tocSmodels.instance"></a>
<a id="tocsmodels.instance"></a>

```json
{
  "alarm_effect": {
    "content": "string",
    "duration": "string",
    "enable": true
  },
  "app_config": "string",
  "app_config_url": "string",
  "app_id": 0,
  "app_label": "string",
  "app_module_definitions": "string",
  "app_module_definitions_url": "string",
  "app_name": "string",
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "fps": 0,
  "has_app_update": true,
  "id": "string",
  "preview_url": "string",
  "reason": "string",
  "report_url": "string",
  "roi_state": "string",
  "selected_feature_lib": {
    "group_ids": [
      0
    ],
    "id": 0
  },
  "sn": "string",
  "st_state": "None",
  "statistics": {
    "limit": 0,
    "usage": 0
  },
  "status": "not_started"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alarm_effect|[models.AlarmEffect](#schemamodels.alarmeffect)|false|none|报警特效|
|app_config|string|false|none|算法应用配置|
|app_config_url|string|false|none|算法应用配置地址|
|app_id|integer|false|none|算法应用ID|
|app_label|string|false|none|算法应用标签|
|app_module_definitions|string|false|none|算法应用模型定义|
|app_module_definitions_url|string|false|none|算法应用模型定义地址|
|app_name|string|false|none|算法应用名称|
|cronjob|[models.Cronjob](#schemamodels.cronjob)|false|none|定时任务|
|fps|integer|false|none|帧率|
|has_app_update|boolean|false|none|有更新|
|id|string|false|none|实例ID|
|preview_url|string|false|none|预览地址|
|reason|string|false|none|异常原因|
|report_url|string|false|none|智能调参报告地址|
|roi_state|string|false|none|ROI状态：<br>* None - 无ROI<br>* Configured - 已配置ROI<br>* NotConfigured - 未配置ROI|
|selected_feature_lib|[models.SelectedFeatureLib](#schemamodels.selectedfeaturelib)|false|none|特征库ID集合|
|sn|string|false|none|推理引擎SN|
|st_state|[models.SmartTuningState](#schemamodels.smarttuningstate)|false|none|智能调参状态：<br>* None - 当前任务不支持智能调参<br>* Available - 当前任务可以智能调参<br>* Configured - 当前任务已配置智能调参<br>* Ready - 当前任务智能调参已准备好,可以开始<br>* Running - 当前任务智能调参正在运行<br>* Finished - 当前任务智能调参已完成|
|statistics|[models.Statistics](#schemamodels.statistics)|false|none|调用统计|
|status|[models.TaskStatus](#schemamodels.taskstatus)|false|none|任务状态:<br>	* not_started - 未启动<br>	* pending - 启动中<br>	* running - 运行中<br>	* finished - 已完成<br>	* failed - 失败<br>	* stream_error - 流异常<br>	* license_error - 授权异常|

<h2 id="tocS_models.InstanceEvent">models.InstanceEvent</h2>
<!-- backwards compatibility -->
<a id="schemamodels.instanceevent"></a>
<a id="schema_models.InstanceEvent"></a>
<a id="tocSmodels.instanceevent"></a>
<a id="tocsmodels.instanceevent"></a>

```json
{
  "anno_url": "string",
  "app_id": 0,
  "event_time": 0,
  "id": "string",
  "image_url": "string",
  "instance_id": "string",
  "labeled_state": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anno_url|string|false|none|none|
|app_id|integer|false|none|none|
|event_time|integer|false|none|none|
|id|string|false|none|none|
|image_url|string|false|none|none|
|instance_id|string|false|none|none|
|labeled_state|integer|false|none|标注状态:<br>- 0: 未处理<br>- 1: 有效<br>- 2: 误报|

<h2 id="tocS_models.InstanceEventList">models.InstanceEventList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.instanceeventlist"></a>
<a id="schema_models.InstanceEventList"></a>
<a id="tocSmodels.instanceeventlist"></a>
<a id="tocsmodels.instanceeventlist"></a>

```json
{
  "false_positive": 0,
  "items": [
    {
      "anno_url": "string",
      "app_id": 0,
      "event_time": 0,
      "id": "string",
      "image_url": "string",
      "instance_id": "string",
      "labeled_state": 0
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|false_positive|integer|false|none|none|
|items|[[models.InstanceEvent](#schemamodels.instanceevent)]|false|none|none|
|total|integer|false|none|none|

<h2 id="tocS_models.InstanceReq">models.InstanceReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.instancereq"></a>
<a id="schema_models.InstanceReq"></a>
<a id="tocSmodels.instancereq"></a>
<a id="tocsmodels.instancereq"></a>

```json
{
  "alarm_effect": {
    "content": "string",
    "duration": "string",
    "enable": true
  },
  "app_config": "string",
  "app_id": 0,
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "selected_feature_lib": {
    "group_ids": [
      0
    ],
    "id": 0
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alarm_effect|[models.AlarmEffect](#schemamodels.alarmeffect)|false|none|报警特效|
|app_config|string|false|none|算法应用配置|
|app_id|integer|false|none|算法应用ID|
|cronjob|[models.Cronjob](#schemamodels.cronjob)|false|none|定时任务|
|selected_feature_lib|[models.SelectedFeatureLib](#schemamodels.selectedfeaturelib)|false|none|特征库ID集合|

<h2 id="tocS_models.LoginReq">models.LoginReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.loginreq"></a>
<a id="schema_models.LoginReq"></a>
<a id="tocSmodels.loginreq"></a>
<a id="tocsmodels.loginreq"></a>

```json
{
  "password": "string",
  "username": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|password|string|true|none|密码，长度为6-20个字符|
|username|string|true|none|用户名，长度为2-20个字符|

<h2 id="tocS_models.LoginResp">models.LoginResp</h2>
<!-- backwards compatibility -->
<a id="schemamodels.loginresp"></a>
<a id="schema_models.LoginResp"></a>
<a id="tocSmodels.loginresp"></a>
<a id="tocsmodels.loginresp"></a>

```json
{
  "token": "string",
  "user": {
    "id": 0,
    "menus": [
      "dashboard"
    ],
    "name": "string",
    "role": "admin"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|token|string|false|none|token|
|user|[models.UserInfo](#schemamodels.userinfo)|false|none|用户信息|

<h2 id="tocS_models.LogoConfig">models.LogoConfig</h2>
<!-- backwards compatibility -->
<a id="schemamodels.logoconfig"></a>
<a id="schema_models.LogoConfig"></a>
<a id="tocSmodels.logoconfig"></a>
<a id="tocsmodels.logoconfig"></a>

```json
{
  "day_ico": "string",
  "day_logo": "string",
  "night_ico": "string",
  "night_logo": "string",
  "platform_name": "string",
  "slogan": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|day_ico|string|false|none|白天ico|
|day_logo|string|false|none|白天logo|
|night_ico|string|false|none|夜晚ico|
|night_logo|string|false|none|夜晚logo|
|platform_name|string|false|none|平台名称，默认为“人工智能应用管理平台”|
|slogan|string|false|none|Slogan|

<h2 id="tocS_models.MenuConfig">models.MenuConfig</h2>
<!-- backwards compatibility -->
<a id="schemamodels.menuconfig"></a>
<a id="schema_models.MenuConfig"></a>
<a id="tocSmodels.menuconfig"></a>
<a id="tocsmodels.menuconfig"></a>

```json
{
  "enable_audit_log": true,
  "enable_feature_lib": true,
  "enable_image_service": true,
  "enable_monitor": true,
  "enable_reflow": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|enable_audit_log|boolean|false|none|显示系统日志|
|enable_feature_lib|boolean|false|none|显示特征库|
|enable_image_service|boolean|false|none|显示图片服务|
|enable_monitor|boolean|false|none|显示监控|
|enable_reflow|boolean|false|none|显示数据回流|

<h2 id="tocS_models.MonitorConfig">models.MonitorConfig</h2>
<!-- backwards compatibility -->
<a id="schemamodels.monitorconfig"></a>
<a id="schema_models.MonitorConfig"></a>
<a id="tocSmodels.monitorconfig"></a>
<a id="tocsmodels.monitorconfig"></a>

```json
{
  "grid": "string",
  "id": 0,
  "name": "string",
  "positions": {
    "property1": {
      "current_instance_id": "string",
      "id": "string",
      "instances": [
        {
          "app_name": "string",
          "fps": 0,
          "id": "string"
        }
      ],
      "source_name": "string",
      "task_name": "string"
    },
    "property2": {
      "current_instance_id": "string",
      "id": "string",
      "instances": [
        {
          "app_name": "string",
          "fps": 0,
          "id": "string"
        }
      ],
      "source_name": "string",
      "task_name": "string"
    }
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|grid|string|false|none|网格<br>* 1x1 - 1x1网格<br>* 2x2 - 2x2网格<br>* 3x3 - 3x3网格<br>* 4x4 - 4x4网格|
|id|integer|false|none|ID|
|name|string|false|none|名称|
|positions|object|false|none|key-位置，value-任务信息|
|» **additionalProperties**|[models.TaskInfo](#schemamodels.taskinfo)|false|none|none|

<h2 id="tocS_models.MonitorConfigList">models.MonitorConfigList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.monitorconfiglist"></a>
<a id="schema_models.MonitorConfigList"></a>
<a id="tocSmodels.monitorconfiglist"></a>
<a id="tocsmodels.monitorconfiglist"></a>

```json
{
  "items": [
    {
      "grid": "string",
      "id": 0,
      "name": "string",
      "positions": {
        "property1": {
          "current_instance_id": "string",
          "id": "string",
          "instances": [
            {
              "app_name": "string",
              "fps": 0,
              "id": "string"
            }
          ],
          "source_name": "string",
          "task_name": "string"
        },
        "property2": {
          "current_instance_id": "string",
          "id": "string",
          "instances": [
            {
              "app_name": "string",
              "fps": 0,
              "id": "string"
            }
          ],
          "source_name": "string",
          "task_name": "string"
        }
      }
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.MonitorConfig](#schemamodels.monitorconfig)]|false|none|列表|
|total|integer|false|none|总数|

<h2 id="tocS_models.MonitorInstance">models.MonitorInstance</h2>
<!-- backwards compatibility -->
<a id="schemamodels.monitorinstance"></a>
<a id="schema_models.MonitorInstance"></a>
<a id="tocSmodels.monitorinstance"></a>
<a id="tocsmodels.monitorinstance"></a>

```json
{
  "app_name": "string",
  "fps": 0,
  "id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|app_name|string|false|none|none|
|fps|integer|false|none|none|
|id|string|false|none|none|

<h2 id="tocS_models.PredictReq">models.PredictReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.predictreq"></a>
<a id="schema_models.PredictReq"></a>
<a id="tocSmodels.predictreq"></a>
<a id="tocsmodels.predictreq"></a>

```json
{
  "additional": null,
  "image": "string",
  "render": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|additional|any|false|none|附加信息|
|image|string|false|none|图片http url 或者 base64|
|render|boolean|false|none|前端渲染模式|

<h2 id="tocS_models.RawDataReflowJob">models.RawDataReflowJob</h2>
<!-- backwards compatibility -->
<a id="schemamodels.rawdatareflowjob"></a>
<a id="schema_models.RawDataReflowJob"></a>
<a id="tocSmodels.rawdatareflowjob"></a>
<a id="tocsmodels.rawdatareflowjob"></a>

```json
{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "current": 0,
  "days": 0,
  "deadline": 0,
  "id": "string",
  "interval": "string",
  "latest_reflow_time": 0,
  "limit": 0,
  "name": "string",
  "source_id": "string",
  "source_name": "string",
  "status": "string",
  "uploaded_count": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cronjob|[models.Cronjob](#schemamodels.cronjob)|false|none|每天定时任务|
|current|integer|false|none|已完成数量|
|days|integer|false|none|服务持续天数|
|deadline|integer|false|none|服务停止时间(可选)|
|id|string|false|none|任务ID|
|interval|string|false|none|抽帧间隔|
|latest_reflow_time|integer|false|none|最近一次回流时间(可选)|
|limit|integer|false|none|数量上限|
|name|string|false|none|任务名称|
|source_id|string|false|none|输入源ID|
|source_name|string|false|none|输入源名称|
|status|string|false|none|任务状态：<br>* not_started - 未开始<br>* running - 运行中<br>* done - 已完成|
|uploaded_count|integer|false|none|已上传数量|

<h2 id="tocS_models.RawDataReflowJobList">models.RawDataReflowJobList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.rawdatareflowjoblist"></a>
<a id="schema_models.RawDataReflowJobList"></a>
<a id="tocSmodels.rawdatareflowjoblist"></a>
<a id="tocsmodels.rawdatareflowjoblist"></a>

```json
{
  "items": [
    {
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "current": 0,
      "days": 0,
      "deadline": 0,
      "id": "string",
      "interval": "string",
      "latest_reflow_time": 0,
      "limit": 0,
      "name": "string",
      "source_id": "string",
      "source_name": "string",
      "status": "string",
      "uploaded_count": 0
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.RawDataReflowJob](#schemamodels.rawdatareflowjob)]|false|none|任务列表|
|total|integer|false|none|总数|

<h2 id="tocS_models.RegisterDeviceReq">models.RegisterDeviceReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.registerdevicereq"></a>
<a id="schema_models.RegisterDeviceReq"></a>
<a id="tocSmodels.registerdevicereq"></a>
<a id="tocsmodels.registerdevicereq"></a>

```json
{
  "code": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|true|none|注册码|

<h2 id="tocS_models.ResetReq">models.ResetReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.resetreq"></a>
<a id="schema_models.ResetReq"></a>
<a id="tocSmodels.resetreq"></a>
<a id="tocsmodels.resetreq"></a>

```json
{
  "password": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|password|string|true|none|none|

<h2 id="tocS_models.SelectedFeatureLib">models.SelectedFeatureLib</h2>
<!-- backwards compatibility -->
<a id="schemamodels.selectedfeaturelib"></a>
<a id="schema_models.SelectedFeatureLib"></a>
<a id="tocSmodels.selectedfeaturelib"></a>
<a id="tocsmodels.selectedfeaturelib"></a>

```json
{
  "group_ids": [
    0
  ],
  "id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|group_ids|[integer]|false|none|特征库组ID集合|
|id|integer|false|none|特征库ID|

<h2 id="tocS_models.SmartTuningJob">models.SmartTuningJob</h2>
<!-- backwards compatibility -->
<a id="schemamodels.smarttuningjob"></a>
<a id="schema_models.SmartTuningJob"></a>
<a id="tocSmodels.smarttuningjob"></a>
<a id="tocsmodels.smarttuningjob"></a>

```json
{
  "app_id": 0,
  "app_name": "string",
  "fp_count": 0,
  "instance_id": "string",
  "labeled_count": 0,
  "name": "string",
  "progress": 0,
  "report_url": "string",
  "state": "None",
  "task_id": 0,
  "task_name": "string",
  "total_count": 0,
  "tp_count": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|app_id|integer|false|none|算法应用ID|
|app_name|string|false|none|算法应用名称|
|fp_count|integer|false|none|FPCount 误报数量|
|instance_id|string|false|none|实例ID|
|labeled_count|integer|false|none|LabeledCount 已标注数量|
|name|string|false|none|任务名称|
|progress|integer|false|none|调参进度|
|report_url|string|false|none|ReportURL 报告URL|
|state|[models.SmartTuningState](#schemamodels.smarttuningstate)|false|none|状态：<br>* None - 当前任务不支持智能调参<br>* Available - 当前任务可以智能调参<br>* Configured - 当前任务已配置智能调参<br>* Ready - 当前任务智能调参已准备好,可以开始<br>* Running - 当前任务智能调参正在运行<br>* Finished - 当前任务智能调参已完成|
|task_id|integer|false|none|任务ID|
|task_name|string|false|none|任务名称|
|total_count|integer|false|none|TotalCount 总数量|
|tp_count|integer|false|none|TPCount 有效数量|

<h2 id="tocS_models.SmartTuningJobList">models.SmartTuningJobList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.smarttuningjoblist"></a>
<a id="schema_models.SmartTuningJobList"></a>
<a id="tocSmodels.smarttuningjoblist"></a>
<a id="tocsmodels.smarttuningjoblist"></a>

```json
{
  "items": [
    {
      "app_id": 0,
      "app_name": "string",
      "fp_count": 0,
      "instance_id": "string",
      "labeled_count": 0,
      "name": "string",
      "progress": 0,
      "report_url": "string",
      "state": "None",
      "task_id": 0,
      "task_name": "string",
      "total_count": 0,
      "tp_count": 0
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.SmartTuningJob](#schemamodels.smarttuningjob)]|false|none|none|
|total|integer|false|none|none|

<h2 id="tocS_models.SmartTuningState">models.SmartTuningState</h2>
<!-- backwards compatibility -->
<a id="schemamodels.smarttuningstate"></a>
<a id="schema_models.SmartTuningState"></a>
<a id="tocSmodels.smarttuningstate"></a>
<a id="tocsmodels.smarttuningstate"></a>

```json
"None"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|None|
|*anonymous*|Available|
|*anonymous*|Configured|
|*anonymous*|Ready|
|*anonymous*|Running|
|*anonymous*|Finished|

<h2 id="tocS_models.Source">models.Source</h2>
<!-- backwards compatibility -->
<a id="schemamodels.source"></a>
<a id="schema_models.Source"></a>
<a id="tocSmodels.source"></a>
<a id="tocsmodels.source"></a>

```json
{
  "id": "string",
  "name": "string",
  "type": "camera"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|源ID|
|name|string|false|none|源名称|
|type|[types.SourceType](#schematypes.sourcetype)|false|none|源类型:<br>	* camera - 摄像头<br>	* video - 视频|

<h2 id="tocS_models.SourceList">models.SourceList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.sourcelist"></a>
<a id="schema_models.SourceList"></a>
<a id="tocSmodels.sourcelist"></a>
<a id="tocsmodels.sourcelist"></a>

```json
{
  "items": [
    {
      "id": "string",
      "name": "string",
      "type": "camera"
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.Source](#schemamodels.source)]|false|none|none|
|total|integer|false|none|none|

<h2 id="tocS_models.StAction">models.StAction</h2>
<!-- backwards compatibility -->
<a id="schemamodels.staction"></a>
<a id="schema_models.StAction"></a>
<a id="tocSmodels.staction"></a>
<a id="tocsmodels.staction"></a>

```json
"Configure"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|Configure|
|*anonymous*|Start|
|*anonymous*|Apply|
|*anonymous*|Cancel|

<h2 id="tocS_models.Statistics">models.Statistics</h2>
<!-- backwards compatibility -->
<a id="schemamodels.statistics"></a>
<a id="schema_models.Statistics"></a>
<a id="tocSmodels.statistics"></a>
<a id="tocsmodels.statistics"></a>

```json
{
  "limit": 0,
  "usage": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|limit|integer|false|none|授权总数，-1表示无限制|
|usage|integer|false|none|已使用|

<h2 id="tocS_models.SubscribeConfig">models.SubscribeConfig</h2>
<!-- backwards compatibility -->
<a id="schemamodels.subscribeconfig"></a>
<a id="schema_models.SubscribeConfig"></a>
<a id="tocSmodels.subscribeconfig"></a>
<a id="tocsmodels.subscribeconfig"></a>

```json
{
  "app_key_id": "string",
  "app_key_secret": "string",
  "enable_push_to_gddi": true,
  "enable_push_to_third": true,
  "event_image_with_roi": true,
  "push_in_order": true,
  "upload_type": 1,
  "url": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|app_key_id|string|false|none|第三方平台AppKeyID|
|app_key_secret|string|false|none|第三方平台AppKeySecret|
|enable_push_to_gddi|boolean|false|none|启动推送到GDDI|
|enable_push_to_third|boolean|false|none|启动推送到第三方平台|
|event_image_with_roi|boolean|false|none|事件带框图片是否保留ROI区域|
|push_in_order|boolean|false|none|按顺序依次推送|
|upload_type|[types.EventReportType](#schematypes.eventreporttype)|false|none|第三方平台推送类型<br>* 1 - 事件详情推送<br>* 2 - 事件原图推送<br>* 4 - 事件带框图片推送<br>* 8 - 事件带框视频推送|
|url|string|false|none|第三方平台地址|

<h2 id="tocS_models.SysTime">models.SysTime</h2>
<!-- backwards compatibility -->
<a id="schemamodels.systime"></a>
<a id="schema_models.SysTime"></a>
<a id="tocSmodels.systime"></a>
<a id="tocsmodels.systime"></a>

```json
{
  "ntp_server": "string",
  "sync": true,
  "timestamp": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ntp_server|string|false|none|NTP服务器地址|
|sync|boolean|false|none|是否同步|
|timestamp|integer|false|none|时间戳|

<h2 id="tocS_models.SystemConfig">models.SystemConfig</h2>
<!-- backwards compatibility -->
<a id="schemamodels.systemconfig"></a>
<a id="schema_models.SystemConfig"></a>
<a id="tocSmodels.systemconfig"></a>
<a id="tocsmodels.systemconfig"></a>

```json
{
  "auto_clean_threshold": 0,
  "max_threshold": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|auto_clean_threshold|integer|false|none|自动清理阈值（条），默认1000, 0表示不清理|
|max_threshold|integer|false|none|最大值，默认1000,000|

<h2 id="tocS_models.SystemResourceMetrics">models.SystemResourceMetrics</h2>
<!-- backwards compatibility -->
<a id="schemamodels.systemresourcemetrics"></a>
<a id="schema_models.SystemResourceMetrics"></a>
<a id="tocSmodels.systemresourcemetrics"></a>
<a id="tocsmodels.systemresourcemetrics"></a>

```json
{
  "cpu_temperature": 0,
  "cpu_usage": 0,
  "gpu_mem_usage": 0,
  "gpu_temperature": 0,
  "gpu_usage": 0,
  "mem_usage": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cpu_temperature|integer|false|none|CPU温度|
|cpu_usage|integer|false|none|CPU使用率|
|gpu_mem_usage|integer|false|none|GPU内存使用率|
|gpu_temperature|integer|false|none|GPU温度|
|gpu_usage|integer|false|none|GPU使用率|
|mem_usage|integer|false|none|内存使用率|

<h2 id="tocS_models.Task">models.Task</h2>
<!-- backwards compatibility -->
<a id="schemamodels.task"></a>
<a id="schema_models.Task"></a>
<a id="tocSmodels.task"></a>
<a id="tocsmodels.task"></a>

```json
{
  "cover": "string",
  "created_at": 0,
  "id": 0,
  "input_from": "camera",
  "input_id": "string",
  "input_type": "video",
  "input_url": "string",
  "instances": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_config": "string",
      "app_config_url": "string",
      "app_id": 0,
      "app_label": "string",
      "app_module_definitions": "string",
      "app_module_definitions_url": "string",
      "app_name": "string",
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "fps": 0,
      "has_app_update": true,
      "id": "string",
      "preview_url": "string",
      "reason": "string",
      "report_url": "string",
      "roi_state": "string",
      "selected_feature_lib": {
        "group_ids": [
          0
        ],
        "id": 0
      },
      "sn": "string",
      "st_state": "None",
      "statistics": {
        "limit": 0,
        "usage": 0
      },
      "status": "not_started"
    }
  ],
  "loop": true,
  "name": "string",
  "scheduler_type": "daemon",
  "status": "not_started",
  "updated_at": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cover|string|false|none|封面|
|created_at|integer|false|none|创建时间|
|id|integer|false|none|任务ID|
|input_from|[types.SourceType](#schematypes.sourcetype)|false|none|输入源类型<br>	* camera - 摄像头<br>	* video - 视频|
|input_id|string|false|none|任务输入ID|
|input_type|[types.InputType](#schematypes.inputtype)|false|none|任务输入类型:<br>	* video - 视频<br>	* image - 图片|
|input_url|string|false|none|输入URL|
|instances|[[models.Instance](#schemamodels.instance)]|false|none|实例列表|
|loop|boolean|false|none|循环分析视频，当输入类型为视频且时有效|
|name|string|false|none|任务名称|
|scheduler_type|[types.SchedulerType](#schematypes.schedulertype)|false|none|任务调度类型:<br>	* daemon - 守护任务<br>	* cron - 定时任务|
|status|[models.TaskStatus](#schemamodels.taskstatus)|false|none|任务状态:<br>	* not_started - 未启动<br>	* pending - 启动中<br>	* running - 运行中<br>	* finished - 已完成<br>	* failed - 失败<br>	* stream_error - 流异常<br>	* license_error - 授权异常|
|updated_at|integer|false|none|更新时间|

<h2 id="tocS_models.TaskInfo">models.TaskInfo</h2>
<!-- backwards compatibility -->
<a id="schemamodels.taskinfo"></a>
<a id="schema_models.TaskInfo"></a>
<a id="tocSmodels.taskinfo"></a>
<a id="tocsmodels.taskinfo"></a>

```json
{
  "current_instance_id": "string",
  "id": "string",
  "instances": [
    {
      "app_name": "string",
      "fps": 0,
      "id": "string"
    }
  ],
  "source_name": "string",
  "task_name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|current_instance_id|string|false|none|当前实例ID|
|id|string|false|none|任务ID|
|instances|[[models.MonitorInstance](#schemamodels.monitorinstance)]|false|none|实例ID列表|
|source_name|string|false|none|输入源名称|
|task_name|string|false|none|任务名称|

<h2 id="tocS_models.TaskList">models.TaskList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.tasklist"></a>
<a id="schema_models.TaskList"></a>
<a id="tocSmodels.tasklist"></a>
<a id="tocsmodels.tasklist"></a>

```json
{
  "items": [
    {
      "cover": "string",
      "created_at": 0,
      "id": 0,
      "input_from": "camera",
      "input_id": "string",
      "input_type": "video",
      "input_url": "string",
      "instances": [
        {
          "alarm_effect": {
            "content": "string",
            "duration": "string",
            "enable": true
          },
          "app_config": "string",
          "app_config_url": "string",
          "app_id": 0,
          "app_label": "string",
          "app_module_definitions": "string",
          "app_module_definitions_url": "string",
          "app_name": "string",
          "cronjob": {
            "duration": "string",
            "start_at": "string"
          },
          "fps": 0,
          "has_app_update": true,
          "id": "string",
          "preview_url": "string",
          "reason": "string",
          "report_url": "string",
          "roi_state": "string",
          "selected_feature_lib": {
            "group_ids": [
              0
            ],
            "id": 0
          },
          "sn": "string",
          "st_state": "None",
          "statistics": {
            "limit": 0,
            "usage": 0
          },
          "status": "not_started"
        }
      ],
      "loop": true,
      "name": "string",
      "scheduler_type": "daemon",
      "status": "not_started",
      "updated_at": 0
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.Task](#schemamodels.task)]|false|none|任务列表|
|total|integer|false|none|总数|

<h2 id="tocS_models.TaskMetrics">models.TaskMetrics</h2>
<!-- backwards compatibility -->
<a id="schemamodels.taskmetrics"></a>
<a id="schema_models.TaskMetrics"></a>
<a id="tocSmodels.taskmetrics"></a>
<a id="tocsmodels.taskmetrics"></a>

```json
{
  "failed": 0,
  "finished": 0,
  "not_started": 0,
  "pending": 0,
  "running": 0,
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|failed|integer|false|none|异常数量|
|finished|integer|false|none|已完成数量|
|not_started|integer|false|none|未启动数量|
|pending|integer|false|none|等待中数量|
|running|integer|false|none|运行中数量|
|total|integer|false|none|任务总数|

<h2 id="tocS_models.TaskStatus">models.TaskStatus</h2>
<!-- backwards compatibility -->
<a id="schemamodels.taskstatus"></a>
<a id="schema_models.TaskStatus"></a>
<a id="tocSmodels.taskstatus"></a>
<a id="tocsmodels.taskstatus"></a>

```json
"not_started"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|not_started|
|*anonymous*|pending|
|*anonymous*|running|
|*anonymous*|finished|
|*anonymous*|failed|
|*anonymous*|stream_error|
|*anonymous*|license_error|

<h2 id="tocS_models.TestSubscribeResponse">models.TestSubscribeResponse</h2>
<!-- backwards compatibility -->
<a id="schemamodels.testsubscriberesponse"></a>
<a id="schema_models.TestSubscribeResponse"></a>
<a id="tocSmodels.testsubscriberesponse"></a>
<a id="tocsmodels.testsubscriberesponse"></a>

```json
{
  "message": "string",
  "pass": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|false|none|错误消息提示|
|pass|boolean|false|none|测试是否通过|

<h2 id="tocS_models.UpdateAppReq">models.UpdateAppReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.updateappreq"></a>
<a id="schema_models.UpdateAppReq"></a>
<a id="tocSmodels.updateappreq"></a>
<a id="tocsmodels.updateappreq"></a>

```json
{
  "config": "string",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|config|string|false|none|算法应用配置|
|name|string|false|none|算法应用名称, 不能超过255个字符|

<h2 id="tocS_models.UpdateCameraReq">models.UpdateCameraReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.updatecamerareq"></a>
<a id="schema_models.UpdateCameraReq"></a>
<a id="tocSmodels.updatecamerareq"></a>
<a id="tocsmodels.updatecamerareq"></a>

```json
{
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|摄像机名称|

<h2 id="tocS_models.UpdateEventReflowJobParams">models.UpdateEventReflowJobParams</h2>
<!-- backwards compatibility -->
<a id="schemamodels.updateeventreflowjobparams"></a>
<a id="schema_models.UpdateEventReflowJobParams"></a>
<a id="tocSmodels.updateeventreflowjobparams"></a>
<a id="tocsmodels.updateeventreflowjobparams"></a>

```json
{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 0,
  "limit": 0,
  "name": "string",
  "task_ids": [
    0
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cronjob|[models.Cronjob](#schemamodels.cronjob)|false|none|定时任务|
|days|integer|false|none|服务持续时间,1-7|
|limit|integer|false|none|AppID   *int64   `json:"app_id"`                           // 算法应用ID|
|name|string|false|none|名称, 任务名称，长度1～20|
|task_ids|[integer]|false|none|*-表示全部，任务ID用逗号分隔|

<h2 id="tocS_models.UpdateEventReq">models.UpdateEventReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.updateeventreq"></a>
<a id="schema_models.UpdateEventReq"></a>
<a id="tocSmodels.updateeventreq"></a>
<a id="tocsmodels.updateeventreq"></a>

```json
{
  "status": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|integer|false|none|事件状态：<br>- 0: 未处理<br>- 1: 有效<br>- 2: 误报|

<h2 id="tocS_models.UpdateFeatureItemReq">models.UpdateFeatureItemReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.updatefeatureitemreq"></a>
<a id="schema_models.UpdateFeatureItemReq"></a>
<a id="tocSmodels.updatefeatureitemreq"></a>
<a id="tocsmodels.updatefeatureitemreq"></a>

```json
{
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|名称|

<h2 id="tocS_models.UpdateRawDataReflowJobParams">models.UpdateRawDataReflowJobParams</h2>
<!-- backwards compatibility -->
<a id="schemamodels.updaterawdatareflowjobparams"></a>
<a id="schema_models.UpdateRawDataReflowJobParams"></a>
<a id="tocSmodels.updaterawdatareflowjobparams"></a>
<a id="tocsmodels.updaterawdatareflowjobparams"></a>

```json
{
  "cronjob": {
    "duration": "string",
    "start_at": "string"
  },
  "days": 0,
  "interval": "string",
  "limit": 0,
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cronjob|[models.Cronjob](#schemamodels.cronjob)|false|none|// 输入源ID<br>SourceID *string `json:"source_id"`<br>每天定时任务|
|days|integer|false|none|服务持续天数,1-7|
|interval|string|false|none|抽帧间隔|
|limit|integer|false|none|数据上限，最小100，最大1000|
|name|string|false|none|任务名称，长度1～20|

<h2 id="tocS_models.UpdateSmartTuningJobReq">models.UpdateSmartTuningJobReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.updatesmarttuningjobreq"></a>
<a id="schema_models.UpdateSmartTuningJobReq"></a>
<a id="tocSmodels.updatesmarttuningjobreq"></a>
<a id="tocsmodels.updatesmarttuningjobreq"></a>

```json
{
  "st_action": "Configure"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|st_action|[models.StAction](#schemamodels.staction)|false|none|智能调参操作：<br>* Configure：配置<br>* Start：启动<br>* Apply：应用<br>* Cancel：取消|

<h2 id="tocS_models.UpdateTaskReq">models.UpdateTaskReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.updatetaskreq"></a>
<a id="schema_models.UpdateTaskReq"></a>
<a id="tocSmodels.updatetaskreq"></a>
<a id="tocsmodels.updatetaskreq"></a>

```json
{
  "input_id": "string",
  "instances": [
    {
      "alarm_effect": {
        "content": "string",
        "duration": "string",
        "enable": true
      },
      "app_config": "string",
      "app_id": 0,
      "cronjob": {
        "duration": "string",
        "start_at": "string"
      },
      "selected_feature_lib": {
        "group_ids": [
          0
        ],
        "id": 0
      }
    }
  ],
  "loop": true,
  "name": "string",
  "scheduler_type": "daemon",
  "start": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|input_id|string|false|none|输入源ID|
|instances|[[models.InstanceReq](#schemamodels.instancereq)]|false|none|算法配置|
|loop|boolean|false|none|循环分析视频，当输入类型为视频且时有效|
|name|string|false|none|任务名称|
|scheduler_type|[types.SchedulerType](#schematypes.schedulertype)|false|none|任务调度类型:<br>	* daemon -守护任务<br>	* cron - 定时任务|
|start|boolean|false|none|是否启动|

<h2 id="tocS_models.UpdateVideoReq">models.UpdateVideoReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.updatevideoreq"></a>
<a id="schema_models.UpdateVideoReq"></a>
<a id="tocSmodels.updatevideoreq"></a>
<a id="tocsmodels.updatevideoreq"></a>

```json
{
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|视频名称|

<h2 id="tocS_models.UpgradeTaskReq">models.UpgradeTaskReq</h2>
<!-- backwards compatibility -->
<a id="schemamodels.upgradetaskreq"></a>
<a id="schema_models.UpgradeTaskReq"></a>
<a id="tocSmodels.upgradetaskreq"></a>
<a id="tocsmodels.upgradetaskreq"></a>

```json
{
  "reserve_roi": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reserve_roi|boolean|false|none|保留ROI，含越线检测配置等|

<h2 id="tocS_models.UserInfo">models.UserInfo</h2>
<!-- backwards compatibility -->
<a id="schemamodels.userinfo"></a>
<a id="schema_models.UserInfo"></a>
<a id="tocSmodels.userinfo"></a>
<a id="tocsmodels.userinfo"></a>

```json
{
  "id": 0,
  "menus": [
    "dashboard"
  ],
  "name": "string",
  "role": "admin"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|用户ID|
|menus|[[types.MenuPermission](#schematypes.menupermission)]|false|none|菜单权限, 菜单权限：<br>* dashboard - 首页<br>* input_source - 输入源<br>* task - 任务<br>* image_service - 图像服务<br>* event - 事件<br>* monitor - 监控<br>* app - 应用<br>* feature_lib - 特征库<br>* audit_log - 日志<br>* device_info - 设备信息<br>* system_setting - 系统设置|
|name|string|false|none|用户名|
|role|[types.Role](#schematypes.role)|false|none|角色:<br>* admin - 管理员<br>* user - 普通用户|

<h2 id="tocS_models.Video">models.Video</h2>
<!-- backwards compatibility -->
<a id="schemamodels.video"></a>
<a id="schema_models.Video"></a>
<a id="tocSmodels.video"></a>
<a id="tocsmodels.video"></a>

```json
{
  "cover_url": "string",
  "created_at": 0,
  "duration": 0,
  "fps": 0,
  "id": "string",
  "name": "string",
  "resolution": "string",
  "size": 0,
  "snapshot_url": "string",
  "updated_at": 0,
  "video_url": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|cover_url|string|false|none|封面|
|created_at|integer|false|none|创建时间|
|duration|integer|false|none|视频时长|
|fps|integer|false|none|帧率|
|id|string|false|none|视频ID|
|name|string|false|none|视频名称|
|resolution|string|false|none|分辨率|
|size|integer|false|none|视频大小|
|snapshot_url|string|false|none|截图|
|updated_at|integer|false|none|更新时间|
|video_url|string|false|none|视频地址|

<h2 id="tocS_models.VideoList">models.VideoList</h2>
<!-- backwards compatibility -->
<a id="schemamodels.videolist"></a>
<a id="schema_models.VideoList"></a>
<a id="tocSmodels.videolist"></a>
<a id="tocsmodels.videolist"></a>

```json
{
  "items": [
    {
      "cover_url": "string",
      "created_at": 0,
      "duration": 0,
      "fps": 0,
      "id": "string",
      "name": "string",
      "resolution": "string",
      "size": 0,
      "snapshot_url": "string",
      "updated_at": 0,
      "video_url": "string"
    }
  ],
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[models.Video](#schemamodels.video)]|false|none|视频列表|
|total|integer|false|none|总数|

<h2 id="tocS_types.CameraStatus">types.CameraStatus</h2>
<!-- backwards compatibility -->
<a id="schematypes.camerastatus"></a>
<a id="schema_types.CameraStatus"></a>
<a id="tocStypes.camerastatus"></a>
<a id="tocstypes.camerastatus"></a>

```json
"online"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|online|
|*anonymous*|offline|
|*anonymous*|abnormality|

<h2 id="tocS_types.EventReportType">types.EventReportType</h2>
<!-- backwards compatibility -->
<a id="schematypes.eventreporttype"></a>
<a id="schema_types.EventReportType"></a>
<a id="tocStypes.eventreporttype"></a>
<a id="tocstypes.eventreporttype"></a>

```json
1

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|integer|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|1|
|*anonymous*|2|
|*anonymous*|4|
|*anonymous*|8|

<h2 id="tocS_types.InputType">types.InputType</h2>
<!-- backwards compatibility -->
<a id="schematypes.inputtype"></a>
<a id="schema_types.InputType"></a>
<a id="tocStypes.inputtype"></a>
<a id="tocstypes.inputtype"></a>

```json
"video"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|video|
|*anonymous*|image|

<h2 id="tocS_types.MenuPermission">types.MenuPermission</h2>
<!-- backwards compatibility -->
<a id="schematypes.menupermission"></a>
<a id="schema_types.MenuPermission"></a>
<a id="tocStypes.menupermission"></a>
<a id="tocstypes.menupermission"></a>

```json
"dashboard"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|dashboard|
|*anonymous*|input_source|
|*anonymous*|task|
|*anonymous*|image_service|
|*anonymous*|event|
|*anonymous*|monitor|
|*anonymous*|app|
|*anonymous*|feature_lib|
|*anonymous*|audit_log|
|*anonymous*|device_info|
|*anonymous*|system_setting|
|*anonymous*|reflow|

<h2 id="tocS_types.Role">types.Role</h2>
<!-- backwards compatibility -->
<a id="schematypes.role"></a>
<a id="schema_types.Role"></a>
<a id="tocStypes.role"></a>
<a id="tocstypes.role"></a>

```json
"admin"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|admin|
|*anonymous*|user|

<h2 id="tocS_types.SchedulerType">types.SchedulerType</h2>
<!-- backwards compatibility -->
<a id="schematypes.schedulertype"></a>
<a id="schema_types.SchedulerType"></a>
<a id="tocStypes.schedulertype"></a>
<a id="tocstypes.schedulertype"></a>

```json
"daemon"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|daemon|
|*anonymous*|cron|

<h2 id="tocS_types.SourceType">types.SourceType</h2>
<!-- backwards compatibility -->
<a id="schematypes.sourcetype"></a>
<a id="schema_types.SourceType"></a>
<a id="tocStypes.sourcetype"></a>
<a id="tocstypes.sourcetype"></a>

```json
"camera"

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|camera|
|*anonymous*|video|

