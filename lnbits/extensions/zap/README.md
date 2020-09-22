<h1>Example Extension</h1>
<h2>*tagline*</h2>
This is an example extension to help you organise and build you own.

Try to include an image
<img src="https://i.imgur.com/9i4xcQB.png">


<h2>If your extension has API endpoints, include useful ones here</h2>

<code>curl -H "Content-type: application/json" -X POST https://YOUR-LNBITS/YOUR-EXTENSION/api/v1/EXAMPLE -d '{"amount":"100","memo":"example"}' -H "X-Api-Key: YOUR_WALLET-ADMIN/INVOICE-KEY"</code>


python3 -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/rpc/*.proto
http://localhost:5000/tpos/api/v1/tposs
/extensionname/urls
https://github.com/LN-Zap/lndconnect/blob/master/lnd_connect_uri.md

echo 'lndconnect://192.168.0.15:10009?cert='"`grep -v 'CERTIFICATE' tls.cert | tr -d '=' | tr '/+' '_-'`"'&macaroon='"`base64 admin.macaroon | tr -d '=' | tr '/+' '_-'`" | tr -d '\n' | qrencode -o out.png

generado con xxd -plain admin.macaroon  > hex.maca

fake macaroon
7e687a3f53084333a1d48bb7a922d45f > base64 : N2U2ODdhM2Y1MzA4NDMzM2ExZDQ4YmI3YTkyMmQ0NWY
N2U2ODdhM2Y1MzA4NDMzM2ExZDQ4YmI3YTkyMmQ0NWY
7e687a3f53084333a1d48bb7a922d45f

lndconnect://192.168.0.15:10009?cert=MIICSjCCAfCgAwIBAgIQPDo9yD-nDWaKsnQA4PvbZjAKBggqhkjOPQQDAjBJMR8wHQYDVQQKExZsbmQgYXV0b2dlbmVyYXRlZCBjZXJ0MSYwJAYDVQQDEx1lbWlsaW8tSFAtUHJvQm9vay14MzYwLTQ0MC1HMTAeFw0yMDA5MTgxMDU1MTZaFw0yMTExMTMxMDU1MTZaMEkxHzAdBgNVBAoTFmxuZCBhdXRvZ2VuZXJhdGVkIGNlcnQxJjAkBgNVBAMTHWVtaWxpby1IUC1Qcm9Cb29rLXgzNjAtNDQwLUcxMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEtxaNkRfDUr9pszdrxzeTMOjIQz6OydEB1lZ3E8fVrwMtEu25Hrt9ioOPI23IjEHOajiuOloMtKLj9XpoqW-d2aOBuTCBtjAOBgNVHQ8BAf8EBAMCAqQwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDwYDVR0TAQH_BAUwAwEB_zB-BgNVHREEdzB1gh1lbWlsaW8tSFAtUHJvQm9vay14MzYwLTQ0MC1HMYIJbG9jYWxob3N0ggR1bml4ggp1bml4cGFja2V0ggdidWZjb25uhwR_AAABhxAAAAAAAAAAAAAAAAAAAAABhwTAqAAPhxD-gAAAAAAAANV1fxf71B3tMAoGCCqGSM49BAMCA0gAMEUCIQDdhqmOKEalYP-MNpdRWcwYObSnsVgiF_oVmiOyW7TlOwIgU1uNK59KiQbcPKnU5vfS3EkXP-pQaIyYWH5sqOO9oBw&macaroon=OGMzMjlhYTU5NmRjNDA4MmFhZDA2MzQ4MDQ0ZjhhYzE